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
        "User-agent": "MyRedditClient/1.0"
    }

    response = requests.get(url, headers=headers)

    results = response.json()

    try:
        return results.get("data").get("subscribers")
    except (Exception):
        return (0)
