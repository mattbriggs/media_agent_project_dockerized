import re
import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

class ContactScraper:
    def __init__(self):
        self.email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')

    def scrape_contact_info(self, url):
        logger.info(f"Scraping contact info from: {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            found_emails = set()
            for link in soup.find_all('a', href=True):
                if "mailto:" in link['href']:
                    found_emails.add(link['href'].split(':')[1])

            page_text = soup.get_text()
            found_emails.update(self.email_pattern.findall(page_text))

            if found_emails:
                return ", ".join(found_emails)

            forms = soup.find_all('form')
            for form in forms:
                form_action = form.get('action', '')
                if any(keyword in form_action.lower() for keyword in ['contact', 'submit', 'message', 'form'])                     or any(keyword in url.lower() for keyword in ['contact', 'submit', 'message', 'form']):
                    return "Contact form available at page"

            return "No contact found"
        except Exception as e:
            logger.error(f"Error scraping {url}: {e}")
            return "Failed to scrape"
