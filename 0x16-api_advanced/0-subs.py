#!/usr/bin/python3
"""module "0-subs.py" fetch data from the reddit api"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "Some-User-Agent-4.0"},
                            allow_redirects=False)
    if (response.status_code == 200) {
        return (response.json()['data']['subscribers'])
    }
    return (0)
