from google import genai
from google.genai import types

from django.conf import settings

from .prompts import SYSTEM_PROMPT
from .schemas import ExtractionResponse


client = genai.Client(
    api_key=settings.GEMINI_API_KEY,
)


class TransactionExtractionService:

    def extract_transactions(
        self,
        *,
        raw_text: str,
    ) -> ExtractionResponse:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=raw_text,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                response_mime_type="application/json",
                response_schema=ExtractionResponse,
                temperature=0,
            ),
        )

        return response.parsed


transaction_extraction_service = (
    TransactionExtractionService()
)