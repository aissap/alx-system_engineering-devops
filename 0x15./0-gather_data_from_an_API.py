#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_response = requests.get(base_url + "users/{}".format(employee_id))

    todo_response = requests.get(base_url + "todos", params={"userId": employee_id})

    user_data = user_response.json()
    todo_data = todo_response.json()

    completed_tasks = [task.get("title") for task in todo_data if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(completed_tasks), len(todo_data)))

    for task_title in completed_tasks:
        print("\t{}".format(task_title))
