from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter(
    prefix="/api/formater",
    tags=["research"],
    responses={404: {"description": "Not found"}},
)


class Format(BaseModel):
    Summary: str
    Reference: list[str]


class FormatRequest(BaseModel):
    prompt: str


@router.post("/generate")
async def generate_recipes(request: FormatRequest):
    """Generate formatted text with summary and references from provided content.

    Args:
        request (FormatRequest): Request object containing the prompt to format.

    Returns:
        list[Format]: List of formatted data containing summary and references.

    Raises:
        HTTPException: If an error occurs during content generation, with status code 500
                      and error details.
    """
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents='convert the given content to highly formatted text with the summary and references . - content to format - ' + request.prompt,
            config={
                'response_mime_type': 'application/json',
                'response_schema': Format,
            },
        )
        format_data: list[Format] = response.parsed
        print(format_data)
        return format_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recipes: {str(e)}")