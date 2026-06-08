# Week 07 Deck Source - Similarity, Ranking, and Hashing

**10-152-119 Algorithmic Problem Solving**

---

# Deck Metadata

| Field | Entry |
| --- | --- |
| Week / Lesson | Week 7 |
| Phase / Unit | Unit 4 - AI/Data Bridges, Tradeoffs, and Explanation |
| Lecture Title | Small Algorithms Under AI and Data Systems |
| Related Lab | Lab 07 - Similarity, Ranking, and Hashing |
| Related Demo | Tiny Music Recommendation by Tag Similarity |
| Estimated Live Lecture Time | 110-170 minutes, or split into two shorter sessions |
| Delivery Category Mix | Core, Optional Deepening, Instructor Reserve |

---

# Lesson Purpose

Students learn that many AI and data systems begin with small algorithmic
choices: how data is represented, how items are compared, how results are
ranked, grouped, recommended, or checked for integrity.

The goal is not to teach a full machine-learning or cryptography course. The
goal is to make one AI/data algorithm idea visible, explain the assumptions
behind it, and avoid overstating what a small result proves.

---

# Possible Two-Session Split

Week 7 draws from unsupervised learning, recommendation engines, basic
cryptography language, and recommended decision-tree reading. This can be
taught as one longer lecture with breaks, but the content is a strong candidate
for a two-session split.

## Session A - Data Representation, Similarity, and Recommendation

Recommended slides:

- 1-4: review and opening frame
- 5-11: textbook review and course boundary
- 12-24: data lifecycle, representation, similarity, ranking, clustering, and
  recommendation engines
- 25-28: limitations and risk

Session A target:

Students can explain how representation and scoring shape a small ranking or
recommendation result.

## Session B - Hashing, Security Language, Demo, and Lab Transfer

Recommended slides:

- 29-38: cryptography vocabulary, hashing, integrity, and decision-tree
  recognition
- 39-43: demo
- 44-47: lab bridge and README evidence
- 48-50: wrap-up

Session B target:

Students can connect a small visible algorithm to AI/data foundations while
explaining assumptions, limitations, and evidence.

---

# Reading Alignment

| Reading Source | Assigned / Referenced Topics | Used In This Lesson |
| --- | --- | --- |
| Textbook Ch. 6, pp. 143-149 | Unsupervised learning and data mining lifecycle | Frames AI/data workflow without turning the week into a full ML course |
| Textbook Ch. 6, pp. 143-149 | Business understanding, data understanding, data preparation, modeling, evaluation, deployment | Used as a practical workflow for small algorithm design |
| Textbook Ch. 6, pp. 143-149 | Current research trends in unsupervised learning | Recognition only |
| Textbook Ch. 12, pp. 373-383 | Recommendation engines | Core bridge to similarity, ranking, and recommendation |
| Textbook Ch. 12, pp. 373-383 | Content-based recommendation and document similarity | Core demo and lab bridge |
| Textbook Ch. 12, pp. 373-383 | Collaborative filtering and limited-sample issues | Conceptual caution |
| Textbook Ch. 12, pp. 373-383 | Hybrid recommendation, similarity matrices, reference vectors, evolving recommendations | Recognition and light conceptual treatment |
| Textbook Ch. 12, pp. 373-383 | Cold start, metadata requirements, data sparsity, and social influence | Limitations and responsible explanation |
| Textbook Ch. 14, pp. 410-418 | Basic cryptography terms and weakest-link concept | Vocabulary and security requirement framing |
| Textbook Ch. 14, pp. 410-418 | Entities, security goals, and data sensitivity | Bridges to hashing/integrity option |
| Textbook Ch. 14, pp. 410-418 | Substitution, Caesar, ROT13, cryptanalysis, transposition | Recognition and light demo context only |
| Recommended Ch. 7, pp. 212-215 | Decision-tree classification, strengths, weaknesses, and use cases | Recognition / instructor reserve |
| Course artifact | Lab 07 - Similarity, Ranking, and Hashing | Student lab target |
| Course artifact | Lab 07 Demo Notes | Music similarity demo bridge |

---

# Textbook Review

The reading shows how algorithmic thinking begins to appear inside AI, data
analytics, recommendation systems, and security contexts.

