# ResearchPilot — Autonomous Research Agent

> **AI Agent Assessment — Option 1: Autonomous Research Agent**

ResearchPilot is an autonomous, LLM-powered research agent designed to collect information from external sources, analyze and synthesize evidence, remove duplicate or low-relevance information, and generate a structured, actionable research report with traceable references.

The system combines autonomous LLM planning, multi-source web research, parallel information gathering, evidence filtering, source tracking, persistent memory, monitoring, and Markdown/PDF report generation.

---

## Overview

ResearchPilot transforms a natural-language research question into a complete research workflow:

```text
User Query
    │
    ▼
┌──────────────────────────┐
│    LLM Research Planner  │
│                          │
│ • Understands intent     │
│ • Generates queries      │
│ • Selects source types   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  Parallel Source Search  │
│                          │
│ • Tavily Web Search      │
│ • Wikipedia              │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Evidence Processing      │
│                          │
│ • Normalization          │
│ • Relevance scoring      │
│ • Duplicate removal      │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    Evidence Pack         │
│                          │
│ • Source IDs             │
│ • URLs                   │
│ • Source content        │
│ • Relevance scores       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    LLM Synthesizer       │
│                          │
│ • Key points             │
│ • Findings               │
│ • Insights               │
│ • Limitations            │
│ • References             │
└────────────┬─────────────┘
             │
             ├───────────────┐
             ▼               ▼
       Markdown/PDF      Monitoring
          Report            & Trace
             │
             ▼
       SQLite Memory
```

---

## Key Capabilities

### Autonomous Research Planning

The agent uses an LLM to determine:

* Research intent
* Required information
* Search queries
* Appropriate source categories
* Research strategy

Search queries are generated dynamically from the user's question rather than being hardcoded.

### Multi-Source Information Gathering

ResearchPilot currently supports:

* Tavily Web Search
* Wikipedia

The retrieval architecture is provider-based, allowing additional external sources to be integrated without modifying the core agent workflow.

### Parallel Retrieval

Independent searches are executed concurrently to reduce research latency and allow information to be gathered from multiple sources.

### Relevance Filtering

Retrieved sources are evaluated against the original research query and assigned a relevance score.

### Duplicate Detection

The system removes:

* Duplicate URLs
* Duplicate source records
* Highly similar source snippets

This prevents repeated information from unnecessarily influencing the synthesis stage.

### Evidence-Grounded Synthesis

The synthesis stage receives the collected evidence rather than an unrestricted request to answer the question.

The model is instructed to:

* Use only the supplied evidence
* Reference source IDs for material findings
* Avoid fabricated sources
* Avoid unsupported claims
* Identify insufficient evidence
* Distinguish findings from interpretation

### Structured Reports

Each research execution produces:

* Executive Summary
* Key Points
* Important Findings
* Actionable Insights
* Limitations
* References

### Persistent Memory

Previous research executions are stored in SQLite.

Stored information includes:

* Research query
* Generated result
* Timestamp

This allows previous searches to be retrieved during future research sessions.

### Monitoring and Execution Tracing

The system records execution information including:

* Number of sources gathered
* Number of sources retained
* Number of duplicates removed
* Number of queries planned
* Number of references generated
* Execution latency
* Source types
* Agent execution steps

### Report Export

Research reports can be exported as:

* Markdown
* PDF

---

# Architecture

```text
                         ┌─────────────────────┐
                         │      User Query     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   LLM Research     │
                         │       Planner      │
                         ├─────────────────────┤
                         │ • Intent            │
                         │ • Search Queries    │
                         │ • Source Selection  │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
          ┌─────────────────┐             ┌─────────────────┐
          │  Tavily Search  │             │    Wikipedia    │
          │  External Web   │             │    Search API   │
          └────────┬────────┘             └────────┬────────┘
                   │                               │
                   └───────────────┬───────────────┘
                                   │
                                   ▼
                         ┌─────────────────────┐
                         │ Parallel Retrieval  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Evidence Processing │
                         ├─────────────────────┤
                         │ Relevance Ranking   │
                         │ Duplicate Removal   │
                         │ Normalization       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Evidence Pack    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   LLM Synthesizer   │
                         ├─────────────────────┤
                         │ Key Points          │
                         │ Findings            │
                         │ Insights            │
                         │ Limitations         │
                         │ References          │
                         └──────────┬──────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
          ┌─────────────┐   ┌─────────────┐  ┌─────────────┐
          │  Markdown   │   │     PDF     │  │ Monitoring  │
          │   Report    │   │    Report   │  │    Trace    │
          └─────────────┘   └─────────────┘  └─────────────┘

                         ┌─────────────────────┐
                         │    SQLite Memory    │
                         │  Previous Searches  │
                         └─────────────────────┘
```

