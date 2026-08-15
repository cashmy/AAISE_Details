# W08A Async Time Matters Live

**10-152-118 Web Development Foundations**  
**Week 8 Monday Live Lecture**  
**Topic:** Async - Time Matters

---

# Session Purpose

Week 8 introduces asynchronous behavior as a timing concept.

Students should leave Monday understanding that some browser work starts now
but finishes later. The goal is not to master every async syntax pattern. The
goal is to notice timing, make waiting visible, and explain what happens now
versus what happens later.

The practical target is intentionally small:

- recognize synchronous versus asynchronous behavior
- use `setTimeout()` to make delayed behavior visible
- connect delayed behavior to user feedback
- explain the order of events in simple language

---

# IIM Alignment

Week 8 Monday:

- introduce async conceptually
- delayed behavior
- waiting

Tuesday lab:

- simulated async actions
- timeouts
- simple timing patterns

AI role:

- AI as Explainer
- AI may explain timing order, callbacks, or confusing output
- AI should not generate the student's timed interaction or replace their
  timing explanation

---

# Reading Alignment

Assigned reading:

- **Required - Course Materials:** `Course_Materials/Week_08_Async_Time_Matters_Handout.md`
- **Skim - JS/JQ:** Chap 8 - Ajax & JSON: selected pages on requests,
  responses, and JSON: pp 367-383, 396-397
- **Skim - Course Materials:** `Course_Materials/Week_08_How_To_Read_JSON_Student_Guide.md`
- **Reference - Supplemental:** MDN `setTimeout()`, `fetch()`, and `Promise`

Reading-to-lab bridge:

- The handout gives the mental model: what happens now, and what happens later?
- Lecture makes timing visible with `setTimeout()`.
- Tuesday lab asks students to build visible delayed or sequential behavior.

What students should not try to master yet:

- full Promise chaining
- advanced error handling
- CORS and authentication
- complex API design
- service workers
- memorizing every async syntax pattern

---

# Prior Lab Review

Use the Week 7 success solution:

```text
Assignments/Success_Solutions/Week_07_Structured_JavaScript/
```

Review rhythm:

1. Open the final site and verify that behavior still works.
2. Show how named functions separate responsibilities.
3. Point out where the event listener calls a named function.
4. Bridge from structured functions to async callbacks.

Bridge:

```text
Last week we made behavior clearer.
This week we watch when behavior actually happens.
```

---

# Demo Set

Demo folder:

```text
Demos/Week_08_Async_Time/01_monday_delayed_message/
```

Demo role:

- build or reveal a button that updates the page
- type the immediate `Waiting...` update first
- add `setTimeout()` to schedule the later update
- narrate what happens now versus later
- keep the focus on observation and timing, not memorizing syntax

---

# Slide Sequence Overview

1. Async Is About Time
2. Previous Lab Review / Success Path
3. From Structure To Timing
4. What Counts As Success Today
5. Today's Toolbox
6. Parked For Later
7. Synchronous Code Runs Now
8. Async Work Starts Now And Finishes Later
9. Python Bridge: Same Timing Question
10. `setTimeout()` Makes Waiting Visible
11. Callback: The Later Function
12. User Feedback During Waiting
13. AI Can Explain Timing, Not Replace Your Work
14. Useful AI Prompt Pattern
15. Demo: Delayed Message
16. Trace The Order
17. Tuesday Lab Bridge
18. Evidence Expectations
19. Closing

---

# Slide-By-Slide Source

### Slide 1 - Async Is About Time

Student-visible text:

```text
Async is about time, not magic.

Some work:

- happens now
- starts now but finishes later
- needs the page to stay understandable while waiting

Today we ask:

What happens now?
What happens later?
```

**Instructor notes:**

- Lower the intimidation level immediately.
- Position async as an observation skill before a syntax skill.
- Connect to the handout title: Time Matters.

**Transition cue:**

- "Before we add a delay, let's look back at last week's structure work."

### Slide 2 - Previous Lab Review / Success Path

Student-visible text:

```text
Previous lab review:

- working behavior
- named functions
- clear responsibilities
- same result after refactoring

Success path:

Structure helps us see where timing belongs.
```

**Instructor notes:**

- Open the Week 7 success solution.
- Show one named function and one event listener.
- Emphasize that async callbacks are still functions.

**Transition cue:**

- "The clearer the function is, the easier it is to understand when it runs."

### Slide 3 - From Structure To Timing

Student-visible text:

```text
Last week:

- What does this function do?
- What is this function responsible for?

This week:

- When does this function run?
- What happens while we wait?
```

**Instructor notes:**

- Make Week 8 feel like a continuation, not a sudden new topic.
- Students already know events happen later after a click; now we name that
  kind of timing more explicitly.

**Transition cue:**

- "Today's success is not writing a large feature. It is being able to explain timing."

