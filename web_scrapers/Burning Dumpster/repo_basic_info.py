import requests
from time import sleep
from bs4 import BeautifulSoup

"""
Okay, time to let the data flow!

I'm going to use BeautifulSoup because it'll be more adaptable to future projects

Eventually I'd like to be able to use this data to predict how many pull requests a repository will have.  So we'll be
scraping data from the repository pages themselves.  This means the BASE_URL will have to be changed for each new repo
"""
BASE_URL = "https://github.com/"


def retrieve(url: str):
    """retrieves content at the specified url"""
    print("*", url)
    sleep(1)  # Play nice with GitHub's Bandwidth
    r = requests.get(url, verify=False)  # get the HTML; ignore SSL errors (present on this particular site)
    soup = BeautifulSoup(r.text, "lxml")  # parse the HTML
    return soup

def get_header_info(username: str, reponame: str):
#gather all the basic information obtainable from the repo header, # of people watching, # stars, # forks

    info = {} # we'll store out info in a dict
    url = BASE_URL + '/' + username + '/' + reponame
    soup = retrieve(url)
    #as of 10/17/2017 all this info is held in social-count tags
    tags = soup.findAll("a", "social-count")
    #watching = tags[0]['aria-label'] #aria-label contains string with # we want
    info['watching'] = tags[0]['aria-label'][0:tags[0]['aria-label'].find(" ")] # add just the number to our dictionary
    info['stars'] = tags[1]['aria-label'][0:tags[1]['aria-label'].find(" ")]
    info['forks'] = tags[2]['aria-label'][0:tags[2]['aria-label'].find(" ")]

    return info
print(get_header_info('tensorflow', 'tensorflow'))
