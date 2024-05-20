#!/usr/bin/python3
''' export data in the json format.'''

import json
import requests
import sys

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{url}/users/{sys.argv[1]}'
    userId_url = f'{url}/todos?userId={sys.argv[1]}'
    response = requests.get(user_url)
    response2 = requests.get(userId_url)
    user_id = response.json().get('id')
    username = response.json().get('username')
    list_userId = response2.json()
    data = {str(user_id): []}
    for task in list_userId:
        d_data = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        data[str(user_id)].append(d_data)

    with open(f'{sys.argv[1]}.json', mode='w') as file:
        json_writer = json.dump(data, file)
