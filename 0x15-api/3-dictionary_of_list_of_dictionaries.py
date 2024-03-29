#!/usr/bin/python3
"""This script retrieves TODO list information for all employees from
the JSONPlaceholder API and writes the data into a JSON file."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(base_url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
