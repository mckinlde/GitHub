# Errors I have gotten:
# /Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/connectionpool.py:852: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
# InsecureRequestWarning)
# Traceback (most recent call last):
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/connectionpool.py", line 379, in _make_request
# httplib_response = conn.getresponse(buffering=True)
# TypeError: getresponse() got an unexpected keyword argument 'buffering'

## Another one
# InsecureRequestWarning)
# /Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/connectionpool.py:852: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
# InsecureRequestWarning)
# Traceback (most recent call last):
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/connection.py", line 141, in _new_conn
#                                                                                                                          (self.host, self.port), self.timeout, **extra_kw)
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/util/connection.py", line 83, in create_connection
# raise err
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/util/connection.py", line 73, in create_connection
# sock.connect(sa)
# OSError: [Errno 50] Network is down
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/connectionpool.py", line 600, in urlopen
# chunked=chunked)
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/connectionpool.py", line 345, in _make_request
# self._validate_conn(conn)
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/connectionpool.py", line 844, in _validate_conn
# conn.connect()
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/connection.py", line 284, in connect
# conn = self._new_conn()
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/connection.py", line 150, in _new_conn
# self, "Failed to establish a new connection: %s" % e)
# requests.packages.urllib3.exceptions.NewConnectionError: <requests.packages.urllib3.connection.VerifiedHTTPSConnection object at 0x1040b5630>: Failed to establish a new connection: [Errno 50] Network is down
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/adapters.py", line 438, in send
# timeout=timeout
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/connectionpool.py", line 649, in urlopen
# _stacktrace=sys.exc_info()[2])
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/packages/urllib3/util/retry.py", line 388, in increment
# raise MaxRetryError(_pool, url, error or ResponseError(cause))
# requests.packages.urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /soumith/ganhacks (Caused by NewConnectionError('<requests.packages.urllib3.connection.VerifiedHTTPSConnection object at 0x1040b5630>: Failed to establish a new connection: [Errno 50] Network is down',))
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
# File "/Users/douglasmckinley/Desktop/gradSchool/GitHub/Integrating/basic_info_queuer.py", line 326, in <module>
# repo_list = populate_user_repository_list(tempPopulatedUser)
# File "/Users/douglasmckinley/Desktop/gradSchool/GitHub/Integrating/basic_info_queuer.py", line 192, in populate_user_repository_list
# newRepo = populate_repo_from_url(item)
# File "/Users/douglasmckinley/Desktop/gradSchool/GitHub/Integrating/basic_info_queuer.py", line 154, in populate_repo_from_url
# temp = get_header_info(box.url)
# File "/Users/douglasmckinley/Desktop/gradSchool/GitHub/Integrating/basic_info_queuer.py", line 129, in get_header_info
# soup = retrieve(url)
# File "/Users/douglasmckinley/Desktop/gradSchool/GitHub/Integrating/basic_info_queuer.py", line 74, in retrieve
# r = requests.get(url, verify=False)  # get the HTML; ignore SSL errors (present on this particular site)
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/api.py", line 72, in get
# return request('get', url, params=params, **kwargs)
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/api.py", line 58, in request
# return session.request(method=method, url=url, **kwargs)
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/sessions.py", line 518, in request
# resp = self.send(prep, **send_kwargs)
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/sessions.py", line 639, in send
# r = adapter.send(request, **kwargs)
# File "/Users/douglasmckinley/anaconda/lib/python3.6/site-packages/requests/adapters.py", line 502, in send
# raise ConnectionError(e, request=request)
# requests.exceptions.ConnectionError: HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /soumith/ganhacks (Caused by NewConnectionError('<requests.packages.urllib3.connection.VerifiedHTTPSConnection object at 0x1040b5630>: Failed to establish a new connection: [Errno 50] Network is down',))
#
# Process finished with exit code 1



# RUN -> Input seed user -> get users following -> add to queue
# imports for functions
import string
import requests
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import mysql.connector

# globals
BASE_URL = "https://github.com/"
FOLLOWING_URL_END = "?tab=following"
FOLLOWER_URL_END = "?tab=followers"
REPO_URL_END = "?tab=repositories"


# classes
class simpleUser:
    # defines a simple github user class
    # simpleUser can spit out all of its own values, and populate them by scraping github with BeautifulSoup
    def __init__(self, username, followers, following, repositories):
        self.username = username or ''
        self.followers = followers or []
        self.following = following or []
        self.repositories = repositories or []


class superUser:
    #superuser is for statistics that are calculated, not scraped
    #functions should assume a simpleuser object with repositories as a list
    #of populated simpleRepo objects
    def __init__(self, username, total_followers, total_following, mutualFollows, total_repositories, total_forks, total_stars, total_watchers):
        self.username = username or ''
        self.total_followers = total_followers or ''
        self.total_following = total_following or ''
        self.mutualFollows = mutualFollows or ''
        self.total_repositories = total_repositories or ''
        self.total_forks = total_forks or ''
        self.total_stars = total_stars or ''
        self.total_watchers = total_watchers or ''


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




