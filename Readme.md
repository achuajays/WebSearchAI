# Research Agent API

## Overview

The Research Agent API is a powerful tool designed to perform comprehensive research using Large Language Model (LLM) agents. This API enables users to conduct systematic web searches, extract data from authoritative sources, analyze recent news coverage, and synthesize findings into well-structured research reports.

## Features

- **Web Search**: Conduct systematic web searches to identify authoritative sources.
- **Data Extraction**: Extract primary content from URLs via web crawling.
- **News Analysis**: Extract and analyze recent news coverage.
- **Synthesis and Analysis**: Organize findings into coherent thematic sections and provide in-depth analysis.

## Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (optional but recommended)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/achuajays/WebSearchAI.git
    cd WebSearchAI
    ```

2. **Create a virtual environment** (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following variables:
    ```env
    SERPER_API_KEY=your_serper_api_key
    GEMINI_API_KEY=your_gemini_api_key
    ```

### Running the API

To run the API, execute the following command:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Research Endpoint

- **Endpoint**: `/api/research/run`
- **Method**: `POST`
- **Description**: Run the research agent to investigate the provided query.
- **Request Body**:
    ```json
    {
        "query": "your research question or topic"
    }
    ```
- **Response**:
    ```json
    {
        "research_data": "Compiled research findings",
        "resource_links": ["Link to source 1", "Link to source 2"]
    }
    ```

### Formatter Endpoint

- **Endpoint**: `/api/formater/generate`
- **Method**: `POST`
- **Description**: Generate formatted text with summary and references from provided content.
- **Request Body**:
    ```json
    {
        "prompt": "Content to format"
    }
    ```
- **Response**:
    ```json
    [
        {
            "Summary": "Formatted summary",
            "Reference": ["Reference 1", "Reference 2"]
        }
    ]
    ```

## Project Structure

```
research-agent-api/
│
├── app/
│   ├── __init__.py
│   ├── agents/
│   │   ├── __init__.py
│   │   └── agent_research.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── scheema.py
│   ├── prompts/
│   │   ├── __init__.py
│   │   └── agent_prompt.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── formater.py
│   │   └── research.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── agent_service.py
│   └── tools/
│       ├── __init__.py
│       ├── news_search_tool.py
│       ├── web_crawler_tool.py
│       └── web_search_tool.py
│
├── tests/
│   └── test_research_agent.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Detailed Documentation

### `main.py`

The entry point of the application. It sets up the FastAPI app, includes routers, and adds CORS middleware.

### `requirements.txt`

List of dependencies required to run the application.

### `app/agents/agent_research.py`

Defines the research agent with web search, crawling, and news search capabilities.

### `app/models/scheema.py`

Defines the request and response models for the research agent.

### `app/prompts/agent_prompt.py`

Generates comprehensive research prompts for LLM agents.

### `app/routers/formater.py`

Defines the endpoint for generating formatted text with summary and references.

### `app/routers/research.py`

Defines the endpoint for running the research agent.

### `app/services/agent_service.py`

Defines the service for running the research agent.

### `app/tools/news_search_tool.py`

Defines the tool for searching news articles using the Serper.dev API.

### `app/tools/web_crawler_tool.py`

Defines the tool for crawling and extracting content from web pages using the Serper.dev API.

### `app/tools/web_search_tool.py`

Defines the tool for performing web searches using the Serper.dev API.


### `app/utils/config.py`

Defines the configuration for the application.

### `tests/test_research_agent.py`

Unit tests for the research agent API.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.
