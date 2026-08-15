# AI Prompting Basics Lecture Deck Source

**Reusable Optional Recording**  
**Audience:** Beginning programming, web development, and algorithms students  
**Working Title:** AI Prompting Basics - Asking For Help Without Giving Up Ownership

---

# Session Purpose

This optional lecture teaches students how to ask AI tools for useful help
without giving up responsibility for the work.

The goal is not advanced prompt engineering. The goal is a small, repeatable
prompt pattern students can use when they need explanation, feedback, or
guidance.

Students should leave with these habits:

- provide task context
- state what they already tried
- define what help is allowed
- set boundaries against full solution replacement
- ask for clarifying questions before suggestions when needed
- understand that browser LLMs, code LLMs, and app-based agents behave
  differently

---

# Recommended Placement

This deck can be used as:

- an optional recorded review
- a support resource before AI-enabled assignments
- a shared resource across 10-152-117, 10-152-118, and 10-152-119
- a reference when students misuse AI by asking for complete solutions

---

# Slide Sequence Overview

1. Asking For Help Without Giving Up Ownership
2. Why Prompting Matters
3. Old Prompt Advice: "Act As..."
4. Current Practice: Context And Permission
5. Role Is Not The Same As Permission
6. The Basic Prompt Pattern
7. Weak Prompt Versus Useful Prompt
8. AI Roles In This Program
9. Browser-Based LLMs
10. Code-Focused LLMs
11. App-Based / Agentic Interfaces
12. Clarifying Questions First
13. Permission Gate For Code-Editing AI
14. What Not To Ask
15. What To Ask Instead
16. Reusable Prompt Templates
17. Student Responsibility
18. Closing Mental Model

---

# Slide-By-Slide Source

### Slide 1 - Asking For Help Without Giving Up Ownership

Student-visible text:

```text
AI Prompting Basics

Asking for help without giving up ownership.

The goal:

- clearer questions
- better explanations
- safer boundaries
- work you can still understand, test, and explain
```

**Instructor notes:**

- Frame this as a learning support skill, not a shortcut skill.
- Emphasize that AI use must still follow the course AI policy and assignment
  instructions.

**Transition cue:**

- "Prompting matters because vague requests often produce confident but unhelpful answers."

### Slide 2 - Why Prompting Matters

Student-visible text:

```text
AI answers depend on:

- the context you give
- the goal you name
- the boundaries you set
- the evidence you include
- the output format you request

Better prompt does not mean longer prompt.
It means clearer instructions.
```

**Instructor notes:**

- Avoid selling prompt engineering as a magic formula.
- The main point is clarity and ownership.

**Transition cue:**

- "Some advice students may have seen online is older than the tools they are using now."

### Slide 3 - Old Prompt Advice: "Act As..."

Student-visible text:

```text
Older prompt advice often said:

"Act as an expert developer."
"Act as a tutor."
"Act as a senior engineer."

This can still help sometimes.

But by itself, it is incomplete.
```

**Instructor notes:**

- Do not dismiss role prompting as wrong.
- Present it as older incomplete advice.
- Modern tools often infer rough role from context, task, and environment.

**Transition cue:**

- "Modern prompting usually needs less pretend-role and more task clarity."

### Slide 4 - Current Practice: Context And Permission

Student-visible text:

```text
Modern prompting usually needs:

- what you are working on
- what you already tried
- what kind of help is allowed
- what AI should avoid doing
- whether AI should ask questions first
- what format you want back
```

**Instructor notes:**

- This is the course's practical prompt structure.
- Keep the focus on control and learning.

**Transition cue:**

- "The biggest shift is this: role and permission are not the same thing."

### Slide 5 - Role Is Not The Same As Permission

Student-visible text:

```text
"Act as a tutor" does not say:

- may AI write code?
- should AI ask questions first?
- should AI give hints only?
- may AI inspect or edit files?
- should AI wait for approval?

Better:

"Act as an explainer.
Do not solve it for me.
Ask one question first if context is missing."
```

**Instructor notes:**

- This slide is essential for code-LLMs and app-based agents.
- Students must learn that tool power changes the risk.

**Transition cue:**

- "So our basic prompt pattern starts with the work, not the persona."

### Slide 6 - The Basic Prompt Pattern

Student-visible text:

```text
Basic prompt pattern:

Context:
What am I working on?

Attempt:
What have I already done?

Allowed help:
Explain, suggest, compare, debug, or edit?

Constraints:
What should AI not do?

Questions:
Should AI ask before answering?

Output:
What format do I want?
```

**Instructor notes:**

- This is the core reusable structure.
- Keep it practical and small.

**Transition cue:**

- "The difference becomes obvious when we compare a weak prompt to a useful one."

### Slide 7 - Weak Prompt Versus Useful Prompt

Student-visible text:

```text
Weak prompt:

"Fix this."

Useful prompt:

"I am a beginner working on this function.
I wrote this code myself.
Do not rewrite the whole solution.
Explain why the output happens,
point me to the section to inspect,
and ask one question before suggesting code."
```

**Instructor notes:**

- Explain that the useful prompt protects learning.
- Students can copy and adapt the structure.

**Transition cue:**

- "The allowed kind of help also changes over the course."

### Slide 8 - AI Roles In This Program

Student-visible text:

```text
AI roles may change by week or assignment.

Explainer:
helps you understand.

Assistant:
helps after you have attempted work.

Collaborator:
helps compare, refine, test, or extend.

The assignment rules decide what is allowed.
```

