# W02B CSS Refinement Recorded

## Deck Metadata

- Course: 10-152-118 Web Development Foundations
- Alternate title: HTML, CSS, and JavaScript
- Week: 2
- Session: Wednesday recorded
- Deck title: CSS Refinement: One Stylesheet, Consistent Pages
- Phase: Foundations
- Target duration: 25-35 minutes
- Recording expected: yes

## Session Type

Wednesday recorded lecture.

## Lesson Purpose

Students should see Monday's first stylesheet grow into a shared styling layer
that supports multiple pages.

The instructional move is refinement:

```text
one page styled -> stylesheet reused -> pages feel consistent
```

## IIM Alignment

Week 2 Wednesday:

- Introduce specificity basics.
- Address common mistakes such as overwriting styles or confusion about why a rule applies.
- Support Thursday lab refinement: visual consistency, readability, spacing, and design intention.

## Reading Alignment

Week 2 assigned reading:

- Required - HTML/CSS: Duckett Chap 10 - Introducing CSS, pp. 226-244
- Required - HTML/CSS: Duckett Chap 11 - Color, pp. 246-262
- Skim - HTML/CSS: Duckett Chap 12 - Text, selected pages on font size and readability, pp. 264-286
- Reference - HTML/CSS: Duckett Chap 12 - Text, selected pages on font size and readability, pp. 287-298

What this recording reinforces:

- one external stylesheet can support more than one page
- selectors decide which HTML receives a style
- class names let repeated parts share styling
- readability and consistency matter more than decoration

What students should not try to master yet:

- full cascade theory
- advanced specificity conflicts
- full box model mastery
- Flexbox or responsive layout
- professional design systems

## Review / Prior Work Bridge

Monday introduced:

```text
index.html -> styles.css -> visible style changes
```

Wednesday grows that first CSS connection into:

```text
index.html + about.html -> one shared styles.css
```

## What Counts As Success Today

By the end of the recording, students should be able to:

- link the same stylesheet from more than one page
- recognize one reusable class name
- explain how one CSS change can affect multiple pages
- identify whether a styling issue is a link problem, selector problem, or readability problem

Success is consistent improvement, not visual perfection.

## Today's Toolbox

Today we will use:

- shared `styles.css`
- stylesheet link on multiple pages
- class selector
- `.site-header`
- `.nav-list`
- `.page`
- margin and padding
- color and contrast checks

## Parked For Later

Parked for later:

- detailed specificity math
- full box model depth
- Flexbox layout
- media queries
- design frameworks

Today, the goal is a consistent CSS layer across pages.

## Assignment Supported

Assignment 2 - Styling & Visual Design

Wednesday supports the concept focus and Thursday refinement:

- consistent styling across pages
- readable typography
- usable color choices
- intentional spacing
- at least one class-based style
- consistent navigation styling

## Readiness Target

By the end of the recording, students should be ready to:

- copy the stylesheet link intentionally across pages
- use class names for repeated page regions
- adjust one CSS value and check the result on multiple pages
- refine readability and consistency before adding more decoration

## Primary Watch Point

Students may treat CSS as page-by-page decoration rather than a shared system.

Reframe:

```text
One stylesheet can make several pages feel like one site.
```

## Demo Set

Demo folder:

```text
Demos/Week_02_CSS_Appearance/02_wednesday_shared_stylesheet/
```

Demo files:

- `index.html`
- `about.html`
- `styles.css`
- `demo_notes.md`

Delivery:

- Start from the Monday first-styles idea.
- Show or add the stylesheet link on multiple pages.
- Type or inspect class names and shared rules.
- Change one CSS value and inspect both pages.

## Slide Sequence Overview

1. Reconnect To Monday
2. From Styled Page To Styled Site
3. What Counts As Success Today
4. One Stylesheet Can Serve Many Pages
5. Class Names Mark Reusable Parts
6. Specificity, Gently
7. Demo: Shared Stylesheet
8. Inspect The Result
9. Common CSS Refinement Mistakes
10. Thursday Lab Refinement
11. Evidence And Reflection
12. How To Read Next Week's Material
13. Closing

## Slide-By-Slide Source

### Slide 1 - Reconnect To Monday

Student-visible text:

```text
Monday:
- one page linked to CSS
- one rule made a visible change

Today:
- one stylesheet supports multiple pages
- styling becomes more consistent
```

**Instructor notes:**

- Make the continuity explicit.
- This is not a new start; it is the same CSS idea reused.
- Keep the recording self-contained for students who need to rewatch.

**Transition cue:**

- "A site should not feel like separate pages wearing unrelated outfits."

Visual notes:

- One styled page becoming two similarly styled pages.

### Slide 2 - From Styled Page To Styled Site

Student-visible text:

