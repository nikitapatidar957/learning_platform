# Document Foundations & CRUD Query Operators

Learn flexible JSON/BSON document structures, embedding vs referencing, and query operators ($gt, $in, $regex).

---

## Relational Tables vs MongoDB BSON Documents

In relational databases, data is split across rigid tables linked by foreign keys. In MongoDB, data is stored in flexible, JSON-like BSON (Binary JSON) documents.

• RDBMS Concept ➔ MongoDB Equivalent:
  - Database ➔ Database
  - Table ➔ Collection
  - Row ➔ Document
  - Column ➔ Field
  - Primary Key (`id`) ➔ ObjectId (`_id`)
  - Table Join ➔ Embedded Documents or `$lookup`

## Essential PyMongo CRUD Queries

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['learning_platform']

# 1. Create (Insert)
db.lessons.insert_one({
    'title': 'MongoDB Queries',
    'difficulty': 'Beginner',
    'tags': ['nosql', 'database'],
    'views': 1200
})

# 2. Read with Operators ($gt, $in)
popular_lessons = list(db.lessons.find({
    'views': {'$gt': 1000},
    'difficulty': {'$in': ['Beginner', 'Intermediate']}
}, {'title': 1, 'views': 1, '_id': 0}))

# 3. Update ($set, $inc)
db.lessons.update_many(
    {'difficulty': 'Beginner'},
    {'$inc': {'views': 1}}  # Atomic increment
)
```