The textbook uses several advanced areas as examples. Students are not expected
to master unsupervised learning, recommendation engines, cryptography, and
decision trees in one week. Instead, they should notice a shared pattern:
systems depend on representation, comparison rules, evidence, assumptions, and
limits.

## Reading Key Ideas

- Unsupervised learning looks for patterns without labeled answers.
- The data mining lifecycle gives structure to applied data work.
- Recommendation engines rank possible suggestions using data and assumptions.
- Similarity rules make comparison possible, but they are design choices.
- Small datasets can demonstrate an idea, but they cannot prove broad truth.
- Cryptography language helps us discuss identity, secrecy, integrity, and risk.
- Hashing can support identity or integrity checks.
- Decision trees are a recognizable supervised-learning model for later study.

## Terms To Carry Forward

| Term | Plain-Language Anchor | Course Use This Week |
| --- | --- | --- |
| Unsupervised learning | Finding patterns without provided labels | Recognition-level AI/data context |
| Data mining lifecycle | Workflow for turning data into usable insight | Practical framing for small data work |
| Representation | How information is stored or described | Determines what the algorithm can compare |
| Similarity | How alike two items are under a rule | Core ranking and recommendation idea |
| Recommendation engine | System that suggests items | Lab 07 option and demo context |
| Content-based | Recommends from item features | Core beginner-friendly recommendation type |
| Collaborative filtering | Recommends from user behavior patterns | Conceptual caution and recognition |
| Hybrid recommender | Combines multiple approaches | Recognition-level system idea |
| Cold start | Not enough starting data | Limitation students should understand |
| Data sparsity | Too many missing or thin data points | Limitation students should understand |
| Cipher | Method for disguising information | Cryptography vocabulary |
| Plaintext | Original readable message | Cryptography vocabulary |
| Ciphertext | Encoded or encrypted message | Cryptography vocabulary |
| Cryptanalysis | Studying how to break or analyze ciphers | Recognition-level security idea |
| Hashing | Producing a stable fingerprint-like value | Integrity or identity checking option |
| Decision tree | Branching model based on feature tests | Recommended-reading recognition |

## What We Will Use Today

- data representation
- similarity scoring
- ranking tables
- simple recommendation logic
- assumptions and limitations
- hashing for identity or integrity
- AI-assisted critique after manual framing
- README evidence

## What We Will Revisit Later

- full machine-learning workflows
- larger datasets
- model training
- collaborative filtering at scale
- cryptography beyond simple ciphers and hashing
- decision trees and supervised learning in more depth
- security, privacy, and responsible AI/data practice

---

# Lesson Outcomes

By the end of this lesson, students should be able to:

1. Explain how data representation shapes a similarity, ranking, or
   recommendation result.
2. Create or interpret a small similarity/ranking table.
3. Identify at least two assumptions behind a small AI/data algorithm.
4. Explain one limitation or risk in a ranking, recommendation, grouping, or
   hashing result.
5. Distinguish hashing/integrity from encryption/secrecy at a beginner level.
6. Use AI as a critique partner without letting it replace evidence or
   explanation.

---

# Slide Sequence Overview

| Section | Slides | Delivery Category | Purpose |
| --- | ---: | --- | --- |
| Review and Opening Frame | 1-4 | Core | Bridge from graph modeling to AI/data algorithm visibility |
| Textbook Review | 5-11 | Core | Curate the wide reading assignment and protect against overload |
| AI/Data Lifecycle and Representation | 12-17 | Core | Ground similarity and recommendation in data preparation |
| Similarity, Ranking, and Recommendation | 18-28 | Core | Teach small recommendation logic and its limits |
| Hashing and Security Vocabulary | 29-36 | Core / Optional | Connect cryptography reading to integrity and representation |
| Decision Tree Recognition | 37-38 | Instructor Reserve | Briefly place recommended reading for later courses |
| Demo Bridge | 39-43 | Core | Demonstrate music similarity ranking and presentation-layer progression |
| Lab Bridge | 44-47 | Core | Connect demo to Lab 07 options and evidence |
| Wrap-Up | 48-50 | Core | Consolidate, assign next action, and preserve next-reading placeholder |

---

# Review and Opening Frame

## Slide 1 - Review: What Lab 06 Taught Us

**Delivery Category:** Core

**Slide Text:**

