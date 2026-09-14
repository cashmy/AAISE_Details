# Contents TOC & Chapter summary

1. MongoDB Architecture, pp 1-9

- Overview of MongoDB architecture, including components like mongod, mongos, replica sets and sharding.
- Brief mapping of MongoDB components (collections, documents, fields) to an equivalent relational database structure.
- Brief mention of Client libraries and their role in interacting with MongoDB. (i.e. pymongo)

2. Getting Started with MongoDB, pp 10-14

- Covers how to install the required tools, create a local deployment, and the first database and collection

3. Data Modeling, pp 15-31

- Covers the fundamentals of schema design and data modeling in MongoDB
- Covers embedding vs. referencing. Shows how to accomplish one-to-one, one-to-many and many-to-many relationships.
- Briefly mentions optimization strategies and denormalization

4. CRUD Operations, pp 33-37

- shows how to interact with the database using Create, Read, Update, and Delete operations.

5. Aggregation, pp 38-45

- show how to the aggregation framework to perform complex data analysis efficiently
- Introduces (very briefly):
  - stages (e.g. $match, $group, $sort, $project, )
  - operators (e.g. $gt, $lt, $eq, $ne)
  - expressions (e.g. $sum, $avg, $push, $addToSet)
  - conditionals (e.g. $cond, $ifNull, $switch)
  - path expressions (e.g. $field, $arrayElemAt)
  - systems variables (e.g. $$NOW, $$ROOT, $$CURRENT)
  - array operators (e.g. $lookup, $unwind )

6. Performance Strategies and Tools, pp 47-50

- Explains the tools available to ensure that the queries run fast and scale well. (indexes, .explain(), profiling, stats())

7. Intelligent Applications with MongoDB, pp 51-60

- Covers the MongoDB tools that support development of AI-based applications: Atlas Search and Atlas Vector Search.
- Lexical search, semantic search, and RAG
