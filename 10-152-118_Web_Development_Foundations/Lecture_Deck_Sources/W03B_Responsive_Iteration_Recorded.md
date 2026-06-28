# W03B Responsive Iteration Recorded

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 3
- Session: Wednesday recorded
- Deck title: Responsive Iteration: Layout That Adapts
- Phase: Foundations
- Target duration: 25-35 minutes
- Recording expected: yes

## Session Type

Wednesday recorded lecture.

## Lesson Purpose

Students should see Monday's first layout become a responsive layout through
iteration.

The instructional move is:

```text
works at one screen size -> test a narrower screen -> revise the layout rule
```

## IIM Alignment

Week 3 Wednesday:

- Introduce responsive thinking.
- Show layout breakpoints.
- Prepare Thursday lab: redesign layout for multiple screen sizes.
- Reinforce iteration mindset.

## Reading Alignment

Week 3 assigned reading:

- Required - HTML/CSS: Duckett Chap 13 - Boxes, pp. 300-328
- Skim - HTML/CSS: Duckett Chap 15 - Layout, pp. 358-404
- Reference - Supplemental: MDN Flexbox guide
- Reference - Supplemental: MDN Media Queries guide

What this recording reinforces:

- layout must be tested under changing screen sizes
- responsive design is about usability, not only shrinking
- media queries let CSS respond to conditions
- one HTML structure can support more than one layout

What students should not try to master yet:

- every media query pattern
- device-specific design
- professional breakpoint strategy
- CSS Grid mastery
- JavaScript-driven responsiveness

## Review / Prior Work Bridge

Monday introduced:

```text
boxes -> container -> Flexbox -> first layout
```

Wednesday grows that into:

```text
first layout -> resize test -> responsive rule -> improved layout
```

## What Counts As Success Today

By the end of the recording, students should be able to:

- explain why a layout that works on a large screen may fail on a small screen
- recognize a media query
- describe a breakpoint as a condition, not a device name
- test a page by resizing the browser
- make one layout change for a narrower screen

Success is one responsive improvement, not a complete mobile design system.

## Today's Toolbox

Today we will use:

- browser resize test
- breakpoint
- `@media`
- `max-width`
- card layout
- one-column layout
- inspect, revise, retest

## Parked For Later

Parked for later:

- mobile-first design strategy
- many breakpoints
- CSS Grid systems
- complex navigation patterns
- responsive images

Today, the goal is one clear layout response.

## Assignment Supported

Assignment 3 - Layout & Responsive Design

Wednesday supports the concept focus and Thursday refinement:

- understand how layout decisions affect readability
- apply at least one media query
- adjust layout for smaller screens
- ensure navigation and content remain usable
- write a short reflection about usability across screen sizes

## Readiness Target

By the end of the recording, students should be ready to:

- test their site at more than one browser width
- identify one layout that becomes awkward
- add or refine one media query
- explain what changed and why it improves usability

## Primary Watch Point

Students may think responsive design means "make everything smaller."

Reframe:

```text
Responsive design means the layout adapts so people can still use the page.
```

## Demo Set

Demo folder:

```text
Demos/Week_03_Layout_Responsive/02_wednesday_responsive_cards/
```

Demo files:

- `index.html`
- `styles.css`
- `demo_notes.md`

Delivery:

- Start from a card layout at desktop width.
- Resize before adding the media query.
- Name the usability problem.
- Type the `@media` rule live.
- Resize again and inspect the improvement.

## Slide Sequence Overview

1. Reconnect To Monday
2. The Working Problem: One Size Is Not Enough
3. What Counts As Success Today
4. Responsive Does Not Mean Smaller
5. Today's Toolbox
6. Breakpoints Are Conditions
7. Media Queries, Gently
8. Demo: Responsive Cards
9. Inspect, Revise, Retest
10. Thursday Lab Refinement
11. End-Of-Unit Reflection
12. Evidence And Submission
13. How To Read Next Week's Material
14. Closing

## Slide-By-Slide Source

### Slide 1 - Reconnect To Monday

Student-visible text:

```text
Monday:
- every element occupies space
- containers can control children
- Flexbox creates a first layout

Today:
- test the layout under pressure
- revise it for a narrower screen
```

**Instructor notes:**

- Make this feel like the next iteration, not a separate lecture.
- Mention that a layout can be successful and still need responsive refinement.

**Transition cue:**

- "The question is not only whether it works on my screen. The question is what happens when the screen changes."

Visual notes:

- Large browser view narrowing into smaller browser view.

### Slide 2 - The Working Problem: One Size Is Not Enough

