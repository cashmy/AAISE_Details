# LAB 4 FULL-ENGLISH ALGORITHM WALKTHROUGHS

**Week 4 - Searching and Sorting**

---

# Purpose

This support artifact gives full-English examples of how to think through the
Lab 4 data set options before writing search code or creating trace tables.

These are not finished submissions. They are thinking scaffolds.

Use them to understand how linear search and binary search behave differently,
and why binary search depends on sorted data.

---

# How To Use This Artifact

For your chosen data set:

1. Read the matching walkthrough.
2. Create at least 12 values.
3. Decide what value you will search for.
4. Trace linear search on one example.
5. Trace binary search on sorted data.
6. Try binary search on unsorted data and explain why it is unreliable.
7. Build your test table and trace evidence.

Do not copy the wording directly as your final answer. Your submitted work must
include your own data set, search logic, tests, trace table, precondition
explanation, and AI-use note if applicable.

---

# What Makes This A Search Algorithm Lab?

A search algorithm tries to locate a target value.

Linear search checks one value at a time. It does not require the data to be
sorted.

Binary search checks the middle value and removes half of the possible search
space each step. It only works when the data is sorted in the same order the
algorithm expects.

The main idea is not simply "binary search is faster." The main idea is:
binary search is valid only when its precondition is true.

---

# Scenario 1 - Product IDs

First, create a list of product IDs. Each ID should be searchable as a value,
such as `P100`, `P205`, or `P410`.

For linear search, start at the first product ID. Compare it to the target. If
it matches, return the position. If it does not match, move to the next product
ID. Continue until the target is found or the list ends.

For binary search, sort the product IDs first. Check the middle ID. If the
middle ID is the target, stop. If the middle ID is lower than the target, search
the upper half. If it is higher than the target, search the lower half.

Then try binary search on the unsorted product ID list. The algorithm may
discard the wrong half because the IDs are not arranged in order.

Questions to guide your trace:

- Which product ID appears near the beginning?
- Which product ID appears near the end?
- Which product ID is missing?
- What sorted order did binary search depend on?

---

# Scenario 2 - Student Usernames

First, create a list of student usernames. Each username should be treated as a
searchable text value.

For linear search, check usernames one at a time. This works even if the
usernames are not sorted.

For binary search, create a sorted version of the username list. Each step
checks the middle username and decides whether the target should be before or
after it alphabetically.

If binary search is attempted on the unsorted list, the alphabetical decision
does not reliably tell the algorithm which half to keep.

Questions to guide your trace:

- Are all usernames using consistent capitalization?
- What happens if the searched username is not in the list?
- Which test proves the found-near-beginning case?
- Which test proves the found-near-end case?

---

# Scenario 3 - Ticket Numbers

First, create a list of ticket numbers. These may be numbers or text labels
such as `T-1004`.

For linear search, check each ticket number until the target ticket is found or
the list ends.

For binary search, sort the ticket numbers first. Then check the middle ticket,
compare it to the target, and keep only the half where the target could still
exist.

If the tickets are unsorted, binary search may move left or right for the wrong
reason.

Questions to guide your trace:

- Are ticket numbers numeric or text?
- Does the sorted order match the way your code compares them?
- What ticket number is intentionally missing?
- How will your trace show low, high, and mid changing?

---

# Scenario 4 - Course Codes

First, create a list of course codes. Each course code may include department
or program numbers, such as `10-152-119`.

For linear search, check each course code one at a time until the target is
found or the list ends.

For binary search, sort the course codes first. The sorted list must match the
comparison method used by the code. If the course codes are strings, the order
may be text-based rather than numeric in the way a human expects.

Then compare what happens when binary search is attempted on the original
unsorted list.

Questions to guide your trace:

- Are course codes stored as strings?
- Does the sorted order look the way you expected?
- Which target is found?
- Which target is not found?

---

# Scenario 5 - Event Attendee Names

First, create a list of attendee names.

For linear search, check each name in the order it appears. This works for an
arrival list, registration list, or any other unsorted order.

For binary search, sort the names alphabetically first. The algorithm then uses
alphabetical order to decide whether to search the earlier or later half.

If binary search is used on the unsorted attendee list, the middle-name
comparison no longer gives reliable information about where the target might
be.

Questions to guide your trace:

- How will you handle capitalization?
- What happens if two people have the same last name?
- Which attendee is found near the beginning?
- Which attendee is not found?

---

# Your Turn

After reading the walkthrough for your data set, build your own list, tests,
and trace evidence.

Your next step is not to memorize binary search. Your next step is to prove
that you understand when the search logic is valid.
