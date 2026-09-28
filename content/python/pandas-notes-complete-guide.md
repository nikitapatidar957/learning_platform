# What is Pandas in Python?

pandas is an open-source Python library mainly used for:

* Data analysis
* Data manipulation
* Data cleaning
* Data transformation
* Working with structured/tabular data

It is built on top of NumPy and is widely used in:

* Data Science
* Machine Learning
* Analytics
* Finance
* AI applications

---

# Why Pandas is Used

Pandas helps you:

* Read data from files/databases
* Clean messy data
* Filter and sort data
* Perform calculations
* Handle missing values
* Merge datasets
* Analyze large datasets easily

---

# Main Data Structures in Pandas

## 1. Series

A one-dimensional labeled array.

Example:

```python
import pandas as pd

s = pd.Series([10, 20, 30])
print(s)
```

Output:

```python
0    10
1    20
2    30
dtype: int64
```

---

## 2. DataFrame

A two-dimensional table (rows + columns).

Example:

```python
import pandas as pd

data = {
    "Name": ["A", "B"],
    "Age": [21, 22]
}

df = pd.DataFrame(data)
print(df)
```

Output:

```python
  Name  Age
0    A   21
1    B   22
```

---

# Important Pandas Functions

| Function         | Purpose               |
| ---------------- | --------------------- |
| `read_csv()`     | Read CSV file         |
| `head()`         | First 5 rows          |
| `tail()`         | Last 5 rows           |
| `info()`         | Dataset summary       |
| `describe()`     | Statistics summary    |
| `shape`          | Rows and columns      |
| `columns`        | Column names          |
| `iloc[]`         | Index-based selection |
| `loc[]`          | Label-based selection |
| `drop()`         | Remove rows/columns   |
| `fillna()`       | Fill missing values   |
| `isnull()`       | Detect null values    |
| `groupby()`      | Group data            |
| `merge()`        | Join datasets         |
| `sort_values()`  | Sorting               |
| `value_counts()` | Count frequency       |

---

# Beginner Interview Questions

## 1. What is Pandas?

Pandas is a Python library used for data manipulation and analysis.

---

## 2. What are the main data structures in Pandas?

* Series
* DataFrame

---

## 3. Difference between Series and DataFrame?

| Series              | DataFrame        |
| ------------------- | ---------------- |
| 1D                  | 2D               |
| Single column       | Multiple columns |
| Homogeneous usually | Heterogeneous    |

---

## 4. What is a DataFrame?

A tabular data structure with rows and columns.

---

## 5. How to read a CSV file?

```python
df = pd.read_csv("file.csv")
```

---

## 6. How to display first rows?

```python
df.head()
```

---

## 7. How to check dataset shape?

```python
df.shape
```

---

## 8. How to check null values?

```python
df.isnull()
```

---

## 9. How to remove null values?

```python
df.dropna()
```

---

## 10. How to fill missing values?

```python
df.fillna(0)
```

---

# Intermediate Interview Questions

## 11. Difference between `loc` and `iloc`?

| loc                | iloc                |
| ------------------ | ------------------- |
| Label based        | Integer index based |
| Includes end index | Excludes end index  |

Example:

```python
df.loc[0, "Name"]
df.iloc[0, 1]
```

---

## 12. Difference between `merge()` and `concat()`?

| merge()               | concat()                |
| --------------------- | ----------------------- |
| SQL-style join        | Stack/append            |
| Common columns needed | No common column needed |

---

## 13. What is GroupBy in Pandas?

Used to split, apply function, and combine data.

Example:

```python
df.groupby("Department")["Salary"].mean()
```

---

## 14. What is pivot table?

Used to summarize data.

```python
pd.pivot_table(df, values="Sales", index="Region")
```

---

## 15. Difference between `apply()` and `map()`?

| apply()               | map()              |
| --------------------- | ------------------ |
| Works on rows/columns | Works element-wise |
| DataFrame/Series      | Series only        |

---

## 16. What is indexing in Pandas?

Selecting/accessing data using labels or positions.

---

## 17. How to rename columns?

