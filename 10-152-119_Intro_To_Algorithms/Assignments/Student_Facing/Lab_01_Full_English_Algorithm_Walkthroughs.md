# LAB 1 FULL-ENGLISH ALGORITHM WALKTHROUGHS

**Week 1 - Algorithms, Precision, and Correctness**

---

# Purpose

This support artifact gives full-English examples of how to think through the
Lab 1 scenario options before writing pseudocode or Python.

These are not finished submissions. They are thinking scaffolds.

Use them to understand how an everyday decision can become a clear, repeatable,
testable algorithm.

---

# How To Use This Artifact

For your chosen scenario:

1. Read the matching walkthrough.
2. Identify the likely inputs.
3. Identify the expected output.
4. Decide which rules must be more precise.
5. Turn the walkthrough into your own pseudocode or Python.
6. Create your own test cases, including edge cases.

Do not copy the wording directly as your final answer. Your submitted algorithm
must include your own assumptions, constraints, tests, and revision note.

---

# What Makes This An Algorithm?

An algorithm is a clear, repeatable process for solving a problem.

It can be shown as:

- full-English steps
- pseudocode
- Python code
- a table of rules
- a flowchart or decision diagram

The format matters less than the reasoning. The process must be precise enough
that someone else can follow it and test it.

---

# Scenario 1 - Cafeteria Meal Recommendation

First, look at each meal option one at a time.

For each meal, check whether it meets the required conditions. For example,
the meal may need to stay under a maximum price, avoid a certain ingredient,
or meet a dietary preference.

If the meal does not meet a required condition, remove it from consideration.

If the meal does meet the required conditions, calculate a simple score based
on the factors that matter for the recommendation. For example, the score may
consider price, preference, nutrition, or preparation time.

Keep track of the meal with the best score so far.

After all meals have been checked, recommend the meal with the best score.

If no meals meet the required conditions, return a clear message that no meal
matches the requirements.

Questions to make the algorithm more precise:

- What makes a meal unacceptable?
- What factors affect the score?
- What happens if two meals have the same score?
- What should the output include besides the meal name?

---

# Scenario 2 - Help Desk Ticket Priority

First, look at the information provided for one help desk ticket.

Identify the factors that affect priority. For example, the ticket may include
the number of people affected, the severity of the problem, the deadline, and
whether work is completely blocked.

Check for any condition that should automatically create a high-priority ticket.
For example, a system outage that affects many users may be high priority even
if the ticket was submitted recently.

If no automatic high-priority condition applies, compare the ticket against
lower-priority rules.

Assign the ticket to one clear priority level, such as high, medium, or low.

Return the assigned priority and the main reason for that decision.

If required information is missing, return a message explaining what information
is needed before the priority can be assigned.

Questions to make the algorithm more precise:

- Which conditions automatically make a ticket high priority?
- What is the difference between medium and low priority?
- What should happen if the ticket has incomplete information?
- Can two rules conflict, and if so, which rule wins?

---

# Scenario 3 - Parking Fee Calculation

First, collect the information needed to calculate the parking fee.

This may include the number of hours parked, whether the person has a permit,
whether the parking happened during a special event, and whether a daily maximum
fee applies.

Check whether the driver qualifies for a free or discounted parking rule.

If a free or discounted rule applies, calculate the fee using that rule.

If no special rule applies, calculate the standard fee based on the number of
hours parked.

After calculating the fee, check whether the total is higher than the maximum
allowed charge. If it is, use the maximum charge instead.

Return the final parking fee and a short explanation of which rule was used.

Questions to make the algorithm more precise:

- How are partial hours handled?
- Is there a maximum daily charge?
- Does a permit always reduce the fee?
- Which rule applies first if more than one rule matches?

---

# Scenario 4 - Event Registration Eligibility

First, collect the registration information for one person.

Identify the eligibility rules. For example, the event may require a minimum
age, a completed prerequisite, a paid fee, or available seats.

Check each required condition one at a time.

If the person fails a required condition, stop the approval process and record
the reason they are not eligible.

If the person meets all required conditions, check whether space is still
available.

If space is available, approve the registration.

If space is not available, place the person on a waitlist or return a message
that registration is closed.

Return the final decision and the reason for that decision.

Questions to make the algorithm more precise:

- Which requirements are mandatory?
- Does one failed requirement immediately end the process?
- What happens when the event is full?
- What should be shown to the user when registration is denied?

---

# Scenario 5 - Library Late-Fee Decision

First, collect the information about the borrowed item.

This may include the due date, return date, item type, borrower type, and
whether a grace period applies.

Determine whether the item was returned late.

If the item was not returned late, the fee is zero.

If the item was returned late, calculate the number of late days.

Check whether the borrower or item qualifies for a special rule, such as a grace
period, fee waiver, or maximum fee.

Calculate the fee using the correct daily rate.

If the fee is higher than the maximum allowed fee, use the maximum fee instead.

Return the final fee and a short explanation of how it was calculated.

Questions to make the algorithm more precise:

- How is a late day counted?
- Is there a grace period?
- Do different item types have different rates?
- Is there a maximum fee?

---

# Your Turn

After reading the walkthrough for your scenario, write your own version using
your chosen assumptions.

Your next step is not to make the program fancy. Your next step is to make the
process precise enough to test.
