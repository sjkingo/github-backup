import re
import requests

API_URL = 'https://api.github.com'
FILTER_ATTRIBS = ['description', 'clone_url', 'default_branch', 'name']

_next_url_patt = re.compile(r'<([-:\/.\?=a-zA-Z0-9]+)>; rel="next"')
def get_repos_for_user(username):
    """
    Fetches a list of all repos for the given user and returns this.
    The GitHub API is paginated, so this function handles multiple pages
    of results being returned.
    """

    def get_repos(url, attribs=FILTER_ATTRIBS):
        """
        Get the repositories at the given URL and return a list
        of dictionaries with the given keys.
        """
        r = requests.get(url)
        r.raise_for_status()
        return (r, [{k: repo[k] for k in attribs} for repo in r.json()])

    # Get the initial page
    repos = []
    initial_url = '{api}/users/{username}/repos'.format(api=API_URL, username=username)
    r, page_1_repos = get_repos(initial_url)
    repos.extend(page_1_repos)

    def next_page(response, repos):
        next_url = _next_url_patt.match(response.headers.get('link'))
        if next_url is None:
            return
        r, page_X_repos = get_repos(next_url.groups()[0])
        repos.extend(page_X_repos)
        next_page(r, repos)

    # Follow the chain of pages
    next_page(r, repos)
    return repos
