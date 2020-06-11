from collections import Counter
from functools import lru_cache

import bs4
import requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


@lru_cache()
def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    table = soup.h2.next_sibling.next_sibling.table
    emails = [tr.find_all('td')[-2].text
              for tr in table.find_all('tr') if tr]
    return emails


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()

    domains = [email.split('@')[-1] for email in emails]
    unique = [domain for domain in domains
              if domain not in common_domains]
    return Counter(unique).most_common()
