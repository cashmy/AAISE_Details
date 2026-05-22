# Textbook Coverage and Reference Map v2

## Purpose

This document maps `50 Algorithms Every Programmer Should Know`, 2nd edition,
by Imran Ahmad, to `10-152-119 Introduction to Algorithms v2`.

The textbook is intentionally broader than the course. It should function as:

- a required conceptual spine for selected foundational topics
- a guided reference for selected bridge topics
- an optional future-reference book for advanced algorithms, AI, data systems,
  and security topics

The course should not attempt full textbook coverage.

## Weekly Textbook Alignment Summary

This table is intended for instructor review and reading-plan development. It
does not mean students should read every listed section. The purpose is to show
which textbook chapters support each phase and week so that required reading can
be curated later into a manageable student workload.

| Unit / Phase | Week | Curriculum Focus | Primary Textbook Support | Secondary / Reference Support | Reading Status |
| --- | --- | --- | --- | --- | --- |
| Unit 1 - Algorithmic Foundations and Correctness | Week 1 | Algorithms, precision, assumptions, correctness, pseudocode, test cases | Ch. 1 - Overview of Algorithms | Ch. 16 - Practical Considerations, for explainability and limits of algorithmic solutions | Required from Ch. 1; guided excerpt from Ch. 16 if useful |
| Unit 1 - Algorithmic Foundations and Correctness | Week 2 | Big-O, time/space intuition, growth patterns, timing experiments, best/worst/average case | Ch. 1 - Overview of Algorithms | Ch. 15 - Large-Scale Algorithms, as future-scale reference only | Required from Ch. 1; Ch. 15 deferred/reference only |
| Unit 2 - Data Structures, Search, Sort, and Growth | Week 3 | Lists, dictionaries, sets, stacks, queues, trees, graphs, representation choices | Ch. 2 - Data Structures Used in Algorithms | Ch. 13 - Algorithmic Strategies for Data Handling, for representation/compression tradeoff reference | Required selected depth from Ch. 2; optional reference from Ch. 13 |
| Unit 2 - Data Structures, Search, Sort, and Growth | Week 4 | Linear search, binary search, sorting, preconditions, scale, library vs manual implementation | Ch. 3 - Sorting and Searching Algorithms | Ch. 4 - Designing Algorithms, for correctness/performance/scalability framing | Required selected depth from Ch. 3; guided excerpt from Ch. 4 |
| Unit 3 - Strategy Patterns and Observable Behavior | Week 5 | Recursion, iteration, brute force, divide and conquer, greedy, dynamic programming recognition | Ch. 4 - Designing Algorithms | Ch. 1 - Overview of Algorithms, for validation and explainability language | Guided from Ch. 4; revisit Ch. 1 as needed |
| Unit 3 - Strategy Patterns and Observable Behavior | Week 6 | Graphs, paths, adjacency representation, BFS, DFS, real-system modeling | Ch. 5 - Graph Algorithms | Ch. 12 - Recommendation Engines, as later graph/similarity bridge if useful | Guided with selected required elements from Ch. 5; optional reference from Ch. 12 |
| Unit 4 - AI/Data Bridges, Tradeoffs, and Explanation | Week 7 | Similarity, clustering, recommendation, hashing, data representation | Ch. 6 - Unsupervised Machine Learning Algorithms; Ch. 12 - Recommendation Engines; Ch. 14 - Cryptography | Ch. 7 - Traditional Supervised Learning Algorithms; Ch. 9 - Algorithms for Natural Language Processing; Ch. 13 - Algorithmic Strategies for Data Handling | Guided from Ch. 6 and Ch. 12; selected guided concept from Ch. 14; optional reference from Ch. 7, Ch. 9, Ch. 13 |
| Unit 4 - AI/Data Bridges, Tradeoffs, and Explanation | Week 8 | Tradeoffs, explainability, bias, assumptions, responsible AI/tool use, final synthesis and assessment | Ch. 16 - Practical Considerations | Ch. 4 - Designing Algorithms; Ch. 15 - Large-Scale Algorithms | Guided from Ch. 16; guided/review from Ch. 4; Ch. 15 reference only |

## Chapter-to-Week Quick View

