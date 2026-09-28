SQL (Structured Query Language) is a standard programming language used to **store, retrieve, manage, and manipulate data in relational databases**.

Databases such as MySQL, PostgreSQL, Microsoft SQL Server, and Oracle Database use SQL.

### Common SQL Operations

**1. Retrieve data (`SELECT`)**

```sql
SELECT name, age
FROM employees;
```

This returns the `name` and `age` columns from the `employees` table.

**2. Insert data (`INSERT`)**

```sql
INSERT INTO employees (name, age)
VALUES ('Alice', 30);
```

**3. Update data (`UPDATE`)**

```sql
UPDATE employees
SET age = 31
WHERE name = 'Alice';
```

**4. Delete data (`DELETE`)**

```sql
DELETE FROM employees
WHERE name = 'Alice';
```

### Example Table

| id | name  | age |
| -- | ----- | --- |
| 1  | Alice | 30  |
| 2  | Bob   | 25  |

Query:

```sql
SELECT * FROM employees;
```

Result:

| id | name  | age |
| -- | ----- | --- |
| 1  | Alice | 30  |
| 2  | Bob   | 25  |

### Why SQL Is Important

* Organizes large amounts of data efficiently.
* Enables fast searching and reporting.
* Used in websites, business applications, banking systems, e-commerce, and analytics.
* One of the most widely used skills in software development, data analysis, and data science.

In simple terms, **SQL is the language you use to communicate with a database and ask it questions about your data.**
For a Google interview, it is important to understand **why databases evolved**, not just memorize the names. Interviewers may ask:

> "What problems did relational databases solve?"
>
> "Why wasn't file storage enough?"
>
> "Explain hierarchical and network databases."
>
> "What is data independence?"

Let's go step by step.

# 1. Paper-Based Systems

Before computers, all information was stored physically.

### Example: Bank

A bank maintains:

| Account No | Name   | Balance |
| ---------- | ------ | ------- |
| 1001       | Nikita | 50,000  |
| 1002       | Rahul  | 75,000  |

This data exists in physical ledgers.

When a customer visits:

1. Clerk finds the ledger.
2. Searches page by page.
3. Updates balance manually.
4. Stores ledger back.

### Problems

#### Search Cost

Finding one customer among 100,000 customers:

```text
Shelf
 ├── Ledger 1
 ├── Ledger 2
 ├── Ledger 3
 ...
```

Could take minutes or hours.

#### No Concurrent Access

Only one person can write in the same ledger at a time.

#### Human Errors

* Wrong calculations
* Missing entries
* Lost pages

#### Reporting

Question:

> How many customers have balances above ₹50,000?

Employees must manually inspect records.

---

# 2. Flat File Systems

When computers arrived, organizations started storing records in files.

Example:

```text
101,Nikita,IT,50000
102,Rahul,HR,60000
103,Aman,IT,70000
```

Stored inside:

```text
employee.txt
```

---

## How Retrieval Worked

Suppose we need employee 103.

Program:

```python
for each line:
    read line
    check employee id
```

Internally:

```text
Read Record 1
Read Record 2
Read Record 3
Found
```

This is called:

**Sequential Access**

Time Complexity:

```text
O(n)
```

---

## Multiple Files Problem

Company maintains:

### employee.txt

```text
101,Nikita,IT
102,Rahul,HR
```

### salary.txt

```text
101,50000
102,60000
```

### attendance.txt

```text
101,25
102,22
```

To answer:

> What is Nikita's salary?

Programmer must:

1. Open employee file
2. Find employee
3. Extract ID
4. Open salary file
5. Find matching ID

This became extremely complex.

---

## Data Redundancy

Sometimes same information appears repeatedly.

### employee.txt

```text
101,Nikita,IT
```

### payroll.txt

```text
101,Nikita,50000
```

If Nikita changes name:

```text
Nikita Patidar
```

Need updates everywhere.

Otherwise:

```text
employee.txt → Nikita Patidar
payroll.txt → Nikita
```

Data becomes inconsistent.

---

# 3. Hierarchical Databases

1960s.

Best example:

IBM Information Management System

Data stored as a tree.

---

## Structure

```text
Company
|
+-- Department
    |
    +-- Employee
```

Example:

```text
Company
|
+-- IT
|   |
|   +-- Nikita
|   +-- Rahul
|
+-- HR
    |
    +-- Aman
```

Every child has exactly one parent.

---

## Storage Internals

Records connected using pointers.

