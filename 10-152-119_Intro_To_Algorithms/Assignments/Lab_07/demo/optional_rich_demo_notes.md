# OPTIONAL RICH DEMO NOTES - LAB 07

This optional demo version shows the same music similarity ranking as
`demo_code.py`, but presents the evidence with the `rich` package.

---

# Purpose

Use this file when you want to demonstrate how a third-party console formatting
package can make structured evidence easier to inspect.

The Rich demo preserves the same:

- reference song
- candidate songs
- tag overlap similarity rule
- ranking behavior
- top recommendation
- assumptions and limitations

Only the presentation layer changes.

---

# Classroom Comparison

This gives students three levels of console presentation:

1. plain logic and tables
2. ANSI color for lightweight emphasis
3. Rich tables and panels for structured evidence

Discussion prompts:

- Which version is easiest to scan?
- Does the richer formatting clarify the evidence?
- Is the dependency worth it for this output?
- When would this be useful?
- When would it be unnecessary polish?

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

This Rich demo is an instructor demonstration option, not a student lab
requirement.
