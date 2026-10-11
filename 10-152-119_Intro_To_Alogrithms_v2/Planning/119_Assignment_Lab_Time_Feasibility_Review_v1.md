# 119 Assignment Lab-Time Feasibility Review

Instructor decision draft v1 | October 9, 2026

Subsequent context: the [updated assignment map](119_Assignment_List_and_Progression_Map_v1.md) now records expected individual homework, Week 1 pairing adjustment, Week 5 lower-pressure consolidation, Week 6 self-selected pairs/trio, and implemented Week 4 modular scaffolding. This review remains the original lab-only planning estimate; its recommendations and completion ranges have not been remeasured. Read its fit findings as lab-capacity risks, not automatic rejection of intentionally planned homework.

## 1. Finding

**Do not approve the current timing splits unchanged.** The proposed assignments are substantially stronger than the original labs, but the workload is uneven. Week 1 has the clearest spare-capacity risk. Weeks 3, 4, 5, and 6 need explicit boundaries or time reallocation before packets are written. Weeks 2 and 7 are plausible fits with the promised scaffolding.

The most actionable concerns are AL04's 100-minute search window, AL06's 90-minute recursion/iteration window, AL03's expanding state-management surface, and AL08's Thursday path-plus-restriction workload. Reallocating split-week minutes alone does not fix a combined weekly overload.

This review evaluates the [Assignment Progression v1](119_Assignment_List_and_Progression_Map_v1.md), [Selective Pairing Plan](119_Selective_Paired_Programming_and_Remote_Lab_Plan_v1.md), [Demo Map](119_Demo_List_and_Reference_App_Milestones_v1.md), and [Coverage Map v3](119_Textbook_Coverage_and_Reference_Map_v3.md). It does **not** create student assignments, change deadlines/grades, adopt collaboration modes, or revise the proposed scope automatically.

These are bottom-up planning estimates, not measured student completion times. The ranges describe prepared prerequisite-level students working toward the complete stated evidence, with ordinary debugging. They are not confidence intervals, a cohort percentile forecast, or a guarantee that all students finish in class.

## 2. Actual Capacity and Counting Rules

| Day | Actual Meeting | Existing Planning Split | Task-Time Capacity Used in This Review |
| --- | --- | --- | --- |
| Monday | 120 min combined lecture/lab | 50 min instruction; 70 min lab | Approximately 60-65 min after 5-10 min operational reserve |
| Tuesday | 60 min lecture + 120 min lab | 120 min lab | Approximately 105-110 min after 10-15 min reserve |
| Thursday | 60 min lecture + 120 min lab | 120 min lab | Approximately 105-110 min after 10-15 min reserve |
| Regular week | 480 min total meeting time | 310 min gross lab | Approximately 270-285 min task time |

The 70-minute Monday lab is a planning choice within the confirmed combined meeting, not a separately guaranteed official lab allocation. A different lecture/lab split changes this analysis and should be an explicit decision.

Task estimates **include** assignment framing, implementation, tests/debugging, comparison/revision, relevant peer reasoning, evidence, and individual explanation. The operational reserve covers room transitions, file access/handoffs, saving/submission mechanics, short pauses, and interruptions; it does not subtract the same testing or explanation twice.

The pairing plan describes 230 minutes of breakout work and 80 minutes of framing/checkpoints/discussion across the week. Those 80 minutes are not all wasted overhead: predictions, review, and explanation are assignment work included in this model. Conversely, 310 scheduled minutes are not 310 uninterrupted coding minutes.

Daily demos and additional LRN recognition belong inside the teaching allocation, not the lab reserve. If instruction overruns by 15 minutes, the week's task capacity falls by another 15. Breaks, platform trouble, or support delays beyond the assumed reserve reduce capacity further.

### Outside-Class Time Is Not a Second Lab

The existing target is **60-120 minutes total** regular-week preparation/completion, including Monday reading.

| Reading Target | Assignment Completion Time Left From a 120-Minute Total |
| --- | --- |
| 45-60 min, most regular weeks | 60-75 min maximum |
| 60-75 min, Weeks 3-5 | 45-60 min maximum |

