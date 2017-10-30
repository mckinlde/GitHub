# defines a class for a github repository


class simpleRepo:
    def __init__(self, url, name, owner, watching, stars, forks):
        self.url = url
        self.name = name
        self.owner = owner
        self.watching = watching
        self.stars = stars
        self.forks = forks
    def get_url(self):
        return self.url
    def get_name(self):
        return self.name
    def get_owner(self):
        return self.owner
    def get_watching(self):
        return self.watching
    def get_stars(self):
        return self.stars
    def get_forks(self):
        return self.forks
