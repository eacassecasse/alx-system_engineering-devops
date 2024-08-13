#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Print counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Dictionary to store word counts.
        after (str): Token to paginate through API results.
        count (int): Total number of results matched so far.
    """
    # Construct the URL for Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "MyRedditClient/1.0"}
    params = {"after": after, "count": count, "limit": 100}

    # Send GET request to Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check for valid response
    try:
        response.raise_for_status()
    except requests.HTTPError:
        print("Error: Unable to retrieve data from Reddit API")
        return

    # Extract relevant data from the response JSON
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    # Process each post in the results
    for child in results.get("children"):
        title = child.get("data").get("title").lower().split()
        # Check if any word in the word_list is present in the post title
        for word in word_list:
            if word.lower() in title:
                times = title.count(word.lower())
                # Update the word count in the instances dictionary
                instances[word] = instances.get(word, 0) + times

    # If there are more pages of results, recursively call count_words
    if after is not None:
        count_words(subreddit, word_list, instances, after, count)
    else:
        # Sort and print the word counts
        if len(instances) > 0:
            instances = sorted(instances.items(), key=lambda x: (-x[1], x[0]))
            for word, count in instances:
                print(f"{word}: {count}")
        else:
            print("No matches found.")