A visual architecture diagram is included in:

```text
artifacts/architecture_diagram.png
```

---

# Technology Stack

| Layer              | Technology    |
| ------------------ | ------------- |
| Language           | Python 3.10+  |
| LLM                | OpenAI API    |
| Web Research       | Tavily        |
| Secondary Source   | Wikipedia     |
| UI                 | Streamlit     |
| Data Validation    | Pydantic      |
| Memory             | SQLite        |
| HTTP Client        | Requests      |
| Content Extraction | BeautifulSoup |
| PDF Generation     | ReportLab     |
| Testing            | Pytest        |
| Configuration      | python-dotenv |

---

# Project Structure

```text
ResearchPilot/
│
├── app.py
├── README.md
├── WRITEUP.md
├── SUBMISSION_FORM_ANSWERS.md
├── SAMPLE_RUN_TRANSCRIPT.md
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
    ├── RUNBOOK.md
    └── assessment_source.docx
```

---

# Installation

## Prerequisites

* Python 3.10 or later
* OpenAI API key
* Tavily API key
* Internet connection

---

## Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ResearchPilot
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Configuration

Create a `.env` file using `.env.example` as the template.

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5-mini

TAVILY_API_KEY=your_tavily_api_key
TAVILY_MAX_RESULTS=6

APP_DB_PATH=data/researchpilot.db
```

### Security

API keys are never stored in the source code.

The `.gitignore` configuration excludes:

```text
.env
```

Do not commit API credentials or other secrets to the repository.

---

# Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application provides:

* Research query input
* Autonomous research execution
* Source information
* Research report
* Execution trace
* Monitoring metrics
* Markdown download
* PDF download

---

# CLI Usage

ResearchPilot can also be executed from the command line.

```bash
python -m researchpilot.cli "What are the main applications of retrieval augmented generation?"
```

Example:

```bash
python -m researchpilot.cli "How does containerization help software deployment?"
```

---

# Agent Workflow

## 1. Query Reception

The system receives a natural-language research question.

Example:

```text
What are the main applications and limitations of retrieval augmented generation?
```

---

## 2. Autonomous Planning

The LLM analyzes the question and creates a structured research plan containing:

```text
Intent
Search Queries
Preferred Source Types
Planning Reasoning
```

The search queries are generated dynamically.

---

## 3. Source Retrieval

The generated queries are submitted to available external source providers.

Current providers:

```text
Tavily
Wikipedia
```

---

## 4. Parallel Information Gathering

Independent search operations are executed concurrently using a thread pool.

This enables multiple research paths to execute without waiting for each other sequentially.

---

## 5. Relevance Scoring

Each retrieved source is evaluated against the original query.

A relevance score is generated based on textual overlap between the research question and retrieved source information.

---

## 6. Deduplication

Duplicate URLs and highly similar source content are removed.

The agent therefore works with a cleaner evidence set before synthesis.

---

## 7. Evidence Pack Creation

Each retained source receives a unique source identifier.

Example:

```json
{
  "id": "src-a83f91",
  "title": "Example Source",
  "url": "https://example.com",
  "source_type": "web",
  "relevance_score": 0.82
}
```

---

## 8. Evidence-Grounded Synthesis

The final LLM receives:

* Original research question
* Research plan
* Retrieved evidence

The synthesis component generates the final structured report.

Material claims are expected to reference source IDs.

---

## 9. Report Generation

The final report contains:

```text
Executive Summary
Key Points
Important Findings
Actionable Insights
Limitations
References
```

---

## 10. Memory and Monitoring

The research execution is stored in SQLite and an execution trace is generated for monitoring and evaluation.

---

# Memory System

ResearchPilot uses SQLite for persistent research memory.

Database:

```text
data/researchpilot.db
```

Stored fields:

```text
Query
Result JSON
Timestamp
```

The agent can retrieve recent searches during future executions.

This provides lightweight long-term memory without requiring an external vector database.

---

# Monitoring

The application includes a monitoring dashboard displaying:

| Metric               | Description                              |
| -------------------- | ---------------------------------------- |
| Sources Gathered     | Total retrieved sources                  |
| Sources Retained     | Sources remaining after filtering        |
| Duplicates Removed   | Duplicate/near-duplicate sources removed |
| Queries Planned      | Number of search queries generated       |
| References Generated | References included in final report      |
| Latency              | Total research execution time            |

The dashboard also displays source-type distribution and the complete agent execution trace.

---

# Execution Trace

ResearchPilot records the major stages of each execution.

Example:

```json
{
  "step": "received_query",
  "query": "What are the main applications of RAG?"
}
```

```json
{
  "step": "planned_research",
  "intent": "technology research",
  "queries": [
    "RAG applications",
    "RAG use cases"
  ],
  "source_types": [
    "web",
    "encyclopedic"
  ]
}
```

```json
{
  "step": "parallel_retrieval",
  "raw_sources": 8
}
```

```json
{
  "step": "filtering",
  "retained": 6,
  "duplicates_removed": 2
}
```

```json
{
  "step": "synthesis_complete",
  "references": 6
}
```

---

# Report Export

Research results can be exported in two formats.

## Markdown

```text
research_report.md
```

## PDF

```text
research_report.pdf
```

The PDF contains the structured report and source registry.

---

# Testing

The project includes automated unit tests.

Run:

```bash
pytest -q
```

Current test coverage includes:

* Duplicate URL detection
* Duplicate content filtering
* Maximum source retention
* Source ranking behavior

Expected result:

```text
2 passed
```

---

# Synthetic Test Traces

The evaluation dataset is located at:

```text
sample_data/test_traces.jsonl
```

The test suite contains labeled research scenarios covering:

| ID     | Scenario                          |
| ------ | --------------------------------- |
| TR-001 | Multi-source technology synthesis |
| TR-002 | Technical concept research        |
| TR-003 | Action-oriented business research |
| TR-004 | Comparative research              |

Each trace contains:

```text
Query
Intent
Expected Source Types
Expected Evidence Terms
Label
```

---

# Evaluation Methodology

The project includes:

```text
researchpilot/evaluator.py
```

Two evaluation metrics are supported.

## Evidence Recall

Measures the proportion of expected evidence themes represented in the generated result.

```text
Evidence Recall =
Expected Evidence Terms Found
/
Total Expected Evidence Terms
```

## Source Precision

When expected source URLs are available:

```text
Source Precision =
Relevant Returned Sources
/
Total Returned Sources
```

These metrics are intended for evaluation of the supplied test traces and are not presented as universal production accuracy measurements.

---

# Test Trace Generation and Labeling

The test traces were created as synthetic research tasks representing different research intents.

Each trace was manually labeled with:

* Research intent
* Expected source categories
* Expected evidence themes
* Task type

This provides a repeatable evaluation framework while avoiding hardcoded answers in the research agent itself.

---

# Sample Run

A sample execution trace is included in:

```text
SAMPLE_RUN_TRANSCRIPT.md
```

The sample demonstrates the expected agent execution sequence:

```text
Query
  ↓
