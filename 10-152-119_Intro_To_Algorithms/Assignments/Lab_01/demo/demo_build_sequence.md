# Lab 01 Demo Build Sequence

**Demo:** Laptop Charger Decision Algorithm

---

# Purpose

This instructor-facing artifact supports live demo delivery for Lab 01.

The recommended teaching sequence is:

1. Build or paste the plain-text demo first.
2. Run the plain-text version and discuss the algorithmic evidence.
3. Add ANSI color as a presentation refinement.
4. Rerun the demo and compare readability.

This keeps the teaching focus on algorithm design first and presentation polish
second.

---

# Why Not Maintain Two Demo Files?

The final `demo_code.py` file should remain the clean, complete, runnable demo.

Maintaining a separate plain version creates a small risk that the two files
will drift apart over time.

For live teaching, it is better to use this build sequence:

- plain version first
- color add-on second
- final file remains the complete reference version

---

# Stage 1 - Plain-Text Demo

When building the demo live, start without the color support.

Skip these blocks at first:

```python
import os


USE_COLOR = os.environ.get("NO_COLOR") is None


class Style:
    RESET = "\033[0m" if USE_COLOR else ""
    BOLD = "\033[1m" if USE_COLOR else ""
    CYAN = "\033[36m" if USE_COLOR else ""
    GREEN = "\033[32m" if USE_COLOR else ""
    RED = "\033[31m" if USE_COLOR else ""
    YELLOW = "\033[33m" if USE_COLOR else ""


def colorize(text, *styles):
    if not USE_COLOR:
        return text
    return "".join(styles) + text + Style.RESET
```

Use plain `print()` calls instead of `colorize()` calls.

## Plain print_rule_list

Use this version first:

```python
def print_rule_list(title, rules):
    print(title)
    for rule in rules:
        print(f"- {rule}")
    print()
```

## Plain print_representation_bridge

Use this version first:

```python
def print_representation_bridge():
    print("REPRESENTATION BRIDGE")
    print_rule_list("Precise Plain English", REVISED_RULES)
    print_rule_list("Pseudocode", PSEUDOCODE)
    print_rule_list("Python-Style Logic", PYTHON_STYLE)
```

## Plain print_test_table

In the first version, keep the pass/fail output plain:

```python
passed = "Yes" if actual == test_case["expected"] else "No"

print(
    f"{test_case['name']:<4} | "
    f"{format_input_summary(test_case):<58} | "
    f"{test_case['expected']:<16} | "
    f"{actual:<16} | "
    f"{passed}"
)
```

## Plain main heading

Use this version first:

```python
def main():
    print("LAB 01 DEMO - PRECISION AND CORRECTNESS")
    print()
    print_rule_list("Before Revision", INITIAL_RULES)
    print_rule_list("After Revision", REVISED_RULES)
    print_representation_bridge()
    print_test_table("Initial Rule Set (< 40)", recommend_charger_initial)
    print_test_table("Revised Rule Set (<= 40)", recommend_charger_revised)
```

---

# Stage 1 Teaching Notes

After the plain version runs:

- focus on the algorithm, not color
- ask students to identify the failed boundary case
- connect expected output to mental expectation
- connect actual output to what the function produced
- revise the rule from strict comparison to inclusive comparison

Useful instructor phrase:

```text
At this point, the algorithmic evidence is already present. The table shows
what we expected, what actually happened, and whether the result passed.
```

---

# Stage 2 - Add ANSI Color

After students understand the plain evidence table, add color as a presentation
refinement.

Add this block at the top of the file:

```python
import os


USE_COLOR = os.environ.get("NO_COLOR") is None


class Style:
    RESET = "\033[0m" if USE_COLOR else ""
    BOLD = "\033[1m" if USE_COLOR else ""
    CYAN = "\033[36m" if USE_COLOR else ""
    GREEN = "\033[32m" if USE_COLOR else ""
    RED = "\033[31m" if USE_COLOR else ""
    YELLOW = "\033[33m" if USE_COLOR else ""


def colorize(text, *styles):
    if not USE_COLOR:
        return text
    return "".join(styles) + text + Style.RESET
```

Then update the print statements below.

## Colorized print_rule_list

Replace:

```python
print(title)
```

With:

```python
print(colorize(title, Style.BOLD, Style.CYAN))
```

## Colorized print_representation_bridge

Replace:

```python
print("REPRESENTATION BRIDGE")
```

With:

```python
print(colorize("REPRESENTATION BRIDGE", Style.BOLD, Style.CYAN))
```

## Colorized pass/fail output

Replace:

```python
passed = "Yes" if actual == test_case["expected"] else "No"
```

With:

```python
passed = "Yes" if actual == test_case["expected"] else "No"
pass_text = (
    colorize("Yes", Style.GREEN)
    if passed == "Yes"
    else colorize("No", Style.RED, Style.BOLD)
)
```

Then replace the final printed value:

```python
f"{passed}"
```

With:

```python
f"{pass_text}"
```

## Colorized main heading

Replace:

```python
print("LAB 01 DEMO - PRECISION AND CORRECTNESS")
```

With:

```python
print(colorize("LAB 01 DEMO - PRECISION AND CORRECTNESS", Style.BOLD, Style.CYAN))
```

---

# Stage 2 Teaching Notes

After adding color, rerun the demo.

Ask:

- Did the algorithm change?
- Did the evidence change?
- What became easier to notice?

Expected conclusion:

```text
The algorithm did not change. The evidence did not change. The presentation
changed so the evidence is easier for a human reader to inspect.
```

---

# NO_COLOR Fallback

The final demo supports the `NO_COLOR` environment variable.

This means the program can still produce plain output if color is disabled or
not supported.

Instructor framing:

```text
This is a small example of separating logic from presentation. The decision
algorithm should not depend on color. Color only helps us read the output.
```

---

# Suggested Live Demo Rhythm

1. Paste or type the rule lists and test data.
2. Add the initial and revised decision functions.
3. Add plain output functions.
4. Run the demo and discuss the failing boundary case.
5. Add the color support block.
6. Replace the few plain output lines with colorized versions.
7. Rerun and ask what changed.
8. Transition to Lab 01.

The key instructional sequence is:

```text
working logic
-> visible evidence
-> evidence-based revision
-> optional presentation improvement
```
