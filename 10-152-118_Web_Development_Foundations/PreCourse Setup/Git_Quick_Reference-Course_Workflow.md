# **Git Quick Reference — Course Workflow**

---

## 🧭 **Core Idea**

> Work in small steps.
> Commit often.
> Push your work.

---

# 🧱 **Weekly Workflow (Always Follow This)**

```plaintext
Create Branch → Work → Commit → Refine → Commit → Push
```

---

# 🔹 **1. Create a New Branch (Start of Week)**

```bash
git checkout -b week01-html
```

✔ Creates a new branch
✔ Keeps your work organized

---

# 🔹 **2. Check Status (What Changed?)**

```bash
git status
```

✔ Shows modified files
✔ Helps you confirm what will be committed

---

# 🔹 **3. Stage Your Changes**

```bash
git add .
```

✔ Adds all changes
✔ Prepares files for commit

---

# 🔹 **4. Commit Your Work**

```bash
git commit -m "Week 1 - Iteration 1"
```

✔ Saves your progress
✔ Creates a checkpoint

---

# 🔹 **5. Push to GitHub**

```bash
git push origin week01-html
```

✔ Sends your work to GitHub
✔ Required for submission

---

# 🔁 **Typical Weekly Commits**

```bash
git commit -m "Week X - Iteration 1"
git commit -m "Week X - Iteration 2"
```

---

# 🧠 **What Each Command Means**

| Command      | Purpose          |
| ------------ | ---------------- |
| `git status` | What changed?    |
| `git add .`  | Prepare files    |
| `git commit` | Save progress    |
| `git push`   | Upload to GitHub |

---

# ⚠️ **Common Problems & Fixes**

---

## ❌ “My changes aren’t showing up on GitHub”

✔ You probably forgot:

```bash
git push origin <branch-name>
```

---

## ❌ “Nothing to commit”

✔ You may need:

```bash
git add .
```

---

## ❌ “I’m on the wrong branch”

✔ Check:

```bash
git branch
```

✔ Switch:

```bash
git checkout <branch-name>
```

---

## ❌ “I broke something”

✔ Good news: Git saved your earlier work
✔ Ask instructor or revert to previous commit

---

# 🔑 **Rules to Follow**

* Create a new branch each week
* Commit at least twice (Iteration 1 & 2)
* Push before submitting
* Keep messages simple and clear

---

# 🧭 **Branch Naming Pattern**

```plaintext
week01-html
week02-css
week03-layout
week04-js
```

---

# 🧠 **Pro Tip**

> If you’re unsure what to do:

```bash
git status
```

It will usually tell you what’s next.

---

# 🔑 **Final Thought**

> Git is not about perfection—it’s about saving progress and staying organized.

---
