from smolagents import Tool
import requests
import json
import logging

logger = logging.getLogger(__name__)


class NewsSearchTool(Tool):
    """
        Tool for searching news articles using the Serper.dev API.

        This tool enables LLM agents to search for recent news articles based on a query.
        It interacts with the Serper.dev API to fetch relevant news content and returns
        the results as a structured JSON string.

        Attributes:
            name (str): The name identifier for the tool.
            description (str): Human-readable description of the tool's functionality.
            inputs (dict): Schema defining the expected input parameters.
            output_type (str): The type of output returned by the tool.
            api_key (str): API key for authenticating with Serper.dev.
            url (str): Endpoint URL for the Serper.dev news API.
            headers (dict): HTTP headers for API requests.
        """
    name = "news_search"
    description = "Fetches news articles using the Serper.dev API based on a search query."

    inputs = {
        "query": {
            "type": "string",
            "description": "The search query for news articles (e.g., 'software developer')."
        }
    }

    output_type = "string"

    def __init__(self, api_key: str, **kwargs):
        """
                Initialize the NewsSearchTool with API credentials.

                Args:
                    api_key (str): The API key for authenticating with Serper.dev API.
                    **kwargs: Additional keyword arguments passed to the parent Tool class.
        """
        super().__init__(**kwargs)
        self.api_key = api_key
        self.url = "https://google.serper.dev/news"
        self.headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }

    def forward(self, query: str) -> str:
        """
        Fetch news articles for the provided query using the Serper.dev API.

        Args:
            query (str): The search query for news.

        Returns:
            str: JSON string of the news results or an error message.
        """
        # Construct the payload
        payload = json.dumps({"q": query})

        try:
            # Send the POST request to the Serper.dev API
            response = requests.post(self.url, headers=self.headers, data=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.text  # Return the raw JSON response as a string
        except requests.RequestException as e:
            error_msg = f"Error fetching news: {str(e)}"
            logger.error(error_msg)
            return error_msg
        except Exception as e:
            error_msg = f"Error processing request: {str(e)}"
            logger.error(error_msg)
            return error_msg