## helper functions



def retrieve(url: str):
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
    box = simpleRepo('', '', '', '', '', '')
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
    user = simpleUser('', [], [], [])
    user.username = username
    user.followers = get_follower_usernames(user.username)
    user.following = get_following_usernames(user.username)
    user.repositories = get_repo_links(user.username)
    # Test
    # print('user.username: %s\nuser.followers: %s\nuser.following: %s\nuser.repos: %s'
    #       % (user.username, user.followers, user.following, user.repositories))
    return user

def print_simpleUser_attributes(user: simpleUser):
    print('user.username: %s\nuser.followers: %s\nuser.following: %s\nuser.repos: %s'
          % (user.username, user.followers, user.following, user.repositories))


def extend_user_list_by_following(seed_user: simpleUser, user_list: []):
    for user in seed_user.following:
        if user not in user_list:
            user_list.append(user)
    return user_list


def populate_user_repository_list(seed_user: simpleUser):
    # get repos, populate
    result_list = list()
    #reference to a module instead of creating a new instance of the thing
    for item in seed_user.repositories:
        newRepo = populate_repo_from_url(item)
        result_list.append(newRepo)
        # Test
        # print('repo values:\n url: %s\n name: %s\n owner: %s\n watching: %s\n stars: %s\n forks: %s\n'
        #       % (repo.url, repo.name, repo.owner, repo.watching, repo.stars, repo.forks))
    return result_list


def insert_repo_info(repo: superRepo):
    db.execute("insert into REPOSITORIES(url, repo_name, watchers, stars, forks, commits, branches, releases, contributors, owner) values(?,?,?,?,?,?,?,?,?,?)",
               [repo.url, repo.name, repo.watching, repo.stars, repo.forks, repo.commits, repo.branches, repo.releases, repo.contributors, repo.owner])
    connection.commit()


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


testSimpleRepo = populate_repo_from_url('https://github.com/tensorflow/tensorflow')
testSuperRepo = populate_superrepo(testSimpleRepo)
print(testSuperRepo.contributors)

#['\n                26,534\n              ', '\n              18\n            ', '\n              43\n            ', '\n      1,231\n    ']



def populate_superuser_statistics(emptyHero: superUser, fullUser: simpleUser):
    emptyHero.username = fullUser.username

    mutualFollows = 0
    for followedUname in fullUser.following:
        if followedUname in fullUser.followers:
            mutualFollows = mutualFollows + 1
    emptyHero.mutualFollows = mutualFollows

    emptyHero.total_followers = len(fullUser.followers)
    emptyHero.total_following = len(fullUser.following)
    emptyHero.total_repositories = len(fullUser.repositories)
    ## ToDo: Make this less brutal
    counter = 0
    for repo in fullUser.repositories:
        counter = counter + int(repo.forks)
    emptyHero.total_forks = counter
    counter = 0
    for repo in fullUser.repositories:
        counter = counter + int(repo.stars)
    emptyHero.total_stars = counter
    counter = 0
    for repo in fullUser.repositories:
        counter = counter + int(repo.watching)
    emptyHero.total_watchers = counter
    return emptyHero


def insert_superuser(myHero: superUser):
    db.execute("insert into USERS(username, num_followers, num_following, mutualFollows, "
               "num_repos, num_forks, num_stars, num_watchers) values(?,?,?,?,?,?,?,?)",
               [myHero.username, myHero.total_followers, myHero.total_following, myHero.mutualFollows,
                myHero.total_repositories, myHero.total_forks, myHero.total_stars, myHero.total_watchers])
    connection.commit()




#print('seed_user.username: %s\nseed_user.followers: %s\nseed_user.following: %s\nseed_user.repos: %s'
#      % (seed_user.get_username, seed_user.get_followers, seed_user.get_following, seed_user.get_repositories))

connection = mysql.connector.connect(host="localhost", port=3306, user="semdemo", passwd="demo", db="semdemo")
db = connection.cursor(prepared=True)

seed_user = simpleUser('', [], [], [])
seed_user = populate_simpleUser_from_username(input('input seed username: '))
print_simpleUser_attributes(seed_user)

print('GATE 1: populated seed_user')

#seed_repo_list = populate_user_repository_list(seed_user)

