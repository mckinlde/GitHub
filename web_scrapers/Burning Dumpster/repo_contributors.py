import requests
from time import sleep
from bs4 import BeautifulSoup

#Okay, I wanna construct a network of all the users who have committed to a repository on GitHub

#This script gets a list of all the usernames that have committed to a repo, and some information about them

BASE_URL = "https://github.com/tensorflow/tensorflow/graphs/contributors"

def retrieve(url: str):
    """retrieves content at the specified url"""
    print("*", url)
    sleep(1)  # Play nice with GitHub's Bandwidth
    r = requests.get(url, verify=False)  # get the HTML; ignore SSL errors (present on this particular site)
    soup = BeautifulSoup(r.text, "lxml")  # parse the HTML
    return soup

def get_header_info():
    #gather all the basic information obtainable from the repo header, # of people watching, # stars, # forks

    info = {} # we'll store out info in a dict

    soup = retrieve(BASE_URL)
    #as of 10/17/2017 all this info is held in li class="contrib-person float-left col-6 pr-2 my-2" tags
    tags = soup.findAll('class="contrib-person float-left col-6 pr-2 my-2"')
    #watching = tags[0]['aria-label'] #aria-label contains string with # we want
    #info['watching'] = tags[0]['aria-label'][0:tags[0]['aria-label'].find(" ")] # add just the number to our dictionary
    print(tags)

    return info
get_header_info()
