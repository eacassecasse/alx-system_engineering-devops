#!/usr/bin/python3
"""Function to print the titles of the top 10 hot posts on
a given Reddit subreddit."""

import requests


def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
    # Construct the URL for the subreddit's hot posts API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set custom User-Agent header to avoid 429 Too Many Requests error
    headers = {
        "User-agent": "MyRedditClient/1.0"
    }

    # Set query parameters to limit the number of posts to 10
    params = {
        "limit": 10
    }

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params)
    results = response.json()

    try:
        posts = results.get('data').get("children")

        for post in posts:
            print(post.get("data").get("title"))
    except (Exception):
        print(None)
