# After 990 Java repos:
# * https://github.com/search?p=100&q=language%3AJava&type=Repositories&utf8=%E2%9C%93
# /Users/studentuser/anaconda3/lib/python3.6/site-packages/urllib3/connectionpool.py:858: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#   InsecureRequestWarning)
# Traceback (most recent call last):
#   File "/Users/studentuser/PycharmProjects/GitHub/web_scrapers/search_query_repo_list.py", line 169, in <module>
#     links, nextPage = get_links(nextPage)
#   File "/Users/studentuser/PycharmProjects/GitHub/web_scrapers/search_query_repo_list.py", line 155, in get_links
#     next_page = next_url[0].get('href')
# IndexError: list index out of range
#
# Process finished with exit code 1



## gets list of repo links that appear in github search query
import string
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from random import randint
import re
import requests
import mysql.connector

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
        CREATE TABLE IF NOT EXISTS JAVA_REPOS (
            url VARCHAR(256) NOT NULL PRIMARY KEY,
            repo_name VARCHAR(256) NOT NULL DEFAULT '',
            watchers VARCHAR(256) NOT NULL DEFAULT '',
            stars VARCHAR(256) NOT NULL DEFAULT '',
            forks VARCHAR(256) NOT NULL DEFAULT '',
            commits VARCHAR(256) NOT NULL DEFAULT '',
            branches VARCHAR(256) NOT NULL DEFAULT '',
            releases VARCHAR(256) NOT NULL DEFAULT '',
            contributors VARCHAR(256) NOT NULL DEFAULT '',
            owner VARCHAR(256) NOT NULL DEFAULT ''
        )""")
connection.commit()

base_soup = 'https://github.com/search?utf8=✓&q=language%3AJava&type='
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

def get_username_reponame_from_url(url: str):
    # 'https://github.com/USERNAME/REPONAME'
    #                  18^^19      ^past_username+1
    past_username = url.rfind('/')
    username = url[19:past_username]
    reponame = url[past_username+1:]
    return [username, reponame]


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
    ## mysql.connector.errors.DatabaseError: 1265 (01000): Data truncated for column 'commits' at row 1

    db.execute("insert into JAVA_REPOS(url, repo_name, watchers, stars, forks, commits, branches, releases, contributors, owner) values(?,?,?,?,?,?,?,?,?,?)",
               [repo.url, repo.name, repo.watching, repo.stars, repo.forks, repo.commits, repo.branches, repo.releases, repo.contributors, repo.owner])
    connection.commit()


def get_links(url):
    # Get all links to repos from current result page
    links = []
    soup = retrieve(url)
    for i in soup.find_all('a'):
        if (i.get('class') and (i.get('class'))[0] =="v-align-middle"):
            full_url = "https://github.com" + i.get('href')
            links.append(full_url)

    sleep(5)

    next_url = soup.find_all("a", class_ ="next_page")

    next_page = next_url[0].get('href')
    next_page_url = urljoin(url_to_join,next_page)

    return links, next_page_url


links, nextPage = get_links(base_soup)
print(links)

while len(nextPage)!=0:
    for link in links:
        simpleR = populate_repo_from_url(link)
        superR = populate_superrepo(simpleR)
        insert_repo_info(superR)
    links, nextPage = get_links(nextPage)

print("End of query results!")

