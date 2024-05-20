#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""
from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    endpoint = 'https://jsonplaceholder.typicode.com'
    todo_path = f'endpoint/user/{user_id}/todos'
    user_path = f'endpoint/users/{user_id}'
    todo_path_output = get(todo_path).json()
    user_path_output = get(todo_user).json()

    user_id = user_path_output.get("id")
    user_name = user_path_output.get("name")
    user_tasks_list = []
    for item in todo_path_output:
        user_task_object = {}
        user_task_object.update({"user_ID": user_id,
                                 "username": user_name,
                                 "completed": item.get("completed"),
                                 "task": todo.get("title")})
        user_tasks_list.append(user_tasks_object)
    with open("{}.csv".format(user_id), 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(user_tasks_list)
