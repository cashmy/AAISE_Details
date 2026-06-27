# Week 10 Success Notes - Data And APIs

This package shows one acceptable successful version for Assignment 10. It continues `Study Sprint` by loading simulated external data from a local JSON file and displaying selected fields in the UI.

## Files Included

- `index.html`
- `tips.html`
- `schedule.html`
- `styles.css`
- `script.js`
- `resources.json`

## What This Version Demonstrates

- local JSON data as an API fallback
- `fetch()`
- `response.json()`
- an array of resource objects
- selected values displayed in the UI
- loading and error feedback
- meaningful display instead of raw JSON dumping

## Instructor Demo Use

Show this at the beginning of Week 11 after Assignment 10 has been submitted.

Recommended rhythm:

1. Open `resources.json` and inspect the data shape.
2. Run the site through a local server.
3. Click "Load study resources."
4. Trace request, receive, loop, and display.
5. Point out that the UI uses selected fields from each object.

## Revision Recovery Connection

Students revising Assignment 10 should focus on reading the data shape, accessing values correctly, and displaying useful fields after the data arrives.

## Tradeoffs

This version uses local JSON instead of a public API so the success solution remains stable and does not depend on network availability.

