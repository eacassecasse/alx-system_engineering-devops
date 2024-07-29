#!/usr/bin/python3
"""Exports the task list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    employee_name = employee.get("username")
    tasks = requests.get(url + "todos", params={"userId": employee_id}).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [wr.writerow(
            [employee_id, employee_name, ts.get("completed"), ts.get("title")]
         ) for ts in tasks]
