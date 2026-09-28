# Gemini API Setup

ResearchPilot uses Google Gemini for both LLM stages:

1. Autonomous research planning
2. Evidence-grounded report synthesis

## Environment

Create `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-2.5-flash

TAVILY_API_KEY=your_tavily_api_key
TAVILY_MAX_RESULTS=6

APP_DB_PATH=data/researchpilot.db
```

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

The Gemini implementation is located in:

```text
researchpilot/llm.py
```

API credentials are loaded from environment variables and are never hardcoded.
