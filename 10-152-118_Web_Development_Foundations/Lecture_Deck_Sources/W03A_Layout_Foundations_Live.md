# W03A Layout Foundations Live

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 3
- Session: Monday live
- Deck title: Layout Foundations: Control Space
- Phase: Foundations
- Target duration: 55-70 minutes
- Recording expected: no

## Session Type

Monday live lecture.

## Lesson Purpose

Students should leave Monday understanding that layout is not visual decoration.
Layout is how page structure is expressed in space.

The practical target is modest: recognize the box model, use Flexbox on one
container, and explain how spacing/alignment changed the page.

## IIM Alignment

Week 3 Monday:

- Box model as mental model.
- Flexbox introduction.
- Layout is not positioning hacks.

## Reading Alignment

Week 3 assigned reading:

- Required - HTML/CSS: Duckett Chap 13 - Boxes, pp. 300-328
- Skim - HTML/CSS: Duckett Chap 15 - Layout, pp. 358-404
- Reference - Supplemental: MDN Flexbox guide
- Reference - Supplemental: MDN Media Queries guide

Reading-to-lab bridge:

- Reading gives vocabulary: box model, width, height, margin, padding, border, layout, alignment.
- Duckett's layout chapter also introduces positioning, fixed/liquid layouts, and 12-column grid planning as layout vocabulary students should recognize.
- Lecture turns that vocabulary into a visible layout decision.
- Tuesday lab applies Flexbox to the existing Week 2 styled site as the course's beginner-friendly applied layout tool.

What students should not try to master yet:

- every Flexbox property
- implementing 960.gs or a full grid framework
- the modern CSS Grid layout module
- professional responsive design
- pixel-perfect layout
- JavaScript behavior

## Review / Prior Work Bridge

Previous lab:

- Assignment 2 - Styling & Visual Design

Success solution:

```text
Assignments/Success_Solutions/Week_02_Styling_Visual_Design/
```

Review focus:

- show one successful path, not the only correct answer
- compare Week 1 HTML-only structure to Week 2 styled version
- point out one shared stylesheet and consistent navigation
- identify margin and padding already present in the CSS
- connect styling to today's question: how do we control larger page regions?

## What Counts As Success Today

By the end of the session, students should be able to:

- describe an element as a box on the page
- distinguish margin, padding, border, and content
- apply Flexbox to one container
- see a page change from default stacking into intentional layout
- resize the browser and notice where layout still needs work

Success is not a complete responsive site today.

## Today's Toolbox

Today we will use:

- box model
- layout vocabulary
- 12-column grid idea
- content
- padding
- border
- margin
- `display: flex`
- `gap`
- `flex`

## Parked For Later

Parked for later:

- full responsive design
- detailed media query strategy
- implementing 960.gs or grid frameworks
- modern CSS Grid module
- framework layouts
- JavaScript-driven layout changes

Today, the win is controlling one layout region intentionally.

## Assignment Supported

Assignment 3 - Layout & Responsive Design

Monday supports Iteration 1:

- use Flexbox to organize at least one section
- improve navigation or main content layout
- make spacing and alignment more intentional
- keep the site readable while changing layout

## Readiness Target

By the end of the session, students should be ready to:

- open their Week 2 site and identify one layout region to improve
- wrap related content in a container
- apply a simple Flexbox rule to that container
- test whether the layout is easier to scan

## Primary Watch Point

Students may think layout means "move things around until it looks right."

Reframe:

```text
Layout is a system for organizing space.
Flexbox works because a container controls its children.
```

## Demo Set

Demo folder:

```text
Demos/Week_03_Layout_Responsive/01_monday_simple_layout/
```

Demo files:

- `index.html`
- `styles.css`
- `demo_notes.md`

Delivery:

- Type or reveal the header, main content, and sidebar regions.
- Show the page before the Flexbox layout rule.
- Type the key Flexbox rules live.
- Refresh and inspect how the page changed.
- Resize the browser and deliberately expose the next problem.

## Slide Sequence Overview

