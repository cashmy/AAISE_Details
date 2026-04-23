# Instructor Notes - The Debugging Process

---

# Purpose

Debugging is not simply changing code until the error disappears.

For many beginning programmers, the first instinct is to modify the code, run it again, modify it again, run it again, and hope that the program eventually works. This can feel productive because the student is "doing something," but it often avoids the most important part of debugging:

* assessing the problem
* finding the correct signal
* separating that signal from the noise
* forming a reasonable hypothesis before changing the code

This note gives an instructor narrative for helping students slow down and treat debugging as an evidence-based process.

---

# Core Message

Debugging is a thinking process before it is a tool process.

The tools matter, but the habit matters more.

Students need to learn that every error, wrong output, failed test, or strange behavior is giving them information. Their job is not to panic, guess, or randomly edit. Their job is to read the evidence and narrow the problem.

You might say:

> "When your code breaks, the program is trying to tell you something. Debugging is the process of learning how to listen carefully enough to hear the useful signal."

---

# The Common Student Pattern

A common beginning pattern looks like this:

1. Run the program.
2. See an error or wrong result.
3. Change something quickly.
4. Run it again.
5. Change something else.
6. Keep going until either it works or the student gets frustrated.

The issue is not that students are lazy. Often, they are overwhelmed.

They see a wall of output, a stack trace, a failed test, or a confusing result. They do not yet know which part matters, so the entire output becomes noise.

When students cannot identify the signal, they may avoid the assessment step completely.

Instructor framing:

> "The first goal is not to fix the bug. The first goal is to understand the bug well enough that the fix becomes smaller."

---

# A Simple Debugging Loop

Use this loop repeatedly during Week 4 demos:

1. Reproduce the problem.
2. Read the exact message or output.
3. Identify what is expected.
4. Identify what actually happened.
5. Find the smallest suspicious area.
6. Make one hypothesis.
7. Test one change or one observation.
8. Explain what changed.

The key constraint is:

> Change one thing at a time.

When students change several things at once, they may make the program work without knowing why. That may solve the immediate problem, but it does not build debugging skill.

---

# Signal vs Noise

Many students need explicit coaching on what to pay attention to.

Useful signal may include:

* the final line of a Python error message
* the file name and line number in a traceback
* the difference between expected and actual output
* the first place where a value becomes wrong
* a failed test case
* a repeated pattern across several failures

Noise may include:

* a long stack trace that contains library internals
* unrelated print output
* earlier guesses that are no longer relevant
* emotional pressure from wanting the code to work immediately
* AI suggestions that are plausible but not connected to the current evidence

Instructor narrative:

> "A stack trace can look like a disaster, but it usually contains a few important clues. We are not trying to understand every line at first. We are trying to find the line that points us back to our code."

---

# Old-Style Debugging: Print and Console Logs

The oldest debugging tool is still one of the most useful:

```python
print("value of total:", total)
print("current item:", item)
print("made it to this line")
```

In Python, this is usually called print debugging.

In JavaScript and browser-based work, students may know the same pattern as console logging:

```javascript
console.log("value of total:", total);
```

This style is not unprofessional. Experienced developers still use it often because it is fast, simple, and highly visible.

The important habit is to use print statements intentionally.

Weak use:

```python
print("here")
print("here")
print("here")
```

Better use:

```python
print("before discount:", subtotal)
print("discount amount:", discount)
print("after discount:", subtotal - discount)
```

Students should learn to label their output so they can understand what they are seeing.

---

# Logging to Files

Print statements are useful for small programs, but they disappear when the program stops unless the console output is saved.

Logging writes information to a more permanent record.

Python includes a built-in `logging` module. Students do not need deep mastery in this course, but they should recognize the idea:

```python
import logging

logging.basicConfig(
    filename="program.log",
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)

logging.info("Program started")
logging.info("Total calculated: %s", total)
```

Logging is useful when:

* the program runs for a long time
* the output is too noisy for the console
* the problem happens only sometimes
* the developer needs a record of what happened
* the program will run outside the IDE or classroom environment

For this course, the goal is recognition and light practice, not full logging architecture.

Instructor narrative:

> "Print statements help us see what is happening right now. Log files help us leave breadcrumbs that can be reviewed after the program runs."

---

# Integrated Debuggers

Modern IDEs and editors include interactive debugging tools.

In VS Code, students can use the integrated debugger to:

