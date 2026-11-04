# Copilot Permission Gate Prompts

**Reusable Student Prompts**

## Why These Prompts Matter

Some AI tools can do more than answer questions. They may be able to inspect
files, edit code, run commands, create branches, or work in sessions.

That power can be useful, but only if you control the boundary.

Use permission gates when a tool can change your project.

## Inspect First

```text
Inspect this project first.
Do not edit files.
Summarize the relevant files and explain what you found.
Ask clarifying questions before suggesting changes.
```

## Explain Before Editing

```text
Explain the current code before suggesting changes.
Do not rewrite it.
Tell me what each relevant part does and where the likely issue is.
```

## Plan Before Editing

```text
Create a short plan before editing.
List the files you think need to change.
Explain why each change is needed.
Do not edit until I approve the plan.
```

## Ask Questions First

```text
Before answering, ask up to three clarifying questions if needed.
If you can proceed safely, state your assumptions first.
Do not make changes until I approve.
```

## Narrow Edit Permission

```text
Make only the changes in the approved plan.
Do not add new features.
Do not change unrelated files.
Do not rename files unless necessary.
After editing, summarize exactly what changed.
```

## No Final Solution Yet

```text
Do not generate a final solution yet.
Give me hints, questions, and a checklist so I can continue the work myself.
```

## Debugging Help

```text
I manually wrote this code.
Do not rewrite the whole file.
Explain the likely cause of the error,
point me to the section to inspect,
and ask one question before suggesting code.
```

## Refactoring Help

```text
I manually wrote this working code.
Do not rewrite it for me.
Suggest how I might organize it more clearly.
Explain the tradeoffs before showing any code.
```

## Review Help

```text
Review these changes for likely bugs or missing requirements.
Do not make edits yet.
List concerns first, then ask whether I want help fixing them.
```

## Submission Check

```text
Compare my work to the assignment requirements.
Do not rewrite my answer.
Tell me what appears complete,
what may be missing,
and what I should verify before submitting.
```

## The One-Sentence Safety Rule

```text
Inspect, summarize, ask, then wait.
```

