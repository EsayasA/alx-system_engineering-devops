#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    res = get('https://jsonplaceholder.typicode.com/todos/')
    information = res.json()
    completed = 0
    total = 0
    tasks = []
    response = get('https://jsonplaceholder.typicode.com/users')
    data = response.json()

    for k in data:
        if k.get('id') == int(argv[1]):
            person = k.get('name')

    for k in information:
        if k.get('userId') == int(argv[1]):
            total += 1

            if k.get('completed') is True:
                completed += 1
                tasks.append(k.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(person, completed,
                                                          total))

    for i in tasks:
        print("\t {}".format(i))
