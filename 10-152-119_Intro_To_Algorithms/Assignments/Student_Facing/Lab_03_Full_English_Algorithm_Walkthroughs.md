# LAB 3 FULL-ENGLISH ALGORITHM WALKTHROUGHS

**Week 3 - Data Structures for Algorithmic Thinking**

---

# Purpose

This support artifact gives full-English examples of how to think through the
Lab 3 scenario options before writing Python or creating a comparison table.

These are not finished submissions. They are thinking scaffolds.

Use them to understand how the same problem can look different when the data is
stored in different structures.

---

# How To Use This Artifact

For your chosen scenario:

1. Read the matching walkthrough.
2. Identify the main operations your problem needs.
3. Choose two possible data structures.
4. Describe how each structure would store the same information.
5. Compare at least three operations.
6. Decide which structure better fits the scenario.

Do not copy the wording directly as your final answer. Your submitted work must
include your own problem statement, structures, operations, comparison table,
recommendation, and AI-use note if applicable.

---

# What Makes This A Data Structure Choice?

A data structure is not just a place to put data.

It affects what is easy, expensive, clear, or awkward.

In this lab, the goal is to explain which structure better fits the operations
your scenario needs most often. The better structure is not always the one that
looks more powerful. It is the one that fits the problem.

---

# Scenario 1 - Inventory Lookup

First, decide what each inventory item needs to store. For example, each item
may have a name, item ID, quantity, price, and category.

Then decide what the system needs to do most often. It may need to add an item,
look up an item by ID, update the quantity, remove an item, or display all
items.

If the inventory is stored as a list, each item could be stored one after
another. To find one item, the algorithm would check each item until it finds a
matching ID. This is simple and easy to display, but lookup may require scanning
the whole list.

If the inventory is stored as a dictionary, the item ID could be the key and
the item details could be the value. To find one item, the algorithm can use
the ID directly. This usually fits lookup and update better.

Questions to guide your comparison:

- What value uniquely identifies an item?
- Which operation matters most: display everything or find one item quickly?
- How would each structure handle a quantity update?
- What happens if the requested item ID does not exist?

---

# Scenario 2 - Student Score Summary

First, decide what information belongs to each student. For example, each
student may have a name, quiz scores, lab scores, and an average.

Then decide what operations are needed. The system may need to add a score,
calculate an average, find one student's scores, display all students, or
identify students below a threshold.

If the data is stored as a list of student records, the algorithm can loop
through each record and display summaries naturally. To find one student,
however, it may need to scan until the matching name or ID is found.

If the data is stored as a dictionary keyed by student name or ID, the
algorithm can find one student directly. This may be clearer for lookup and
updates, especially when the task starts with a specific student.

Questions to guide your comparison:

- Are students identified by name, ID, or another key?
- Does the problem mostly summarize everyone or update one student?
- Which structure makes score updates easier to explain?
- How will you handle a student with no scores yet?

---

# Scenario 3 - Help Desk Ticket Status

First, decide what each ticket needs to store. A ticket may include a ticket
number, title, status, priority, and assigned technician.

Then identify the common operations. The system may need to add a ticket, find
a ticket by number, update status, list open tickets, or count tickets by
status.

If the tickets are stored in a list, the algorithm can preserve the order the
tickets arrived. This is useful if order matters. To update one ticket, the
algorithm may need to scan the list until it finds the matching ticket number.

If the tickets are stored in a dictionary, the ticket number can be the key.
This makes lookup and status updates more direct. Displaying all tickets still
works, but the structure is mainly designed around finding a ticket by key.

Questions to guide your comparison:

- Does ticket arrival order matter?
- Is ticket number lookup a frequent operation?
- Which structure makes status updates clearer?
- How would each structure list only unresolved tickets?

---

# Scenario 4 - Menu Item Search

First, decide what information a menu item needs. A menu item may have a name,
price, category, ingredients, and dietary tags.

Then decide what the user needs to do. The program may need to display all menu
items, search by name, filter by tag, update a price, or list items in one
category.

If the menu is stored as a list, the algorithm can loop through all menu items
and filter them by category or tag. This is simple and readable, especially for
small menus.

If the menu is stored as a dictionary, the menu item name or ID can be the key.
This makes direct lookup easier when the user already knows the item name or
ID.

If the main goal is checking dietary tags, a set may also be useful because it
can represent unique labels such as vegetarian, spicy, gluten-free, or nut-free.

Questions to guide your comparison:

- Is the user searching by exact name, category, or tag?
- Which operation happens most often?
- Would a set help represent dietary tags?
- How should the program respond if no items match?

---

# Scenario 5 - Simple Contact Lookup

First, decide what each contact needs to store. A contact may include name,
phone number, email, company, and notes.

Then decide how contacts are normally found. The program may need to find a
contact by name, add a new contact, update a phone number, remove a contact, or
display all contacts.

If contacts are stored in a list, the algorithm can display them in the order
they were entered. To find one contact, it may need to scan one contact at a
time.

If contacts are stored in a dictionary, the contact name or email can be the
key. This makes direct lookup and update easier, but you need to choose the key
carefully.

Questions to guide your comparison:

- What should uniquely identify a contact?
- What happens if two contacts have the same name?
- Is display order important?
- Which structure makes updates easiest to explain?

---

# Scenario 6 - Event Registration List

First, decide what needs to be tracked for registration. This may include a
person's name, email, registration status, payment status, and waitlist
position.

Then identify the main operations. The system may need to add a registrant,
check whether someone is already registered, update a status, remove someone,
or display the roster.

If the registration list is stored as a list, the algorithm can preserve the
order people registered. This is helpful if first-come, first-served order
matters.

If registered emails are stored in a set, the algorithm can quickly check
whether an email is already registered. This helps prevent duplicates.

If detailed registration records are stored in a dictionary, the email or ID
can point to the full record. This helps with lookup and updates.

Questions to guide your comparison:

- Is order important?
- Is duplicate prevention important?
- Do you need only membership, or full registration details?
- Which structure best matches the most important operation?

---

# Your Turn

After reading the walkthrough for your scenario, choose two structures and
compare them honestly.

Your next step is not to prove that one structure is always best. Your next step
is to explain which structure better fits your scenario's operations.
