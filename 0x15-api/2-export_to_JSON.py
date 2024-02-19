#!/usr/bin/python3

"""
Python script.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    ans = get('https://jsonplaceholder.typicode.com/todos/')
    da = ans.json()

    roww = []
    ans2 = get('https://jsonplaceholder.typicode.com/users')
    da2 = ans2.json()

    for k in da2:
        if k['id'] == int(argv[1]):
            name = k['username']
            idd = k['id']

    roww = []

    for j in da:

        new = {}

        if j['userId'] == int(argv[1]):
            new['username'] = name
            new['task'] = j['title']
            new['completed'] = j['completed']
            roww.append(new)

    final = {}
    final[idd] = roww
    json_obj = json.dumps(final)

    with open(argv[1] + ".json",  "w") as x:
        x.write(json_obj)