In Lab 06, representation shaped the result.

You had to decide:

- what the nodes represented
- what the edges represented
- where traversal started
- what the model included
- what the model left out

**Instructor Notes:**

Use one graph example if available. The bridge is direct: in Week 6,
representation shaped traversal. In Week 7, representation shapes similarity,
ranking, recommendation, and integrity checks.

**Transition Cue:**

This week, the model changes from connected things to comparable things.

---

## Slide 2 - Today's Question

**Delivery Category:** Core

**Slide Text:**

How can a small algorithm compare, rank, recommend, group, or verify data?

**Instructor Notes:**

This question should sound broad, but not intimidating. The lesson uses small
examples so students can inspect the behavior manually.

**Transition Cue:**

These are small ideas under many larger AI and data systems.

---

## Slide 3 - Small Algorithms Under Larger Systems

**Delivery Category:** Core

**Slide Text:**

Larger systems often rely on small algorithmic choices:

- represent the data
- compare items
- score matches
- rank results
- group similar items
- check identity or integrity

**Instructor Notes:**

Connect this to the whole course: an algorithm is structured problem solving,
not only math notation in a textbook.

**Transition Cue:**

The goal today is visibility, not magic.

---

## Slide 4 - Success Today

**Delivery Category:** Core

**Slide Text:**

Today you should be able to:

- make one AI/data idea visible
- explain the representation
- show evidence
- name assumptions
- name a limitation
- avoid overstating the result

**Instructor Notes:**

This mirrors Lab 07. Students do not need to produce a sophisticated AI system.
They need one visible, explainable bridge from algorithm to data/AI thinking.

**Transition Cue:**

Now anchor this in the assigned reading.

---

# Textbook Review

## Slide 5 - Textbook Review: Four Reading Areas

**Delivery Category:** Core

**Slide Text:**

This week's reading touches four areas:

1. unsupervised learning
2. recommendation engines
3. cryptography basics
4. decision trees as recommended context

**Instructor Notes:**

Set the boundary early. This is a wide reading week. The lecture curates the
parts that support the lab and future AI/data courses.

**Transition Cue:**

Start with unsupervised learning as pattern-finding.

---

## Slide 6 - Textbook Review: Unsupervised Learning

**Delivery Category:** Core

**Slide Text:**

Unsupervised learning looks for patterns without provided answer labels.

Examples:

- grouping similar items
- finding clusters
- detecting structure
- discovering patterns

**Instructor Notes:**

Keep this recognition-level. Students are not training ML models this week.
They are learning that pattern-finding still depends on representation and
comparison rules.

**Transition Cue:**

The reading also gives a lifecycle for data work.

---

## Slide 7 - Textbook Review: Data Mining Lifecycle

**Delivery Category:** Core

**Slide Text:**

The lifecycle:

1. business understanding
2. data understanding
3. data preparation
4. modeling
5. evaluation
6. deployment

**Instructor Notes:**

Translate "business understanding" broadly: What problem are we solving and why
does it matter? Even a small lab needs a problem frame before code.

**Transition Cue:**

This workflow is useful even when our dataset is tiny.

---

## Slide 8 - Textbook Review: Recommendation Engines

**Delivery Category:** Core

**Slide Text:**

Recommendation engines suggest options by using data.

Common types:

- content-based
- collaborative filtering
- hybrid

**Instructor Notes:**

This is the core bridge to the demo. Recommendation can be explained as
ranking possible suggestions based on a rule and available data.

**Transition Cue:**

Content-based recommendation is the most beginner-friendly path.

---

## Slide 9 - Textbook Review: Cryptography Basics

**Delivery Category:** Core

**Slide Text:**

The cryptography reading introduces:

- weakest link
- security goals
- sensitive data
- ciphers
- plaintext and ciphertext
- cryptanalysis

**Instructor Notes:**

Keep this as vocabulary and framing. The lab's hashing option connects more to
identity and integrity than to full encryption.

**Transition Cue:**

Some terms are for recognition now and deeper study later.

---

## Slide 10 - Textbook Review: Decision Trees

**Delivery Category:** Instructor Reserve

**Slide Text:**

Recommended reading introduces decision trees.

For this week:

- recognize the branching idea
- notice strengths and weaknesses
- save deeper use for later AI/data courses

