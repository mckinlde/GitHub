# defines a simple github user class


class simpleUser:
    def __init__(self, username, followers, following, repositories):
        self.username = username
        self.followers = followers
        self.following = following
        self.repositories = repositories
    def get_username(self):
        return self.username
    def get_followers(self):
        return self.followers
    def get_following(self):
        return self.following
    def get_repositories(self):
        return self.repositories