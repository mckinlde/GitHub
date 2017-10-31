import requests
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


# defines a scraper class, with methods to populate simpleRepo and simpleUser classes

class scraper:
    
    def __init__(self):

        self.base_url = "https://github.com/"
        self.following_url_end = "?tab=following"
        self.follower_url_end = "?tab=followers"
        self.repo_url_end = "?tab=repositories"

    def retrieve(self, url: str):
        """retrieves content at the specified url"""
        print("*", url)
        sleep(1)  # Play nice with GitHub's Bandwidth
        r = requests.get(url, verify=False)  # get the HTML; ignore SSL errors (present on this particular site)
        soup = BeautifulSoup(r.text, "lxml")  # parse the HTML
        return soup

    def get_followed_usernames(self, username: str):
        # gather all the usernames a user follows
    
        result_list = []  # we'll store them in a list
    
        url = self.base_url + username + self.follower_url_end
        soup = self.retrieve(url)
        # as of 10/17/2017 all this info is held in link-gray pl-1 tags
        usernames = soup.findAll("span", "link-gray pl-1")
        for username in usernames:
            result_list.append(username.text)
        return result_list

    def get_following_usernames(self, username: str):
        # gather all the usernames a user is followed by
    
        result_list = []  # we'll store them in a list
    
        url = self.base_url + username + self.following_url_end
        soup = self.retrieve(url)
        # as of 10/17/2017 all this info is held in link-gray pl-1 tags
        usernames = soup.findAll("span", "link-gray pl-1")
        for username in usernames:
            result_list.append(username.text)
        return result_list

    def get_repo_links(self, username: str):
        # gather links to all the repositories a user has
    
        result_list = {}
    
        url = self.base_url + username + self.repo_url_end
        soup = self.retrieve(url)
        # as of 10/17/2017 all this info is held in name codeRepository tags
        links = soup.findAll(itemprop="name codeRepository")
        for link in links:
            repo_url = urljoin(url, link.get('href'))
            repo_title = link.text  # repo titles are coming out funny so let's use RegEx to clean them up
            title = re.sub(r"(\\n\s*)(\w*)", "", repo_title).strip()
            result_list[repo_url] = title
        return result_list
    
    def get_header_info(self, username: str, reponame: str):
        #gather all the basic information obtainable from the repo header, # of people watching, # stars, # forks
    
        info = {} # we'll store out info in a dict
        url = self.base_url + '/' + username + '/' + reponame
        soup = self.retrieve(url)
        #as of 10/17/2017 all this info is held in social-count tags
        tags = soup.findAll("a", "social-count")
        #watching = tags[0]['aria-label'] #aria-label contains string with # we want
        info['watching'] = tags[0]['aria-label'][0:tags[0]['aria-label'].find(" ")] # add just the number to our dictionary
        info['stars'] = tags[1]['aria-label'][0:tags[1]['aria-label'].find(" ")]
        info['forks'] = tags[2]['aria-label'][0:tags[2]['aria-label'].find(" ")]
        return info