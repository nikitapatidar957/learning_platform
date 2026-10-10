# Day 15: Working with CSV Files in Pandas (16 Parameters Mastery)

Master high-performance CSV ingestion in Pandas using `pd.read_csv()`: custom delimiters (`sep`), headers, selective columns (`usecols`), data type optimization (`dtype`), date parsing (`parse_dates`), handling corrupted rows (`on_bad_lines`), and memory-efficient chunk loading (`chunksize`).

---

## 1. Complete Hands-on Guide & Parameter Walkthrough

# CSV Handling Quick Notes

This notebook covers different ways to read and work with CSV files using pandas.

## 1. Importing pandas
Definition: Import the pandas library so we can work with DataFrames.

```python
import pandas as pd
```

Example output:
```python
# No output, just library is loaded and available for use.
```

## 2. Opening a local CSV file
Definition: Read a CSV file stored on your computer into a DataFrame.

```python
df = pd.read_csv('aug_train.csv')
df.head()
```

Example output:
```text
   enrollee_id  city  ...  target
0          1001   23  ...       1
1          1002   13  ...       0
2          1003   17  ...       1
```

## 3. Opening a CSV file from a URL
Definition: Read CSV data directly from an online source using requests and StringIO.

```python
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
```

Example output:
```text
    Country  Region  Population
0  USA      North   331000000
1  India    Asia    1400000000
```

## 4. sep parameter
Definition: Use `sep` when the file is separated by a character other than a comma, like tabs.

```python
pd.read_csv('movie_titles_metadata.tsv', sep='\t')
```

Example output:
```text
   sno  name                 release_year  rating  votes  genres
0  1   Toy Story            1995          8.3     1000   Animation
```

## 5. index_col parameter
Definition: Set one column as the DataFrame index.

```python
pd.read_csv('aug_train.csv', index_col='enrollee_id')
```

Example output:
```text
              city  gender  education_level
enrollee_id
1001          23     Male    Masters
1002          13     Female  Graduate
```

## 6. header parameter
Definition: Tell pandas which row is the header row.

```python
pd.read_csv('test.csv', header=1)
```

Example output:
```text
   row2_value  row2_value2
0  value1     value2
1  value3     value4
```

## 7. usecols parameter
Definition: Load only selected columns from a large CSV file.

```python
pd.read_csv('aug_train.csv', usecols=['enrollee_id', 'gender', 'education_level'])
```

Example output:
```text
   enrollee_id  gender  education_level
0  1001        Male    Masters
1  1002        Female  Graduate
```

## 8. squeeze parameter
Definition: Convert a single-column DataFrame into a Series.

```python
pd.read_csv('aug_train.csv', usecols=['gender'], squeeze=True)
```

Example output:
```text
0      Male
1      Female
2      Male
3      NaN
Name: gender, dtype: object
```

## 9. skiprows / nrows parameter
Definition: Skip rows at the top and limit how many rows to read.

```python
pd.read_csv('aug_train.csv', nrows=100)
```

Example output:
```text
   enrollee_id  city  ...
0  1001        23   ...
1  1002        13   ...
...
99 1100       10   ...
```

## 10. encoding parameter
Definition: Use the correct text encoding when a file contains special characters.

```python
pd.read_csv('zomato.csv', encoding='latin-1')
```

Example output:
```text
   restaurant_id  name              cuisine
0  1             Cafe Moon        Italian
1  2             La Pasta         Pasta
```

## 11. Skip bad lines
Definition: Ignore rows that cannot be parsed correctly.

```python
pd.read_csv('BX-Books.csv', sep=';', encoding='latin-1', error_bad_lines=False)
```

Example output:
```text
   book_id  title                 author
0  101      Clean Code           Robert C. Martin
```

## 12. dtypes parameter
Definition: Force specific columns to have a certain data type.

```python
pd.read_csv('aug_train.csv', dtype={'target': int}).info()
```

Example output:
```text
Data columns (total 9 columns):
#   Column      Non-Null Count  Dtype
0  target      9000 non-null   int64
```

## 13. Handling Dates
Definition: Parse date columns automatically so pandas treats them as datetime values.

```python
pd.read_csv('IPL Matches 2008-2020.csv', parse_dates=['date']).info()
```

Example output:
```text
date    datetime64[ns]
```

## 14. Converters
Definition: Apply a custom function to a column while reading the CSV.

```python
pd.read_csv('IPL Matches 2008-2020.csv', converters={'team1': rename})
```

