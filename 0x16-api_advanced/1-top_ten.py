#!/usr/bin/python3
"""Function to print the titles of the top 10 hot posts on a given Reddit subreddit."""

import requests

def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    # Construct the URL for the subreddit's hot posts API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Set custom User-Agent header to avoid 429 Too Many Requests error
    headers = {
        "User-Agent": "MyRedditClient/1.0"
    }

    # Set query parameters to limit the number of posts to 10
    params = {
        "limit": 10
    }

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params)

    # Check if the subreddit exists
    if response.status_code == 404:
        print("Subreddit not found.")
        return

    # Parse the JSON response to extract the titles of the top 10 hot posts
    data = response.json().get("data")
    posts = data.get("children")
    for post in posts:
        title = post.get("data").get("title")
        print(title)
