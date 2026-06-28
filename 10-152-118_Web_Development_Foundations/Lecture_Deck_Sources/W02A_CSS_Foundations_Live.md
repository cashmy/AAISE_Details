# W02A CSS Foundations Live

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 2
- Session: Monday live
- Deck title: CSS Foundations: I Can Control Appearance
- Phase: Foundations
- Target duration: 55-70 minutes
- Recording expected: no

## Session Type

Monday live lecture.

## Lesson Purpose

Students should leave Monday understanding that CSS is a separate appearance
layer added to existing HTML structure.

The practical target is modest: connect one external stylesheet, make visible
style changes, and explain that the HTML meaning did not change.

## IIM Alignment

Week 2 Monday:

- Introduce CSS as a separate layer.
- Emphasize: HTML is not styling.
- Introduce basic selectors, classes, and IDs at a recognition level.

## Reading Alignment

Week 2 assigned reading:

- Required - HTML/CSS: Duckett Chap 10 - Introducing CSS, pp. 226-244
- Required - HTML/CSS: Duckett Chap 11 - Color, pp. 246-262
- Skim - HTML/CSS: Duckett Chap 12 - Text, selected pages on font size and readability, pp. 264-286
- Reference - HTML/CSS: Duckett Chap 12 - Text, selected pages on font size and readability, pp. 287-298

Reading-to-lab bridge:

- Reading gives vocabulary: CSS rule, selector, property, value, stylesheet, color, font, class, id.
- Lecture shows how an external stylesheet connects to HTML.
- Tuesday lab applies the first styling layer to the existing Week 1 site.

What students should not try to master yet:

- every CSS property
- advanced layout
- responsive design
- professional visual design
- JavaScript behavior

## Review / Prior Work Bridge

Previous lab:

- Assignment 1 - HTML Multi-Page Site

Success solution:

```text
Assignments/Success_Solutions/Week_01_HTML_Multi_Page_Site/
```

Review focus:

- show one successful path, not the only correct answer
- click through the site navigation
- point out clear headings, paragraphs, lists, and semantic regions
- emphasize that Week 1 success was structure without CSS
- connect the HTML-only site to today's question: how do we change its appearance?

## What Counts As Success Today

By the end of the session, students should be able to:

- link one external CSS file to one HTML page
- make one visible style change
- explain that CSS changes appearance, not meaning
- save, refresh, and identify whether the stylesheet is connected

Success is not a polished design today.

## Today's Toolbox

Today we will use:

- `styles.css`
- `<link rel="stylesheet" href="styles.css">`
- selector
- property
- value
- `body`, `h1`, `p`, `a`
- save and refresh

## Parked For Later

Parked for later:

- Flexbox and layout systems
- responsive design
- animation
- design frameworks
- JavaScript behavior

Today, the win is a stylesheet that visibly changes existing HTML.

## Assignment Supported

Assignment 2 - Styling & Visual Design

Monday supports Iteration 1:

- create one external CSS file
- link it to existing HTML
- apply first text, color, and spacing rules
- verify the page remains readable

The full visual-consistency target belongs in the Wednesday recording and Thursday refinement.

## Readiness Target

By the end of Monday, students should be ready to:

- add `styles.css` to their project folder
- link the stylesheet from at least one page
- write simple element selectors
- change font, color, background, and spacing in a controlled way
- notice when a style does not apply because the stylesheet is not linked

## Primary Watch Point

Students may try to rebuild the HTML or chase attractive colors before the CSS
connection works.

Redirect:

```text
First prove the CSS file is connected.
Then improve appearance one rule at a time.
```

## Demo Set

Demo folder:

```text
Demos/Week_02_CSS_Appearance/01_monday_first_styles/
```

Demo files:

- `index.html`
- `styles.css`
- `demo_notes.md`

Delivery:

- Type the stylesheet link and first CSS rules live.
- Save and refresh after each visible change.
- Keep the demo to one page.

## Slide Sequence Overview

1. From Structure To Appearance
2. Previous Lab Review: One Successful HTML Path
3. What Week 1 Proved
4. CSS Is A Separate Layer
5. What Counts As Success Today
6. Today's Toolbox
7. Parked For Later
8. A CSS Rule Has Parts
9. External Stylesheet Connection
10. Demo: First Styles
11. What Changed And What Did Not
12. Common Week 2 Mistakes
13. Tuesday Lab Bridge
14. Evidence To Preserve
15. Closing Success Target

## Slide-By-Slide Source

### Slide 1 - From Structure To Appearance

Student-visible text:

```text
Last week:
- HTML made the site exist.
- Structure gave content meaning.

This week:
- CSS changes how that structure appears.
- We add a new layer.
```

**Instructor notes:**

- Frame Week 2 as continuation, not restart.
- Use the phrase "add a layer" early.
- Avoid making CSS sound like decoration only; it affects readability and usability.

**Transition cue:**

- "Before we add the new layer, let's look at one successful HTML-only path."

Visual notes:

- HTML structure layer with CSS appearance layer added above it.

### Slide 2 - Previous Lab Review: One Successful HTML Path

