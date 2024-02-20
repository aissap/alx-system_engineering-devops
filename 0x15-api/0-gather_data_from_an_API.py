#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todo_data = requests.get(base_url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = [t.get("title") for t in todo_data if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todo_data)))
    [print("\t {}".format(c)) for c in completed_tasks]