```text
Department Record
       |
       v
Employee Record
       |
       v
Employee Record
```

Instead of tables:

```text
Pointer --> Pointer --> Pointer
```

---

## Query Example

Find Nikita.

Database performs:

```text
Company
   ↓
Department
   ↓
Employee
```

Must traverse the tree.

Cannot directly jump.

---

## Strength

Very fast when relationships naturally form a tree.

Example:

```text
Country
 → State
   → City
```

Perfect hierarchy.

---

## Major Weakness

Suppose:

Employee works in:

```text
IT
HR
```

Tree becomes impossible.

Because child can only have:

```text
ONE parent
```

Not two.

---

# 4. Network Databases

Created to solve hierarchical limitations.

Popular systems:

* Integrated Data Store
* IDMS

---

## Structure

Instead of tree:

```text
Department ---- Employee
      \         /
       \       /
        Project
```

This becomes a graph.

---

## Example

Employee:

```text
Nikita
```

Works in:

```text
IT
HR
```

And:

```text
Project A
Project B
```

Representation:

```text
 IT
  \
   Nikita
  /
 HR

Nikita
 /   \
A     B
```

Now multiple parents possible.

---

## How Query Worked

Programmer navigates manually.

Pseudo-code:

```text
Find Department
Move to Employee
Move to Project
Read Record
```

This is called:

**Navigational Access**

You tell database exactly how to travel.

---

## Problem

Complex code.

Example query:

> Find all employees working on Project A

Programmer must know:

```text
Project Record
      ↓
Employee Pointer
      ↓
Employee Pointer
      ↓
Employee Pointer
```

Database doesn't figure it out.

Programmer does.

---

# Biggest Problem Before SQL

The application knew:

1. Where data was stored
2. How data was connected
3. How to navigate

Meaning:

```text
Application Logic
       +
Data Structure
```

Were tightly coupled.

Changing database structure required changing application code.

---

# Relational Databases (SQL Era)

In 1970, Edgar F. Codd proposed the relational model.

Instead of:

```text
Pointers
Trees
Graphs
```

Use:

```text
Rows
Columns
Tables
```

---

## Example

Employee

| EmpID | Name   |
| ----- | ------ |
| 101   | Nikita |
| 102   | Rahul  |

Department

| EmpID | Dept |
| ----- | ---- |
| 101   | IT   |
| 102   | HR   |

---

Now ask:

```sql
SELECT *
FROM Employee
WHERE EmpID = 101;
```

You specify:

### WHAT

not

### HOW

Database decides:

* Index usage
* Search strategy
* Memory management
* Disk access

This is called:

### Declarative Querying

and it is one of the most important concepts in database history.

---

# Interview-Level Comparison

| Feature           | Flat File   | Hierarchical | Network        | Relational(SQL)  |
| ----------------- | ----------- | ------------ | -------------- | ---------------- |
| Structure         | Files       | Tree         | Graph          | Tables           |
| Relationships     | Manual      | One-to-many  | Many-to-many   | Any relationship |
| Query Language    | Custom Code | Navigation   | Navigation     | SQL              |
| Data Redundancy   | High        | Medium       | Medium         | Low              |
| Maintenance       | Difficult   | Difficult    | Very Difficult | Easier           |
| Data Independence | No          | Limited      | Limited        | Strong           |
| Ad-hoc Queries    | Poor        | Poor         | Poor           | Excellent        |
| Scalability       | Low         | Medium       | Medium         | High             |

### Key Google Interview Takeaway

The most important evolution was:

**Paper → Flat Files → Hierarchical DB → Network DB → Relational DB (SQL)**

And the fundamental reason SQL won was:

> It separated *what data you want* from *how the database retrieves it*, providing data independence, reduced redundancy, easier querying, and better scalability.
In databases, **consistency** and **inconsistency** refer to whether the same piece of data has the same value everywhere it appears.

## Consistent Data

Data is **consistent** when all copies of the data match each other.

### Example

**employee.txt**

```text
101,Nikita Patidar,IT
```

**payroll.txt**

```text
101,Nikita Patidar,50000
```

Both files contain the same employee name.

✅ Consistent

---

## Inconsistent Data

Data is **inconsistent** when different copies of the same data have different values.

### Example

**employee.txt**

```text
101,Nikita Patidar,IT
```

**payroll.txt**

```text
101,Nikita,50000
```

The same employee has two different names.

❌ Inconsistent

---

## Real-Life Example

Suppose you change your address.

### Bank System

**Customer Table**

