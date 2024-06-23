#!/usr/bin/python3
"""module '1-top_ten.py' to fetch from reddit api"""


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""
    import requests


    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Chrome/1.0;Mozilla/5.0'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data.get('data').get('children')
        for item in children:
            print(item.get('data').get('title'))
    else:
        print("None")

