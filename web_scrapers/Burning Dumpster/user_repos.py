import requests
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

#Let's get a list of all the repos a user owns

#URL will be of format: https://github.com/ USERNAME ?tab=repositories
BASE_URL = "https://github.com/"
URL_END = "?tab=repositories"


def retrieve(url: str):
    """retrieves content at the specified url"""
    print("*", url)
    sleep(1)  # Play nice with GitHub's Bandwidth
    r = requests.get(url, verify=False)  # get the HTML; ignore SSL errors (present on this particular site)
    soup = BeautifulSoup(r.text, "lxml")  # parse the HTML
    return soup

def get_repo_links(username: str):
    #gather links to all the repositories a user has

    result_list = {}

    url = BASE_URL + username + URL_END
    soup = retrieve(url)
    #as of 10/17/2017 all this info is held in name codeRepository tags
    links = soup.findAll(itemprop="name codeRepository")
    for link in links:
        repo_url = urljoin(url, link.get('href'))
        repo_title = link.text #repo titles are coming out funny so let's use RegEx to clean them up
        title = re.sub(r"(\\n\s*)(\w*)", "", repo_title).strip()
        result_list[repo_url] = title
    return result_list


print(get_repo_links('mckinlde'))