At the lower 60-minute total, little or no completion time remains; a 75-minute reading already exceeds that lower target. Optional reading, if chosen, also uses time. Do not assume an additional 1-2 hours of assignment homework after reading.

Required paired work must fit synchronous lab time. A modest individual explanation or cleanup can use the remaining allowance if explicitly planned; unfinished shared algorithm development cannot quietly become a required off-class partner meeting.

## 3. Bottom-Up Assignment Estimates

Minutes below are student/group elapsed task time, **not person-minutes**. Shared implementation is estimated once; individual predictions/explanations remain work for each student. Pairing does not halve learning time and a trio does not have three times the capacity.

Assumptions: supplied fixtures, interfaces, local drivers, timer/generation plumbing, and indicated reference helpers are ready; no menu/UI, persistence, live API, dataset research, or general framework is required. One compact evidence record reuses test output/traces rather than requiring several essays. If those supports are missing, these estimates are optimistic.

| Assignment | Contract / Framing | Core Build | Tests / Debugging | Comparison / Revision | Evidence / Review / Individual Explanation | Total Task Min |
| --- | --- | --- | --- | --- | --- | --- |
| AL01 | 20-30 | 45-65 | 25-35 | 30-45 | 35-55 | 155-230 |
| AL02 | 20-30 | 40-60 | 35-50 | 55-85 | 40-60 | 190-285 |
| AL03 | 25-35 | 90-130 | 55-85 | 30-45 | 35-55 | 235-350 |
| AL04 | 10-15 | 35-55 | 25-40 | 10-20 | 15-20 | 95-150 |
| AL05 | 15-25 | 60-90 | 35-55 | 40-60 | 30-40 | 180-270 |
| AL06 | 10-15 | 45-70 | 25-40 | 15-20 | 20-30 | 115-175 |
| AL07 | 15-20 | 40-60 | 30-45 | 40-65 | 25-35 | 150-225 |
| AL08 | 35-50 | 100-150 | 55-85 | 35-55 | 35-50 | 260-390 |
| AL09 | 20-30 | 70-110 | 45-65 | 50-75 | 35-50 | 220-330 |

| Assignment | Proposed Gross Lab Min | Estimated Task Min | Assessment |
| --- | --- | --- | --- |
| AL01 | 310 | 155-230 | Likely spare capacity; not too much work |
| AL02 | 310 | 190-285 | Conditional fit; protect interpretation time |
| AL03 | 310 | 235-350 | Overload risk unless operations are bounded |
| AL04 | 100 | 95-150 | Too tight for first independent binary search |
| AL05 | 210 | 180-270 | Tight; integration/measurement can exceed window |
| AL06 | 90 | 115-175 | Under-allocated; strongest split-week mismatch |
| AL07 | 220 | 150-225 | Fits current window; could lose time to AL06 |
| AL08 | 310 | 260-390 | High overload risk; Thursday bottleneck |
| AL09 | 310 | 220-330 | Conditional fit; weighting and evidence must be bounded |

AL04/05 and AL06/07 share a weekly reserve; their windows are not fully available task time. Working planning capacity is roughly 90-95 minutes for AL04, 180-190 for AL05, 80-85 for AL06, and 190-200 for AL07. These splits assign Monday's reserve to the first task and most Tue/Thu reserve to the second; actual transition placement can change them, but their weekly sum stays 270-285.

### Combined Weekly Fit

| Week | Assignments | Estimated Task Min | Against 270-285 Min Capacity |
| --- | --- | --- | --- |
| 1 | AL01 | 155-230 | Approximately 40-130 min spare across the modeled range |
| 2 | AL02 | 190-285 | Plausible fit; up to 15 min over at the high-demand/low-capacity combination |
| 3 | AL03 | 235-350 | Higher-demand cases exceed capacity by approximately 65-80 min |
| 4 | AL04 + AL05 | 275-420 | Tight even at the low estimate; high estimate exceeds capacity by 135-150 min |
| 5 | AL06 + AL07 | 265-400 | Low estimate fits; high estimate exceeds capacity by 115-130 min; AL06 is individually under-allocated |
| 6 | AL08 | 260-390 | Low estimate fits narrowly; high estimate exceeds capacity by 105-120 min |
| 7 | AL09 | 220-330 | Plausible with boundaries; high estimate exceeds capacity by 45-60 min |

