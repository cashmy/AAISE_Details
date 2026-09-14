# Data Modeling: Selected Readings Draft
## Course 123 - Modern Data Modeling for Systems

**Status:** Updated Selection  
**Primary Textbook:** Data Modeling: A Beginner's Guide by Andy Oppel  
**Supplemental Text:** MongoDB Essentials: A quick introduction by The MongoDB Team  
**Version:** 0.3  
**Purpose:** Updated reading selection with MongoDB supplement integration

---

## Course 123 Alignment

Course 123 focuses on: "modern approaches to organizing, modeling, and managing data for software systems. The course emphasizes selecting appropriate data structures and storage patterns, working across relational and non-relational models, and understanding how data design affects reporting, integration, security, and scalability."

---

## Proposed Reading Selections

### **Foundation Concepts (Week 1-2)**
**Chapter 1: Introduction to Data Modeling**
- Data-centric design principles
- Anatomy of a data model
- Layers of data abstraction (conceptual, logical, physical)
- Types of data models
- Importance of data modeling (documentation, visualization, alternatives, expansion)
- Measures of a good data model (business rules enforcement, flexibility)

**Chapter 2: Relational Model Components**
- Core relational concepts (entities, attributes, relationships)
- Keys and relationship types
- Basic integrity constraints

**Chapter 3: Data and Process Modeling**
- Relationship between data and process
- How data modeling supports system design

### **ERD Design - Strong Treatment (Week 2-3)**
**Chapter 4: ERD Design and Practice**
- Entity-relationship diagram fundamentals
- ERD notation and conventions
- Creating effective ERDs
- *Practical application: Students will complete ERD assignments using draw.io or similar tool*
- translating conceptual models to visual diagrams
- ERD as communication tool for technical and non-technical stakeholders

### **Conceptual Modeling (Week 3)**
**Chapter 5: Conceptual Data Modeling**
- The conceptual modeling process
- Preparation and solution design
- What differentiates conceptual from logical modeling
- Creating the model
- Generic models and patterns
- Roles vs. subtypes
- Dealing with hierarchies, networks, and linked lists
- Bottom-up vs. top-down modeling
- Subject areas
- Evaluating the model and what makes a good conceptual model

### **Normalization - Reference/Cursory Treatment (Week 4)**
**Chapter 6: Logical Database Design Using Normalization (REFERENCE)**
- Basic normalization concepts at awareness level
- The need for normalization (insert, delete, update anomalies)
- First through Third Normal Forms overview
- *Focus on conceptual understanding rather than deep implementation*

**Chapter 7: Beyond Third Normal Form (OPTIONAL REFERENCE)**
- Brief mention of advanced normalization concepts
- Denormalization for performance efficiency
- *Critical human responsibility: AI does not automatically consider denormalization for operational efficiency*
- When and why to break normalization rules
- Human governor role for performance optimization

### **Business Rules - Summary Treatment (Week 5)**
**Chapter 9: Alternatives for Incorporating Business Rules (SUMMARY)**
- Anatomy and origin of business rules
- Business rules impact on database design
- Greenfield vs. legacy application considerations
- Business rules placement: backend vs. database design
- Functional classification of business rules
- *Emphasis on architectural decision-making for rule placement*

### **Physical Design - Modern Context (Week 5)**
**Chapter 8: Physical Database Design (CONDENSED)**
- The physical design process (modern implementation context)
- Designing tables with ORM consideration
- Naming conventions
- Integrating business rules and data integrity
- NOT NULL and primary key constraints
- *Reduce emphasis on manual implementation details*

### **Excluded - Discovered Through RBA Process**
**Chapters 10+ (Temporal Data, Analytical Modeling, Enterprise Modeling)**
- These concepts will be discovered through the RBA process
- Human-AI collaboration naturally surfaces temporal needs, analytical patterns, and enterprise boundaries
- Students will learn to identify these through iterative Sky-Bounce and Reality Contact
- Process-oriented discovery rather than separate theoretical modules

---

## Supplemental Textbook: MongoDB Essentials

**Textbook:** MongoDB Essentials: A quick introduction by The MongoDB Team  
**ISBN-13:** 978-1806706099  
**Pages:** 66  
**Purpose:** Supplemental coverage for document/NoSQL modeling and AI-ready data concepts

### **Chapter 1: MongoDB Architecture (pp 1-9)**
- Overview of MongoDB architecture (mongod, mongos, replica sets, sharding)
- Mapping MongoDB components to relational database structures
- Client libraries role (pymongo)
- **Usage:** Foundational context for Week 6 document modeling

