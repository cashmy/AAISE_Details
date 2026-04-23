"""
Assignment 11 Success Example: API Data Fetcher (live approved API)

This example uses JSONPlaceholder, which is on the approved API list.

It retrieves user data, selects a few meaningful values, and prints a small
report instead of dumping raw JSON.

Run note:
This example requires network access.
"""

import json
from urllib.request import urlopen


API_URL = "https://jsonplaceholder.typicode.com/users"


with urlopen(API_URL) as response:
    users = json.load(response)

print("Approved API source: JSONPlaceholder")
print("Selected user summary:")

for user in users[:3]:
    print(
        user["name"],
        "-",
        user["email"],
        "-",
        user["address"]["city"],
    )

print("\nTotal users retrieved:", len(users))

