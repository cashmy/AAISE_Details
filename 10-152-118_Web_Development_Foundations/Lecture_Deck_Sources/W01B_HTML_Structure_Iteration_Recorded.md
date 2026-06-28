# W01B HTML Structure Iteration Recorded

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 1
- Session: Wednesday recorded
- Deck title: HTML Structure: From Page To Small Site
- Phase: Foundations
- Target duration: 25-35 minutes
- Recording expected: yes

## Lesson Purpose

Students should see Monday's single page grow into a small structured site with semantic regions, navigation, a list, and a second page.

The instructional move is iteration:

```text
one page exists -> structure improves -> pages connect
```

## IIM Alignment

Week 1 Wednesday:

- Deepen semantic elements versus generic tags.
- Show "bad versus good structure" through improvement.
- Support Thursday lab refinement: fix navigation, improve hierarchy, clean organization.

## Reading Alignment

Week 1 assigned reading:

- Required - HTML/CSS: Duckett Chap 1 - Structure, pp. 8-28
- Required - HTML/CSS: Duckett Chap 2 - Text, selected headings and paragraphs, pp. 40-60
- Required - HTML/CSS: Duckett Chap 4 - Links and relative paths, pp. 74-92
- Reference - HTML/CSS: Duckett Chap 3 - Lists, pp. 62-72

What this recording reinforces:

- elements give content meaning
- headings create hierarchy
- links connect files
- file names and paths must match exactly

What students should not try to master yet:

- visual layout
- CSS styling
- advanced semantic elements
- forms, tables, media, or scripts

## Prior Work Bridge

Monday created one page:

```text
index.html -> browser -> visible page
```

Wednesday grows that first page into:

```text
index.html + about.html + navigation
```

## Today's Working Set

Today we will use:

- `header`
- `nav`
- `main`
- `section`
- `footer`
- `ul` and `li`
- `<a href="...">`
- `index.html`
- `about.html`

Today we will not use yet:

- CSS
- JavaScript
- styling decisions
- folders beyond the basic project folder

## Assignment Supported

Assignment 1 - HTML Multi-Page Site

Wednesday supports the concept focus and Thursday refinement:

- improve heading hierarchy
- clean up structure
- fix broken links
- make navigation understandable

## Readiness Target

By the end of the recording, students should be able to:

- explain how one page can become a small site
- identify the purpose of `header`, `nav`, `main`, `section`, and `footer`
- create a basic link between two local HTML files
- recognize that a broken link is often a file-name or path mismatch

## Primary Watch Point

Students may think semantic structure is "extra" because the page looks similar.

Reframe:

```text
Structure is for meaning, maintenance, and future layers.
```

## Demo Set

Demo folder:

```text
Demos/Week_01_HTML_Multi_Page_Site/02_wednesday_multi_page_structure/
```

Demo files:

- `index.html`
- `about.html`
- `demo_notes.md`

Delivery:

- Begin from the Monday Hello World shape.
- Type the first structural additions live.
- Paste repeated scaffolding for `about.html` if time requires it.
- Click links in the browser to verify navigation.

## Slide Sequence Overview

1. Reconnect To Monday
2. From Page To Site
3. Structure Has Jobs
4. Semantic Regions
5. Demo Plan
6. Demo: Add Page Regions
7. Demo: Add Navigation
8. Demo: Create About Page
9. Broken Links Are Usually Exact
10. Better Structure Check
11. Thursday Lab Refinement
12. Evidence And Reflection
13. How To Read Next Week's Material
14. Closing

## Slide-By-Slide Source

### Slide 1 - Reconnect To Monday

Student-visible text:

```text
Monday: one page existed.
Today: that page becomes a small site.

We will keep the first page and improve it:

- add structure
- add navigation
- add another page
- test movement between pages
```

**Instructor notes:**

- Remind students that the first page did its job.
- Today is not a new topic; it is the next iteration.

**Transition cue:**

- "A site is more than one file sitting alone."

Visual notes:

- One page card transforms into two connected page cards.

### Slide 2 - System

Student-visible text:

```text
Pages are connected.
Not isolated.

- Each page is a file.
- Each file has an exact name.
- Links point to file names.
- Navigation lets the browser move through the site.
```

**Instructor notes:**

- Use this to introduce multi-page thinking.
- Keep it concrete: the browser follows `href`.

**Transition cue:**

- "Before we add links, we need better structure inside the page."

Visual notes:

- Node-and-arrow diagram: Home -> About -> Home.

### Slide 3 - Core Idea

Student-visible text:

```text
Structure gives each part a job.

- `header`: introduction or page identity
- `nav`: movement between pages
- `main`: primary page content
- `footer`: closing or supporting information
```

**Instructor notes:**

- Do not overteach semantics.
- Students only need useful recognition.

**Transition cue:**

- "These names are not decoration. They help us describe the page."

Visual notes:

- Page wireframe with labeled regions.

### Slide 4 - Semantic Regions

Student-visible text:

```text
Use meaningful containers
when the page has meaningful parts.

Semantic structure helps:

- readers understand the page
- future CSS target the right areas
- future JavaScript find the right areas
- you explain your own work
```

**Instructor notes:**

- Compare all-content-in-body versus organized regions.
- Avoid suggesting every line needs a special tag.

**Transition cue:**

- "Let's apply that to the page from Monday."

Visual notes:

- Split: messy pile of text versus labeled document regions.

### Slide 5 - Demo Plan

Student-visible text:

```text
Demo path:

1. add regions
2. add navigation
3. add a second page
4. test the links

Watch how each step keeps the site working before adding more.
```

**Instructor notes:**

- This slide sets expectations for the recording.
- Tell students to pause and compare with their own site if useful.

**Transition cue:**

- "We will build the improvement in visible stages."

Visual notes:

- Four-step checklist.

### Slide 6 - Demo: Add Page Regions

Student-visible text:

```text
First improve the shape.
Then add more pages.

In `index.html`:

- wrap the top content in `header`
- add `main` for page content
- use `section` for grouped ideas
- add `footer` for closing information
```

**Instructor notes:**

- Start with `index.html`.
- Add `header`, `main`, sections, and footer.
- Save and refresh after adding structure.
- Point out that appearance barely changes, and that is expected.

**Transition cue:**

- "Now this page needs a way to move."

Visual notes:

- Live editor/browser; no generated image needed.

Demo connection:

- `02_wednesday_multi_page_structure/index.html`

### Slide 7 - Demo: Add Navigation

Student-visible text:

```text
`href` points to a file.
The file name must match.

Example:

- file: `about.html`
- link: `href="about.html"`

If one character changes, the link can break.
```

**Instructor notes:**

- Type the `nav` and first links.
- Explain `index.html` and `about.html` as local file names.
- Do not introduce absolute URLs yet unless asked.

**Transition cue:**

- "A link to about.html only works if about.html exists."

Visual notes:

- Callout on `href="about.html"` pointing to file list.

### Slide 8 - Demo: Create About Page

Student-visible text:

```text
New page.
Same site.
Shared navigation.

For `about.html`:

- keep the same basic HTML shape
- use a different `title`
- use a different `h1`
- include navigation back to Home
```

**Instructor notes:**

- Create `about.html`.
- Paste repeated scaffolding if needed.
- Type unique page title, `h1`, and content.
- Click between pages.

**Transition cue:**

- "If the link fails, the browser is giving us information."

Visual notes:

- Two file tabs: `index.html`, `about.html`.

### Slide 9 - Common Failure

Student-visible text:

```text
Broken links are usually exact-match problems.

- file name mismatch
- wrong extension
- missing file
- wrong folder

Debug by comparing the `href` to the actual file name.
```

**Instructor notes:**

- Deliberately mistype a link only if time allows.
- Keep the debugging calm.

**Transition cue:**

- "After links work, refinement is about structure quality."

Visual notes:

- Magnified file name and `href` mismatch.

### Slide 10 - Thinking Tool

Student-visible text:

```text
Structure check:

- Can I explain each section?
- Do headings make sense?
- Can I move between pages?

If the answer is yes, the site is becoming easier to maintain.
```

**Instructor notes:**