```python
df.rename(columns={"old":"new"})
```

---

## 18. How to sort data?

```python
df.sort_values("Salary")
```

---

## 19. How to remove duplicates?

```python
df.drop_duplicates()
```

---

## 20. What is vectorization in Pandas?

Performing operations on entire columns instead of loops for faster execution.

Example:

```python
df["Bonus"] = df["Salary"] * 0.1
```

---

# Advanced Interview Questions

## 21. Why is Pandas faster than Python loops?

Because Pandas uses vectorized operations built on NumPy.

---

## 22. Difference between shallow copy and deep copy?

| Shallow Copy             | Deep Copy        |
| ------------------------ | ---------------- |
| References original data | Independent copy |
| Changes affect original  | No effect        |

```python
df.copy(deep=True)
```

---

## 23. What is MultiIndex?

Hierarchical indexing using multiple levels.

---

## 24. What are categorical data types?

Memory-efficient data type for repeated categories.

---

## 25. Explain `groupby().agg()`

Used for multiple aggregations.

```python
df.groupby("Dept").agg({
    "Salary": ["mean", "max"]
})
```

---

## 26. Difference between `apply()`, `applymap()`, and `map()`?

| Function     | Works On                      |
| ------------ | ----------------------------- |
| `map()`      | Series                        |
| `apply()`    | Series/DataFrame              |
| `applymap()` | Entire DataFrame element-wise |

---

## 27. How does Pandas handle large datasets?

* Chunk processing
* Efficient indexing
* Vectorized operations
* Memory optimization

---

## 28. What is chained indexing problem?

Multiple indexing causing unexpected results.

Bad:

```python
df[df["Age"] > 20]["Salary"]
```

Better:

```python
df.loc[df["Age"] > 20, "Salary"]
```

---

## 29. What is SettingWithCopyWarning?

Warning caused when modifying copied data unintentionally.

---

## 30. Difference between `join()` and `merge()`?

| join()      | merge()            |
| ----------- | ------------------ |
| Index-based | Column/index-based |
| Simpler     | More flexible      |

---

# Scenario-Based Cross Questions

## Q1.

You have 10 million rows. `apply()` is slow. What will you do?

### Answer

* Use vectorization
* Use NumPy operations
* Avoid loops
* Use categorical datatype
* Process in chunks

---

## Q2.

How will you optimize memory in Pandas?

### Answer

* Convert object → category
* Use smaller datatypes
* Remove unnecessary columns
* Use chunking

---

## Q3.

Why use `loc` instead of chained indexing?

### Answer

To avoid:

* `SettingWithCopyWarning`
* Unexpected behavior
* Data inconsistency

---

## Q4.

How to merge 3 datasets efficiently?

### Answer

* Use indexed joins
* Remove duplicate columns
* Merge in stages
* Optimize datatypes first

---

## Q5.

When will you use `pivot_table()` instead of `groupby()`?

### Answer

Use `pivot_table()` when:

* Need Excel-like summaries
* Need multi-dimensional analysis
* Need automatic aggregation

---

# Frequently Asked Cross Questions

## Why Pandas over Excel?

| Pandas                   | Excel        |
| ------------------------ | ------------ |
| Handles millions of rows | Limited rows |
| Automation               | Manual       |
| Faster                   | Slower       |
| Coding-based             | GUI-based    |

---

## Why Pandas over SQL?

| Pandas                   | SQL                      |
| ------------------------ | ------------------------ |
| In-memory processing     | Database processing      |
| Better for ML pipelines  | Better for storage/query |
| Flexible transformations | Structured querying      |

---

## Why is Pandas built on NumPy?

Because NumPy provides:

* Fast array operations
* Vectorization
* Memory efficiency

---

# Real Interview Coding Questions

## Find duplicate rows

```python
df[df.duplicated()]
```

---

## Top 5 highest salaries

```python
df.nlargest(5, "Salary")
```

---

## Count null values column-wise

```python
df.isnull().sum()
```

---

## Employees with salary > 50000

```python
df[df["Salary"] > 50000]
```

