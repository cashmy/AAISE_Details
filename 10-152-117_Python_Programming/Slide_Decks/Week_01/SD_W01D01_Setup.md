# SLIDE DECK SOURCE - WEEK 1 DAY 1 PRELOAD SETUP

**10-152-117 Python Programming**

---

# Deck Metadata

| Field | Value |
| --- | --- |
| Course | 10-152-117 Python Programming |
| Placement | Pre-course / Week 1 Day 1 preload |
| Recommended Use | Assign before first class; optionally review briefly during first class |
| Lecture Title | Python, Virtual Environments, VS Code, and GitHub Setup |
| Assignments Supported | A1 - First Programs; all later Python assignments |
| Readiness Target | Students can install Python, open VS Code, create/select a virtual environment, and understand basic GitHub submission paths |
| Primary Watch Point | Setup can consume the first learning session if not bounded and verified early |
| Source Version | v1 |

---

# Session Purpose

This preload deck prepares students for the local development environment used
in the course.

Students should understand:

- where to download Python
- how to verify Python installed correctly
- what a virtual environment is
- how to create and activate `.venv`
- how VS Code supports Python development
- which VS Code extensions are useful
- how VS Code can use a virtual environment
- how GitHub can be used through VS Code as an alternative to Git CLI workflows

This deck is not a programming lecture. It is setup and orientation.

---

# Review / Prior Work Bridge

There is no prior Python lab for this deck.

Bridge into Week 1:

Before students can run their first Python program reliably, they need a stable
toolchain:

```text
Python installation
-> project folder
-> virtual environment
-> VS Code
-> GitHub submission path
```

---

# Reading Alignment

Primary weekly reading:

- `Weekly_Reading_Guide.md`, Week 1
- textbook chapter area: **A Gentle Introduction to Python**

Reading focus:

- what Python is
- setting up the environment
- how to run a Python program
- a word about AI

Reading boundary:

Students should not worry yet about professional package publishing, advanced
project layouts, modules, scopes, third-party libraries, or full Git workflow
mastery.

---

# What We Will Use In This Setup

We will use:

- Python from `python.org`
- PowerShell or terminal verification commands
- project folders
- `.venv` virtual environments
- Visual Studio Code
- Microsoft Python extension
- VS Code interpreter selection
- VS Code source control / GitHub integration

We will skip for now and revisit later:

- advanced dependency management
- publishing packages
- complex Git branching
- pull request reviews
- deployment
- Python pre-release versions

---

# Current Version Note

As of June 9, 2026, `python.org/downloads/` lists **Python 3.14.5** as the
latest Python release.

Course guidance:

- Use the latest stable Python release from `python.org` unless the instructor
  specifies a course version.
- Do not install Python pre-release versions for this course.
- Verify the current download page immediately before the course starts,
  because Python releases change over time.

---

# Slide Sequence Overview

| Section | Slides | Category | Purpose |
| --- | ---: | --- | --- |
| Setup Frame | 1-3 | Core | Explain why setup matters and what students need |
| Python Install | 4-7 | Core | Download, install, and verify Python |
| Project Folder and venv | 8-12 | Core | Create a stable project folder and virtual environment |
| VS Code Setup | 13-17 | Core | Install VS Code, Python extension, and select interpreter |
| GitHub In VS Code | 18-22 | Core | Show GitHub extension and source-control workflow options |
| Troubleshooting and Success | 23-25 | Assessment / Evidence | Verify environment and define setup success |

---

# Slide-by-Slide Source

## Slide 1 - Setup Is Part Of The Course

**Delivery Category:** Core

**Student-Visible Text:**

Before writing Python comfortably, your computer needs a stable setup.

The goal is not to memorize setup steps. The goal is to create a reliable place
to run your code.

**Instructor Notes:**

Frame setup as infrastructure, not as the first "programming test." Students
can become discouraged if installation issues feel like proof that they cannot
code.

**Transition Cue:**

The setup has several pieces, but each has a clear job.

---

## Slide 2 - Setup Path

**Delivery Category:** Core

**Student-Visible Text:**

Course setup path:

Python -> project folder -> `.venv` -> VS Code -> GitHub

Each piece supports a different part of the workflow.

**Instructor Notes:**

Give the mental map before the details. Students need to know why these tools
exist before they see commands.

**Visual Notes:**

Use a left-to-right flow diagram.

---

## Slide 3 - What Success Looks Like

**Delivery Category:** Core

**Student-Visible Text:**

Setup is successful when you can:

- check your Python version
- open a project in VS Code
- select a `.venv` interpreter
- run a small `.py` file
- see your code in GitHub or prepare it for submission

**Instructor Notes:**

This slide defines the end state. It also gives students a checklist they can
return to if they are uncertain.

