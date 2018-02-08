## gets list of repo links that appear in github search query
import string
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from random import randint
import re
import requests

BASE_URL = "https://github.com/"
FOLLOWING_URL_END = "?tab=following"
FOLLOWER_URL_END = "?tab=followers"
REPO_URL_END = "?tab=repositories"


class simpleRepo:
    def __init__(self, url, name, owner, watching, stars, forks):
        self.url = url or ''
        self.name = name or ''
        self.owner = owner or ''
        self.watching = watching or ''
        self.stars = stars or ''
        self.forks = forks or ''


class superRepo(simpleRepo):
    def __init__(self, url, name, owner, watching, stars, forks, commits, branches, releases, contributors, lic, languages):
        simpleRepo.__init__(self, url, name, owner, watching, stars, forks)
        self.commits = commits
        self.branches = branches
        self.releases = releases
        self.contributors = contributors
        self.lic = lic
        self.languages = languages


connection = mysql.connector.connect(host="localhost", port=3306, user="semdemo", passwd="demo", db="semdemo")
db = connection.cursor(prepared=True)

db.execute("""
        CREATE TABLE IF NOT EXISTS PYTHON_REPOS (
            url VARCHAR(256) NOT NULL PRIMARY KEY,
            repo_name VARCHAR(256) NOT NULL DEFAULT '',
            watchers INT(10) UNSIGNED NULL,
            stars INT(10) UNSIGNED NULL,
            forks INT(10) UNSIGNED NULL,
            commits INT(10) UNSIGNED NULL,
            branches INT(10) UNSIGNED NULL,
            releases INT(10) UNSIGNED NULL,
            contributors INT(10) UNSIGNED NULL,
            owner VARCHAR(256) NOT NULL DEFAULT ''
        )""")
connection.commit()

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

def get_header_info(soup: str):
    #gather all the basic information obtainable from the repo header, # of people watching, # stars, # forks

    info = [] # we'll store our info as a list
    #as of 10/17/2017 all this info is held in social-count tags
    tags = soup.findAll("a", "social-count")
    #watching = tags[0]['aria-label'] #aria-label contains string with # we want
    info.append(tags[0]['aria-label'][0:tags[0]['aria-label'].find(" ")]) # add just the numbers to our list
    info.append(tags[1]['aria-label'][0:tags[1]['aria-label'].find(" ")])
    info.append(tags[2]['aria-label'][0:tags[2]['aria-label'].find(" ")])
    return info


def populate_repo_from_url(url: str):
    box = simpleRepo('', '', '', '', '', '')
    box.url = url
    names = get_username_reponame_from_url(url)
    box.name = names[1]
    box.owner = names[0]
    soup = retrieve(box.url)
    temp = get_header_info(soup)
    box.watching = temp[0]
    box.stars = temp[1]
    box.forks = temp[2]
    # Test
    # print('repo values:\n url: %s\n name: %s\n owner: %s\n watching: %s\n stars: %s\n forks: %s\n'
    #       % (box.url, box.name, box.owner, box.watching, box.stars, box.forks))
    return box


def scrape_superRepo_numbers(soup: BeautifulSoup):
    numbers = []
    for item in soup.find_all("span", class_="num text-emphasized"):
        value = re.sub(r'\s', '', item.text)
        numbers.append(value)
    return numbers


def populate_superrepo(fullRepo: simpleRepo):
    #url, name, owner, watching, stars, forks, commits, branches, releases, contributors, lic, languages):
    emptyHero = superRepo(fullRepo.url, fullRepo.name, fullRepo.owner, fullRepo.watching, fullRepo.stars,
                          fullRepo.forks, '', '', '', '', '', [])
    soup = retrieve(emptyHero.url)
    numbers = scrape_superRepo_numbers(soup)
    emptyHero.commits = numbers[0]
    emptyHero.branches = numbers[1]
    emptyHero.releases = numbers[2]
    emptyHero.contributors = numbers[3]
    #emptyHero.lic = scrape_lic(soup)
    #emptyHero.languages = scrape_languages(soup)


    return emptyHero


def insert_repo_info(repo: superRepo):
    db.execute("insert into REPOSITORIES(url, repo_name, watchers, stars, forks, commits, branches, releases, contributors, owner) values(?,?,?,?,?,?,?,?,?,?)",
               [repo.url, repo.name, repo.watching, repo.stars, repo.forks, repo.commits, repo.branches, repo.releases, repo.contributors, repo.owner])
    connection.commit()

