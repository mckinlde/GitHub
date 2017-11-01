# RUN -> Input seed user -> get users following -> add to queue
# imports for functions
import requests
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

# classes I made
from Integrating import simpleRepo
from Integrating import simpleUser


## Okay new plan, I'm going to put function definitions right here in this script
## simpleUser and simpleRepo objects will just be used to hold data
## This script will create users and repos, populate their fields, and add them to the DB
## The DB will hold a USERS table and a REPOS table, with a 1-to-many relation based on ownership
## In the future I can add relations based on social network



## 4 globals
BASE_URL = "https://github.com/"
FOLLOWING_URL_END = "?tab=following"
FOLLOWER_URL_END = "?tab=followers"
REPO_URL_END = "?tab=repositories"


## 5 functions
def retrieve( url: str):
    """retrieves content at the specified url"""
    print("*", url)
    sleep(1)  # Play nice with GitHub's Bandwidth
    r = requests.get(url, verify=False)  # get the HTML; ignore SSL errors (present on this particular site)
    soup = BeautifulSoup(r.text, "lxml")  # parse the HTML
    return soup


def get_followed_usernames( username: str):
    # gather all the usernames a user follows

    result_list = []  # we'll store them in a list

    url = BASE_URL + username + FOLLOWER_URL_END
    soup = retrieve(url)
    # as of 10/17/2017 all this info is held in link-gray pl-1 tags
    usernames = soup.findAll("span", "link-gray pl-1")
    for username in usernames:
        result_list.append(username.text)
    return result_list


def get_following_usernames( username: str):
    # gather all the usernames a user is followed by

    result_list = []  # we'll store them in a list

    url = BASE_URL + username + FOLLOWING_URL_END
    soup = retrieve(url)
    # as of 10/17/2017 all this info is held in link-gray pl-1 tags
    usernames = soup.findAll("span", "link-gray pl-1")
    for username in usernames:
        result_list.append(username.text)
    return result_list


def get_repo_links(username: str):
    #gather links to all the repositories a user has

    result_list = [] # we just want an array of links

    url = BASE_URL + username + REPO_URL_END
    soup = retrieve(url)
    #as of 10/17/2017 all this info is held in name codeRepository tags
    links = soup.findAll(itemprop="name codeRepository")
    for link in links:
        repo_url = urljoin(url, link.get('href'))
        #repo_title = link.text #repo titles are coming out funny so let's use RegEx to clean them up
        #title = re.sub(r"(\\n\s*)(\w*)", "", repo_title).strip()
        #result_list[repo_url] = title
        result_list.append(repo_url)
    return result_list


def get_header_info(username: str, reponame: str):
    #gather all the basic information obtainable from the repo header, # of people watching, # stars, # forks

    info = [] # we'll store out info in an array
    url = BASE_URL + '/' + username + '/' + reponame
    soup = retrieve(url)
    #as of 10/17/2017 all this info is held in social-count tags
    tags = soup.findAll("a", "social-count")
    #watching = tags[0]['aria-label'] #aria-label contains string with # we want
    info['watching'] = tags[0]['aria-label'][0:tags[0]['aria-label'].find(" ")] # add just the number to our dictionary
    info['stars'] = tags[1]['aria-label'][0:tags[1]['aria-label'].find(" ")]
    info['forks'] = tags[2]['aria-label'][0:tags[2]['aria-label'].find(" ")]

    return info

# get seed user
seed_user = simpleUser
seed_user.username = ('mckinlde')
seed_user.followers = get_followed_usernames(seed_user.username)
seed_user.following = get_following_usernames(seed_user.username)
seed_user.repositories = get_repo_links(seed_user.username)

# Test statements
# print('seed_user.username: ')
# print(seed_user.username)
# print('seed_user.following: ')
# print(seed_user.following)
# print('seed_user.followers: ')
# print(seed_user.followers)
print('seed_user.repositories: ')
print(seed_user.repositories)

#for repo in seed_user.repositories:
#    box = simpleRepo
#    box.url = repo.url




#for user in users:
#    # get repos created
#    repos = scraper.get_repo_links(user)
#    for repo in repos: # asynchronous?
#        info = scraper.get_header_info(repo)
#        print(info)
#    users.append(scraper.get_followed_usernames(user)) #add followed usernames to queue