**Transition Cue:**

The first installation is Python itself.

---

## Slide 4 - Download Python

**Delivery Category:** Core

**Student-Visible Text:**

Download Python from:

`https://www.python.org/downloads/`

Use the latest stable release unless your instructor specifies a course version.

**Instructor Notes:**

As of June 9, 2026, Python.org lists Python 3.14.5 as the latest release.
Students should use the official Python website rather than random download
mirrors.

For Windows, Python.org may offer the Python install manager or a standalone
installer. Either path is acceptable if the installation can be verified in the
terminal.

**Transition Cue:**

After downloading, install in a way that lets the terminal find Python.

---

## Slide 5 - Install Python

**Delivery Category:** Core

**Student-Visible Text:**

During installation, choose options that make Python available from the
terminal.

On Windows, make sure the installer or install manager creates a usable `py` or
`python` command.

**Instructor Notes:**

Avoid over-teaching every installer screen. The practical success check is
whether students can open PowerShell and run a version command.

If the installer offers PATH-related options, students should enable the option
that lets Python run from the terminal.

**Transition Cue:**

The install is not complete until we verify it.

---

## Slide 6 - Verify Python

**Delivery Category:** Core

**Student-Visible Text:**

Open PowerShell or Terminal and run:

```powershell
python --version
py --version
python -m pip --version
```

At least one Python version command should show the installed Python version.

**Instructor Notes:**

On Windows, `py --version` may work even when `python --version` does not.
That is acceptable for course use as long as students know which command they
are using.

The `pip` check confirms that package management is available through the
selected Python.

**Transition Cue:**

Next, create a project folder so course work is organized from the beginning.

---

## Slide 7 - Version Boundary

**Delivery Category:** Core

**Student-Visible Text:**

Use a stable Python release.

Do not use pre-release versions for this course unless the instructor tells you
to.

**Instructor Notes:**

Students may see beta, alpha, or release candidate builds. Those are not
appropriate for this course.

If a student already has Python installed, verify the version before deciding
whether they need to change anything.

**Transition Cue:**

Now we need a place for the course files.

---

## Slide 8 - Create A Course Folder

**Delivery Category:** Core

**Student-Visible Text:**

Create a folder for course work.

Example:

```text
Python_Programming_117
```

Keep projects and assignments organized from the start.

**Instructor Notes:**

Recommend a simple path without spaces or unusual characters if possible.
Students can use their normal Documents folder, but should know where the work
is stored.

**Transition Cue:**

Inside project folders, Python can use a local virtual environment.

---

## Slide 9 - What A Virtual Environment Does

**Delivery Category:** Core

**Student-Visible Text:**

A virtual environment is a local Python workspace for one project.

It helps keep project packages separate from the rest of your computer.

**Instructor Notes:**

Keep this conceptual. Students do not need dependency theory yet. They need the
idea that `.venv` belongs to the project and helps prevent package confusion.

**Transition Cue:**

The standard beginner-friendly folder name is `.venv`.

---

## Slide 10 - Create `.venv`

**Delivery Category:** Core

**Student-Visible Text:**

From the project folder, create a virtual environment:

```powershell
py -m venv .venv
```

If `py` is not available, use:

```powershell
python -m venv .venv
```

**Instructor Notes:**

Explain the command in plain language:

- `py` or `python` starts Python
- `-m venv` runs the virtual environment tool
- `.venv` is the folder being created

**Transition Cue:**

After creating `.venv`, activate it or select it in VS Code.

---

## Slide 11 - Activate `.venv` In PowerShell

**Delivery Category:** Core

**Student-Visible Text:**

Windows PowerShell activation:

```powershell
.\.venv\Scripts\Activate.ps1
```

When active, the terminal prompt usually shows:

```text
(.venv)
```

**Instructor Notes:**

If execution policy blocks activation, do not derail the whole lesson. VS Code
can still select the interpreter, and the issue can be handled individually.

The visible `(.venv)` prefix is useful evidence, but the stronger check is
which Python interpreter VS Code is using.

**Transition Cue:**

You can also let VS Code use the `.venv` directly.

---

## Slide 12 - Why `.venv` Matters Later

**Delivery Category:** Core

**Student-Visible Text:**

Later, when projects use packages, `.venv` helps keep installs project-specific.

For Week 1, the goal is simply to know what `.venv` is and how to create/select
it.

**Instructor Notes:**

This prevents a common misconception: students may think venv is unnecessary
because early scripts do not install packages. The value becomes more visible
later.

**Transition Cue:**

Now we need an editor that can use Python and the virtual environment.

---

## Slide 13 - Install Visual Studio Code

**Delivery Category:** Core

**Student-Visible Text:**

Download Visual Studio Code from:

`https://code.visualstudio.com/`

