# GitHub Assignment Submission Guide v2

## 10-152-117 Python Programming Foundations

Use this guide to prepare and submit Python programming assignments. Schoology is the source for assignment instructions, due dates, grading criteria, and submission activities. GitHub is where you keep the code and supporting evidence for your work.

## The Two Repository Roles

Do not confuse the public course repository with your submission repository.

```text
Public SWTC-AAISE course repository
  weeks/
    week-01-.../
      demos/

Your private assignment repository
  README.md
  assignment_01_solution.py
  reasoning-and-ai-use.md
  testing-evidence.md
  data/
```

The public course repository is a reference library. It contains instructor demos and selected course code. Your private repository is your own assignment submission package.

## Individual Assignment Workflow

1. Open the assigned demo, starter, template, or other public SWTC-AAISE resource identified in Schoology.
2. Create a **new private repository** in your personal GitHub account. Unless your instructor provides another name, use:

   ```text
   aaise-117-assignment-01-your-github-username
   ```

3. Create the repository without adding a README, `.gitignore`, or license. This keeps it ready for one of the starter-code methods below.

### Method 1: Copy an assigned starter file into your new repository

Use this method for a small starter, such as one Python file.

1. Clone your new private repository to your computer:

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   ```

2. Open the cloned folder in VS Code.
3. Download or copy the assigned starter file from the public course repository into this folder.
4. Add the required Markdown evidence artifacts.
5. Make the first commit and push it:

   ```bash
   git add .
   git commit -m "Add assignment starter and submission artifacts"
   git push -u origin main
   ```

### Method 2: Clone an assigned public SWTC-AAISE resource, then connect it to your repository

Use this method when your instructor designates an existing public SWTC-AAISE resource as the starting point for your work. The assigned source may be:

- a dedicated starter-code repository
- a public course repository
- a public demo repository
- a larger multi-file starter project

Do not assume that every public demo is a starter. Use this method only for the resource your instructor identifies in Schoology or during class.

1. Clone the assigned public source repository:

   ```bash
   git clone https://github.com/ORGANIZATION/ASSIGNED-STARTER-REPOSITORY.git
   cd ASSIGNED-STARTER-REPOSITORY
   ```

2. Rename the original remote so you retain a reference to the public source:

   ```bash
   git remote rename origin course-source
   ```

3. Add your new private repository as `origin`:

   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   git remote -v
   ```

4. Push the starter baseline to your private repository:

   ```bash
   git push -u origin main
   ```

5. Open the folder in VS Code, complete the assignment, and add the required Markdown evidence artifacts.

### Complete and submit the assignment

1. Complete the assignment, update the evidence artifacts, and save meaningful commits as you work:

   ```bash
   git add .
   git commit -m "Implement assignment requirements"
   git push
   ```

2. Complete the final submission checklist and submit the repository URL through Schoology.

Do not commit directly to the public SWTC-AAISE course repository.

## Required Submission Artifacts

Unless a specific assignment says otherwise, your private repository should include the following.

| Artifact | Purpose |
| --- | --- |
| `README.md` | A concise index that identifies the assignment and links to the submitted files. |
| Assignment solution file(s) | Your executable Python implementation. |
| `reasoning-and-ai-use.md` | Your problem framing, assumptions, reasoning, revisions, and AI-use explanation. |
| `testing-evidence.md` | Your test cases, expected and actual results, validation evidence, or other required testing. |
| `data/` or other supporting files | Any required input, output, JSON, CSV, or supporting resource. |

For a larger assignment or capstone, organize the code into clear folders as directed in Schoology, but retain the root `README.md`, `reasoning-and-ai-use.md`, and `testing-evidence.md` files.

## Reasoning and AI Use

In `reasoning-and-ai-use.md`, explain:

1. Your initial understanding of the problem.
2. Your inputs, outputs, assumptions, constraints, and intended approach.
3. Important decisions, tradeoffs, debugging, or changes you made while working.
4. Whether, when, and how AI was used.
5. What AI suggestions you accepted, rejected, corrected, tested, or adapted.
6. How you verified that you understand and can explain the final submission.

Follow the AI-use boundary stated in the Schoology assignment. You remain responsible for the correctness, testing, explanation, and submitted work.

## Testing Evidence

Use `testing-evidence.md` to make your program’s behavior visible. Include the evidence required by the assignment, such as:

- normal and edge test cases
- expected and actual results
- pass/fail outcomes
- file, data, error-handling, or API response evidence
- failed tests, debugging steps, and revisions

Someone reviewing your repository should be able to understand how you tested the solution without guessing.

## Paired Programming Workflow

Use paired programming only when the assignment permits it. Use one shared **private** repository for the pair.

1. Choose one repository owner.
2. Create the shared private repository using this pattern unless directed otherwise:

   ```text
   aaise-117-assignment-01-lastname-lastname
   ```

3. The owner invites the partner as a collaborator.
4. Both partners clone the same repository and make commits for the work they perform.
5. Use branches and pull requests when work needs partner review before it is merged into `main`.
6. Add `collaboration-record.md` describing each partner's contributions, decisions, review activity, and shared work.
7. Before submission, confirm both partners have access, both names appear in the README, and the final work is committed and pushed to `main`.

Each partner must be able to explain the completed code, testing evidence, and documented AI use.

## Final Submission Checklist

Before submitting in Schoology:

1. Confirm the repository is private unless the assignment explicitly requires public visibility.
2. Confirm the repository includes the required code, Markdown evidence artifacts, and supporting files.
3. Run the program locally using the required command or workflow.
4. Check that all work is committed and pushed:

   ```bash
   git status
   git push
   ```

5. Confirm that `README.md` links to or identifies the solution, reasoning-and-AI-use, and testing-evidence artifacts.
6. Submit the repository URL and any other required item through the Schoology activity.
7. Do not rewrite Git history, force-push, delete commits, or change visibility after submission unless your instructor directs you to do so.

## Common Mistakes To Avoid

- Editing or committing directly in the public course repository.
- Submitting only Python code with no reasoning or testing evidence.
- Leaving evidence only in a Schoology comment.
- Forgetting to push the final version.
- Treating an instructor demo as the required assignment solution.
- Using AI beyond the assignment boundary or failing to explain its use.
- In pair work, leaving one partner without access or without visible contribution.

## Simple Rule

If your instructor opens your repository, they should be able to locate your code, reasoning and AI-use explanation, testing evidence, and supporting files without searching through unrelated locations.
