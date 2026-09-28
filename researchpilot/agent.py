import json
import time
from .config import Settings
from .llm import LLMClient
from .models import ResearchPlan, ResearchReport
from .sources import (
    TavilySource,
    WikipediaSource,
    retrieve_parallel,
    rank_and_deduplicate,
)
from .memory import MemoryStore

PLANNER_SYSTEM = """
You are the planning component of an autonomous research agent.

Given a user's research question, determine:
1. The research intent.
2. Several focused search queries.
3. Appropriate external source categories.
4. A concise explanation of the research strategy.

Do not answer the research question. Return only the structured research plan.
"""

SYNTHESIS_SYSTEM = """
You are the synthesis component of an autonomous research agent.

Use ONLY the supplied evidence pack to create the research report.

Requirements:
- Ground material findings in supplied evidence.
- Cite source IDs such as [src-abc123].
- Never invent URLs, statistics, studies, quotes, or references.
- Clearly identify uncertainty or insufficient evidence.
- Distinguish evidence-supported findings from interpretation.
- Provide actionable insights only when supported by the evidence.
"""

class ResearchAgent:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.llm = LLMClient(
            settings.gemini_api_key,
            settings.gemini_model,
        )
        self.tavily = TavilySource(
            settings.tavily_api_key,
            settings.tavily_max_results,
        )
        self.wikipedia = WikipediaSource()
        self.memory = MemoryStore(settings.app_db_path)

    def run(self, query, max_sources=6, use_memory=True):
        started = time.perf_counter()
        trace = [{"step": "received_query", "query": query}]

        plan = self.llm.structured(
            PLANNER_SYSTEM,
            f"Research question: {query}",
            ResearchPlan,
        )

        trace.append({
            "step": "planned_research",
            "intent": plan.intent,
            "queries": plan.search_queries,
            "source_types": plan.preferred_source_types,
            "reasoning": plan.reasoning,
        })

        if use_memory:
            previous = self.memory.recent(3)
            if previous:
                trace.append({
                    "step": "memory_retrieved",
                    "count": len(previous),
                })

        raw_sources = retrieve_parallel(
            plan.search_queries,
            self.tavily,
            self.wikipedia,
        )

        trace.append({
            "step": "parallel_retrieval",
            "raw_sources": len(raw_sources),
        })

        sources, duplicates = rank_and_deduplicate(
            raw_sources,
            query,
            max_sources,
        )

        trace.append({
            "step": "filtering",
            "retained": len(sources),
            "duplicates_removed": duplicates,
        })

        evidence = [
            {
                "id": source.id,
                "title": source.title,
                "url": source.url,
                "source_type": source.source_type,
                "relevance_score": source.relevance_score,
                "content": (source.content or source.snippet)[:5000],
            }
            for source in sources
        ]

        report = self.llm.structured(
            SYNTHESIS_SYSTEM,
            json.dumps(
                {
                    "question": query,
                    "research_plan": plan.model_dump(),
                    "evidence": evidence,
                },
                ensure_ascii=False,
            ),
            ResearchReport,
        )

        report_data = report.model_dump()

        trace.append({
            "step": "synthesis_complete",
            "references": len(report.references),
        })

        latency = time.perf_counter() - started

        metrics = {
            "sources_gathered": len(raw_sources),
            "sources_retained": len(sources),
            "duplicates_removed": duplicates,
            "latency_seconds": round(latency, 3),
            "queries_planned": len(plan.search_queries),
            "references_generated": len(report.references),
        }

        result = {
            "query": query,
            "plan": plan.model_dump(),
            "sources": [source.model_dump() for source in sources],
            "report": {
                "data": report_data,
                "markdown": markdown_from_report(report_data),
            },
            "trace": trace,
            "metrics": metrics,
        }

        if use_memory:
            self.memory.save(query, result)

        return result

def markdown_from_report(report):
    lines = [
        f"# {report['title']}",
        "",
        "## Executive Summary",
        report["executive_summary"],
        "",
    ]

    sections = [
        ("Key Points", "key_points"),
        ("Important Findings", "important_findings"),
        ("Actionable Insights", "actionable_insights"),
        ("Limitations", "limitations"),
        ("References", "references"),
    ]

    for heading, key in sections:
        lines.append(f"## {heading}")
        for item in report.get(key, []):
            lines.append(f"- {item}")
        lines.append("")

    return "\n".join(lines)
