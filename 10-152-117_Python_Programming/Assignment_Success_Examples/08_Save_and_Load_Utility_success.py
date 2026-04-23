"""
Assignment 8 Success Example: Save and Load Utility

This example saves study tasks to JSON, loads them again, and handles a
missing-file case in a beginner-readable way.
"""

import json
from pathlib import Path


def save_tasks(task_list, output_file):
    with output_file.open("w", encoding="utf-8") as file:
        json.dump(task_list, file, indent=2)


def load_tasks(input_file):
    try:
        with input_file.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("The file was not found:", input_file.name)
        return []


tasks = [
    {"course": "Python Programming", "task": "Practice file handling", "minutes": 30},
    {"course": "Algorithms", "task": "Review tree notes", "minutes": 25},
]

data_file = Path(__file__).with_name("08_saved_tasks.json")

save_tasks(tasks, data_file)
print("Saved tasks to:", data_file.name)

loaded_tasks = load_tasks(data_file)

print("\nLoaded tasks:")
for task in loaded_tasks:
    print(task["course"], "-", task["task"], "-", task["minutes"], "minutes")