Research Planning
  ↓
Search Strategy
  ↓
Parallel Retrieval
  ↓
Filtering
  ↓
Evidence Pack
  ↓
Synthesis
  ↓
Final Report
```

---

# Design Decisions

## Planner and Synthesizer Separation

The system separates research planning from final synthesis.

This provides:

* Better observability
* Clearer agent stages
* Easier testing
* Better control over evidence usage

---

## Provider Abstraction

External search providers are separated from the core agent.

This allows additional providers to be added without changing the main research workflow.

---

## Parallel Retrieval

Concurrent retrieval reduces latency when multiple search queries or providers are required.

---

## Deterministic Filtering

The system uses deterministic filtering as a guardrail around the LLM.

This helps reduce:

* Duplicate sources
* Low-value results
* Repeated evidence

---

## Source Traceability

Every retained source receives a source ID.

The source ID can then be referenced by the synthesis model.

This creates a connection between generated findings and retrieved evidence.

---

## Structured LLM Outputs

Pydantic models are used for:

* Research plans
* Sources
* Final reports

This reduces the risk of malformed responses and provides predictable data structures.

---

# Assumptions

The implementation assumes:

1. A valid OpenAI API key is available.
2. A valid Tavily API key is available for web search.
3. Internet access is available during execution.
4. External source providers are operational.
5. Test traces are synthetic.
6. SQLite is sufficient for the assessment environment.

---

# Limitations

### External Search Dependency

The quality and coverage of research depend partly on external search providers.

### Relevance Model

The current relevance scoring mechanism is intentionally lightweight and uses token overlap.

A production implementation should use semantic embeddings or a dedicated reranking model.

### Duplicate Detection

The current system combines URL canonicalization and text similarity.

It may not detect every semantically equivalent source.

### Citation Verification

The system tracks source IDs and instructs the LLM to cite them.

A production implementation should additionally verify every generated claim against the cited source.

### Memory Scalability

SQLite is appropriate for the current single-user application but should be replaced with a scalable database for multi-user deployment.

### Dynamic Web Content

External websites can change or become unavailable, which can affect reproducibility of live research results.

---

# Production Readiness

The current implementation provides the core architecture required for an autonomous research prototype.

Implemented:

* Modular agent architecture
* LLM-based planning
* Dynamic search generation
* Multi-source retrieval
* Parallel retrieval
* Relevance filtering
* Duplicate detection
* Evidence-grounded synthesis
* Source traceability
* Persistent memory
* Monitoring
* Execution tracing
* Markdown export
* PDF export
* Automated testing
* Evaluation traces

Recommended production enhancements:

```text
Authentication
Rate Limiting
Retry / Circuit Breakers
Semantic Reranking
Claim-Level Citation Verification
Source Trust Scoring
Distributed Database
Background Job Queue
Distributed Tracing
Advanced Content Filtering
Large-Scale Evaluation Benchmark
Prompt / Model Version Tracking
```

---

# Security

The application follows an environment-variable-based secret management approach.

Sensitive configuration is not embedded in source code.

Before publishing the project:

```bash
git status
```

should be checked to ensure `.env` and other secrets are not included.

---

# Assessment Requirement Mapping

| Requirement                    | Implementation             |
| ------------------------------ | -------------------------- |
| Accept user query/topic        | Streamlit UI + CLI         |
| Search external sources        | Tavily + Wikipedia         |
| Extract relevant information   | Source normalization       |
| Remove duplicate information   | URL + similarity filtering |
| Remove irrelevant information  | Relevance scoring          |
| Generate key points            | LLM synthesis              |
| Generate important findings    | LLM synthesis              |
| Provide references             | Source registry            |
| Generate actionable insights   | LLM synthesis              |
| Autonomous source selection    | LLM planner                |
| Parallel information gathering | Concurrent retrieval       |
| Markdown export                | Implemented                |
| PDF export                     | Implemented                |
| Previous search memory         | SQLite                     |
| Synthetic test traces          | Implemented                |
| Monitoring dashboard           | Implemented                |
| Execution logs                 | Implemented                |
| Evaluation                     | Implemented                |

---

# Running the Complete System

```bash
# 1. Clone
git clone <YOUR_GITHUB_REPOSITORY_URL>