These comparisons intentionally exclude homework. Some overrun could fit a published individual completion allowance, but the highest-risk cases exceed that allowance and/or involve shared work. The endpoints are illustrative planning bounds, not simultaneous predictions for every assignment.

## 4. Assignment-Specific Alerts and Decisions

### AL01: Likely Light for Stronger Students

The proposed record filtering, modular responsibilities, tests, defective-rule repair, and one changed rule should be reachable within the week. Familiarity with filtering and architectural thinking makes early completion credible, especially if the defective rule is obvious and the revision merely changes a constant.

Keep an accessible baseline. Before adding more features, ensure the required change demands a meaningful interaction between rules and that students independently justify expected outcomes. A compact unfamiliar-rule transfer check can use spare time without building a larger app. If students complete that with accurate explanations, add a bounded second revision or deeper cases; do not require everyone to spend 310 minutes on a task already mastered.

Risk: adding long documentation or artificial test counts to occupy time would not solve under-scoping.

### AL02: Fits if Experiment Mechanics Are Truly Supplied

The algorithms themselves may be short. The substantial work is predicting counted work, establishing result parity, controlling measurements, separating setup/query cost, and interpreting two workloads.

Four sizes by two workloads should run through a supplied batch harness, not eight manually assembled reports. Automate repeated trials and reuse one result table. Do not require an observed crossover, plots, memory profiling, or extra performance tuning.

Stronger pairs may finish early; one student-selected confound or held-out workload provides deeper investigation. Slower groups can fit if they do not build timer/data tooling from scratch. A functionally correct lookup is the baseline, not completion of the experiment.

### AL03: State Scope Needs Tightening

This is not just a dictionary/queue exercise. Duplicate identity, processing, undo, updates, cancellation, stale entries, and filtered snapshots interact. Their interaction tests create more work than the number of short functions suggests.

Before writing the packet, select one reversible action and specify its restoration contract. Compare list/keyed operations using focused functions or traces; do not require two complete registry implementations. Use a supplied action driver and a defined cancellation/update policy, not arbitrary operations in every state. Assess one clear invariant plus issued interaction cases.

Do not introduce unrestricted edit/delete-after-processing and then require a general undo/conflict policy. A narrowed task can target roughly 230-285 minutes; the existing broad interpretation is not reliably accommodated.

### AL04 and AL05: Week 4 Is the Highest Combined Load

AL04 is individual and includes two implementations, a wrong-key failure case, duplicate semantics, tests, and two traces. Only 100 gross minutes are allocated. First independent binary-search debugging can consume the Tuesday checkpoint before AL05 starts.

AL05 then requires stable insertion sort, instrumentation, library parity, composition, two ordering contracts, workload evidence, and an adaptation. Its recovery search scaffold prevents a missing AL04 from blocking progress; it does not make the rest of AL05 free.

Recommendation before packet production:

- Use one documented any-match duplicate policy; keep first/last-match algorithms optional.
- Supply compatible function signatures and malformed-record handling.
- Let AL05 reuse one tested filter or supply it, rather than re-assess a fresh filter build.
- Reuse AL02 measurement plumbing and AL04 evidence; do not duplicate the same report.
- Bound the pipeline experiment and issue one changed requirement, not multiple independent changes.
- Consider a 120/190 gross-minute split instead of 100/210, but only after narrowing the combined task. That reallocation gives AL04 time by taking it from AL05.

Seek a combined target near 250-285 task minutes. Without these boundaries, flag Week 4 as **too much proposed work**, not merely a release-timing problem.

### AL06 and AL07: Week 5 Has a Wrong-Sized Split

AL06's 90 gross minutes leave roughly 80-85 task minutes for two traversal implementations, base/malformed cases, tests, traces, and comparison. Even the modeled low estimate is 115 minutes. Prior architecture/filtering success does not establish recursion readiness.

