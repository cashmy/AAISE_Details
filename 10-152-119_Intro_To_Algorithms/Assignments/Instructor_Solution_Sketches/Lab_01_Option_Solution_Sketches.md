# LAB 01 OPTION SOLUTION SKETCHES

**Lab:** Precision and Correctness  
**Instructor Use:** grading calibration, alternate examples, quick response support

---

# Instructor Boundary

These sketches are instructor-only calibration notes. They are not
student-facing walkthroughs and are not runnable solution packages.

For Lab 01, a strong submission should turn an everyday decision into a
precise, testable process. The student's algorithm may be pseudocode or Python,
but it should include inputs, outputs, assumptions, normal tests, edge tests,
and a revision note.

---

# Common Required Evidence

Every option should include:

- short problem statement
- inputs and outputs
- at least three assumptions or constraints
- pseudocode or Python code
- at least five tests
- at least three normal cases
- at least two edge cases
- expected vs actual table
- before/after revision note
- walkthrough-use note or AI-use note if applicable

Suggested evidence table:

| Test | Input Summary | Expected Output | Actual Output | Pass? |
| --- | --- | --- | --- | --- |

---

# Option 1 - Cafeteria Meal Recommendation

## Viable Framing

Recommend one meal from a small menu based on requirements such as budget,
dietary restriction, preference, nutrition, or preparation time.

## Expected Inputs

- meal options
- maximum price
- dietary restrictions
- preference or scoring weights
- time limit, if used

## Expected Outputs

- recommended meal
- reason for recommendation
- no-match message if no meal qualifies

## Expected Assumptions

- required restrictions are checked before scoring
- tie-breaking rule is defined
- no-match case returns a clear message

## Useful Edge Cases

- no meals meet restrictions
- two meals have the same score
- meal price exactly equals the maximum budget
- missing preference information

## Grading Watch-Fors

- Student uses vague terms such as "healthy" or "cheap" without defining them.
- Student recommends a meal without explaining why other meals were excluded.
- Student lacks a no-match test.

## Runnable Expansion Note

Use five meal records with price, tags, preference score, and prep time. Include
one tied score and one item exactly at the budget boundary.

---

# Option 2 - Help Desk Ticket Priority

## Viable Framing

Assign a help desk ticket to high, medium, low, or needs-clarification priority.

## Expected Inputs

- severity
- users affected
- deadline or urgency
- blocked-work flag
- required-information flag

## Expected Outputs

- priority label
- reason for the priority

## Expected Assumptions

- missing required information is handled before priority scoring
- automatic high-priority conditions are clearly defined
- rule order matters and is stated

## Useful Edge Cases

- missing required information
- exact threshold for users affected
- critical severity with one user
- low severity with urgent deadline

## Grading Watch-Fors

- Student uses "many users" or "soon" without a numeric threshold.
- Student allows two conflicting priorities without a rule-order decision.
- Student cannot explain why a ticket became high instead of medium.

## Runnable Expansion Note

The existing Lab 01 success package already implements this option.

---

# Option 3 - Parking Fee Calculation

## Viable Framing

Calculate a parking fee based on time parked, permit status, event status, and
maximum daily charge.

## Expected Inputs

- hours parked
- hourly rate
- permit status
- event status
- daily maximum

## Expected Outputs

- final fee
- rule or reason used

## Expected Assumptions

- partial hours are rounded or handled consistently
- maximum fee is applied after base calculation
- discounts or waivers have a defined order

## Useful Edge Cases

- zero hours
- exactly one hour
- partial hour
- fee exactly reaches maximum
- permit holder during special event

## Grading Watch-Fors

- Student does not define partial-hour handling.
- Student applies maximum fee before discounts without explaining order.
- Student returns a number but no rule explanation.

## Runnable Expansion Note

Use a base rate such as `$2` per hour, a daily max such as `$12`, and one permit
discount rule. Keep currency formatting simple.

---

# Option 4 - Event Registration Eligibility

## Viable Framing

Decide whether a person can register for an event based on eligibility rules.

## Expected Inputs

- age or status requirement
- prerequisite completion
- payment status
- seat availability
- waitlist policy

## Expected Outputs

- approved, denied, waitlisted, or needs information
- reason for the decision

## Expected Assumptions

- mandatory requirements are checked before seat availability
- failed requirements produce a clear reason
- full event triggers waitlist or closed response

## Useful Edge Cases

- exactly at minimum age
- prerequisite missing
- event full
- payment missing
- multiple failed requirements

## Grading Watch-Fors

- Student does not decide whether to stop at first failed requirement.
- Student forgets the event-full case.
- Student gives approval without checking all mandatory requirements.

## Runnable Expansion Note

Use five applicant records. Include one applicant exactly at the age boundary
and one otherwise qualified applicant when seats are full.

---

# Option 5 - Library Late-Fee Decision

## Viable Framing

Calculate or decide a late fee based on due date, return date, item type,
borrower type, grace period, and maximum fee.

## Expected Inputs

- due date or days late
- return date or days late
- item type
- borrower type
- grace period
- daily rate
- maximum fee

## Expected Outputs

- final fee
- explanation of calculation

## Expected Assumptions

- late days are counted consistently
- grace period is defined
- item type or borrower type affects rate only if stated
- maximum fee is applied after fee calculation

## Useful Edge Cases

- returned on due date
- one day late
- exactly within grace period
- exactly at maximum fee
- special borrower type

## Grading Watch-Fors

- Student does not define how dates or days late are calculated.
- Student applies grace period inconsistently.
- Student omits zero-fee case.

## Runnable Expansion Note

Use `days_late` instead of actual dates if quick demonstration is needed.
Include a grace-period boundary case and max-fee boundary case.

---

# Cross-Option Grading Calibration

Strong work should:

- define vague terms with thresholds or rules
- show both normal and edge cases
- include expected and actual results
- revise one ambiguity based on evidence
- explain assumptions instead of hiding them
