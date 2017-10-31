import requests
from time import sleep
from bs4 import BeautifulSoup

class simpleUser:
    # defines a simple github user class
    # simpleUser can spit out all of its own values, and populate them by scraping github with BeautifulSoup
    def __init__(self, username, followers, following, repositories):
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
