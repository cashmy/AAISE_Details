"""
Assignment 9 Success Example: Structured Data Reader

This example reads a CSV file and creates a useful summary.
"""

import csv
from pathlib import Path


input_file = Path(__file__).with_name("09_course_progress.csv")

total_minutes = 0
completed_count = 0
python_tasks = []

with input_file.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        minutes = int(row["minutes"])
        total_minutes += minutes

        if row["completed"] == "yes":
            completed_count += 1

        if row["course"] == "Python Programming":
            python_tasks.append(row["task"])

print("Total minutes studied:", total_minutes)
print("Completed tasks:", completed_count)
print("Python tasks:")

for task in python_tasks:
    print("-", task)

