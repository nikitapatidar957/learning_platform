"""
SQL & Relational Databases Topics and Lessons Seed Data
Incorporating concepts from:
- python_interview/sql_notes.md
- python_interview/important_note.md
"""

SQL_TOPICS = [
    {
        "subjectSlug": "sql",
        "title": "Relational Foundations & Architecture",
        "slug": "sql-foundations-architecture",
        "description": "Database history, the relational model, ACID guarantees, relational keys, and database normalization (1NF to BCNF).",
        "order": 1,
        "isPublished": True,
    },
    {
        "subjectSlug": "sql",
        "title": "SQL Query Mastery & Clauses",
        "slug": "sql-query-mastery",
        "description": "Sublanguages, the exact SQL execution order, joins visualizer, subqueries, CTEs, window functions, and indexing.",
        "order": 2,
        "isPublished": True,
    },
]

SQL_LESSONS = [
    # -------------------------------------------------------------------------
    # Topic 1: Relational Foundations & Architecture
    # -------------------------------------------------------------------------
    {
        "topicSlug": "sql-foundations-architecture",
        "subjectSlug": "sql",
        "title": "Evolution of Databases & The Relational Model",
        "slug": "db-evolution-relational-model",
        "description": "Trace the history from paper and flat files to RDBMS, tabular schemas, and the foundational ACID transaction properties.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Why Did We Need Relational Databases?",
                    "content": (
                        "Before modern databases existed, data storage evolved through distinct historical phases:\n\n"
                        "1. Paper-Based Systems: Ledgers and physical filing cabinets. Severe physical search costs, no concurrent access, high risk of fire/damage, and zero real-time reporting.\n\n"
                        "2. Flat File Systems (.txt, .csv): Sequential text files on disks. Faster than paper, but lacked concurrent write locks (file corruption), lacked data validation (corrupted formats), and suffered from O(n) table scans.\n\n"
                        "3. Relational Databases (E.F. Codd, 1970): Modeled data as structured relations (tables) with typed columns and unique row identifiers, supporting declarative SQL querying and ACID reliability."
                    )
                },
                {
                    "type": "explanation",
                    "title": "ACID Properties: The Cornerstones of Reliable Transactions",
                    "content": (
                        "• Atomicity (All-or-Nothing): A transaction is indivisible. If an online bank transfer debits Account A by $1,000, but crashes before crediting Account B, the entire transaction rolls back. No partial executions!\n\n"
                        "• Consistency: Every transaction brings the database from one valid state to another, strictly satisfying all schema rules, foreign keys, and check constraints.\n\n"
                        "• Isolation: Concurrent transactions execute independently without interfering with one another. "
                        "Prevents concurrency bugs: Dirty Reads (reading uncommitted data), Non-repeatable Reads (data changes between reads), and Phantom Reads.\n\n"
                        "• Durability: Once a transaction commits, its changes survive permanently in disk storage even if the server suffers an abrupt power outage, thanks to Write-Ahead Logging (WAL)."
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "Transaction Isolation Levels: Read Uncommitted < Read Committed (default in PostgreSQL) < Repeatable Read (default in MySQL InnoDB) < Serializable (highest safety, lowest concurrency)."
                }
            ]
        }
    },
    {
        "topicSlug": "sql-foundations-architecture",
        "subjectSlug": "sql",
        "title": "Database Keys & Referential Integrity",
        "slug": "database-keys-integrity",
        "description": "Understand Candidate Keys, Primary Keys, Composite Keys, and Foreign Keys with cascading referential actions.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Understanding Keys in Relational Schemas",
                    "content": (
                        "• Candidate Key: Any minimal column (or set of columns) that can uniquely identify a row in a table.\n\n"
                        "• Primary Key (PK): The single candidate key selected by the database architect to uniquely identify every row. A primary key CANNOT contain NULL values and must be UNIQUE.\n\n"
                        "• Composite Key: A primary key composed of two or more columns combined (e.g., `user_id` and `course_id` together form a unique enrollment record).\n\n"
                        "• Foreign Key (FK): A column in one table that references the Primary Key of another table, enforcing referential integrity."
                    )
                },
                {
                    "type": "code",
                    "title": "Foreign Key Cascading Actions in DDL",
                    "language": "sql",
                    "code": (
                        "CREATE TABLE departments (\n"
                        "    dept_id SERIAL PRIMARY KEY,\n"
                        "    dept_name VARCHAR(100) NOT NULL UNIQUE\n"
                        ");\n\n"
                        "CREATE TABLE employees (\n"
                        "    emp_id SERIAL PRIMARY KEY,\n"
                        "    name VARCHAR(100) NOT NULL,\n"
                        "    department_id INT,\n"
                        "    -- Enforce referential integrity with cascading rules\n"
                        "    CONSTRAINT fk_dept\n"
                        "        FOREIGN KEY (department_id)\n"
                        "        REFERENCES departments(dept_id)\n"
                        "        ON DELETE SET NULL  -- If department deleted, keep employee but set dept to null\n"
                        "        ON UPDATE CASCADE   -- If dept_id changes, cascade update to employees\n"
                        ");"
                    )
                },
                {
                    "type": "callout",
                    "variant": "warning",
                    "content": "Referential Actions on Delete: `RESTRICT` / `NO ACTION` (blocks delete if children exist), `CASCADE` (deletes children automatically), `SET NULL` (sets child FK column to NULL)."
                }
            ]
        }
    },
    {
        "topicSlug": "sql-foundations-architecture",
        "subjectSlug": "sql",
        "title": "Database Normalization: 1NF to BCNF",
        "slug": "database-normalization",
        "description": "Learn how database normalization eliminates data redundancy and prevents insertion, update, and deletion anomalies.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 3,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Why Normalization Matters: The 3 Anomalies",
                    "content": (
                        "If you dump all customer, product, and order details into one giant unnormalized table, you suffer from three fatal anomalies:\n\n"
                        "• Insertion Anomaly: You cannot add a new department until at least one employee is hired into it.\n"
                        "• Update Anomaly: If the department manager changes, you must update 50,000 employee rows! If 1 row fails, data becomes inconsistent.\n"
                        "• Deletion Anomaly: If the last employee in the department quits and you delete their row, the department itself is erased from the database!"
                    )
                },
                {
                    "type": "explanation",
                    "title": "The Normal Forms Explained Simply",
                    "content": (
                        "1. First Normal Form (1NF):\n"
                        "   • Every table column must hold atomic (indivisible) values. No comma-separated lists like `phone_numbers = '123, 456'`!\n"
                        "   • Each row must be uniquely identifiable (has a primary key).\n\n"
                        "2. Second Normal Form (2NF):\n"
                        "   • Must be in 1NF.\n"
                        "   • No Partial Dependency: Every non-key column must depend on the ENTIRE primary key, not just part of a composite key.\n\n"
                        "3. Third Normal Form (3NF):\n"
                        "   • Must be in 2NF.\n"
                        "   • No Transitive Dependency: Non-key columns must NOT depend on other non-key columns (e.g., `Employee -> Dept_ID -> Dept_Name`. `Dept_Name` must move to a `departments` table).\n\n"
                        "4. Boyce-Codd Normal Form (BCNF):\n"
                        "   • Stricter version of 3NF where for every functional dependency X -> Y, X must be a super key."
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "The Classic Rule: In 3NF, \"Every non-key attribute must provide a fact about the key, the whole key, and nothing but the key, so help me Codd!\""
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 2: SQL Query Mastery & Clauses
    # -------------------------------------------------------------------------
    {
        "topicSlug": "sql-query-mastery",
        "subjectSlug": "sql",
        "title": "SQL Sublanguages & The Exact Query Execution Order",
        "slug": "sql-sublanguages-execution-order",
        "description": "Master DDL, DML, DQL, DCL, and discover the exact internal order in which database engines process SQL clauses.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": "SQLEditor",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The 5 Sublanguages of SQL",
                    "content": (
                        "• DDL (Data Definition Language): `CREATE`, `ALTER`, `DROP`, `TRUNCATE` (schema structure).\n"
                        "• DML (Data Manipulation Language): `INSERT`, `UPDATE`, `DELETE` (manipulating rows).\n"
                        "• DQL (Data Query Language): `SELECT` (reading data).\n"
                        "• DCL (Data Control Language): `GRANT`, `REVOKE` (user permissions).\n"
                        "• TCL (Transaction Control Language): `COMMIT`, `ROLLBACK`, `SAVEPOINT`."
                    )
                },
                {
                    "type": "explanation",
                    "title": "The Exact SQL Execution Order (Top Interview Question)",
                    "content": (
                        "You write a query starting with `SELECT`, but the database engine processes clauses in a completely different logical order:\n\n"
                        "1. `FROM` & `JOIN`: The tables are identified and cartesian products/joins are assembled in memory.\n"
                        "2. `WHERE`: Filters out non-matching rows before grouping.\n"
                        "3. `GROUP BY`: Aggregates the remaining rows into summary buckets.\n"
                        "4. `HAVING`: Filters aggregated group rows (cannot use `WHERE` for aggregate functions like `COUNT(*)`!).\n"
                        "5. `SELECT`: The specific output expressions and calculations are finally projected.\n"
                        "6. `DISTINCT`: Eliminates duplicate rows from the projected columns.\n"
                        "7. `ORDER BY`: Sorts the final result set.\n"
                        "8. `LIMIT` / `OFFSET`: Truncates output to the requested row window."
                    )
                },
                {
                    "type": "callout",
                    "variant": "warning",
                    "content": "Why does `WHERE salary_bonus > 10000` fail if `salary_bonus` is defined in `SELECT`? Because `WHERE` executes at Step 2, long before `SELECT` executes at Step 5! The alias does not yet exist!"
                },
                {
                    "type": "visualization",
                    "component": "SQLEditor",
                    "initialState": {
                        "defaultQuery": "SELECT name, department, salary, experience_years\nFROM employees\nWHERE salary > 70000\nORDER BY salary DESC;"
                    }
                }
            ]
        }
    },
    {
        "topicSlug": "sql-query-mastery",
        "subjectSlug": "sql",
        "title": "SQL Joins Complete Guide & Dry Runs",
        "slug": "sql-joins-deep-dive",
        "description": "Master INNER, LEFT, RIGHT, FULL, CROSS, and SELF joins with visual explanations and multi-table query patterns.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": "SQLEditor",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Visualizing SQL Joins",
                    "content": (
                        "• `INNER JOIN`: Returns only rows that have matching values in BOTH tables. Intersecting records.\n\n"
                        "• `LEFT (OUTER) JOIN`: Returns ALL rows from the left table, plus matched values from the right table. If no match exists, columns from the right table appear as `NULL`.\n\n"
                        "• `RIGHT (OUTER) JOIN`: Returns ALL rows from the right table, plus matched values from the left table.\n\n"
                        "• `FULL (OUTER) JOIN`: Returns all rows when there is a match in EITHER left or right table, filling nulls where no match exists.\n\n"
                        "• `CROSS JOIN`: Cartesian product. Every single row of Table A is paired with every row of Table B (produces count(A) * count(B) rows).\n\n"
                        "• `SELF JOIN`: Joining a table with itself (using aliases like `e` and `m`) to resolve hierarchical relationships like employee-manager."
                    )
                },
                {
                    "type": "code",
                    "title": "Self Join Example: Finding Managers for Employees",
                    "language": "sql",
                    "code": (
                        "-- Self Join matching employee to their manager\n"
                        "SELECT \n"
                        "    e.name AS employee_name,\n"
                        "    COALESCE(m.name, 'Top Executive (No Manager)') AS manager_name\n"
                        "FROM employees e\n"
                        "LEFT JOIN employees m ON e.manager_id = m.emp_id\n"
                        "ORDER BY e.name;"
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Anti-Join Pattern: To find records in Table A that have NO matching entry in Table B, use: `SELECT a.* FROM a LEFT JOIN b ON a.id = b.a_id WHERE b.a_id IS NULL;`"
                }
            ]
        }
    },
    {
        "topicSlug": "sql-query-mastery",
        "subjectSlug": "sql",
        "title": "Subqueries, CTEs & Window Functions",
        "slug": "subqueries-ctes-window-functions",
        "description": "Write readable queries using Common Table Expressions (WITH), master ROW_NUMBER/RANK/DENSE_RANK, and understand B-Tree indexes.",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 3,
        "isPublished": True,
        "interactiveType": "SQLEditor",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Common Table Expressions (CTEs) with the WITH Clause",
                    "content": (
                        "A CTE creates a temporary, named result set that you can reference within a subsequent `SELECT`, `INSERT`, `UPDATE`, or `DELETE`. "
                        "CTEs make complex nested subqueries dramatically more readable and maintainable."
                    )
                },
                {
                    "type": "code",
                    "title": "Clean CTE Example: High Earners by Department",
                    "language": "sql",
                    "code": (
                        "WITH DeptAverage AS (\n"
                        "    SELECT department, AVG(salary) AS avg_dept_salary\n"
                        "    FROM employees\n"
                        "    GROUP BY department\n"
                        ")\n"
                        "SELECT \n"
                        "    e.name,\n"
                        "    e.department,\n"
                        "    e.salary,\n"
                        "    ROUND(d.avg_dept_salary, 2) AS dept_average\n"
                        "FROM employees e\n"
                        "JOIN DeptAverage d ON e.department = d.department\n"
                        "WHERE e.salary > d.avg_dept_salary;"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Window Functions: ROW_NUMBER vs RANK vs DENSE_RANK",
                    "content": (
                        "Unlike `GROUP BY` (which collapses rows into a single summary), Window Functions perform calculations across a partition of rows "
                        "while preserving each individual row's identity!\n\n"
                        "Suppose three employees have equal salaries: $100k, $100k, $90k:\n"
                        "• `ROW_NUMBER()`: Assigns strict consecutive numbers: 1, 2, 3 (no ties).\n"
                        "• `RANK()`: Ties get same rank, but skips ranks: 1, 1, 3 (rank 2 is skipped).\n"
                        "• `DENSE_RANK()`: Ties get same rank, NO ranks skipped: 1, 1, 2."
                    )
                },
                {
                    "type": "code",
                    "title": "Top 2 Highest Paid Employees per Department (Nth Highest Problem)",
                    "language": "sql",
                    "code": (
                        "WITH RankedEmployees AS (\n"
                        "    SELECT \n"
                        "        name,\n"
                        "        department,\n"
                        "        salary,\n"
                        "        DENSE_RANK() OVER (\n"
                        "            PARTITION BY department \n"
                        "            ORDER BY salary DESC\n"
                        "        ) as salary_rank\n"
                        "    FROM employees\n"
                        ")\n"
                        "SELECT name, department, salary, salary_rank\n"
                        "FROM RankedEmployees\n"
                        "WHERE salary_rank <= 2;"
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "PostgreSQL Aliasing Gotcha: In PostgreSQL, aliasing the target table directly in `UPDATE emp AS e SET ...` is invalid SQL syntax. PostgreSQL requires join tables in the `FROM` clause: `UPDATE employees SET salary = salary * 1.1 FROM departments d WHERE employees.dept_id = d.id;`."
                }
            ]
        }
    }
]