Student-visible text:

```text
One successful Week 1 path:

- at least three pages
- clear headings and paragraphs
- lists where useful
- navigation between pages
- semantic regions

This is one acceptable path, not the only answer.
```

**Instructor notes:**

- Open `Assignments/Success_Solutions/Week_01_HTML_Multi_Page_Site/success_solution/index.html`.
- Click through `tips.html` and `schedule.html`.
- Keep the review concise; the purpose is to bridge, not reteach Week 1.
- Normalize revision and recovery.

**Transition cue:**

- "This structure works. Now we can ask how the experience should feel."

Visual notes:

- Browser view of the Study Sprint site, then one quick file view.

### Slide 3 - What Week 1 Proved

Student-visible text:

```text
Week 1 proved:

- the browser can read your files
- pages can link to each other
- headings and sections create meaning
- plain can still be correct

CSS should improve the experience without replacing the structure.
```

**Instructor notes:**

- Emphasize that Week 2 builds on the same site.
- Students should not delete working HTML to "start over."
- This slide protects continuity.

**Transition cue:**

- "That gives us the boundary: HTML keeps meaning; CSS changes presentation."

Visual notes:

- Plain HTML page with a label: "structure already exists."

### Slide 4 - CSS Is A Separate Layer

Student-visible text:

```text
CSS controls appearance.

- color
- font
- spacing
- readable line length
- visual consistency

HTML still controls structure and meaning.
```

**Instructor notes:**

- Tie directly to reading: CSS styles HTML; it does not replace HTML.
- Say "separate layer" more than once.
- Avoid going into the cascade deeply today.

**Transition cue:**

- "So what counts as success for our first day with CSS?"

Visual notes:

- Same HTML document with CSS layer affecting appearance.

### Slide 5 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- one stylesheet is connected
- one rule visibly changes the page
- you can name the selector
- you can name one property and value
- the page remains readable
```

**Instructor notes:**

- Keep this intentionally smaller than the full Assignment 2 endpoint.
- Reinforce that attractive design comes after the connection works.
- Make "visible change" the first confidence target.

**Transition cue:**

- "Here are the tools we need for that first visible change."

Visual notes:

- Success checklist, not a rubric.

### Slide 6 - Today's Toolbox

Student-visible text:

```text
Today's toolbox:

- `styles.css`
- stylesheet link
- selector
- property
- value
- save and refresh
```

**Instructor notes:**

- This is the active set for Monday.
- Students may have read about many more properties; keep the working set narrow.
- Avoid class/id depth here; introduce recognition later.

**Transition cue:**

- "A few useful tools are parked because they solve problems we are not working on yet."

Visual notes:

- Toolbox or workbench with the listed active CSS tools only.

### Slide 7 - Parked For Later

Student-visible text:

```text
Parked for later:

- full layout systems
- Flexbox
- media queries
- animation
- JavaScript behavior

Today: connect CSS and make readable changes.
```

**Instructor notes:**

- Use this to reduce overload from the textbook and the web.
- Clarify that Flexbox and responsive design are coming soon, but not today.
- If time is tight, this can be compressed verbally.

**Transition cue:**

- "Now we can look at the smallest useful CSS unit: a rule."

Visual notes:

- Separate parked shelf visual, not combined with the toolbox.

### Slide 8 - A CSS Rule Has Parts

Student-visible text:

```text
A CSS rule has parts:

selector {
  property: value;
}

Example:

h1 {
  color: #204b57;
}
```

**Instructor notes:**

- Explain selector as "what to style."
- Explain property as "what part of appearance changes."
- Explain value as "the chosen setting."
- Do not teach every selector type today.

**Transition cue:**

- "The rule can only work if the HTML page knows where the stylesheet is."

Visual notes:

- Large annotated CSS rule.

### Slide 9 - External Stylesheet Connection

Student-visible text:

```text
The HTML page must link to the CSS file.

In `head`:

<link rel="stylesheet" href="styles.css">

If the link is wrong,
the CSS rules are ignored.
```

**Instructor notes:**

- Show that the link belongs in `head`, not `body`.
- Connect to Week 1 exact-file-name habit.
- Mention that `href` must match the CSS file name.

**Transition cue:**

- "Let's build the first stylesheet and prove the connection."

Visual notes:

- File pair: `index.html` connected to `styles.css`.

### Slide 10 - Demo: First Styles

Student-visible text:

```text
Demo: first styles

Watch for:
- stylesheet link
- first visible change
- one selector at a time
- save and refresh
- HTML content staying the same
```

**Instructor notes:**

- Use `Demos/Week_02_CSS_Appearance/01_monday_first_styles/`.
- Type the `link rel="stylesheet"` line if showing from scratch.
- Type `body`, `h1`, `p`, and `a` rules in small steps.
- Refresh after each meaningful change.
- If useful, temporarily break the `href` file name to show no styles apply.

**Transition cue:**

- "Now that the page looks different, let's name what actually changed."

Visual notes:

- Live editor/browser; no generated image needed.

Demo connection:

- `Demos/Week_02_CSS_Appearance/01_monday_first_styles/index.html`
- `Demos/Week_02_CSS_Appearance/01_monday_first_styles/styles.css`

### Slide 11 - What Changed And What Did Not

Student-visible text:

```text
CSS changed:

