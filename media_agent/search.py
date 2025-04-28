import logging
from serpapi import GoogleSearch
from media_agent.config import SERPAPI_KEY

logger = logging.getLogger(__name__)

class SearchClient:
    def __init__(self):
        self.api_key = SERPAPI_KEY

    def search_google(self, query, num_results=10):
        logger.info(f"Searching Google for query: {query}")
        search = GoogleSearch({
            "q": query,
            "num": num_results,
            "api_key": self.api_key
        })
        results = search.get_dict()
        urls = []
        if "organic_results" in results:
            for result in results["organic_results"]:
                if 'link' in result:
                    urls.append(result['link'])
        return urls
