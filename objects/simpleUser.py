class simpleUser:
    # defines a simple github user class
    # simpleUser can spit out all of its own values, and populate them by scraping github with BeautifulSoup
    def __init__(self, username, followers, following, repositories):
        self.username = username
        self.followers = followers
        self.following = following
        self.repositories = repositories