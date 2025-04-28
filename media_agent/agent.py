import logging
from media_agent.search import SearchClient
from media_agent.scraper import ContactScraper
from media_agent.notion_client_wrapper import NotionClientWrapper
from media_agent.config import SEARCH_QUERY, NUM_RESULTS

logger = logging.getLogger(__name__)

class MediaAgent:
    def __init__(self):
        self.search_client = SearchClient()
        self.scraper = ContactScraper()
        self.notion_client = NotionClientWrapper()

    def run_daily(self):
        logger.info("Starting daily media agent run")
        urls = self.search_client.search_google(SEARCH_QUERY, NUM_RESULTS)

        for url in urls:
            logger.info(f"Processing: {url}")
            if not self.notion_client.contact_exists(url):
                contact_info = self.scraper.scrape_contact_info(url)
                self.notion_client.add_contact(url, contact_info)
            else:
                logger.info(f"URL already exists in Notion: {url}")