Example output:
```text
      team1        team2
0     RCB          Mumbai Indians
1     CSK          Delhi Capitals
```

## 15. na_values parameter
Definition: Treat specified values as missing values (NaN).

```python
pd.read_csv('aug_train.csv', na_values=['Male'])
```

Example output:
```text
   gender
0  NaN
1  Female
2  NaN
```

## 16. Loading a huge dataset in chunks
Definition: Read a very large dataset in smaller parts to save memory.

```python
dfs = pd.read_csv('aug_train.csv', chunksize=5000)
for chunk in dfs:
    print(chunk.shape)
```

Example output:
```text
(5000, 10)
(5000, 10)
(3000, 10)
```

### Summary
Pandas makes CSV reading easy with parameters like `sep`, `header`, `index_col`, `usecols`, `dtype`, and `parse_dates`. These options help us handle real-world datasets efficiently.

# 1. Importing pandas

```python
# !pip install pandas
```

**Execution Output:**
```text
Collecting pandas
  Downloading pandas-3.0.6-cp312-cp312-macosx_11_0_arm64.whl.metadata (79 kB)
Requirement already satisfied: numpy>=1.26.0 in /opt/miniconda3/envs/data-science/lib/python3.12/site-packages (from pandas) (2.5.3)
Requirement already satisfied: python-dateutil>=2.8.2 in /opt/miniconda3/envs/data-science/lib/python3.12/site-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in /opt/miniconda3/envs/data-science/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)
Downloading pandas-3.0.6-cp312-cp312-macosx_11_0_arm64.whl (10.1 MB)
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m10.1/10.1 MB[0m [31m668.1 kB/s[0m  [33m0:00:15[0mm0:00:01[0m0:01[0m
[?25hInstalling collected packages: pandas
Successfully installed pandas-3.0.6
```

```python
import pandas as pd
```

# 2. Opening a local csv file

```python
df = pd.read_csv('aug_train.csv')
df
```

**Execution Output:**
```text
enrollee_id      city  city_development_index gender  \
0             8949  city_103                   0.920   Male   
1            29725   city_40                   0.776   Male   
2            11561   city_21                   0.624    NaN   
3            33241  city_115                   0.789    NaN   
4              666  city_162                   0.767   Male   
...            ...       ...                     ...    ...   
19153         7386  city_173                   0.878   Male   
19154        31398  city_103                   0.920   Male   
19155        24576  city_103                   0.920   Male   
19156         5756   city_65                   0.802   Male   
19157        23834   city_67                   0.855    NaN   

           relevent_experience enrolled_university education_level  \
0      Has relevent experience       no_enrollment        Graduate   
1       No relevent experience       no_enrollment        Graduate   
2       No relevent experience    Full time course        Graduate   
3       No relevent experience                 NaN        Graduate   
4      Has relevent experience       no_enrollment         Masters   
...                        ...                 ...             ...   
19153   No relevent experience       no_enrollment        Graduate   
19154  Has relevent experience       no_enrollment        Graduate   
19155  Has relevent experience       no_enrollment        Graduate   
19156  Has relevent experience       no_enrollment
... [Output truncated for brevity]
```

```python
df = pd.read_csv('aug_train.csv')
df
```

**Execution Output:**
```text
enrollee_id      city  city_development_index gender  \
0             8949  city_103                   0.920   Male   
1            29725   city_40                   0.776   Male   
2            11561   city_21                   0.624    NaN   
3            33241  city_115                   0.789    NaN   
4              666  city_162                   0.767   Male   
...            ...       ...                     ...    ...   
19153         7386  city_173                   0.878   Male   
19154        31398  city_103                   0.920   Male   
19155        24576  city_103                   0.920   Male   
19156         5756   city_65                   0.802   Male   
19157        23834   city_67                   0.855    NaN   

           relevent_experience enrolled_university education_level  \
0      Has relevent experience       no_enrollment        Graduate   
1       No relevent experience       no_enrollment        Graduate   
2       No relevent experience    Full time course        Graduate   
3       No relevent experience                 NaN        Graduate   
4      Has relevent experience       no_enrollment         Masters   
...                        ...                 ...             ...   
19153   No relevent experience       no_enrollment        Graduate   
19154  Has relevent experience       no_enrollment        Graduate   
19155  Has relevent experience       no_enrollment        Graduate   
19156  Has relevent experience       no_enrollment
... [Output truncated for brevity]
```

