#!/usr/bin/python3
"""extends the script from 0 to export data in CSV"""

import csv
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


def export_to_csv(employee_id, userdata, tododata):
    """exports to CSV format"""
    fn = "{}.csv".format(employee_id)

    with open(fn, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in tododata:
            csvwriter.writerow([employee_id, userdata["username"],
                                task["completed"], task["title"]])

    print("Data exported to {}".format(fn))


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        exit(1)

    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        exit(1)

    userdata, tododata = get_employee_data(employee_id)
    
    if userdata and tododata:
        export_to_csv(employee_id, userdata, tododata)