| Chapter | Primary Course Use | Week(s) | Student Reading Likelihood |
| --- | --- | --- | --- |
| Ch. 1 - Overview of Algorithms | Algorithm definition, Big-O, validation, explainability | Weeks 1-2; revisit Week 5 | High |
| Ch. 2 - Data Structures Used in Algorithms | Core data structures and representation choices | Week 3 | High, selected sections |
| Ch. 3 - Sorting and Searching Algorithms | Search/sort comparison and preconditions | Week 4 | High, selected sections |
| Ch. 4 - Designing Algorithms | Strategy comparison and tradeoffs | Weeks 4-5; revisit Week 8 | Medium, guided sections |
| Ch. 5 - Graph Algorithms | Graph representation, BFS, DFS, paths | Week 6 | Medium, selected sections |
| Ch. 6 - Unsupervised Machine Learning Algorithms | Similarity, distance, clustering | Week 7 | Medium, guided sections |
| Ch. 7 - Traditional Supervised Learning Algorithms | Decision tree/classification preview | Week 7 optional | Low, optional reference |
| Ch. 8 - Neural Network Algorithms | Future AI/ML reference | Deferred | Very low / deferred |
| Ch. 9 - Algorithms for Natural Language Processing | Text-to-number representation preview | Week 7 optional | Low, optional reference |
| Ch. 10 - Understanding Sequential Models | Future AI/ML reference | Deferred | Very low / deferred |
| Ch. 11 - Advanced Sequential Modeling Algorithms | Future transformers/LLM reference | Deferred | Very low / deferred |
| Ch. 12 - Recommendation Engines | Similarity, ranking, recommendation bridge | Week 7; possible Week 6 reference | Medium, guided sections |
| Ch. 13 - Algorithmic Strategies for Data Handling | Data representation/compression tradeoffs | Week 3 or 7 optional | Low, optional reference |
| Ch. 14 - Cryptography | Hashing and integrity concepts | Week 7 | Low to medium, selected concept |
| Ch. 15 - Large-Scale Algorithms | Scale reference and future systems orientation | Week 2 or 8 reference | Low, reference only |
| Ch. 16 - Practical Considerations | Explainability, ethics, bias, limits, when to use algorithms | Weeks 1 and 8 | Medium, guided sections |

## Coverage Categories

Required:

- Core course material.
- Should be taught, practiced, and assessed.

Guided:

- Instructor-selected excerpts, examples, or simplified applications.
- May be assessed through labs, discussion, reflection, or applied examples.

Optional Reference:

- Useful for students to know exists.
- May support enrichment, projects, or future coursework.

Deferred:

- Too advanced, too broad, or belongs more clearly in later courses.
- May be named briefly for orientation, but should not be taught in depth.

## Course-to-Textbook Alignment Summary

```text
Unit 1 -> Overview of Algorithms; Big-O; validation; correctness
Unit 2 -> Data Structures; Sorting and Searching
Unit 3 -> Designing Algorithms; Graph Algorithms
Unit 4 -> Selected AI/data bridges and practical considerations
```

## Section 1: Fundamentals and Core Algorithms

Section 1 is the main course spine.

### Chapter 1 - Overview of Algorithms

Coverage: Required

Use for:

- What an algorithm is
- Algorithm design techniques
- Performance analysis
- Space and time complexity
- Best, worst, and average case
- Big-O notation
- Selecting and validating algorithms
- Exact, approximate, and randomized algorithms at a light recognition level
- Explainability

Course placement:

- Unit 1
- Week 1: Algorithms, precision, and correctness
- Week 2: Big-O and growth intuition

Notes:

- This chapter should set the vocabulary for the course.
- Big-O should be taught as applied reasoning and comparison, not as a formal
  proof unit.
- Explainability should be connected to AI-generated solutions and later
  algorithmic accountability.

### Chapter 2 - Data Structures Used in Algorithms

Coverage: Required with selected depth

Use for:

- Python built-in types
- Lists
- Dictionaries
- Sets
- Time complexity for common operations
- Stacks
- Queues
- Introductory trees
- Introductory graph-related representation

Guided or optional portions:

- Tuples as contrast, not a major assessment target
- Series and DataFrames as a light preview for analytics
- Matrices as recognition or enrichment unless needed for a lab
- Vectors as recognition for AI/data bridge language

Course placement:

- Unit 2
- Week 3: Data structures for algorithmic thinking

Notes:

- The course should emphasize data-structure choice and tradeoffs.
- Students should understand why representation affects access, lookup,
  traversal, and performance.
- Pandas/DataFrames can be previewed as a bridge to `10-152-121 Advanced Python
  Systems`, but should not take over this course.

### Chapter 3 - Sorting and Searching Algorithms

Coverage: Required with selected depth

Use for:

- Linear search
- Binary search
- Preconditions such as sorted data
- Sorting as a way to explore scale and tradeoffs
- Simple sorts such as selection, insertion, or bubble sort
- Merge sort as a divide-and-conquer contrast
- Choosing a sorting/searching algorithm

Optional/reference portions:

- Shell sort
- Interpolation search
- Full implementation of every listed sort

Course placement:

- Unit 2
- Week 4: Searching and sorting

Notes:

- Students should not memorize every sorting algorithm.
- The goal is to compare assumptions, correctness, and growth behavior.
- Students should learn when to implement an algorithm for learning and when to
  use a language/library-provided operation in practice.

