#!/usr/bin/python3
""" This script uses a rest API to request data and
displays it in readable format """
import json
from sys import argv
from urllib.request import urlopen, Request


if __name__ == "__main__":
    base_url_todo = "https://jsonplaceholder.typicode.com/users/"
    base_url_name = "https://jsonplaceholder.typicode.com/todos?userId="
    id = argv[1]

    url_1 = f"{base_url_todo}{id}"
    url_2 = f"{base_url_name}{id}"

    req_1 = Request(url_1)
    with urlopen(req_1) as response:
        data = json.loads(response.read().decode('utf-8'))
        username = data.get('username')

    req_2 = Request(url_2)
    with urlopen(req_2) as response:
        data = json.loads(response.read().decode('utf-8'))
    user = {
            f"{id}": [
                {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                } for task in data
            ]
        }
    json_file = f"{id}.json"
    with open(json_file, 'w', encoding="utf-8") as json_file_obj:
        json.dump(user, json_file_obj)
