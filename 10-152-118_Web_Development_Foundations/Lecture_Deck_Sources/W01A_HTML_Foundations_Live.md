# W01A HTML Foundations Live

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 1
- Session: Monday live
- Deck title: HTML Foundations: Something Exists
- Phase: Foundations
- Target duration: 55-70 minutes
- Recording expected: no

## Lesson Purpose

Students should leave Monday understanding that a web page is a structured document that can be saved, opened in a browser, changed, and refreshed.

The emotional target is safety: the first win is not beauty or complexity. The first win is creating a file the browser can read.

## IIM Alignment

Week 1 Monday:

- Establish web page as a structured document, not "code" in the abstract.
- Introduce HTML as meaning and structure, not appearance.
- Show full page lifecycle: file -> browser -> render.

## Reading Alignment

Week 1 assigned reading:

- Required - HTML/CSS: Duckett Chap 1 - Structure, pp. 8-28
- Required - HTML/CSS: Duckett Chap 2 - Text, selected pages on headings and paragraphs, pp. 40-60
- Required - HTML/CSS: Duckett Chap 4 - Links, selected pages on basic links and relative paths, pp. 74-92
- Reference - HTML/CSS: Duckett Chap 3 - Lists, pp. 62-72, use only if needed for the list requirement

Reading-to-lab bridge:

- Reading gives vocabulary: element, tag, attribute, heading, paragraph, link, href, relative path.
- Lecture shows the file-to-browser cycle and the first page structure.
- Tuesday lab turns that into the first working page.
- Wednesday and Thursday grow that first page toward the small multi-page site.

What students should not try to master yet:

- every HTML element
- CSS styling
- JavaScript behavior
- professional site design

## Prior Work Bridge

There is no previous web lab to review in Week 1.

Use this space for course setup and first-contact reassurance:

- We are starting from zero.
- Imperfect first versions are expected.
- The first goal is that a page exists and opens.

## Today's Working Set

Today we will use:

- `index.html`
- `<!doctype html>`
- `<html>`, `<head>`, `<title>`, `<body>`
- `<h1>`
- `<p>`
- save and refresh

Today we will not use yet:

- CSS
- JavaScript
- layout tools
- image assets
- frameworks

## Assignment Supported

Assignment 1 - HTML Multi-Page Site

Monday supports Iteration 1:

- create the first project folder and `index.html` file
- organize content with headings and paragraphs
- practice save/open/refresh
- understand that "ugly but working" is acceptable this week

## Readiness Target

By the end of the session, students should be able to:

- create an `index.html` file
- type a minimal HTML page
- open the file in a browser
- explain the difference between the browser tab title and the visible page heading
- change content, save, and refresh

## Primary Watch Point

Students may judge success by appearance. Redirect them:

```text
This week, working structure beats visual polish.
```

## Demo Set

Demo folder:

```text
Demos/Week_01_HTML_Multi_Page_Site/01_monday_hello_world/
```

Demo files:

- `index.html`
- `demo_notes.md`

Delivery:

- Type the full file live.
- Save and refresh after meaningful changes.
- Use the finished file only as a reference state.

## Slide Sequence Overview

1. Something Exists
2. What This Course Builds
3. HTML Is Structure
4. File To Browser
5. Today's Toolbox
6. Parked For Later
7. The Smallest Useful Page
8. Demo Setup
9. Demo: First Page
10. What The Browser Did
11. Title Versus Heading
12. Working Beats Pretty
13. Common Week 1 Mistakes
14. Tuesday Lab Bridge
15. Evidence To Preserve
16. Closing Success Target

## Slide-By-Slide Source

### Slide 1 - Opening Frame

Student-visible text:

```text
Build something that exists.

- A web page starts as a file.
- The browser reads that file.
- If the page opens, the first goal is met.
- Visual polish comes later.
```

**Instructor notes:**

- Start with pressure reduction.
- Say that professional-looking pages come later.
- Today's success condition is visible existence in a browser.

**Transition cue:**

- "Before we make it pretty or interactive, the browser needs something real to read."

Visual notes:

- Split visual: blank file on left, simple browser page on right.
- The right side should look plain and unstyled.

### Slide 2 - Course Layer Map

Student-visible text:

```text
Web pages have layers:

- HTML gives content structure.
- CSS controls appearance.
- JavaScript adds behavior.

Today: HTML only.
```

**Instructor notes:**

- Establish the course's separation of concerns.
- HTML comes first because CSS and JavaScript need something to attach to.
- Avoid going into CSS/JS details.

**Transition cue:**

- "Today we only work in the first layer."

Visual notes:

- Three stacked layers or stepping stones.
- Highlight HTML; dim CSS and JavaScript.