### Chapter 4 - Designing Algorithms

Coverage: Guided

Use for:

- Correctness
- Performance
- Scalability
- Divide-and-conquer strategy
- Greedy strategy
- Dynamic programming as recognition or light exposure
- Brute force versus improved strategies
- Strategy comparison

Optional/reference portions:

- P, NP, NP-complete, and NP-hard as orientation only
- PageRank as reference or enrichment
- Linear programming as reference or enrichment
- Apache Spark divide-and-conquer example as future reference

Course placement:

- Unit 3
- Week 5: Recursion, iteration, and strategy patterns
- Week 8: Tradeoffs, final synthesis, and final assessment preparation

Notes:

- This chapter contains more than an introductory bridge course can absorb.
- Use it to teach students that algorithm design is about choosing strategies
  under constraints, not collecting named algorithms.

### Chapter 5 - Graph Algorithms

Coverage: Guided with selected required elements

Required elements:

- Graph vocabulary
- Nodes/vertices and edges
- Directed and undirected relationships
- Adjacency-list representation at an introductory level
- Breadth-first search
- Depth-first search
- Path and traversal intuition

Guided or optional portions:

- Centrality measures
- Social network analysis
- Fraud detection case study
- Network density and advanced graph analytics

Course placement:

- Unit 3
- Week 6: Graphs, paths, and models of real systems

Notes:

- Graphs are highly valuable for later data modeling, networks, recommendation,
  workflows, and AI systems.
- Keep the implementation modest and visual.
- A grid, map, workflow, dependency graph, or small social network can make this
  tangible.

## Section 2: Machine Learning Algorithms

Section 2 should be used selectively as an AI/data bridge, not as a full ML
unit.

### Chapter 6 - Unsupervised Machine Learning Algorithms

Coverage: Guided

Use for:

- Similarity and distance
- Euclidean distance
- Manhattan distance
- Cosine similarity as recognition or light application
- Clustering as grouping similar records
- k-means intuition
- Hierarchical clustering or DBSCAN as optional comparison

Optional/reference portions:

- Full data-mining lifecycle
- Principal component analysis
- Association rules
- Apriori and FP-growth implementation

Course placement:

- Unit 4
- Week 7: Similarity, clustering, recommendation, and hashing

Notes:

- This is one of the highest-value bridge chapters.
- Use small visual examples, such as 2D points or simple records.
- The goal is to show the algorithmic idea beneath later AI and analytics.

### Chapter 7 - Traditional Supervised Learning Algorithms

Coverage: Optional Reference with selected guided exposure

Guided exposure:

- Decision tree logic as explainable branching
- Classification versus regression vocabulary
- Confusion matrix, precision, and recall as recognition if time allows

Optional/reference portions:

- XGBoost
- Random forest
- Logistic regression
- SVM
- Naive Bayes
- Full regression modeling
- Weather prediction example

Course placement:

- Unit 4, if time allows
- Possible enrichment or capstone comparison

Notes:

- Do not turn this into a supervised machine-learning course.
- Decision trees are the best candidate for light exposure because students can
  connect them to conditionals and explainability.

### Chapter 8 - Neural Network Algorithms

Coverage: Deferred

May name briefly for:

- Awareness that later AI systems use different algorithmic structures
- Connection to future AI/ML coursework

Do not teach in depth:

- Perceptrons
- Training neural networks
- Activation functions
- Keras/TensorFlow implementation
- CNNs
- GANs
- Transfer learning

Notes:

- Too advanced for this course.
- Better suited to later machine-learning or AI-focused coursework.

### Chapter 9 - Algorithms for Natural Language Processing

Coverage: Optional Reference with one possible guided bridge

Possible guided bridge:

- Text-to-number representation
- Term-document matrix or TF-IDF at a conceptual level
- Why text must be cleaned, tokenized, and represented before algorithms can use
  it

Optional/reference portions:

- Word2Vec
- Sentiment analysis case study
- Full NLP pipeline

Course placement:

- Unit 4, if time allows
- Possible enrichment lab or instructor demonstration

Notes:

- This can be valuable for AI literacy, but should be kept lightweight.
- The key idea is representation: algorithms cannot reason about raw text until
  it is transformed.

### Chapter 10 - Understanding Sequential Models

Coverage: Deferred

Do not teach in depth:

- RNNs
- GRUs
- LSTMs
- Sequence model training

Notes:

- Better as future reference for AI/ML coursework.

### Chapter 11 - Advanced Sequential Modeling Algorithms

Coverage: Deferred

May name briefly for:

- Awareness that transformers and LLMs are later advanced topics

Do not teach in depth:

- Autoencoders
- Seq2Seq
- Attention
- Self-attention
- Transformers
- LLM internals

Notes:

- Students may be curious about LLMs, but this course should not attempt LLM
  architecture instruction.
