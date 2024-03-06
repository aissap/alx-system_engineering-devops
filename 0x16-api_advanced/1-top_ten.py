#!/usr/bin/python3
import requests
"""Queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])
        for post in data:
            print(post.get("data", {}).get("title"))
    else:
        print(None)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
