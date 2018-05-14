import string
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from random import randint
import re
import requests
import mysql.connector
from datetime import datetime

## For a list of repo URLs, scrape the age of the repo

def retrieve(url: str):
    """retrieves content at the specified url"""
    print("*", url)
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    r=requests.get(url, headers=header, verify=False, timeout=5)
    sleep(61) #github ratelimits me at 60 requests/hour
    soup = BeautifulSoup(r.text, "lxml")

    return soup

test_url = 'https://github.com/0x5e/wechat-deleted-friends'

#modified_url = 'https://api.github.com/repos/0x5e/wechat-deleted-friends'

def url_modifier(url: str): #turn url into url for curl statement
    #https://github.com/0x5e/wechat-deleted-friends
    #0123456789123456789
    new_url = url[0:8] + 'api.' + url[8:19] + 'repos/' + url[19:]
    return new_url


modified_url = url_modifier(test_url)
print(modified_url)

def get_json(url:str):
    r = requests.get(url)
    return r.json()

json = get_json(modified_url)
print(json)
created_at = str(datetime.now())
if 'created_at' in json:
    created_at = json.get('created_at')

# compute months til now, ftw
from dateutil import parser
create_date = parser.parse(created_at)


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

print(str(create_date) + " was " + str(diff_month(datetime.now(), create_date)) + " months ago")


import csv

with open('/Users/douglasmckinley/Desktop/gradSchool/GitHub/data/repo ages - ages.csv','r') as userFile:
     with open('/Users/douglasmckinley/Desktop/gradSchool/GitHub/data/repo ages - ages.csv', 'w') as writeFile:
        userFileReader = csv.reader(userFile)
        writer = csv.writer(writeFile, lineterminator='\n')
        for row in userFileReader:
            url = row[0]
            if url == 'url':
                continue
            data = get_json(url_modifier(url))
            created_at = str(datetime.now())
            if 'created_at' in data:
                created_at = data.get('created_at')
            create_date = parser.parse(created_at)
            row[3] = diff_month(datetime.now(), create_date)
            writer.writerow(row)