**Instructor Notes:**

Use this only if time allows or if students ask. Decision trees are useful, but
they are not the center of Lab 07.

**Transition Cue:**

Now clarify what to learn deeply today.

---

## Slide 11 - What To Deeply Learn vs Recognize

**Delivery Category:** Core

**Slide Text:**

Deeply learn now:

- representation
- similarity
- ranking
- assumptions
- limitations
- visible evidence

Recognize for later:

- full ML workflows
- advanced recommendation systems
- full cryptography
- decision-tree modeling

**Instructor Notes:**

This slide reduces overload. The textbook is broader than the assignment. The
student's effort should concentrate on making a small idea explainable.

**Transition Cue:**

Start with the workflow that keeps the work grounded.

---

# AI/Data Lifecycle and Representation

## Slide 12 - Start With The Problem

**Delivery Category:** Core

**Slide Text:**

Before the algorithm:

- What are we trying to help decide?
- Who or what is being compared?
- What data is available?
- What result would be useful?

**Instructor Notes:**

Connect to the data mining lifecycle. The lab should begin with a problem
frame, not with a random formula.

**Transition Cue:**

Then inspect the data.

---

## Slide 13 - Data Understanding

**Delivery Category:** Core

**Slide Text:**

Ask:

- What items do we have?
- What features describe them?
- What is missing?
- What might be unreliable?
- What should not be collected?

**Instructor Notes:**

The final question matters. If students use people-related examples, they need
to avoid sensitive or unnecessary personal data.

**Transition Cue:**

Then prepare data into a usable representation.

---

## Slide 14 - Data Preparation

**Delivery Category:** Core

**Slide Text:**

Data preparation turns messy information into usable structure.

Examples:

- tags
- categories
- numbers
- records
- dictionaries
- tables

**Instructor Notes:**

Tie this to Python. A dictionary, list of dictionaries, set of tags, or table
is not merely code structure. It is the representation the algorithm can use.

**Transition Cue:**

Representation decides what comparison is possible.

---

## Slide 15 - Representation Shapes Results

**Delivery Category:** Core

**Slide Text:**

If the representation changes, the result may change.

Example:

- compare songs by genre
- compare songs by mood
- compare songs by tempo
- compare songs by all three

Each choice can change the ranking.

**Instructor Notes:**

This slide prepares the music demo. Ask which feature students think should
matter most, then point out that the algorithm cannot use a feature not
included in the data.

**Transition Cue:**

Now define similarity.

---

## Slide 16 - Similarity

**Delivery Category:** Core

**Slide Text:**

Similarity is a rule for deciding how alike two things are.

It may use:

- shared tags
- matching categories
- numeric distance
- text overlap
- feature weights

**Instructor Notes:**

Stress "rule." Similarity is designed. It is not automatically objective.

**Transition Cue:**

Once similarity exists, we can score.

---

## Slide 17 - Scores Need Meaning

**Delivery Category:** Core

**Slide Text:**

A score should answer:

- What does a high score mean?
- What does a low score mean?
- Are all features equal?
- What score range is possible?
- What does the score ignore?

**Instructor Notes:**

Students may produce a number and assume the number explains itself. It does
not. The README should explain what the score means.

**Transition Cue:**

Scores often lead to ranking.

---

# Similarity, Ranking, and Recommendation

## Slide 18 - Ranking

**Delivery Category:** Core

**Slide Text:**

Ranking orders items by a score or rule.

Ranking can show:

- strongest match
- weakest match
- top recommendation
- items needing review

**Instructor Notes:**

Ranking is a visible result, which makes it useful for this lab. The caution is
that a ranking can look more authoritative than it really is.

**Transition Cue:**

Recommendation is a common ranking use case.

---

## Slide 19 - Content-Based Recommendation

**Delivery Category:** Core

**Slide Text:**

Content-based recommendation uses item features.

Example:

If a user likes items with tags A and B, recommend other items with similar
tags.

**Instructor Notes:**

This is the most accessible recommendation type. It connects directly to the
demo and to the study-resource alternate success path.

**Transition Cue:**

The textbook also mentions document similarity.

---

## Slide 20 - Similarity In Unstructured Documents

**Delivery Category:** Core / Optional

**Slide Text:**

Text can be compared by features such as:

