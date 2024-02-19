#!/usr/bin/python3

"""
Python script that exports
"""

from requests import get
import json

if __name__ == "__main__":
    ans = get('https://jsonplaceholder.typicode.com/todos/')
    da = ans.json()

    roww = []
    ans2 = get('https://jsonplaceholder.typicode.com/users')
    da2 = ans2.json()

    new = {}

    for k in da2:

        roww = []
        for j in da:

            new2 = {}

            if k['id'] == j['userId']:

                new2['username'] = k['username']
                new2['task'] = j['title']
                new2['completed'] = j['completed']
                roww.append(new2)

        new[k['id']] = roww

    with open("todo_all_employees.json",  "w") as x:

        json_obj = json.dumps(new)
        x.write(json_obj)