Student-visible text:

```text
A layout can work at one size and fail at another.

Common signs:
- content feels squeezed
- navigation wraps awkwardly
- cards become too narrow
- text becomes hard to scan
- the user has to fight the page
```

**Instructor notes:**

- Avoid shame language. This is a normal development stage.
- Tie this to Thursday: students will revise, not start over.

**Transition cue:**

- "So today's success is not perfection. It is one clear response to a real layout problem."

Visual notes:

- Same page at wide and narrow widths with the narrow version visibly cramped.

### Slide 3 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- you test the page at more than one width
- you notice one layout problem
- one media query changes the layout
- content remains readable
- you can explain why the change helps
```

**Instructor notes:**

- Use the standard SmartArt or built-in success graphic.
- Keep it concrete and tied to the demo.

**Transition cue:**

- "The first misconception to remove is that responsive design just shrinks everything."

### Slide 4 - Responsive Does Not Mean Smaller

Student-visible text:

```text
Responsive design means the layout adapts.

It may:
- stack columns
- change spacing
- simplify navigation
- adjust card width
- preserve readability

The goal is usability under changing conditions.
```

**Instructor notes:**

- This is the key concept slide for the recording.
- Keep device names out of the center. Focus on conditions and usability.

**Transition cue:**

- "To make that happen, we need a small set of tools."

Visual notes:

- Content cards shifting from row layout to stacked layout.

### Slide 5 - Today's Toolbox

Student-visible text:

```text
Today we will use:

- resize test
- breakpoint
- `@media`
- `max-width`
- card layout
- one-column layout
- inspect, revise, retest
```

**Instructor notes:**

- Name the workflow as much as the syntax.
- Students should see responsive design as a test-and-revise process.

**Transition cue:**

- "A breakpoint is not a phone model. It is a condition."

Visual notes:

- Toolbox with responsive-testing tools.

### Slide 6 - Breakpoints Are Conditions

Student-visible text:

```text
A breakpoint says:

"When the screen meets this condition,
use these CSS rules."

Example:
- wide screen: cards can sit in a row
- narrow screen: cards may need to stack

Choose breakpoints because the content needs help.
```

**Instructor notes:**

- This should prevent device-name thinking.
- Use the card layout as the example.

**Transition cue:**

- "CSS expresses that condition with a media query."

Visual notes:

- Width ruler with a clear threshold and layout change.

### Slide 7 - Media Queries, Gently

Student-visible text:

```text
Small pattern:

`@media (max-width: 700px) {`
`  .card-grid {`
`    grid-template-columns: 1fr;`
`  }`
`}`

Read it as:
"At 700px or smaller, stack the cards."
```

**Instructor notes:**

- Use "read it as" to reduce syntax anxiety.
- If students have not seen CSS Grid deeply, frame this as reading the example, not mastering Grid.
- The assignment may use Flexbox or simple layout changes; the key is media-query thinking.

**Transition cue:**

- "Now let's watch the same content fail, then improve."

### Slide 8 - Demo: Responsive Cards

Student-visible text:

```text
Demo: Responsive Cards

Watch for:
- desktop layout first
- resize before the fix
- name the usability problem
- add the media query
- resize again
- confirm the HTML stayed the same
```

**Instructor notes:**

- Type the `@media` rule live.
- Resize before and after so the iteration is visible.
- Emphasize that changing CSS can adapt the same HTML.

**Transition cue:**

- "The fix matters because it responds to evidence, not because we guessed a magic number."

Demo connection:

- `Demos/Week_03_Layout_Responsive/02_wednesday_responsive_cards/`

### Slide 9 - Inspect, Revise, Retest

Student-visible text:

```text
Responsive work is a loop:

1. inspect the current layout
2. resize the browser
3. identify one problem
4. revise one rule
5. retest the page

Do not fix five problems at once.
```

**Instructor notes:**

- This reinforces iteration mindset.
- Connect to the broader course pattern: build, inspect, revise.

**Transition cue:**

- "That loop becomes Thursday's lab work."

Visual notes:

- Simple inspect-revise-retest loop.

### Slide 10 - Thursday Lab Refinement

Student-visible text:

```text
Thursday lab: responsive refinement

Your goal:
- test your site at different widths
- add at least one media query
- improve spacing or alignment
- keep navigation usable
- make the layout adapt, not just shrink
```

**Instructor notes:**

- This is now safe to present as the full weekly target because the responsive concept has been introduced.
- Remind students to improve their own site, not copy the demo.

**Transition cue:**

- "Before we leave Unit 1, we also need to pause and name what has changed in your understanding."

Lab connection:

- Assignment 3 - Iteration 2

### Slide 11 - End-Of-Unit Reflection

Student-visible text:

```text
Pause for reflection:

