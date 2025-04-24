from smolagents import Tool
import requests
import json
import logging

logger = logging.getLogger(__name__)



class WebCrawlerTool(Tool):
    name = "web_crawler"
    description = "Crawls and extracts all content from a specified URL using the Serper.dev API."

    inputs = {
        "url": {
            "type": "string",
            "description": "The URL of the web page to crawl and extract content from."
        }
    }

    output_type = "string"

    def __init__(self, api_key: str, **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key
        self.url = "https://scrape.serper.dev"
        self.headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }

    def forward(self, url: str) -> str:
        """
        Crawl and extract content from the provided URL using the Serper.dev API.

        Args:
            url (str): The URL to crawl.

        Returns:
            str: JSON string of the extracted content or an error message.
        """
        # Construct the payload
        payload = json.dumps({"url": url})

        try:
            # Send the POST request to the Serper.dev API
            response = requests.post(self.url, headers=self.headers, data=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = json.loads(response.text)
            logger.info(f"Successfully crawled URL: {url}")
            return data.get('text', 'No text content found')
        except requests.RequestException as e:
            error_msg = f"Error crawling URL '{url}': {str(e)}"
            logger.error(error_msg)
            return error_msg
        except Exception as e:
            error_msg = f"Error processing request: {str(e)}"
            logger.error(error_msg)
            return error_msg


