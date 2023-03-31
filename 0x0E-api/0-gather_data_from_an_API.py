#!/usr/bin/python3
"""gets employee information about their TO DO list"""

import requests
from sys import argv, exit


def get_employee_todo_progress(employee_id):
    """gets employee progress via their employee ID"""
    baseurl = "https://jsonplaceholder.typicode.com"

    user_resp = requests.get("{}/users/{}"
                                 .format(baseurl, employee_id))
    userdata = user_resp.json()

    if 'name' not in userdata:
        print("Invalid employee ID")
        return

    todo_resp = requests.get("{}/users/{}/todos"
                             .format(baseurl, employee_id))
    tododata = todo_resp.json()

    completedtasks = [task for task in tododata if task["completed"]]
    totaltasks = len(tododata)

    print("Employee {} is done with tasks({}/{}): "
          .format(userdata['name'], len(completedtasks), totaltasks))

    for task in completedtasks:
        print("\t", task["title"])


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        exit(1)

    get_employee_todo_progress(employee_id)