### Slide 3 - Core Idea

Student-visible text:

```text
HTML gives content meaning.

- A heading means "this is a heading."
- A paragraph means "this is body text."
- A link means "go somewhere."

HTML is not responsible for making the page look finished.
```

**Instructor notes:**

- Explain heading, paragraph, and link as meaning.
- Appearance will feel unfinished because CSS has not arrived yet.

**Transition cue:**

- "So what does a meaningful page look like as a file?"

Visual notes:

- Show simple content labels: heading, paragraph, link.

### Slide 4 - File To Browser

Student-visible text:

```text
File -> Save -> Browser -> Refresh

- The file stores the structure.
- Save writes your changes.
- The browser reads the saved file.
- Refresh shows the latest saved version.
```

**Instructor notes:**

- This is the first development loop.
- Students need to see that the browser does not magically know unsaved changes.

**Transition cue:**

- "Let's look at the minimum file the browser can understand."

Visual notes:

- Process diagram with four steps.

### Slide 5 - Today's Toolbox

Student-visible text:

```text
Today's toolbox:

- `index.html`
- `<!doctype html>`
- `html`, `head`, `title`, `body`
- `h1` and `p`
- save and refresh
```

**Instructor notes:**

- Use this as the scope boundary before the first code demo.
- Keep the visible focus on active tools only.
- Keep the tone calm and practical.

**Transition cue:**

- "That also means a few tempting tools are intentionally not in our hands yet."

Visual notes:

- Toolbox or workbench with today's active HTML tools.

### Slide 6 - Parked For Later

Student-visible text:

```text
Parked for later:

- CSS will handle appearance.
- JavaScript will handle behavior.
- Layout tools will help arrange pages.
- Frameworks and publishing come much later.

Today, the win is HTML structure that opens.
```

**Instructor notes:**

- Explain that parked topics are not forbidden or scary; they are simply not today's job.
- Use this to reduce the common beginner urge to style before the structure works.
- Name this as separation of concerns by example: active tools and deferred tools stay separate.

**Transition cue:**

- "Now let's see the shape today's tools create."

Visual notes:

- Separate calm bookshelf, shelf, or parking area visual.
- Do not combine this with the toolbox image.

### Slide 7 - The Smallest Useful Page

Student-visible text:

```text
Every first page needs a shape.

- `<!doctype html>` tells the browser what kind of document this is.
- `head` stores page information.
- `body` stores visible content.
- The browser uses the shape to understand the page.
```

**Instructor notes:**

- Keep this conceptual.
- The exact typing happens in the demo.

**Transition cue:**

- "Now we will build that shape from nothing."

Visual notes:

- Simple outline of `html`, `head`, and `body` as nested boxes.

### Slide 8 - Demo Setup

Student-visible text:

```text
Demo: index.html

Watch for:

- file name: `index.html`
- save before refresh
- browser tab title
- visible page heading

Goal: one page that opens in the browser.
```

**Instructor notes:**

- Create a new folder and file.
- Narrate file naming: `index.html` is the common home page name.
- Do not mention hosting/deployment.

**Transition cue:**

- "I am going to type this slowly enough that the shape is visible."

Visual notes:

- Screenshot-style workspace: file explorer, editor, browser.

Demo connection:

- `01_monday_hello_world/index.html`

### Slide 9 - Demo: First Page

Student-visible text:

```text
Type. Save. Refresh. Observe.

- Type the structure.
- Save the file.
- Open or refresh the browser.
- Change one line and confirm the browser updates.
```

**Instructor notes:**

- Type:
  - `<!doctype html>`
  - `<html lang="en">`
  - `<head>`
  - `<meta charset="utf-8">`
  - `<title>Hello World</title>`
  - `<body>`
  - `<h1>Hello World</h1>`
  - `<p>This is my first web page.</p>`
- Save and open in browser.
- Change one line and refresh.

**Transition cue:**

- "Now that it exists, what exactly did the browser use?"

Visual notes:

- No generated image needed. Use live editor/browser.

### Slide 10 - What The Browser Did

Student-visible text:

```text
The browser did not guess.

- `<title>` became the browser tab label.
- `<h1>` became the visible page heading.
- `<p>` became visible paragraph text.
- The result came from the saved HTML structure.
```

**Instructor notes:**

- Reinforce that HTML is interpreted by the browser.
- Avoid making this mystical.

**Transition cue:**

- "One early confusion is the difference between two different 'titles.'"

Visual notes:

- Browser tab label callout and page heading callout.

### Slide 11 - Title Versus Heading

Student-visible text:

```text
`<title>` names the browser tab.
`<h1>` names the page content.

Common confusion:

- The title may not appear inside the page.
- The heading may not appear in the browser tab.
- Both are useful, but they do different jobs.
```

