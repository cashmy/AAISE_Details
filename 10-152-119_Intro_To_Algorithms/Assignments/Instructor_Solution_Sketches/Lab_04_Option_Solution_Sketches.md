# LAB 04 OPTION SOLUTION SKETCHES

**Lab:** Search and Sort Behavior  
**Instructor Use:** grading calibration, alternate examples, quick response support

---

# Instructor Boundary

These sketches are instructor-only calibration notes. They provide sample
expectations for the allowed data-set options without replacing the student's
own trace work.

For Lab 04, the central grading question is whether the student understands
that binary search is valid only when the sorted-data precondition is true.

---

# Common Required Evidence

Every option should include:

- at least 12 values
- linear search
- binary search
- found near beginning
- found near end
- not found
- binary search attempted on unsorted data
- at least one trace table
- explanation of sorted-data precondition

Suggested binary trace table:

| Step | Low | High | Mid | Mid Value | Decision |
| --- | --- | --- | --- | --- | --- |

---

# Option 1 - Product IDs

## Viable Data

Use product IDs such as `P100`, `P105`, `P110`, through `P155`, shuffled for
the unsorted list.

## Expected Tests

- found near beginning: `P105`
- found near end: `P150`
- not found: `P999`
- unsorted binary attempt: target that linear search can find but binary search
  misses or reaches through invalid reasoning

## Expected Explanation

Linear search is safe on any order because it checks each product ID. Binary
search requires the product IDs to be sorted according to the same comparison
rules used by the code.

## Grading Watch-Fors

- Student sorts the original list before the unsorted-binary test.
- Student uses numeric-looking strings and misreads text sort order.
- Student says binary search is "better" without conditions.

---

# Option 2 - Student Usernames

## Viable Data

Use usernames such as `acarter`, `bnguyen`, `cmiller`, `dpatel`, and so on.
Keep capitalization consistent.

## Expected Tests

- found near beginning: first or second sorted username
- found near end: one of the last sorted usernames
- not found: username not in the list
- unsorted binary attempt: run binary search on the original shuffled list

## Expected Explanation

Binary search uses alphabetical order. If capitalization is inconsistent, the
actual comparison order may differ from what students expect.

## Grading Watch-Fors

- Student mixes uppercase and lowercase without explaining order.
- Student accidentally tests only targets that binary search finds by luck.
- Student omits not-found behavior.

---

# Option 3 - Ticket Numbers

## Viable Data

Use ticket numbers such as `T-1001` through `T-1012`, shuffled for unsorted
data.

## Expected Tests

- found near beginning: `T-1002`
- found near end: `T-1011`
- not found: `T-9999`
- unsorted binary attempt with a ticket that is present

## Expected Explanation

Ticket numbers are common lookup keys. Linear search checks them one by one.
Binary search can be efficient only after the ticket numbers are sorted.

## Grading Watch-Fors

- Student compares ticket labels inconsistently.
- Student reports only final result and no trace.
- Student hides precondition failure by always searching the sorted copy.

---

# Option 4 - Course Codes

## Viable Data

Use course codes such as `10-152-117`, `10-152-118`, `10-152-119`,
`10-152-120`, and additional plausible codes.

## Expected Tests

- found near beginning: a low sorted course code
- found near end: a high sorted course code
- not found: `10-152-999`
- unsorted binary attempt on shuffled course list

## Expected Explanation

Course codes should usually be treated as strings unless the student explicitly
parses their parts. Binary search depends on the sorted string order or parsed
numeric order being clear.

## Grading Watch-Fors

- Student assumes human course order without checking actual sort order.
- Student does not explain string comparison.
- Student has fewer than 12 values.

---

# Option 5 - Event Attendee Names

## Viable Data

Use at least 12 names. Keep a consistent format such as first name only or
`Last, First`.

## Expected Tests

- found near beginning: early sorted name
- found near end: late sorted name
- not found: absent name
- unsorted binary attempt on original registration order

## Expected Explanation

Registration order and alphabetical order are different. Linear search can
work on registration order. Binary search requires alphabetical order.

## Grading Watch-Fors

- Student mixes first-name and last-name sorting.
- Student does not address duplicate names.
- Student claims binary search failed because of Python, not because the
  precondition was false.

---

# Cross-Option Grading Calibration

Strong work should:

- state the sorted-data precondition in plain language
- show at least one trace table with decisions
- include found and not-found cases
- distinguish "works by luck" from "valid algorithm"
- avoid treating built-in `in`, `index`, or `sort` as a replacement for the
  required algorithm explanation
