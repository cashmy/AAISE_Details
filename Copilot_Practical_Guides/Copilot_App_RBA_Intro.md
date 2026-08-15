# Copilot App And RBA: A Light Introduction

**Student Guide**

## Purpose

This guide gives a light introduction to how the GitHub Copilot app can support
RBA-style work later in the program.

This is not the full RBA method.

The goal is to understand why an agent/session-based tool may become useful
when your projects become larger and more structured.

## What Changes Later In The Program

Early work is usually small:

- one file
- one function
- one page
- one lab goal
- immediate instructor feedback

Later work becomes larger:

- multiple files
- multiple features
- larger projects
- staged milestones
- planning before coding
- review before accepting changes

The tool choice changes because the work changes.

## RBA-Friendly Thinking

A lightweight RBA-style workflow asks:

- What is the goal?
- What is the current state?
- What is the smallest useful next step?
- What should not change?
- What evidence proves the change worked?
- What needs human approval before continuing?

The Copilot app can help with parts of this workflow, but it should not remove
your responsibility.

## Where The Copilot App Can Help

Later in the program, the Copilot app may help with:

- inspecting a repository
- summarizing current structure
- creating a plan
- splitting work into sessions
- working on a branch or worktree
- comparing implementation options
- reviewing a change before you accept it

## Where You Must Stay In Control

You are still responsible for:

- deciding the goal
- approving the plan
- limiting scope
- testing the result
- rejecting changes you do not understand
- explaining the final work

AI can assist the process.

It cannot own the submission for you.

## RBA-Style Prompt Pattern

```text
Inspect the project and summarize the current state.
Do not edit yet.

Goal:
[state the goal]

Scope:
[state what may change]

Out of scope:
[state what must not change]

Evidence:
[state how we will know it works]

Ask clarifying questions and wait for approval before making changes.
```

## Example: Later Project Prompt

```text
Inspect this web project and summarize the current file structure.
Do not edit yet.

Goal:
Add a small saved-preferences feature.

Scope:
You may inspect HTML, CSS, JS, and README files.

Out of scope:
Do not add a framework, backend, login system, or new dependency.

Evidence:
The page should save a selected preference, reload, and show the saved value.

Ask clarifying questions before proposing a plan.
Wait for approval before editing.
```

## Why This Is Different From Early Assignments

Early assignments are designed to build skill through manual practice.

Later project work may include:

- planning
- review
- comparison
- structured iteration
- larger context

The Copilot app fits better when you are ready to manage those pieces.

## Practical Rule

```text
Use the Copilot app when you are ready to manage the work,
not when you are trying to avoid learning the work.
```