**Instructor notes:**

- Show both in the demo.
- This small distinction prevents lots of beginner confusion.

**Transition cue:**

- "This page is not impressive. That is fine."

Visual notes:

- Two callouts: tab title and visible `h1`.

### Slide 12 - Contrast

Student-visible text:

```text
Working beats pretty.
This week, every time.

Prioritize:

- the file opens
- the content is structured
- the links work
- the page can be changed and refreshed
```

**Instructor notes:**

- Explicitly tell students not to chase styling.
- A plain working page is a success.

**Transition cue:**

- "Here is what usually goes wrong in Week 1."

Visual notes:

- Side-by-side: plain working page versus decorative but broken page.

### Slide 13 - Common Week 1 Mistakes

Student-visible text:

```text
Common mistakes:

- unsaved file
- wrong file name
- broken tag pair
- expecting CSS

Fix one small thing, then refresh and check again.
```

**Instructor notes:**

- Explain each briefly.
- Keep the tone normal: mistakes are part of the loop.

**Transition cue:**

- "The lab takes this from one page to a small connected site."

Visual notes:

- Checklist with calm repair icons.

### Slide 14 - Tuesday Lab Bridge

Student-visible text:

```text
Tuesday lab:
Start the first page.

- create the project folder
- create `index.html`
- add a heading and paragraph
- save, open, refresh, and revise

Do not worry about the full site yet.
```

**Instructor notes:**

- Emphasize that Tuesday is the first build loop, not the full endpoint.
- Students need one working page before the multi-page assignment makes sense.
- Preview only lightly that Wednesday will show how one page grows into a site.

**Transition cue:**

- "What evidence should you preserve as you work?"

Visual notes:

- One project folder with `index.html` and a plain browser page.

Lab connection:

- `Assignments/1_HTML_Multi-Page_Site.md`

### Slide 15 - Evidence To Preserve

Student-visible text:

```text
Evidence:

- your project folder
- your `index.html` file
- a page that opens in the browser
- notes about what changed

The full reflection comes after the site has been refined.
```

**Instructor notes:**

- Keep evidence expectations limited to the first lab moment.
- Do not ask students to prove navigation before Wednesday introduces it.
- Mention that later evidence will include multiple pages and the final reflection.

**Transition cue:**

- "Wednesday continues this same site by improving structure and navigation."

Visual notes:

- Folder containing one HTML file plus a simple browser result.

### Slide 16 - Closing Success Target

Student-visible text:

```text
If your page opens,
and the structure makes sense,
you are on track.

Week 1 success is:

- visible page
- clear structure
- saved files
- working links beginning to form
```

**Instructor notes:**

- Close with confidence.
- Re-state: ugly is not failure in Week 1.
- Mention that Wednesday will continue the same site by adding structure and navigation.

**Transition cue:**

- End.

Visual notes:

- Simple browser window showing an unstyled but readable page.

## Demo Execution Notes

Type live:

- full `index.html`
- visible `h1` and `p`
- one small content change after first browser view

May paste:

- nothing required; demo is short enough to type fully

Inspect:

- browser tab title
- page heading
- saved change after refresh

Likely mistake to show only if time allows:

- change file but do not save before refresh

## Lab / Assignment Bridge

Tuesday lab begins Assignment 1 Iteration 1.

Monday only needs to show the first file and first browser loop.

The full multi-page assignment target belongs in the Wednesday recording after
students have seen one page become a small site.

## Evidence / Submission Expectations

For Tuesday's first build:

- one organized folder
- `index.html`
- a page that opens in the browser
- evidence of save/refresh/revise

The final submission requirements are reinforced in Wednesday's recording.

## AI-Use Boundary

No AI use is needed for this first build.

Student expectation:

- type the first structures manually
- practice file/save/refresh
- ask for help when the browser does not show expected changes

## Image Prompt Notes

See:

```text
Lecture_Deck_Sources/Week_01_Image_Prompts.md
```

Priority images:

- file-to-browser lifecycle
- HTML/CSS/JS layer map
- plain working page versus decorative broken page
- today's toolbox and parked-for-later scope boundary

## Instructor Timing Notes

Compressible:

- Slide 2 if students already understand course layers
- Slide 11 if demo time runs long

Do not compress:

- demo typing
- title versus heading distinction
- Assignment 1 bridge

Likely pause points:

- after first browser render
- after changing content and refreshing

## Post-Lecture Notes

After teaching, record:

- Which setup issue appeared most often?
- Did students understand save/refresh?
- Did any students try to jump into CSS?
- Should Wednesday emphasize file paths more strongly?