AL07 is more generously allocated at 220 gross minutes and supplies the exhaustive reference, recurrence, and counters. It can fit as two tightly bounded investigations. Open-ended counterexample discovery, a new exhaustive solver, or a general DP build would change that finding.

Consider approximately 130/180 gross minutes: Monday 70 plus Tuesday 60 for AL06; Tuesday 60 plus Thursday 120 for AL07. This is a proposal, not an adopted schedule. It requires Tuesday's greedy investigation to fit a shorter segment.

To make that split plausible, specify AL06's leaf/schema policy, keep malformed cases focused, and reuse equivalent expected outputs in one compact trace/comparison. For AL07, supply the counterexample when needed, keep exhaustive inputs tiny, and require only one memoization change and a small fresh-cache count comparison. Aim for roughly 110-125 task minutes for AL06 and 150-160 for AL07; near the upper combined estimate there is little slack.

Do not make AL06's checkpoint a hard mid-class deadline or require unfinished recursion work to compete with the newly introduced greedy task without a recovery path.

### AL08: Graph Debugging and Thursday Are High Risk

A personally justified model, adjacency validation, two traversals, cycle/disconnection behavior, parent tracking, path reconstruction, tests, and an individual restriction response are substantive new work. Pairing supports questions but does not remove the learning burden.

Monday modeling should use a bounded supplied node/edge vocabulary and a small model choice, not unrestricted network invention. After that, use the proposed common fixture for shared traversal work. Reuse BFS parent information for path finding rather than requiring a separate traversal implementation.

Thursday introduces path reconstruction before an individual node/edge restriction and evidence. Keep one restriction type/core variant, supply surrounding path interfaces/driver, and retain enough individual time to test and explain the change. Teach/practice some parent-state reasoning Tuesday where appropriate, without requiring an untaught path implementation.

Target the bounded version near 250-285 minutes. If the published packet still expects the broad 260-390-minute interpretation, it does not reliably fit. The highest demand is shared development, so off-class individual cleanup is not a complete remedy.

### AL09: Plausible, but Not a Miniature Full Navigator

Shared-tag count, Jaccard, top-k, weights, sensitivity, missing data, and digest interpretation are several related learning targets. They can fit when the resource subset, schema and canonicalization helper are supplied.

Specify one weighted formula/default policy rather than asking students to invent several. Keep hand calculations to selected small cases, use one changed profile/coverage example, and demonstrate one local metadata edit/digest comparison. No URL research, live API, app shell, clustering implementation, or independent serialization framework.

Finish weighted ranking during Tuesday where possible. Thursday's main required outcome is a concrete limitation plus a bounded integrity investigation, not a second scoring system. Keep evidence in one score/rank table and a short individual explanation. Target roughly 220-285 minutes; the broad upper estimate would consume most or all outside-class completion allowance.

## 5. Day-Level Bottlenecks

| Week | Bottleneck | Checkpoint Needed Before the Next Phase |
| --- | --- | --- |
| 1 | Thursday's rule change can be trivial or excessive depending on wording | Tuesday: working baseline with independently justified boundary tests |
| 2 | Tuesday can disappear into harness setup | Monday: equivalent lookup contracts, initial parity/counts; harness launches successfully |
| 3 | Thursday interaction failures can expose an incomplete queue/undo foundation | Tuesday: one processing/undo transition works and preserves the stated invariant |
| 4 | AL04 overrun consumes AL05's Tuesday sort baseline | Flexible search checkpoint plus recovery interface; sort parity before Thursday pipeline work |
| 5 | AL06 overrun blocks Tuesday's greedy investigation | Recursion/iteration parity or targeted recovery; explicit revised split before release |
| 6 | Path reconstruction and individual restrictions both land Thursday | Tuesday: both traversals terminate on the common cyclic fixture; parent-state scaffold is understood |
| 7 | Incomplete weighted ranking competes with Thursday critique/integrity | Tuesday: baseline and weighted ranks work on the issued fixture; integrity helper already launches |

Early completion must be measured against complete evidence and individual understanding. A shared package produced quickly by one confident partner is not proof that the pair/trio needs a harder assignment.