VS Code is the editor we will use for writing and running Python code.

**Instructor Notes:**

Emphasize Visual Studio Code, not Visual Studio. These are different products.

**Transition Cue:**

VS Code becomes Python-aware through extensions.

---

## Slide 14 - Install Python Extensions

**Delivery Category:** Core

**Student-Visible Text:**

Recommended VS Code extensions:

- Python
- Pylance
- Python Environments
- Jupyter, optional

Use trusted publishers such as Microsoft.

**Instructor Notes:**

The Microsoft Python extension provides core Python support. Pylance provides
language intelligence. Python Environments helps manage and select
environments. Jupyter is optional and only needed if notebooks are used.

Mention extension trust: students should avoid random extensions that claim to
help with Python unless the instructor approves them.

**Transition Cue:**

After extensions are installed, VS Code must know which Python to use.

---

## Slide 15 - Select The Python Interpreter

**Delivery Category:** Core

**Student-Visible Text:**

In VS Code:

1. Open the project folder.
2. Open the Command Palette (Ctrl+Shift+P).
3. Choose `Python: Select Interpreter`.
4. Select the interpreter inside `.venv`.

**Instructor Notes:**

This is the most important VS Code setup step. Students often install Python
correctly but run code with the wrong interpreter.

The selected interpreter may appear in the VS Code status bar or Python
environment selector.

**Transition Cue:**

The terminal should also line up with the selected environment.

---

## Slide 16 - VS Code And `.venv`

**Delivery Category:** Core

**Student-Visible Text:**

VS Code can detect and use virtual environments.

When the `.venv` interpreter is selected, new VS Code terminals can activate
that environment automatically.

**Instructor Notes:**

VS Code's Python tooling can switch between interpreters, including virtual
environments. If the terminal does not activate automatically, students can
still activate manually or reselect the interpreter.

**Transition Cue:**

Now verify that VS Code can run a small Python file.

---

## Slide 17 - Run A Test File

**Delivery Category:** Core

**Student-Visible Text:**

Create a file:

```text
setup_test.py
```

Add:

```python
print("Python setup works!")
```

Run it in VS Code and confirm the output appears.

**Instructor Notes:**

This is the practical setup success check. It is intentionally tiny.

**Transition Cue:**

After code runs locally, students need a way to submit and preserve work.

---

## Slide 18 - GitHub Submission Paths

**Delivery Category:** Core

**Student-Visible Text:**

There are two common GitHub paths:

- Git CLI commands
- VS Code Source Control and GitHub extensions

Both paths should preserve code changes clearly.

**Instructor Notes:**

Frame VS Code GitHub integration as an alternate workflow, not as a separate
standard. The underlying concepts remain the same: files change, changes are
committed, and work is pushed or submitted.

**Transition Cue:**

VS Code includes source control tools directly in the editor.

---

## Slide 19 - Source Control In VS Code

**Delivery Category:** Core

**Student-Visible Text:**

VS Code has a Source Control view for Git work.

You can see changed files, write a commit message, commit, and sync without
typing every Git command manually.

**Instructor Notes:**

Important boundary: VS Code still relies on Git being available on the
computer for normal local Git workflows.

If Git is missing, install Git for Windows or use the GitHub tools supported by
the instructor's workflow.

**Transition Cue:**

GitHub extensions can make GitHub-specific actions easier.

---

## Slide 20 - GitHub Extensions

**Delivery Category:** Core

**Student-Visible Text:**

Useful GitHub-related VS Code extensions:

- GitHub Pull Requests
- GitHub Repositories

These can help with GitHub sign-in, repositories, commits, and pull-request
workflows.

**Instructor Notes:**

For this course, the most important student workflow is basic submission, not
advanced pull request review.

GitHub Repositories can browse and work with remote GitHub repositories from VS
Code. GitHub Pull Requests supports PR and issue workflows.

**Transition Cue:**

Students should still understand the basic vocabulary.

---

## Slide 21 - GitHub Vocabulary

**Delivery Category:** Core

**Student-Visible Text:**

Core GitHub words:

- repository: project storage
- clone: copy repository to your computer
- commit: save a meaningful change
- push: send commits to GitHub
- sync: pull and push changes through VS Code

**Instructor Notes:**

Keep this vocabulary practical. Do not teach complex branching here.

**Transition Cue:**

Now compare CLI and VS Code workflows.

---

## Slide 22 - CLI Or VS Code

**Delivery Category:** Core

**Student-Visible Text:**

Git CLI and VS Code can both support the same workflow:

change files -> review changes -> commit -> push or sync

Use the path your instructor approves for the assignment.

**Instructor Notes:**

This prevents students from treating VS Code as a separate concept from Git.
The interface changes; the core workflow remains.

**Transition Cue:**

