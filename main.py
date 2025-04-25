"""
Research Agent API

The Research Agent API is a powerful tool designed to perform comprehensive research using Large Language Model (LLM) agents.
This API enables users to conduct systematic web searches, extract data from authoritative sources, analyze recent news coverage, and synthesize findings into well-structured research reports.

The API is built using the FastAPI framework and utilizes the Pydantic library to create comprehensive documentation and enforce data validation.

The API is organized into the following endpoints:

- `/api/research/run`: Run the research agent to investigate the provided query.
- `/api/formater/generate`: Generate formatted text with summary and references from provided content.

The API is designed to be easily extensible and maintainable.  The code is written to be readable and well-commented.
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.research import router
from app.routers import formater

app = FastAPI(
    title="Research Agent API",
    description="API for performing research using LLM agents",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router)
app.include_router(formater.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)