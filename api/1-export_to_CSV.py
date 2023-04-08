#!/usr/bin/python3
"""Script to export data in the CSV format."""
import requests
import csv
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    # User information
    user_response = requests.get(f"{API_URL}/users/{argv[1]}")
    user_data = user_response.json()

    # Todo list for the given user
    todo_response = requests.get(f"{API_URL}/todos?userId={argv[1]}")
    todo_data = todo_response.json()

    # Filter completed tasks
    task_completed = [task for task in todo_data if task['completed']]

    # Write to CSV file
    with open(f"{argv[1]}.csv", mode='w') as csv_file:
        writer = csv.writer(csv_file)

        for task in todo_data:
            writer.writerow({
                user_data['id'],
                user_data['username'],
                task['completed'],
                task['title']
            })

    print(f"Data has been exported to {argv[1]}.csv")