Before the first assignment, check the setup end to end.

---

## Slide 23 - Setup Verification Checklist

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

Setup checklist:

- Python version command works
- project folder exists
- `.venv` exists
- VS Code opens the folder
- VS Code selects the `.venv` interpreter
- `setup_test.py` runs
- GitHub workflow is understood or ready to practice

**Instructor Notes:**

This slide can become the student-facing checklist in Schoology.

**Transition Cue:**

If something fails, diagnose the exact layer.

---

## Slide 24 - Troubleshooting Layers

**Delivery Category:** Core

**Student-Visible Text:**

When setup fails, locate the layer:

- Python install
- terminal command
- project folder
- `.venv`
- VS Code interpreter
- Git or GitHub sign-in

Fix one layer at a time.

**Instructor Notes:**

This prevents broad panic. Students often say "Python does not work" when the
actual issue is PATH, interpreter selection, or terminal activation.

**Transition Cue:**

Once setup is verified, students are ready for the first real coding session.

---

## Slide 25 - Ready For First Programs

**Delivery Category:** Assessment / Evidence

**Student-Visible Text:**

You are ready for Week 1 coding when:

- Python runs
- VS Code opens your project
- `.venv` is available
- a tiny `.py` file prints output
- your submission path is clear

**Instructor Notes:**

End with readiness, not tool worship. The setup exists to support learning
Python, not to become the course itself.

**Transition Cue:**

Next, we write the first tiny Python program.

---

# Demo / Walkthrough Notes

Recommended walkthrough order:

1. Open `python.org/downloads/`.
2. Show the latest stable Python release.
3. Install or verify Python.
4. Run version checks in PowerShell.
5. Create a project folder.
6. Create `.venv`.
7. Open VS Code.
8. Install Python-related extensions.
9. Select the `.venv` interpreter.
10. Run `setup_test.py`.
11. Show Source Control and GitHub extension locations in VS Code.

If time is limited, require students to complete steps 1-10 before class and
use class time only for verification and troubleshooting.

---

# Student Setup Evidence

Recommended evidence students can show or submit:

- screenshot or copied terminal text showing Python version
- screenshot or note showing `.venv` exists
- screenshot or copied output from `setup_test.py`
- confirmation that VS Code selected the `.venv` interpreter
- confirmation of GitHub sign-in or instructor-approved submission path

Keep this as setup evidence only. Do not grade it like a programming
assignment unless the instructor chooses to make it a formal checkpoint.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 2 | Setup path | Python -> folder -> `.venv` -> VS Code -> GitHub workflow | Avoid complex DevOps diagrams |
| 3 | Setup success | Checklist of version, folder, `.venv`, VS Code, GitHub path | Keep checklist readable |
| 4 | Python download | Browser download page concept with official python.org emphasis | Do not show outdated version number unless editable |
| 9 | venv concept | Project folder with local `.venv` environment bubble | Avoid container/VM confusion |
| 10 | venv command | Terminal command creating `.venv` folder | Keep command readable |
| 15 | Select interpreter | VS Code command palette selecting `.venv` interpreter | Avoid too much UI detail |
| 17 | Test file | `setup_test.py` running and printing success output | Keep code tiny |
| 18 | GitHub paths | Two paths: Git CLI and VS Code Source Control | Do not imply students need both equally |
| 23 | Verification checklist | Setup checklist with all required layers | Keep as student-facing checklist |
| 24 | Troubleshooting layers | Layered stack from install to GitHub sign-in | Avoid panic/error-heavy imagery |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Setup frame | 5 min | Use Slides 1-2 only | Discuss why setup is not a programming test |
| Python install | 10-20 min | Assign as pre-work | Walk through installer and version checks |
| Project folder and `.venv` | 15-20 min | Demonstrate only | Have students create `.venv` live |
| VS Code setup | 15-25 min | Show screenshots only | Install extensions and select interpreter live |
| GitHub workflow | 10-20 min | Introduce only | Sign in, clone/open repo, show source control |
| Verification | 10-15 min | Use checklist only | Troubleshoot student machines individually |

---

# Source References

Use these official references when updating this deck:

- Python downloads: `https://www.python.org/downloads/`
- VS Code Python documentation: `https://code.visualstudio.com/docs/languages/python`
- VS Code Python environments: `https://code.visualstudio.com/docs/python/environments`
- VS Code GitHub documentation: `https://code.visualstudio.com/docs/sourcecontrol/github`
- VS Code source control documentation: `https://code.visualstudio.com/docs/sourcecontrol/overview`

---

# Post-Setup Notes

Use after delivery to record what worked, what needs adjustment, and what
should change in the next course run.

## Worked Well

-

## Needs Adjustment

-

## Common Setup Issues

-

## Future Revision Notes

-