---

## Average salary department-wise

```python
df.groupby("Department")["Salary"].mean()
```

---

# Tricky Pandas Interview Questions

## Why does this fail?

```python
if df["Salary"] > 50000:
```

### Answer

Because it returns a Series of booleans, not a single boolean.

Correct:

```python
df[df["Salary"] > 50000]
```

---

## Difference between:

```python
df["A"]
```

and

```python
df[["A"]]
```

### Answer

| Syntax      | Returns   |
| ----------- | --------- |
| `df["A"]`   | Series    |
| `df[["A"]]` | DataFrame |

---

# Important Topics Interviewers Ask

* Indexing
* GroupBy
* Merge/Join
* Missing values
* Performance optimization
* Vectorization
* Pivot tables
* MultiIndex
* Datetime handling
* Memory optimization
* Window functions
* Categorical data
* String operations
* File handling

---

# Most Important Practical Pandas Topics

## Datetime Handling

```python
df["Date"] = pd.to_datetime(df["Date"])
```

---

## String Operations

```python
df["Name"].str.upper()
```

---

## Conditional Filtering

```python
df.query("Salary > 50000")
```

---

## Window Functions

```python
df["rolling_avg"] = df["Sales"].rolling(3).mean()
```

---

# Expert-Level Cross Questions

## Why is vectorization faster internally?

Because operations are executed in optimized C-level NumPy code instead of Python loops.

---

## Why object datatype is memory expensive?

Because objects store Python references instead of raw binary values.

---

## Why can chained indexing create bugs?

Because Pandas may return a view or copy unpredictably.

---

## When should Pandas not be used?

Avoid Pandas when:

* Data is extremely large (TBs)
* Distributed processing needed

Use:

* Apache Spark
* Dask instead.

---

# Final Interview Tip

Most interviews focus on:

1. Data cleaning
2. GroupBy
3. Merge
4. loc vs iloc
5. Missing values
6. Optimization
7. Real-world problem solving
8. Writing efficient code

Interviewers usually ask:

* “How will you optimize this?”
* “What happens internally?”
* “Why use this method?”
* “Can this fail in production?”

Those cross-questions decide seniority level.

Here are the most important Pandas `df.isnull()` interview questions and practice questions — from beginner to advanced — commonly asked in Data Science, Data Analysis, and Python interviews.

---

# What is `df.isnull()`?

```python
df.isnull()
```

Returns a DataFrame of boolean values:

* `True` → value is missing (`NaN`, `None`)
* `False` → value exists

Example:

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, np.nan, 3],
    "B": [None, 5, 6]
})

print(df.isnull())
```

Output:

```python
       A      B
