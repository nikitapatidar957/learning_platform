# Day 17: Ingesting REST APIs into Pandas DataFrames

Master fetching data from external REST APIs and transforming JSON responses into structured Pandas DataFrames: HTTP requests with `requests.get()`, pagination handling, schema parsing, robust concatenation, and dataset export.

---

## 1. Complete Hands-on Guide: API to DataFrame

# API to DataFrame

This notebook shows how to fetch JSON data from an API and convert it into a pandas DataFrame for analysis.

## 1. Import required libraries
Definition: We need `pandas` to create DataFrames and `requests` to call the API.

```python
import pandas as pd
import requests
```

Example output:
```text
# No visible output, just the libraries are imported.
```

## 2. Make an API request
Definition: Use the `requests.get()` method to fetch data from a public API endpoint.

```python
response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=...&language=en-US&page=1')
```

Example output:
```text
<Response [200]>
```

## 3. Convert API JSON to DataFrame
Definition: Extract the `results` list from the JSON response and convert it into a DataFrame.

```python
temp_df = pd.DataFrame(response.json()['results'])[['id', 'title', 'overview', 'release_date', 'popularity', 'vote_average', 'vote_count']]
```

Example output:
```text
      id                 title                         overview               release_date  popularity   vote_average  vote_count
0    278     The Shawshank Redemption      ...             1994-09-23    110.5         8.7          24000
1    238     The Godfather                ...             1972-03-14    95.2          8.7          18000
```

## 4. View the DataFrame
Definition: Display the first few rows of the DataFrame using `head()`.

```python
df.head()
```

Example output:
```text
      id     title                 overview                 release_date  popularity  vote_average  vote_count
0    278    The Shawshank Redemption ...                   1994-09-23   110.5      8.7          24000
1    238    The Godfather           ...                   1972-03-14    95.2      8.7          18000
```

## 5. Collect multiple pages from the API
Definition: Loop through many pages of the API and append each page result to a single DataFrame.

```python
for i in range(1, 429):
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?page={}'.format(i))
    temp_df = pd.DataFrame(response.json()['results'])[['id', 'title', 'overview', 'release_date', 'popularity', 'vote_average', 'vote_count']]
    df = df.append(temp_df, ignore_index=True)
```

Example output:
```text
# No immediate printed output, but the DataFrame grows with each page.
```

## 6. Check dataset size
Definition: Use `.shape` to see how many rows and columns the DataFrame has.

```python
df.shape
```

Example output:
```text
(8560, 7)
```

## 7. Save DataFrame to CSV
Definition: Export the processed data into a CSV file for later use.

```python
df.to_csv('movies.csv')
```

Example output:
```text
# Creates a file named movies.csv in the current folder.
```

---

### Summary
API data is often returned as JSON. By using `requests` and `pandas`, we can fetch that data, convert it into a DataFrame, and save it for further analysis.

```python
import pandas as pd
import requests
```

```python
response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1')
```

```python
temp_df = pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]
```

```python
df.head()
```

**Execution Output:**
```text
id                        title  \
0   19404  Dilwale Dulhania Le Jayenge   
1  724089    Gabriel's Inferno Part II   
2     278     The Shawshank Redemption   
3     238                The Godfather   
4  761053   Gabriel's Inferno Part III   

                                            overview release_date  popularity  \
0  Raj is a rich, carefree, happy-go-lucky second...   1995-10-20      18.433   
1  Professor Gabriel Emerson finally learns the t...   2020-07-31       8.439   
2  Framed in the 1940s for the double murder of h...   1994-09-23      65.570   
3  Spanning the years 1945 to 1955, a chronicle o...   1972-03-14      63.277   
4  The final part of the film adaption of the ero...   2020-11-19      26.691   

   vote_average  vote_count  
0           8.7        2763  
1           8.7        1223  
2           8.7       18637  
3           8.7       14052  
4           8.7         773
```

```python
df = pd.DataFrame()
```

```python
df
```

**Execution Output:**
```text
Empty DataFrame
Columns: []
Index: []
```

```python
for i in range(1,429):
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={}'.format(i))
    temp_df = pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]
    df = df.append(temp_df,ignore_index=True)
```

```python
df
```

**Execution Output:**
```text
id                        title  \
0      19404  Dilwale Dulhania Le Jayenge   
1     724089    Gabriel's Inferno Part II   
2        278     The Shawshank Redemption   
3        238                The Godfather   
4     761053   Gabriel's Inferno Part III   
...      ...                          ...   
8546   13805               Disaster Movie   
8547    5491            Battlefield Earth   
8548   14164         Dragonball Evolution   
8549   11059            House of the Dead   
8550   40016   Birdemic: Shock and Terror   

                                               overview release_date  \
0     Raj is a rich, carefree, happy-go-lucky second...   1995-10-20   
1     Professor Gabriel Emerson finally learns the t...   2020-07-31   
2     Framed in the 1940s for the double murder of h...   1994-09-23   
3     Spanning the years 1945 to 1955, a chronicle o...   1972-03-14   
4     The final part of the film adaption of the ero...   2020-11-19   
...                                                 ...          ...   
8546  The filmmaking team behind the hits "Scary Mov...   2008-08-29   
8547  In the year 3000, man is no match for the Psyc...   2000-05-12   
8548  The young warrior Son Goku sets out on a quest...   2009-03-12   
8549  Set on an island off the coast, a techno rave ...   2003-04-11   
8550  A platoon of eagles and vultures attacks the r...   2010-02-27   

      popularity  vote_average  vote_count  
0         18.433           8.7        2763  
1          8.4
... [Output truncated for brevity]
```

```python
df.shape
```

**Execution Output:**
```text
(8551, 7)
```

```python
df.to_csv('movies.csv')
```

---

## Key Interview Concepts: Production API Ingestion

### 1. Multi-Page Pagination Best Practices
When collecting data across hundreds or thousands of API pages:
1. **Never use `df.append()` in loops** (deprecated in modern Pandas due to $O(N^2)$ quadratic memory allocations).
2. **Collect dictionaries or small DataFrames in a Python list**, then concatenate once with `pd.concat(list_of_dfs, ignore_index=True)`:
```python
import requests
import pandas as pd
import time

all_records = []
total_pages = 50

for page in range(1, total_pages + 1):
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key=API_KEY&language=en-US&page={page}"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        all_records.extend(results)
    elif response.status_code == 429:
        # Rate limit hit: exponential backoff
        time.sleep(2)
    else:
        break

df = pd.DataFrame(all_records)[['id', 'title', 'overview', 'release_date', 'popularity', 'vote_average', 'vote_count']]
df.to_csv('movies_consolidated.csv', index=False)
```

### 2. Error Handling & Rate Limiting
- **Status Code Validation**: Always check `response.raise_for_status()` or inspect `response.status_code`.
- **Timeouts**: Always set `requests.get(url, timeout=10)` to prevent worker thread hangs.
- **Rate Limits**: Handle HTTP 429 (Too Many Requests) with retry logic (`urllib3.util.retry.Retry` or `tenacity`).
