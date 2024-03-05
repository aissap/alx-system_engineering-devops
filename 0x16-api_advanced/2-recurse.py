#!/usr/bin/python3
import requests
"""
Recursively queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""


def recurse(subreddit, hot_list=[]):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        return None
    
    data = response.json().get("data")
    children = data.get("children")
    
    for post in children:
        title = post.get("data").get("title")
        hot_list.append(title)
    
    if data.get("after"):
        params["after"] = data.get("after")
        recurse(subreddit, hot_list)
    
    return len(hot_list)

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    print(recurse(subreddit))