0  False   True
1   True  False
2  False  False
```

---

# Beginner Interview Questions

## 1. What does `isnull()` do in Pandas?

Checks missing/null values and returns boolean results.

---

## 2. Difference between `isnull()` and `notnull()`?

| Function    | Meaning                   |
| ----------- | ------------------------- |
| `isnull()`  | Detect missing values     |
| `notnull()` | Detect non-missing values |

---

## 3. Difference between `isnull()` and `isna()`?

They are identical.

```python
df.isnull() == df.isna()
```

returns `True`.

---

## 4. What values are treated as null in Pandas?

* `np.nan`
* `None`
* `pd.NA`

---

## 5. How to count null values in each column?

```python
df.isnull().sum()
```

---

## 6. How to count total null values in entire DataFrame?

```python
df.isnull().sum().sum()
```

---

## 7. How to find rows containing null values?

```python
df[df.isnull().any(axis=1)]
```

---

## 8. How to find columns having null values?

```python
df.columns[df.isnull().any()]
```

---

## 9. How to check if a DataFrame has any null values?

```python
df.isnull().values.any()
```

---

## 10. How to calculate null percentage column-wise?

```python
(df.isnull().sum() / len(df)) * 100
```

---

# Intermediate Interview Questions

## 11. Difference between `None` and `NaN`?

| None          | NaN                            |
| ------------- | ------------------------------ |
| Python object | NumPy floating missing value   |
| Generic       | Numeric missing representation |

---

## 12. What is `axis=1` in `.any(axis=1)`?

Checks row-wise.

```python
df.isnull().any(axis=1)
```

Returns rows having at least one null.

---

## 13. What is `axis=0`?

Checks column-wise.

---

## 14. How to select rows where all values are null?

```python
df[df.isnull().all(axis=1)]
```

---

## 15. How to remove rows with null values?

```python
df.dropna()
```

---

## 16. How to remove columns with null values?

```python
df.dropna(axis=1)
```

---

## 17. How to fill null values?

```python
df.fillna(0)
```

---

## 18. How to replace null values with column mean?

```python
df["A"].fillna(df["A"].mean())
```

---

## 19. Difference between `dropna()` and `fillna()`?

| dropna               | fillna                |
| -------------------- | --------------------- |
| Removes missing data | Replaces missing data |

---

## 20. How to count null values row-wise?

```python
df.isnull().sum(axis=1)
```

---

# Advanced Interview Questions

## 21. Why does `NaN != NaN`?

IEEE floating-point standard defines NaN as unequal to everything, including itself.

```python
np.nan == np.nan
# False
```

---

## 22. Performance difference between `isnull()` and loops?

`isnull()` is vectorized and much faster.

---

## 23. How does Pandas internally represent missing values?

Mostly using:

* `NaN`
* masked arrays
* nullable dtypes (`Int64`, `string`, `boolean`)

---

## 24. What is nullable integer type in Pandas?

```python
dtype="Int64"
```

Supports null values unlike normal `int64`.

---

## 25. Why normal integer columns convert to float when NaN appears?

Because `NaN` is float type.

Example:

```python
pd.Series([1, 2, np.nan])
```

becomes:

```python
float64
```

---

## 26. How to detect missing values in specific columns only?

```python
df["A"].isnull()
```

or

```python
df[["A", "B"]].isnull()
```

---

## 27. How to sort columns based on missing values?

```python
df.isnull().sum().sort_values(ascending=False)
```

---

## 28. How to visualize missing values?

Using libraries like:

* `missingno`
* `seaborn`
* `matplotlib`

Example:

```python
import missingno as msno
msno.matrix(df)
```

---

## 29. How to remove rows if a specific column has null?

```python
df.dropna(subset=["A"])
```

---

## 30. How to keep rows having at least 2 non-null values?

```python
df.dropna(thresh=2)
```

---

# Scenario-Based Interview Questions

## 31. Dataset has 80% missing values in one column. What will you do?

Possible answers:

* Drop column
* Impute values
* Investigate business importance
* Use advanced imputation

---

## 32. Which imputation techniques do you know?

* Mean
* Median
* Mode
* Forward fill
* Backward fill
* KNN imputation
* Regression imputation

---

## 33. Why median is preferred over mean sometimes?

Median handles outliers better.

---

## 34. When should you not drop null values?

When dataset is small or missing data is meaningful.

---

## 35. Difference between Missing Completely at Random and Missing Not at Random?

Important ML theory question.

| Type | Meaning                                 |
| ---- | --------------------------------------- |
| MCAR | Missing independent of data             |
| MAR  | Missing depends on observed data        |
| MNAR | Missing depends on missing value itself |

---

# Coding Practice Questions

# Easy Practice

## Q1. Count null values in each column

```python
df.isnull().sum()
```

---

## Q2. Find rows containing at least one null

```python
df[df.isnull().any(axis=1)]
```

---

## Q3. Remove rows where all values are null

```python
df.dropna(how="all")
```

---

## Q4. Replace nulls with 0

```python
df.fillna(0)
```

---

## Q5. Find null percentage

```python
(df.isnull().mean()) * 100
```

---

# Medium Practice

## Q6. Fill numeric columns with mean and categorical with mode

```python
for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].mean(), inplace=True)
```

---

## Q7. Remove columns having more than 50% null values

```python
threshold = len(df) * 0.5

df = df.loc[:, df.isnull().sum() < threshold]
```

---

## Q8. Create a heatmap of missing values

```python
import seaborn as sns