- words
- tags
- topics
- categories
- extracted terms

The representation still matters.

**Instructor Notes:**

Do not drift into NLP internals. Keep the point simple: text must be converted
into comparable features before an algorithm can compare it.

**Transition Cue:**

Collaborative filtering uses a different signal.

---

## Slide 21 - Collaborative Filtering

**Delivery Category:** Core

**Slide Text:**

Collaborative filtering uses patterns from users or behavior.

It may ask:

- What did similar users choose?
- What did people with similar histories like?
- What patterns appear across many users?

**Instructor Notes:**

Keep this conceptual. Students should understand the idea but not implement it
this week.

**Transition Cue:**

The reading warns that this approach has risks.

---

## Slide 22 - Collaborative Filtering Risks

**Delivery Category:** Core

**Slide Text:**

Risks include:

- limited sample size
- over-reliance on history
- isolated analysis
- reinforcing past patterns
- weak recommendations for new users

**Instructor Notes:**

This slide connects directly to the user's reading notes. Use plain examples:
if the system only knows one old behavior, it may keep recommending the same
kind of thing.

**Transition Cue:**

Hybrid systems combine approaches.

---

## Slide 23 - Hybrid Recommendation

**Delivery Category:** Optional Deepening

**Slide Text:**

Hybrid recommendation combines signals.

It may use:

- item features
- user history
- similarity scores
- reference vectors
- feedback over time

**Instructor Notes:**

Use this as recognition. Students do not need to build hybrid recommenders.
They should see that real systems often combine multiple weak signals.

**Transition Cue:**

The textbook names similarity matrices and reference vectors.

---

## Slide 24 - Similarity Matrix And Reference Vector

**Delivery Category:** Optional Deepening

**Slide Text:**

Two useful structures:

- similarity matrix: compares items to items
- reference vector: represents a user, target, or profile

Both make comparison visible.

**Instructor Notes:**

If students are ready, draw a tiny three-item matrix. Keep it small. The goal
is recognition and evidence, not matrix math mastery.

**Transition Cue:**

Recommendation systems evolve, but they also fail in predictable ways.

---

## Slide 25 - Recommendation Limits

**Delivery Category:** Core

**Slide Text:**

Recommendation systems have limits:

- cold start
- metadata requirements
- data sparsity
- social influence
- missing context
- biased or incomplete data

**Instructor Notes:**

This is one of the most important responsible-data slides. Connect every term
back to "what the result can and cannot claim."

**Transition Cue:**

Cold start is especially easy to understand.

---

## Slide 26 - Cold Start And Sparse Data

**Delivery Category:** Core

**Slide Text:**

Cold start:

- not enough information at the beginning

Data sparsity:

- too many blanks or thin signals

Both weaken recommendations.

**Instructor Notes:**

Use a new user with no history or a small class dataset with only a few
examples. The lesson is that the algorithm cannot invent reliable context.

**Transition Cue:**

Social influence can help and harm.

---

## Slide 27 - Social Influence Is Double-Edged

**Delivery Category:** Core / Optional

**Slide Text:**

Social influence can:

- reveal useful patterns
- amplify popularity
- hide better-fit options
- reinforce existing bias
- make recommendations feel objective

**Instructor Notes:**

Keep the tone practical. Students should learn caution without feeling that all
recommendations are bad.

**Transition Cue:**

Now connect similarity to clustering.

---

## Slide 28 - Clustering As Grouping By Closeness

**Delivery Category:** Core

**Slide Text:**

Clustering groups items by closeness or similarity.

For Lab 07, clustering can be simple:

- choose features
- compare items
- create groups
- explain why the groups make sense
- name what the grouping does not prove

**Instructor Notes:**

This supports one lab option. Keep clustering at the visible, beginner level.
No advanced clustering algorithm is required.

**Transition Cue:**

The reading also gives a security vocabulary bridge.

---

# Hashing and Security Vocabulary

## Slide 29 - Cryptography Context

**Delivery Category:** Core

**Slide Text:**

Cryptography helps discuss:

- secrecy
- identity
- integrity
- sensitive data
- risk
- trust

This week uses only a small beginner slice.

**Instructor Notes:**

Set the boundary clearly. We are not teaching applied security in depth. We are
using the reading to support vocabulary and the hashing lab option.