* set breakpoints
* run the program one line at a time
* inspect variable values
* step into functions
* step over lines
* restart the program
* watch how values change over time

This is a major shift from guessing.

Instead of adding many print statements, the student can pause the program at a specific line and inspect the current state.

Key vocabulary:

* breakpoint - a line where the program pauses
* step over - run the current line and move to the next one
* step into - enter the function being called
* continue - keep running until the next breakpoint
* call stack - the chain of function calls that led to the current point
* watch - a variable or expression the debugger tracks

Instructor narrative:

> "A debugger lets you freeze time inside the program. Instead of asking what probably happened, you can inspect what is happening at that exact moment."

---

# Python Debugger Tools and Packages

Students should know that debugging tools exist at several levels.

Built-in and common tools include:

* `pdb` - Python's built-in command-line debugger
* `breakpoint()` - a built-in way to pause execution and enter a debugger
* VS Code debugger - an integrated graphical debugging experience
* `debugpy` - the debug adapter used by VS Code and other tools

There are also third-party packages and enhanced debugging tools in the Python ecosystem. These may provide richer tracebacks, better visual output, or friendlier debugging experiences.

Examples students may encounter later include:

* `ipdb`
* `pudb`
* `rich`
* `icecream`

These are not required for the course, but students should recognize that professional debugging includes a tool ecosystem.

Instructor framing:

> "You do not need every debugging tool today. But you do need to understand that debugging is a professional workflow, and tools exist to help you inspect the program instead of guessing."

---

# Browser Inspectors and Transferable Debugging

Even though this is a Python course, students may also work with browser-based tools in other courses or projects.

Browser developer tools use the same debugging mindset:

* Console - view `console.log()` output and runtime errors
* Network - inspect requests, responses, status codes, and payloads
* Elements - inspect HTML and CSS structure
* Sources - set JavaScript breakpoints and step through code
* Application or Storage - inspect local storage, cookies, and session data

This is especially relevant when Python code later connects to APIs, web applications, templates, forms, or MVT-style applications.

The larger point:

> Debugging is transferable.

The syntax changes. The tools change. The process remains similar:

* What did I expect?
* What actually happened?
* Where is the first place the data or behavior diverged?
* What evidence supports my next move?

---

# AI-Assisted Debugging

AI can be useful during debugging, but it should not replace the student's assessment process.

A weak AI debugging prompt:

> "Fix this."

A stronger AI debugging prompt:

> "This Python function should return 80 when the original price is 100 and the discount is 20 percent, but it returns 120. Here is the function and the test case. Help me identify where the logic diverges before suggesting a fix."

The second prompt includes:

* expected behavior
* actual behavior
* relevant code
* a request for diagnosis before repair

This supports the course's manual-first, AI-after-understanding approach.

Instructor narrative:

> "AI can help you debug, but if you skip the evidence-gathering step, you may not know whether AI fixed the real problem or simply changed the code into something that appears to work."

---

# Instructor Demonstration Pattern

When demonstrating debugging, avoid fixing too quickly.

Model the thinking out loud:

1. "What did I expect?"
2. "What actually happened?"
3. "What line or value is suspicious?"
4. "What evidence do I have?"
5. "What is one small thing I can inspect?"
6. "What did that inspection tell me?"
7. "Now what change is justified?"

This may feel slower than simply correcting the code, but the slowness is the point.

Students need to see the process, not just the polished answer.

---

# Classroom Moves

Useful teaching moves:

* Ask students to predict the output before running the program.
* Have students circle or highlight the meaningful line in a traceback.
* Require expected vs actual language before a fix is attempted.
* Ask students to add one labeled print statement, not five unlabeled ones.
* Ask students to explain why a breakpoint belongs on a specific line.
* Require students to remove temporary debug prints before final submission.
* Celebrate finding the bug, not just fixing the bug.

The last point matters.

For students who are anxious about errors, debugging can feel like proof that they are bad at programming. The instructor can reframe it:

> "Finding the bug is not evidence that you failed. Finding the bug is evidence that you are learning how the program works."

---

# Most Important Point

Debugging is not random repair.

Debugging is disciplined curiosity.

The student is learning to pause, observe, form a hypothesis, test carefully, and explain the result.

The tools are helpful:

* print statements
* console logs
* log files
* IDE debuggers
* Python debugger packages
* browser inspectors
* AI assistants

But the central habit is the same:

> Find the signal before changing the code.

