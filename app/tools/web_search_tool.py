from smolagents import Tool
import requests
import json
import logging

logger = logging.getLogger(__name__)


class WebSearchTool(Tool):
    """
        Tool for performing web searches using the Serper.dev API.

        This tool enables LLM agents to search the web for information based on queries.
        It interacts with the Serper.dev search API to fetch relevant search results,
        including links, snippets, and other metadata.

        Attributes:
            name (str): The name identifier for the tool.
            description (str): Human-readable description of the tool's functionality.
            inputs (dict): Schema defining the expected input parameters.
            output_type (str): The type of output returned by the tool.
            api_key (str): API key for authenticating with Serper.dev.
            url (str): Endpoint URL for the Serper.dev search API.
            headers (dict): HTTP headers for API requests.
    """
    name = "web_search"
    description = "Performs a web search using the Serper.dev API and returns the results."

    inputs = {
        "query": {
            "type": "string",
            "description": "The search query to send to the Serper.dev API."
        }
    }

    output_type = "string"

    def __init__(self, api_key: str, **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key
        self.url = "https://google.serper.dev/search"
        self.headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }

    def forward(self, query: str) -> str:
        """
        Perform a web search using the Serper.dev API.

        Args:
            query (str): The search query.

        Returns:
            str: JSON string of the search results or an error message.
        """
        # Construct the payloads
        payload = json.dumps({"q": query})

        try:
            # Send the POST request to the Serper.dev API
            response = requests.post(self.url, headers=self.headers, data=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors

            return response.text  # Return the raw JSON response as a string
        except requests.RequestException as e:
            error_msg = f"Error performing web search: {str(e)}"
            logger.error(error_msg)
            return error_msg
        except Exception as e:
            error_msg = f"Error processing request: {str(e)}"
            logger.error(error_msg)
            return error_msg


