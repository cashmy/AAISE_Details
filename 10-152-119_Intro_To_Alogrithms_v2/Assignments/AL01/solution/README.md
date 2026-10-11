# AL01 Instructor Reference Solution

Instructor-only reference for the conceptual-starter experiment. Do not include
this folder in the student packet or copy it into a student assignment repository.

Run from this folder:

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

The application implements the final Thursday policy with ordinary loops and
named functions. Small duplicate selection loops are intentional: no generic
engine, classes, parser, or framework is needed.

Reports use the demos' cyan headings, green results, and yellow cautions.
Redirected output stays plain; `NO_COLOR` or `TERM=dumb` disables color.
Color is reference presentation support, not an added student requirement.

`console_style.py` contains the reusable palette and terminal fallback. Import
`color_text` from it; keep the module alongside each independently runnable
application. `main.py` retains the ticket rules and domain-specific report.
This is the initial support module; other helpers should be extracted only
when there is actual reusable behavior.

Expected supplied-fixture results:
- Open tickets: T01, T02, T03, T04, T06, T07, T09.
- Tuesday baseline: T02, T03, T04, T07, T09.
- Thursday follow-up: T02, T04, T09.
- Invalid records: T10, T11, T12.

The tests retain instructor-only v1 and pre-extraction comparisons. The application
has one active final selector. Issue count is the number of messages, not always
the number of invalid records: a record can contain multiple field errors.

A local copy of the unchanged fixture makes the solution independently runnable.
Keep it aligned with the packet fixture. This solution is the basis for a later
retrofit into the full-English M / T / Th prompts now in the optional starter.
The starter includes a copy of the reusable console styling support, not the
completed ticket logic. Keep both styling copies aligned if the helper changes.
