# Indexing Strategies & Aggregation Pipelines

Master single/compound/text indexes, index selectivity, and analytical multi-stage aggregation pipelines ($match, $group, $sort).

---

## MongoDB Indexing Strategies

Without indexes, MongoDB performs a Collection Scan (`COLLSCAN`), inspecting every single document in the collection to satisfy a query.

• Single Field Index: `db.users.create_index([('email', 1)], unique=True)`
• Compound Index: `db.progress.create_index([('user_id', 1), ('lesson_id', 1)])` (Rule: Equality, Sort, Range - ESR rule)
• Text Search Index: `db.lessons.create_index([('title', 'text'), ('description', 'text')])`
• Explain Plan: Use `db.collection.find().explain('executionStats')` to verify that `totalDocsExamined` equals `nReturned` (Index Scan `IXSCAN`).

## Analytical Aggregation Pipeline

```python
# Pipeline: Filter completed lessons -> Group by subject -> Calculate stats
pipeline = [
    # Stage 1: Match only completed items
    {'$match': {'status': 'completed'}},
    # Stage 2: Group by subject and count completions
    {'$group': {
        '_id': '$subject_slug',
        'total_completions': {'$sum': 1},
        'avg_score': {'$avg': '$progress_percentage'}
    }},
    # Stage 3: Sort descending by completions
    {'$sort': {'total_completions': -1}},
    # Stage 4: Limit to top 5
    {'$limit': 5}
]
results = list(db.progress.aggregate(pipeline))
```