### Slide 4 - What Counts As Success Today

Student-visible text:

```text
Today counts as success if you can:

- identify what runs immediately
- identify what is scheduled for later
- make a waiting state visible
- explain the order without guessing
- keep the browser page understandable while waiting
```

**Instructor notes:**

- Use the standard course SmartArt / built-in graphic pattern.
- Do not generate a separate AI image for this slide.
- Keep this as a confidence anchor.

**Transition cue:**

- "To do that, we only need a small toolbox."

### Slide 5 - Today's Toolbox

Student-visible text:

```text
What we will use today:

- synchronous
- asynchronous
- delay
- callback
- `setTimeout()`
- waiting state
- visible feedback
- retest
```

**Instructor notes:**

- Keep the list concrete.
- Note that `fetch` and Promises are coming, but the Monday lab can succeed
  with delayed behavior.

**Transition cue:**

- "And there are some things we are deliberately parking."

### Slide 6 - Parked For Later

Student-visible text:

```text
Parked for later:

- full Promise chains
- advanced error handling
- API authentication
- CORS details
- service workers
- complex loading systems

For now:

Make timing visible.
Explain the order.
```

**Instructor notes:**

- This slide matters because async can explode into too much vocabulary.
- Reinforce that Week 8 is introductory and concept-first.

**Transition cue:**

- "Let's start with the kind of code that does exactly what beginners expect."

### Slide 7 - Synchronous Code Runs Now

Student-visible text:

```text
Synchronous code runs in order:

`A`
`B`
`C`

One line finishes before the next line runs.

This is the pattern most beginner code appears to follow.
```

**Instructor notes:**

- Draw from the handout's console example.
- The slide can show three steps in a straight line.
- Avoid implying that all JavaScript is simple; this is a baseline.

**Transition cue:**

- "Async code changes the timing, not the need for logic."

### Slide 8 - Async Work Starts Now And Finishes Later

Student-visible text:

```text
Asynchronous work:

- starts now
- waits for something
- finishes later
- often uses a function that runs later

The page should not feel frozen while waiting.
```

**Instructor notes:**

- Use simple causes: timer, file, network request, user action.
- Tie to user experience: waiting should be visible.

**Transition cue:**

- "This should feel familiar if students are also seeing async in Python."

### Slide 9 - Python Bridge: Same Timing Question

Student-visible text:

```text
Python and JavaScript use different syntax.

But the core question is familiar:

- What happens now?
- What happens later?
- What waits?
- What keeps going?

The timing problem is shared.
```

**Instructor notes:**

- Do not teach Python async here.
- Use this only as a bridge for students taking Python at the same time.
- The bridge reduces cognitive load by naming the shared mental model.

**Transition cue:**

- "In JavaScript today, our smallest timing tool is `setTimeout()`."

### Slide 10 - `setTimeout()` Makes Waiting Visible

Student-visible text:

```text
`setTimeout()` says:

Run this function later.

It needs:

- a function to run later
- an amount of time to wait

The waiting is real, even when the code is short.
```

**Instructor notes:**

- Keep syntax minimal.
- Show the phrase "function later" before showing code.
- Avoid making students memorize milliseconds beyond "1000 is about one second."

**Transition cue:**

- "The function that runs later has a name: callback."

### Slide 11 - Callback: The Later Function

Student-visible text:

```text
A callback is a function used later.

For Week 8, read it as:

"When the timer finishes, run this."

The callback is not skipped.
It is scheduled.
```

**Instructor notes:**

- Connect back to Week 7 callbacks and event handlers.
- This is a recognition definition, not an exhaustive callback lecture.

**Transition cue:**

- "If something finishes later, the user needs to know what is happening."

### Slide 12 - User Feedback During Waiting

Student-visible text:

```text
Good timed behavior gives feedback:

- starting
- waiting
- finished

Example:

Click button -> "Waiting..." -> "Finished."

The user should not have to guess.
```

**Instructor notes:**

- This connects technical timing to UI clarity.
- Show why the assignment requires visible page changes.

**Transition cue:**

- "AI can help explain timing, but it cannot do the observation for you."

### Slide 13 - AI Can Explain Timing, Not Replace Your Work

Student-visible text:

```text
AI as Explainer:

You may ask:

"Explain why this message appears after the other message."

You may not submit:

- AI-generated timed behavior you cannot explain
- code pasted without testing
- a reflection written from AI's point of view

You still observe, test, and explain.
```

**Instructor notes:**

- Keep this in the Week 6-8 Explainer role.
- Make the allowed use practical: timing explanation, not solution generation.

**Transition cue:**

- "If students use AI for explanation, the prompt should protect their ownership."

### Slide 14 - Useful AI Prompt Pattern

Student-visible text:

```text
Useful AI prompt pattern:

"I manually wrote this timed JavaScript interaction.
Do not rewrite it for me.
Explain what happens immediately,
what happens later,
and why the delayed message appears after the waiting message.
Ask me one question before suggesting code."
```

**Instructor notes:**

- This gives students a safe prompt before Tuesday lab.
- Emphasize manually wrote, do not rewrite, explain timing, ask first.
- The purpose is to clarify timing order, not outsource the assignment.

**Transition cue:**

- "Now let's build the smallest visible version."

Visual notes:

- Form-like prompt card with labeled parts: context, constraint, timing
  explanation, and ask-first behavior.

### Slide 15 - Demo: Delayed Message

Student-visible text:

```text
Demo:

Button click starts a delay.

The page shows:

- immediate waiting message
- delayed completion message

Watch for:

What happens now?
What happens later?
```

**Instructor notes:**

- Use `Demos/Week_08_Async_Time/01_monday_delayed_message/`.
- Type selectors and the immediate status update first.
- Then add `setTimeout()` and retest.

**Transition cue:**

- "Now that it works, we trace the order carefully."

### Slide 16 - Trace The Order

Student-visible text:

```text
Trace the order:

1. The user clicks.
2. The page shows "Waiting..."
3. The timer starts.
4. Other browser work can continue.
5. The delayed function runs.
6. The page shows the final message.
```

**Instructor notes:**

- This slide is the conceptual payoff for the demo.
- Invite students to say which steps happen now and which happen later.

**Transition cue:**

- "That same trace becomes the Tuesday lab strategy."

### Slide 17 - Tuesday Lab Bridge

Student-visible text:

```text
Tuesday lab:

Build visible timed behavior.

Your page should show:

- a start action
- a waiting state
- a later result

Keep the feature small enough to explain.
```

**Instructor notes:**

- Connect directly to Assignment 8 Iteration 1.
- Offer examples: delayed message, simulated loading, sequence after delay.

**Transition cue:**

- "The submission evidence should prove the timing was intentional."

### Slide 18 - Evidence Expectations

Student-visible text:

```text
Evidence this week:

- the timed behavior is visible
- the code runs without errors
- the waiting state is clear
- the final result appears later
- your reflection explains timing

Do not rely on "it eventually worked."
Explain the order.
```

**Instructor notes:**

- Reinforce that async evidence is about observation.
- Tie to debugging habits from Week 6 and refactoring habits from Week 7.

**Transition cue:**

- "The short version: timing is now part of how we design behavior."

### Slide 19 - Closing

Student-visible text:

```text
Week 8 begins a new question:

Not just:

"What does the code do?"

Also:

"When does it happen?"

Programs do not just execute.
They react over time.
```

**Instructor notes:**

- Close with the assignment's subtle concept.
- Preview that Wednesday connects this to request-shaped behavior.

**Transition cue:**

- "Next, we connect this same timing idea to data requests and loading."

---

# AI Use Notes

AI may help explain why a timed message appears later, why `setTimeout()` uses a
callback, or what a simple output order means. Students still need to write,
test, observe, and explain their own timed behavior.

---

# Image Prompt Notes

Use the Week 8 prompt packet for the following:

| Slide | Image Concept | Prompt Packet Note |
| --- | --- | --- |
| 1 | Async as time, not magic | Include in Week 8 prompt packet |
| 2 | Week 7 structure to timing | Include in Week 8 prompt packet |
| 3 | Structure questions to timing questions | Include in Week 8 prompt packet |
| 5 | Today's toolbox | Include in Week 8 prompt packet |
| 6 | Parked for later | Include in Week 8 prompt packet |
| 7 | Synchronous order | Include in Week 8 prompt packet |
| 8 | Async now/later split | Include in Week 8 prompt packet |
| 9 | Python bridge timing question | Include in Week 8 prompt packet |
| 10 | `setTimeout()` delay | Include in Week 8 prompt packet |
| 11 | Callback as later function | Include in Week 8 prompt packet |
| 12 | Waiting feedback states | Include in Week 8 prompt packet |
| 13 | AI as timing explainer | Include in Week 8 prompt packet |
| 14 | useful AI prompt pattern | Include in Week 8 prompt packet |
| 15 | Delayed message demo | Include in Week 8 prompt packet |
| 16 | Trace the order | Include in Week 8 prompt packet |

No separate image prompt is needed for Slide 4 because the standard course
SmartArt / built-in graphic pattern is used for "What Counts As Success Today."

---

# Timing Notes

Suggested pacing:

- prior lab review: 8-10 minutes
- concept framing: 10-15 minutes
- toolbox / parked topics: 5 minutes
- timing model: 15 minutes
- demo: 10-15 minutes
- AI-as-explainer boundary and prompt pattern: 4-6 minutes
- lab bridge / evidence: 5-8 minutes
