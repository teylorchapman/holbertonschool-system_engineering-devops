#!/usr/bin/python3
"""extends the script from 0 to export data in CSV"""
import hashlib
import json
import requests


def get_all_employees():
    """gathers employees"""
    baseurl = "https://jsonplaceholder.typicode.com"

    userresp = requests.get("{}/users".format(baseurl))
    userdata = userresp.json()

    return userdata


def get_employee_tasks(user_id, username):
    """gathers employee tasks"""
    baseurl = "https://jsonplaceholder.typicode.com"

    todoresp = requests.get("{}/users/{}/todos"
                            .format(baseurl, user_id))
    tododata = todoresp.json()

    taskdata = []
    for task in tododata:
        taskdata.append({
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        })

    return taskdata


def export_to_json(all_employees_data):
    """exporting info to json"""
    fn = "todo_all_employees.json"

    alltasks = {}
    for employee in all_employees_data:
        user_id = employee["id"]
        username = employee["username"]
        tasks = get_employee_tasks(user_id, username)
        alltasks[user_id] = tasks

    with open(fn, "w") as jsonfile:
        json.dump(alltasks, jsonfile)

    print("Data exported to {}".format(fn))


if __name__ == "__main__":
    all_employees_data = get_all_employees()
    export_to_json(all_employees_data)
