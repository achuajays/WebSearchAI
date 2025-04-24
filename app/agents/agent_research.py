from smolagents import LiteLLMModel, CodeAgent
from app.tools.web_search_tool import WebSearchTool
from app.tools.web_crawler_tool import WebCrawlerTool
from app.tools.news_search_tool import NewsSearchTool
from typing import List, Optional



def create_research_agent(
        model_name: str,
        temperature: float,
        serper_api_key: str,
        api_key: Optional[str] = None,
        max_token: int = 8000,
        verbosity_level: int = 2,
        max_steps: int = 10
) -> CodeAgent:
    """
    Create a research agent with web search, crawling, and news search capabilities.

    Args:
        model_name (str): The name of the LLM model to use
        temperature (float): The temperature for the LLM
        serper_api_key (str): API key for Serper.dev services
        api_key (Optional[str]): API key for the LLM model (if required)
        max_token (int): Maximum token limit for the LLM
        verbosity_level (int): Level of verbosity for agent (0-2)
        max_steps (int): Maximum number of steps for the agent to take

    Returns:
        CodeAgent: A configured research agent
    """
    # Initialize the LLM model
    model = LiteLLMModel(
        model_name,
        temperature=temperature,
        api_key=api_key,
        max_token=max_token
    )

    # Initialize the tools
    web_search = WebSearchTool(api_key=serper_api_key)
    web_crawler = WebCrawlerTool(api_key=serper_api_key)
    news_search = NewsSearchTool(api_key=serper_api_key)

    # List of additional authorized imports
    additional_imports = [
        'math', 'statistics', 'datetime', 'collections',
        'queue', 'random', 're', 'unicodedata', 'itertools',
        'time', 'stat', 'json'
    ]

    # Create and return the research agent
    return CodeAgent(
        model=model,
        tools=[web_search, web_crawler, news_search],
        name="research_agent",
        verbosity_level=verbosity_level,
        max_steps=max_steps,
        additional_authorized_imports=additional_imports
    )