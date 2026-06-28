# Week 2 Image Generation Prompts

**10-152-118 Web Development Foundations**

---

# Purpose

This companion artifact expands the image notes from the Week 2 deck sources
into explicit image-generation prompts for browser-based ChatGPT image
generation.

Primary workflow:

- Copy one prompt block at a time into the browser-based ChatGPT image tool.
- Use Codex image generation only as a fallback if the browser image result is
  significantly unusable.
- Reject any image that makes Week 2 look like professional visual design
  mastery. Week 2 is about CSS as a separate appearance layer, first visible
  style changes, readability, and consistency.

Source decks:

- `W02A_CSS_Foundations_Live.md`
- `W02B_CSS_Refinement_Recorded.md`

Global style guidance:

- clean instructional PowerPoint visual
- white or very light background
- modern, flat, classroom-friendly style
- large readable labels
- minimal decorative detail
- restrained SWTC-friendly colors: navy, teal, warm gold, white, soft gray
- no complex screenshots unless requested
- no dense code blocks
- no polished portfolio or agency-style website mockups
- no futuristic, hacker, or AI-themed imagery

---

# Week 2 Monday Live Prompts

## W02A Slide 1 - From Structure To Appearance

```text
Create a clean instructional PowerPoint visual showing HTML structure gaining a CSS appearance layer.

Use a white or very light background. Show two simple layers:

Bottom layer: HTML - structure and meaning
Top layer: CSS - appearance and readability

Show a plain HTML document or page outline underneath, with a gentle visual styling layer placed above it. The image should communicate that CSS is added to existing structure, not a replacement for HTML.

Add a small note:
"Add a layer. Do not rebuild the structure."

Use large readable labels and a calm classroom-friendly flat style.

Avoid polished website mockups, advanced layout grids, JavaScript, frameworks, dark developer imagery, or anything that makes CSS look like a full design profession on day one.
```

## W02A Slide 2 - Successful HTML Path

```text
Create a clean instructional PowerPoint visual showing one successful HTML-only multi-page site from Week 1.

Use a white or very light background. Show three plain document cards connected by navigation arrows:

- Home
- Tips
- Schedule

Each card should suggest headings, paragraphs, and lists, but keep the pages intentionally unstyled. Add a small check mark near the connected navigation.

Add a small note:
"One successful path. Not the only answer."

The tone should support revision and recovery, not perfection.

Avoid CSS styling, colorful website design, complex sitemap diagrams, corporate navigation menus, or anything that implies students needed a polished site in Week 1.
```

## W02A Slide 6 - Today's Toolbox

```text
Create a clean instructional PowerPoint visual showing today's beginner CSS toolbox.

Use a white or very light background. Show a realistic toolbox or workbench with today's active tools:

- styles.css
- stylesheet link
- selector
- property
- value
- save
- refresh

Make the active tools visually available and approachable. The image should show only today's active tools.

Use large readable labels and a classroom-friendly flat style.

Avoid dense code, complicated IDE screenshots, dark developer imagery, polished website previews, Flexbox, media queries, animation, JavaScript, frameworks, or a "later" tray.
```

## W02A Slide 7 - Parked For Later

```text
Create a clean instructional PowerPoint visual showing topics parked for later in Week 2 Web Development Foundations.

Use a white or very light background. Show a calm bookshelf, shelf, or parking area with separate cards labeled:

- Flexbox
- media queries
- animation
- JavaScript
- design frameworks

Add a small note:
"Useful later. Not today's job."

The tone should be calm and reassuring. The visual should communicate separation of concerns: these topics matter, but they are intentionally outside today's active CSS toolbox.

Keep the labels large and readable. Use a classroom-friendly flat style with restrained navy, teal, warm gold, white, and soft gray.

Avoid warning signs, danger imagery, locked doors, red alarms, dark hacker aesthetics, dense code, or anything that makes the later topics look forbidden or bad.
```

## W02A Slide 8 - CSS Rule Parts

