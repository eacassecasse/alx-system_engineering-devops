# API Advanced

This folder contains Python functions to interact with the Reddit API for retrieving information about subreddits and posts.

## General Objectives

In addition to using the provided functions, this folder also aims to help users achieve the following general objectives related to working with APIs:

### How to read API documentation to find the endpoints you’re looking for

Understanding how to navigate and interpret API documentation is crucial for effectively utilizing any API. The README provides examples of how to construct URLs for Reddit's API endpoints based on the documentation.

### How to use an API with pagination

Many APIs implement pagination to limit the number of results returned in a single request. The `recurse` function demonstrates how to handle pagination by recursively making API requests until all desired data is retrieved.

### How to parse JSON results from an API

Most modern APIs return data in JSON format. The provided functions demonstrate how to parse JSON responses using Python's `requests` library and extract relevant information from the API response.

### How to make a recursive API call

Some APIs require recursive calls to fetch all desired data, especially when dealing with paginated results. The `recurse` function illustrates how to make recursive API calls to retrieve all hot posts from a subreddit.

### How to sort a dictionary by value

Sorting a dictionary by value can be useful in various scenarios. The `count_words` function sorts the word count dictionary by value in descending order to display the most frequently occurring words first.

## Functions

### 1. `number_of_subscribers(subreddit)`

This function retrieves the total number of subscribers for a given subreddit.

#### Parameters:

- `subreddit` (str): The name of the subreddit.

#### Returns:

- `int`: The total number of subscribers for the subreddit.

### 2. `top_ten(subreddit)`

This function prints the titles of the 10 hottest posts on a given subreddit.

#### Parameters:

- `subreddit` (str): The name of the subreddit.

#### Returns:

- None

### 3. `recurse(subreddit, hot_list=[], after="", count=0)`

This function recursively retrieves a list of titles of all hot posts on a given subreddit.

#### Parameters:

- `subreddit` (str): The name of the subreddit.
- `hot_list` (list): List to store titles of hot posts.
- `after` (str): Token for paginating through API results.
- `count` (int): Total number of posts matched so far.

#### Returns:

- `list`: A list of titles of hot posts on the subreddit.

### 4. `count_words(subreddit, word_list)`

This function prints the counts of given words found in hot posts of a given subreddit.

#### Parameters:

- `subreddit` (str): The name of the subreddit.
- `word_list` (list): The list of words to search for in post titles.

#### Returns:

- None

## Usage

1. Clone the repository:

```
git clone https://github.com/eacassecasse/alx-system_engineering-devops.git
```

2. Import the functions into your Python script:

```python
from alx_system_engineering_devops_0x16_api_advanced.your_script import
import number_of_subscribers, top_ten, recurse, count_words
```

3. Use the functions as needed, passing the appropriate parameters.

```python
subreddit = "python"
word_list = ["python", "reddit", "programming"]

# Example usage of each function
print("Number of subscribers:", number_of_subscribers(subreddit))
print("\nTop Ten Posts:")
top_ten(subreddit)
print("\nAll Hot Posts:")
hot_posts = recurse(subreddit)
for post in hot_posts:
    print(post)
print("\nWord Counts:")
count_words(subreddit, word_list)
```

## Dependencies

- Python 3.x
- Requests library: `pip install requests`