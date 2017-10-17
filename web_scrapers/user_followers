import requests
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

#Let's get a list of all the users a user is followed by

#URL will be of format: https://github.com/ USERNAME ?tab=followers
BASE_URL = "https://github.com/"
URL_END = "?tab=followers"


def retrieve(url: str):
    """retrieves content at the specified url"""
    print("*", url)
    sleep(1)  # Play nice with GitHub's Bandwidth
    r = requests.get(url, verify=False)  # get the HTML; ignore SSL errors (present on this particular site)
    soup = BeautifulSoup(r.text, "lxml")  # parse the HTML
    return soup

def get_following_usernames(username: str):
    #gather all the usernames a user is followed by

    result_list = [] # we'll store them in a list

    url = BASE_URL + username + URL_END
    soup = retrieve(url)
    #as of 10/17/2017 all this info is held in link-gray pl-1 tags
    usernames = soup.findAll("span", "link-gray pl-1")
    for username in usernames:
        result_list.append(username.text)
    return result_list


print(get_following_usernames('mckinlde'))
