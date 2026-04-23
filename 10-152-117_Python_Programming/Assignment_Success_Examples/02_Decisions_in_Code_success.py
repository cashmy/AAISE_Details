"""
Assignment 2 Success Example: Decisions in Code

This example uses conditionals to create a library late-fee message.
Change days_late to test different branches.
"""


book_title = "Python Basics"
days_late = 5

print("Book:", book_title)
print("Days late:", days_late)

if days_late == 0:
    fee = 0.00
    message = "No late fee. Thank you for returning the book on time."
elif days_late <= 3:
    fee = 1.00
    message = "Small late fee. Please return future books a little sooner."
elif days_late <= 7:
    fee = 3.00
    message = "Moderate late fee. Please check your due dates carefully."
else:
    fee = 5.00
    message = "Large late fee. Please contact the library desk."

print("Fee:", fee)
print(message)