**Transition Cue:**

Security work begins with the weakest link.

---

## Slide 30 - Weakest Link

**Delivery Category:** Core

**Slide Text:**

A system can fail at its weakest link.

Possible weak links:

- poor data handling
- unclear security goals
- exposed sensitive data
- weak process
- misunderstood algorithm

**Instructor Notes:**

Connect this to algorithmic reasoning. A correct function does not automatically
make the whole system safe or appropriate.

**Transition Cue:**

The reading asks us to identify entities and goals.

---

## Slide 31 - Security Requirement Frame

**Delivery Category:** Core

**Slide Text:**

Before choosing a method:

1. identify the entities
2. establish security goals
3. understand data sensitivity

**Instructor Notes:**

Use this as a problem-framing slide. Who is involved? What needs protection?
What would count as failure?

**Transition Cue:**

Now define a few terms.

---

## Slide 32 - Cryptography Terms

**Delivery Category:** Core

**Slide Text:**

Terms to recognize:

- cipher
- plaintext
- ciphertext
- cipher suite
- encryption
- decryption
- cryptanalysis
- PII

**Instructor Notes:**

Define briefly and do not dwell. Students need recognition and vocabulary, not
full implementation details.

**Transition Cue:**

Simple ciphers are useful teaching examples.

---

## Slide 33 - Substitution, Caesar, and ROT13

**Delivery Category:** Optional Deepening

**Slide Text:**

Simple ciphers can show how transformation works.

Examples:

- substitution cipher
- Caesar cipher
- ROT13

These are teaching examples, not modern security.

**Instructor Notes:**

Be careful: do not let students walk away thinking ROT13 is secure. It is a
learning example for transformation and weakness.

**Transition Cue:**

Cryptanalysis studies how methods can be broken or analyzed.

---

## Slide 34 - Cryptanalysis And Transposition

**Delivery Category:** Optional Deepening

**Slide Text:**

Cryptanalysis asks how a method might be analyzed or broken.

Transposition ciphers rearrange positions rather than substituting symbols.

Both show that algorithm design includes attack thinking.

**Instructor Notes:**

Keep this short. The valuable transferable idea is that algorithms must be
tested against how they can fail, not only how they work.

**Transition Cue:**

For the lab, hashing is the most practical security-adjacent option.

---

## Slide 35 - Hashing

**Delivery Category:** Core

**Slide Text:**

Hashing produces a stable value from input data.

Useful for:

- identity checks
- integrity checks
- lookup support
- change detection

**Instructor Notes:**

Use the phrase "fingerprint-like value" if helpful, but clarify that it is an
analogy. The important point is that a small input change produces a different
hash.

**Transition Cue:**

Hashing is not the same as encryption.

---

## Slide 36 - Hashing vs Encryption

**Delivery Category:** Core

**Slide Text:**

Hashing:

- one-way check value
- useful for identity or integrity

Encryption:

- protects readable content
- should be decryptable by authorized parties

Do not treat them as the same.

**Instructor Notes:**

This distinction protects beginners from a common misunderstanding. The lab
hashing option can show whether content changed; it does not explain whether
the change is meaningful.

**Transition Cue:**

The recommended reading adds one more AI/data model to recognize.

---

# Decision Tree Recognition

## Slide 37 - Decision Tree Recognition

**Delivery Category:** Instructor Reserve

**Slide Text:**

A decision tree uses branching questions.

Example shape:

- Is the feature present?
- Is the value above a threshold?
- Which branch applies?
- What class or decision results?

**Instructor Notes:**

This is recommended-reading recognition only. It can connect back to earlier
if/elif logic, but do not make it a new lab requirement.

**Transition Cue:**

Decision trees have strengths and weaknesses.

---

## Slide 38 - Decision Tree Strengths And Weaknesses

**Delivery Category:** Instructor Reserve

**Slide Text:**

Strengths:

- explainable structure
- visible decision path
- useful for classification

Weaknesses:

- can overfit
- depends on selected features
- can become brittle

**Instructor Notes:**

Use cases from the reading can be named quickly: mortgage applications,
customer segmentation, medical diagnosis, treatment effectiveness, and feature
selection. Keep this brief.

**Transition Cue:**

Now move from reading concepts to the instructor demo.

---

# Demo Bridge

