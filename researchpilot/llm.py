from typing import Type, TypeVar
from google import genai
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class LLMClient:
    """Google Gemini client used for planning and evidence-grounded synthesis."""

    def __init__(self, api_key: str, model: str):
        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured. Add it to your .env file."
            )
        self.model = model
        self.client = genai.Client(api_key=api_key)

    def structured(self, system: str, user: str, schema: Type[T]) -> T:
        response = self.client.models.generate_content(
            model=self.model,
            contents=user,
            config={
                "system_instruction": system,
                "response_mime_type": "application/json",
                "response_schema": schema,
                "temperature": 0.2,
            },
        )
        if not response.parsed:
            raise RuntimeError("Gemini returned no structured response.")
        return response.parsed
