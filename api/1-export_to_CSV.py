#!/usr/bin/python3
"""Script to export data in the CSV format."""
import csv
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    USER_ID = argv[1]

    # User information
    user_response = requests.get(f"{API_URL}/users/{USER_ID}").json()

    # Todo list for the given user
    todo_response = requests.get(f"{API_URL}/todos?userId={USER_ID}").json()

    # Write to CSV file
    with open(f"{USER_ID}.csv", mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todo_response:
            writer.writerow([
                user_response['id'],
                user_response['username'],
                task['completed'],
                task['title']
            ])

    print(f"Data has been exported to {USER_ID}.csv")