sns.heatmap(df.isnull())
```

---

# Advanced Practice Questions

## Q9. Build custom function to summarize missing values

```python
def missing_report(df):
    return pd.DataFrame({
        "Null_Count": df.isnull().sum(),
        "Null_Percentage": df.isnull().mean() * 100
    })

print(missing_report(df))
```

---

## Q10. Find consecutive missing values in time series

```python
df["is_null"] = df["A"].isnull()

groups = (df["is_null"] != df["is_null"].shift()).cumsum()

result = df.groupby(groups)["is_null"].sum()
```

---

# Very Common Real Interview Questions

## "How do you handle missing values in machine learning?"

Expected answer:

1. Analyze missing pattern
2. Measure percentage
3. Understand business reason
4. Decide:

   * drop
   * impute
   * predictive filling
5. Validate impact on model

---

## "What problems can missing values create?"

* Model errors
* Biased predictions
* Wrong statistics
* Data leakage
* Reduced accuracy

---

# Most Important One-Liners

```python
df.isnull()

df.isnull().sum()

df.isnull().sum().sum()

df.isnull().any()

df.isnull().any(axis=1)

df.isnull().all(axis=1)

df.dropna()

df.fillna()

df.notnull()

df.isna()
```

---

# Trick Interview Questions

## Q. Why does this fail?

```python
df[df["A"] == np.nan]
```

Because:

```python
np.nan != np.nan
```

Correct way:

```python
df[df["A"].isnull()]
```

---

## Q. Difference between:

```python
df.isnull().sum()
```

and

```python
df.count()
```

| Expression       | Meaning            |
| ---------------- | ------------------ |
| `isnull().sum()` | Counts missing     |
| `count()`        | Counts non-missing |

---

Here’s a simple explanation of each Pandas statement with examples.

---

# 1. `df3.dropna(how="all")`

This removes rows where **all values are NaN (missing)**.

### Example

```python
import pandas as pd
import numpy as np

df3 = pd.DataFrame({
    "A": [1, np.nan, np.nan],
    "B": [2, np.nan, np.nan]
})

print(df3)
```

Output:

|   | A   | B   |
| - | --- | --- |
| 0 | 1.0 | 2.0 |
| 1 | NaN | NaN |
| 2 | NaN | NaN |

Now:

```python
df3.dropna(how="all")
```

Output:

|   | A   | B   |
| - | --- | --- |
| 0 | 1.0 | 2.0 |

### Meaning of `how="all"`

* Remove row only if **all columns are NaN**
* If even one value exists, row stays

---

## Difference

### `how="all"`

```python
df3.dropna(how="all")
```

Remove row if **everything is null**

### `how="any"`

```python
df3.dropna(how="any")
```

Remove row if **even one null exists**

---

# 2. `pd.pivot_table(df3, values="B", index="C")`

This creates a **pivot table**.

A pivot table groups data and summarizes it.

---

### Example

```python
df3 = pd.DataFrame({
    "C": ["X", "X", "Y", "Y"],
    "B": [10, 20, 30, 40]
})
```

|   | C | B  |
| - | - | -- |
| 0 | X | 10 |
| 1 | X | 20 |
| 2 | Y | 30 |
| 3 | Y | 40 |

Now:

```python
pd.pivot_table(df3, values="B", index="C")
```

Output:

| C | B  |
| - | -- |
| X | 15 |
| Y | 35 |

---

## What happened?

It grouped by column `"C"` and took the **mean (average)** of `"B"`.

### Internally:

For `X`:
[
(10 + 20)/2 = 15
]

For `Y`:
[
(30 + 40)/2 = 35
]

---

## Equivalent to:

```python
df3.groupby("C")["B"].mean()
```

---

## Important Parameters

### `values="B"`

Which column to summarize.

### `index="C"`

Group by this column.

---

# 3. `df3.isnull().values.any()`

This checks:

> “Does the DataFrame contain at least one missing value?”

---

## Step-by-step

### Step 1: `df3.isnull()`

Converts values into True/False.

Example:

```python
df3 = pd.DataFrame({
    "A": [1, None],
    "B": [3, 4]
})
```

```python
df3.isnull()
```

Output:

|   | A     | B     |
| - | ----- | ----- |
| 0 | False | False |
| 1 | True  | False |

---

### Step 2: `.values`

Converts DataFrame into NumPy array.

```python
array([[False, False],
       [ True, False]])