```text
Nikita, Bhopal
```

**Loan Table**

```text
Nikita, Indore
```

Now the bank doesn't know which address is correct.

This is called **data inconsistency**.

---

## Why It Happened Before SQL

In file-based systems, the same information was often stored in multiple files:

```text
employee.txt
payroll.txt
attendance.txt
insurance.txt
```

If a name changed, programmers had to update every file manually.

Missing even one update created inconsistency.

---

## SQL Solution

In a relational database, employee information is usually stored once:

### Employees

| EmpID | Name           |
| ----- | -------------- |
| 101   | Nikita Patidar |

### Payroll

| EmpID | Salary |
| ----- | ------ |
| 101   | 50000  |

Both tables use `EmpID = 101`.

If the name changes:

```sql
UPDATE Employees
SET Name = 'Nikita P.'
WHERE EmpID = 101;
```

The name is updated in one place only.

This greatly reduces inconsistency.

---

### Interview Definition

**Consistency:** The same data has the same value across all locations where it is referenced.

**Inconsistency:** Different copies of the same data contain conflicting values, leading to ambiguity and incorrect results.
This is exactly the level where Google, Meta, Amazon, and database-system interviews start becoming interesting.

Most people know:

```sql
SELECT * FROM employees WHERE emp_id = 101;
```

Very few understand what happens inside the database engine.

---

# First Important Clarification

Many beginners think:

```text
My Laptop
   ↓
Internet
   ↓
Database Server
```

always exists.

Not true.

You can install MySQL locally.

In that case:

```text
My SQL Client
      ↓
MySQL Process
      ↓
Local Disk
```

Everything runs on your machine.

The architecture is almost identical.

The only difference is:

```text
Network Communication = No
```

instead of

```text
Client ----TCP/IP---- Database Server
```

The SQL engine, optimizer, parser, storage engine all still exist.

---

# Internally MySQL Is Just A Process

When you start MySQL:

```bash
mysqld
```

OS creates a process.

Think:

```text
Operating System
    |
    +-- Chrome
    |
    +-- VS Code
    |
    +-- MySQL
```

MySQL gets:

* CPU
* RAM
* File Handles
* Threads

just like any other application.

---

# Component 1: SQL Parser

Suppose query arrives:

```sql
SELECT name
FROM employees
WHERE emp_id = 101;
```

Database cannot execute text.

It must convert text into structures.

---

## Lexical Analysis (Tokenizer)

First step:

```text
SELECT
name
FROM
employees
WHERE
emp_id
=
101
```

becomes tokens:

```text
KEYWORD(SELECT)

IDENTIFIER(name)

KEYWORD(FROM)

IDENTIFIER(employees)

KEYWORD(WHERE)

IDENTIFIER(emp_id)

OPERATOR(=)

NUMBER(101)
```

Similar to compiler design.

---

## Syntax Tree Generation

Parser builds:

```text
SELECT
 ├── COLUMN(name)
 ├── TABLE(employees)
 └── CONDITION
      ├── emp_id
      └── 101
```

This is called:

```text
Abstract Syntax Tree (AST)
```

Google interviewers love AST questions.

---

# Component 2: Semantic Analyzer

Parser only checks grammar.

Semantic Analyzer checks meaning.

---

Example:

```sql
SELECT salary
FROM employees;
```

Suppose salary column doesn't exist.

Parser says:

```text
Syntax Valid
```

Semantic Analyzer says:

```text
Column Not Found
```

---

Internally database searches system catalogs.

Think:

```text
metadata tables

employees
---------
emp_id
name
department
```

Database verifies requested columns.

---

# Component 3: Query Optimizer

This is the heart of modern databases.

Most database interview questions revolve around this.

---

# Why Optimizer Exists

Suppose table:

```text
employees

10 million rows
```

Query:

```sql
SELECT *
FROM employees
WHERE emp_id = 101;
```

Database can execute in many ways.

---

# Plan 1: Full Table Scan

```text
Row1
Row2
Row3
...
Row10,000,000
```

Read every row.

Cost:

```text
10 million comparisons
```

---

# Plan 2: Use Index

Suppose index exists.

```text
101 → page 14
102 → page 18
103 → page 25
```

Jump directly.

Cost:

```text
~20 operations
```

Much faster.

---

Optimizer chooses lowest cost plan.

---

# How Optimizer Thinks

Optimizer is basically a cost estimation machine.

It asks:

### How many rows exist?

Example:

```text
10 million rows
```

