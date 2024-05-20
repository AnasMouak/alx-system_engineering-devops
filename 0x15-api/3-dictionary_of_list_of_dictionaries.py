#!/usr/bin/python3
''' export data in the json format.'''

import json
import requests

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{url}/users'
    response = requests.get(user_url)
    data = {}
    for task in response.json():
        userId_url = f'{url}/todos?userId={task.get("id")}'
        response2 = requests.get(userId_url)
        user_id = task.get('id')
        username = task.get('username')
        list_userId = response2.json()

        data[user_id] = []
        for task in list_userId:
            d_data = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            data[user_id].append(d_data)

    with open(f'todo_all_employees.json', mode='w', newline='') as file:
        json_writer = json.dump(data, file)