```

---

### Step 3: `.any()`

Checks if **at least one True exists**.

```python
True
```

---

# Final Meaning

```python
df3.isnull().values.any()
```

returns:

* `True` → at least one missing value exists
* `False` → no missing values

---

# Interview-style Summary

| Code                    | Meaning                               |
| ----------------------- | ------------------------------------- |
| `dropna(how="all")`     | Remove rows where all values are null |
| `pivot_table()`         | Group and summarize data              |
| `isnull().values.any()` | Check if any null value exists        |
To remove a **column** where all values are `NaN`, use:

```python
df3.dropna(axis=1, how="all")
```

---

# Explanation

## `axis=1`

* `axis=0` → rows (default)
* `axis=1` → columns

## `how="all"`

Remove column only if **all values are null**

---

# Example

```python id="5bgsg2"
import pandas as pd
import numpy as np

df3 = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [np.nan, np.nan, np.nan],
    "C": [4, 5, 6]
})

print(df3)
```

Output:

| A | B   | C |
| - | --- | - |
| 1 | NaN | 4 |
| 2 | NaN | 5 |
| 3 | NaN | 6 |

---

Now:

```python id="ab3af7"
df3.dropna(axis=1, how="all")
```

Output:

| A | C |
| - | - |
| 1 | 4 |
| 2 | 5 |
| 3 | 6 |

Column `"B"` is removed because every value is null.

---

# Interview Point

```python
df.dropna(axis=1, how="all")
```

means:

> “Drop columns where all values are missing.”
# Indexing in Pandas

Indexing means:

> Selecting or accessing rows and columns using labels or positions.

Pandas mainly uses:

1. `loc[]` → label-based indexing
2. `iloc[]` → position-based indexing

---

# Example DataFrame

```python id="k5it0q"
import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Riya", "John"],
    "Age": [21, 25, 30],
    "City": ["Delhi", "Mumbai", "Pune"]
})

print(df)
```

Output:

|   | Name | Age | City   |
| - | ---- | --- | ------ |
| 0 | Aman | 21  | Delhi  |
| 1 | Riya | 25  | Mumbai |
| 2 | John | 30  | Pune   |

---

# 1. Access Column

```python id="dmbd4n"
df["Name"]
```

Output:

```python id="38e43q"
0    Aman
1    Riya
2    John
```

---

# 2. Access Row using `loc[]` (label/index)

```python id="65n7gj"
df.loc[1]
```

Output:

| Name | Age | City   |
| ---- | --- | ------ |
| Riya | 25  | Mumbai |

Here `1` is the row label/index.

---

# 3. Access Row using `iloc[]` (position)

```python id="cnzmd8"
df.iloc[2]
```

Output:

| Name | Age | City |
| ---- | --- | ---- |
| John | 30  | Pune |

Here `2` means third row position.

---

# 4. Access Specific Value

```python id="22d6q6"
df.loc[0, "City"]
```

Output:

```python id="3sdfe0"
Delhi
```

Meaning:

* Row label = `0`
* Column label = `"City"`

---

# 5. Access Multiple Columns

```python id="88vckl"
df[["Name", "Age"]]
```

Output:

| Name | Age |
| ---- | --- |
| Aman | 21  |
| Riya | 25  |
| John | 30  |

---

# 6. Slicing

```python id="8p6s5y"
df.iloc[0:2]
```

Output:

First 2 rows.

---

# Quick Difference

| Method   | Uses              |
| -------- | ----------------- |
| `loc[]`  | Labels/names      |
| `iloc[]` | Integer positions |

---

# Interview Definition

> Indexing in Pandas is the process of selecting and accessing rows, columns, or specific values using labels (`loc`) or integer positions (`iloc`).

In Pandas, datatype conversion is mainly done using `astype()`.

Example dataframe:

```python id="d1"
import pandas as pd

