import concurrent.futures
import hashlib
import re
from typing import List
import requests
from bs4 import BeautifulSoup
from .models import Source

class TavilySource:
    def __init__(self, api_key: str, max_results: int = 6):
        self.api_key = api_key
        self.max_results = max_results

    def search(self, query: str) -> List[Source]:
        if not self.api_key:
            return []
        response = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": self.api_key,
                "query": query,
                "search_depth": "advanced",
                "max_results": self.max_results,
                "include_answer": False,
            },
            timeout=30,
        )
        response.raise_for_status()
        sources = []
        for item in response.json().get("results", []):
            url = item["url"]
            sources.append(Source(
                id="src-" + hashlib.sha1(url.encode()).hexdigest()[:10],
                title=item.get("title", url),
                url=url,
                snippet=item.get("content", "")[:1800],
                content=item.get("content", ""),
                source_type="web",
                metadata={"provider": "tavily"},
            ))
        return sources

class WikipediaSource:
    def search(self, query: str) -> List[Source]:
        response = requests.get(
            "https://en.wikipedia.org/w/api.php",
            params={
                "action": "query",
                "list": "search",
                "srsearch": query,
                "format": "json",
                "srlimit": 5,
            },
            timeout=20,
        )
        response.raise_for_status()
        results = response.json().get("query", {}).get("search", [])
        sources = []
        for item in results:
            title = item["title"]
            url = "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")
            snippet = BeautifulSoup(
                item.get("snippet", ""), "html.parser"
            ).get_text(" ")
            sources.append(Source(
                id="wiki-" + hashlib.sha1(url.encode()).hexdigest()[:10],
                title=title,
                url=url,
                snippet=snippet,
                content=snippet,
                source_type="encyclopedic",
                metadata={"provider": "wikipedia"},
            ))
        return sources

def retrieve_parallel(queries, tavily, wikipedia):
    jobs = []
    for query in queries:
        if tavily.api_key:
            jobs.append(tavily.search)
        jobs.append(wikipedia.search)

    results = []
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=min(8, max(1, len(jobs)))
    ) as executor:
        futures = []
        index = 0
        for query in queries:
            if tavily.api_key:
                futures.append(executor.submit(tavily.search, query))
            futures.append(executor.submit(wikipedia.search, query))

        for future in futures:
            try:
                results.extend(future.result())
            except Exception:
                continue

    return results

def tokenize(text):
    return set(re.findall(r"[a-zA-Z0-9]{3,}", text.lower()))

def rank_and_deduplicate(sources, query, max_sources):
    query_tokens = tokenize(query)
    scored = []

    for source in sources:
        source_tokens = tokenize(
            (source.title + " " + source.snippet + " " + source.content)[:8000]
        )
        overlap = len(query_tokens & source_tokens) / max(1, len(query_tokens))
        source.relevance_score = round(min(1.0, overlap), 3)
        scored.append(source)

    scored.sort(key=lambda item: item.relevance_score, reverse=True)

    kept = []
    duplicates = 0
    seen_urls = set()
    seen_signatures = []

    for source in scored:
        canonical_url = source.url.lower().rstrip("/")

        if canonical_url in seen_urls:
            duplicates += 1
            continue

        signature = tokenize(source.title + " " + source.snippet)
        is_duplicate = any(
            len(signature & old) / max(1, len(signature | old)) >= 0.78
            for old in seen_signatures
        )

        if is_duplicate:
            duplicates += 1
            continue

        seen_urls.add(canonical_url)
        seen_signatures.append(signature)
        kept.append(source)

        if len(kept) >= max_sources:
            break

    return kept, duplicates
