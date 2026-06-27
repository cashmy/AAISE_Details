# Web Development Foundations Demos

This folder contains instructor-facing demo materials for `10-152-118 Web Development Foundations`.

## Purpose

These demos support lecture, guided demonstration, and lab transfer. They should be similar to the weekly assignments, but not complete assignment solutions.

The demo sequence is designed to make each major course idea visible before students are expected to apply it independently.

The files in each demo folder are the finished reference state. In class or recording, the default delivery mode is to build the demo live by typing the important lines and copy/pasting selected sections only when time compression is useful.

This quietly reinforces manual code entry, syntax attention, and incremental checking without turning "type it yourself" into a repeated lecture point.

For weeks with both a Monday live lecture and a Wednesday recorded lecture, prefer this rhythm:

```text
01_monday_*      smallest visible version of the concept
02_wednesday_*   iteration, deepening, or refinement of the same concept
```

## Organization

```text
Demos/
  Week_01_HTML_Multi_Page_Site/
    01_monday_hello_world/
      index.html
      demo_notes.md
    02_wednesday_multi_page_structure/
      index.html
      about.html
      demo_notes.md
```

Each runnable demo lives in its own folder because web demos often need more than one file.

## Running Demos

Most demos can be opened directly by double-clicking `index.html`.

Demos that use `fetch()` to load local JSON should be run through a local web server from the demo folder, for example:

```powershell
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

This avoids browser restrictions that can block local `fetch()` calls from `file://` pages.

## Demo Notes Pattern

Each `demo_notes.md` should identify:

- purpose
- related assignment
- delivery mode
- when to use it
- concept shown
- walkthrough
- student misconceptions
- lab bridge
- optional extension

## PageForge Relationship

PageForge is a separate instructor-only iterative model. These demos are the normal student-facing visual learning points. PageForge can later show a larger project using the same idea, but it should not replace these smaller weekly examples.

## Current Demo Spine

- Week 1: Monday Hello World -> Wednesday multi-page HTML structure
- Week 2: Monday first CSS rules -> Wednesday shared stylesheet across pages
- Week 3: Monday simple layout -> Wednesday responsive card revision
- Week 4: Monday values/conditions -> Wednesday function-based decision
- Week 5: Monday button text change -> Wednesday input and feedback
- Week 6: Monday broken selector -> Wednesday multi-issue debugging
- Week 7: Monday messy working code -> Wednesday refactored functions
- Week 8: Monday delayed message -> Wednesday fetch timing shape
- Week 9: Monday one-file responsibilities -> Wednesday multi-file organization
- Week 10: Monday JSON shape -> Wednesday JSON data displayed on the page
- Week 11: Monday counter state -> Wednesday persistent localStorage preference
- Week 12: Monday repeated work -> Wednesday debounced filter
- Week 13: Monday validate/output safely -> Wednesday trust boundaries
- Week 14: Monday usability friction -> Wednesday refined interaction
- Week 15: Monday basic form submit -> Wednesday simulated login form
