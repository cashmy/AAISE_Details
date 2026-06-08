# README Example - Lab 01 Demo

**Course:** 10-152-119 Algorithmic Problem Solving  
**Lab:** Lab 01 - Precision and Correctness  
**Example Scenario:** Laptop Charger Decision Algorithm  

---

# Purpose Of This Example

This is a filled README example based on the Week 1 instructor demo.

It shows how a README can explain the thinking behind an algorithm, not just
list assignment requirements.

Do not copy this scenario for your Lab 01 submission unless your instructor
specifically tells you to. Your own lab should use your assigned or selected
scenario.

---

# Problem Statement

A student is leaving for campus and needs a clear rule for deciding whether to
bring a laptop charger.

The first version of the rule used vague phrases such as "low battery" and
"long time." Those phrases were not precise enough to test. The revised version
turns the decision into clear threshold rules.

---

# Inputs And Outputs

| Type | Name | Description |
| --- | --- | --- |
| Input | `battery_percent` | Current laptop battery percentage |
| Input | `expected_hours` | Number of hours the student expects to be on campus |
| Input | `outlet_access` | Whether the student expects reliable outlet access |
| Output | recommendation | Either `bring charger` or `charger optional` |

---

# Assumptions And Constraints

1. A battery at `40` percent or below should count as low.
2. Four or more hours on campus counts as a long enough time to matter.
3. If reliable outlet access is available, the student has less need to bring a
   charger unless the battery is already low.
4. The algorithm only considers battery level, expected time, and outlet
   access. It does not consider charger weight, laptop age, battery health, or
   whether the student will use power-intensive software.

---

# First Version Of The Algorithm

```text
If the laptop battery is low, bring the charger.
If the student will be on campus for a long time and does not have reliable
outlet access, bring the charger.
Otherwise, the charger is optional.
```

## Problem With The First Version

The first version is understandable, but it is not precise enough.

It does not define:

- what counts as "low"
- what counts as "a long time"
- what should happen at the exact boundary values

Because of that, two people could follow the same instructions and make
different decisions.

---

# Revised Algorithm

## Precise Plain English

```text
If battery_percent is 40 or below, bring the charger.
Else if expected_hours is 4 or more and outlet_access is false, bring the
charger.
Otherwise, the charger is optional.
```

## Pseudocode

```text
if battery_percent <= 40:
    recommend bringing charger
else if expected_hours >= 4 and outlet_access is false:
    recommend bringing charger
else:
    charger is optional
```

## Python-Style Logic

```python
if battery_percent <= 40:
    recommendation = "bring charger"
elif expected_hours >= 4 and not outlet_access:
    recommendation = "bring charger"
else:
    recommendation = "charger optional"
```

---

# Test Evidence

| Test | Input Summary | Expected Output | Initial Actual Output | Revised Actual Output | Pass After Revision? |
| --- | --- | --- | --- | --- | --- |
| 1 | Battery 25%, 2 hours on campus, outlet available | bring charger | bring charger | bring charger | Yes |
| 2 | Battery 80%, 3 hours on campus, outlet unavailable | charger optional | charger optional | charger optional | Yes |
| 3 | Battery 55%, 5 hours on campus, outlet unavailable | bring charger | bring charger | bring charger | Yes |
| 4 | Battery exactly 40%, 4 hours on campus, outlet unavailable | bring charger | charger optional | bring charger | Yes |
| 5 | Battery 39%, 1 hour on campus, outlet unavailable | bring charger | bring charger | bring charger | Yes |

---

# Revision Note

The first version failed the boundary case where the battery was exactly `40`
percent and the student expected to be on campus for exactly `4` hours.

The original code used:

```python
battery_percent < 40
expected_hours > 4
```

That meant `40` percent was not treated as low, and `4` hours was not treated
as a long time.

The revised version uses:

```python
battery_percent <= 40
expected_hours >= 4
```

This better matches the intended rule.

---

# Reflection

One ambiguous instruction in the first version was "low battery."

Testing helped reveal that the phrase needed an exact cutoff. Once the cutoff
was defined as `40` percent or below, the algorithm became easier to test and
explain.

The important pattern is:

1. Start with a real decision.
2. Identify the inputs and output.
3. Make vague words precise.
4. Test normal and edge cases.
5. Revise the rule when evidence shows ambiguity.

---

# AI Use Note

No AI was used to create the original demo logic in this example.

If AI had been used, the README would need to explain:

- what AI helped with
- what was changed by the student
- what tests were used
- what the student still understands and owns

---

# Known Issues Or Improvements

1. The algorithm does not consider battery health or laptop age.
2. The algorithm assumes the student can accurately estimate campus time.
3. The algorithm does not consider whether the student will use software that
   drains the battery quickly.

These limitations do not make the algorithm useless. They explain the boundary
of what the algorithm can claim.
