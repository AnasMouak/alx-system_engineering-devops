#!/usr/bin/python3
"""
write a function that queries the Reddit API ,
parse the title of all hot articles, and prints
a sorted count of given keywords (case-insensitive,
delimited by spaces.
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Get the top ten posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to search for in the titles of the
            hot articles.
        hot_list (list): A list to store the titles of the hot articles.
        after (str): The id of the last post in the previous request.

    Returns:
        None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        for post in posts:
            hot_list.append(post.get("data").get("title"))
        after = data.get("data").get("after")
        if after is not None:
            count_words(subreddit, word_list, hot_list, after)
        else:
            word_dict = {}
            normalized_word_list = [word.lower() for word in word_list]

            for title in hot_list:
                words_in_title = title.lower().split()
                for word in normalized_word_list:
                    word_dict[word] = word_dict.get(
                        word, 0) + words_in_title.count(word)

            sorted_word_counts = sorted(word_dict.items(), key=lambda x:
                                        (-x[1], x[0]))

            for key, value in sorted_word_counts:
                if value > 0:
                    print(f"{key}: {value}")
    else:
        print(None)