### **Chapter 2: Getting Started with MongoDB (pp 10-14)**
- Installation and local deployment
- First database and collection creation
- **Usage:** Reference for practical MongoDB setup

### **Chapter 3: Data Modeling (pp 15-31) - PRIMARY FOR WEEK 6**
- Schema design and data modeling fundamentals in MongoDB
- Embedding vs. referencing strategies
- One-to-one, one-to-many, many-to-many relationships
- Optimization strategies and denormalization
- **Usage:** Core reading for Week 6 document modeling activities

### **Chapter 4: CRUD Operations (pp 33-37)**
- Create, Read, Update, Delete operations
- **Usage:** Reference for understanding document database operations

### **Chapter 5: Aggregation (pp 38-45)**
- Aggregation framework for complex data analysis
- Stages ($match, $group, $sort, $project)
- Operators, expressions, conditionals
- **Usage:** Context for understanding document database analytical capabilities

### **Chapter 6: Performance Strategies and Tools (pp 47-50)**
- Indexes, .explain(), profiling, stats()
- Query performance and scaling
- **Usage:** Reference for performance considerations in Week 8

### **Chapter 7: Intelligent Applications with MongoDB (pp 51-60) - SUPPLEMENT FOR WEEK 8**
- Atlas Search and Atlas Vector Search
- Lexical search, semantic search, and RAG
- **Usage:** Supplemental support for Week 8 AI-ready data concepts

---

## Selection Rationale

**Modern Relevance Focus:**
- Emphasize conceptual modeling as thinking skill (ORMs don't replace this)
- Strong ERD design treatment with practical tool application (draw.io)
- Summary treatment of business rules with architectural placement considerations
- Reference/cursory treatment of normalization (basic awareness, not deep theory)

**Human Governor Role Emphasis:**
- Denormalization for performance efficiency is critical human responsibility
- AI does not automatically consider operational efficiency optimization
- Human knowledge base required for performance decisions
- When and how to instruct AI about denormalization needs

**Industry Reality Consideration:**
- Many shops won't have high-level AI processing - students need foundational knowledge
- Basic skills essential regardless of AI availability
- Performance optimization requires human expertise and governance

**Process-Oriented Discovery:**
- Temporal data, analytical patterns, enterprise boundaries discovered through RBA process
- Human-AI collaboration naturally surfaces complex patterns through iterative Sky-Bounce
- Students learn to identify needs through Reality Contact rather than separate theoretical modules
- Process skill over comprehensive topic coverage

**Reduced Emphasis:**
- Deep normalization theory (ORFs handle much implementation, humans focus on exceptions)
- Extensive physical design details (automated by modern tools)
- Traditional implementation patterns (superseded by modern frameworks)
- Separate modules for temporal/analytical/enterprise concepts (discovered through process)

**Reduced Missing Content (Still Required):**
- API and integration patterns
- Data exchange formats (JSON, XML, etc.)
- System boundaries and data security considerations
- Performance and scalability reasoning (human governor role)

**Now Covered by MongoDB Essentials:**
- Document/NoSQL modeling approaches (Chapter 3)
- AI-ready data modeling concepts (Chapter 7 - Atlas Vector Search, RAG, semantic search)

---

## Pathway Convergence Test Notes

**Areas of Alignment with Instructor Feedback:**
- Trimmed more aggressively from original dense selection
- Chapters 6-7 treated as reference/cursory rather than core
- Chapters 9+ excluded based on RBA process discovery
- Acknowledged industry reality: not all shops have high-level AI
- Human governor role for performance optimization

**Key Revisions Based on Reality Contact:**
- Added strong ERD design treatment with practical tool application
- Added summary treatment of business rules with architectural placement considerations
- Emphasized denormalization as critical human responsibility
- Explicit human governor role for performance decisions
- Process-oriented discovery for complex patterns vs. separate modules

**Practical Skill Emphasis:**
- ERD assignments using draw.io or similar tool
- Business rules placement decisions (greenfield vs. legacy)
- Performance optimization as human knowledge domain
- Foundational skills essential regardless of AI availability

**MongoDB Supplement Integration:**
- Added MongoDB Essentials as supplemental text (ISBN: 978-1806706099)
- Chapter 3 (Data Modeling) identified as primary for Week 6 document modeling
- Chapter 7 (Intelligent Applications) provides actual AI-ready content support for Week 8
- Reduces missing content areas that would otherwise require independent development

---

**Next Steps:** Reading selections now complete with MongoDB supplement integration.