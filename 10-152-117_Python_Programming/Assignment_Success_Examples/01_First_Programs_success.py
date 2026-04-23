"""
Assignment 1 Success Example: First Programs

This example shows three very small programs in one file:
1. a personalized message
2. a unit conversion
3. a total-cost estimate

It uses assigned variables instead of input() so the example can run without
interactive typing.
"""


print("PROGRAM 1: PERSONALIZED MESSAGE")

student_name = "Jordan"
course_name = "Python Programming"
weekly_goal = "practice for 30 minutes after class"

message = student_name + " is taking " + course_name + "."
goal_message = "This week's goal is to " + weekly_goal + "."

print(message)
print(goal_message)


print("\nPROGRAM 2: UNIT CONVERSION")

miles_walked = 2.5
kilometers_per_mile = 1.60934
kilometers_walked = miles_walked * kilometers_per_mile

print("Miles walked:", miles_walked)
print("Kilometers walked:", kilometers_walked)


print("\nPROGRAM 3: TOTAL-COST ESTIMATE")

notebook_price = 3.49
notebook_quantity = 4
tax_rate = 0.055

subtotal = notebook_price * notebook_quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Notebook price:", notebook_price)
print("Quantity:", notebook_quantity)
print("Subtotal:", subtotal)
print("Tax:", tax)
print("Total:", total)

