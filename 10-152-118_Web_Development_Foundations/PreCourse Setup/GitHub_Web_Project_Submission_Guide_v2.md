# GitHub Web Project Submission Guide v2

## 10-152-118 Web Development Foundations

Use this guide to prepare and submit web-development work. Schoology is the source for assignment instructions, due dates, grading criteria, and submission activities. GitHub is where you keep the HTML, CSS, JavaScript, documentation, and testing evidence for your work.

## The Two Repository Roles

Do not confuse the public course repository with your project repository.

```text
Public SWTC-AAISE course repository
  weeks/
    week-01-.../
      demos/

Your private web project repository
  index.html
  css/
    styles.css
  js/
    script.js
  data/
  README.md
  reasoning-and-ai-use.md
  testing-evidence.md
```

The public course repository is a reference library. It contains instructor demos and selected course code. Your private repository is your own evolving project and submission package.

## Course Project Continuity

In this course, you will usually build and improve **one project repository over time**. Each week, you add, revise, test, and explain a new layer of the same project.

Do not create a new repository every week unless the Schoology assignment explicitly tells you to do so. Preserve your prior work and use meaningful commits to show how your project develops.

## Individual Project Workflow

1. Review the assigned Schoology material and any designated public SWTC-AAISE demo, starter, template, or project resource.
2. Create a **new private repository** in your personal GitHub account for your course project. Unless your instructor provides another name, use:

   ```text
   aaise-118-project-name-your-github-username
   ```

3. Create the repository without adding a README, `.gitignore`, or license. This keeps it ready for one of the starter-code methods below.

### Method 1: Copy assigned starter files into your new repository

Use this method for a small set of starter files or when you are building your own project structure.

1. Clone your new private repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   ```

2. Open the cloned folder in VS Code.
3. Copy the assigned starter files into the appropriate folders, or create the project structure required by Schoology.
4. Add `README.md`, `reasoning-and-ai-use.md`, and `testing-evidence.md`.
5. Make the first commit and push it:

   ```bash
   git add .
   git commit -m "Create project foundation"
   git push -u origin main
   ```

### Method 2: Clone an assigned public SWTC-AAISE resource, then connect it to your repository

Use this method when your instructor designates an existing public SWTC-AAISE resource as the starting point for your project. The assigned source may be:

- a dedicated starter-code repository
- a public course repository
- a public demo repository
- a larger multi-file starter project

Do not assume that every public demo or the PageForge example is a starter. Use this method only for the resource your instructor identifies in Schoology or during class.

1. Clone the assigned public SWTC-AAISE source repository:

   ```bash
   git clone https://github.com/ORGANIZATION/ASSIGNED-STARTER-REPOSITORY.git
   cd ASSIGNED-STARTER-REPOSITORY
   ```

2. Rename the original remote so you retain a reference to the public source:

   ```bash
   git remote rename origin course-source
   ```

3. Add your new private project repository as `origin`:

   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   git remote -v
   ```

4. Push the baseline to your private repository:

   ```bash
   git push -u origin main
   ```

5. Open the folder in VS Code and begin building your own project. Replace, extend, or refactor starter content as the assignment requires.

## Required Project Artifacts

Unless a specific assignment says otherwise, your private project repository should include the following.

| Artifact | Purpose |
| --- | --- |
| `README.md` | A concise project index with purpose, current features, run instructions, and links to evidence artifacts. |
| HTML, CSS, and JavaScript files | Your working web project. |
| `reasoning-and-ai-use.md` | Your project framing, design/technical decisions, revisions, and AI-use explanation. |
| `testing-evidence.md` | Your browser, interaction, layout, form, data, or accessibility testing evidence. |
| `data/`, images, or other supporting files | Any required project resources. |

Use clear folders and file names. Do not place passwords, access tokens, API keys, or private personal information in the repository.

## Reasoning and AI Use

In `reasoning-and-ai-use.md`, explain:

1. Your project purpose, intended users, and selected project track or approved idea.
2. Your design, structure, behavior, data, and usability decisions.
3. Important revisions, debugging, tradeoffs, or improvements made over time.
4. Whether, when, and how AI was used.
5. What AI suggestions you accepted, rejected, corrected, tested, or adapted.
6. How you verified that you understand and can explain the current project.

Follow the AI-use boundary stated in the Schoology assignment. You remain responsible for the functionality, testing, explanation, and submitted work.

## Testing Evidence

Use `testing-evidence.md` to make your project behavior visible. Include the evidence required by the assignment, such as:

- page and navigation checks
- browser or viewport checks
- expected and actual interaction results
- input validation or form behavior
- data, storage, or API-response checks
- accessibility, usability, or security observations
- bugs found, fixes made, and retesting evidence

Someone reviewing your repository should be able to understand how you tested the project without guessing.

## Weekly Progress and Submission

Commit small, meaningful changes as your project evolves:

```bash
git add .
git commit -m "Add responsive card layout"
git push
```

When Schoology requires a weekly checkpoint, submit the project repository URL and any required commit hash, tag, screenshot, reflection, or evidence. Do not rewrite Git history, force-push, or delete commits after a checkpoint unless your instructor directs you to do so.

## Paired Programming Workflow

Use paired programming only when the assignment permits it. Use one shared **private** repository for the pair.

1. Choose one repository owner.
2. Create the shared private repository using this pattern unless directed otherwise:

   ```text
   aaise-118-project-name-lastname-lastname
   ```

3. The owner invites the partner as a collaborator.
4. Both partners clone the same repository and make commits for the work they perform.
5. Use branches and pull requests when work needs partner review before it is merged into `main`.
6. Add `collaboration-record.md` describing each partner's contributions, decisions, review activity, and shared work.
7. Before submission, confirm both partners have access, both names appear in the README, and the final work is committed and pushed to `main`.

Each partner must be able to explain the completed project, testing evidence, and documented AI use.

## Final Submission Checklist

Before submitting in Schoology:

1. Confirm the repository is private unless the assignment explicitly requires public visibility.
2. Confirm the project runs locally and its navigation, styling, and required interactions work as expected.
3. Confirm the repository includes the required code, Markdown evidence artifacts, and supporting files.
4. Check that all work is committed and pushed:

   ```bash
   git status
   git push
   ```

5. Confirm that `README.md` identifies or links to the reasoning-and-AI-use and testing-evidence artifacts.
6. Submit the repository URL and any other required item through the Schoology activity.
7. Do not change repository visibility or rewrite Git history after submission unless your instructor directs you to do so.

## Common Mistakes To Avoid

- Editing or committing directly in the public course repository.
- Starting a new project repository every week when the course expects iterative development.
- Treating an instructor demo or PageForge as the required project to copy.
- Submitting only source code with no reasoning or testing evidence.
- Leaving evidence only in a Schoology comment.
- Forgetting to push the final version.
- Using AI beyond the assignment boundary or failing to explain its use.
- In pair work, leaving one partner without access or without visible contribution.

## Simple Rule

If your instructor opens your repository, they should be able to locate your working project, reasoning and AI-use explanation, testing evidence, and supporting files without searching through unrelated locations.
