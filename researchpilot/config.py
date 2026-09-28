import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    tavily_api_key: str = os.getenv("TAVILY_API_KEY", "")
    tavily_max_results: int = int(os.getenv("TAVILY_MAX_RESULTS", "6"))
    app_db_path: str = os.getenv("APP_DB_PATH", "data/researchpilot.db")
