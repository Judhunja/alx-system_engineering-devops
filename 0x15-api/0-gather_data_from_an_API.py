#!/usr/bin/python3
""" This script uses a rest API to request data and
displays it in readable format """
from sys import argv
from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json


if __name__ == "__main__":
    base_url_todo = "https://jsonplaceholder.typicode.com/users/"
    base_url_name = "https://jsonplaceholder.typicode.com/todos?userId="
    id = argv[1]

    url_1 = f"{base_url_todo}{id}"
    url_2 = f"{base_url_name}{id}"

    req_1 = Request(url_1)
    with urlopen(req_1) as response:
        data = json.loads(response.read().decode('utf-8'))
        name = data.get('name')

    req_2 = Request(url_2)
    with urlopen(req_2) as response:
        data = json.loads(response.read().decode('utf-8'))

        completed = 0
        not_done = 0
        task_titles = []

        for task in data:
            if task.get('completed', False):
                completed += 1
            else:
                not_done += 1
            task_titles.append(task.get('title'))

        total = completed + not_done

    print(f"Employee {name} is done with tasks({completed}/{total}):")

    for task in task_titles:
        print(f"     {task}")