---

### How many rows match?

Suppose:

```sql
WHERE gender='M'
```

and table has:

```text
50% male
50% female
```

Then:

```text
5 million rows expected
```

---

### Is Index Useful?

Suppose:

```sql
WHERE gender='M'
```

Index exists.

Still optimizer may ignore it.

Why?

Because:

```text
50% table must be read anyway
```

Reading entire table may be cheaper.

---

This surprises many developers.

Index existing does NOT mean optimizer uses it.

---

# Statistics

Optimizer depends heavily on statistics.

Database stores:

```text
Row count

Distinct values

Value distribution

Null counts

Index cardinality
```

Example:

```text
country

India
India
India
India
USA
UK
```

Statistics may say:

```text
Distinct values = 3
```

---

# Cardinality

Interview favorite.

Definition:

```text
Number of distinct values
```

Example:

```text
Gender

M
F
```

Cardinality:

```text
2
```

Poor index candidate.

---

Example:

```text
Employee ID

1
2
3
4
...
10 million
```

Cardinality:

```text
10 million
```

Excellent index candidate.

---

# Cost-Based Optimization

Modern databases estimate:

```text
CPU Cost
+
Memory Cost
+
Disk Cost
```

and choose cheapest plan.

---

# Join Optimization

Google frequently asks this.

Suppose:

```sql
SELECT *
FROM employees e
JOIN departments d
ON e.dept_id = d.id;
```

How should join happen?

Many possibilities.

---

## Nested Loop Join

```text
Employee1 → search department

Employee2 → search department

Employee3 → search department
```

Simple.

---

## Hash Join

Build hash table:

```text
DepartmentID
   ↓
Department Row
```

Then lookup quickly.

---

## Merge Join

Sort both tables.

Walk simultaneously.

```text
Table A
Table B
```

Very efficient.

---

Optimizer decides.

Developer doesn't.

---

# Component 4: Execution Engine

After plan selection:

```text
Use Index
Perform Hash Join
Apply Filter
Return Rows
```

Execution engine follows the plan.

Think:

```text
Plan
 ↓
Execution
```

---

# Component 5: Storage Engine

SQL Engine doesn't know disk details.

Storage Engine does.

In MySQL:

Most common:

InnoDB

---

Responsibilities:

### Read Data

```text
Disk → Memory
```

### Write Data

```text
Memory → Disk
```

### Transactions

```sql
BEGIN;
UPDATE ...
COMMIT;
```

### Locking

Prevent conflicts.

### Index Management

Maintain B+ Trees.

---

# Internal Data Structure: B+ Tree

Google loves this.

Indexes are NOT hash maps.

Usually:

```text
B+ Trees
```

---

Imagine:

```text
          50
       /      \
    20         80
   /  \       /  \
10 30    70  90
```

Large version stored on disk.

---

Searching:

```sql
WHERE emp_id = 70
```

Path:

```text
50
 ↓
80
 ↓
70
```

Only few reads.

---

Without index:

```text
1
2
3
4
...
10 million
```

Need scanning.

---

# Why B+ Tree?

Disk access is expensive.

Suppose:

```text
RAM Access
≈ nanoseconds

Disk Access
≈ milliseconds
```

Disk is millions of times slower.

B+ Tree minimizes disk reads.

---

# Buffer Pool

Most important performance feature.

Storage engine keeps:

```text
Frequently used pages
```

in RAM.

```text
Disk
 ↓
Buffer Pool
```

---

First query:

```sql
SELECT * FROM employees WHERE emp_id=101;
```

May read disk.

Second query:

```sql
SELECT * FROM employees WHERE emp_id=101;
```

May come directly from memory.

Huge speedup.

---

# What Interviewers Usually Ask

### Why is index fast?

Answer:

```text
Because B+ Tree reduces search from O(n)
to roughly O(log n) and minimizes disk I/O.
```

---

### Why optimizer sometimes ignores index?

Answer:

```text
Because estimated cost of index lookup
can be higher than full table scan.
```

---

### Why statistics matter?

Answer:

```text
Optimizer uses statistics to estimate
row counts and choose execution plans.
```

---

### What is cardinality?

Answer:

```text
Number of distinct values in a column.
Higher cardinality usually means better indexing.
```

---

### What is the most expensive operation in databases?

For large systems:

```text
Disk I/O
```

not CPU.

That's why database design focuses heavily on:

* Indexes
* Buffer pools
* Query optimization
* Reducing page reads