# 2. Enter project
cd ResearchPilot

# 3. Create environment
python -m venv .venv

# 4. Activate — Windows
.venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Configure environment
# Create .env and add API keys

# 7. Run tests
pytest -q

# 8. Start application
streamlit run app.py
```

---

# Example Research Questions

The agent can process different research topics without requiring predefined answers.

Examples:

```text
What are the main applications and limitations of retrieval augmented generation?
```

```text
How does containerization improve software deployment?
```

```text
What factors should a small business consider before adopting cloud computing?
```

```text
Compare supervised and unsupervised machine learning.
```

The system can also accept previously unseen research questions.

---

# Submission Artifacts

The repository includes the required assessment materials:

```text
README.md
WRITEUP.md
SUBMISSION_FORM_ANSWERS.md
SAMPLE_RUN_TRANSCRIPT.md
architecture_diagram.png
Assessment_Writeup.pdf
sample_data/test_traces.jsonl
tests/test_sources.py
```

---

# Project Status

**Status: Complete**

The ResearchPilot implementation includes the autonomous research workflow, external information gathering, parallel retrieval, relevance filtering, duplicate detection, evidence-grounded synthesis, source references, memory, monitoring, test traces, evaluation, Markdown/PDF export, automated tests, architecture documentation, and assessment write-up.

---