```text
Create a clean instructional PowerPoint visual explaining the parts of a CSS rule.

Use a white or very light background. Show one large readable CSS rule:

h1 {
  color: #204b57;
}

Use callouts:

- selector: h1
- property: color
- value: #204b57

Add a small note:
"Selector chooses. Property changes. Value sets."

Keep the code large and simple. The image should teach the shape of a rule, not overwhelm students with many examples.

Avoid dense CSS sheets, tiny code, advanced selectors, specificity math, browser DevTools, or decorative design mockups.
```

## W02A Slide 9 - External Stylesheet Connection

```text
Create a clean instructional PowerPoint visual showing an HTML page connected to an external CSS file.

Use a white or very light background. Show two file cards:

index.html
styles.css

Draw a clear connector from index.html to styles.css labeled:
<link rel="stylesheet" href="styles.css">

Add a small note:
"The file name must match."

Keep the visual simple and readable from a projector. The purpose is to show connection, not a full code listing.

Avoid folder trees with many files, server/cloud imagery, deployment concepts, complex IDE screenshots, or dense code.
```

## W02A Slide 11 - What Changed And What Did Not

```text
Create a clean instructional PowerPoint visual showing that CSS changes appearance while HTML meaning stays the same.

Use a white or very light background. Show a before-and-after pair of the same simple page:

Before: plain readable HTML page
After: same content with better color, font, spacing, and line length

Under both pages, show stable labels:

- heading stays heading
- paragraph stays paragraph
- link stays link

Add a small note:
"Appearance changed. Meaning stayed."

Avoid making the after version look like a polished professional website. Keep improvements restrained and beginner-level.
```

---

# Week 2 Wednesday Recorded Prompts

## W02B Slide 2 - From Styled Page To Styled Site

```text
Create a clean instructional PowerPoint visual showing one styled page growing into a consistently styled small site.

Use a white or very light background. On the left, show one simple styled page card labeled:
"One styled page"

On the right, show three page cards with similar header, navigation, color, and spacing labeled:
"Consistent small site"

Use a simple arrow from left to right. Keep the pages beginner-level, restrained, and readable.

Add a small note:
"Consistency makes pages feel related."

Avoid professional website previews, complex layouts, landing-page hero sections, design-system dashboards, or excessive visual polish.
```

## W02B Slide 4 - One Stylesheet Serves Many Pages

```text
Create a clean instructional PowerPoint visual showing several HTML pages connected to one shared stylesheet.

Use a white or very light background. Show three file cards on the left:

index.html
about.html
tips.html

Show one file card on the right:

styles.css

Draw arrows from each HTML file to styles.css. Add a small note:
"Change one CSS rule. Check every page."

Use large readable labels and a calm flat style.

Avoid server diagrams, build tools, cloud hosting, package managers, complex folder structures, or dense code.
```

## W02B Slide 5 - Class Names And Class Selectors

```text
Create a clean instructional PowerPoint visual comparing an HTML class attribute and a CSS class selector.

Use a white or very light background. Show two side-by-side cards:

Left card title: HTML
Content: <header class="site-header">

Right card title: CSS
Content: .site-header { background: #204b57; }

Add a callout:
"The dot in CSS means class."

Use large readable labels and keep the code snippets short.

Avoid long code blocks, advanced selector examples, specificity calculations, JavaScript, or browser DevTools screenshots.
```

## W02B Slide 6 - Specificity Gently

```text
Create a clean instructional PowerPoint visual showing that the browser chooses between CSS rules when more than one could apply.

Use a white or very light background. Show one simple HTML heading in the center. On the left, show a broad rule card labeled:
h1

On the right, show a more specific rule card labeled:
.site-header h1

Use a calm "browser chooses" callout between them. Add a small note:
"CSS conflicts are checkable, not random."

Keep this beginner-friendly and conceptual. Do not show specificity numbers.

Avoid full specificity math, dense code, advanced cascade diagrams, red error imagery, or anything that makes CSS feel intimidating.
```

## W02B Slide 8 - Inspect The Result