## Slide 39 - Demo Scenario

**Delivery Category:** Core

**Slide Text:**

Demo: tiny music recommendation.

We will use:

- a reference song
- candidate songs
- simple tags
- tag-overlap similarity
- ranked recommendations

**Instructor Notes:**

Use the existing Lab 07 demo. The demo is intentionally different from the
withheld hashing success solution and the student lab options can use other
datasets.

**Transition Cue:**

First inspect the representation.

---

## Slide 40 - Demo Evidence

**Delivery Category:** Core

**Slide Text:**

The demo produces:

- item-feature table
- reference song summary
- similarity score table
- ranked recommendation
- assumption and limitation notes

**Instructor Notes:**

Emphasize that the ranking table is evidence, not proof of musical quality.
Students should see exactly how the score was produced.

**Transition Cue:**

Ask what changes if the representation changes.

---

## Slide 41 - Demo Key Questions

**Delivery Category:** Core

**Slide Text:**

Ask during the demo:

- Which tags are being compared?
- What does the score mean?
- Which feature is missing?
- Why did the top item win?
- What should the result not claim?

**Instructor Notes:**

These questions prepare students for their reflection and README. Keep the
discussion grounded in the printed evidence.

**Transition Cue:**

The optional presentation layer can make evidence easier to inspect.

---

## Slide 42 - Presentation Layer Progression

**Delivery Category:** Optional Deepening

**Slide Text:**

Same logic, different presentation:

1. plain tables
2. ANSI color
3. Rich tables and panels

The algorithm should not change.

**Instructor Notes:**

Use this if demonstrating the optional Rich version. The teaching point is
quality console evidence and UI/UX judgment, not decorative output.

Ask: Does the formatting clarify the evidence, or is it unnecessary polish?

**Transition Cue:**

Now state the explanation pattern students should imitate.

---

## Slide 43 - Demo Explanation Pattern

**Delivery Category:** Core

**Slide Text:**

Example explanation:

> The top recommendation ranked highest because it shared the most tags with
> the reference song. This result depends on the tags I chose, and it does not
> prove the listener would actually prefer the song.

**Instructor Notes:**

This is the Week 7 explanation pattern: result, reason, assumption, limitation.
Students can adapt the pattern to hashing, clustering, or recommendation.

**Transition Cue:**

Now transfer this to Lab 07.

---

# Lab Bridge

## Slide 44 - From Demo To Lab

**Delivery Category:** Core

**Slide Text:**

In Lab 07, choose or receive one option:

1. similarity ranking
2. simple clustering
3. tiny recommendation
4. hashing demonstration

**Instructor Notes:**

Remind students that the lab does not require a full AI system. It requires one
small algorithmic idea made visible and explained.

**Transition Cue:**

Every option needs visible evidence.

---

## Slide 45 - Lab 07 Evidence

**Delivery Category:** Core

**Slide Text:**

Your evidence may include:

- similarity matrix
- ranking table
- cluster grouping table
- scatter plot
- hash comparison
- representation table

**Instructor Notes:**

Students should choose evidence that fits their option. A screenshot alone is
not enough unless it clearly shows the algorithm behavior and is explained.

**Transition Cue:**

The README ties the evidence to explanation.

---

## Slide 46 - README Evidence

**Delivery Category:** Core

**Slide Text:**

Your README should include:

- selected option
- data set
- representation explanation
- visible evidence
- two assumptions
- one limitation or risk
- AI/data connection
- AI-use note, if applicable

**Instructor Notes:**

This is a submission-quality checklist. The README should make grading easier
and help students practice professional technical explanation.

**Transition Cue:**

Now clarify the AI-use boundary.

---

## Slide 47 - AI Use In Lab 07

**Delivery Category:** Core

**Slide Text:**

Manual first:

- select the data
- define representation
- choose the algorithm idea
- create first evidence

AI-assisted after:

- critique assumptions
- suggest missing features
- explain a misleading result
- review limitations

**Instructor Notes:**

This is a strong Week 7 boundary. AI can be a comparison partner after the
student has a framed problem and initial evidence. If AI generates code or an
alternate method, students must validate it against their own evidence.

**Transition Cue:**

Close with the main lesson.

---

# Wrap-Up

## Slide 48 - What To Carry Forward