These topics (Optimizer, B+ Trees, Indexes, Cardinality, Statistics, Join Algorithms, Buffer Pool, Disk I/O) are the database internals most likely to appear in a Google-level systems or backend interview.


For an experienced Google interview, you need to go much deeper than:

> "Optimizer chooses the best query plan."

The interviewer will expect you to understand **how the optimizer thinks**, **how indexes work internally**, **why an index is or isn't used**, **cardinality**, **statistics**, **join order selection**, **cost estimation**, and **tradeoffs**.

---

# What Is Query Optimization?

When you write:

```sql
SELECT *
FROM employees
WHERE emp_id = 1001;
```

you are only describing:

```text
WHAT you want
```

The optimizer decides:

```text
HOW to get it
```

This is the core idea of relational databases.

---

## Analogy

Suppose you're in Bhopal and want to go to Delhi.

Possible routes:

```text
Road
Train
Flight
```

All reach Delhi.

But each has different cost.

The optimizer behaves similarly.

---

For:

```sql
SELECT *
FROM employees
WHERE emp_id = 1001;
```

Possible plans:

### Plan A

```text
Scan entire table
```

### Plan B

```text
Use primary key index
```

### Plan C

```text
Use secondary index
```

Optimizer evaluates all plans and picks the cheapest.

---

# What Does "Cost" Mean?

Many developers think:

```text
Cost = Time
```

Not exactly.

Databases estimate:

```text
Cost =
Disk I/O
+
CPU
+
Memory
+
Network
```

Disk I/O is usually the dominant factor.

---

# Why Disk I/O Dominates

Approximate access times:

| Resource  | Time           |
| --------- | -------------- |
| CPU Cache | ~1 ns          |
| RAM       | ~100 ns        |
| SSD       | ~100,000 ns    |
| HDD       | millions of ns |

Reading from disk can be thousands to millions of times slower than memory.

Therefore:

```text
Optimizer's primary goal:
Minimize disk reads
```

---

# Statistics: Optimizer's Brain

Optimizer does not inspect all rows.

That would defeat the purpose.

Instead it relies on statistics.

Example table:

| id | country |
| -- | ------- |
| 1  | India   |
| 2  | India   |
| 3  | India   |
| 4  | USA     |

Statistics might be:

```text
Rows = 1,000,000

Distinct countries = 50

India = 40%

USA = 10%

Others = 50%
```

These statistics are periodically maintained.

---

# Cardinality

Google interview favorite.

Definition:

```text
Number of distinct values
```

Example:

### Gender

| Gender |
| ------ |
| M      |
| F      |

Cardinality:

```text
2
```

Very low.

---

### Employee ID

| EmpID |
| ----- |
| 1     |
| 2     |
| 3     |
| 4     |

Cardinality:

```text
1,000,000
```

Very high.

---

# Why Cardinality Matters

Suppose:

```sql
WHERE emp_id = 500
```

Expected rows:

```text
1 row
```

Excellent index candidate.

---

Suppose:

```sql
WHERE gender='M'
```

Expected rows:

```text
500,000 rows
```

Index may not help.

---

# Why Optimizer May Ignore Your Index

Many developers assume:

```text
Index Exists
=
Index Used
```

False.

---

Example:

```sql
SELECT *
FROM employees
WHERE gender='M';
```

Table:

```text
1,000,000 rows

500,000 males
500,000 females
```

Using index:

```text
Find 500k pointers
Read 500k rows
```

Huge work.

---

Full scan:

```text
Read table once
```

May be cheaper.

Optimizer chooses full scan.

---

# What Is Indexing?

An index is an additional data structure that helps locate rows quickly.

Without index:

```text
1
2
3
4
5
...
10,000,000
```

Need scanning.

---

With index:

```text
1001 → Row Location
1002 → Row Location
1003 → Row Location
```

Jump directly.

---

# Internally: B+ Tree

Most relational databases use B+ Trees.

Not arrays.

Not linked lists.

Usually not hash maps.

---

Imagine:

```text
          50
       /      \
     20        80
    /  \      /  \
 10 30   70  90
```

Searching for:

```text
70
```

Path:

```text
50
↓
80
↓
70
```

Few comparisons.

---

Real databases have huge trees:

```text
Root
 ↓
Internal Node
 ↓
Internal Node
 ↓
Leaf Node
```

Even billions of rows may require only 3-5 page reads.

---

# Why B+ Tree Instead of Binary Tree?

Because databases care about disk.

A binary tree:

