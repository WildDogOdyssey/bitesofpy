from collections import namedtuple

from bs4 import BeautifulSoup
import requests
import re

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# url = 'https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html'
# url = 'https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html'

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    # Create soup object
    soup = _create_soup_obj(url)
    
    # Separate object since target information is nested in layers of tags
    title_list = soup.find_all(class_="title")
    score = soup.find_all(class_="controls")
    
    # Setup regex to match target information
    pt_pat = re.compile(r'(\d+?)\spoint(s)?\sby')
    comment_pat = re.compile(r'(\d+?)\scomments')
    
    # Create paired tuples of title and body of text for iteration
    titles = list(zip(title_list, score))
    
    # Iterate through the list of title and regex match text for namedtuple
    lst = []
    
    for item in titles:
        title = item[0].get_text().strip()
        text = item[1].find('span').get_text()
        points = int(re.search(pt_pat, text).group(1))
        comments = int(re.search(comment_pat, text).group(1))
        t = Entry(title=title, points=points, comments=comments)
        lst.append(t)
    
    # Sort based on points then comments
    return sorted(lst, key=lambda x: (x[1], x[2]), reverse=True)[:top]