**Delivery Category:** Core

**Slide Text:**

Carry forward:

- representation shapes results
- similarity is a design choice
- rankings need explanation
- small data has limits
- hashing can support integrity
- evidence must be visible

**Instructor Notes:**

This is the Week 7 takeaway. Connect it to future AI, analytics, and data
modeling courses.

**Transition Cue:**

Now make the immediate lab action concrete.

---

## Slide 49 - Lab 07 Success Check

**Delivery Category:** Core

**Slide Text:**

Successful Lab 07 work:

- uses at least 6 items
- explains representation
- implements or simulates one idea
- shows visible evidence
- names assumptions
- names a limitation or risk
- connects to AI/data foundations

**Instructor Notes:**

Students should compare this slide directly to their submission before turning
it in.

**Transition Cue:**

Prepare students for the next reading once Week 8 reading details are assigned.

---

## Slide 50 - How To Use The Textbook For Next Week's Reading

**Delivery Category:** Core

**Slide Text:**

Next week is final synthesis.

As you read Chapter 16:

- focus on practical considerations
- notice explainability, bias, privacy, and evidence quality
- do not try to implement every advanced idea
- connect the reading to how you explain your final solutions
- watch for ideas that could strengthen your README or Part 2 explanation

**Instructor Notes:**

Use this slide to prepare students for the final-week shift. Chapter 16 is not
a new implementation assignment; it provides language for explaining,
defending, and responsibly evaluating algorithmic work.

Mention that selected Chapter 16 ideas may support instructor-option bonus
credit if students clearly apply them to their final work.

---

# Image Prompt Notes

| Slide | Visual Need | Prompt / Direction | Cautions |
| --- | --- | --- | --- |
| 3 | Small algorithms under larger systems | Layered visual showing simple table, scoring rule, ranking output, and larger AI/data system around it | Avoid robot imagery or magical AI visuals |
| 7 | Data mining lifecycle | Clean circular or stepped workflow with six lifecycle phases | Keep text readable; avoid corporate stock look |
| 15 | Representation shapes result | Same set of songs ranked differently by genre, mood, and tempo | Keep the example visibly small |
| 18 | Ranking | Simple ordered list with scores and a note that the score rule is visible | Avoid implying the top item is objectively best |
| 24 | Similarity matrix/reference vector | Tiny matrix beside a profile vector with highlighted comparisons | Keep math light and readable |
| 25 | Recommendation limits | Recommendation list with warning callouts: cold start, sparse data, missing context | Avoid alarmist security-style imagery |
| 35 | Hashing | Text record producing a hash value, then a changed record producing a different hash | Do not imply hashing encrypts content |
| 42 | Presentation progression | Three console screenshots/styles: plain, ANSI, Rich | Use as optional visual support only |
| 45 | Lab evidence choices | Four mini-panels: ranking table, cluster table, hash comparison, representation table | Keep visual simple and student-facing |

---

# Instructor Timing Notes

| Section | Target Time | Can Shorten By | Can Expand By |
| --- | ---: | --- | --- |
| Review and Opening Frame | 10 min | Use Slides 2-4 only | Discuss one Lab 06 graph model and limitation |
| Textbook Review | 18 min | Use Slide 11 as effort filter | Add examples from each assigned reading area |
| AI/Data Lifecycle and Representation | 25 min | Combine Slides 12-14 | Have students propose features for a recommendation |
| Similarity, Ranking, and Recommendation | 35 min | Skip Slides 23-24 and 27 if needed | Build a tiny similarity matrix live |
| Hashing and Security Vocabulary | 25 min | Focus on Slides 35-36 only | Demonstrate one text change and hash mismatch |
| Decision Tree Recognition | 5 min | Skip completely if needed | Draw one tiny decision tree |
| Demo | 25 min | Run only ANSI demo | Compare plain/ANSI/Rich presentation layers |
| Lab Bridge | 12 min | Combine Slides 44-47 | Review README expectations line by line |
| Wrap-Up | 8 min | Use Slide 49 only | Ask students to state one assumption for their option |

---

# Post-Lecture Notes

Use after delivery to record what worked, what needs adjustment, and what
should change in the next course run.

## Worked Well

-

## Needs Adjustment

-

## Student Confusion Points

-

## Future Revision Notes

-
