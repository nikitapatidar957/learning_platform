# Day 16: Working with JSON & SQL in Pandas

Master ingesting semi-structured JSON and querying relational SQL databases directly into Pandas DataFrames: `pd.read_json()`, REST API endpoints, database connection pooling with `mysql.connector`, SQLAlchemy, and executing SQL queries with `pd.read_sql_query()`.

---

## 1. Complete Hands-on Guide: JSON & SQL Ingestion

# Working with JSON and SQL

This notebook explains how to read and analyze data stored in JSON format and how to connect to a MySQL database using pandas.

## 1. Working with JSON
Definition: JSON is a lightweight data format used to store structured information like dictionaries and lists. Pandas can read JSON files directly into a DataFrame.

```python
import pandas as pd
pd.read_json('train.json')
```

Example output:
```text
   enrollee_id  city  gender  target
0  1001        23    Male    1
1  1002        13    Female  0
2  1003        17    Male    1
```

### JSON from a URL
Definition: You can also load JSON directly from an online API endpoint.

```python
pd.read_json('https://api.exchangerate-api.com/v4/latest/INR')
```

Example output:
```text
   base       date       rates
0  INR       2026-10-08  {'USD': 0.012, 'EUR': 0.011, 'JPY': 1.75}
```

---

## 2. Working with SQL
Definition: SQL is used to query data from a database. Pandas can run SQL queries and return results as a DataFrame.

```python
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='world'
)
```

Example output:
```text
<mysql.connector.connection_cext.CMySQLConnection at 0x...>
```

### Reading data using SQL query
Definition: Use `pd.read_sql_query()` to fetch table data into a DataFrame.

```python
df = pd.read_sql_query("SELECT * FROM countrylanguage", conn)
```

Example output:
```text
   CountryCode  Language  IsOfficial  Percentage
0  AFG         Dari      T          32.1
1  AFG         Pashto    T          52.4
2  ALB         Albanian  T          97.7
```

---

### Summary
- JSON is useful for reading nested or structured data.
- SQL helps work with data stored in databases.
- Pandas makes both formats easy to read and analyze using DataFrames.

```python
import pandas as pd
```

# Woking with JSON

```python
pd.read_json('train.json')
```

**Execution Output:**
```text
id      cuisine                                        ingredients
0      10259        greek  [romaine lettuce, black olives, grape tomatoes...
1      25693  southern_us  [plain flour, ground pepper, salt, tomatoes, g...
2      20130     filipino  [eggs, pepper, salt, mayonaise, cooking oil, g...
3      22213       indian                [water, vegetable oil, wheat, salt]
4      13162       indian  [black pepper, shallots, cornflour, cayenne pe...
...      ...          ...                                                ...
39769  29109        irish  [light brown sugar, granulated sugar, butter, ...
39770  11462      italian  [KRAFT Zesty Italian Dressing, purple onion, b...
39771   2238        irish  [eggs, citrus fruit, raisins, sourdough starte...
39772  41882      chinese  [boneless chicken skinless thigh, minced garli...
39773   2362      mexican  [green chile, jalapeno chilies, onions, ground...

[39774 rows x 3 columns]
```

```python
pd.read_json('https://api.exchangerate-api.com/v4/latest/INR')
```

**Execution Output:**
```text
api_url  \
AED  https://www.exchangerate-api.com   
AFN  https://www.exchangerate-api.com   
ALL  https://www.exchangerate-api.com   
AMD  https://www.exchangerate-api.com   
ANG  https://www.exchangerate-api.com   
..                                ...   
XOF  https://www.exchangerate-api.com   
XPF  https://www.exchangerate-api.com   
YER  https://www.exchangerate-api.com   
ZAR  https://www.exchangerate-api.com   
ZMW  https://www.exchangerate-api.com   

                                       api_docs  \
AED  https://www.exchangerate-api.com/docs/free   
AFN  https://www.exchangerate-api.com/docs/free   
ALL  https://www.exchangerate-api.com/docs/free   
AMD  https://www.exchangerate-api.com/docs/free   
ANG  https://www.exchangerate-api.com/docs/free   
..                                          ...   
XOF  https://www.exchangerate-api.com/docs/free   
XPF  https://www.exchangerate-api.com/docs/free   
YER  https://www.exchangerate-api.com/docs/free   
ZAR  https://www.exchangerate-api.com/docs/free   
ZMW  https://www.exchangerate-api.com/docs/free   

                                  api_terms base       date  \
AED  https://www.exchangerate-api.com/terms  INR 2021-03-31   
AFN  https://www.exchangerate-api.com/terms  INR 2021-03-31   
ALL  https://www.exchangerate-api.com/terms  INR 2021-03-31   
AMD  https://www.exchangerate-api.com/terms  INR 2021-03-31   
ANG  https://www.exchangerate-api.com/terms  INR 2021-03-31   
..                                      ...  .
... [Output truncated for brevity]
```

# Working with SQL

```python
!pip install mysql.connector
```

**Execution Output:**
```text
Processing c:\users\91842\appdata\local\pip\cache\wheels\57\e4\98\5feafb5c393dd2540e44b064a6f95832990d543e5b4f53ea8f\mysql_connector-2.2.9-cp38-cp38-win_amd64.whl
Installing collected packages: mysql.connector
Successfully installed mysql.connector
```

```python
import mysql.connector
```

```python
conn = mysql.connector.connect(host='localhost',user='root',password='',database='world')
```

```python
df = pd.read_sql_query("SELECT * FROM countrylanguage",conn)
```

```python
df
```

**Execution Output:**
```text
CountryCode    Language IsOfficial  Percentage
0           ABW       Dutch          T         5.3
1           ABW     English          F         9.5
2           ABW  Papiamento          F        76.7
3           ABW     Spanish          F         7.4
4           AFG     Balochi          F         0.9
..          ...         ...        ...         ...
979         ZMB      Tongan          F        11.0
980         ZWE     English          T         2.2
981         ZWE     Ndebele          F        16.2
982         ZWE      Nyanja          F         2.2
983         ZWE       Shona          F        72.1

[984 rows x 4 columns]
```

---

## Key Interview Concepts & Production Architecture

### 1. Ingesting JSON with Pandas
- **Standard Flat JSON**:
  `pd.read_json('data.json')` loads records into a DataFrame.
- **Nested JSON & Flattening**:
  When dealing with deeply nested JSON structures from microservices, use `pd.json_normalize()`:
  ```python
  import json
  from pandas import json_normalize
  
  with open('nested_data.json') as f:
      data = json.load(f)
  df = json_normalize(data, record_path=['orders'], meta=['customer_id', 'name'])
  ```

### 2. SQL to DataFrame Best Practices
- **`pd.read_sql_query()` vs `pd.read_sql_table()`**:
  - `pd.read_sql_query(query, engine)` executes custom SQL queries, pushing filtering, joins, and aggregations down to the database engine.
  - `pd.read_sql_table(table_name, engine)` loads the whole table.
- **Connection Management**:
  Always use SQLAlchemy engines or context managers so database connections and pool cursors close automatically:
  ```python
  from sqlalchemy import create_engine
  
  engine = create_engine('mysql+mysqlconnector://user:password@localhost/world')
  with engine.connect() as conn:
      df = pd.read_sql_query("SELECT CountryCode, Language, Percentage FROM countrylanguage WHERE IsOfficial = 'T'", conn)
  ```
- **Writing to SQL (`df.to_sql`)**:
  ```python
  df.to_sql('clean_customers', con=engine, if_exists='replace', index=False, chunksize=1000)
  ```
