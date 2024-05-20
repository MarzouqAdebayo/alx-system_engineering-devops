#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv

if __name__ = "__main__":
    user_id = argv[1]
    endpoint = 'https://jsonplaceholder.typicode.com'
    todo_path = f'endpoint/user/{user_id}/todos'
    user_path = f'endpoint/users/{user_id}'
    todo_path_output = get(todo_path).json()
    user_path_output = get(todo_user).json()

    total_todo = len(todo_path_output)
    completed_todo = len([todo for todo in todo_path_output
                         if todo.get("completed")])
    user_name = user_path_output.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, completed_todo, total_todo))
    for todo in todo_path_output:
        if (todo.get("completed")):
            print(f'\t {todo.get("title")}')