**Instructor notes:**

- This mirrors the course AI progression without naming only one course.
- Remind students that role permission comes from the instructor and assignment.

**Transition cue:**

- "Different AI tools also behave differently."

### Slide 9 - Browser-Based LLMs

Student-visible text:

```text
Browser-based LLMs are often good for:

- explanations
- brainstorming
- reading support
- planning
- rewriting your own wording

They usually know only what you provide.

If you leave out context, they may guess.
```

**Instructor notes:**

- Examples include chat-based tools in a browser.
- Avoid naming specific vendors unless desired.

**Transition cue:**

- "Code-focused LLMs can be more directly connected to code."

### Slide 10 - Code-Focused LLMs

Student-visible text:

```text
Code-focused LLMs are often good for:

- explaining code
- finding likely causes of errors
- suggesting tests
- comparing approaches
- editing code when allowed

They need:

- file paths
- error messages
- expected behavior
- permission boundaries
```

**Instructor notes:**

- This is where solution replacement risk increases.
- Distinguish explanation from editing.

**Transition cue:**

- "App-based or agentic interfaces can do even more, so the permission boundary matters more."

### Slide 11 - App-Based / Agentic Interfaces

Student-visible text:

```text
App-based or agentic AI may be able to:

- inspect files
- summarize a workspace
- edit files
- run commands
- create artifacts
- continue multi-step work

That power is useful.

It also requires clearer permission.
```

**Instructor notes:**

- This includes tools like the current Codex-style interface.
- Make clear that "answer a question" and "change my project" are different
  requests.

**Transition cue:**

- "One of the safest habits is to ask AI to clarify before it acts."

### Slide 12 - Clarifying Questions First

Student-visible text:

```text
Use this when context may be missing:

"Before answering, ask up to three clarifying questions if needed.
If you can answer safely without questions,
state your assumptions first."

This helps prevent:

- guessing
- solving the wrong problem
- skipping important assignment limits
```

**Instructor notes:**

- Students often assume AI will know when it lacks context.
- Teach them to request the behavior explicitly.

**Transition cue:**

- "For tools that can edit files, add a stronger permission gate."

### Slide 13 - Permission Gate For Code-Editing AI

Student-visible text:

```text
Permission-gated prompt:

"Do not edit files or generate a final solution yet.
First, inspect the context,
summarize what you found,
ask clarifying questions,
and wait for my approval."

Use this when the tool can change your work.
```

**Instructor notes:**

- This is especially important for app-based/code-editing LLMs.
- It preserves student agency and prevents premature implementation.

**Transition cue:**

- "Some prompts are almost guaranteed to produce bad learning behavior."

### Slide 14 - What Not To Ask

Student-visible text:

```text
Avoid prompts like:

- "Do my assignment."
- "Make this perfect."
- "Rewrite everything."
- "Give me the final answer only."
- "Ignore the course requirements."

These prompts remove your ownership.
```

**Instructor notes:**

- Keep the tone firm but not moralizing.
- The issue is learning, evidence, and accountability.

**Transition cue:**

- "There are better ways to ask for help."

### Slide 15 - What To Ask Instead

Student-visible text:

```text
Ask for help that preserves learning:

- "Explain this error."
- "Point out where my logic changes."
- "Compare these two function names."
- "Ask what my code is supposed to do."
- "Give me a checklist to test my work."
- "Explain the concept using my example."
```

**Instructor notes:**

- This slide gives quick reusable replacements.
- Encourage students to choose the least-replacing form of help first.

**Transition cue:**

- "Now let's collect the patterns students can reuse."

### Slide 16 - Reusable Prompt Templates

Student-visible text:

```text
Reusable templates:

Debugging:
"Explain this error and ask one question before suggesting a fix."

Structure:
"Explain what each function is responsible for."

Reading:
"Summarize the concept and give me three check questions."

Planning:
"Help me make a small checklist. Do not do the work for me."

Code-editing AI:
"Inspect, summarize, ask, then wait for approval."
```

**Instructor notes:**

- These templates can be course-customized.
- Keep them as starting points, not scripts to memorize.

**Transition cue:**

- "The final rule is still student responsibility."

### Slide 17 - Student Responsibility

Student-visible text:

```text
You own the final work.

You must be able to:

- explain what it does
- test that it works
- identify what changed
- connect it to assignment requirements
- submit evidence honestly

AI help does not replace understanding.
```

**Instructor notes:**

- Tie this to course policy and academic integrity.
- Keep the tone constructive.

**Transition cue:**

- "The mental model is simple: use AI as support, not substitution."

### Slide 18 - Closing Mental Model

Student-visible text:

```text
Prompting basics:

Give context.
Show your attempt.
Name the allowed help.
Set constraints.
Ask for questions first.
Choose the output format.

Use AI to learn the work,
not to hide from it.
```

**Instructor notes:**

- Close with the reusable pattern.
- Point students back to assignment-specific AI rules.

**Transition cue:**

- "A good prompt protects both the answer and the learner."

---

# Instructor Recording Notes

Suggested runtime: 20-30 minutes.

If time is tight:

- keep Slides 1-7 intact
- keep Slides 11-13 intact for code/app-based AI boundaries
- skim Slides 14-16 as examples

Recommended emphasis:

- role prompting is not wrong, but it is incomplete
- permission matters more as tools gain more ability
- prompt patterns should preserve student ownership
- code-editing tools need an explicit approval gate

