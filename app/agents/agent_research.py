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

    The research agent is a CodeAgent that uses a LiteLLMModel to generate code based on human instructions.
    It is configured with a web search tool, a web crawler tool, and a news search tool.
    The agent is designed to be used for research and information gathering tasks.

    Args:
        model_name (str): The name of the LLM model to use. For example, "codegen-350M-mono".
        temperature (float): The temperature for the LLM. A higher temperature will result in more
            diverse and unpredictable code generation.
        serper_api_key (str): The API key for Serper.dev services. This is required for the web search,
            web crawler, and news search tools.
        api_key (Optional[str]): The API key for the LLM model. This is only required if the model requires
            an API key.
        max_token (int): The maximum number of tokens that the LLM can generate. This is useful for limiting
            the amount of code that the agent can generate.
        verbosity_level (int): The level of verbosity for the agent. This can be one of the following values:
            * 0: No output
            * 1: Only output the final result
            * 2: Output all intermediate steps and the final result
        max_steps (int): The maximum number of steps that the agent can take. This is useful for limiting
            the amount of time that the agent can spend on a task.

    Returns:
        CodeAgent: A configured research agent
    """
    # Initialize the LLM model
    model = LiteLLMModel(
        model_id=model_name,
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