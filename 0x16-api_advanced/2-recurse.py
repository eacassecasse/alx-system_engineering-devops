#!/usr/bin/python3
"""Function to retrieve a list of all hot posts on a given Reddit subreddit."""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Retrieve a list of titles of all hot posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot posts (default is an empty list).
        after (str): The ID of the last post in the previous request (default is an empty string).
        count (int): The count of posts retrieved so far (default is 0).

    Returns:
        list: A list containing the titles of all hot posts on the subreddit.

    Note:
        Reddit API limits the number of posts per request to 100.
        To retrieve more posts, the function makes recursive requests until all posts are fetched.
    """
    # Construct the URL for the subreddit's hot posts API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Set custom User-Agent header to avoid 429 Too Many Requests error
    headers = {
        "User-Agent": "MyRedditClient/1.0"
    }

    # Set query parameters including the 'after' parameter for pagination
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params)

    # Check if the subreddit exists
    if response.status_code == 404:
        return None

    # Parse the JSON response to extract post data
    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    # If there are more posts to fetch, make a recursive call
    if after:
        return recurse(subreddit, hot_list, after, count)

    # Return the list of hot posts once all posts have been fetched
    return hot_list
