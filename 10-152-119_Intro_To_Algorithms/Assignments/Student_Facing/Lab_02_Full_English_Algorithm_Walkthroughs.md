# LAB 2 FULL-ENGLISH ALGORITHM WALKTHROUGHS

**Week 2 - Growth and Big-O Intuition**

---

# Purpose

This support artifact gives full-English examples of how to think through the
Lab 2 comparison options before writing or timing code.

These are not finished submissions. They are thinking scaffolds.

Use them to understand how two correct approaches can behave differently as the
input gets larger.

---

# How To Use This Artifact

For your chosen comparison:

1. Read the matching walkthrough.
2. Identify what both approaches are trying to accomplish.
3. Identify what work each approach repeats.
4. Predict which approach may grow more slowly or more quickly.
5. Implement or attempt both approaches.
6. Time both approaches with increasing input sizes.
7. Use your evidence to explain what happened.

Do not copy the wording directly as your final answer. Your submitted work must
include your own code, timing evidence, explanation, and limitation note.

---

# What Makes This An Algorithm Comparison?

In this lab, the goal is not only to make the code work.

The goal is to compare how two working approaches behave as the amount of data
increases.

Small inputs can make two approaches look similar. Larger inputs can reveal
that one approach repeats more work than the other.

---

# Option 1 - Count Duplicates With Nested Loops vs Dictionary Counting

## Approach A - Nested Loops

First, look at the first item in the list.

Compare it to every other item in the list to see how many times it appears.

Record the count for that item.

Then move to the next item and compare it to every other item again.

Continue this process until each item has been checked.

This approach is easy to understand because it directly asks, "How many times
does this item appear in the whole list?"

The possible problem is that it repeats a lot of comparisons. As the list grows,
each item may cause another pass through the list.

## Approach B - Dictionary Counting

First, create an empty dictionary to store counts.

Look at each item in the list one time.

If the item is not already in the dictionary, add it with a count of one.

If the item is already in the dictionary, increase its count by one.

After the list has been processed, the dictionary contains the count for each
item.

This approach may be faster because it avoids repeatedly scanning the whole
list for each item.

Questions to guide your comparison:

- Which approach looks at the same data more than once?
- What happens when the list doubles in size?
- Does the dictionary approach require extra storage?
- Are both approaches producing the same result?

---

# Option 2 - Find A Maximum With One Loop vs Repeated Sorting

## Approach A - One Loop

First, assume the first value is the largest value seen so far.

Then look at each remaining value one at a time.

If the current value is larger than the largest value seen so far, replace the
largest value with the current value.

After all values have been checked, return the largest value found.

This approach keeps only the best answer found so far and checks each value
once.

## Approach B - Repeated Sorting

First, take the list of values and sort it.

After sorting, the largest value will be at one end of the list.

Return that largest value.

If this sorting process is repeated many times, the program may do much more
work than necessary because sorting organizes the entire list even though only
one value is needed.

This approach may still be correct, but it may be inefficient for the task.

Questions to guide your comparison:

- Does the one-loop approach need the whole list to be sorted?
- What extra work does sorting do?
- How does each approach behave as the list grows?
- Are both approaches returning the same maximum value?

---

# Option 3 - Check Pair Sums With Nested Loops vs A Set-Based Approach

## Approach A - Nested Loops

First, choose the first number in the list.

Pair it with each other number in the list.

For each pair, add the two numbers together.

If the sum equals the target value, report that a matching pair was found.

If no match is found, move to the next starting number and repeat the process.

Continue until a matching pair is found or all possible pairs have been checked.

This approach is direct, but it may check many pairs as the list grows.

## Approach B - Set-Based Approach

First, create an empty set to remember numbers that have already been seen.

Look at each number in the list one at a time.

For the current number, calculate what other number would be needed to reach
the target sum.

Check whether that needed number is already in the set.

If it is, a matching pair has been found.

If it is not, add the current number to the set and continue.

This approach may be faster because it avoids checking every possible pair.

Questions to guide your comparison:

- Which approach checks more combinations?
- What does the set allow the program to remember?
- What happens if the matching pair appears near the end of the list?
- Are both approaches handling the same target value?

---

# Option 4 - Build A String Repeatedly vs Collect Pieces And Join Them

## Approach A - Repeated String Building

First, start with an empty string.

Take the first piece of text and add it to the string.

Then take the next piece of text and create a new combined string.

Continue adding one piece at a time until all pieces have been added.

This approach is simple to read, but it may create many intermediate string
values as the input grows.

## Approach B - Collect Pieces And Join

First, create an empty list to hold the pieces of text.

Add each piece of text to the list.

After all pieces have been collected, join the list into one final string.

This approach separates collecting the pieces from building the final output.

It may be more efficient because the final string is assembled in a more
controlled way.

Questions to guide your comparison:

- Which approach repeatedly rebuilds the result?
- Which approach stores pieces before creating the final string?
- Does the difference matter for very small inputs?
- What changes when the number of text pieces becomes large?

---

# Your Turn

After reading the walkthrough for your chosen comparison, write or attempt both
approaches and collect timing evidence.

Your explanation should connect the observed timing results to the amount of
repeated work each approach performs.
