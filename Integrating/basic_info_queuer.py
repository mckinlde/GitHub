# RUN -> Input seed user -> get users following -> add to queue
import web_scrapers
# get seed user
seed_username = input("Seed Username: ")
users = [seed_username]

for user in users:
    # get repos created
    repos = web_scrapers.user_repos.get_repo_links(user)
    for repo in repos: # asynchronous?
        info = web_scrapers.repo_basic_info.get_header_info(repo)
        print(info)
    users.append(web_scrapers.user_following.get_followed_usernames(user)) #add followed usernames to queue