```text
Create a clean instructional PowerPoint visual showing a simple CSS refinement inspection checklist across two pages.

Use a white or very light background. Show two small page cards labeled:

Home
About

Beside them, show a checklist:

- both pages open
- stylesheet linked
- navigation consistent
- text readable
- spacing improved

Use calm check marks and restrained colors. The visual should communicate a practical inspection habit.

Avoid formal audit imagery, complex QA dashboards, professional design review scenes, or dense technical screenshots.
```

## W02B Slide 10 - Thursday Lab Refinement

```text
Create a clean instructional PowerPoint visual showing Thursday CSS refinement as improving an existing site, not rebuilding it.

Use a white or very light background. Show a before-and-after pair:

Before: same site with inconsistent spacing and navigation
After: same structure with more consistent navigation, better spacing, and readable text

Add a small note:
"Refine the styling layer. Keep the structure."

The after version should be restrained and beginner-level, not professionally designed.

Avoid dramatic redesign makeover imagery, complex layout grids, animation, JavaScript, framework logos, or polished agency-style mockups.
```

## W02B Slide 12 - How To Read Week 3

```text
Create a clean instructional PowerPoint visual previewing Week 3 reading about boxes and spacing.

Use a white or very light background. Show a simple box model concept:

content
padding
border
margin

Use large readable labels and gentle color bands. Add three small reading cards:

Required: boxes and spacing
Skim: layout examples
Reference: Flexbox and media queries

Add a small note:
"Next week: CSS controls space."

Avoid advanced layout dashboards, full responsive breakpoints, dense textbook pages, code-heavy diagrams, or polished web design mockups.
```

---

# Generation Priority

If time is limited, generate these first:

1. `w02_img_01_structure_to_appearance.png`
2. `w02_img_03_todays_css_toolbox.png`
3. `w02_img_06_stylesheet_connection.png`
4. `w02_img_09_one_stylesheet_many_pages.png`
5. `w02_img_10_class_selector.png`

Use live demo screenshots or direct browser/editor views for slides where code
inspection matters more than a concept visual.

Suggested filenames and alt text:

| Filename | Alt Text Intent |
|---|---|
| `w02_img_01_structure_to_appearance.png` | HTML structure gaining a separate CSS appearance layer. |
| `w02_img_02_successful_html_path.png` | Three plain HTML pages connected as one successful Week 1 site path. |
| `w02_img_03_todays_css_toolbox.png` | Beginner CSS toolbox showing active tools for Monday. |
| `w02_img_04_parked_for_later.png` | Flexbox, media queries, animation, JavaScript, and frameworks parked calmly for later. |
| `w02_img_05_css_rule_parts.png` | A CSS rule labeled with selector, property, and value. |
| `w02_img_06_stylesheet_connection.png` | An HTML file connected to an external stylesheet with a matching href. |
| `w02_img_07_appearance_changed_meaning_stayed.png` | Same HTML content before and after CSS, with meaning unchanged. |
| `w02_img_08_styled_page_to_site.png` | One styled page growing into a consistently styled small site. |
| `w02_img_09_one_stylesheet_many_pages.png` | Multiple HTML pages pointing to one shared stylesheet. |
| `w02_img_10_class_selector.png` | HTML class attribute compared with CSS class selector. |
| `w02_img_11_specificity_gently.png` | Browser choosing between a broad selector and a more specific selector. |
| `w02_img_12_inspect_result.png` | CSS refinement inspection checklist across two pages. |
| `w02_img_13_refine_styling_layer.png` | Existing site refined with better styling while structure remains. |
| `w02_img_14_week3_boxes_spacing.png` | Box model preview for Week 3 reading on spacing and layout. |

# Notes For PowerPoint Construction

- Do not place generated images where live code inspection is more useful.
- Keep images large and uncluttered.
- Add alt text based on the alt text intent table.
- If an image contains labels, verify they remain readable in slide view.
- Reject any image that makes Week 2 look like professional visual design mastery.
- Prefer restrained beginner-friendly before/after visuals over dramatic redesigns.
