#!/usr/bin/python3
"""extends the script from 0 to export data in CSV"""

import json
import requests
from sys import argv, exit


def get_employee_data(employee_id):
    """gets employee progress via their employee ID"""
    baseurl = "https://jsonplaceholder.typicode.com"

    user_resp = requests.get("{}/users/{}"
                             .format(baseurl, employee_id))
    userdata = user_resp.json()

    if 'name' not in userdata:
        print("Invalid employee ID")
        return None, None

    todoresp = requests.get("{}/users/{}/todos"
                            .format(baseurl, employee_id))

    tododata = todoresp.json()

    return userdata, tododata


def export_to_json(employee_id, userdata, tododata):
    fn = "{}.json".format(employee_id)

    taskdata = []
    for task in tododata:
        taskdata.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": userdata["username"]
            })

    jsondata = {employee_id: taskdata}

    with open(fn, "w") as jsonfile:
        json.dump(jsondata, jsonfile)

    print("Data exported to {}".format(fn))


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        exit(1)

    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        exit(1)

    userdata, tododata = get_employee_data(employee_id)

    if userdata and tododata:
        export_to_json(employee_id, userdata, tododata)
