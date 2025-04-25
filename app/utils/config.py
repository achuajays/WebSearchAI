"""
Configuration file for the Web Search AI project.

This file is responsible for loading environment variables from the `.env` file
and making them available to the rest of the application.

Environment Variables:
    GEMINI_API_KEY: The API key for the Gemini LLM model.
    SERPER_API_KEY: The API key for the Serper.dev API.
"""

import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
SERPER_API_KEY: str = os.getenv("SERPER_API_KEY")