#!/usr/bin/python3
"""Script to export data in the CSV format."""
import requests
from sys import argv
import csv

API_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    # User information
    user_response = requests.get(f"{API_URL}/users/{argv[1]}")
    user_data = user_response.json()

    # Todo list for the given user
    todo_response = requests.get(f"{API_URL}/todos?userId={argv[1]}")
    todo_data = todo_response.json()

    # Prepare the CSV file
    user_id = user_data['id']
    username = user_data['username']
    csv_file = f"{user_id}.csv"

    with open(csv_file, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            task_completed = task['completed']
            task_titl = task['title']
            csv_writer.writerow([user_id, username, task_completed, task_titl])

    print(f"Data has been exported to {csv_file}")
