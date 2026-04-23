# Assignment 6 Success Notes - Debug and Explain

## Issue 1

The discount was being added to the subtotal instead of subtracted.

## Evidence Used

The expected-vs-actual comparison showed that the final total was too high. A labeled print statement for the discount amount made it clear that the discount was being calculated, but then used in the wrong direction.

Example evidence:

```text
Subtotal: 35.25
Discount: 3.525
Broken total before shipping: 38.775
```

## Fix

The formula was changed from:

```python
subtotal + discount
```

to:

```python
subtotal - discount
```

## Issue 2

Shipping was being added inside the loop that processed each item.

## Evidence Used

A labeled print statement inside the loop showed that shipping was being added more than once. Shipping should be added once to the final order, not once for every item.

## Fix

Shipping was moved out of the loop and added after the subtotal and discount were calculated.

## How I Know the Fix Worked

The corrected program now prints:

```text
Final total: 33.565
Expected final total: 33.565
Check: True
```

This confirms that the program output matches the expected result.

