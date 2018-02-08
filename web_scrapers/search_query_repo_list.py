## gets list of repo links that appear in github search query
import string
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from random import randint
import re
import requests

base_soup = 'https://github.com/search?utf8=%E2%9C%93&q=language%3APython&type='
url_to_join = "https://github.com"
links=[]

def retrieve(url: str):
    """retrieves content at the specified url"""
    print("*", url)
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    r=requests.get(url, headers=header, verify=False, timeout=5)
    sleep(1)
    soup = BeautifulSoup(r.text, "lxml")

    return soup

def get_links(url):
    # Get all links to repos from current result page
    soup = retrieve(url)
    for i in soup.find_all('a'):
        if (i.get('class') and (i.get('class'))[0] =="v-align-middle"):
            full_url = "https://github.com" + i.get('href')
            links.append(full_url)

    sleep(5)

    next_url = soup.find_all("a", class_ ="next_page")

    while len(next_url)!=0:
        next_page = next_url[0].get('href')
        next_page_url = urljoin(url_to_join,next_page)
        get_links(next_page_url)

    return links


j = get_links(base_soup)
print(j)


