# Week 11 Success Notes - State Management

This package shows one acceptable successful version for Assignment 11. It continues `Study Sprint` by tracking selected resources and saving the selected resource in `localStorage`.

## Files Included

- `index.html`
- `tips.html`
- `schedule.html`
- `styles.css`
- `script.js`
- `resources.json`

## What This Version Demonstrates

- state stored in a JavaScript variable
- UI updates from state
- user interaction changes state
- selected state is persisted with `localStorage`
- saved state is restored on page load

## Instructor Demo Use

Show this at the beginning of Week 12 after Assignment 11 has been submitted.

Recommended rhythm:

1. Load resources.
2. Select a resource.
3. Refresh the page.
4. Point out that the selected resource returns because persistence was handled intentionally.

## Revision Recovery Connection

Students revising Assignment 11 should identify what value their application stores, what interaction changes it, and how the UI reflects the current state.

## Tradeoffs

This version stores only a resource name, not an entire account or private profile. That keeps persistence simple and avoids sensitive data.

