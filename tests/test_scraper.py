import pytest
from media_agent.scraper import ContactScraper

@pytest.fixture
def scraper():
    return ContactScraper()

def test_scrape_contact_info_invalid_url(scraper):
    result = scraper.scrape_contact_info("https://invalid-url.fake")
    assert result in ["Failed to scrape", "No contact found"]
