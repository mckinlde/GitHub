# RUN -> Input seed user -> get users following -> add to queue
from Integrating import scraper
from Integrating import simpleRepo
from Integrating import simpleUser
# get seed user
seed_user = simpleUser
seed_user.username = input("Seed Username: ")
seed_user.followers = []
seed_user.get_followers


#for user in users:
#    # get repos created
#    repos = scraper.get_repo_links(user)
#    for repo in repos: # asynchronous?
#        info = scraper.get_header_info(repo)
#        print(info)
#    users.append(scraper.get_followed_usernames(user)) #add followed usernames to queue