Instructor support also has a capacity limit: four breakout rooms and nine individual explanations. Use short written/recorded checkpoints where suitable, let groups keep working while the instructor visits, and do not plan a separate lengthy oral examination for every student in every lab.

## 6. Week 8 Assessment-Time Review

### FINAL-P1: Plausible but No Task-Level Recovery Margin

The proposed 180-minute meeting contains 15 minutes briefing, 150 minutes work, and 15 minutes submission/check. Three 45-minute tasks plus 15 minutes organization exactly exhaust the work block.

That schedule assumes each task's implementation, debugging, tests, evidence, and disclosure fit inside its 45 minutes. An unfamiliar full graph implementation or a new multi-part benchmark is not a 45-minute task merely because it uses previously taught concepts.

Recommendation: calibrate core tasks around 35-40 minutes each, leaving 15-30 minutes inside the 150-minute block after the existing 15-minute organization allowance. Supply surrounding I/O and use completion/repair/transfer rather than three fresh application builds. Pilot variants and avoid hiding optional extensions in the assessed core.

### FINAL-P2: Instructor Throughput and Student Spare Time Are Different Issues

Nine sequential 20-minute oral defenses consume all 180 minutes before briefing, transitions, submission, or a delay. With 30 minutes reserved for opening/closing, the average ceiling is about 16.7 minutes per student.

A 10-15-minute targeted oral follow-up would require 90-135 instructor minutes. Students can complete independent written/adaptation work while other students are interviewed; those activities occur concurrently, not as 90-135 additional student minutes.

The current draft does not define the amount of written/adaptation work, so **student workload cannot yet be validated**. One small change and a short explanation may leave much of a three-hour meeting unused for stronger students. That is not automatically a problem in an assessment window; do not inflate the final to occupy every minute.

Before packet production, specify the common independent response/adaptation work, any oral appointment length, how waiting students progress, no-show/recovery handling, and the opening/closing reserve. Instructor preparation of personalized prompts between Tuesday/Thursday is additional staff workload, not student lab time.

## 7. Recommended Decision Before Crafting Packets

| Area | Decision Recommended |
| --- | --- |
| Week 1 | Retain approachable entry; make the core revision genuinely consequential. Add a bounded transfer/deeper case only if full-core completion remains early. |
| Week 2 | Retain scope with supplied batch tooling and compact evidence; pilot whether interpretation uses the available time. |
| Week 3 | Bound operation/state/undo contracts and comparison implementation before approving scope. |
| Week 4 | Narrow duplicate construction/reporting and bounded experiment demands; then choose the split. Do not accept 100/210 unchanged as a reliable fit. |
| Week 5 | Give AL06 more time and constrain AL07 accordingly; evaluate the proposed 130/180 split. |
| Week 6 | Bound model invention, reuse BFS parent state, and protect Thursday individual restriction time. |
| Week 7 | Retain bounded weighting/digest core with supplied helpers; exclude full-app/data-research scope. |
| Final | Add Part 1 recovery margin; define Part 2 individual task volume and oral throughput before validating the 180-minute window. |

**No across-the-board scope increase is recommended.** The earlier under-scoping problem has largely been addressed on paper; the remaining problem is distribution and interpretation of required work. Preserve deeper reasoning while removing duplicate machinery and uncontrolled feature scope.

### Pilot Evidence

For each assignment/phase, record time to first working baseline, time to passing core cases, time to complete evidence/revision, support needed, and whether each student can independently explain or adapt the result. Track elapsed group work separately from individual closing work; include the trio and students needing support.

Treat thresholds as pilot triggers, not grades or compulsory time-on-task:

- If students repeatedly finish the complete core before roughly two-thirds of its usable window and demonstrate transfer, consider a relevant bounded promotion.
- If required work repeatedly uses the entire window before individual evidence is complete, narrow redundant work or adjust the split.
- If a correct group package masks weak individual explanation, improve checkpoints rather than add features.
- If required shared work spills beyond synchronous labs, redesign that phase; do not prescribe off-class partner coordination.

The next step is instructor approval of the proposed boundaries/splits, followed by packet drafting and empirical timing checks. Until then, current assignment specifications remain proposals rather than verified workload commitments.
