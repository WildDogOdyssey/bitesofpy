from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.select('.list-table')[0].tbody
    
    match = ['time', 'a']
    tags = table.find_all(match)
    
    holiday = []
    date = []
    
    for tag in tags:
        if tag.name == 'a':
            holiday.append(tag.string.strip())
        elif tag.name == 'time':
            date.append(tag.string)
    
    h = list(zip(date, holiday))
    
    for k, v in h:
        holidays[k[5:7]].append(v)
        
    return holidays