- This is the Thursday lab checklist.
- Emphasize headings read as an outline.

**Transition cue:**

- "That checklist becomes your Thursday refinement target."

Visual notes:

- Checklist over simple page outline.

### Slide 11 - Thursday Lab Refinement

Student-visible text:

```text
Thursday: improve the first version.

- grow toward at least 3 pages
- fix links
- improve heading hierarchy
- clean content organization
- keep it HTML-only

Assignment target:

- multiple pages
- clear structure
- links between pages
- final reflection after refinement
```

**Instructor notes:**

- Tie directly to Assignment 1 Iteration 2.
- This is the right moment to name the full multi-page target because students have now seen one page become a small site.
- No CSS yet.

**Transition cue:**

- "Your final submission should show that refinement happened."

Visual notes:

- Three simple page cards connected by arrows, or before/after document outline.

### Slide 12 - Evidence And Reflection

Student-visible text:

```text
Submit:

- HTML files
- working navigation
- 2-3 sentence reflection

Reflection prompt:
What changed between your first version and final version, and why?
```

**Instructor notes:**

- Reflection answers: what improved and why.
- Evidence is not a screenshot-only submission unless assignment system requires it.

**Transition cue:**

- "Next week we finally start controlling appearance."

Visual notes:

- Folder with three HTML pages and a small reflection note.

### Slide 13 - How To Read Next Week's Material

Student-visible text:

```text
How to read Week 2:

Required: CSS rules and color.
Skim: text readability.
Reference: return during lab.

Focus on:

- what CSS changes
- how CSS connects to HTML
- how color and text affect readability

Do not memorize every CSS property.
```

**Instructor notes:**

- Week 2 readings:
  - Chap 10 Introducing CSS, pp. 226-244
  - Chap 11 Color, pp. 246-262
  - Chap 12 Text selected pages
- Tell students to look for the problem CSS solves.

**Transition cue:**

- "This week we made the structure. Next week we change how it looks."

Visual notes:

- HTML document on left, CSS brush/layer on right; do not imply CSS changes meaning.

### Slide 14 - Closing

Student-visible text:

```text
If someone can move through your site
and understand it,
your structure is working.

Before submitting, check:

- each page opens
- each link works
- each page has a clear purpose
- no CSS is required yet
```

**Instructor notes:**

- End with the success condition.
- Repeat: no CSS required.

**Transition cue:**

- End.

Visual notes:

- Simple connected-site diagram with a check mark on navigation.

## Demo Execution Notes

Type live:

- first `header`, `nav`, `main`, `section`, and `footer`
- first two links
- unique `about.html` content

May paste:

- repeated HTML scaffolding for the second page
- repeated navigation after explaining it once

Inspect:

- browser navigation
- visible headings
- file names compared to `href`

Optional deliberate mistake:

- change `about.html` link to `abot.html`, click, then fix it

## Lab / Assignment Bridge

Thursday lab is Assignment 1 Iteration 2:

- fix navigation
- improve heading structure
- clean up organization
- keep the project HTML-only

## Evidence / Submission Expectations

Students submit:

- final HTML files
- organized folder
- working links
- short reflection: what changed and why

## AI-Use Boundary

No AI use is needed for this first structural build.

If a student is stuck, the preferred support path is:

```text
compare file names -> check href -> save -> refresh -> ask instructor
```

## Image Prompt Notes

See:

```text
Lecture_Deck_Sources/Week_01_Image_Prompts.md
```

Priority images:

- one page becoming connected pages
- semantic page regions
- file name / href exact-match warning

## Recording Notes

Target recording length:

- 25-35 minutes

Self-contained transitions:

- Reconnect to Monday at the start.
- Name each demo stage before doing it.
- Pause after navigation works.
- Leave students with Thursday refinement checklist.

Compressible:

- Slide 4 if demo time is needed
- repeated scaffolding in `about.html`

Do not compress:

- broken-link explanation
- Thursday lab bridge
- no-CSS boundary

## Post-Recording Notes

After recording, record:

- Did the link/path explanation feel clear enough?
- Did the demo stay HTML-only?
- Is the Wednesday recording short enough for students to watch before Thursday lab?
