#!/usr/bin/python3
''' script that returns information about a TODO list progress
    for a given employee ID'''

import requests
import sys

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{url}/users/{sys.argv[1]}'
    userId_url = f'{url}/todos?userId={sys.argv[1]}'
    response = requests.get(user_url)
    response2 = requests.get(userId_url)
    EMPLOYEE_NAME = response.json().get('name')
    NUMBER_OF_DONE_TASKS = len([task for task in response2.json()
                                if task.get('completed')])

    TOTAL_NUMBER_OF_TASKS = len(response2.json())
    TASK_TITLE = [task for task in response2.json() if task.get('completed')]
    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in TASK_TITLE:
        print(f'\t{task.get("title")}')
