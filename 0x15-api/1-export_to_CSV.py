#!/usr/bin/python3
""" This script uses a rest API to request data and
displays it in readable format """
import csv
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

        csvfile = f"{id}.csv"

        with open(csvfile, 'w', encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            for task in data:
                task_status = task.get('completed')
                task_title = task.get('title')
                csv_writer.writerow([id, username, task_status, task_title])