df = pd.DataFrame({
    "A": ["1", "2", "3"],
    "B": ["10.5", "20.5", "30.5"]
})

print(df.dtypes)
```

Output:

```python id="d2"
A    object
B    object
```

---

# 1. Change column datatype using `astype()`

## Convert to integer

```python id="d3"
df["A"] = df["A"].astype(int)
```

## Convert to float

```python id="d4"
df["B"] = df["B"].astype(float)
```

Now:

```python id="d5"
print(df.dtypes)
```

Output:

```python id="d6"
A      int64
B    float64
```

---

# 2. Change multiple columns together

```python id="d7"
df = df.astype({
    "A": "int",
    "B": "float"
})
```

---

# 3. Convert to string

```python id="d8"
df["A"] = df["A"].astype(str)
```

---

# 4. Convert to datetime

```python id="d9"
df["date"] = pd.to_datetime(df["date"])
```

Example:

```python id="d10"
df = pd.DataFrame({
    "date": ["2026-01-01", "2026-01-02"]
})

df["date"] = pd.to_datetime(df["date"])

print(df.dtypes)
```

---

# 5. Convert with error handling

```python id="d11"
pd.to_numeric(df["A"], errors="coerce")
```

`errors="coerce"` converts invalid values to `NaN`.

Example:

```python id="d12"
s = pd.Series(["1", "2", "abc"])

print(pd.to_numeric(s, errors="coerce"))
```

Output:

```python id="d13"
0    1.0
1    2.0
2    NaN
```

---

# 6. Common datatype conversions

| Convert To | Code                  |
| ---------- | --------------------- |
| int        | `.astype(int)`        |
| float      | `.astype(float)`      |
| string     | `.astype(str)`        |
| bool       | `.astype(bool)`       |
| datetime   | `pd.to_datetime()`    |
| category   | `.astype("category")` |

---

# 7. Check datatype

```python id="d14"
print(df.dtypes)
```

Single column:

```python id="d15"
print(df["A"].dtype)
```

---

# Important Interview Questions

## Difference between `astype()` and `to_numeric()`

| Method            | Purpose                                      |
| ----------------- | -------------------------------------------- |
| `astype()`        | strict conversion                            |
| `pd.to_numeric()` | safer numeric conversion with error handling |

---

## Why object datatype occurs?

Because Pandas stores:

* mixed values
* strings
* text columns

as:

```python id="d16"
object
```
t looks like you're working on the Pivot Table problem. Let me help you understand what might be missing.

Your current code:

return pd.pivot_table(weather, values="city", index="month")
Apply Code
Questions to consider:

What does a pivot table do? It transforms data by rotating rows into columns. Think about what should become the new columns after pivoting.

What columns does the input DataFrame have? Check the problem description for the schema (likely includes month, city, and temperature or similar).

What should the output look like? In a pivot operation, you typically need:

index → what stays as rows
columns → what becomes new column headers
values → what data fills the cells
Hint: Your code is missing the columns parameter. Look at the problem's example input/output to identify which column should be rotated into headers.

Try revising your pivot_table() call with all three parameters. Would you like me to give more specific guidance once you've checked the problem examples?


 can see you're working on the pd.melt() function. There's an issue with how you're using var_name. Let me guide you to understand it better:

Key Questions to Consider:

What does var_name do? After melting, the original column names (quarter_1, quarter_2, etc.) need to be stored somewhere. var_name specifies the name of that single new column, not the list of values it contains.

What should the output look like?

Before melt: columns are product, quarter_1, quarter_2, quarter_3, quarter_4
After melt: columns should be product, quarter, sales
quarter column contains: quarter_1, quarter_2, quarter_3, quarter_4
sales column contains: the actual sales values
Try This:

Change var_name from a list to a single string: var_name="quarter"
Keep value_vars as the list of columns to unpivot
Would you like to test this modification and see if the output matches the expected format?