# 3. Opening a csv file from an URL

```python
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

pd.read_csv(data)
```

**Execution Output:**
```text
Country         Region
0      Algeria         AFRICA
1       Angola         AFRICA
2        Benin         AFRICA
3     Botswana         AFRICA
4      Burkina         AFRICA
..         ...            ...
189   Paraguay  SOUTH AMERICA
190       Peru  SOUTH AMERICA
191   Suriname  SOUTH AMERICA
192    Uruguay  SOUTH AMERICA
193  Venezuela  SOUTH AMERICA

[194 rows x 2 columns]
```

# 4. Sep Parameter

```python
pd.read_csv('movie_titles_metadata.tsv',sep='\t',names=['sno','name','release_year','rating','votes','genres'])
```

**Execution Output:**
```text
sno                        name release_year  rating     votes  \
0      m0  10 things i hate about you         1999     6.9   62847.0   
1      m1  1492: conquest of paradise         1992     6.2   10421.0   
2      m2                  15 minutes         2001     6.1   25854.0   
3      m3       2001: a space odyssey         1968     8.4  163227.0   
4      m4                     48 hrs.         1982     6.9   22289.0   
..    ...                         ...          ...     ...       ...   
612  m612                    watchmen         2009     7.8  135229.0   
613  m613                         xxx         2002     5.6   53505.0   
614  m614                       x-men         2000     7.4  122149.0   
615  m615          young frankenstein         1974     8.0   57618.0   
616  m616                   zulu dawn         1979     6.4    1911.0   

                                                genres  
0                                 ['comedy' 'romance']  
1          ['adventure' 'biography' 'drama' 'history']  
2                ['action' 'crime' 'drama' 'thriller']  
3                     ['adventure' 'mystery' 'sci-fi']  
4       ['action' 'comedy' 'crime' 'drama' 'thriller']  
..                                                 ...  
612  ['action' 'crime' 'fantasy' 'mystery' 'sci-fi'...  
613                     ['action' 'adventure' 'crime']  
614                                ['action' 'sci-fi']  
615                                ['comedy' 'sci-fi']  
616     ['acti
... [Output truncated for brevity]
```

# 5. Index_col parameter

```python
pd.read_csv('aug_train.csv',index_col='enrollee_id')
```

**Execution Output:**
```text
city  city_development_index gender      relevent_experience  \
enrollee_id                                                                     
8949         city_103                   0.920   Male  Has relevent experience   
29725         city_40                   0.776   Male   No relevent experience   
11561         city_21                   0.624    NaN   No relevent experience   
33241        city_115                   0.789    NaN   No relevent experience   
666          city_162                   0.767   Male  Has relevent experience   
...               ...                     ...    ...                      ...   
7386         city_173                   0.878   Male   No relevent experience   
31398        city_103                   0.920   Male  Has relevent experience   
24576        city_103                   0.920   Male  Has relevent experience   
5756          city_65                   0.802   Male  Has relevent experience   
23834         city_67                   0.855    NaN   No relevent experience   

            enrolled_university education_level major_discipline experience  \
enrollee_id                                                                   
8949              no_enrollment        Graduate             STEM        >20   
29725             no_enrollment        Graduate             STEM         15   
11561          Full time course        Graduate             STEM          5   
33241                       NaN        Graduate  Business Degree    
... [Output truncated for brevity]
```

# 6. Header parameter

```python
pd.read_csv('test.csv',header=1)
```

**Execution Output:**
```text
0  enrollee_id      city  city_development_index gender  \
0  1        29725   city_40                   0.776   Male   
1  2        11561   city_21                   0.624    NaN   
2  3        33241  city_115                   0.789    NaN   
3  4          666  city_162                   0.767   Male   

       relevent_experience enrolled_university education_level  \
0   No relevent experience       no_enrollment        Graduate   
1   No relevent experience    Full time course        Graduate   
2   No relevent experience                 NaN        Graduate   
3  Has relevent experience       no_enrollment         Masters   

  major_discipline experience company_size    company_type last_new_job  \
0             STEM         15        50-99         Pvt Ltd           >4   
1             STEM          5          NaN             NaN        never   
2  Business Degree         <1          NaN         Pvt Ltd        never   
3             STEM        >20        50-99  Funded Startup            4   

   training_hours  target  
0              47       0  
1              83       0  
2              52       1  
3               8       0
```

# 7. use_cols parameter

