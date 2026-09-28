# Assessment Submission Answers

## GitHub Repo / Code Link

`<PASTE FINAL GITHUB REPOSITORY URL>`

## Upload Code

`ResearchPilot_Gemini_Autonomous_Research_Agent.zip`

## Architecture Diagram

`artifacts/architecture_diagram.png`

## Sample Run Transcripts/Logs

`SAMPLE_RUN_TRANSCRIPT.md`

## Write-up

`WRITEUP.md`

## Which domain/goal did you choose for your agent?

I selected **Autonomous Research**.

The agent accepts a research question, autonomously plans an information-gathering strategy using Google Gemini, generates focused search queries, selects appropriate external source types, gathers information in parallel, removes duplicate and low-relevance results, and generates a structured evidence-grounded research report containing key points, important findings, references, limitations and actionable insights.

## Any assumptions or mock data used?

The system assumes access to public external sources and API credentials supplied through environment variables.

Google Gemini is used for the LLM reasoning stages and Tavily is used for broader web retrieval. Wikipedia is implemented as a secondary source.

No private dataset is required.

The evaluation suite contains synthetic research tasks with labels for intent, source categories and expected evidence themes.

## Total time spent (hours)

`ENTER ACTUAL DEVELOPMENT AND TESTING TIME`

## Synthetic/Test Traces Used

`sample_data/test_traces.jsonl`

Included labels:

- Multi-source technology synthesis
- Technical concept research
- Action-oriented business research
- Comparative research

## Monitoring Report / Dashboard Output

The Streamlit monitoring dashboard records:

- Sources gathered
- Sources retained
- Duplicates removed
- Search queries planned
- References generated
- Execution latency
- Source-type distribution
- Agent execution trace

## Write-up — Approach, Precision/Recall, Production Readiness

See `WRITEUP.md` and `researchpilot/evaluator.py`.

## How did you generate/label your test traces?

Synthetic research tasks were manually designed to cover different research intents.

Each trace was labeled with:

- Research intent
- Expected source categories
- Expected evidence themes
- Research task category

These labels are used to evaluate the agent without hardcoding answers into the production research workflow.
