#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""
from json import dump
from requests import get
from sys import argv


def get_tasks_for_user(user):
    endpoint = 'https://jsonplaceholder.typicode.com'
    todo_path = f'{endpoint}/user/{user.get("id")}/todos'
    todo_path_output = get(todo_path).json()

    user_name = user.get("username")
    user_tasks_list = []
    for item in todo_path_output:
        user_tasks_list.append({"username": user_name,
                                "task": item.get("title"),
                                "completed": item.get("completed")}),
    return user_tasks_list


if __name__ == "__main__":
    endpoint = 'https://jsonplaceholder.typicode.com'
    users_path = f'{endpoint}/users/'
    users_path_output = get(users_path).json()

    users_tasks_object = {}
    for user in users_path_output:
        users_tasks_object.update(
            {user.get("id"): get_tasks_for_user(user)})
    with open("todo_all_employees.json", 'w') as f:
        dump(users_tasks_object, f)
