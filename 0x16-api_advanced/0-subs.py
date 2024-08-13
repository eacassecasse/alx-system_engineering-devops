#!/usr/bin/python3
"""Function to query the number of subscribers on a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The total number of subscribers on the subreddit.
             Returns 0 if the subreddit does not exist or if there is an error.
    """
    # Construct the URL for the subreddit information API endpoint
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set custom User-Agent header to avoid 429 Too Many Requests error
    headers = {
        "User-Agent": "MyRedditClient/1.0"
    }

    # Send a GET request to the Reddit API
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except (requests.HTTPError, requests.RequestException):
        return 0

    # Check if the subreddit exists
    # if response.status_code != 200:
    #    return 0

    # Parse the JSON response to extract the number of subscribers

    try:
        subreddit_info = response.json().get("data")
        if subreddit_info is None:
            return 0
        return subreddit_info.get("subscribers", 0)
    except ValueError:
        return 0