db.execute("""
        CREATE TABLE IF NOT EXISTS REPOSITORIES (
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

db.execute("""
        CREATE TABLE IF NOT EXISTS FOLLOWS (
            mid MEDIUMINT AUTO_INCREMENT PRIMARY KEY,
            username_following VARCHAR(256) NOT NULL DEFAULT '',
            username_followed VARCHAR(256) NOT NULL DEFAULT ''
        )""")

db.execute("""
        CREATE TABLE IF NOT EXISTS OWNS (
            username VARCHAR(256) NOT NULL DEFAULT '',
            url VARCHAR(256) NOT NULL PRIMARY KEY
        )""")

db.execute("""
        CREATE TABLE IF NOT EXISTS USERS (
            username VARCHAR(256) NOT NULL DEFAULT '',
            num_followers INT(10) UNSIGNED NULL,
            num_following INT(10) UNSIGNED NULL,
            mutualFollows INT(10) UNSIGNED NULL,
            num_repos INT(10) UNSIGNED NULL,
            num_forks INT(10) UNSIGNED NULL,
            num_stars INT(10) UNSIGNED NULL,
            num_watchers INT(10) UNSIGNED NULL
        )""")
connection.commit()



print('GATE 2: CREATED TABLES')

# Input seed_user's repositories (info and owner relationshp) to DB
# nevermind don't do this because it'll get caught later
#for repo in seed_repo_list:
#    insert_repo_info(repo)
#    db.execute("insert into OWNS(username, url) values(?,?)", [seed_user.username, repo.url])

user_list = seed_user.following
print('INITAL USER LIST')
# Input seed_user's follow relationships to DB
# yeah same don't do this primary key goof
#for user in user_list:
#    db.execute("insert into FOLLOWS(username_following, username_followed) values(?,?)",[seed_user.username, user])


for user in user_list:
    tempPopulatedUser = populate_simpleUser_from_username(user) # this will only be populated for this iter of loop
    #print_simpleUser_attributes(tempPopulatedUser)
    print('POPULATED USER')
    for followedUser in tempPopulatedUser.following:
        db.execute("insert into FOLLOWS(username_following, username_followed) values(?,?)",
                   [tempPopulatedUser.username, followedUser])
        connection.commit()
    print('UPDATE FOLLOWS')
    for ownedRepo in tempPopulatedUser.repositories:
        db.execute("insert into OWNS(username, url) values(?,?)", [tempPopulatedUser.username, ownedRepo])
        connection.commit()
    print('UPDATE OWNS')

    repo_list = populate_user_repository_list(tempPopulatedUser)

    print('UPDATE REPO LIST')
    tempPopulatedUser.repositories = repo_list
    for tempRepo in repo_list:
        #tempSimpleRepo = populate_repo_from_url(tempRepo.url)
        print(tempRepo)
        try:
            superTemp = populate_superrepo(tempRepo)
            ## Bug:  contributors value isn't populated, resolve with 0 as when cleaning data all repos obviously have at least 1 contributor
            if superTemp.contributors == '':
                superTemp.contributors = 0
            try:
                insert_repo_info(superTemp)
            except:
                print('failed to insert: ' + superTemp.name + 'by' + superTemp.owner)
        except:
            print('failed to populate: ' + tempRepo.name)
    print('POPULATED REPOS')
    #print(user_list)
    #populate superUser, insert into DB
    myHero = superUser('', '', '', '', '', '','', '')
    #populate_superuser requires a FULL user (user.repositories is a list of populated repos)

    print('tempPopulatedUser is now a FULL user')
    populate_superuser_statistics(myHero, tempPopulatedUser)
    insert_superuser(myHero)
    print('UPDATE USERS')
    user_list = extend_user_list_by_following(tempPopulatedUser, user_list)


#print('repo values:\n url: %s\n name: %s\n owner: %s\n watching: %s\n stars: %s\n forks: %s\n'
#      % (user_repos[1].url, user_repos[1].name, user_repos[1].owner, user_repos[1].watching, user_repos[1].stars, user_repos[0].forks))
#
# print('GATE 2')
# import mysql.connector
#
#
#
#
# db.execute("""
#         CREATE TABLE IF NOT EXISTS REPOSITORIES (
#             mid MEDIUMINT AUTO_INCREMENT PRIMARY KEY,
#             url VARCHAR(256) NOT NULL DEFAULT '',
#             repo_name VARCHAR(256) NOT NULL DEFAULT '',
#             username VARCHAR(256) NOT NULL DEFAULT '',
#             watchers INT(10) UNSIGNED NULL,
#             stars INT(10) UNSIGNED NULL,
#             forks INT(10) UNSIGNED NULL
#         )""")
#
#
# def insert_repo_info(repo: simpleRepo):
#     db.execute("insert into REPOSITORIES(url, repo_name, username, watchers, stars, forks) values(?,?,?,?,?,?)",
#                [repo.url, repo.name, repo.owner, repo.watching, repo.stars, repo.forks])
#
#
# for repo in user_repos:
#     print('flag')
#     db.execute("insert into REPOSITORIES(url, repo_name, username, watchers, stars, forks) values(?,?,?,?,?,?)",
#                [repo.url, repo.name, repo.owner, repo.watching, repo.stars, repo.forks])
#     connection.commit()