```python
pd.read_csv('aug_train.csv',usecols=['enrollee_id','gender','education_level'])
```

**Execution Output:**
```text
enrollee_id gender education_level
0             8949   Male        Graduate
1            29725   Male        Graduate
2            11561    NaN        Graduate
3            33241    NaN        Graduate
4              666   Male         Masters
...            ...    ...             ...
19153         7386   Male        Graduate
19154        31398   Male        Graduate
19155        24576   Male        Graduate
19156         5756   Male     High School
19157        23834    NaN  Primary School

[19158 rows x 3 columns]
```

# 8. Squeeze parameters

```python
pd.read_csv('aug_train.csv',usecols=['gender'],squeeze=True)
```

**Execution Output:**
```text
0        Male
1        Male
2         NaN
3         NaN
4        Male
         ... 
19153    Male
19154    Male
19155    Male
19156    Male
19157     NaN
Name: gender, Length: 19158, dtype: object
```

# 9. Skiprows/nrows Parameter

```python
pd.read_csv('aug_train.csv',nrows=100)
```

**Execution Output:**
```text
enrollee_id      city  city_development_index gender  \
0          8949  city_103                   0.920   Male   
1         29725   city_40                   0.776   Male   
2         11561   city_21                   0.624    NaN   
3         33241  city_115                   0.789    NaN   
4           666  city_162                   0.767   Male   
..          ...       ...                     ...    ...   
95        12081   city_65                   0.802   Male   
96         7364  city_160                   0.920    NaN   
97        11184   city_74                   0.579    NaN   
98         7016   city_65                   0.802   Male   
99         8695   city_11                   0.550   Male   

        relevent_experience enrolled_university education_level  \
0   Has relevent experience       no_enrollment        Graduate   
1    No relevent experience       no_enrollment        Graduate   
2    No relevent experience    Full time course        Graduate   
3    No relevent experience                 NaN        Graduate   
4   Has relevent experience       no_enrollment         Masters   
..                      ...                 ...             ...   
95  Has relevent experience    Full time course        Graduate   
96   No relevent experience    Full time course     High School   
97   No relevent experience    Full time course        Graduate   
98  Has relevent experience       no_enrollment        Graduate   
99  Has relevent experience       no_enrollmen
... [Output truncated for brevity]
```

# 10. Encoding parameter

```python
pd.read_csv('zomato.csv',encoding='latin-1')
```

**Execution Output:**
```text
Restaurant ID           Restaurant Name  Country Code              City  \
0           6317637          Le Petit Souffle           162       Makati City   
1           6304287          Izakaya Kikufuji           162       Makati City   
2           6300002    Heat - Edsa Shangri-La           162  Mandaluyong City   
3           6318506                      Ooma           162  Mandaluyong City   
4           6314302               Sambo Kojin           162  Mandaluyong City   
...             ...                       ...           ...               ...   
9546        5915730              NamlÛ± Gurme           208         ÛÁstanbul   
9547        5908749             Ceviz AÛôacÛ±           208         ÛÁstanbul   
9548        5915807                     Huqqa           208         ÛÁstanbul   
9549        5916112              Aôôk Kahve           208         ÛÁstanbul   
9550        5927402  Walter's Coffee Roastery           208         ÛÁstanbul   

                                                Address  \
0     Third Floor, Century City Mall, Kalayaan Avenu...   
1     Little Tokyo, 2277 Chino Roces Avenue, Legaspi...   
2     Edsa Shangri-La, 1 Garden Way, Ortigas, Mandal...   
3     Third Floor, Mega Fashion Hall, SM Megamall, O...   
4     Third Floor, Mega Atrium, SM Megamall, Ortigas...   
...                                                 ...   
9546  Kemankeô Karamustafa Paôa Mahallesi, RÛ±htÛ±...   
9547  Koôuyolu Mahallesi, Muhittin íìstí_ndaÛô Cadd...   
95
... [Output truncated for brevity]
```

# 11. Skip bad lines

```python
pd.read_csv('BX-Books.csv', sep=';', encoding="latin-1",error_bad_lines=False)
```

