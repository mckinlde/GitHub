# RUN -> Input seed user -> get users following -> add to queue
# imports for functions
import string
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



## globals
BASE_URL = "https://github.com/"
FOLLOWING_URL_END = "?tab=following"
FOLLOWER_URL_END = "?tab=followers"
REPO_URL_END = "?tab=repositories"


## helper functions
def retrieve( url: str):
    """retrieves content at the specified url"""
    print("*", url)
    sleep(1)  # Play nice with GitHub's Bandwidth
    r = requests.get(url, verify=False)  # get the HTML; ignore SSL errors (present on this particular site)
    soup = BeautifulSoup(r.text, "lxml")  # parse the HTML
    return soup


def get_follower_usernames( username: str):
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


def get_header_info(url: str):
    #gather all the basic information obtainable from the repo header, # of people watching, # stars, # forks

    info = [] # we'll store our info as a list
    soup = retrieve(url)
    #as of 10/17/2017 all this info is held in social-count tags
    tags = soup.findAll("a", "social-count")
    #watching = tags[0]['aria-label'] #aria-label contains string with # we want
    info.append(tags[0]['aria-label'][0:tags[0]['aria-label'].find(" ")]) # add just the numbers to our list
    info.append(tags[1]['aria-label'][0:tags[1]['aria-label'].find(" ")])
    info.append(tags[2]['aria-label'][0:tags[2]['aria-label'].find(" ")])
    return info


def get_username_reponame_from_url(url: str):
    # 'https://github.com/USERNAME/REPONAME'
    #                  18^^19      ^past_username+1
    past_username = url.rfind('/')
    username = url[19:past_username]
    reponame = url[past_username+1:]
    return [username, reponame]


def populate_repo_from_url(url: str):
    box = simpleRepo
    box.url = url
    names = get_username_reponame_from_url(url)
    box.name = names[1]
    box.owner = names[0]
    temp = get_header_info(box.url)
    box.watching = temp[0]
    box.stars = temp[1]
    box.forks = temp[2]
    # Test
    # print('repo values:\n url: %s\n name: %s\n owner: %s\n watching: %s\n stars: %s\n forks: %s\n'
    #       % (box.url, box.name, box.owner, box.watching, box.stars, box.forks))
    return box


def populate_simpleUser_from_username(username: str):
    user = simpleUser
    user.username = username
    user.followers = get_follower_usernames(user.username)
    user.following = get_following_usernames(user.username)
    user.repos = get_repo_links(user.username)
    # Test
    # print('user.username: %s\nuser.followers: %s\nuser.following: %s\nuser.repos: %s'
    #       % (user.username, user.followers, user.following, user.repos))
    return user
# Test statements




def extend_user_list_by_following(seed_user: simpleUser, user_list: []):
    for user in seed_user.following:
        if user not in user_list:
            user_list.append(user)
    return user_list

# get seed user
user = simpleUser
user = populate_simpleUser_from_username('mckinlde')
print('user.username: %s\nuser.following: %s\nuser.followers%s\nuser.repositories: %s\n'
      % (user.username, user.following, user.followers, user.repositories))

print('GATE 1')

for item in seed_user.repositories:
    box = simpleRepo
    box = populate_repo_from_url(item)
    print('repo values:\n url: %s\n name: %s\n owner: %s\n watching: %s\n stars: %s\n forks: %s\n'
          % (box.url, box.name, box.owner, box.watching, box.stars, box.forks))


print('GATE 2')



print('GATE 3')

print(extend_user_list_by_following(seed_user, [seed_user.username]))

#for user in users:
#    # get repos created
#    repos = scraper.get_repo_links(user)
#    for repo in repos: # asynchronous?
#        info = scraper.get_header_info(repo)
#        print(info)
#    users.append(scraper.get_followed_usernames(user)) #add followed usernames to queue

