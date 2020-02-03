from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

# =============================================================================
# PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
# CONTENT = requests.get(PACKT).text
# =============================================================================

with open('packet.html', 'r') as r:
    CONTENT = r.read()

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    
    deal_section = soup.find(id="deal-of-the-day")
    summary = deal_section.find(class_='dotd-main-book-summary float-left')
    
    title = summary.find('h2').string.strip()
    description = summary.find_all('div')[2].string.strip()
    image = deal_section.find('img').get('src') #image
    link = deal_section.find('a').get('href')
    
    return Book(title=title, description=description, image=image, link=link)

print(get_book())