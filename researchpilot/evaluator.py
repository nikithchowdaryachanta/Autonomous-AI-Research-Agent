import json
from pathlib import Path

def load_traces(path="sample_data/test_traces.jsonl"):
    return [
        json.loads(line)
        for line in Path(path).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

def keyword_recall(expected_terms, observed_text):
    observed = observed_text.lower()
    hits = sum(
        1 for term in expected_terms
        if term.lower() in observed
    )
    return hits / max(1, len(expected_terms))

def evaluate_result(result, trace):
    text = json.dumps(result).lower()
    expected_terms = trace.get("expected_evidence_terms", [])
    recall = keyword_recall(expected_terms, text)

    returned_urls = {
        source["url"]
        for source in result.get("sources", [])
    }

    expected_urls = set(trace.get("expected_urls", []))

    precision = None
    if expected_urls:
        precision = (
            len(returned_urls & expected_urls)
            / max(1, len(returned_urls))
        )

    return {
        "trace_id": trace["id"],
        "evidence_recall": round(recall, 3),
        "source_precision": precision,
    }