- Explainability and evaluation are more appropriate for `119` than deep model
  mechanics.

## Section 3: Advanced Topics

Section 3 should be used as selective bridge material and future reference.

### Chapter 12 - Recommendation Engines

Coverage: Guided

Use for:

- Similarity
- Ranking
- Content-based recommendation intuition
- Collaborative filtering vocabulary as recognition
- Recommendation as an applied algorithmic decision problem

Optional/reference portions:

- Full movie recommender implementation
- Full similarity matrix workflow
- Retraining and feedback loops

Course placement:

- Unit 4
- Week 7: Similarity, clustering, recommendation, and hashing

Notes:

- This is a strong lab candidate because recommendations feel tangible.
- Keep the dataset tiny and the algorithm explainable.
- Connect to later AI/data systems without requiring ML depth.

### Chapter 13 - Algorithmic Strategies for Data Handling

Coverage: Optional Reference with selected guided concepts

Possible guided concepts:

- Data representation choices affect storage, speed, and tradeoffs
- Compression as a tradeoff example
- Huffman coding as an optional visual/tangible algorithm

Deferred:

- CAP theorem in depth
- Distributed storage theory
- AWS-focused data management
- LZ77 and advanced compression formats unless used as enrichment

Course placement:

- Unit 4 enrichment or optional lab

Notes:

- Use only if it supports the data-modeling and analytics bridge.
- Avoid distributed-systems depth.

### Chapter 14 - Cryptography

Coverage: Optional Reference with selected guided concepts

Possible guided concepts:

- Hashing for identity, lookup, integrity, and security awareness
- Why hash choice matters
- Difference between hashing and encryption at a conceptual level

Deferred:

- Full cipher design
- Symmetric encryption implementation
- Asymmetric encryption implementation
- SSL/TLS handshakes
- PKI
- Blockchain
- MITM mitigation in depth

Course placement:

- Unit 4
- Week 7: Similarity, clustering, recommendation, and hashing

Notes:

- Hashing is worth including because it connects algorithms, data structures,
  identity, integrity, and security.
- Full cryptography belongs elsewhere.

### Chapter 15 - Large-Scale Algorithms

Coverage: Deferred with light recognition

May name briefly for:

- Why scale changes algorithmic decisions
- Amdahl's law as future reference
- Cloud/distributed processing as later systems context

Do not teach in depth:

- Load balancing
- CUDA/GPU architectures
- Spark implementation
- Distributed computing
- Cloud-scale processing

Course placement:

- Week 8 reference only, if useful

Notes:

- Too broad for this course.
- The course should build scale intuition, not distributed systems expertise.

### Chapter 16 - Practical Considerations

Coverage: Guided

Use for:

- Explainability
- Ethics and algorithms
- Bias
- Traceability
- Misleading evidence
- Unfair outcomes
- When to use or not use algorithms
- Limits of algorithmic solutions

Course placement:

- Unit 4
- Week 8: Tradeoffs, explainability, final synthesis, and final assessment

Notes:

- This chapter strongly supports the final course identity.
- It should be connected to AI-generated code, data quality, representation,
  and student communication of tradeoffs.

## Suggested Reading Model

### Required Reading

- Chapter 1: selected sections on algorithms, performance, Big-O, selection,
  validation, and explainability
- Chapter 2: selected sections on Python structures, stacks, queues, trees, and
  graphs
- Chapter 3: selected sections on searching and sorting

### Guided Reading

- Chapter 4: selected sections on correctness, performance, scalability,
  divide-and-conquer, greedy, and dynamic programming
- Chapter 5: selected sections on graph basics, representation, BFS, and DFS
- Chapter 6: selected sections on similarity, clustering, and k-means intuition
- Chapter 12: selected sections on recommendation engines
- Chapter 14: selected sections on hashing
- Chapter 16: selected sections on explainability, ethics, bias, and when to use
  algorithms

### Optional Reference

- Chapter 7: decision trees and classification vocabulary
- Chapter 9: text-to-number representation and TF-IDF
- Chapter 13: compression and data-handling tradeoffs
- Chapter 15: scale and distributed-processing orientation

### Deferred

- Chapter 8: neural networks
- Chapter 10: sequential models
- Chapter 11: advanced sequential modeling, attention, transformers, and LLMs
- Advanced portions of Chapters 7, 13, 14, and 15

## Course Design Guardrails

- Do not attempt to cover all 50 algorithms.
- Do not make advanced AI model internals a primary course target.
- Do not require students to implement every classic sort or search.
- Do not make the course a web-development course.
- Do not let the textbook order automatically become the course order.
- Use the book to build durable reference habits.
- Select chapters according to bridge-program needs:
  algorithmic judgment, data structures, Big-O, AI/data foundations, and
  explainability.