**Execution Output:**
```text
ISBN                                         Book-Title  \
0       0195153448                                Classical Mythology   
1       0002005018                                       Clara Callan   
2       0060973129                               Decision in Normandy   
3       0374157065  Flu: The Story of the Great Influenza Pandemic...   
4       0393045218                             The Mummies of Urumchi   
...            ...                                                ...   
271355  0440400988                         There's a Bat in Bunk Five   
271356  0525447644                            From One to One Hundred   
271357  006008667X  Lily Dale : The True Story of the Town that Ta...   
271358  0192126040                        Republic (World's Classics)   
271359  0767409752  A Guided Tour of Rene Descartes' Meditations o...   

                 Book-Author Year-Of-Publication  \
0         Mark P. O. Morford                2002   
1       Richard Bruce Wright                2001   
2               Carlo D'Este                1991   
3           Gina Bari Kolata                1999   
4            E. J. W. Barber                1999   
...                      ...                 ...   
271355        Paula Danziger                1988   
271356            Teri Sloat                1991   
271357      Christine Wicker                2004   
271358                 Plato                1996   
271359   Christopher  Biffle                2000   

            
... [Output truncated for brevity]
```

# 12. dtypes parameter

```python
pd.read_csv('aug_train.csv',dtype={'target':int}).info()
```

**Execution Output:**
```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 19158 entries, 0 to 19157
Data columns (total 14 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   enrollee_id             19158 non-null  int64  
 1   city                    19158 non-null  object 
 2   city_development_index  19158 non-null  float64
 3   gender                  14650 non-null  object 
 4   relevent_experience     19158 non-null  object 
 5   enrolled_university     18772 non-null  object 
 6   education_level         18698 non-null  object 
 7   major_discipline        16345 non-null  object 
 8   experience              19093 non-null  object 
 9   company_size            13220 non-null  object 
 10  company_type            13018 non-null  object 
 11  last_new_job            18735 non-null  object 
 12  training_hours          19158 non-null  int64  
 13  target                  19158 non-null  int32  
dtypes: float64(1), int32(1), int64(2), object(10)
memory usage: 2.0+ MB
```

# 13. Handling Dates

```python
pd.read_csv('IPL Matches 2008-2020.csv',parse_dates=['date']).info()
```

**Execution Output:**
```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 816 entries, 0 to 815
Data columns (total 17 columns):
 #   Column           Non-Null Count  Dtype         
---  ------           --------------  -----         
 0   id               816 non-null    int64         
 1   city             803 non-null    object        
 2   date             816 non-null    datetime64[ns]
 3   player_of_match  812 non-null    object        
 4   venue            816 non-null    object        
 5   neutral_venue    816 non-null    int64         
 6   team1            816 non-null    object        
 7   team2            816 non-null    object        
 8   toss_winner      816 non-null    object        
 9   toss_decision    816 non-null    object        
 10  winner           812 non-null    object        
 11  result           812 non-null    object        
 12  result_margin    799 non-null    float64       
 13  eliminator       812 non-null    object        
 14  method           19 non-null     object        
 15  umpire1          816 non-null    object        
 16  umpire2          816 non-null    object        
dtypes: datetime64[ns](1), float64(1), int64(2), object(13)
memory usage: 108.5+ KB
```

```python
def rename(name):
    if name == "Royal Challengers Bangalore":
        return "RCB"
    else:
        return name
```

```python
rename("Royal Challengers Bangalore")
```

**Execution Output:**
```text
'RCB'
```

# 14. Convertors

```python
pd.read_csv('IPL Matches 2008-2020.csv',converters={'team1':rename})
```

**Execution Output:**
```text
id        city        date player_of_match  \
0     335982   Bangalore  2008-04-18     BB McCullum   
1     335983  Chandigarh  2008-04-19      MEK Hussey   
2     335984       Delhi  2008-04-19     MF Maharoof   
3     335985      Mumbai  2008-04-20      MV Boucher   
4     335986     Kolkata  2008-04-20       DJ Hussey   
..       ...         ...         ...             ...   
811  1216547       Dubai  2020-09-28  AB de Villiers   
812  1237177       Dubai  2020-11-05       JJ Bumrah   
813  1237178   Abu Dhabi  2020-11-06   KS Williamson   
814  1237180   Abu Dhabi  2020-11-08      MP Stoinis   
815  1237181       Dubai  2020-11-10        TA Boult   

                                          venue  neutral_venue  \
0                         M Chinnaswamy Stadium              0   
1    Punjab Cricket Association Stadium, Mohali              0   
2                              Feroz Shah Kotla              0   
3                              Wankhede Stadium              0   
4                                  Eden Gardens              0   
..                                          ...            ...   
811         Dubai International Cricket Stadium              0   
812         Dubai International Cricket Stadium              0   
813                        Sheikh Zayed Stadium              0   
814                        Sheikh Zayed Stadium              0   
815         Dubai International Cricket Stadium              0   

                     team1                  
... [Output truncated for brevity]
```

