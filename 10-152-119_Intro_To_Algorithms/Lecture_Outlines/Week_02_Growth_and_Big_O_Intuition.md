# WEEK 2 LECTURE OUTLINE - GROWTH AND BIG-O INTUITION

**10-152-119 Algorithmic Problem Solving**

---

# 1. Session Identity

- **Week / Day:** Week 2 / Day 1
- **Unit:** Unit 1 - Algorithmic Foundations and Correctness
- **Weekly Theme:** Big-O and Growth Intuition
- **Lecture Title:** When Working Code Starts to Slow Down

---

# 2. Alignment Anchor

- **Lab / Assignment Supported:** `Assignments/Lab_02_Growth_and_Big_O_Intuition.md`
- **Readiness Target:** Students can collect timing evidence and explain growth behavior using introductory Big-O vocabulary.
- **Textbook Anchor:** Performance analysis; time and space complexity; growth patterns.
- **AI Involvement Level:** Manual First -> AI-Assisted
- **Primary Watch Point:** Students may confuse noisy timing measurements with complete proof.

---

# 3. Review / Bridge From Prior Week

Review Lab 1:

- show one successful precision/correctness solution pattern
- review a normal case and an edge case
- discuss one ambiguity that changed the expected output

Bridge:

Last week, students proved correctness by testing different inputs. This week, they will keep changing inputs, but now they will observe what happens as input size grows.

---

# 4. Opening Frame

Today we are moving from "Does this work?" to "How does this behave when the amount of data changes?"

---

# 5. Course Positioning

Students have practiced defining and testing a solution. Now they add performance awareness without turning the course into advanced math.

---

# 6. Core Concepts

- Input size: the amount of data an algorithm works on.
- Growth pattern: how work changes as input grows.
- Big-O vocabulary: constant, linear, quadratic, logarithmic.
- Timing experiment: measured evidence from running code.
- Limitation of timing: hardware, noise, and setup can affect results.

---

# 7. Algorithm Visibility / Demo Plan

Demo list lookup vs set lookup.

Show:

- same lookup goal
- different representation
- timing table across several input sizes
- small-input noise and larger-input separation

Evidence:

- timing table
- optional chart or formatted comparison

---

# 8. Hands-On / Lab Bridge

Students begin Lab 2 by comparing two different approaches.

Their goal is not to make a perfect benchmark. Their goal is to collect enough evidence to explain growth intuition responsibly.

---

# 9. Common Mistakes / Watch-Fors

- testing only one input size
- timing unrelated work
- assuming small input results prove scalability
- using Big-O words without connecting them to evidence

---

# 10. AI Use Frame

AI may help explain timing patterns after students collect evidence.

Students should ask AI to critique the timing setup, not invent results.

---

# 11. Explain / Checkpoint Questions

- What changed as input size grew?
- Which approach seemed to do more work?
- Why can timing be noisy?
- What Big-O vocabulary fits the evidence?
- What does the evidence not prove?

---

# 12. End-of-Class Success Check

By the end of this session, students should be able to compare two approaches with timing evidence and a cautious growth explanation.

---

# 13. Materials / Artifacts Used

- `Assignments/Lab_02_Growth_and_Big_O_Intuition.md`
- prior Lab 1 solution or successful-version notes
- `v2/Textbook_Coverage_and_Reference_Map_v2.md`
