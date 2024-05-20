#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""
from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    endpoint = 'https://jsonplaceholder.typicode.com'
    todo_path = f'{endpoint}/user/{user_id}/todos'
    user_path = f'{endpoint}/users/{user_id}'
    todo_path_output = get(todo_path).json()
    user_path_output = get(user_path).json()

    user_id = user_path_output.get("id")
    user_name = user_path_output.get("username")
    user_tasks_list = []
    for item in todo_path_output:
        user_tasks_list.append({"task": item.get("title"),
                                "completed": item.get("completed"),
                                "username": user_name})
    with open("{}.json".format(user_id), 'w') as f:
        dump({user_id: user_tasks_list}, f)
