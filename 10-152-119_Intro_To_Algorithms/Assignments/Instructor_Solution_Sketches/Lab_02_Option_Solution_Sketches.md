# LAB 02 OPTION SOLUTION SKETCHES

**Lab:** Growth and Big-O Intuition  
**Instructor Use:** grading calibration, alternate examples, quick response support

---

# Instructor Boundary

These sketches are instructor-only calibration notes. They are not
student-facing walkthroughs and are not runnable solution packages.

For Lab 02, a strong submission should compare two approaches fairly enough for
an introductory timing experiment. The exact timing values are less important
than the evidence pattern, same-output check, and cautious explanation.

---

# Common Required Evidence

Every option should include:

- short task description
- two approaches solving the same problem
- at least four input sizes
- timing table
- simple chart or comparison table
- likely growth explanation for each approach
- limitation of timing experiment
- walkthrough-use note or AI-use note if applicable

Suggested timing table:

| Input Size | Approach A Time | Approach B Time | What Changed? |
| --- | --- | --- | --- |

---

# Option 1 - Count Duplicates With Nested Loops vs Dictionary Counting

## Viable Framing

Count how many times each value appears in a list.

## Expected Approaches

- nested loops or repeated scanning
- dictionary counting in one pass

## Expected Evidence

- same-output check before timing
- timing table for at least four list sizes
- explanation that nested loops repeat comparisons
- explanation that dictionary counting updates counts as it scans once

## Useful Input Sizes

Start small enough to finish quickly, then grow visibly. Example sizes:

- 1,000
- 5,000
- 10,000
- 20,000

## Grading Watch-Fors

- Student times approaches that do not produce the same counts.
- Student includes print statements inside timed code.
- Student makes a formal Big-O proof claim from one timing table.

## Runnable Expansion Note

The existing Lab 02 success package already implements this option.

---

# Option 2 - Find A Maximum With One Loop vs Repeated Sorting

## Viable Framing

Find the largest value in a list.

## Expected Approaches

- one pass that tracks the largest value seen so far
- sort the full list and take the largest value

## Expected Evidence

- same maximum returned by both approaches
- timing table across increasing list sizes
- explanation that sorting organizes more information than the task requires
- limitation note about machine variability and list generation

## Useful Input Sizes

- 1,000
- 10,000
- 50,000
- 100,000

## Grading Watch-Fors

- Student sorts once outside the timed section for the sorting approach.
- Student compares a built-in `max` call to custom sort without explaining the
  difference.
- Student forgets to include negative numbers or repeated maximum values if
  relevant.

## Runnable Expansion Note

Generate deterministic random lists with a fixed seed if repeatability matters.
Include one same-output assertion before timing.

---

# Option 3 - Check Pair Sums With Nested Loops vs Set-Based Approach

## Viable Framing

Determine whether any two numbers in a list add to a target value.

## Expected Approaches

- nested loops checking every pair
- set-based complement lookup

## Expected Evidence

- same true/false result for both approaches
- timing table across increasing list sizes
- explanation that nested loops check many pairs
- explanation that the set remembers seen values for faster complement checks

## Useful Input Sizes

- 500
- 1,000
- 5,000
- 10,000

Keep sizes modest because nested pair checking can become slow quickly.

## Grading Watch-Fors

- Student allows the same list element to pair with itself incorrectly.
- Student does not test a not-found case.
- Student changes the target or data between approaches.

## Runnable Expansion Note

Use generated lists with a guaranteed matching pair for one timing set, then a
separate small correctness test with no pair.

---

# Option 4 - Build A String Repeatedly vs Collect Pieces And Join Them

## Viable Framing

Build one large string from many smaller pieces.

## Expected Approaches

- repeated string concatenation
- collect pieces in a list and join once

## Expected Evidence

- same final string or same final length
- timing table across increasing number of pieces
- explanation that repeated string building can create many intermediate
  strings
- explanation that join separates collection from final assembly

## Useful Input Sizes

- 1,000 pieces
- 10,000 pieces
- 50,000 pieces
- 100,000 pieces

Adjust if runtime is too fast or too slow on the available machine.

## Grading Watch-Fors

- Student prints the large string during timing.
- Student compares different text content across approaches.
- Student only checks length when content correctness also matters.

## Runnable Expansion Note

Use simple repeated fragments such as `"abc"`. Compare both final length and a
small prefix/suffix check if the full string is too large to display.

---

# Cross-Option Grading Calibration

Strong work should:

- compare two approaches to the same task
- verify both approaches produce equivalent results
- use increasing input sizes
- separate timing evidence from Big-O reasoning
- name at least one limitation of the experiment
- avoid broad claims from a small timing sample
