# PowerPoint Deck Production Workflow

**Context:** AI-assisted course slide deck production  
**Primary Use:** Reproducing the lecture-deck construction process for later courses  
**Origin:** Python 117 and Algorithms slide-deck production experience  
**Status:** Reusable process artifact

---

# Purpose

This artifact preserves the practical workflow used to convert slide deck source
artifacts, image prompt artifacts, and AI-generated visuals into finished
PowerPoint lecture decks.

The exact slide sequence may vary by course. For example, Python and Algorithms
use different instructional rhythms. However, the production concept is
transferable:

1. begin with a consistent deck template
2. generate visuals from constrained prompts
3. assemble slides in controlled passes
4. add accessibility and instructor-support material
5. validate the final deck sequentially before publication

This workflow is intended for instructor production use, not student-facing
distribution.

---

# Phase 1 - Create The Template Deck

Create a reusable PowerPoint template deck for the course or course family.

The template should contain empty, preformatted slides with consistent layouts,
visual style, spacing, and presentation sequence. The template establishes the
visual and instructional rhythm before content is added.

For Python, the common sequence may include:

- intro slide with lecture title and subtitle
- lecture frame slide or slides
- review slide or slides from the previous lecture
- optional previous lab coding review
- today's success pattern
- today's toolbox items
- parked-for-later items
- lecture concept slides
- interspersed demo slides
- optional common failure slides
- lab assignment slide
- evidence slide
- optional AI-use or suggested-prompt slide
- success check slide
- thank-you slide
- blank image slide to copy for generated images

Template slides may include decorative images for visual interest. Any reusable
decorative images should already have appropriate alt text designated.

Important note:

The exact sequence should be adapted to the course. Algorithms may use a
different presentation structure than Python, but the template-first production
concept remains the same.

---

# Phase 2 - Create The Day-Level Lecture Decks

From the template deck, create each day-level lecture deck for the weekly topic.

Each lecture deck should begin as a copy of the template, then be shaped around
the specific deck source artifact for that day.

Do not begin by free-form building slides from scratch. The template preserves:

- visual consistency
- expected instructional sequence
- accessibility habits
- slide layout efficiency
- reduced production friction

---

# Phase 3 - Generate Images From Prompt Artifacts

Use the image prompt artifact for the lecture or week.

Recommended process:

1. Generate one image at a time.
2. Copy the specific image prompt into the browser-based image model.
3. Review the result against the slide purpose.
4. Edit or regenerate if the image is inaccurate, misleading, visually cluttered,
   or inconsistent with the lesson.
5. Save the accepted image in its own subfolder for easy discovery and reuse.

Use separate image folders by course, week, or lecture day when practical.

Images should support the concept. Do not accept an image merely because it is
visually attractive.

---

# Phase 4 - Insert Image Holding Slides

Perform image insertion as a controlled set of passes.

## Pass 1 - Copy Blank Image Slides

Copy the blank image slide once for each generated image.

Place these copied image slides at the end of the deck as a staging area.

## Pass 2 - Add Image Titles

Add the image title to each image slide using the slide title from the deck
source or image prompt artifact.

This makes the image staging area easier to manage before images are inserted.

## Pass 3 - Insert Images

Insert one generated image per staged image slide.

Do not move the image slides into their final deck positions yet unless the deck
is very small. Keeping them staged prevents sequence disruption during bulk
image insertion.

## Pass 4 - Generate Alt Text

Generate or write alt text for each inserted image.

PowerPoint's embedded AI may be used for draft alt text, but the instructor
should review it for instructional accuracy.

Alt text should describe the visual's teaching purpose, not merely list colors
or decorative features.

---

# Phase 5 - Build Instructional Slides From The Deck Source

After image slides are staged, build the instructional slides from the deck
source artifact.

## Pass 5 - Copy Specific Slides To Match The Deck Source

Copy template slides as needed to match the slide sequence in the deck source
artifact.

Use the correct layout type for the slide purpose:

- concept slide
- review slide
- demo slide
- lab bridge slide
- evidence slide
- success check slide
- image slide

## Pass 6 - Add Slide Titles

Add slide titles from the deck source artifact.

This establishes the deck skeleton before adding detailed content.

## Pass 7 - Add Student-Facing Text And Instructor Notes

Copy, edit, and paste the student-facing text and instructor notes from the deck
source artifact into the actual PowerPoint slides.

During this pass:

- adjust student-facing text for readability and slide fit
- preserve the instructional meaning of the deck source
- add instructor notes or transition reminders where useful
- avoid overloading slides with too much text
- add decorative slides or smart text when helpful
- add alt text for any additional decorative or explanatory visuals

The goal is faithful translation, not mechanical copying.

---

# Phase 6 - Place Images Into The Instructional Sequence

## Pass 8 - Move Image Slides Into Position

Move the staged image slides from the end of the deck into the correct locations
within the lecture sequence.

Use the deck source artifact and image prompt artifact to confirm placement.

Images may be used as separate visual-anchor slides when the concept benefits
from repetition or when the image would overload a text slide.

This approach supports:

- visual anchoring
- repeated exposure
- cognitive separation between explanation and diagram
- cleaner slide layouts

---

# Phase 7 - Validate The Full Deck

## Pass 9 - Sequential Validation And Integrity Check

Perform a full sequential pass through the deck.

Check:

- slide order
- title accuracy
- student-facing text clarity
- instructor notes presence
- transition flow
- image placement
- image accuracy
- alt text quality
- demo slide alignment
- lab/assignment bridge accuracy
- evidence expectations
- AI-use guidance
- success check
- visual consistency
- text fit and readability

This pass is essential. Multi-AI production and rapid context switching can
create subtle sequence errors, duplicated ideas, missing slides, or mismatched
images.

---

# Phase 8 - Final Output And Publication

After validation:

1. Save the final PowerPoint deck.
2. Print or export student handout versions:
   - 3 slides per page with notes
   - 6 slides per page horizontal
3. Upload the approved materials to Schoology.

Confirm that the uploaded files match the final validated versions.

---

# Quality Notes

This workflow can produce a high volume of finished lecture material quickly,
but it requires disciplined human oversight.

The instructor should watch for:

- day-to-day topic conflation
- image prompt drift
- copied text in the wrong deck
- missing instructor notes
- missing alt text
- slide sequence errors
- visually appealing but conceptually misleading images
- AI-generated compression of important scaffolding

The process is most effective when supported by:

- a strong deck source artifact
- a separate image prompt artifact
- a stable PowerPoint template
- deliberate pass-based construction
- final sequential validation

---

# Reusable Principle

The production process works because it separates deck construction into
controlled passes.

Rather than trying to create a finished deck slide by slide in one pass, the
workflow separates:

- template structure
- image generation
- image staging
- alt text
- slide skeleton
- student-facing content
- instructor notes
- image placement
- final validation

This reduces cognitive load, preserves consistency, and makes high-throughput
slide production more reliable.

