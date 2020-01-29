import csv
import requests
from collections import Counter
from pprint import pprint

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as dl:
        download = dl.get(CSV_URL)
        content = download.content.decode('utf-8')
        return content


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    cnt = Counter()

    for user in csv.DictReader(content.splitlines()):
        cnt[user['tz']] += 1

    title_len = max([len(key) for key in cnt.keys()])

    for k, v in cnt.items():
        title = k.ljust(title_len+3)
        count = '+'*v
        print(f'{title}|{count}')
