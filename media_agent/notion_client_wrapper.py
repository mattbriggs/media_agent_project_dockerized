import logging
from notion_client import Client
from media_agent.config import NOTION_SECRET, DATABASE_ID

logger = logging.getLogger(__name__)

class NotionClientWrapper:
    def __init__(self):
        self.notion = Client(auth=NOTION_SECRET)
        self.database_id = DATABASE_ID

    def contact_exists(self, url):
        response = self.notion.databases.query(
            database_id=self.database_id,
            filter={
                "property": "Name",
                "title": {
                    "equals": url
                }
            }
        )
        return bool(response.get('results'))

    def add_contact(self, url, contact_info):
        logger.info(f"Adding new contact to Notion: {url}")
        self.notion.pages.create(
            parent={"database_id": self.database_id},
            properties={
                "Name": {
                    "title": [{"text": {"content": url}}]
                },
                "Contact Info": {
                    "rich_text": [{"text": {"content": contact_info}}]
                },
                "Status": {
                    "select": {"name": "Not Contacted"}
                }
            }
        )