```text
A styled site needs consistency.

- pages should feel related
- navigation should look familiar
- headings should have a pattern
- spacing should feel intentional

Consistency helps users trust where they are.
```

**Instructor notes:**

- Use "feel related" in a beginner-friendly way.
- Keep design judgment practical: readability, navigation, hierarchy.
- Avoid design theory depth.

**Transition cue:**

- "So today's success target is not more decoration. It is consistent improvement."

Visual notes:

- Two page cards with matching header/nav styling.

### Slide 3 - What Counts As Success Today

Student-visible text:

```text
What counts as success today:

- the same CSS file styles more than one page
- navigation looks consistent
- text is readable
- spacing is less crowded
- one class-based style is used on purpose
```

**Instructor notes:**

- This names the full weekly target more clearly than Monday because students have seen first CSS connection.
- Keep "class-based style" at useful recognition depth.
- Do not require polished visual design.

**Transition cue:**

- "The main tool for consistency is a shared stylesheet."

Visual notes:

- Success checklist.

### Slide 4 - One Stylesheet Can Serve Many Pages

Student-visible text:

```text
Each page links to the same CSS file.

index.html  -> styles.css
about.html  -> styles.css
tips.html   -> styles.css

Change one CSS rule.
Check every page that uses it.
```

**Instructor notes:**

- Students may think each page needs its own CSS file.
- Explain that multiple pages can share the same `href`.
- Connect to maintainability without overusing the term.

**Transition cue:**

- "Shared styling works best when repeated parts have names."

Visual notes:

- Several HTML files pointing to one `styles.css`.

### Slide 5 - Class Names Mark Reusable Parts

Student-visible text:

```text
Class names help CSS find repeated parts.

HTML:
<header class="site-header">

CSS:
.site-header {
  background: #204b57;
}

The dot in CSS means class.
```

**Instructor notes:**

- Keep the difference clear: HTML uses `class="..."`; CSS uses `.class-name`.
- Use class names as a way to name page parts, not as an abstraction lecture.
- Mention IDs only as recognition if needed; do not make IDs central today.

**Transition cue:**

- "Now we need one gentle rule about which style wins."

Visual notes:

- Side-by-side HTML class attribute and CSS class selector.

### Slide 6 - Specificity, Gently

Student-visible text:

```text
When two rules could apply,
the browser must choose.

Beginner version:

- more specific selectors usually win
- later rules may override earlier ones
- class selectors target named parts
- inspect the rule before guessing
```

**Instructor notes:**

- Keep this intentionally gentle.
- Do not teach full specificity math.
- The goal is recognition: CSS conflicts are not random.

**Transition cue:**

- "Let's see a shared stylesheet and class names working together."

Visual notes:

- Two CSS rules pointing at one element, with "browser chooses" callout.

### Slide 7 - Demo: Shared Stylesheet

Student-visible text:

```text
Demo: shared stylesheet

Watch for:
- same CSS link on multiple pages
- class names in HTML
- shared rules in `styles.css`
- one change affecting more than one page
- navigation becoming consistent
```

**Instructor notes:**

- Use `Demos/Week_02_CSS_Appearance/02_wednesday_shared_stylesheet/`.
- Briefly recall the Monday first-styles demo.
- Inspect `index.html`, `about.html`, and `styles.css`.
- Change one value such as `.site-header` background or `.page` max width and refresh both pages.
- Keep it to one demo slide unless the recording feels rushed.

**Transition cue:**

- "The important question is not only whether it looks nicer, but what became more consistent."

Visual notes:

- Live editor/browser; no generated image needed.

Demo connection:

- `Demos/Week_02_CSS_Appearance/02_wednesday_shared_stylesheet/index.html`
- `Demos/Week_02_CSS_Appearance/02_wednesday_shared_stylesheet/about.html`
- `Demos/Week_02_CSS_Appearance/02_wednesday_shared_stylesheet/styles.css`

### Slide 8 - Inspect The Result

Student-visible text:

```text
Inspect after styling:

- Do both pages still open?
- Is the stylesheet linked?
- Does navigation look consistent?
- Is text easier to read?
- Did spacing improve?
```

**Instructor notes:**

- Model browser inspection as a habit.
- Readability is more important than color preference.
- Students should check multiple pages, not only the page they edited.

**Transition cue:**

- "When something looks wrong, start with the simplest possible cause."

Visual notes:

- Browser checklist over two page views.

### Slide 9 - Common CSS Refinement Mistakes

Student-visible text:

```text
Common refinement mistakes:

- linking CSS on one page only
- changing HTML just to make space
- using random colors
- making text harder to read
- using inline styles everywhere
- forgetting to check every page
```

**Instructor notes:**

- Tie directly to Assignment 2 instructor notes.
- Use "random color usage" carefully and practically.
- Encourage restrained, intentional improvement.

**Transition cue:**

