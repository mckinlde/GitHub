## Search Query Repo List

## Include

## Helpers


# Get soup from url
def retrieve(url: str):
    soup = ''
    return soup


# Get list of links to repos on current page in search results
def get_links(soup: str):
    links = []
    return links


# Get url for next page in search results
def get_next_url(soup: str):
    next_url = ''
    return next_url


def main(query_url):
    # Take query url from:
        # console?
        # other script call?
    # Get first page of results, next page link from query
    first_soup = retrieve(query_url)
    repo_links = get_links(first_soup)
    next_url = get_next_url(first_soup) #gnu(url: str)
    # While we have more results
    while next_url is not None:
        current_soup = retrieve(next_url)
        # Get THIS page of query results, nextpage link
        repo_links.append(get_links(current_soup))
        next_url = get_next_url(current_soup)
        # Output links to:
            # console?
            # []?
            # numpy?
            # pandas?
            # SQL?
        # Pass Object Query?
