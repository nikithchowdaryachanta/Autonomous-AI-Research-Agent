from researchpilot.sources import rank_and_deduplicate
from researchpilot.models import Source

def test_duplicate_filter():
    sources = [
        Source(
            id="1",
            title="Python data science",
            url="https://a.example/x",
            snippet="python pandas numpy",
        ),
        Source(
            id="2",
            title="Python data science",
            url="https://a.example/x",
            snippet="python pandas numpy",
        ),
        Source(
            id="3",
            title="Unrelated",
            url="https://b.example/y",
            snippet="football weather",
        ),
    ]

    kept, duplicates = rank_and_deduplicate(
        sources,
        "python data science",
        5,
    )

    assert len(kept) == 2
    assert duplicates == 1

def test_max_sources():
    sources = [
        Source(
            id=str(i),
            title=f"Python topic {i}",
            url=f"https://x{i}.example",
            snippet=(
                f"python data science "
                f"marker{i+100} distinct{i+200}"
            ),
        )
        for i in range(10)
    ]

    kept, _ = rank_and_deduplicate(
        sources,
        "python data science",
        4,
    )

    assert len(kept) == 4