1. Layout Is Structure In Space
2. Previous Lab Review / Success Path
3. From Styled Page To Organized Page
4. What Counts As Success Today
5. Today's Toolbox
6. Parked For Later
7. The Box Model Is The First Layout Map
8. Margin And Padding Are Not The Same
9. Layout Systems In The Reading
10. Grid Thinking, Not Grid Implementation
11. Containers Control Groups
12. Flexbox, Gently
13. Demo: Simple Layout
14. Inspect The Result
15. Tuesday Lab Bridge
16. Evidence Expectations
17. Closing

## Slide-By-Slide Source

### Slide 1 - Layout Is Structure In Space

Student-visible text:

```text
A web page is not just content plus color.

Layout answers:
- what belongs together?
- what should be easy to scan?
- where does the reader's eye go first?
- what happens when the screen changes?
```

**Instructor notes:**

- Start with the idea that layout is a thinking problem, not a decoration problem.
- Connect back to Week 1 structure and Week 2 appearance.
- Name Week 3 as the point where students begin controlling page space.

**Transition cue:**

- "Before we move anything, let's look at one successful styled version from last week."

Visual notes:

- Page content blocks being arranged into readable zones.

### Slide 2 - Previous Lab Review / Success Path

Student-visible text:

```text
Assignment 2 success path:

- one shared stylesheet
- readable text
- consistent navigation
- intentional color and spacing
- class-based styling

Today we keep the CSS layer and improve the space.
```

**Instructor notes:**

- Open the Week 2 success solution.
- Show that the site has structure and style, but layout can still be improved.
- Keep this focused; it is a bridge, not a full reteaching.

**Transition cue:**

- "The page looks better than plain HTML. Now we ask whether the space helps the reader."

Demo connection:

- `Assignments/Success_Solutions/Week_02_Styling_Visual_Design/`

### Slide 3 - From Styled Page To Organized Page

Student-visible text:

```text
Styling changes appearance.
Layout organizes space.

A styled page may still feel:
- crowded
- scattered
- hard to scan
- awkward on different screens

Layout makes relationships visible.
```

**Instructor notes:**

- Do not make students feel their Week 2 work was wrong.
- Present Week 3 as the next layer of the same site.
- Emphasize improvement through iteration.

**Transition cue:**

- "So today's success condition is not a perfect design. It is one visible layout decision."

Visual notes:

- Before/after page where the same content becomes grouped.

### Slide 4 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- you can point to the boxes on a page
- you can explain margin, padding, and border
- one Flexbox container changes layout
- the page becomes easier to scan
- you notice what still needs responsive work
```

**Instructor notes:**

- Use the standard SmartArt or built-in success graphic.
- Emphasize reachable progress.
- Say explicitly that responsive mastery is not today's target.

**Transition cue:**

- "Here are the tools we actually need in our hands today."

### Slide 5 - Today's Toolbox

Student-visible text:

```text
Today we will use:

- box model
- layout vocabulary
- 12-column grid idea
- content, padding, border, margin
- container
- `display: flex`
- `gap`
- `flex`
- save, refresh, resize
```

**Instructor notes:**

- The toolbox now includes recognition vocabulary from Duckett and the applied Flexbox path.
- The resize action matters: students should see layout as testable.
- Keep the Flexbox property set intentionally small.

**Transition cue:**

- "And just as important, here is the line between recognition and implementation."

Visual notes:

- Toolbox with box model, grid-planning recognition, and Flexbox tools.

### Slide 6 - Parked For Later

Student-visible text:

```text
Parked for later:

- full responsive design strategy
- many Flexbox properties
- implementing 960.gs or grid frameworks
- modern CSS Grid module
- frameworks like Bootstrap
- JavaScript behavior

Today: recognize grid thinking; implement one Flexbox layout.
```

**Instructor notes:**

- This protects the week from becoming a layout survey while still honoring the assigned reading.
- Mention that Wednesday will introduce responsive thinking.
- Distinguish Duckett's 12-column grid system as a recognition/planning concept from modern CSS Grid as a later implementation tool.

**Transition cue:**

- "Now that the scope is clear, we can start with the smallest layout unit: the box."

Visual notes:

- Shelf with deferred layout topics.

### Slide 7 - The Box Model Is The First Layout Map

Student-visible text:

```text
Every element takes up space.

Think of an element as:
- content: the actual text or image
- padding: breathing room inside the box
- border: the edge of the box
- margin: space outside the box

