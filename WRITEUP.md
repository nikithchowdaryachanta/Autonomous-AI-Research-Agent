# Assessment Write-up — ResearchPilot

## Assessment Option

**Option 1 — Autonomous Research Agent**

## Domain / Goal

ResearchPilot automates evidence-based research. A user supplies a research question and the agent autonomously plans the research strategy, generates search queries, selects source categories, gathers external information, filters the results, and synthesizes a structured report.

## Design Decisions

### Gemini-based Agent

Google Gemini is used for both reasoning stages:

- Research planning
- Evidence-grounded synthesis

The Gemini model is configurable through `GEMINI_MODEL`.

### Planner/Synthesizer Separation

The system separates planning from synthesis. The planner determines what should be researched, while the synthesizer works only from the retrieved evidence pack.

### Multi-Source Retrieval

Tavily and Wikipedia are implemented as separate source adapters.

### Parallel Retrieval

Independent search operations execute concurrently to reduce latency.

### Relevance and Deduplication

Retrieved sources are ranked using a lightweight relevance score and duplicate/near-duplicate sources are removed before synthesis.

### Evidence Traceability

Every retained source receives a stable source ID. The synthesis stage is instructed to use source IDs when making material findings.

### Memory

SQLite stores previous searches and results, providing persistent search memory without requiring a separate vector database.

### Monitoring

Each run records execution stages and operational metrics.

## Assumptions

- Gemini API credentials are available.
- Tavily API credentials are available for broader web search.
- Internet connectivity is available.
- Test traces are synthetic.
- SQLite is sufficient for the assessment environment.

## Limitations

The prototype uses lightweight relevance and duplicate-detection heuristics. A production system should add semantic reranking, stronger citation verification, source reliability policies, authentication, rate limiting, retries, distributed storage and larger evaluation benchmarks.

## Evaluation

The included evaluator supports evidence-term recall and source precision when expected URLs are available.

These metrics are intended for the supplied test traces and should not be interpreted as universal production accuracy.

## Production Readiness

The system already provides modular retrieval, structured Gemini outputs, concurrent research, source tracking, memory, monitoring and automated tests.

Recommended production improvements include:

- Semantic reranking
- Claim-level citation verification
- Source trust scoring
- Authentication
- Rate limiting
- Retry and circuit-breaker mechanisms
- Distributed storage
- Background processing
- Advanced content filtering
- Larger regression datasets
- Prompt and model version tracking

## Why the Agent Is Autonomous

The system does not contain predefined research answers.

For each new question, Gemini determines the research intent and search strategy. The retrieval layer gathers external information, filtering determines which sources are retained, and Gemini synthesizes the final report from the resulting evidence pack.