# 15. na_values parameter

```python
pd.read_csv('aug_train.csv',na_values=['Male',])
```

**Execution Output:**
```text
enrollee_id      city  city_development_index gender  \
0             8949  city_103                   0.920   Male   
1            29725   city_40                   0.776   Male   
2            11561   city_21                   0.624    NaN   
3            33241  city_115                   0.789    NaN   
4              666  city_162                   0.767   Male   
...            ...       ...                     ...    ...   
19153         7386  city_173                   0.878   Male   
19154        31398  city_103                   0.920   Male   
19155        24576  city_103                   0.920   Male   
19156         5756   city_65                   0.802   Male   
19157        23834   city_67                   0.855    NaN   

           relevent_experience enrolled_university education_level  \
0      Has relevent experience       no_enrollment        Graduate   
1       No relevent experience       no_enrollment        Graduate   
2       No relevent experience    Full time course        Graduate   
3       No relevent experience                 NaN        Graduate   
4      Has relevent experience       no_enrollment         Masters   
...                        ...                 ...             ...   
19153   No relevent experience       no_enrollment        Graduate   
19154  Has relevent experience       no_enrollment        Graduate   
19155  Has relevent experience       no_enrollment        Graduate   
19156  Has relevent experience       no_enrollment
... [Output truncated for brevity]
```

# 16. Loading a huge dataset in chunks

```python
dfs = pd.read_csv('aug_train.csv',chunksize=5000)
```

```python
for chunks in dfs:
    print(chunk.shape)
```

**Execution Output:**
```text
(4158, 14)
(4158, 14)
(4158, 14)
(4158, 14)
```

---

## Key Interview Concepts & Production Ingestion Best Practices

### 1. The 16 Core Parameters of `pd.read_csv()`
| Parameter | Primary Purpose | Production Use Case |
| :--- | :--- | :--- |
| `filepath_or_buffer` | Path or URL | Load local paths or remote URLs directly via `StringIO` |
| `sep` | Column delimiter | Handles TSVs (`\t`), semicolons (`;`), or pipes (`\|`) |
| `header` | Header row index | Set `header=1` or `header=None` when data starts after metadata |
| `names` | Custom column names | Provide meaningful column names when CSV lacks header |
| `index_col` | Index column | Set primary ID column as DataFrame index without duplicating memory |
| `usecols` | Selective column loading | **Drastically saves RAM** by reading only needed features |
| `squeeze` | Dimension reduction | Converts single-column DataFrame to `pd.Series` |
| `nrows` | Row limit | Quick EDA and schema validation on multi-GB datasets |
| `skiprows` | Skip initial rows | Skip metadata or license headers |
| `encoding` | Character encoding | Fix `UnicodeDecodeError` using `'latin-1'`, `'iso-8859-1'`, or `'utf-8'` |
| `error_bad_lines` / `on_bad_lines` | Corrupted row handling | Use `on_bad_lines='skip'` to ignore rows with extra fields |
| `dtype` | Explicit data typing | Downcast types (`int64` $\to$ `int32`, `float64` $\to$ `float32`, `object` $\to$ `'category'`) |
| `parse_dates` | Datetime parsing | Automatically parses string dates into `datetime64[ns]` |
| `converters` | On-the-fly transformations | Clean values during ingestion using dictionary of functions |
| `na_values` | Custom null indicators | Specify strings like `'N/A'`, `'?'`, `'missing'`, `'-'` as `np.nan` |
| `chunksize` | Stream-based chunk loading | Stream massive datasets that exceed physical RAM |

### 2. Interview Question: How do you read a 50 GB CSV file with only 8 GB of RAM?
**Answer**:
1. **Selective Columns (`usecols`)**: Never load unused columns into memory.
2. **Type Downcasting (`dtype`)**: Cast string categories to `'category'` and large integers to `int32`/`int16`.
3. **Iterative Chunk Processing (`chunksize`)**:
```python
chunk_size = 50_000
total_records = 0
for chunk in pd.read_csv('huge_dataset.csv', chunksize=chunk_size, usecols=['id', 'amount', 'category']):
    # Process or aggregate chunk in-place
    total_records += len(chunk)
```
