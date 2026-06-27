# Debugging Report - Study Sprint Planner

## Issue 1 - Button Selector Did Not Match

**Problem:** The JavaScript selected `#createPlanButton`, but the HTML button id was `planButton`.

**How I identified it:** The console showed an error when the script tried to attach an event listener. I compared the selector in JavaScript to the id in the HTML.

**Fix:** I changed the selector to `document.querySelector("#planButton")`.

**Verification:** I refreshed the page, clicked the button, and confirmed that the event ran.

## Issue 2 - Empty Input Produced A Weak Result

**Problem:** Empty input was converted to `0`, so the feedback was technically handled but not clear enough for the user.

**How I identified it:** I tested the form without typing anything and reviewed the message.

**Fix:** I added a specific check for an empty input before converting the value to a number.

**Verification:** I tested empty input, `10`, `30`, and `60` minutes.

## Issue 3 - Output Needed Better User Feedback

**Problem:** The result message updated, but it did not clearly label itself as the plan.

**How I identified it:** I read the page as a user and noticed the message appeared without enough context.

**Fix:** I updated the JavaScript so successful results begin with `Plan:`.

**Verification:** I tested the planner and confirmed the result area shows a clear message.

