"""
Assignment 3 Success Example: Loops and Repetition

This example uses a loop to calculate total reading minutes for a week.
The program repeats over a fixed list and stops when all values are processed.
"""


daily_reading_minutes = [20, 35, 30, 0, 45]

total_minutes = 0

print("Reading minutes by study session:")

for minutes in daily_reading_minutes:
    print("-", minutes, "minutes")
    total_minutes = total_minutes + minutes

average_minutes = total_minutes / len(daily_reading_minutes)

print("Total minutes:", total_minutes)
print("Average minutes:", average_minutes)

if total_minutes >= 120:
    print("Goal met: at least 120 minutes of reading.")
else:
    print("Goal not met yet: add more reading time.")

