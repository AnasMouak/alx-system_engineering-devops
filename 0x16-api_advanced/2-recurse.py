#!/usr/bin/python3
"""
write a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Get the top ten posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        for post in posts:
            hot_list.append(post.get("data").get("title"))
        recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
