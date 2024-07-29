#!/usr/bin/python3
"""Returns task list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    com_ts = [ts.get("title") for ts in tasks if ts.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(com_ts), len(tasks)))
    [print("\t {}".format(ct)) for ct in com_ts]