- text color
- background color
- font
- line length
- line spacing

CSS did not change:

- headings as headings
- paragraphs as paragraphs
- links as links
- page meaning
```

**Instructor notes:**

- Reinforce separation of concerns.
- Connect "appearance changed" to "meaning stayed stable."
- This is the key conceptual payoff of the demo.

**Transition cue:**

- "When CSS does not work, the problem is usually small and checkable."

Visual notes:

- Before/after view with stable HTML structure highlighted.

### Slide 12 - Common Week 2 Mistakes

Student-visible text:

```text
Common CSS mistakes:

- stylesheet not linked
- wrong file name
- missing `{ }`
- missing `:`
- missing `;`
- expecting unsaved changes to appear

Check connection first.
```

**Instructor notes:**

- Keep the tone normal and repair-oriented.
- Tie file-name mismatch back to Week 1 link problems.
- Do not turn this into a full debugging lecture; Week 6 handles deeper debugging.

**Transition cue:**

- "Tuesday lab starts with this same first styling layer."

Visual notes:

- Calm repair checklist.

### Slide 13 - Tuesday Lab Bridge

Student-visible text:

```text
Tuesday lab:
Add the first CSS layer.

- create `styles.css`
- link it to your site
- style text, color, and spacing
- keep the site readable
- do not rebuild the HTML
```

**Instructor notes:**

- This is Assignment 2 Iteration 1.
- Keep the endpoint scoped to first styling, not full visual consistency.
- Students may style one page first, then continue linking across pages as lab time allows.

**Transition cue:**

- "As you work, preserve evidence that the new layer is connected."

Visual notes:

- Existing HTML site plus new `styles.css` file.

Lab connection:

- `Assignments/2_Styling_&_Visual_Design.md`

### Slide 14 - Evidence To Preserve

Student-visible text:

```text
Evidence for the Lab:

- HTML files still open
- `styles.css` exists
- at least one page links to it
- visible style changes appear
- readability improves or stays clear
```

**Instructor notes:**

- Evidence is about connection and first visible changes.
- Thursday/Wednesday will reinforce full consistency across pages.
- Encourage students to notice what changed and why.

**Transition cue:**

- "Today, a simple connected stylesheet is enough."

Visual notes:

- Folder showing HTML files and `styles.css`.

### Slide 15 - Closing Success Target

Student-visible text:

```text
If CSS is linked,
one rule visibly works,
and the page is still readable,
you are on track.

Style is a layer.
Structure stays underneath.
```

**Instructor notes:**

- Close with confidence.
- Remind students that Week 2 starts simple and grows toward consistency.
- Mention that Wednesday will show how one stylesheet can support multiple pages.

**Transition cue:**

- End.

Visual notes:

- Simple HTML/CSS layer model.

## Demo Execution Notes

Type live:

- stylesheet link in `head`
- `body` rule
- `h1` rule
- `p` rule
- `a` rule

Inspect:

- browser before CSS
- browser after first rule
- effect of `max-width` and `line-height`
- whether HTML content remains recognizable

Optional deliberate mistake:

- rename `styles.css` in the `href` or omit the stylesheet link, then refresh.

## Lab / Assignment Bridge

Tuesday lab begins Assignment 2 Iteration 1.

Students should add a first CSS layer to their existing Week 1 site. The full
consistency target is reinforced in Wednesday's recording and Thursday lab.

## Evidence / Submission Expectations

For Tuesday's first build:

- existing HTML files remain organized
- `styles.css` exists
- stylesheet is linked from at least one page
- visible style changes appear
- students can explain one selector/property/value combination

Final submission requirements are reinforced in Wednesday's recording.

## AI-Use Boundary

No AI use is needed for the first CSS connection.

Student expectation:

- type the first CSS rules manually
- practice save/refresh
- ask for help when styles do not apply

AI can be useful later for explaining why a rule did not apply, but it should
not replace the first manual stylesheet connection.

## Image Prompt Notes

Generate image prompts only after this Week 2 deck source is approved.

Likely useful visuals:

- HTML structure layer with CSS appearance layer
- one stylesheet connected to one HTML page
- today's CSS toolbox
- parked-for-later shelf for layout/responsive/JavaScript
- before/after where structure stays the same but appearance changes

## Instructor Timing Notes

Compressible:

- Slide 7 if scope feels clear
- Slide 12 if demo time runs long

Do not compress:

- Week 1 success review
- stylesheet link
- first visible style change
- what changed / what did not

Likely pause points:

- after first CSS rule applies
- after a broken stylesheet link is shown or discussed

## Post-Lecture Notes

After teaching, record:

- Did students understand CSS as a separate layer?
- Did stylesheet linking cause issues?
- Did students try to rewrite HTML instead of styling it?
- Should Wednesday emphasize shared stylesheets, classes, or specificity more strongly?
