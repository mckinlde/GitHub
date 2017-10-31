import requests
from time import sleep
from bs4 import BeautifulSoup

class simpleUser:
    # defines a simple github user class
    # simpleUser can spit out all of its own values, and populate them by scraping github with BeautifulSoup
    def __init__(self, username, followers, following, repositories):

        self.base_url = "https://github.com/"
        self.following_url_end = "?tab=following"
        self.follower_url_end = "?tab=followers"
        self.repo_url_end = "?tab=repositories"

        self.username = username
        self.followers = followers
        self.following = following
        self.repositories = repositories

    def get_username(self):
        return self.username

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following

    def get_repositories(self):
        return self.repositories

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
