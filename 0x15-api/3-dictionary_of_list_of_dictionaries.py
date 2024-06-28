#!/usr/bin/python3
"""Exports the task list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            e.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": e.get("username")
            } for task in requests.get(url + "todos",
                                       params={"userId": e.get("id")}).json()]
            for e in employees}, jsonfile)