```text
1 key per node
```

causes too many disk reads.

---

B+ Tree node:

```text
100
200
300
400
500
...
```

Many keys per page.

Tree becomes very shallow.

Fewer I/O operations.

---

# Clustered vs Non-Clustered Index

Important interview topic.

---

## Clustered Index

Data itself stored in index order.

```text
Primary Key B+ Tree

Leaf Node
↓
Actual Data
```

Example:

```sql
PRIMARY KEY(emp_id)
```

Searching:

```sql
WHERE emp_id=1001
```

One traversal.

---

## Non-Clustered Index

Index stores pointer.

```text
Index
↓
Row Address
↓
Table Row
```

Two lookups.

---

# Covering Index

Google interview favorite.

Suppose:

```sql
SELECT name
FROM employees
WHERE emp_id=1001;
```

Index contains:

```text
emp_id
name
```

Database gets answer directly from index.

No table lookup.

This is called:

```text
Covering Index
```

Very efficient.

---

# Composite Index

Suppose:

```sql
WHERE country='India'
AND city='Bhopal'
```

Index:

```sql
(country, city)
```

B+ Tree sorted as:

```text
India,Bhopal
India,Delhi
India,Mumbai
USA,NewYork
```

Efficient.

---

# Leftmost Prefix Rule

Interview classic.

Index:

```sql
(country, city, zipcode)
```

Works for:

```sql
WHERE country='India'
```

Works for:

```sql
WHERE country='India'
AND city='Bhopal'
```

Works for:

```sql
WHERE country='India'
AND city='Bhopal'
AND zipcode='462001'
```

---

Usually doesn't help much for:

```sql
WHERE city='Bhopal'
```

because ordering starts with country.

---

# Join Optimization

Suppose:

```sql
SELECT *
FROM orders o
JOIN customers c
ON o.customer_id=c.id;
```

Optimizer must decide:

### Which table first?

```text
Orders → Customers

or

Customers → Orders
```

---

Suppose:

```text
Customers = 100

Orders = 100 million
```

Starting with customers is usually better.

Optimizer estimates this.

---

# Predicate Pushdown

Example:

```sql
SELECT *
FROM orders
WHERE status='completed';
```

Bad plan:

```text
Read all rows
Then filter
```

Good plan:

```text
Filter early
Read fewer rows
```

Called predicate pushdown.

---

# SARGability

Very common Google-level topic.

Bad:

```sql
WHERE YEAR(order_date)=2025
```

Optimizer cannot efficiently use index.

---

Good:

```sql
WHERE order_date >= '2025-01-01'
AND order_date < '2026-01-01'
```

Index usable.

---

# Experienced-Level Google Interview Questions

### Q1

You have:

```sql
WHERE gender='M'
```

Index exists.

Why full table scan?

Expected answer:

* Low cardinality
* Poor selectivity
* Index lookup more expensive

---

### Q2

Difference between clustered and non-clustered index?

Expected answer:

* Clustered stores data in index order
* Non-clustered stores row pointers
* Clustered usually faster for range scans

---

### Q3

Why are B+ Trees used instead of hash tables?

Expected answer:

* Support range queries
* Better disk locality
* Sequential leaf traversal
* Fewer page reads

---

### Q4

Why can stale statistics cause bad performance?

Expected answer:

* Wrong cardinality estimation
* Wrong join order
* Wrong index choice
* Poor execution plan

---

### Q5

Given:

```sql
INDEX(country, city)
```

Which queries use it efficiently?

You should discuss:

```sql
country
country+city
```

and leftmost-prefix rule.

---

### Q6

What is a covering index?

Expected answer:

Query satisfied entirely from index without accessing base table.

---

### Q7

Explain Nested Loop Join, Hash Join, Merge Join and when each is chosen.

This is extremely common.

---

### Q8

A query became slow overnight without code changes. What would you investigate?

Expected discussion:

* Statistics changed
* Data skew
* Execution plan changes
* Missing index
* Parameter sniffing
* Lock contention

---

### Q9

Why can adding an index sometimes slow down a system?

Expected answer:

Indexes accelerate reads but increase:

* INSERT cost
* UPDATE cost
* DELETE cost
* Storage usage
* Maintenance overhead

---

### Q10

If a table has 1 billion rows and query returns 90% of rows, should optimizer use index?

Expected answer:

Usually no.

Full scan is often cheaper.

These are the kinds of discussions that differentiate an experienced backend/data engineer candidate from someone who only knows SQL syntax.
