# OPTIONAL RICH SUCCESS VERSION - LAB 07 SIMILARITY PATH

This file demonstrates a third presentation layer for the Lab 07 similarity /
recommendation successful version.

---

# Purpose

`optional_rich_success_solution.py` uses the same recommendation logic as:

- `success_solution.py`
- `optional_colorized_success_solution.py`

The difference is presentation only.

The Rich version uses panels and formatted tables to make the profile,
resource representation, ranking evidence, recommendation, assumptions, and
limitations easier to inspect.

---

# Instructional Point

This version extends the MVP development progression:

```text
Correct -> Observable -> Explainable -> Usable -> Refined
```

The progression for this Lab 07 success path is:

1. plain successful version
2. ANSI colorized version
3. Rich formatted version

This lets students compare presentation choices:

- Does the richer table layout make the evidence easier to read?
- Is the added dependency worth it for this type of output?
- When does UI polish clarify meaning?
- When would it be unnecessary?

---

# Dependency Note

This version requires the third-party `rich` package.

The dependency is documented in:

```text
Assignments/requirements.txt
```

Install instructor testing dependencies from the `Assignments` folder with:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

This Rich version is optional and is not a student grading requirement.
