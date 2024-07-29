#!/usr/bin/python3
"""Exports the task list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    employee_name = employee.get("username")
    tasks = requests.get(url + "todos", params={"userId": employee_id}).json()

    with open("{}.json".format(employee_id), "w") as file:
        json.dump({employee_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name
            } for task in tasks]}, file)
