# I need to do some very basic object testing,
# let's see if I can import my classes and access their attributes
from objects import simpleRepo


class repo:
    def __init__(self, url, name, owner, watching, stars, forks):
        self.url = url
        self.name = name
        self.owner = owner
        self.watching = watching
        self.stars = stars
        self.forks = forks


Repo = repo()
Repo.name = 'Repo'
print(Repo.name)
