ResearchPilot — Autonomous Research Agent
> **Agentic AI Assessment — Option 1: Autonomous Research Agent**
ResearchPilot is an autonomous, LLM-powered research agent that accepts a natural-language research question, plans an information-gathering strategy, searches external sources, processes and filters retrieved evidence, removes duplicate information, and generates a structured, evidence-grounded research report.
The system uses Google Gemini for autonomous planning and final synthesis, Tavily and Wikipedia for external research, Streamlit for the user interface, and SQLite for persistent search memory.
---
1. Project Objective
ResearchPilot automates the research workflow:
```
Research Question
       ↓
Autonomous Planning
       ↓
Search Strategy
       ↓
External Information Gathering
       ↓
Relevance Filtering
       ↓
Duplicate Removal
       ↓
Evidence Pack
       ↓
Evidence-Grounded Synthesis
       ↓
Structured Research Report
       ↓
Monitoring + Memory + Export

```
The system does not contain predefined answers for research topics. The research strategy and final report are generated dynamically from the user's query and retrieved evidence.
---
2. Assessment Option
This implementation targets:
Option 1 — Autonomous Research Agent
Implemented assessment capabilities:
User query/topic input
External information gathering
Relevant information extraction
Duplicate removal
Relevance filtering
Key point generation
Important finding generation
Reference/source generation
Actionable insights
Autonomous research planning
Dynamic search query generation
Parallel information gathering
Markdown export
PDF export
Persistent search memory
Monitoring
Execution traces
Synthetic test traces
Evaluation utilities
---
3. Core Features
Autonomous LLM Planning
Google Gemini analyzes each research question and dynamically determines:
Research intent
Search queries
Source categories
Research strategy
Multi-Source Research
Current source adapters:
Tavily Web Search
Wikipedia Search
The source layer is modular and can be extended with additional providers.
Parallel Retrieval
Independent search operations are executed concurrently to reduce unnecessary sequential waiting.
Relevance Filtering
Retrieved sources are scored against the original research question.
Duplicate Detection
The system removes:
Duplicate URLs
Highly similar source records
Near-duplicate snippets
Evidence-Grounded Synthesis
Gemini receives the evidence pack and generates the report using only the supplied evidence.
The synthesis stage is instructed to:
Cite source IDs
Avoid fabricated references
Avoid unsupported claims
State insufficient evidence
Distinguish evidence from interpretation
Persistent Memory
Previous searches are stored in SQLite and can be retrieved during subsequent research executions.
Monitoring
Each execution records:
Sources gathered
Sources retained
Duplicates removed
Queries planned
References generated
Latency
Source types
Agent execution stages
Report Export
Reports can be downloaded as:
Markdown
PDF
---
4. Architecture
```
                         ┌──────────────────────┐
                         │      User Query      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Gemini Planner     │
                         │                      │
                         │ Intent               │
                         │ Search Queries       │
                         │ Source Categories    │
                         └──────────┬───────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     │                             │
                     ▼                             ▼
             ┌────────────────┐           ┌────────────────┐
             │ Tavily Search  │           │   Wikipedia    │
             │  Web Research  │           │     Search     │
             └───────┬────────┘           └───────┬────────┘
                     │                            │
                     └─────────────┬──────────────┘
                                   │
                                   ▼
                         ┌──────────────────────┐
                         │ Parallel Retrieval   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Evidence Processing  │
                         │                      │
                         │ Relevance Ranking    │
                         │ Duplicate Removal    │
                         │ Normalization        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Evidence Pack     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Gemini Synthesizer   │
                         │                      │
                         │ Summary              │
                         │ Findings             │
                         │ Insights             │
                         │ Limitations          │
                         │ References            │
                         └──────────┬───────────┘
                                    │
                   ┌────────────────┼────────────────┐
                   │                │                │
                   ▼                ▼                ▼
             ┌───────────┐    ┌───────────┐   ┌────────────┐
             │ Markdown  │    │    PDF    │   │ Monitoring │
             │  Report   │    │  Report   │   │   Trace    │
             └───────────┘    └───────────┘   └────────────┘

                         ┌──────────────────────┐
                         │    SQLite Memory     │
                         │  Previous Searches   │
                         └──────────────────────┘

```
A visual architecture diagram is included at:
```
artifacts/architecture_diagram.png

```
---
5. Technology Stack
Component	Technology
Programming Language	Python 3.10+
LLM	Google Gemini API
Default Gemini Model	`gemini-3.5-flash-lite`
Web Search	Tavily
Secondary Source	Wikipedia
User Interface	Streamlit
Structured Outputs	Pydantic
Memory	SQLite
HTTP Client	Requests
HTML Parsing	BeautifulSoup
PDF Generation	ReportLab
Testing	Pytest
Configuration	python-dotenv
---
6. Project Structure
```
ResearchPilot/
│
├── app.py
├── README.md
├── WRITEUP.md
├── SUBMISSION_FORM_ANSWERS.md
├── SAMPLE_RUN_TRANSCRIPT.md
├── GEMINI_SETUP.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── researchpilot/
│   ├── __init__.py
│   ├── agent.py
│   ├── cli.py
│   ├── config.py
│   ├── evaluator.py
│   ├── llm.py
│   ├── memory.py
│   ├── models.py
│   ├── reporting.py
│   └── sources.py
│
├── tests/
│   └── test_sources.py
│
├── sample_data/
│   └── test_traces.jsonl
│
└── artifacts/
    ├── architecture_diagram.png
    ├── Assessment_Writeup.pdf
    ├── sample_run_transcript.md
    └── RUNBOOK.md

```
---
7. Gemini Configuration
ResearchPilot uses Google Gemini for both LLM reasoning stages:
Autonomous research planning
Evidence-grounded report synthesis
Environment Variables
Create a `.env` file:
```
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash-lite

TAVILY_API_KEY=your_tavily_api_key
TAVILY_MAX_RESULTS=6

APP_DB_PATH=data/researchpilot.db
```
The Gemini API key is loaded from the environment and is never hardcoded in the application.
The Gemini implementation is located at:
```
researchpilot/llm.py

```
---
8. Installation
Prerequisites
Python 3.10+
Google Gemini API key
Tavily API key
Internet connection
Clone
```
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ResearchPilot
```
Create Virtual Environment
Windows
```
python -m venv .venv
.venv\Scripts ctivate
```
Linux/macOS
```
python3 -m venv .venv
source .venv/bin/activate
```
Install Dependencies
```
pip install -r requirements.txt
```
Configure Environment
Create `.env` from `.env.example` and add your API keys.
---
9. Run the Application
```
streamlit run app.py
```
The application provides:
Research query input
Autonomous research execution
Source inspection
Structured research report
Agent execution trace
Monitoring metrics
Markdown download
PDF download
---
10. CLI Usage
ResearchPilot can also run from the command line:
```
python -m researchpilot.cli "What are the main applications of retrieval augmented generation?"
```
Example:
```
python -m researchpilot.cli "How does containerization help software deployment?"
```
---
11. Agent Workflow
Step 1 — Query Reception
The system receives a natural-language research question.
Step 2 — Gemini Planning
Gemini determines the research intent and generates focused search queries and source categories.
Step 3 — External Retrieval
The generated queries are executed against configured external sources.
Step 4 — Parallel Gathering
Independent retrieval operations execute concurrently.
Step 5 — Evidence Processing
Retrieved sources are normalized, scored and filtered.
Step 6 — Deduplication
Duplicate URLs and highly similar source records are removed.
Step 7 — Evidence Pack
Retained sources are assigned stable source IDs.
Step 8 — Gemini Synthesis
Gemini receives the original question, research plan and evidence pack.
Step 9 — Structured Report
The system generates:
Executive Summary
Key Points
Important Findings
Actionable Insights
Limitations
References
Step 10 — Monitoring and Memory
Execution metrics are recorded and the research result is stored in SQLite.
---
12. Evidence Structure
Each retained source has a structured representation:
```
{
  "id": "src-a83f91",
  "title": "Example Source",
  "url": "https://example.com",
  "source_type": "web",
  "relevance_score": 0.82
}
```
Source IDs allow generated findings to be traced back to retrieved evidence.
---
13. Memory
Research history is stored in:
```
data/researchpilot.db

```
Stored information includes:
Query
Result JSON
Timestamp
This provides persistent search memory without requiring an external vector database.
---
14. Monitoring
The Streamlit monitoring dashboard displays:
Metric	Description
Sources Gathered	Total retrieved sources
Sources Retained	Sources remaining after filtering
Duplicates Removed	Duplicate/near-duplicate sources removed
Queries Planned	Queries generated by Gemini
References Generated	References included in the report
Latency	Total execution time
Source-type distribution and the complete execution trace are also displayed.
---
14A. Actual Final Run Monitoring Snapshot
The final documented run used the following research question:
```text
What are the main applications and limitations of retrieval augmented generation?
```
Observed dashboard metrics:
Metric	Actual result
Sources gathered	18
Sources retained	6
Duplicates removed	0
Queries planned	3
References generated	6
Latency	11.56 seconds
Previous-search memory retrieved	1
The Streamlit dashboard also displayed the retrieved source-type distribution and the complete autonomous execution trace.
These are measurements from this specific execution and should not be interpreted as universal production performance guarantees.
---
15. Execution Trace
The following trace is from an actual ResearchPilot execution using the query:
```text
What are the main applications and limitations of retrieval augmented generation?
```
Query Reception
```json
{
  "step": "received_query",
  "query": "What are the main applications and limitations of retrieval augmented generation?"
}
```
Autonomous Research Planning
```json
{
  "step": "planned_research",
  "intent": "To identify and analyze the primary applications and current limitations of Retrieval-Augmented Generation (RAG) in artificial intelligence and natural language processing.",
  "queries": [
    "retrieval augmented generation applications",
    "limitations and challenges of RAG in LLMs",
    "state of the art RAG use cases"
  ],
  "source_types": [
    "academic papers",
    "tech blogs",
    "industry reports",
    "documentation"
  ]
}
```
Memory Retrieval
```json
{
  "step": "memory_retrieved",
  "count": 1
}
```
Parallel Retrieval
```json
{
  "step": "parallel_retrieval",
  "raw_sources": 18
}
```
Evidence Filtering
```json
{
  "step": "filtering",
  "retained": 6,
  "duplicates_removed": 0
}
```
Synthesis Completion
```json
{
  "step": "synthesis_complete",
  "references": 6
}
```
This trace demonstrates that the agent dynamically planned the research, generated multiple search queries, selected source categories, retrieved external evidence, filtered the results, and synthesized a report with references.
---
16. Report Export
The application supports:
Markdown
```
research_report.md

```
PDF
```
research_report.pdf

```
---
17. Testing
Run:
```
pytest -q
```
The test suite validates:
Duplicate URL filtering
Duplicate content filtering
Maximum source retention
Source ranking behavior
The repository includes automated tests covering duplicate URL filtering,
duplicate content filtering, maximum source retention, and source ranking behavior.
The final submission should report the test result produced by the submitted repository/environment.

