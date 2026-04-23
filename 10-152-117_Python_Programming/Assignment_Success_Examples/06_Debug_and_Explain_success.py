"""
Assignment 6 Success Example: Debug and Explain

This is the corrected version of a small checkout program.

The original broken version had two issues:
1. The discount was added instead of subtracted.
2. Shipping was added inside the item loop, so it was added once per item.
"""


items = [
    {"name": "flash drive", "price": 8.00, "quantity": 2},
    {"name": "notebook", "price": 3.50, "quantity": 3},
    {"name": "binder", "price": 5.25, "quantity": 1},
]

discount_rate = 0.10
shipping = 4.99


def calculate_subtotal(cart_items):
    subtotal = 0

    for item in cart_items:
        line_total = item["price"] * item["quantity"]
        subtotal = subtotal + line_total

    return subtotal


def calculate_final_total(subtotal, discount_rate, shipping_cost):
    discount = subtotal * discount_rate
    return subtotal - discount + shipping_cost


subtotal = calculate_subtotal(items)
final_total = calculate_final_total(subtotal, discount_rate, shipping)

print("Subtotal:", subtotal)
print("Discount rate:", discount_rate)
print("Shipping:", shipping)
print("Final total:", final_total)

print("\nExpected final total:", 33.565)
print("Check:", final_total == 33.565)