Layout begins when you can see the boxes.
```

**Instructor notes:**

- Draw or show the box model slowly.
- Use a heading or paragraph from a student page as the mental example.
- Avoid turning this into memorization of all box properties.

**Transition cue:**

- "The two spacing words students mix up most are margin and padding."

Visual notes:

- Simple labeled box model diagram.

### Slide 8 - Margin And Padding Are Not The Same

Student-visible text:

```text
Padding adds space inside the element.

Margin adds space outside the element.

Quick check:
- text too close to its own edge? padding
- two boxes too close together? margin or gap
- layout feels cramped? inspect the space before adding more color
```

**Instructor notes:**

- This slide should be very practical.
- Tie it directly to Week 2 CSS where margin and padding already appeared.

**Transition cue:**

- "Once we understand individual boxes, we can control a group of boxes."

Visual notes:

- Two labeled boxes comparing inner and outer spacing.

### Slide 9 - Layout Systems In The Reading

Student-visible text:

```text
Duckett's layout chapter introduces several layout ideas:

- positioning moves elements from normal flow
- fixed layouts use set widths
- liquid layouts stretch with the browser
- grid systems align content into columns

Read these as vocabulary and history.
Do not try to implement all of them this week.
```

**Instructor notes:**

- This slide exists to honor the assigned reading without overloading the lab.
- Keep the tone clear: these are useful layout concepts, but not all become assignment requirements.
- Mention 960.gs as an older/common grid-system example, not the main tool students will use.

**Transition cue:**

- "The grid section is still worth noticing because it teaches a planning habit."

Visual notes:

- Four-panel layout vocabulary visual: positioning, fixed width, liquid width, column grid.

### Slide 10 - Grid Thinking, Not Grid Implementation

Student-visible text:

```text
The 12-column grid idea helps designers plan alignment.

Useful idea:
- line up content consistently
- divide space into columns
- make pages feel organized

This week:
- recognize the grid-planning idea
- do not build a 960.gs layout
- use Flexbox for the lab implementation
```

**Instructor notes:**

- Make the distinction explicit: Duckett grid system recognition is in; implementing 960.gs is out.
- This prevents the false impression that all grid thinking is skipped.
- Tie it to the course's current applied path: Flexbox is the required lab tool.

**Transition cue:**

- "For our first implementation, the simplest useful move is still container controls children."

Visual notes:

- Simple 12-column overlay behind content blocks, with a separate Flexbox implementation path.

### Slide 11 - Containers Control Groups

Student-visible text:

```text
Flexbox starts with a container.

The container decides how its children line up.

Example:
- `.page` is the container
- `.content` and `.sidebar` are children
- the layout rule goes on `.page`
```

**Instructor notes:**

- This is the key mental model for Flexbox.
- Repeat: put Flexbox on the parent/container.
- Students often put the rule on the item they want to move.

**Transition cue:**

- "Now we can introduce Flexbox without treating it like magic."

Visual notes:

- Parent container holding two child boxes.

### Slide 12 - Flexbox, Gently

Student-visible text:

```text
Flexbox can organize children in a row or column.

Today's small pattern:

`.page {`
`  display: flex;`
`  gap: 16px;`
`}`

Start with one container.
Then inspect what changed.
```

**Instructor notes:**

- Keep the code small enough to type live.
- Mention that there are many Flexbox properties, but not today.
- Emphasize observable change.

**Transition cue:**

- "Let's build the smallest useful version and watch the page move."

### Slide 13 - Demo: Simple Layout

Student-visible text:

```text
Demo: Simple Layout

Watch for:
- the page before layout CSS
- `.page` as the container
- `display: flex`
- `gap`
- content and sidebar widths
- what breaks when the browser narrows
```

**Instructor notes:**

- Type key regions and key CSS rules live.
- Paste repeated markup if timing requires it.
- Show the page before adding Flexbox so the layout change is visible.

**Transition cue:**

- "The important moment is not the code appearing. It is the page changing because the container got a rule."

Demo connection:

- `Demos/Week_03_Layout_Responsive/01_monday_simple_layout/`

### Slide 14 - Inspect The Result

Student-visible text:

```text
After the demo, inspect:

- Did the main content and sidebar line up?
- Is the gap visible?
- Is the text still readable?
- What happens when the browser gets narrower?