You have worked with:
- HTML structure
- CSS appearance
- layout and responsiveness

Write 4-6 sentences:
What feels clear now?
What still feels challenging?
Where do structure, styling, and layout affect each other?
```

**Instructor notes:**

- This prepares students for the shift into JavaScript.
- Treat the reflection as stabilization, not extra busywork.

**Transition cue:**

- "The reflection is part of learning the system before we add behavior."

### Slide 12 - Evidence And Submission

Student-visible text:

```text
Final Assignment 3 evidence:

- updated HTML files
- updated CSS file
- Flexbox used in layout
- at least one media query
- pages render correctly
- short reflection on usability across screen sizes
```

**Instructor notes:**

- Remind students that the media query should visibly change something.
- Evidence should make the improvement easy to verify.

**Transition cue:**

- "Next week is a phase shift: the page will start to behave."

### Slide 13 - How To Read Next Week's Material

Student-visible text:

```text
How to read next week's material:

Required:
- read slowly for scripts, variables, and basic instructions
- notice examples that look like step-by-step commands

Skim:
- use headings and examples to preview programming ideas

Reference:
- do not read function and loop chapters straight through yet
- return to them when a lab needs the idea

Before next time:
predict what small code examples will do before reading the explanation.
```

**Instructor notes:**

- Week 4 introduces JavaScript as programming before DOM work.
- Students are also beginning Python, so emphasize shared programming thinking without collapsing the courses together.

**Transition cue:**

- "You have learned how a page is built and how it looks. Next, we make code execute."

### Slide 14 - Closing

Student-visible text:

```text
Unit 1 foundation:

- HTML gives the page structure
- CSS gives it appearance
- layout organizes space
- responsiveness tests the design under changing conditions

Next:
JavaScript introduces behavior.
```

**Instructor notes:**

- Close the foundation unit clearly.
- The point is confidence plus readiness, not mastery of every detail.

**Transition cue:**

- "Bring the same inspect-and-explain habit into JavaScript next week."

## Demo Execution Notes

- Use `Demos/Week_03_Layout_Responsive/02_wednesday_responsive_cards/`.
- Start with the page at desktop width.
- Resize before adding the media query and name the problem.
- Type the `@media (max-width: 700px)` block live.
- Resize again and explain the change as iteration.

## Lab / Assignment Bridge

Students should use Thursday to finish Assignment 3:

- apply one real responsive change
- test more than one viewport width
- confirm navigation remains usable
- write the short required reflection

## Evidence / Submission Expectations

Assignment 3 final evidence should show:

- Flexbox in the CSS
- at least one media query
- readable content at different widths
- a short reflection that connects layout changes to usability

## AI-Use Boundary

AI discussion is not central this week.

If students use AI, they should use it for explanation or comparison, not for a
complete generated layout they cannot explain. They must be able to identify
the breakpoint, the condition, and the CSS rule that changes.

## Image Prompt Notes

| Slide | Image need | Prompt artifact note |
|---|---|---|
| 1 | Monday layout to responsive iteration | Include in Week 3 prompt packet |
| 2 | one size is not enough | Include in Week 3 prompt packet |
| 3 | success today | Use SmartArt; no image prompt by default |
| 4 | responsive means adapt | Include in Week 3 prompt packet |
| 5 | toolbox | Include in Week 3 prompt packet |
| 6 | breakpoint as condition | Include in Week 3 prompt packet |
| 8 | demo responsive cards | Include in Week 3 prompt packet |
| 9 | inspect, revise, retest loop | Include in Week 3 prompt packet |
| 11 | Unit 1 reflection | Include in Week 3 prompt packet |
| 14 | structure-style-layout-behavior transition | Include in Week 3 prompt packet |

## Instructor Timing Notes

- Reconnect and problem framing: 5-7 minutes
- Responsive concept and syntax: 8-10 minutes
- Demo: 12-18 minutes
- Lab bridge and reflection: 5-8 minutes
- Next-reading guidance and close: 3-5 minutes

Compress by shortening visual explanation, not by skipping the before/after
resize test.

## Post-Lecture Notes

- Note whether students understand breakpoints as content conditions.
- Note whether the CSS Grid example causes distraction; if so, verbally frame it as a readable example while allowing Flexbox-based assignment solutions.
- Use Week 4 opening to acknowledge that the course is shifting from structure/style/layout into behavior.
