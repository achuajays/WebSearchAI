"""
Formatter Router

This module provides an API endpoint for generating formatted text with summary and references.
It utilizes the LLM capabilities to process the input prompt and return a structured response.

The router is defined with a prefix and tags for better organization within the FastAPI application.
It includes a single POST endpoint that accepts a request body containing the content to format.

Environment variables are loaded using dotenv for configuration purposes.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
from app.models.scheema import FormatRequest, Format
from app.utils import config
import os

# Load environment variables from a .env file
load_dotenv()

# Initialize the API router with prefix and tags
router = APIRouter(
    prefix="/api/formater",
    tags=["research"],
    responses={404: {"description": "Not found"}},
)

@router.post("/generate")
async def generate_recipes(request: FormatRequest):
    """
    Generate formatted text with summary and references from provided content.

    This endpoint processes the input content, generates a summary, and provides references
    using the LLM model. It returns a list of formatted data objects.

    Args:
        request (FormatRequest): Request object containing the prompt to format.

    Returns:
        list[Format]: List of formatted data containing summary and references.
    """
    # [Function logic goes here]
    pass


from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
from app.models.scheema import FormatRequest, Format
from app.utils import config
import os

load_dotenv()

router = APIRouter(
    prefix="/api/formater",
    tags=["research"],
    responses={404: {"description": "Not found"}},
)





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
        client = genai.Client(api_key=config.GEMINI_API_KEY)
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