# WEEK 4 LECTURE OUTLINE - SEARCH AND SORT BEHAVIOR

**10-152-119 Algorithmic Problem Solving**

---

# 1. Session Identity

- **Week / Day:** Week 4 / Day 1
- **Unit:** Unit 2 - Data Structures, Search, Sort, and Growth
- **Weekly Theme:** Searching and Sorting
- **Lecture Title:** Preconditions Make Algorithms Honest

---

# 2. Alignment Anchor

- **Lab / Assignment Supported:** `Assignments/Lab_04_Search_and_Sort_Behavior.md`
- **Readiness Target:** Students can compare linear and binary search, trace behavior, and explain sorted-data preconditions.
- **Textbook Anchor:** Searching, sorting, preconditions, and algorithm design concerns.
- **AI Involvement Level:** Manual First -> AI-Assisted -> selective AI-Injected
- **Primary Watch Point:** Students may memorize binary search without understanding the sorted-data assumption.

---

# 3. Review / Bridge From Prior Week

Review Lab 3:

- compare one list-based and one dictionary-based solution
- ask which operation determined the better fit
- revisit how representation affects lookup

Bridge:

Last week, students chose structures for access patterns. This week, they see how search algorithms depend on representation and preconditions.

---

# 4. Opening Frame

Today we are moving from "Which structure fits?" to "What assumptions must be true before this algorithm works?"

---

# 5. Course Positioning

Searching and sorting are classic examples because they make correctness, efficiency, and assumptions visible in a small space.

---

# 6. Core Concepts

- Linear search: checks items one at a time.
- Binary search: repeatedly cuts the search space in half.
- Precondition: something that must be true before the algorithm is valid.
- Sorted data: the key condition for binary search.
- Trace: visible evidence of algorithm steps.

---

# 7. Algorithm Visibility / Demo Plan

Demo book-title search.

Show:

- linear search on unsorted and sorted data
- binary search on sorted data
- binary search failure or unreliable behavior on unsorted data

Evidence:

- linear search trace
- binary search low/high/mid table
- sorted vs unsorted comparison

---

# 8. Hands-On / Lab Bridge

Students begin Lab 4 with a different data set.

Their goal is not only to make search code run. Their goal is to prove when the search approach is valid.

---

# 9. Common Mistakes / Watch-Fors

- sorting after choosing the target without noticing
- off-by-one errors in binary search
- infinite loops from incorrect low/high updates
- claiming binary search is better without naming the precondition

---

# 10. AI Use Frame

AI may generate or revise search code only after students trace or write their own attempt.

Students must test and explain any generated code.

---

# 11. Explain / Checkpoint Questions

- Why does binary search need sorted data?
- What do low, high, and mid represent?
- What test proves the not-found case?
- What happens if the data violates the precondition?

---

# 12. End-of-Class Success Check

By the end of this session, students should be able to trace search behavior and explain the sorted-data precondition.

---

# 13. Materials / Artifacts Used

- `Assignments/Lab_04_Search_and_Sort_Behavior.md`
- prior Lab 3 structure comparison
- search trace table
