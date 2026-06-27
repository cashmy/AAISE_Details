# Reliability Note

## Issue

User input could be empty or could include text that looks like HTML.

## What Could Go Wrong

Empty input would create unclear feedback. Treating user input as raw HTML could create unsafe output habits.

## What Was Added

The code checks for empty input and uses `textContent` to display the note as text.

## Verification

I tested empty input, normal text, and text that looks like an HTML tag. The page displays all user-provided content as text.

