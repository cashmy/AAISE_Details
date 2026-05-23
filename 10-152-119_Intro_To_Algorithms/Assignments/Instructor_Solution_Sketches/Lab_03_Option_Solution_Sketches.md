# LAB 03 OPTION SOLUTION SKETCHES

**Lab:** Data Structure Choice  
**Instructor Use:** grading calibration, alternate examples, quick response support

---

# Instructor Boundary

These sketches are not student-facing walkthroughs. They assume the student has
already selected a scenario and is responsible for their own code, comparison
table, and recommendation.

For Lab 03, a strong submission should make the access pattern visible. The
student does not need the most advanced structure. They need to explain why the
selected structures fit or do not fit the operations.

---

# Common Required Evidence

Every option should include:

- short problem statement
- two data structures
- equivalent or comparable data in both structures
- at least three operations, such as add, lookup, update, remove, display
- comparison table
- recommendation
- AI-use note if applicable

Suggested comparison table:

| Operation | Structure A | Structure B | Better Fit | Why? |
| --- | --- | --- | --- | --- |

---

# Option 1 - Inventory Lookup

## Viable Framing

Manage a small inventory where each item has an item ID, name, quantity, and
price.

## Recommended Pairing

- list of dictionaries
- dictionary keyed by item ID

## Expected Operations

- add item
- look up item by ID
- update quantity
- display all items

## Expected Recommendation

Dictionary keyed by item ID is usually the better fit if lookup and quantity
updates are common. List of dictionaries is acceptable but usually requires
scanning.

## Edge Cases

- item ID not found
- duplicate item ID
- quantity update that produces zero

## Grading Watch-Fors

- Student claims dictionary is better without naming the item-ID lookup pattern.
- Student stores different data in each structure, making comparison unfair.
- Student compares only display behavior and ignores lookup/update.

## Runnable Expansion Note

Create six inventory records. Use `SKU101` through `SKU106`. Demonstrate lookup
for one existing SKU, one missing SKU, and one quantity update.

---

# Option 2 - Student Score Summary

## Viable Framing

Track student scores and summarize or update scores for one student.

## Recommended Pairing

- list of student dictionaries
- dictionary keyed by student ID or username

## Expected Operations

- add score
- calculate average
- look up one student
- display all summaries

## Expected Recommendation

Dictionary keyed by student ID is usually better for lookup and score updates.
List of dictionaries remains readable for displaying all students.

## Edge Cases

- student has no scores
- student ID not found
- score outside expected range

## Grading Watch-Fors

- Student uses names as keys without considering duplicate names.
- Student calculates averages but does not compare structures.
- Student chooses a structure based only on familiarity.

## Runnable Expansion Note

Use at least five students. Include one student with an empty score list to
force an edge-case explanation.

---

# Option 3 - Help Desk Ticket Status

## Viable Framing

Track help desk tickets with ticket number, status, priority, and assigned
technician.

## Recommended Pairing

- list of ticket dictionaries
- dictionary keyed by ticket number

## Expected Operations

- add ticket
- look up ticket by number
- update ticket status
- list open tickets

## Expected Recommendation

Dictionary keyed by ticket number is usually better for direct lookup and
status update. List may be better if arrival order is the main concern.

## Edge Cases

- ticket number not found
- invalid status
- duplicate ticket number

## Grading Watch-Fors

- Student does not define allowed statuses.
- Student updates status in one structure but not the other.
- Student ignores the difference between listing all tickets and finding one.

## Runnable Expansion Note

Use statuses such as `open`, `waiting`, `resolved`, and `closed`. Include one
status update from `open` to `resolved`.

---

# Option 4 - Menu Item Search

## Viable Framing

Manage a small menu and support item search, category filtering, or dietary-tag
lookup.

## Recommended Pairing

- list of menu item dictionaries
- dictionary keyed by item name or ID
- optional set of tags inside each item

## Expected Operations

- search by item name
- filter by category
- check dietary tag
- update price

## Expected Recommendation

If exact item lookup is the main access pattern, dictionary is usually better.
If filtering through categories or tags is the main behavior, list traversal
with sets for tags may be easier to explain.

## Edge Cases

- no matching item
- duplicate item names
- missing dietary tag

## Grading Watch-Fors

- Student adds sets but does not explain membership checking.
- Student overstates dictionary benefits for category filtering.
- Student ignores what the user is actually searching by.

## Runnable Expansion Note

Use six menu items with categories and tag sets. Demonstrate exact lookup and
tag membership.

---

# Option 5 - Simple Contact Lookup

## Viable Framing

Store contacts and support lookup or update by name, email, or contact ID.

## Recommended Pairing

- list of dictionaries
- dictionary of dictionaries

## Expected Operations

- add contact
- look up contact
- update phone or email
- display all contacts

## Expected Recommendation

Dictionary of dictionaries is usually better when the key is stable and lookup
is the main access pattern. List of dictionaries is still readable and may
preserve entry order.

## Edge Cases

- duplicate contact names
- missing contact
- contact has incomplete details

## Grading Watch-Fors

- Student uses name as unique key without noting duplicate-name risk.
- Student implements only one representation.
- Student recommends dictionary but does not compare display behavior.

## Runnable Expansion Note

The existing Lab 03 success package already implements this option.

---

# Option 6 - Event Registration List

## Viable Framing

Track event registration, prevent duplicates, update registration status, and
display the roster.

## Recommended Pairing

- list of registrant dictionaries
- set of registered emails
- dictionary keyed by email

## Expected Operations

- add registrant
- check duplicate registration
- update payment or attendance status
- display roster

## Expected Recommendation

Set is best for membership-only duplicate checks. Dictionary keyed by email is
better when the system also needs full registrant details. List is useful for
arrival order or roster display.

## Edge Cases

- duplicate email
- waitlist status
- cancellation or removal

## Grading Watch-Fors

- Student compares list to set but then needs details the set cannot store.
- Student does not clarify whether order matters.
- Student omits duplicate-prevention evidence.

## Runnable Expansion Note

Use six registrants. Include one attempted duplicate email and one status
change from `registered` to `waitlist` or `cancelled`.
