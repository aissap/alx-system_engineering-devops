#!/usr/bin/python3
import requests
"""
Recursively queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""


def recurse(subreddit, list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])
        if children:
            for child in children:
               list.append(child["data"]["title"])
            after = data.get("after")
            if after:
                return recurse(subreddit, list, after)
            return list
        else:
            return list
    else:
        return None


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    r = recurse(subreddit)
    if r is not None:
        print(len(r))
    else:
        print("None")
