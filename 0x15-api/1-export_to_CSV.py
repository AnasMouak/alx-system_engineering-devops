#!/usr/bin/python3
''' export data in the CSV format.'''

import requests
import sys
import csv

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{url}/users/{sys.argv[1]}'
    userId_url = f'{url}/todos?userId={sys.argv[1]}'
    response = requests.get(user_url)
    response2 = requests.get(userId_url)
    user_id = response.json().get('id')
    username = response.json().get('username')
    list_userId = [task for task in response2.json()]

    with open('USER_ID.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        for task in list_userId:
            csv_writer.writerow([f'{user_id}', f'{username}',
                                 f'{task.get("completed")}',
                                 f'{task.get("title")}'])