Working at one size is progress.
It is not the finish line.
```

**Instructor notes:**

- Resize the browser and let the weakness show.
- This sets up Wednesday without trying to solve responsiveness today.
- Normalize the idea that layout is tested by changing conditions.

**Transition cue:**

- "Tuesday's lab is your first layout iteration, not the final responsive version."

### Slide 15 - Tuesday Lab Bridge

Student-visible text:

```text
Tuesday lab: first layout iteration

Use your existing site.

Your goal:
- choose one section to organize
- use Flexbox at least once
- improve spacing or alignment
- keep navigation usable
- save evidence of the change
```

**Instructor notes:**

- Frame this as improving the site they already have.
- The assignment endpoint includes responsiveness, but Monday only prepares the first iteration.

**Transition cue:**

- "Keep your evidence small and concrete. Show what changed."

Lab connection:

- Assignment 3 - Iteration 1

### Slide 16 - Evidence Expectations

Student-visible text:

```text
Preserve evidence:

- HTML and CSS files still render
- Flexbox appears in your CSS
- before/after screenshot if possible
- one sentence explaining the layout change
- note one problem you still need to improve
```

**Instructor notes:**

- This supports revision and recovery.
- Ask students to name the remaining weakness rather than hiding it.

**Transition cue:**

- "A known layout problem is not failure. It is the backlog for the next iteration."

### Slide 17 - Closing

Student-visible text:

```text
Today:

- boxes became visible
- spacing became intentional
- one container controlled a group
- Flexbox created a first layout

Next:
we make layout respond when the screen changes.
```

**Instructor notes:**

- Close by previewing Wednesday's responsive iteration.
- Keep tone steady; Week 3 can feel harder than Weeks 1-2.

**Transition cue:**

- "You now have the first version. Wednesday is about making it adapt."

## Demo Execution Notes

- Use `Demos/Week_03_Layout_Responsive/01_monday_simple_layout/`.
- Type the `.page { display: flex; gap: 16px; }` rule live.
- Explain `flex: 2` and `flex: 1` as "more space" and "less space," not as a full Flexbox theory lesson.
- Resize the browser at the end to reveal the limitation.

## Lab / Assignment Bridge

Students should apply Monday's lesson to their own Week 2 site:

- pick one region
- organize related content
- use one Flexbox container
- improve readability or navigation
- preserve evidence

## Evidence / Submission Expectations

For Tuesday, students should have a first working layout iteration. The full
Assignment 3 endpoint, including media query responsiveness, belongs after
Wednesday's recorded lesson and Thursday refinement.

## AI-Use Boundary

AI discussion is not central this week.

If students use AI, they should use it only to explain a CSS property or help
compare two layout attempts. They must still be able to point to the container,
the children, and the rule that changed the layout.

## Image Prompt Notes

| Slide | Image need | Prompt artifact note |
|---|---|---|
| 1 | layout as structure in space | Include in Week 3 prompt packet |
| 2 | Week 2 success path | Include in Week 3 prompt packet |
| 4 | success today | Use SmartArt; no image prompt by default |
| 5 | toolbox | Include in Week 3 prompt packet |
| 6 | parked for later | Include in Week 3 prompt packet |
| 7 | box model diagram | Include in Week 3 prompt packet |
| 8 | margin vs padding | Include in Week 3 prompt packet |
| 9 | Duckett layout vocabulary | Include in Week 3 prompt packet |
| 10 | 12-column grid recognition | Include in Week 3 prompt packet |
| 11 | container controls children | Include in Week 3 prompt packet |
| 13 | demo simple layout | Include in Week 3 prompt packet |
| 14 | resize exposes limitation | Include in Week 3 prompt packet |

## Instructor Timing Notes

- Review / success path: 7-10 minutes
- Box model and spacing: 12-15 minutes
- Duckett layout/grid recognition: 5-8 minutes
- Flexbox mental model: 10-12 minutes
- Demo: 10-15 minutes
- Lab bridge and evidence: 5-8 minutes

Compress by shortening the success review, not by rushing the demo inspection.

## Post-Lecture Notes

- Note whether students confuse margin and padding.
- Note whether students put `display: flex` on the child instead of the container.
- Use those observations to shape the Wednesday recording if needed.
