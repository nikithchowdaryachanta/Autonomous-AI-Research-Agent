from typing import List, Dict, Any
from pydantic import BaseModel, Field

class ResearchPlan(BaseModel):
    intent: str
    search_queries: List[str] = Field(default_factory=list)
    preferred_source_types: List[str] = Field(default_factory=list)
    reasoning: str = ""

class Source(BaseModel):
    id: str
    title: str
    url: str
    snippet: str = ""
    content: str = ""
    source_type: str = "web"
    relevance_score: float = 0.0
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ResearchReport(BaseModel):
    title: str
    executive_summary: str
    key_points: List[str] = Field(default_factory=list)
    important_findings: List[str] = Field(default_factory=list)
    actionable_insights: List[str] = Field(default_factory=list)
    limitations: List[str] = Field(default_factory=list)
    references: List[str] = Field(default_factory=list)
