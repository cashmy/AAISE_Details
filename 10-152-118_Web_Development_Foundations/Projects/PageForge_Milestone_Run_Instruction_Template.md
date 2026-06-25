# **PageForge — Milestone Run Instruction Template**

---

## **Purpose**

This template is the lightweight operator wrapper used alongside the reusable milestone prompts.

It is not a replacement for:

* `PageForge_Initial_Milestone_Prompt.md`
* `PageForge_Ongoing_Milestone_Generation_Prompt.md`

Instead, it provides the run-specific instruction layer for a single milestone generation.

Use it to supply:

* the exact target milestone
* the exact source milestone
* the target week
* the target phase
* what the milestone should represent
* what it must improve or preserve
* what it must avoid

This keeps the core prompts reusable while still giving each run the specificity it needs.

---

## **How to Use**

1. Choose the correct reusable prompt:
   * use the **Initial Milestone Prompt** for the very first milestone
   * use the **Ongoing Milestone Prompt** for all later milestones
2. Copy this template into the VS Code session as the run-specific instruction block
3. Fill in the bracketed placeholders
4. Attach the governing artifacts:
   * roadmap
   * phase constraints
   * preservation directives
   * design contract
   * source milestone, when applicable

---

## **Run Instruction Template**

```text
Generate the PageForge milestone for the following target:

Target milestone:
`[target-milestone-name]`

Target week:
`[week-number or week-title]`

Target phase:
`[build | refine | contrastive-build | contrastive-refine]`

Source milestone:
`[source-milestone-name or N/A if first milestone]`

This is a `[phase]` phase generation.
It is NOT:
- a canonical generation run
- a generic week-level completed milestone
- permission to introduce features from later weeks

Follow the roadmap strictly.
Follow the phase constraints artifact strictly.

If the phase constraints artifact is more specific than the roadmap for this target, the phase constraints artifact wins.

This output must represent what could plausibly exist at this exact point in the course.

MILESTONE INTENT
This milestone should represent:
[describe what this milestone should mean instructionally]

WHAT TO IMPROVE OR INTRODUCE
- [item]
- [item]
- [item]

WHAT TO PRESERVE
- [item]
- [item]
- [item]

WHAT TO AVOID
- [item]
- [item]
- [item]

PHASE RULES
If this is a `build` phase:
- keep the milestone intentionally incomplete
- do not include improvements that belong to the same week’s refine state

If this is a `refine` phase:
- begin from the same week’s build milestone unless explicitly instructed otherwise
- improve clarity, correctness, and structure only within this week’s scope
- do not leak next-week capabilities into this milestone

If this is a contrastive phase:
- preserve the instructional contrast clearly
- do not “helpfully” remove the flawed or incomplete state if it is part of the lesson

OUTPUT REQUIREMENTS
Generate:
1. the target milestone file tree
2. the contents of each created or updated file in the target milestone
3. a short summary of what changed from the source milestone
4. a short list of intentionally deferred features or intentionally preserved flaws
5. suggested `notes.md` content
6. a short statement confirming the exact week and phase represented by the output
```

---

## **Example Use Cases**

### **Week 1 Build**

* Target milestone: `week01-build-foundation`
* Source milestone: `N/A`
* Phase: `build`

### **Week 1 Refine**

* Target milestone: `week01-refine-structured-pages`
* Source milestone: `week01-build-foundation`
* Phase: `refine`

### **Week 6 Debug Seeded**

* Target milestone: `week06-build-debug-seeded`
* Source milestone: `week05-refine-[state]`
* Phase: `contrastive-build`

### **Week 6 Debug Fixed**

* Target milestone: `week06-refine-debug-fixed`
* Source milestone: `week06-build-debug-seeded`
* Phase: `contrastive-refine`

---

## **Operator Reminder**

This template provides the run-specific instruction layer only.

The stable governance should still come from the main prompt artifacts and the supporting documents.

If a run starts drifting, fix the governing artifacts first where appropriate, then refine this instruction layer as needed.

---
