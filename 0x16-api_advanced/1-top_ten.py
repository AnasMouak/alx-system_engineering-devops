#!/usr/bin/python3
""""write a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """
    Get the top ten posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
    else:
        print(None)