---
18. Synthetic Test Traces
Located at:
```
sample_data/test_traces.jsonl

```
Included test categories:
ID	Label
TR-001	Multi-source technology synthesis
TR-002	Technical concept research
TR-003	Action-oriented business research
TR-004	Comparative research
Each trace contains:
Query
Intent
Expected source types
Expected evidence terms
Label
---
19. Evaluation
The evaluator is located at:
```
researchpilot/evaluator.py

```
Evidence Recall
```
Evidence Recall =
Expected Evidence Terms Found
/
Total Expected Evidence Terms

```
Source Precision
When expected URLs are available:
```
Source Precision =
Relevant Returned Sources
/
Total Returned Sources

```
These metrics are intended for the included evaluation traces and are not presented as universal production accuracy measurements.
---
20. Test Trace Generation
The synthetic test traces were designed to cover different research intents.
Each trace was labeled using:
Research intent
Expected source categories
Expected evidence themes
Task category
The production agent does not use these labels to generate answers.
---
21. Assumptions
The implementation assumes:
A valid Gemini API key is available.
A Tavily API key is available for broader web research.
Internet access is available during execution.
External providers are operational.
Test traces are synthetic.
SQLite is sufficient for the assessment environment.
---
22. Limitations
External Search Dependency
Research quality depends on the availability and quality of external search providers.
Lightweight Relevance Scoring
The prototype uses textual token overlap for initial relevance scoring.
A production system should use semantic embeddings or a dedicated reranker.
Duplicate Detection
The current implementation combines URL canonicalization and text similarity.
It may not identify every semantically equivalent document.
Citation Verification
Source IDs provide traceability, but a production implementation should add claim-level verification against cited source content.
SQLite Scalability
SQLite is appropriate for a single-user assessment/demo but should be replaced by a scalable datastore for multi-user production deployment.
Dynamic Web Content
External sources can change over time, which can affect reproducibility.
---
23. Production Readiness
Implemented:
Modular agent architecture
Gemini LLM integration
Dynamic research planning
Dynamic search generation
Multi-source retrieval
Parallel retrieval
Relevance filtering
Duplicate detection
Evidence-grounded synthesis
Source traceability
Persistent memory
Monitoring
Execution tracing
Markdown export
PDF export
Automated tests
Synthetic evaluation traces
Recommended production enhancements:
Semantic reranking
Claim-level citation verification
Source trust scoring
Authentication
Rate limiting
Retry/circuit-breaker logic
Distributed storage
Background processing
Advanced content filtering
Large-scale regression benchmarks
Prompt/model version tracking
---
24. Security
API credentials are loaded exclusively through environment variables.
The repository excludes:
```
.env

```
from version control.
Never commit API keys, credentials or secrets to GitHub.
---
25. Assessment Requirement Mapping
Assessment Requirement	Implementation
Accept user query/topic	Streamlit + CLI
Search external sources	Tavily + Wikipedia
Extract relevant information	Source normalization
Remove duplicate content	URL + similarity filtering
Remove irrelevant content	Relevance scoring
Generate key points	Gemini synthesis
Generate important findings	Gemini synthesis
Provide references	Source registry
Generate actionable insights	Gemini synthesis
Autonomous source selection	Gemini planner
Parallel information gathering	Concurrent retrieval
Markdown export	Implemented
PDF export	Implemented
Previous searches in memory	SQLite
Synthetic/test traces	Implemented
Monitoring dashboard	Implemented
Execution logs	Implemented
Evaluation	Implemented
---
26. Example Research Questions
The system supports previously unseen research questions and does not depend on hardcoded responses.
Examples:
```
What are the main applications and limitations of retrieval augmented generation?

```
```
How does containerization help software deployment?

```
```
What factors should a small business consider before adopting cloud computing?

```
```
Compare supervised and unsupervised machine learning.

```
---
26A. Actual Dashboard Evidence
The final submission was validated through the Streamlit dashboard. The captured dashboard evidence includes:
Research report output for the RAG research question
Important findings, actionable insights and limitations
Monitoring metrics and retrieved source-type visualization
Autonomous agent trace showing query reception, planning, memory retrieval, parallel retrieval, filtering and synthesis
The corresponding monitoring report can be included with the submission as supporting execution evidence.
---
27. Submission Artifacts
The project includes:
```
README.md
WRITEUP.md
SUBMISSION_FORM_ANSWERS.md
SAMPLE_RUN_TRANSCRIPT.md
GEMINI_SETUP.md
requirements.txt
.env.example
researchpilot/
tests/
sample_data/
artifacts/

```
The `artifacts` directory contains the architecture diagram, assessment write-up, sample trace and runbook.
---
28. Final Run
Query Used
```text
What are the main applications and limitations of retrieval augmented generation?
```
Runtime Configuration
```text
LLM: Google Gemini
Model: gemini-3.5-flash-lite
Maximum sources: 6
Previous-search memory: enabled
Tavily: configured
```
Observed Execution
```text
Queries planned: 3
Sources gathered: 18
Sources retained: 6
Duplicates removed: 0
References generated: 6
Latency: 11.56 seconds
Previous-search memory retrieved: 1
```
Reproducibility Commands
```bash
# Clone
git clone <YOUR_GITHUB_REPOSITORY_URL>

# Enter project
cd ResearchPilot

# Create environment
python -m venv .venv

# Activate — Windows
.venv\Scripts\activate

# Install
pip install -r requirements.txt

# Configure Gemini and Tavily in .env

# Test
pytest -q

# Run
streamlit run app.py
```
---
29. Project Status
Status: Complete
ResearchPilot includes the complete autonomous research workflow, Google Gemini integration using `gemini-3.5-flash-lite`, external source retrieval, parallel information gathering, relevance filtering, duplicate detection, evidence-grounded synthesis, source references, persistent memory, monitoring, execution tracing, evaluation traces, Markdown/PDF export, automated tests, architecture documentation and assessment documentation.
The final documented run successfully produced a structured RAG research report and recorded 18 gathered sources, 6 retained sources, 0 duplicates removed, 3 planned queries, 6 generated references, 1 previous-search memory result, and 11.56 seconds of observed latency.
---
Author
ResearchPilot — Autonomous Research Agent
Assessment: Agentic AI Assessment
Option: Option 1 — Autonomous Research Agent
LLM: Google Gemini
Implementation: Python + Gemini + Tavily + Wikipedia + Streamlit + SQLite
