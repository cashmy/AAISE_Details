# GitHub Lab Submission Guide v2

## 10-152-119 Algorithmic Problem Solving

Use this guide to prepare and submit programming labs. Schoology is the source for assignment instructions, due dates, grading criteria, and submission activities. GitHub is where you keep the code and supporting evidence for your lab work.

## The Two Repository Roles

Do not confuse the public course repository with your submission repository.

```text
Public SWTC-AAISE course repository
  labs/
    lab-01/
      demo/
      starter/

Your private lab submission repository
  README.md
  lab_01_solution.py
  reasoning-and-ai-use.md
  testing-evidence.md
  data/
```

The public course repository is a release library. It contains the instructor demo and starter files. Your private repository is your own lab submission package.

## Lab Release Sequence

Each lab follows this instructional sequence:

```text
Lecture concept -> instructor demo -> guided starter -> student evidence
-> post-lab success version
```

The instructor demo shows a related algorithmic pattern. Your lab requires you to apply that pattern to the assigned scenario and produce your own evidence. Complete success versions are released after the applicable attempt window closes.

## Individual Lab Workflow

1. Open the assigned lab in the public course repository and review the instructor demo.
2. Create a **new private repository** in your personal GitHub account. Use the required course naming convention. Unless your instructor provides another name, use:

   ```text
   aaise-119-lab-01-your-github-username
   ```

3. Create the repository without adding a README, `.gitignore`, or license. This keeps it ready for one of the starter-code methods below.

### Method 1: Copy the assigned starter file into your new repository

Use this method for a small starter, such as one Python file.

1. Clone your new private repository to your computer:

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   ```

2. Open the cloned folder in VS Code.
3. Download or copy the assigned starter file from the public course repository into this folder. Rename the solution file only if the Schoology assignment directs you to do so.
4. Add the required Markdown evidence artifacts.
5. Make the first commit and push it:

   ```bash
   git add .
   git commit -m "Add lab starter and submission artifacts"
   git push -u origin main
   ```

### Method 2: Clone an assigned public SWTC-AAISE resource, then connect it to your repository

Use this method when your instructor designates an existing public SWTC-AAISE resource as the starting point for your work. The assigned source may be:

- a dedicated starter-code repository
- a public course repository
- a public demo repository
- a larger multi-file starter project

Do not assume that every public demo is a starter. Use this method only for the repository or demo your instructor identifies in Schoology or during class.

1. Clone the assigned public SWTC-AAISE source repository:

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

5. Open the folder in VS Code, complete the lab, and add the required Markdown evidence artifacts.

### Complete and submit the lab

1. Complete the lab, update the evidence artifacts, and save meaningful commits as you work:

   ```bash
   git add .
   git commit -m "Implement initial lab decision rules"
   git push
   ```

2. Complete the final submission checklist and submit the repository URL through Schoology.

Do not commit directly to the public SWTC-AAISE course repository.

## Required Submission Artifacts

Unless a specific lab says otherwise, your private repository should include the following.

| Artifact | Purpose |
| --- | --- |
| `README.md` | A concise index that identifies the lab, names the submitted files, and links to the evidence artifacts. |
| Lab solution file(s) | Your executable Python implementation or required simulation. |
| `reasoning-and-ai-use.md` | Your problem framing, assumptions, reasoning, revisions, and AI-use explanation. |
| `testing-evidence.md` | Your test cases, expected and actual results, evidence tables, timing/comparison data, or other required validation. |
| `data/` or other supporting files | Any required input, output, diagram, image, or data file. |

Keep reasoning and evidence in separate Markdown files rather than placing all written material in a Schoology comment or inside the Python file.

## Reasoning and AI Use

In `reasoning-and-ai-use.md`, explain:

1. Your initial understanding of the problem.
2. Your inputs, outputs, assumptions, constraints, and selected approach.
3. Important decisions, tradeoffs, or changes you made while working.
4. Whether, when, and how AI was used.
5. What AI suggestions you accepted, rejected, corrected, tested, or adapted.
6. How you verified that you understand and can explain the final submission.

Follow the AI-use boundary stated in the specific Schoology assignment. You remain responsible for the correctness, testing, explanation, and submitted work.

## Testing Evidence

Use `testing-evidence.md` to make your algorithm’s behavior visible. Include the evidence required by the lab, such as:

- normal and edge test cases
- expected and actual results
- pass/fail outcomes
- trace, timing, comparison, ranking, or traversal tables
- explanation of failed tests and revisions

Someone reviewing your repository should be able to understand how you tested the solution without guessing.

## Paired Programming Workflow

Use one shared **private** repository for the pair. Do not create two separate repositories and attempt to merge them at the end.

1. Choose one repository owner.
2. Create the shared private repository using this pattern unless directed otherwise:

   ```text
   aaise-119-lab-01-lastname-lastname
   ```

3. The owner invites the partner as a collaborator.
4. Both partners clone the same repository and make commits for the work they perform.
5. Use branches and pull requests when work needs partner review before it is merged into `main`.
6. Add `collaboration-record.md` describing each partner’s contributions, decisions, review activity, and any shared work.
7. Before submission, confirm both partners have access, both names appear in the README, and the final work is committed and pushed to `main`.

Each partner must be able to explain the completed solution, testing evidence, and documented AI use.

## Final Submission Checklist

Before submitting in Schoology:

1. Confirm the repository is private unless the assignment explicitly requires public visibility.
2. Confirm the repository includes the required code, Markdown evidence artifacts, and supporting files.
3. Run the project locally using the required command or workflow.
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
- Submitting only code with no reasoning or testing evidence.
- Leaving evidence only in a Schoology comment.
- Forgetting to push the final version.
- Treating an instructor demo as the required lab solution.
- Using AI beyond the assignment boundary or failing to explain its use.
- In pair work, leaving one partner without access or without visible contribution.

## Simple Rule

If your instructor opens your repository, they should be able to locate your code, reasoning and AI-use explanation, testing evidence, and supporting files without searching through unrelated locations.
