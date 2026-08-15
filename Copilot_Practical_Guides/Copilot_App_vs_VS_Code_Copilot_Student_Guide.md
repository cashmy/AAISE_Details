# Copilot App vs VS Code Copilot

**Student Guide**

## Big Idea

You are not choosing the "best" AI tool.

You are choosing the tool that matches the kind of work you are doing.

For most early programming work, staying close to your code matters more than
running background agents. Later in the program, when projects become larger,
agent-style tools may become useful for planning, review, and structured
iteration.

## VS Code Integrated Copilot

VS Code Copilot is best when you are actively working inside the editor.

Use it when you need:

- inline suggestions while typing
- help explaining code you are looking at
- help understanding an error
- small edits in the file you are actively viewing
- tight edit-test-debug cycles
- visible code, terminal, debugger, and file tree in one place

Student-friendly rule:

```text
Use VS Code Copilot when you need to stay close to the code.
```

## GitHub Copilot App

The GitHub Copilot app is more useful when the work is larger, more
project-oriented, or spread across sessions.

Use it later when you are ready to manage:

- agent sessions
- worktrees or branches
- planning before coding
- repository-level questions
- background work that must be reviewed
- issue or pull-request style workflows
- multiple tasks that need separate context

Student-friendly rule:

```text
Use the Copilot app when you need to manage work, not just type code.
```

## Practical Comparison

| Situation | Better Starting Tool |
| --- | --- |
| I am learning a new syntax pattern | VS Code Copilot |
| I am debugging one file | VS Code Copilot |
| I need inline suggestions while typing | VS Code Copilot |
| I need to inspect several files and make a plan | Copilot app, later in the program |
| I want an agent to work on a branch/session | Copilot app, later in the program |
| I am managing multiple related tasks | Copilot app, later in the program |
| I am doing a beginner assignment | Usually VS Code, unless instructor says otherwise |

## Early Program Recommendation

Early in the program:

- stay close to your code
- type important lines yourself
- test frequently
- ask AI for explanation before asking for code
- avoid background/autonomous editing unless explicitly allowed

Good early prompt:

```text
Explain this code to me.
Do not rewrite it.
Ask me one question if you need more context.
```

## Later Program Recommendation

Later in the program, the Copilot app may be useful when you can:

- describe the task clearly
- review a plan before edits begin
- inspect a diff
- reject changes you do not understand
- test the result yourself
- explain why you accepted the changes

Good later prompt:

```text
Inspect this repository and summarize the relevant files.
Do not edit yet.
Ask clarifying questions and wait for my approval before making changes.
```

## Main Warning

The more powerful the tool is, the more important your permission boundary
becomes.

VS Code Copilot may suggest code while you work.

The Copilot app may help manage agent sessions and larger workflows.

That means you must be clearer about what AI may do and what it must not do.

## Simple Rule

```text
If you cannot explain the change, do not submit it.
```

