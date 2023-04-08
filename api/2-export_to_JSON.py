#!/usr/bin/python3
"""Script to export data in the JSON format."""
import json
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    USER_ID = argv[1]

    # User information
    user_response = requests.get(f"{API_URL}/users/{USER_ID}").json()

    # Todo list for the given user
    todo_response = requests.get(f"{API_URL}/todos?userId={USER_ID}").json()

    # Prepare data for export
    data = {
        USER_ID: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_response['username']
            }
            for task in todo_response
        ]
    }

    # Write to JSON file
    with open(f"{USER_ID}.json", mode='w') as json_file:
        json.dump(data, json_file)

    print(f"Data has been exported to {USER_ID}.json")