- "Thursday is where you use this checklist on your own site."

Visual notes:

- Calm warning list with repair-oriented tone.

### Slide 10 - Thursday Lab Refinement

Student-visible text:

```text
Thursday:
Refine the styling layer.

- link one CSS file across pages
- improve readability
- make navigation consistent
- adjust spacing
- use at least one class-based style

Do not add JavaScript yet.
```

**Instructor notes:**

- This is the full Assignment 2 target.
- Name the final expectations now because students have the needed CSS mental model.
- Keep JavaScript out of scope.

**Transition cue:**

- "Your final evidence should show both the files and the design reasoning."

Visual notes:

- Before/after site cards with the same structure and improved styling.

Lab connection:

- `Assignments/2_Styling_&_Visual_Design.md`

### Slide 11 - Evidence And Reflection

Student-visible text:

```text
Submit:

- HTML files
- `styles.css`
- pages that render correctly
- visible consistency across pages
- 2-3 sentence reflection

Reflection:
What design changes improved readability or usability?
```

**Instructor notes:**

- Reinforce that CSS must be in a separate file.
- Reflection should explain why changes helped, not just list colors.
- Mention that screenshots may help students verify before submission if useful.

**Transition cue:**

- "Next week, we start thinking about space more deliberately."

Visual notes:

- Folder with HTML files, CSS file, and short reflection note.

### Slide 12 - How To Read Next Week's Material

Student-visible text:

```text
How to read Week 3:

Required: understand boxes and spacing.
Skim: layout examples for the big idea.
Reference: return during lab for Flexbox/media queries.

Focus on:
- margin, padding, border
- elements as boxes
- layout as controlled space

Do not memorize every layout technique.
```

**Instructor notes:**

- Week 3 readings:
  - Chap 13 Boxes, pp. 300-328
  - Chap 15 Layout, pp. 358-404 as skim
  - MDN Flexbox and Media Queries as reference
- Tell students that Week 3 moves from appearance to space.

**Transition cue:**

- "This week CSS made the site look consistent. Next week CSS helps control space."

Visual notes:

- Reading labels as Required, Skim, Reference cards.

### Slide 13 - Closing

Student-visible text:

```text
If one stylesheet supports the site,
the pages are readable,
and the design choices are intentional,
your CSS layer is doing its job.
```

**Instructor notes:**

- Close with the layer language again.
- Reassure students that restraint is acceptable.
- End with Thursday refinement focus.

**Transition cue:**

- End.

Visual notes:

- Three page cards connected to one stylesheet with a check mark.

## Demo Execution Notes

Type or inspect:

- stylesheet link in `index.html`
- stylesheet link in `about.html`
- `class="site-header"`
- `class="nav-list"`
- `class="page"`
- `.site-header`, `.nav-list`, and `.page` rules

May paste:

- larger CSS rule groups after explaining the selector and purpose

Inspect:

- both pages in browser
- one CSS change affecting more than one page
- navigation consistency
- readability and spacing

Optional deliberate mistake:

- remove the stylesheet link from one page and compare the result.

## Lab / Assignment Bridge

Thursday lab is Assignment 2 Iteration 2:

- improve styling consistency across all pages
- use one external CSS file
- improve readability, spacing, color, and navigation
- use at least one class-based style
- keep the project HTML/CSS only

## Evidence / Submission Expectations

Students submit:

- updated HTML files
- `styles.css`
- organized project folder
- working pages that render correctly
- short reflection explaining design changes and their effect on readability or usability

## AI-Use Boundary

AI use is not needed for Assignment 2, but students may ask for explanation
after they have attempted their own CSS.

Appropriate support:

- explain why a selector did not apply
- compare two color choices for readability
- suggest what to inspect next

AI should not generate the whole stylesheet as a substitute for the student's
own first CSS layer.

## Image Prompt Notes

Generate image prompts only after this Week 2 deck source is approved.

Likely useful visuals:

- multiple HTML pages connected to one stylesheet
- class attribute and class selector comparison
- gentle specificity visual
- consistency before/after across multiple pages
- Week 3 boxes/spacing reading preview

## Recording Notes

Target recording length:

- 25-35 minutes

Self-contained transitions:

- reconnect to Monday's first stylesheet
- name shared stylesheet as the deepening move
- pause after one CSS change affects multiple pages
- leave students with Thursday refinement checklist

Compressible:

- Slide 6 if specificity feels heavy
- repeated HTML inspection if demo time runs long

Do not compress:

- shared stylesheet concept
- class selector distinction
- Thursday full assignment bridge
- next-reading guidance

## Post-Recording Notes

After recording, record:

- Did shared stylesheet reuse feel clear?
- Did specificity stay gentle enough?
- Did the class selector explanation land?
- Is Thursday's refinement target clear without making design feel overwhelming?
