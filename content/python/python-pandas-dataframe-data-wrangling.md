# Python Pandas: DataFrames, Series & Data Wrangling

Mastering Pandas Series and DataFrames, creating tables from dictionaries and lists, head/tail inspection, dropping columns and duplicates, missing value handling, column renaming, indexing, and resetting indices.

---

# 10_Python_Pandas_Module


## Introduction 👋

### What is Pandas in Python?
[![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/) is the most famous python library providing fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, **real world** data analysis in Python. Additionally, it has the broader goal of becoming **the most powerful and flexible open source data analysis / manipulation tool available in any language**. It is already well on its way towards this goal.

In Pandas, the data is usually utilized to support the statistical analysis in **SciPy**, plotting functions from **Matplotlib**, and machine learning algorithms in **Scikit-learn**.


## Main Features
Here are just a few of the things that pandas does well:

  - Easy handling of [**missing data**][missing-data] (represented as `NaN`) in floating point as well as non-floating point data
  - Size mutability: columns can be [**inserted and deleted**][insertion-deletion] from DataFrame and higher dimensional objects
  - Automatic and explicit [**data alignment**][alignment]: objects can be explicitly aligned to a set of labels, or the user can simply
    ignore the labels and let `Series`, `DataFrame`, etc. automatically align the data for you in computations
  - Powerful, flexible [**group by**][groupby] functionality to perform split-apply-combine operations on data sets, for both aggregating
    and transforming data
  - Make it [**easy to convert**][conversion] ragged, differently-indexed data in other Python and NumPy data structures
    into DataFrame objects
  - Intelligent label-based [**slicing**][slicing], [**fancy indexing**][fancy-indexing], and [**subsetting**][subsetting] of
    large data sets
  - Intuitive [**merging**][merging] and [**joining**][joining] datasets
  - Flexible [**reshaping**][reshape] and [**pivoting**][pivot-table] of datasets
  - [**Hierarchical**][mi] labeling of axes (possible to have multiple labels per tick)
  - Robust IO tools for loading data from [**flat files**][flat-files] (CSV and delimited), [**Excel files**][excel], [**databases**][db],
    and saving/loading data from the ultrafast [**HDF5 format**][hdfstore]
  - [**Time series**][timeseries]-specific functionality: date range generation and frequency conversion, moving window statistics,
    moving window linear regressions, date shifting and lagging, etc.


   [missing-data]: https://pandas.pydata.org/pandas-docs/stable/missing_data.html#working-with-missing-data
   [insertion-deletion]: https://pandas.pydata.org/pandas-docs/stable/dsintro.html#column-selection-addition-deletion
   [alignment]: https://pandas.pydata.org/pandas-docs/stable/dsintro.html?highlight=alignment#intro-to-data-structures
   [groupby]: https://pandas.pydata.org/pandas-docs/stable/groupby.html#group-by-split-apply-combine
   [conversion]: https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe
   [slicing]: https://pandas.pydata.org/pandas-docs/stable/indexing.html#slicing-ranges
   [fancy-indexing]: https://pandas.pydata.org/pandas-docs/stable/indexing.html#advanced-indexing-with-ix
   [subsetting]: https://pandas.pydata.org/pandas-docs/stable/indexing.html#boolean-indexing
   [merging]: https://pandas.pydata.org/pandas-docs/stable/merging.html#database-style-dataframe-joining-merging
   [joining]: https://pandas.pydata.org/pandas-docs/stable/merging.html#joining-on-index
   [reshape]: https://pandas.pydata.org/pandas-docs/stable/reshaping.html#reshaping-and-pivot-tables
   [pivot-table]: https://pandas.pydata.org/pandas-docs/stable/reshaping.html#pivot-tables-and-cross-tabulations
   [mi]: https://pandas.pydata.org/pandas-docs/stable/indexing.html#hierarchical-indexing-multiindex
   [flat-files]: https://pandas.pydata.org/pandas-docs/stable/io.html#csv-text-files
   [excel]: https://pandas.pydata.org/pandas-docs/stable/io.html#excel-files
   [db]: https://pandas.pydata.org/pandas-docs/stable/io.html#sql-queries
   [hdfstore]: https://pandas.pydata.org/pandas-docs/stable/io.html#hdf5-pytables
   [timeseries]: https://pandas.pydata.org/pandas-docs/stable/timeseries.html#time-series-date-functionality


### Core Components of Pandas Data Structure
Pandas have two core data structure components, and all operations are based on those two objects. Organizing data in a particular way is known as a data structure. Here are the two pandas data structures:

* **Series**
* **DataFrame**

---

## Table of contents 📋

| **No.** | **Name** | 
| ------- | -------- | 
| 01 | **[Python_Pandas_DataFrame](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/001_Python_Pandas_DataFrame.ipynb)** |
|    | 1.1 **[001_Python_Pandas_DataFrame_from_Dictionary](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/001_Python_Pandas_Methods/001_Python_Pandas_DataFrame_from_Dictionary.ipynb)** |
|    | 1.2 **[Python_Pandas_DataFrame_from_List](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/001_Python_Pandas_Methods/002_Python_Pandas_DataFrame_from_List.ipynb)** |
|    | 1.3 **[Python_Pandas_DataFrame_head()_and_tail()](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/001_Python_Pandas_Methods/003_Python_Pandas_DataFrame_head()_and_tail().ipynb)** |
|    | 1.4 **[004_Python_Pandas_DataFrame_drop_columns](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/001_Python_Pandas_Methods/004_Python_Pandas_DataFrame_drop_columns.ipynb)** |
|    | 1.5 **[Python_Pandas_DataFrame_drop_duplicates](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/001_Python_Pandas_Methods/005_Python_Pandas_DataFrame_drop_duplicates.ipynb)** |
|    | 1.6 **[Python_Pandas_DataFrame_drop_columns_with_NA](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/001_Python_Pandas_Methods/006_Python_Pandas_DataFrame_drop_columns_with_NA.ipynb)** |
|    | 1.7 **[Python_Pandas_DataFrame_rename_columns](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/001_Python_Pandas_Methods/007_Python_Pandas_DataFrame_rename_columns.ipynb)** |
|    | 1.8 **[Python_Pandas_DataFrame_to_Python_dictionary](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/001_Python_Pandas_Methods/008_Python_Pandas_DataFrame_to_Python_dictionary.ipynb)** |
|    | 1.9 **[Python_Pandas_DataFrame_set_index](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/001_Python_Pandas_Methods/009_Python_Pandas_DataFrame_set_index.ipynb)** |
|    | 1.10 **[Python_Pandas_DataFrame_reset_index](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/001_Python_Pandas_Methods/010_Python_Pandas_DataFrame_reset_index.ipynb)** |
| 02 | **[Python_Pandas_Exercise_1](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/002_Python_Pandas_Exercise_1.ipynb)** |
| 03 | **[Python_Pandas_Exercise_2](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/003_Python_Pandas_Exercise_2.ipynb)** |
|    | **[automobile_data.csv](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/automobile_data.csv)** |
|    | **[pokemon_data.csv](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/pokemon_data.csv)** |
| 04 | **[Pandas Cheat Sheet Data Wrangling in Python.pdf](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/Pandas%20Cheat%20Sheet%20Data%20Wrangling%20in%20Python.pdf)** |
| 05 | **[Pandas Cheat Sheet for Data Science in Python.pdf](https://github.com/milaan9/10_Python_Pandas_Module/blob/main/Pandas%20Cheat%20Sheet%20for%20Data%20Science%20in%20Python.pdf)** |

These are online **read-only** versions. However you can **`Run ▶`**  all the codes **online** by clicking here ➞ 

---

## Install Pandas Module:

Open your [![Anaconda](https://img.shields.io/badge/Anaconda-342B029.svg?&style=flate&logo=anaconda&logoColor=white)](https://www.anaconda.com/products/individual) Prompt <img alt="propmt" src="https://img.shields.io/badge/-__-000000?style=flat-square&logo=Plex&logoColor=white"> and type and run the following command (individually):

 -       pip install pandas  
 

Once Installed now we can import it inside our python code.

---  

## Frequently asked questions ❔

### How can I thank you for writing and sharing this tutorial? 🌷

You can <img src="https://img.shields.io/static/v1?label=%E2%AD%90 Star &message=if%20useful&style=style=flat&color=blue" alt="Star Badge"/> and <img src="https://img.shields.io/static/v1?label=%E2%B5%96 Fork &message=if%20useful&style=style=flat&color=blue" alt="Fork Badge"/> Starring and Forking is free for you, but it tells me and other people that it was helpful and you like this tutorial.

Go [**`here`**](https://github.com/milaan9/10_Python_Pandas_Module) if you aren't here already and click ➞ **`✰ Star`** and **`ⵖ Fork`** button in the top right corner. You'll be asked to create a GitHub account if you don't already have one.

---

### How can I read this tutorial without an Internet connection? <img alt="GIF" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/hmm.gif" width="20" />

1. Go [**`here`**](https://github.com/milaan9/10_Python_Pandas_Module) and click the big green ➞ **`Code`** button in the top right of the page, then click ➞ [**`Download ZIP`**](https://github.com/milaan9/10_Python_Pandas_Module/archive/refs/heads/main.zip).

    ![Download ZIP](img/dnld_rep.png)

2. Extract the ZIP and open it. Unfortunately I don't have any more specific instructions because how exactly this is done depends on which operating system you run.
    
3. Launch ipython notebook from the folder which contains the notebooks. Open each one of them
  
    **`Kernel > Restart & Clear Output`**
    
This will clear all the outputs and now you can understand each statement and learn interactively.

If you have git and you know how to use it, you can also clone the repository instead of downloading a zip and extracting it. An advantage with doing it this way is that you don't need to download the whole tutorial again to get the latest version of it, all you need to do is to pull with git and run ipython notebook again.

---

## Authors ✍️

I'm Dr. Milaan Parmar and I have written this tutorial. If you think you can add/correct/edit and enhance this tutorial you are most welcome🙏

See [github's contributors page](https://github.com/milaan9/10_Python_Pandas_Module/graphs/contributors) for details.

If you have trouble with this tutorial please tell me about it by [Create an issue on GitHub](https://github.com/milaan9/10_Python_Pandas_Module/issues/new). and I'll make this tutorial better. This is probably the best choice if you had trouble following the tutorial, and something in it should be explained better. You will be asked to create a GitHub account if you don't already have one.

If you like this tutorial, please [give it a ⭐ star](https://github.com/milaan9/10_Python_Pandas_Module).

---

## Licence 📜

You may use this tutorial freely at your own risk. See [LICENSE](./LICENSE).

---

## 📘 Python Pandas Dataframe From Dictionary
*Source: `7. Python Pandas/1. Python Pandas DataFrame from Dictionary.ipynb`*

# Create Pandas DataFrame from Python Dictionary

In this class shows how to convert a **Python dictionary** to **Pandas DataFrame**. It covers the creating DataFrame from all types of dictionaries using the DataFrame constructor and **`from_dict()`** method.

And at the end of this class, we summarize the usage of both ways with the comparison. So please stay till the end.

Python dictionary is the data structure that stores the data in key-value pairs. By converting data from dictionary format to DataFrame will make it very competent for analysis by using functions of DataFrame.

There are multiple ways to convert Python dictionary object into Pandas DataFrame. Majorly used ways are,

1. DataFrame constructor
2. **`from_dict()`**

## Create DataFrame from dict using constructor

**DataFrame constructor** can be used to create DataFrame from different data structures in python like dict, list, set, tuple, and ndarray.

**Example:** 

We create a DataFrame object using dictionary objects contain student data.

<div>

</div>

```python
import pandas as pd

# Create dict object
student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}
print(student_dict)

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)
```

**Output:**
```text
{'name': ['Joe', 'Nat', 'Harry'], 'age': [20, 21, 19], 'marks': [85.1, 77.8, 91.54]}
    name  age  marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
```

>**Note:** When you convert a **`dict`** to DataFrame by default,  all the keys of the **`dict`** object becomes columns, and the range of numbers 0, 1, 2,…,n is assigned as a row index.

## DataFrame from dict with required columns only

While converting the whole **`dict`** to DataFrame, we may need only some of the columns to be included in the resulting DataFrame.

We can select only required columns by passing list column labels to **`columns=['col1', 'col2']`** parameter in the constructor.

**Example:**

In the case of student DataFrame for analyzing the annual score, we need only student **`name`** and **`marks`** whereas the **`age`** column is not required. We can select only required columns, as shown in the below example.

```python
import pandas as pd

# Create dict object
student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}
print(student_dict)

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict, columns=["name", "marks"])
print(student_df)
```

**Output:**
```text
{'name': ['Joe', 'Nat', 'Harry'], 'age': [20, 21, 19], 'marks': [85.1, 77.8, 91.54]}
    name  marks
0    Joe  85.10
1    Nat  77.80
2  Harry  91.54
```

## DataFrame from dict with user-defined indexes

In pandas DataFrame, each row has an index that is used to identify each row. In some cases, we need to provide a customized index for each row. We can do that while creating the DataFrame from **`dict`** using the **`index`** parameter of the DataFrame constructor.

The default index is a range of integers starting from 0 to a number of rows. We can pass a list of the row indexes as **`index=['index1','index2']`** to the dataFrame constructor.

**Example:**

In the below example, we have given a customer index for each student, making it more readable and easy to access the row using it.

```python
# import pandas library
import pandas as pd

# Create dict object
student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}
print(student_dict)

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict, index=["stud1", "stud2", "stud3"])
print(student_df)
```

**Output:**
```text
{'name': ['Joe', 'Nat', 'Harry'], 'age': [20, 21, 19], 'marks': [85.1, 77.8, 91.54]}
        name  age  marks
stud1    Joe   20  85.10
stud2    Nat   21  77.80
stud3  Harry   19  91.54
```

## DataFrame from dict by changing the column data type

By default, while creating a DataFrame from **`dict`** using constructor, it keeps the original data type of the values in dict. But, if we need to change the data type of the data in the resulting DataFrame, we can use the **`dtype`** parameter in the constructor.

Only one data type is allowed to specify as **`dtype='data_type'`** which will be applicable for all the data in the resultant DataFrame. If we do not force such a data type, it internally infers from the Data.

**Example:**

As you can see below example, we are trying to change the data type to **float64** for all the columns. But, it changes the data type of **`age`** and **`marks`** columns only to **float64** even though the **`marks`** column type was **`object`**. But, the **`name`** column type is not changed because string values in that column cannot be converted to **float64**.

```python
# import pandas library
import pandas as pd

# Create dict object
student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": ["85", "77", "91.54"]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("DataFrame with inferred data type : \n", student_df.dtypes)

student_df = pd.DataFrame(student_dict, dtype="float64")
print("DataFrame with changed data type : \n", student_df.dtypes)

print(student_df)
```

**Output:**
```text
DataFrame with inferred data type : 
 name     object
age       int64
marks    object
dtype: object
DataFrame with changed data type : 
 name      object
age      float64
marks    float64
dtype: object
    name   age  marks
0    Joe  20.0  85.00
1    Nat  21.0  77.00
2  Harry  19.0  91.54
```

>**Note:** It changes the data type only if it is compatible with the new data type. Otherwise, it keeps the original data type.

```python
cars = pd.read_csv("automobile_data.csv")
print(cars)
```

**Output:**
```text
index      company   body-style  wheel-base  length engine-type  \
0       0  alfa-romero  convertible        88.6   168.8        dohc   
1       1  alfa-romero  convertible        88.6   168.8        dohc   
2       2  alfa-romero    hatchback        94.5   171.2        ohcv   
3       3         audi        sedan        99.8   176.6         ohc   
4       4         audi        sedan        99.4   176.6         ohc   
..    ...          ...          ...         ...     ...         ...   
56     81   volkswagen        sedan        97.3   171.7         ohc   
57     82   volkswagen        sedan        97.3   171.7         ohc   
58     86   volkswagen        sedan        97.3   171.7         ohc   
59     87        volvo        sedan       104.3   188.8         ohc   
60     88        volvo        wagon       104.3   188.8         ohc   

   num-of-cylinders  horsepower  average-mileage    price  
0              four         111               21  13495.0  
1              four         111
... [Output truncated for brevity]
```

## DataFrame from dict with a single value

If we have a **`dict`** with only single values for each key and need to convert such **`dict`** to the DataFrame, we can use the DataFrame constructor.

In such a case, it converts the **`dict`** to DataFrame as we have seen before, like keys of the **`dict`** will be column labels and values will be the column data. But, we must provide the index parameter to give the row index. Else it throws an error,

```python
ValueError: If using all scalar values, you must pass an index
```
**Example:**

In the below example, we have provided the customized **`index=['stud1']`** to the DataFrame.

```python
# import pandas library
import pandas as pd

# Create dict object
student_dict = {'name': 'Smith', 'age': 22, 'marks': 88.90}
print(student_dict)

student_df = pd.DataFrame(student_dict, index=['stud1'])
print(student_df)
```

**Output:**
```text
{'name': 'Smith', 'age': 22, 'marks': 88.9}
        name  age  marks
stud1  Smith   22   88.9
```

## DataFrame from dict with key and value as a column

Suppose we have a dictionary object where the key is the **student’s name**, and the value is the student’s marks. And we want the keys in one column and all the values in another column of the DataFrame.

For that, rather than passing a whole **`dict`** object, we need to pass each key-value pair in the dictionary to the DataFrame constructor to create a new DataFrame.

We can get the entry of key-value pair using **`dict.items()`** and pass that function to the constructor.

**Example:**

As shown in the below example, we need to pass an entry of key-value to the constructor and give **`column`** labels using columns parameter.

```python
import pandas as pd

# Create dict object
student_dict = {"Joe": 85.10, "Nat": 75.83, "Harry": 69.70}
print(student_dict)

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict.items(), columns=["name", "marks"])
print(student_df)
```

**Output:**
```text
{'Joe': 85.1, 'Nat': 75.83, 'Harry': 69.7}
    name  marks
0    Joe  85.10
1    Nat  75.83
2  Harry  69.70
```

## Create DataFrame from list of dict

For the sake of our understanding, consider the case where each school stores data of students into the dictionary data structure. Each school store different information about students. Like, some school stores student’s hobby whereas some school only stores academic information. If we want to analyze data of all the students from the city, we need to gather all this information into the DataFrame.

To convert such a list of **`dict`** from different schools can be converted to a single DataFrame using either **`DataFrame.from_dict()`** function or DataFrame constructor.

By default, keys of all the different dictionary objects are converted into columns of resultant DataFrame. It handles the missing keys by adding NaN where the values for the column are missing.

**Example:**

Let’s see how we can use a constructor to create DataFrame from different dictionary objects.

```python
import pandas as pd

# Create dict object
student_dict = [{"name": "Joe", "age": 20, "marks": "85.58", "hobby": "smimming"},
                {"name": "Nat", "age": 21, "marks": "77.21", },
                {"name": "Harry", "age": 19, "marks": "91.54"}]
print(student_dict)

# Create DataFrame object
student_df = pd.DataFrame(student_dict)
print(student_df)
```

**Output:**
```text
[{'name': 'Joe', 'age': 20, 'marks': '85.58', 'hobby': 'smimming'}, {'name': 'Nat', 'age': 21, 'marks': '77.21'}, {'name': 'Harry', 'age': 19, 'marks': '91.54'}]
    name  age  marks     hobby
0    Joe   20  85.58  smimming
1    Nat   21  77.21       NaN
2  Harry   19  91.54       NaN
```

## The `from_dict()` function

This is another way of creating DataFrame from a Python dictionary using **`DataFrame.from_dict() `** method.

>**Note:** This method is useful for the cases when you need to **transpose** the DataFrame i.e. when we need the keys in the dictionary object as rows in the resultant DataFrame. In all the other cases DataFrame constructor should be preferred.

**Syntax:**

```python
DataFrame.from_dict(data, orient='columns', dtype=None, columns=None)
```

**Parameters:**

1. **`data`**: It takes **`dict`**, **`list`**, **`set`**, **`ndarray`**, **`Iterable`**, or **`DataFrame`** as input. An empty DataFrame will be created if it is not provided. The resultant column order follows the insertion order.


2. **`orient`**: (Optional) If the keys of the **`dict`** should be the rows of the DataFrame, then set **`orient = index`** else set it to **`column (Default)`** if the keys should be columns of the resultant DataFrame.


3. **`dtype`**: (Optional) data type to force on resulting DataFrame. Only a single data type is allowed. If not given, then it’s inferred from the data.


4. **`columns`**: (Optional) **Only be used in case of** **`orient="index"`** to specify column labels in the resulting DataFrame. Default column labels are range of integer i.e. 0,1,2…n. 
>**Note:** If we use the **`columns`** parameter with **`orient='columns'`** it throws an **`ValueError: cannot use columns parameter with orient='columns'`**

## DataFrame from dict with dict keys as a row

It is used to transpose the DataFrame, i.e., when keys in the dictionary should be the rows in the resultant DataFrame. We can change the orientation of the DataFrame using a parameter **`orient="index"`** in **`DataFrame.from_dict()`**.

**Example:**

In the below example, keys **`name`**, **`age`**, and **`marks`** becomes row indexes in the DataFrame, and values are added in respective rows. New column labels are provided using **`columns`** parameter.

```python
import pandas as pd

# Create dict object
student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}
print(student_dict)

# Create DataFrame from dict
student_df = pd.DataFrame.from_dict(student_dict, orient="index", columns=["stud1", "stud2", "stud3"])
print(student_df)
```

**Output:**
```text
{'name': ['Joe', 'Nat', 'Harry'], 'age': [20, 21, 19], 'marks': [85.1, 77.8, 91.54]}
      stud1 stud2  stud3
name    Joe   Nat  Harry
age      20    21     19
marks  85.1  77.8  91.54
```

## DataFrame from dict where values are variable-length lists

It is a widespread use case in the IT industry where data is stored in the dictionary with different values against each key.

If such a dictionary object needs to be converted into the DataFrame such that keys and values will be added as columns in DataFrame. Then it can be done using chaining of **`DataFrame.from_dict()`**, **`stack()`**, and **`reset_index()`** functions.

**Example:**

Here, we have **`dict`** with values are of different sizes and still we need to add all the key-values into a DataFrame.

```python
import pandas as pd

# Create dict object
student_dict = {"Grade A": ["Joe", "Harry"], "Grade B": ["Nat"]}
print(student_dict)

student_df = pd.DataFrame.from_dict(student_dict, 'index').stack().reset_index(level=0)
print(student_df)
```

**Output:**
```text
{'Grade A': ['Joe', 'Harry'], 'Grade B': ['Nat']}
   level_0      0
0  Grade A    Joe
1  Grade A  Harry
0  Grade B    Nat
```

## DataFrame from dict nested dict

In this section, we cover the complex structure of the dictionary object where we have a hierarchical structure of the dictionary i.e. one dictionary object into another dictionary object.

**Example:**

We have a student dictionary object where student data categorized by their grades and further divided as per their class. Such a dictionary object is converted into the multi-index DataFrame using **`DataFrame.from_dict()`** by iterating over each key and its values and parameter **`orient='index'`**.

```python
import pandas as pd

# Create hierarchical dict
student_dict = {"Grade A": {'Class A': {'name': 'Joe', 'marks': 91.56},
                            'Class B': {'name': 'Harry', 'marks': 87.90}},
                "Grade B": {'Class A': {'name': 'Sam', 'marks': 70},
                            'Class B': {'name': 'Alan', 'marks': 65.48}}}
print(student_dict)

# Create multi-index DataFrame
student_df = pd.DataFrame.from_dict({(i, j): student_dict[i][j]
                                     for i in student_dict.keys()
                                     for j in student_dict[i].keys()},
                                    orient='index')
print(student_df)
```

**Output:**
```text
{'Grade A': {'Class A': {'name': 'Joe', 'marks': 91.56}, 'Class B': {'name': 'Harry', 'marks': 87.9}}, 'Grade B': {'Class A': {'name': 'Sam', 'marks': 70}, 'Class B': {'name': 'Alan', 'marks': 65.48}}}
                  name  marks
Grade A Class A    Joe  91.56
        Class B  Harry  87.90
Grade B Class A    Sam  70.00
        Class B   Alan  65.48
```

## DataFrame constructor vs `from_dict()`

The below table summarizes all the cases of converting **`dict`** to the DataFrame that we have already discussed in this article. It shows the comparison of using the DataFrame constructor and **`DataFrame.from_dict()`** method.

It will help you to choose the correct function for converting the **`dict`** to the DataFrame.

| Use Case | DataFrame constructor | **`from_dict()`** method |
|:---- |:---- |:---- |
| **`Custom column names`** | **Yes** | **No** | 
| **`custom index`** | **Yes** | **No** | 
| **`dict with a single value`** | **Yes** | **No** | 
| **`list of dict`** | **Yes** | **Yes** | 
| **`handle missing keys`** | **Yes** | **Yes** | 
| **`keys and values as columns`** | **Yes** | **Yes** | 
| **`change datatype`** | **Yes** | **Yes** | 
| **`Orient=column(Keys as columns)`** | **Yes** | **Yes** | 
| **`Orient=index(Keys as rows)`** | **No** | **Yes** | 
| **`Multi-index DataFrame`** | **No** | **Yes** |

---

## 📘 Python Pandas Dataframe
*Source: `7. Python Pandas/1. Python Pandas DataFrame.ipynb`*

# Python Pandas

**[Pandas](https://pandas.pydata.org/)** is an open-source, BSD-licensed Python library. Python package providing fast, flexible, handy, and expressive data structures tool designed to make working with 'relationa' or 'labeled' data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world complex data analysis in Python.

pandas is well suited for many different kinds of data:

* Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet
* Ordered and unordered (not necessarily fixed-frequency) time series data.
* Arbitrary matrix data with row and column labels
* Any other form of observational / statistical data sets.

# Python DataFrame

In this lesson, you will learn pandas DataFrame. It covers the basics of DataFrame, its attributes, functions, and how to use DataFrame for Data Analysis.

DataFrame is the most widely used data structure in Python pandas. You can imagine it as a table in a database or a spreadsheet.

Imagine you have an automobile showroom, and you want to analyze cars’ data to make business strategies. For example, you need to check how many vehicles you have in your showroom of type sedan, or the cars that give good mileage. For such analysis pandas DataFrame is used.

## What is DataFrame in Pandas

Dataframe is a tabular(rows, columns) representation of data. It is a two-dimensional data structure with potentially heterogeneous data.

Dataframe is a size-mutable structure that means data can be added or deleted from it, unlike data series, which does not allow operations that change its size.

<div>

</div>

## DataFrame creation

Data is available in various forms and types like CSV, SQL table, JSON, or Python structures like list, dict etc. We need to convert all such different data formats into a DataFrame so that we can use pandas libraries to analyze such data efficiently.

To create DataFrame, we can use either the DataFrame constructor or pandas built-in functions. Below are some examples.

### DataFrame constructor

```python
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
```

#### Parameters:

* **`data`**: It takes input **`dict`**, **`list`**, **`set`**, **`ndarray`**, **`iterable`**, or DataFrame. If the input is not provided, then it creates an empty DataFrame. The resultant column order follows the insertion order.


* **`index`**: (Optional) It takes the list of row index for the DataFrame. The default value is a range of integers 0, 1,…n.


* **`columns`** : (Optional) It takes the list of columns for the DataFrame. The default value is a range of integers 0, 1,…n.


* **`dtype`**: (Optional) By default, It infers the data type from the data, but this option applies any specific data type to the whole DataFrame.


* **`copy`**: (Optional) Copy data from inputs. Boolean, Default False. Only affects DataFrame or 2D array-like inputs

### Dataframe from dict

When we have data in **`dict`** or any default data structures in Python, we can convert it into DataFrame using the DataFrame constructor.

To construct a DataFrame from a **`dict`** object, we can pass it to the DataFrame constructor **`pd.DataFrame(dict)`**. It creates DataFrame using, where **`dict`** keys will be column labels, and **`dict`** values will be the columns’ data. We can also use **`DataFrame.from_dict()`** function to **Create DataFrame from dict**.

**Key and Imports:**

| Operator | Description |
|:----: |:---- |
| **`df`** | **pandas DataFrame object** | 
| **`s`**  | **pandas Series object** |

```python
# Example: 

student_dict = {'Name':['Joe','Nat'], 'Age':[20,21], 'Marks':[85.10, 77.80]}
student_dict
```

**Output:**
```text
{'Name': ['Joe', 'Nat'], 'Age': [20, 21], 'Marks': [85.1, 77.8]}
```

**'Name'**, **'Age'** and **'Marks'** are the keys in the **`dict`** when you convert they will become the column labels of the DataFrame.

```python
import pandas as pd

# Python dict object
student_dict = {'Name': ['Joe', 'Nat'], 'Age': [20, 21], 'Marks': [85.10, 77.80]}
print(student_dict)

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)
```

**Output:**
```text
{'Name': ['Joe', 'Nat'], 'Age': [20, 21], 'Marks': [85.1, 77.8]}
  Name  Age  Marks
0  Joe   20   85.1
1  Nat   21   77.8
```

```python
# Example

import pandas as pd

# We pass a dict of {column name: column values}
df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)
```

**Output:**
```text
X   Y   Z
0  78  84  86
1  85  94  97
2  96  89  96
3  80  83  72
4  86  86  83
```

```python
# Example

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [True, True, False],
                   'C': [0.496714, -0.138264, 0.647689]},
                  index=['a', 'b', 'c'])  # also this weird index thing
df
```

**Output:**
```text
A      B         C
a  1   True  0.496714
b  2   True -0.138264
c  3  False  0.647689
```

### Indexing

Our first improvement over numpy arrays is labeled indexing. We can select subsets by column, row, or both. Column selection uses the regular python **`__getitem__`** machinery. Pass in a single column label **`'A'`** or a list of labels **`['A', 'C']`** to select subsets of the original **`DataFrame`**.

```python
# Single column, reduces to a Series
df['A']
```

**Output:**
```text
a    1
b    2
c    3
Name: A, dtype: int64
```

```python
cols = ['A', 'C']
df[cols]
```

**Output:**
```text
A         C
a  1  0.496714
b  2 -0.138264
c  3  0.647689
```

For row-wise selection, use the special **`.loc`** accessor.

```python
df.loc[['a', 'b']]
```

**Output:**
```text
A     B         C
a  1  True  0.496714
b  2  True -0.138264
```

You can use ranges to select rows or columns.

```python
df.loc['a':'b']
```

**Output:**
```text
A     B         C
a  1  True  0.496714
b  2  True -0.138264
```

Notice that the slice is *inclusive* on both sides,  unlike your typical slicing of a list. Sometimes, you'd rather slice by *position* instead of label. **`.iloc`** has you covered:

```python
df.iloc[[0, 1]]
```

**Output:**
```text
A     B         C
a  1  True  0.496714
b  2  True -0.138264
```

```python
df.iloc[:2]
```

**Output:**
```text
A     B         C
a  1  True  0.496714
b  2  True -0.138264
```

This follows the usual python slicing rules: closed on the left, open on the right.

As I mentioned, you can slice both rows and columns. Use **`.loc`** for label or **`.iloc`** for position indexing.

```python
df.loc['a', 'B']
```

**Output:**
```text
True
```

Pandas, like NumPy, will reduce dimensions when possible. Select a single column and you get back `Series` (see below). Select a single row and single column, you get a scalar.

You can get pretty fancy:

```python
df.loc['a':'b', ['A', 'C']]
```

**Output:**
```text
A         C
a  1  0.496714
b  2 -0.138264
```

#### Summary

- Use **`[]`** for selecting columns
- Use **`.loc[row_lables, column_labels]`** for label-based indexing
- Use **`.iloc[row_positions, column_positions]`** for positional index

I've left out boolean and hierarchical indexing, which we'll see later.

## Series

You've already seen some **Series** up above. It's the 1-dimensional analog of the DataFrame. Each column in a **DataFrame** is in some sense a **Series**. You can select a **Series** from a DataFrame in a few ways:

```python
# __getitem__ like before
df['A']
```

**Output:**
```text
a    1
b    2
c    3
Name: A, dtype: int64
```

```python
# .loc, like before
df.loc[:, 'A']
```

**Output:**
```text
a    1
b    2
c    3
Name: A, dtype: int64
```

```python
# using `.` attribute lookup
df.A
```

**Output:**
```text
a    1
b    2
c    3
Name: A, dtype: int64
```

```python
df['mean'] = ['a', 'b', 'c']
df
```

**Output:**
```text
A      B         C mean
a  1   True  0.496714    a
b  2   True -0.138264    b
c  3  False  0.647689    c
```

```python
df.mean
```

```python
df['mean']
```

**Output:**
```text
a    a
b    b
c    c
Name: mean, dtype: object
```

```python
# Create DataSeries:

import pandas as pd
s = pd.Series([2, 4, 6, 8, 10])
print(s)
```

**Output:**
```text
0     2
1     4
2     6
3     8
4    10
dtype: int64
```

You'll have to be careful with the last one. It won't work if you're column name isn't a valid python identifier (say it has a space) or if it conflicts with one of the (many) methods on **DataFrame**. The **`.`** accessor is extremely convient for interactive use though.

You should never *assign* a column with **`.`** e.g. don't do

```python
# bad
df.A = [1, 2, 3]
```

It's unclear whether your attaching the list **`[1, 2, 3]`** as an attribute of **`df`**, or whether you want it as a column. It's better to just say

```python
df['A'] = [1, 2, 3]
# or
df.loc[:, 'A'] = [1, 2, 3]
```

**Series** share many of the same methods as **DataFrame**s.

## Index

**`Index`** are something of a peculiarity to pandas.
First off, they are not the kind of indexes you'll find in SQL, which are used to help the engine speed up certain queries.
In pandas, **`Index`** are about lables. This helps with selection (like we did above) and automatic alignment when performing operations between two **DataFrames** or **Series**.

R does have row labels, but they're nowhere near as powerful (or complicated) as in pandas. You can access the index of a **DataFrame** or **Series** with the **`.index`** attribute.

```python
df.index
```

**Output:**
```text
Index(['a', 'b', 'c'], dtype='object')
```

```python
df.columns
```

**Output:**
```text
Index(['A', 'B', 'C', 'mean'], dtype='object')
```

There are special kinds of `Index`es that you'll come across. Some of these are

- **`MultiIndex`** for multidimensional (Hierarchical) labels
- **`DatetimeIndex`** for datetimes
- **`Float64Index`** for floats
- **`CategoricalIndex`** for, you guessed it, **Categoricals**

* **How do you slice a DataFrame by row label?**
  - Use **`.loc[label]`**. For position based use **`.iloc[integer]`**.
* **How do you select a column of a DataFrame?**
  - Standard **`__getitem__`**: **`df[column_name]`**
* **Is the Index a column in the DataFrame?**
  - No. It isn't included in any operations (**`mean`**, etc). It can be inserted as a regular column with **`df.reset_index()`**.

### Dataframe from CSV

In the field of Data Science, **[CSV](https://en.wikipedia.org/wiki/Comma-separated_values)** files are used to store large datasets. To efficiently analyze such datasets, we need to convert them into pandas DataFrame.

To create a DataFrame from CSV, we use the **`read_csv('file_name')`** function that takes the file name as input and returns DataFrame as output.

**Example 1:** 

Let’s see how to read the **stockprice_data.csv** file into the DataFrame and then convert it into Pandas Series

<div>

</div>

```python
import pandas as pd
data = pd.read_csv("stockprice_data.csv")
data
```

**Output:**
```text
Date  Closing price    Return
0    1/1/2020            100  0.010000
1    2/1/2020            120  0.200000
2    3/1/2020            130  0.083333
3    4/1/2020             98 -0.246154
4    5/1/2020             50 -0.489796
5    6/1/2020            102  1.040000
6    7/1/2020            104  0.019608
7    8/1/2020            150  0.442308
8    9/1/2020            160  0.066667
9   10/1/2020            109 -0.318750
10  11/1/2020             95 -0.128440
```

```python
type(data)
```

**Output:**
```text
pandas.core.frame.DataFrame
```

```python
data1 = data.iloc[:,2]     # Convert Pandas Data Frame in to Pandas Series
data1
```

**Output:**
```text
0     0.010000
1     0.200000
2     0.083333
3    -0.246154
4    -0.489796
5     1.040000
6     0.019608
7     0.442308
8     0.066667
9    -0.318750
10   -0.128440
Name: Return, dtype: float64
```

```python
type(data1)
```

**Output:**
```text
pandas.core.series.Series
```

**Example 2:**

Let’s see how to read the **automobile_data.csv** file into the DataFrame.

<div>

</div>

```python
cars = pd.read_csv("automobile_data.csv")  # just give the name of file only if the file is in the same folder.
print(cars)
```

**Output:**
```text
index      company   body-style  wheel-base  length engine-type  \
0       0  alfa-romero  convertible        88.6   168.8        dohc   
1       1  alfa-romero  convertible        88.6   168.8        dohc   
2       2  alfa-romero    hatchback        94.5   171.2        ohcv   
3       3         audi        sedan        99.8   176.6         ohc   
4       4         audi        sedan        99.4   176.6         ohc   
..    ...          ...          ...         ...     ...         ...   
56     81   volkswagen        sedan        97.3   171.7         ohc   
57     82   volkswagen        sedan        97.3   171.7         ohc   
58     86   volkswagen        sedan        97.3   171.7         ohc   
59     87        volvo        sedan       104.3   188.8         ohc   
60     88        volvo        wagon       104.3   188.8         ohc   

   num-of-cylinders  horsepower  average-mileage    price  
0              four         111               21  13495.0  
1              four         111
... [Output truncated for brevity]
```

## DataFrame Options

When DataFrame is vast, and we can not display the whole data while printing. In that case, we need to change how DataFrame gets display on the console using the **`print()`** function. For that, pandas have provided many options and functions to customize the presentation of the DataFrame.

### To customize the display of DataFrame while printing

When we display the DataFrame using **`print()`** function by default, it displays 10 rows (top 5 and bottom 5). Sometimes we may need to show more or lesser rows than the default view of the DataFrame.

We can change the setting by using **`pd.options`** or **`pd.set_option()`** functions. Both can be used interchangeably.

The below example will show a maximum of 20 and a minimum of 5 rows while printing DataFrame.

```python
import pandas as pd

# Setting maximum rows to be shown 
pd.options.display.max_rows = 20

# Setting minimum rows to be shown
pd.set_option("display.min_rows", 5)

# Print DataFrame
print(cars)
```

**Output:**
```text
index      company   body-style  wheel-base  length engine-type  \
0       0  alfa-romero  convertible        88.6   168.8        dohc   
1       1  alfa-romero  convertible        88.6   168.8        dohc   
..    ...          ...          ...         ...     ...         ...   
59     87        volvo        sedan       104.3   188.8         ohc   
60     88        volvo        wagon       104.3   188.8         ohc   

   num-of-cylinders  horsepower  average-mileage    price  
0              four         111               21  13495.0  
1              four         111               21  16500.0  
..              ...         ...              ...      ...  
59             four         114               23  12940.0  
60             four         114               23  13415.0  

[61 rows x 10 columns]
```

## DataFrame metadata

Sometimes we need to get metadata of the DataFrame and not the content inside it. Such metadata information is useful to understand the DataFrame as it gives more details about the DataFrame that we need to process.

In this section, we cover the functions which provide such information of the DataFrame.

Let’s take an example of student DataFrame which contains **'Name'**, **'Age'** and **'Marks'** of students as shown below:

```python
    Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
```

### Metadata info of DataFrame

**`DataFrame.info()`** is a function of DataFrame that gives metadata of DataFrame. Which includes,

* Number of rows and its range of index
* Total number of columns
* List of columns
* Count of the total number of non-null values in the column
* Data type of column
* Count of columns in each data type
* Memory usage by the DataFrame

```python
# Example: In the below example, we got metadata information of student DataFrame.

# get dataframe info
student_df.info()
```

### Get the statistics of DataFrame

**`DataFrame.describe()`** is a function that gives mathematical statistics of the data in DataFrame. But, it applies to the columns that contain numeric values.

In our example of student DataFrame, it gives descriptive statistics of **'Age'** and **'Marks'** columns only, that includes:

1. **count**: Total number of non-null values in the column
2. **mean**: an average of numbers
3. **std**: a standard deviation value
4. **min**: minimum value
5. **25%**: 25th percentile
6. **50%**: 50th percentile
7. **75%**: 75th percentile
8. **max**: maximum value

>**Note:** Output of **`DataFrame.describe()`** function varies depending on the input DataFrame.

```python
# Example

# get dataframe description
student_df.describe()
```

**Output:**
```text
Age     Marks
count   2.000000   2.00000
mean   20.500000  81.45000
std     0.707107   5.16188
min    20.000000  77.80000
25%    20.250000  79.62500
50%    20.500000  81.45000
75%    20.750000  83.27500
max    21.000000  85.10000
```

## DataFrame Attributes

DataFrame has provided many built-in attributes. Attributes do not modify the underlying data, unlike functions, but it is used to get more details about the DataFrame.

Following are majorly used attributes of the DataFrame:

| Attribute | Description |
|:---- |:---- |
| **`DataFrame.index`**   | **It gives the Range of the row index** | 
| **`DataFrame.columns`** | **It gives a list of column labels** |
| **`DataFrame.dtypes`**  | **It gives column names and their data type** | 
| **`DataFrame.values`**  | **It gives all the rows in DataFrame** |
| **`DataFrame.empty`**   | **It is used to check if the DataFrame is empty** | 
| **`DataFrame.size`**    | **It gives a total number of values in DataFrame** |
| **`DataFrame.shape`**   | **It a number of rows and columns in DataFrame** |

```python
# Example:

import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)

print("DataFrame : ", student_df)

print("DataFrame Index : ", student_df.index)
print("DataFrame Columns : ", student_df.columns)

print("DataFrame Column types : ", student_df.dtypes)

print("DataFrame is empty? : ", student_df.empty)

print("DataFrame Shape : ", student_df.shape)
print("DataFrame Size : ", student_df.size)

print("DataFrame Values : ", student_df.values)
```

**Output:**
```text
DataFrame :      Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
DataFrame Index :  RangeIndex(start=0, stop=3, step=1)
DataFrame Columns :  Index(['Name', 'Age', 'Marks'], dtype='object')
DataFrame Column types :  Name      object
Age        int64
Marks    float64
dtype: object
DataFrame is empty? :  False
DataFrame Shape :  (3, 3)
DataFrame Size :  9
DataFrame Values :  [['Joe' 20 85.1]
 ['Nat' 21 77.8]
 ['Harry' 19 91.54]]
```

## DataFrame selection 

While dealing with the vast data in DataFrame, a data analyst always needs to select a particular row or column for the analysis. In such cases, functions that can choose a set of rows or columns like top rows, bottom rows, or data within an index range play a significant role.

Following are the functions that help in selecting the subset of the DataFrame:

| Attribute | Description |
|:---- |:---- |
| **`DataFrame.head(n)`**  | **It is used to select top ‘n’ rows in DataFrame.** | 
| **`DataFrame.tail(n)`**  | **It is used to select bottom ‘n’ rows in DataFrame.** | 
| **`DataFrame.at`**       | **It is used to get and set the particular value of DataFrame using row and column labels.** | 
| **`DataFrame.iat`**      | **It is used to get and set the particular value of DataFrame using row and column index positions.** | 
| **`DataFrame.get(key)`** | **It is used to get the value of a key in DataFrame where Key is the column name.** | 
| **`DataFrame.loc()`**    | **It is used to select a group of data based on the row and column labels. It is used for slicing and filtering of the DataFrame.** | 
| **`DataFrame.iloc()`**   | **It is used to select a group of data based on the row and column index position. Use it for slicing and filtering the DataFrame.** |

```python
# Example

import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)

# display dataframe
print("DataFrame : ", student_df)

# select top 2 rows
print(student_df.head(2))

# select bottom 2 rows
print(student_df.tail(2))

# select value at row index 0 and column 'Name'
print(student_df.at[0, 'Name'])

# select value at first row and first column
print(student_df.iat[0, 0])

# select values of 'Name' column
print(student_df.get('Name'))

# select values from row index 0 to 2 and 'Name' column
print(student_df.loc[0:2, ['Name']])

# select values from row index 0 to 2(exclusive) and column position 0 to 2(exclusive)
print(student_df.iloc[0:2, 0:2])
```

**Output:**
```text
DataFrame :      Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
  Name  Age  Marks
0  Joe   20   85.1
1  Nat   21   77.8
    Name  Age  Marks
1    Nat   21  77.80
2  Harry   19  91.54
Joe
Joe
0      Joe
1      Nat
2    Harry
Name: Name, dtype: object
    Name
0    Joe
1    Nat
2  Harry
  Name  Age
0  Joe   20
1  Nat   21
```

## DataFrame modification

DataFrame is similar to any excel sheet or a database table where we need to insert new data or **[drop columns]()** and rows if not required. Such data manipulation operations are very common on a DataFrame.

In this section, we discuss the data manipulation functions of the DataFrame.

### Insert columns

Sometimes it is required to add a new column in the DataFrame. **`DataFrame.insert()`** function is used to insert a new column in DataFrame at the specified position.

In the below example, we insert a new column **'Class'** as a third new column in the DataFrame with default value ‘**A**’ using the syntax:

```python
df.insert(loc = col_position, column = new_col_name, value = default_value)
```

```python
# Example:

import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}
student_df = pd.DataFrame(student_dict)
print(student_df)

# insert new column in dataframe and display
student_df.insert(loc=2, column="Class", value='A')
print(student_df)
```

**Output:**
```text
Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
    Name  Age Class  Marks
0    Joe   20     A  85.10
1    Nat   21     A  77.80
2  Harry   19     A  91.54
```

### Drop columns

DataFrame may contain redundant data, in such cases, we may need to delete such data that is not required. **`DataFrame.drop()`** function is used to **delete the columns from DataFrame**.

Refer to the following articles to get more details

* **Drop duplicates**
* **Drop columns with NA**

In the below example, we delete the “**Age**” column from the student DataFrame using **`df.drop(columns=[col1,col2...])`**.

```python
import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
print(student_df)

# delete column from dataframe
student_df = student_df.drop(columns='Age')
print(student_df)
```

**Output:**
```text
Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
    Name  Marks
0    Joe  85.10
1    Nat  77.80
2  Harry  91.54
```

### Apply condition

We may need to update the value in the DataFrame based on some condition. **`DataFrame.where() `**function is used to replace the value of DataFrame, where the condition is **`False`**.

**Syntax:**
```python
where(filter, other=new_value)
```

It applies the filter condition on all the rows in the DataFrame, as follows:

* If the filter condition returns **`False`**, then it updates the row with the value specified in **`other`** parameter.
* If the filter condition returns **`True`**, then it does not update the row.

In the below example, we want to replace the student marks with ‘0’ where marks are less than 80. We pass a filter condition **`df['Marks'] > 80`** to the function.

```python
import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
print(student_df)

# Define filter condition
filter = student_df['Marks'] > 80

student_df['Marks'].where(filter, other=0, inplace=True)
print(student_df)
```

**Output:**
```text
Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
    Name  Age  Marks
0    Joe   20  85.10
1    Nat   21   0.00
2  Harry   19  91.54
```

## DataFrame filter columns

Datasets contain massive data that need to be analyzed. But, sometimes, we may want to analyze relevant data and filter out all the other data. In such a case, we can use **`DataFrame.filter() `** function to fetch only required data from DataFrame.

It returns the subset of the DataFrame by applying conditions on each row index or column label as specified using the below syntax.

**Syntax:**
```python
df.filter(like = filter_cond, axis = 'columns' or 'index')
```

It applies the condition on each row index or column label.

* If the condition passed then, it includes that row or column in the resultant DataFrame.
* If the condition failed, then it does not have that row or column in the resulting DataFrame.

>**Note:** It applies the filter on row index or column label, not on actual data.

In the below example, we only include the column with a column label that starts with ‘**N**’.

```python
import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
print(student_df)

# apply filter on dataframe
student_df = student_df.filter(like='N', axis='columns')
print(student_df)
```

**Output:**
```text
Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
    Name
0    Joe
1    Nat
2  Harry
```

## DataFrame rename columns

While working with DataFrame, we may need to **rename the column** or row index. We can use **`DataFrame.rename()`** function to alter the row or column labels.

We need to pass a dictionary of key-value pairs as input to the function. Where key of the **`dict`** is the existing column label, and the value of **`dict`** is the new column label.

```python
df.rename(columns = {'old':'new'})
```

It can be used to rename single or multiple columns and row labels.

In the below example, we rename column '**Marks**' to '**Percentage**' in the student DataFrame.

```python
import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
print(student_df)

# rename column
student_df = student_df.rename(columns={'Marks': 'Percentage'})
print(student_df)
```

**Output:**
```text
Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
    Name  Age  Percentage
0    Joe   20       85.10
1    Nat   21       77.80
2  Harry   19       91.54
```

## DataFrame Join

In most of the use cases of Data Analytics, data gathered from multiple sources, and we need to combine that data for further analysis. In such instances, join and merge operations are required.

**`DataFrame.join()`** function is used to join one DataFrame with another DataFrame as **`df1.join(df2)`**

In the below example, we joined two different DataFrames to create a new resultant DataFrame.

```python
import pandas as pd

# create dataframe from dict 
student_dict = {'Name': ['Joe', 'Nat'], 'Age': [20, 21]}
student_df = pd.DataFrame(student_dict)
print(student_df)

# create dataframe from dict 
marks_dict = {'Marks': [85.10, 77.80]}
marks_df = pd.DataFrame(marks_dict)
print(marks_df)

# join dfs
joined_df = student_df.join(marks_df)
print(joined_df)
```

**Output:**
```text
Name  Age
0  Joe   20
1  Nat   21
   Marks
0   85.1
1   77.8
  Name  Age  Marks
0  Joe   20   85.1
1  Nat   21   77.8
```

## DataFrame GroupBy

**`GroupBy`** operation means splitting the data and then combining them based on some condition. Large data can be divided into logical groups to analyze it.

**`DataFrame.groupby()`** function groups the DataFrame row-wise or column-wise based on the condition.

If we want to analyze each class’s average marks, we need to combine the student data based on the ‘Class’ column and calculate its average using **`df.groupby(col_label).mean()`** as shown in the below example.

```python
import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Class': ['A', 'B', 'A'], 'Marks': [85.10, 77.80, 91.54]}
student_df = pd.DataFrame(student_dict)
print(student_df)

# apply group by 
student_df = student_df.groupby('Class').mean()
print(student_df)
```

**Output:**
```text
Name Class  Marks
0    Joe     A  85.10
1    Nat     B  77.80
2  Harry     A  91.54
       Marks
Class       
A      88.32
B      77.80
```

## DataFrame Iteration

DataFrame iteration means visiting each element in the DataFrame one by one. While analyzing a DataFrame, we may need to iterate over each row of the DataFrame.

There are multiple ways to iterate a DataFrame. We will see the function **`DataFrame.iterrows()`**, which can loop a DataFrame row-wise. It returns the index and row of the DataFrame in each iteration of the for a loop.

```python
import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat'], 'Age': [20, 21], 'Marks': [85, 77]}
student_df = pd.DataFrame(student_dict)

# Iterate all the rows of DataFrame
for index, row in student_df.iterrows():
    print(index, row)
```

**Output:**
```text
0 Name     Joe
Age       20
Marks     85
Name: 0, dtype: object
1 Name     Nat
Age       21
Marks     77
Name: 1, dtype: object
```

## DataFrame Sorting

Data Analyst always needs to perform different operations on the underlying data like merge, sort, concatenate, etc. The most frequently used operation is the sorting of data. Sorted data becomes easy to analyze and inferred.

The **`DataFrame.sort_values()`** function is used to sort the DataFrame using one or more columns in ascending (default) or descending order.

In the below example, we sort the student data based on the '**Marks**'.

```python
import pandas as pd

# Create DataFrame from dict
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}
student_df = pd.DataFrame(student_dict)
print(student_df)

# rename column
student_df = student_df.sort_values(by=['Marks'])
print(student_df)
```

**Output:**
```text
Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
    Name  Age  Marks
1    Nat   21  77.80
0    Joe   20  85.10
2  Harry   19  91.54
```

## DataFrame conversion

After all the processing on DataFrame, we will get the expected data in the DataFrame. But, we may require to convert the DataFrame back to its original formats like CSV file or **`dict`**, or we may need to convert it to another format for further action like storing it into the Database as SQL table format.

Pandas have provided plenty of functions to convert the DataFrames into many different formats.

For example, **`DataFrame.to_dict()`** function is used to converts the **DataFrame into a Python dictionary** object.

Below is the example of a DataFrame which we need to convert into the Python **`dict`**.

```python
    Name  Class Marks
0    Joe     A  85.10
1    Nat     B  77.80
2  Harry     A  91.54
```

Let’s see how we can use **`DataFrame.to_dict()`** function to convert the DataFrame into the Python dictionary. By default, it creates the dictionary with keys as column labels and values as mapping of the row index and data.

```python
# convert dataframe to dict
dict = student_df.to_dict()
print(dict)
```

**Output:**
```text
{'Name': {1: 'Nat', 0: 'Joe', 2: 'Harry'}, 'Age': {1: 21, 0: 20, 2: 19}, 'Marks': {1: 77.8, 0: 85.1, 2: 91.54}}
```

# Summary:

## Create Test Objects

| Operator | Description |
|:---- |:---- |
| **`pd.DataFrame(np.random.rand(20,5))`** | **5 columns and 20 rows of random floats** | 
| **`pd.Series(my_list)`** | **Create a series from an iterable my_list** | 
| **`df.index = pd.date_range('1900/1/30', periods=df.shape[0])`** | **Add a date index** |

## Viewing/Inspecting Data

| Operator | Description |
|:---- |:---- |
| **`df.head(n)`** | **First n rows of the DataFrame** | 
| **`df.tail(n)`** | **Last n rows of the DataFrame** | 
| **`df.shape`** | **Number of rows and columns** | 
| **`df.info()`** | **Index, Datatype and Memory information** | 
| **`df.describe()`** | **Summary statistics for numerical columns** | 
| **`s.value_counts(dropna=False)`** | **View unique values and counts** | 
| **`df.apply(pd.Series.value_counts)`** | **Unique values and counts for all columns** |

## Selection

| Operator | Description |
|:---- |:---- |
| **`df[col]`** | **Returns column with label col as Series** | 
| **`df[[col1, col2]]`** | **Returns columns as a new DataFrame** | 
| **`s.iloc[0]`** | **Selection by position** | 
| **`s.loc['index_one']`** | **Selection by index** | 
| **`df.iloc[0,:]`** | **First row** | 
| **`df.iloc[0,0]`** | **First element of first column** |

## Data Cleaning

| Operator | Description |
|:---- |:---- |
| **`df.columns = ['a','b','c']`** | **Rename columns** | 
| **`pd.isnull()`** | **Checks for null Values, Returns Boolean Arrray** | 
| **`pd.notnull()`** | **Opposite of pd.isnull()** | 
| **`df.dropna()`** | **Drop all rows that contain null values** | 
| **`df.dropna(axis=1)`** | **Drop all columns that contain null values** | 
| **`df.dropna(axis=1,thresh=n)`** | **Drop all rows have have less than n non null values** | 
| **`df.fillna(x)`** | **Replace all null values with x** | 
| **`s.fillna(s.mean())`** | **Replace all null values with the mean** | 
| **`s.astype(float)`** | **Convert the datatype of the series to float** | 
| **`s.replace(1,'one')`** | **Replace all values equal to 1 with 'one'** | 
| **`s.replace([2,3],['two', 'three'])`** | **Replace all 2 with 'two' and 3 with 'three'** | 
| **`df.rename(columns=lambda x: x + 1)`** | **Mass renaming of columns** | 
| **`df.rename(columns={'old_name': 'new_ name'})`** | **Selective renaming** | 
| **`df.set_index('column_one')`** | **Change the index** | 
| **`df.rename(index=lambda x: x + 1)`** | **Mass renaming of index** |

## Filter, Sort, and Groupby

| Operator | Description |
|:---- |:---- |
| **`df[df[col] > 0.6]`** | **Rows where the column col is greater than 0.6** | 
| **`df[(df[col] > 0.6) & (df[col] < 0.8)]`** | **Rows where 0.8 > col > 0.6** | 
| **`df.sort_values(col1)`** | **Sort values by col1 in ascending order** | 
| **`df.sort_values(col2,ascending=False)`** | **Sort values by col2 in descending order.5** | 
| **`df.sort_values([col1,col2],ascending=[True,False])`** | **Sort values by col1 in ascending order then col2 in descending order** | 
| **`df.groupby(col)`** | **Returns a groupby object for values from one column** | 
| **`df.groupby([col1,col2])`** | **Returns groupby object for values from multiple columns** | 
| **`df.groupby(col1)[col2]`** | **Returns the mean of the values in col2, grouped by the values in col1** | 
| **`df.pivot_table(index=col1,values=[col2,col3],aggfunc=mean)`** | **Create a pivot table that groups by col1 and calculates the mean of col2 and col3** | 
| **`df.groupby(col1).agg(np.mean)`** | **Find the average across all columns for every unique col1 group** | 
| **`df.apply(np.mean)`** | **Apply the function np.mean() across each column** | 
| **`nf.apply(np.max,axis=1)`** | **Apply the function np.max() across each row** |

## Join/Combine

| Operator | Description |
|:---- |:---- |
| **`df1.append(df2)`** | **Add the rows in df1 to the end of df2 (columns should be identical)** | 
| **`pd.concat([df1, df2],axis=1)`** | **Add the columns in df1 to the end of df2 (rows should be identical)** | 
| **`df1.join(df2,on=col1, how='inner')`** | **SQL-style join the columns in df1 with the columns on df2 where the rows for col have identical values. The 'how' can be 'left', 'right', 'outer' or 'inner'** |

## Statistics

| Operator | Description |
|:---- |:---- |
| **`df.describe()`** | **Summary statistics for numerical columns** | 
| **`df.mean()`** | **Returns the mean of all columns** | 
| **`df.corr()`** | **Returns the correlation between columns in a DataFrame** | 
| **`df.count()`** | **Returns the number of non-null values in each DataFrame column** | 
| **`df.max()`** | **Returns the highest value in each column** | 
| **`df.min()`** | **Returns the lowest value in each column** | 
| **`df.median()`** | **Returns the median of each column** | 
| **`df.std()`** | **Returns the standard deviation of each column** |

## Importing Data

| Operator | Description |
|:---- |:---- |
| **`pd.read_csv(filename)`** | **From a CSV file** | 
| **`pd.read_table(filename)`** | **From a delimited text file (like TSV)** | 
| **`pd.read_excel(filename)`** | **From an Excel file** | 
| **`pd.read_sql(query, connection_object)`** | **Read from a SQL table/database** | 
| **`pd.read_json(json_string)`** | **Read from a JSON formatted string, URL or file.** | 
| **`pd.read_html(url)`** | **Parses an html URL, string or file and extracts tables to a list of dataframes** | 
| **`pd.read_clipboard()`** | **Takes the contents of your clipboard and passes it to read_table()** | 
| **`pd.DataFrame(dict)`** | **From a dict, keys for columns names, values for data as lists** |

## Exporting Data

| Operator | Description |
|:---- |:---- |
| **`df.to_csv(filename)`** | **Write to a CSV file** | 
| **`df.to_excel(filename)`** | **Write to an Excel file** | 
| **`df.to_sql(table_name, connection_object)`** | **Write to a SQL table** | 
| **`df.to_json(filename)`** | **Write to a file in JSON format** |

---

## 📘 Python Pandas Dataframe From List
*Source: `7. Python Pandas/2. Python Pandas DataFrame from List.ipynb`*

# Create Pandas DataFrame from Python List

In this class, you will learn how to convert Python **List** to a **Pandas DataFrame**. It covers creating DataFrame from different types of a list like single list, multiple lists, nested lists. It creates DataFame from a list where a list can be added as a row or a column.

The List is a simple data structure in Python that stores the values as a List. The List can have heterogeneous elements, i.e., it can have values of different types. To analyze such a List, we can convert it into the pandas DataFrame. By converting the List into a 2-dimensional structure makes it efficient to process.

DataFrame can be created from List using DataFrame constructor. In this class, we will discusses all the cases of it in detail.

## Create DataFrame from list using constructor

**DataFrame constructor** can create DataFrame from different data structures in python like **`dict`**, list, set, tuple, and **`ndarray`**.

**Example:**

Here we create a DataFrame object using a list of heterogeneous data. By default, all list elements are added as a row in the DataFrame. And row index is the range of numbers(starting at 0).

```python
import pandas as pd

# Create list
fruits_list = ['Apple', 10, 'Orange', 55.50]
print(fruits_list)

# Create DataFrame from list
fruits_df = pd.DataFrame(fruits_list)
print(fruits_df)
```

**Output:**
```text
['Apple', 10, 'Orange', 55.5]
        0
0   Apple
1      10
2  Orange
3    55.5
```

## Create DataFrame from list with a customized column name

While creating a DataFrame from the list, we can give a customized column label in the resultant DataFrame. By default, it provides a range of integers as column labels, i.e., 0, 1, 2…n.

We can specify column labels into the **`columns=[col_labels]`** parameter in the DataFrame constructor.

**Example:**

In the below example, we create DataFrame from a list of fruit names and provides a column label as **`Fruits`**.

```python
import pandas as pd

# Create list
fruits_list = ['Apple', 'Banana', 'Orange','Mango']
print(fruits_list)

# Create DataFrame from list
fruits_df = pd.DataFrame(fruits_list, columns=['Fruits'])
print(fruits_df)
```

**Output:**
```text
['Apple', 'Banana', 'Orange', 'Mango']
   Fruits
0   Apple
1  Banana
2  Orange
3   Mango
```

## Create DataFrame from list with a customized index

As we just discussed the changing column label, we can even customize the row index as well. We can give a meaningful row index to identify each row uniquely. It becomes easier to access the rows using the index label.

We can specify row index into the **`index=[row_index1, row_index2]`** parameter in the DataFrame constructor. By default, it gives a range of integers as row index i.e. 0, 1, 2…n.

**Example:**

Let’s see how we can provide the custom row index while creating DataFrame from the List.

```python
import pandas as pd

# Create list
fruits_list = ['Apple', 'Banana', 'Orange','Mango']
print(fruits_list)

# Create DataFrame from list
fruits_df = pd.DataFrame(fruits_list, index=['Fruit1', 'Fruit2', 'Fruit3', 'Fruit4'])
print(fruits_df)
```

**Output:**
```text
['Apple', 'Banana', 'Orange', 'Mango']
             0
Fruit1   Apple
Fruit2  Banana
Fruit3  Orange
Fruit4   Mango
```

## Create DataFrame from list by changing data type

While converting a Python List to the DataFrame, we may need to change the values’ data type.

We can change the data type of the list elements using the **`dtype`** parameter of the DataFrame constructor.

**Example:**

Suppose we have a list of fruit’s prices of type **object**. But, while creating DataFrame we need to correct its data type to **float64**. In such case we use **`dtype`** parameter as shown below example.

```python
import pandas as pd

# Create list
price_list = ['50', '100', '60', '20']
print(price_list)

# Create DataFrame from list
price_df = pd.DataFrame(price_list)
print("Data type before : ", price_df.dtypes)

# Create DataFrame from list with type change
price_df = pd.DataFrame(price_list, dtype='float64')
print("Data type after : ", price_df.dtypes)
print(price_df)
```

**Output:**
```text
['50', '100', '60', '20']
Data type before :  0    object
dtype: object
Data type after :  0    float64
dtype: object
       0
0   50.0
1  100.0
2   60.0
3   20.0
```

## Create DataFrame from hierarchical lists as rows

It may be possible to have data scattered into multiple lists or in the list of lists, also called a **multi-dimensional list**. In such a case, We can pass such a list to the DataFrame constructor to convert it into the DataFrame. By default, it adds each list as a row in the resultant DataFrame.

**Example:**

In the below example, we have a list that has lists of fruit names and their prices. DataFrame constructor will add both the lists as a separate row in the resulting DataFrame.

```python
import pandas as pd

# Create list
fruits_list = [['Apple', 'Banana', 'Orange', 'Mango'],[120, 40, 80, 500]]
print(fruits_list)

# Create DataFrame from list
fruits_df = pd.DataFrame(fruits_list)
print(fruits_df)
```

**Output:**
```text
[['Apple', 'Banana', 'Orange', 'Mango'], [120, 40, 80, 500]]
       0       1       2      3
0  Apple  Banana  Orange  Mango
1    120      40      80    500
```

## Create DataFrame from Hierarchical lists as columns

As discussed in the above section, we have a multi-dimensional list, but we do not want them to add to the DataFrame as a row. Instead, we want to add each list as a separate column in the DataFrame. For that, we need to use the **`transpose()`** function.

**Example:**

Here we have a list of two lists, fruit names and another for the fruits’ price. And we want to add both the list as a separate column in the DataFrame.

```python
import pandas as pd

# Create list
fruits_list = [['Apple', 'Banana', 'Orange', 'Mango'],[120, 40, 80, 500]]
print(fruits_list)

# Create DataFrame from list
fruits_df = pd.DataFrame(fruits_list).transpose()
print(fruits_df)
```

**Output:**
```text
[['Apple', 'Banana', 'Orange', 'Mango'], [120, 40, 80, 500]]
        0    1
0   Apple  120
1  Banana   40
2  Orange   80
3   Mango  500
```

## Create DataFrame from multiple lists

It is the most common use case in the industry where you have multiple separate lists, and you need to add them as different columns in the DataFrame. This case can be resolved by using following two ways:

1. **`zip(list1, list2...)`**
2. **`dict { 'col1' : list1, 'col2' : list2}`**

**Example:**

The below example demonstrates the use of **`zip()`** function to combine multiple lists in one list and pass it to the DataFrame constructor.

```python
import pandas as pd

# Create multiple lists
fruits_list = ['Apple', 'Banana', 'Orange', 'Mango']
price_list = [120, 40, 80, 500]

# Create DataFrame
fruits_df = pd.DataFrame(list(zip(fruits_list, price_list )), columns = ['Name', 'Price'])
print(fruits_df)
```

**Output:**
```text
Name  Price
0   Apple    120
1  Banana     40
2  Orange     80
3   Mango    500
```

The below example demonstrates the use of Python dictionary data structure to solve the purpose. Here, column names are keys of the dict and, lists are the values of dict which need to be added in the DataFrame.

```python
import pandas as pd

# Create multiple lists
fruits_list = ['Apple', 'Banana', 'Orange', 'Mango']
price_list = [120, 40, 80, 500]

# Create dict
fruits_dict = {'Name': fruits_list,
               'Price': price_list}
print(fruits_dict)

# Create DataFrame from dict
fruits_df = pd.DataFrame(fruits_dict)
print(fruits_df)
```

**Output:**
```text
{'Name': ['Apple', 'Banana', 'Orange', 'Mango'], 'Price': [120, 40, 80, 500]}
     Name  Price
0   Apple    120
1  Banana     40
2  Orange     80
3   Mango    500
```

---

## 📘 Python Pandas Exercise 1
*Source: `7. Python Pandas/2. Python Pandas Exercise 1.ipynb`*

# Python Pandas

**[Pandas](https://pandas.pydata.org/)** is an open-source, BSD-licensed Python library. Pandas is a handy and useful data-structure tool for analyzing large and complex data.

In this exercise, we are using **pokemon_data.csv** for data analysis. This Dataset has different characteristics of an auto such as body-style, wheel-base, engine-type, price, mileage, horsepower, etc.

## Loading data into Pandas

```python
import pandas as pd

df = pd.read_csv('pokemon_data.csv') # just give the name of file only if the file is in the same folder.

# print(df.head(5))
# print(df.tail(5))

# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))

# df = pd.read_csv('pokemon_data.txt', delimiter='\t') # without delimiter the data will look like mess.
# print(df.head(5))

df['HP']
```

**Output:**
```text
0      45
1      60
2      80
3      80
4      39
       ..
795    50
796    50
797    80
798    80
799    80
Name: HP, Length: 800, dtype: int64
```

## Reading Data in Pandas

```python
#### Read Headers
df.columns

## Read each Column
#print(df[['Name', 'Type 1', 'HP']])

## Read Each Row
#print(df.iloc[0:4])
# for index, row in df.iterrows():
#     print(index, row['Name'])
#df.loc[df['Type 1'] == "Grass"]

## Read a specific location (R,C)
#print(df.iloc[2,1])
```

**Output:**
```text
Index(['#', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk',
       'Sp. Def', 'Speed', 'Generation', 'Legendary'],
      dtype='object')
```

## Sorting/Describing Data

```python
df

df.sort_values('Name') #arrange acco to Name starting with 'A'
#df.sort_values('Name', ascending=False) #arrange acco to Name starting with 'Z'
```

**Output:**
```text
#                     Name   Type 1  Type 2   HP  Attack  Defense  \
510  460                Abomasnow    Grass     Ice   90      92       75   
511  460  AbomasnowMega Abomasnow    Grass     Ice   90     132      105   
68    63                     Abra  Psychic     NaN   25      20       15   
392  359                    Absol     Dark     NaN   65     130       60   
393  359          AbsolMega Absol     Dark     NaN   65     150       60   
..   ...                      ...      ...     ...  ...     ...      ...   
632  571                  Zoroark     Dark     NaN   60     105       60   
631  570                    Zorua     Dark     NaN   40      65       40   
46    41                    Zubat   Poison  Flying   40      45       35   
695  634                 Zweilous     Dark  Dragon   72      85       70   
794  718         Zygarde50% Forme   Dragon  Ground  108     100      121   

     Sp. Atk  Sp. Def  Speed  Generation  Legendary  
510       92       85     60           4
... [Output truncated for brevity]
```

```python
df.sort_values(['Type 1', 'HP'], ascending=[1,0]) # 'Type1' is ascending and 'HP' is decending
```

**Output:**
```text
#                     Name Type 1    Type 2  HP  Attack  Defense  \
520  469                  Yanmega    Bug    Flying  86      76       86   
698  637                Volcarona    Bug      Fire  85      60       65   
231  214                Heracross    Bug  Fighting  80     125       75   
232  214  HeracrossMega Heracross    Bug  Fighting  80     185      115   
678  617                 Accelgor    Bug       NaN  80      70       40   
..   ...                      ...    ...       ...  ..     ...      ...   
106   98                   Krabby  Water       NaN  30     105       90   
125  116                   Horsea  Water       NaN  30      40       70   
129  120                   Staryu  Water       NaN  30      45       55   
139  129                 Magikarp  Water       NaN  20      10       55   
381  349                   Feebas  Water       NaN  20      15       20   

     Sp. Atk  Sp. Def  Speed  Generation  Legendary  
520      116       56     95           4      False 
... [Output truncated for brevity]
```

## Making changes to the data

```python
df.head(5)
```

**Output:**
```text
#                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
0  1              Bulbasaur  Grass  Poison  45      49       49       65   
1  2                Ivysaur  Grass  Poison  60      62       63       80   
2  3               Venusaur  Grass  Poison  80      82       83      100   
3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122   
4  4             Charmander   Fire     NaN  39      52       43       60   

   Sp. Def  Speed  Generation  Legendary  
0       65     45           1      False  
1       80     60           1      False  
2      100     80           1      False  
3      120     80           1      False  
4       50     65           1      False
```

```python
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

df.head(5)
```

**Output:**
```text
#                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \
0  1              Bulbasaur  Grass  Poison  45      49       49       65   
1  2                Ivysaur  Grass  Poison  60      62       63       80   
2  3               Venusaur  Grass  Poison  80      82       83      100   
3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122   
4  4             Charmander   Fire     NaN  39      52       43       60   

   Sp. Def  Speed  Generation  Legendary  Total  
0       65     45           1      False    318  
1       80     60           1      False    405  
2      100     80           1      False    525  
3      120     80           1      False    625  
4       50     65           1      False    309
```

```python
45+49+49+65+65+45
```

**Output:**
```text
318
```

```python
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

df = df.drop(columns=['Total'])

df['Total'] = df.iloc[:, 4:10].sum(axis=1) # axis=0 column wise and axis=1 row wise
df
```

**Output:**
```text
#                   Name   Type 1  Type 2  HP  Attack  Defense  \
0      1              Bulbasaur    Grass  Poison  45      49       49   
1      2                Ivysaur    Grass  Poison  60      62       63   
2      3               Venusaur    Grass  Poison  80      82       83   
3      3  VenusaurMega Venusaur    Grass  Poison  80     100      123   
4      4             Charmander     Fire     NaN  39      52       43   
..   ...                    ...      ...     ...  ..     ...      ...   
795  719                Diancie     Rock   Fairy  50     100      150   
796  719    DiancieMega Diancie     Rock   Fairy  50     160      110   
797  720    HoopaHoopa Confined  Psychic   Ghost  80     110       60   
798  720     HoopaHoopa Unbound  Psychic    Dark  80     160       60   
799  721              Volcanion     Fire   Water  80     110      120   

     Sp. Atk  Sp. Def  Speed  Generation  Legendary  Total  
0         65       65     45           1      False    318  
1       
... [Output truncated for brevity]
```

```python
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

df.head(5)
```

**Output:**
```text
#                   Name Type 1  Type 2  Total  HP  Attack  Defense  \
0  1              Bulbasaur  Grass  Poison    318  45      49       49   
1  2                Ivysaur  Grass  Poison    405  60      62       63   
2  3               Venusaur  Grass  Poison    525  80      82       83   
3  3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123   
4  4             Charmander   Fire     NaN    309  39      52       43   

   Sp. Atk  Sp. Def  Speed  Generation  Legendary  
0       65       65     45           1      False  
1       80       80     60           1      False  
2      100      100     80           1      False  
3      122      120     80           1      False  
4       60       50     65           1      False
```

## Saving our Data (Exporting into Desired Format)

```python
df
```

**Output:**
```text
#                   Name   Type 1  Type 2  Total  HP  Attack  Defense  \
0      1              Bulbasaur    Grass  Poison    318  45      49       49   
1      2                Ivysaur    Grass  Poison    405  60      62       63   
2      3               Venusaur    Grass  Poison    525  80      82       83   
3      3  VenusaurMega Venusaur    Grass  Poison    625  80     100      123   
4      4             Charmander     Fire     NaN    309  39      52       43   
..   ...                    ...      ...     ...    ...  ..     ...      ...   
795  719                Diancie     Rock   Fairy    600  50     100      150   
796  719    DiancieMega Diancie     Rock   Fairy    700  50     160      110   
797  720    HoopaHoopa Confined  Psychic   Ghost    600  80     110       60   
798  720     HoopaHoopa Unbound  Psychic    Dark    680  80     160       60   
799  721              Volcanion     Fire   Water    600  80     110      120   

     Sp. Atk  Sp. Def  Speed  Generation  Lege
... [Output truncated for brevity]
```

```python
df.to_csv('modified.csv', index=False)

#df.to_excel('modified.xlsx', index=False)

df.to_csv('modified.txt', index=False, sep='\t')
```

## Filtering Data

```python
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

new_df
```

**Output:**
```text
#                   Name Type 1  Type 2  Total   HP  Attack  Defense  \
2      3               Venusaur  Grass  Poison    525   80      82       83   
3      3  VenusaurMega Venusaur  Grass  Poison    625   80     100      123   
50    45              Vileplume  Grass  Poison    490   75      80       85   
77    71             Victreebel  Grass  Poison    490   80     105       65   
652  591              Amoonguss  Grass  Poison    464  114      85       70   

     Sp. Atk  Sp. Def  Speed  Generation  Legendary  
2        100      100     80           1      False  
3        122      120     80           1      False  
50       110       90     50           1      False  
77       100       70     70           1      False  
652       85       80     30           5      False
```

```python
df.loc[df['Name'].str.contains('Mega')]
```

**Output:**
```text
#                       Name    Type 1    Type 2  Total   HP  Attack  \
3      3      VenusaurMega Venusaur     Grass    Poison    625   80     100   
7      6  CharizardMega Charizard X      Fire    Dragon    634   78     130   
8      6  CharizardMega Charizard Y      Fire    Flying    634   78     104   
12     9    BlastoiseMega Blastoise     Water       NaN    630   79     103   
19    15      BeedrillMega Beedrill       Bug    Poison    495   65     150   
23    18        PidgeotMega Pidgeot    Normal    Flying    579   83      80   
71    65      AlakazamMega Alakazam   Psychic       NaN    590   55      50   
87    80        SlowbroMega Slowbro     Water   Psychic    590   95      75   
102   94          GengarMega Gengar     Ghost    Poison    600   60      65   
124  115  KangaskhanMega Kangaskhan    Normal       NaN    590  105     125   
137  127          PinsirMega Pinsir       Bug    Flying    600   65     155   
141  130      GyaradosMega Gyarados     Water      Dark    
... [Output truncated for brevity]
```

```python
df.loc[~df['Name'].str.contains('Mega')]
```

**Output:**
```text
#                 Name   Type 1  Type 2  Total   HP  Attack  Defense  \
0      1            Bulbasaur    Grass  Poison    318   45      49       49   
1      2              Ivysaur    Grass  Poison    405   60      62       63   
2      3             Venusaur    Grass  Poison    525   80      82       83   
4      4           Charmander     Fire     NaN    309   39      52       43   
5      5           Charmeleon     Fire     NaN    405   58      64       58   
..   ...                  ...      ...     ...    ...  ...     ...      ...   
794  718     Zygarde50% Forme   Dragon  Ground    600  108     100      121   
795  719              Diancie     Rock   Fairy    600   50     100      150   
797  720  HoopaHoopa Confined  Psychic   Ghost    600   80     110       60   
798  720   HoopaHoopa Unbound  Psychic    Dark    680   80     160       60   
799  721            Volcanion     Fire   Water    600   80     110      120   

     Sp. Atk  Sp. Def  Speed  Generation  Legendary  
0   
... [Output truncated for brevity]
```

```python
import re

# df.loc[df['Type 1'].str.contains('Fire|Grass', regex = True)]

df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
```

**Output:**
```text
#                   Name Type 1  Type 2  Total   HP  Attack  Defense  \
0      1              Bulbasaur  Grass  Poison    318   45      49       49   
1      2                Ivysaur  Grass  Poison    405   60      62       63   
2      3               Venusaur  Grass  Poison    525   80      82       83   
3      3  VenusaurMega Venusaur  Grass  Poison    625   80     100      123   
4      4             Charmander   Fire     NaN    309   39      52       43   
..   ...                    ...    ...     ...    ...  ...     ...      ...   
735  667                 Litleo   Fire  Normal    369   62      50       58   
736  668                 Pyroar   Fire  Normal    507   86      68       72   
740  672                 Skiddo  Grass     NaN    350   66      65       48   
741  673                 Gogoat  Grass     NaN    531  123     100       62   
799  721              Volcanion   Fire   Water    600   80     110      120   

     Sp. Atk  Sp. Def  Speed  Generation  Legendary  
0   
... [Output truncated for brevity]
```

```python
# To list all the names starating wirh 'pi'

import re

df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I, regex=True)] # '*' means zero or more

#df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)] # '^' means beginning
```

**Output:**
```text
#                     Name    Type 1    Type 2  Total   HP  Attack  \
13    10                 Caterpie       Bug       NaN    195   45      30   
20    16                   Pidgey    Normal    Flying    251   40      45   
21    17                Pidgeotto    Normal    Flying    349   63      60   
22    18                  Pidgeot    Normal    Flying    479   83      80   
23    18      PidgeotMega Pidgeot    Normal    Flying    579   83      80   
30    25                  Pikachu  Electric       NaN    320   35      55   
42    37                   Vulpix      Fire       NaN    299   38      41   
76    70               Weepinbell     Grass    Poison    390   65      90   
84    78                 Rapidash      Fire       NaN    500   65     100   
136  127                   Pinsir       Bug       NaN    500   65     125   
137  127        PinsirMega Pinsir       Bug    Flying    600   65     155   
181  167                 Spinarak       Bug    Poison    250   40      60   
186  1
... [Output truncated for brevity]
```

```python
new_df.reset_index(drop=True, inplace=True)

new_df
```

**Output:**
```text
#                   Name Type 1  Type 2  Total   HP  Attack  Defense  \
0    3               Venusaur  Grass  Poison    525   80      82       83   
1    3  VenusaurMega Venusaur  Grass  Poison    625   80     100      123   
2   45              Vileplume  Grass  Poison    490   75      80       85   
3   71             Victreebel  Grass  Poison    490   80     105       65   
4  591              Amoonguss  Grass  Poison    464  114      85       70   

   Sp. Atk  Sp. Def  Speed  Generation  Legendary  
0      100      100     80           1      False  
1      122      120     80           1      False  
2      110       90     50           1      False  
3      100       70     70           1      False  
4       85       80     30           5      False
```

```python
new_df.to_csv('filtered.csv')
```

## Conditional Changes

```python
# TO change 'Fire' category of 'Type 1' to 'Flamer'

df.loc[df['Type 1'] == 'Fire','Type 1' ] = 'Flamer'
df
```

**Output:**
```text
#                   Name   Type 1  Type 2  Total  HP  Attack  Defense  \
0      1              Bulbasaur    Grass  Poison    318  45      49       49   
1      2                Ivysaur    Grass  Poison    405  60      62       63   
2      3               Venusaur    Grass  Poison    525  80      82       83   
3      3  VenusaurMega Venusaur    Grass  Poison    625  80     100      123   
4      4             Charmander   Flamer     NaN    309  39      52       43   
..   ...                    ...      ...     ...    ...  ..     ...      ...   
795  719                Diancie     Rock   Fairy    600  50     100      150   
796  719    DiancieMega Diancie     Rock   Fairy    700  50     160      110   
797  720    HoopaHoopa Confined  Psychic   Ghost    600  80     110       60   
798  720     HoopaHoopa Unbound  Psychic    Dark    680  80     160       60   
799  721              Volcanion   Flamer   Water    600  80     110      120   

     Sp. Atk  Sp. Def  Speed  Generation  Lege
... [Output truncated for brevity]
```

```python
# To chaange it back

df.loc[df['Type 1'] == 'Flamer','Type 1' ] = 'Fire'
df
```

**Output:**
```text
#                   Name   Type 1  Type 2  Total  HP  Attack  Defense  \
0      1              Bulbasaur    Grass  Poison    318  45      49       49   
1      2                Ivysaur    Grass  Poison    405  60      62       63   
2      3               Venusaur    Grass  Poison    525  80      82       83   
3      3  VenusaurMega Venusaur    Grass  Poison    625  80     100      123   
4      4             Charmander     Fire     NaN    309  39      52       43   
..   ...                    ...      ...     ...    ...  ..     ...      ...   
795  719                Diancie     Rock   Fairy    600  50     100      150   
796  719    DiancieMega Diancie     Rock   Fairy    700  50     160      110   
797  720    HoopaHoopa Confined  Psychic   Ghost    600  80     110       60   
798  720     HoopaHoopa Unbound  Psychic    Dark    680  80     160       60   
799  721              Volcanion     Fire   Water    600  80     110      120   

     Sp. Atk  Sp. Def  Speed  Generation  Lege
... [Output truncated for brevity]
```

```python
# To make all 'Fire' pokemon 'Legandary'

df.loc[df['Type 1'] == 'Fire','Legandary' ] = True
df
```

**Output:**
```text
#                   Name   Type 1  Type 2  Total  HP  Attack  Defense  \
0      1              Bulbasaur    Grass  Poison    318  45      49       49   
1      2                Ivysaur    Grass  Poison    405  60      62       63   
2      3               Venusaur    Grass  Poison    525  80      82       83   
3      3  VenusaurMega Venusaur    Grass  Poison    625  80     100      123   
4      4             Charmander     Fire     NaN    309  39      52       43   
..   ...                    ...      ...     ...    ...  ..     ...      ...   
795  719                Diancie     Rock   Fairy    600  50     100      150   
796  719    DiancieMega Diancie     Rock   Fairy    700  50     160      110   
797  720    HoopaHoopa Confined  Psychic   Ghost    600  80     110       60   
798  720     HoopaHoopa Unbound  Psychic    Dark    680  80     160       60   
799  721              Volcanion     Fire   Water    600  80     110      120   

     Sp. Atk  Sp. Def  Speed  Generation  Lege
... [Output truncated for brevity]
```

```python
df.loc[df['Total'] > 500, ['Generation','Legendary']] = 'TEST VALUE'
df
```

**Output:**
```text
#                   Name   Type 1  Type 2  Total  HP  Attack  Defense  \
0      1              Bulbasaur    Grass  Poison    318  45      49       49   
1      2                Ivysaur    Grass  Poison    405  60      62       63   
2      3               Venusaur    Grass  Poison    525  80      82       83   
3      3  VenusaurMega Venusaur    Grass  Poison    625  80     100      123   
4      4             Charmander     Fire     NaN    309  39      52       43   
..   ...                    ...      ...     ...    ...  ..     ...      ...   
795  719                Diancie     Rock   Fairy    600  50     100      150   
796  719    DiancieMega Diancie     Rock   Fairy    700  50     160      110   
797  720    HoopaHoopa Confined  Psychic   Ghost    600  80     110       60   
798  720     HoopaHoopa Unbound  Psychic    Dark    680  80     160       60   
799  721              Volcanion     Fire   Water    600  80     110      120   

     Sp. Atk  Sp. Def  Speed  Generation   Leg
... [Output truncated for brevity]
```

```python
df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['Test 1', 'Test 2']
df
```

**Output:**
```text
#                   Name   Type 1  Type 2  Total  HP  Attack  Defense  \
0      1              Bulbasaur    Grass  Poison    318  45      49       49   
1      2                Ivysaur    Grass  Poison    405  60      62       63   
2      3               Venusaur    Grass  Poison    525  80      82       83   
3      3  VenusaurMega Venusaur    Grass  Poison    625  80     100      123   
4      4             Charmander     Fire     NaN    309  39      52       43   
..   ...                    ...      ...     ...    ...  ..     ...      ...   
795  719                Diancie     Rock   Fairy    600  50     100      150   
796  719    DiancieMega Diancie     Rock   Fairy    700  50     160      110   
797  720    HoopaHoopa Confined  Psychic   Ghost    600  80     110       60   
798  720     HoopaHoopa Unbound  Psychic    Dark    680  80     160       60   
799  721              Volcanion     Fire   Water    600  80     110      120   

     Sp. Atk  Sp. Def  Speed Generation Legend
... [Output truncated for brevity]
```

So far we have messed up our dataframe so lets go back to our checkpoint 'modified.csv'

```python
df = pd.read_csv('modified.csv')

df
```

**Output:**
```text
#                   Name   Type 1  Type 2  Total  HP  Attack  Defense  \
0      1              Bulbasaur    Grass  Poison    318  45      49       49   
1      2                Ivysaur    Grass  Poison    405  60      62       63   
2      3               Venusaur    Grass  Poison    525  80      82       83   
3      3  VenusaurMega Venusaur    Grass  Poison    625  80     100      123   
4      4             Charmander     Fire     NaN    309  39      52       43   
..   ...                    ...      ...     ...    ...  ..     ...      ...   
795  719                Diancie     Rock   Fairy    600  50     100      150   
796  719    DiancieMega Diancie     Rock   Fairy    700  50     160      110   
797  720    HoopaHoopa Confined  Psychic   Ghost    600  80     110       60   
798  720     HoopaHoopa Unbound  Psychic    Dark    680  80     160       60   
799  721              Volcanion     Fire   Water    600  80     110      120   

     Sp. Atk  Sp. Def  Speed  Generation  Lege
... [Output truncated for brevity]
```

## Aggregate Statistics (Groupby)

```python
df = pd.read_csv('modified.csv')

df.groupby(['Type 1']).mean() # Computing avg attack of 'Type 1' pokemon

#df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False) # computing avg defense
```

**Output:**
```text
#       Total         HP      Attack     Defense  \
Type 1                                                                
Bug       334.492754  378.927536  56.884058   70.971014   70.724638   
Dark      461.354839  445.741935  66.806452   88.387097   70.225806   
Dragon    474.375000  550.531250  83.312500  112.125000   86.375000   
Electric  363.500000  443.409091  59.795455   69.090909   66.295455   
Fairy     449.529412  413.176471  74.117647   61.529412   65.705882   
Fighting  363.851852  416.444444  69.851852   96.777778   65.925926   
Fire      327.403846  458.076923  69.903846   84.769231   67.769231   
Flying    677.750000  485.000000  70.750000   78.750000   66.250000   
Ghost     486.500000  439.562500  64.437500   73.781250   81.187500   
Grass     344.871429  421.142857  67.271429   73.214286   70.800000   
Ground    356.281250  437.500000  73.781250   95.750000   84.843750   
Ice       423.541667  433.458333  72.000000   72.750000   71.416667   
Normal    319.173469  401
... [Output truncated for brevity]
```

```python
df = pd.read_csv('modified.csv')

df['count'] = 1

df.groupby(['Type 1']).count()['count']

#df.groupby(['Type 1', 'Type 2']).count()['count']
```

**Output:**
```text
Type 1
Bug          69
Dark         31
Dragon       32
Electric     44
Fairy        17
Fighting     27
Fire         52
Flying        4
Ghost        32
Grass        70
Ground       32
Ice          24
Normal       98
Poison       28
Psychic      57
Rock         44
Steel        27
Water       112
Name: count, dtype: int64
```

## Working with large amounts of data

```python
for df in pd.read_csv('modified.csv', chunksize=5):
    print("CHUNK DF")
    print(df)
```

**Output:**
```text
CHUNK DF
   #                   Name Type 1  Type 2  Total  HP  Attack  Defense  \
0  1              Bulbasaur  Grass  Poison    318  45      49       49   
1  2                Ivysaur  Grass  Poison    405  60      62       63   
2  3               Venusaur  Grass  Poison    525  80      82       83   
3  3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123   
4  4             Charmander   Fire     NaN    309  39      52       43   

   Sp. Atk  Sp. Def  Speed  Generation  Legendary  
0       65       65     45           1      False  
1       80       80     60           1      False  
2      100      100     80           1      False  
3      122      120     80           1      False  
4       60       50     65           1      False  
CHUNK DF
   #                       Name Type 1  Type 2  Total  HP  Attack  Defense  \
5  5                 Charmeleon   Fire     NaN    405  58      64       58   
6  6                  Charizard   Fire  Flying    534  78      84    
... [Output truncated for brevity]
```

```python
new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    
    new_df = pd.concat([new_df, results])
```

---

## 📘 Python Pandas Dataframe Head() And Tail()
*Source: `7. Python Pandas/3. Python Pandas DataFrame head() and tail().ipynb`*

# Pandas DataFrame head, tail, at, iat

In this class, we learn how to use **`DataFrame.head()`** and **`DataFrame.tail()`** functions to select top and bottom rows of the **Pandas DataFrame** respectively. Also, learn **`DataFrame.at()`** and **`DataFrame.iat()`** functions to access a specific value in the DataFrame.

## How to use `DataFrame.head()` function

This function is used to see the first n rows in the DataFrame. It is beneficial when we have massive datasets, and it is not possible to see the entire dataset at once.

It takes input as the number of rows to be displayed from the top. The default value is 5.

**Syntax:**
```python
DataFrame.head(n=5)
```

**Example:**

In the below Student DataFrame with columns like Name, Age, and Marks. If we apply **`DataFrame.head()`** function, we can see that only the first five rows are displayed.

<div>

</div>

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry','Jack','Jose','Jill','Rose'],
                'Age': [20, 21, 19,17,18,19,17],
                'Marks': [85.10, 77.80, 91.54,72,87.9,90,72]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)

# display first 5 rows
topRows = student_df.head()
print(topRows)
```

**Output:**
```text
Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
3   Jack   17  72.00
4   Jose   18  87.90
```

## Select top n rows in pandas DataFrame

When we want to see a smaller section of data, we can use the function **`DataFrame.head()`** and pass a parameter as the number of rows to display from the top.

**Example:**

In the below example, after we apply the **`DataFrame.head(3)`** function, only the first three rows of the DataFrame are displayed.

```python
# display first 3 rows
topRows = student_df.head(3)
print(topRows)
```

**Output:**
```text
Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
```

## Select top rows except for last n rows

When we have a vast DataFrame, and we want to see all the rows except for the last n rows, we can pass the negative value as a parameter to **`DataFrame.head()`**.

**Example:**

In the below example, if we want to display all the rows except the bottom two rows, we can use **`DataFrame.head(-2)`** function.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry','Jack','Jose',"Jill","Rose"],
                'Age': [20, 21, 19,17,18,19,17],
                'Marks': [85.10, 77.80, 91.54,72,87.9,90,72]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)

# display rows except bottom 2 rows
topRows = student_df.head(-2)
print(topRows)
```

**Output:**
```text
Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
3   Jack   17  72.00
4   Jose   18  87.90
```

## Select top rows from multi-index DataFrames

When Python pandas DataFrame has multiple row index or column headers, then are called multi-level or hierarchical DataFrame. As we have discussed in the above section, we can use the **`DataFrame.head()`** function on multi-index DataFrames to display the top rows.

The below diagram shows hierarchical DataFrame of Student data with two-column headers where column labels **`Name`** and **`Marks`** are at level 0 and **`Surname`** and **`Percentage`** at level 1. Similarly, two-row indexes are index ‘Standard‘ at level 0 and **`Class`** at level 1 of the DataFrame.

**Example:**

The below example shows how to create such DataFrame and display top rows rather than the whole DataFrame.

<div>

</div>

```python
import pandas as pd

index = pd.MultiIndex.from_tuples([('Standard 1', 'Class A'), ('Standard 1', 'Class B'),
                                   ('Standard 2', 'Class A'), ('Standard 2', 'Class B'),
                                   ('Standard 3', 'Class A'), ('Standard 3', 'Class B')],
                                  names=['Standard', 'Class'])

columns = pd.MultiIndex.from_tuples([('Name', 'Surname'),
('Marks', 'Percentage')])

# create multi-index dataframe
student_df = pd.DataFrame([('Joe', 91.56), ('Nat', 87.90),('Harry', 70.10), 
                           ('Sam', 65.48), ("Jill", 72), ("Jane", 80)],
                          index=index, columns=columns)

topRows = student_df.head()
print(topRows)
```

**Output:**
```text
Name      Marks
                   Surname Percentage
Standard   Class                     
Standard 1 Class A     Joe      91.56
           Class B     Nat      87.90
Standard 2 Class A   Harry      70.10
           Class B     Sam      65.48
Standard 3 Class A    Jill      72.00
```

## How to use `DataFrame.tail()` function

We can use the **`DataFrame.tail()`** function to display the last n rows of the DataFrame. Like the head function, this function is used when we want to view a smaller section of the entire DataFrame.

It takes input as the number of rows to be displayed from the bottom. The default value is 5.

**Syntax:**
```python
DataFrame.tail(n=5)
```

**Example:**

In the below Student DataFrame with columns like **`Name`**, **`Age`**, and **`Marks`**. If we apply **`DataFrame.tail()`** function, we can see that only the bottom five rows are displayed in the output.

<div>

</div>

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry','Jack','Jose',"Jill","Rose"],
                'Age': [20, 21, 19,17,18,19,17],
                'Marks': [85.10, 77.80, 91.54,72,87.9,90,72]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)

# display the bottom 5 rows
bottomRows = student_df.tail()
print(bottomRows)
```

**Output:**
```text
Name  Age  Marks
2  Harry   19  91.54
3   Jack   17  72.00
4   Jose   18  87.90
5   Jill   19  90.00
6   Rose   17  72.00
```

## Select bottom n rows in pandas DataFrame

When we want to see a smaller section of data from the bottom of the DataFrame, we can use the function **`DataFrame.tail()`** and pass a parameter as the number of rows to display from the bottom.

**Example:**

In the below example, after we apply the **`DataFrame.tail(3)`** function, we see that only the last 3 rows of the DataFrame are displayed.

```python
bottomRows = student_df.tail(3)
print(bottomRows)
```

**Output:**
```text
Name  Age  Marks
4  Jose   18   87.9
5  Jill   19   90.0
6  Rose   17   72.0
```

## Select bottom rows except for first n rows

When we want to see our entire dataset except for the first few rows, we can use **`DataFrame.tail()`** function and pass the negative value as a parameter to it.

**Example:**

In the below example, if we display all the rows except the top 2 rows using **`DataFrame.tail(2)`**.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry','Jack','Jose',"Jill","Rose"],
                'Age': [20, 21, 19,17,18,19,17],
                'Marks': [85.10, 77.80, 91.54,72,87.9,90,72]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)

# display top rows except the last 2 rows
bottomRows = student_df.tail(-2)
print(bottomRows)
```

**Output:**
```text
Name  Age  Marks
2  Harry   19  91.54
3   Jack   17  72.00
4   Jose   18  87.90
5   Jill   19  90.00
6   Rose   17  72.00
```

## Select bottom rows from the multi index DataFrame

We can apply the **`DataFrame.tail()`** function on multi-index DataFrames as well. It works in the same way as normal DataFrames.

**Example:**

In our example, after we have applied the **`DataFrame.tail()`** function, only the bottom 5 row are displayed.

<div>

</div>

```python
import pandas as pd

index = pd.MultiIndex.from_tuples([('Standard 1', 'Class A'), ('Standard 1', 'Class B'),
                                   ('Standard 2', 'Class A'), ('Standard 2', 'Class B'),
                                   ('Standard 3', 'Class A'), ('Standard 3', 'Class B')],
                                  names=['Standard', 'Class'])

columns = pd.MultiIndex.from_tuples([('Name', 'Surname'),
('Marks', 'Percentage')])

# create multi-index dataframe
student_df = pd.DataFrame([('Joe', 91.56), ('Nat', 87.90), ('Harry', 70.10), 
                           ('Sam', 65.48), ("Jill", 72), ("Jane", 80)],
                          index=index, columns=columns)

bottomRows = student_df.tail()
print(bottomRows)
```

**Output:**
```text
Name      Marks
                   Surname Percentage
Standard   Class                     
Standard 1 Class B     Nat      87.90
Standard 2 Class A   Harry      70.10
           Class B     Sam      65.48
Standard 3 Class A    Jill      72.00
           Class B    Jane      80.00
```

## Select value using row and column labels using `DataFrame.at`

There are cases in the field of Data Science that we need to access a specific element of the DataFrame using its column label and row index. In such cases, we can use the **`DataFrame.at`** property and pass the row index and column labels of the value to access as parameters. This property can be used with Multi-index DataFrame as well.

>**Note:** It throws **`KeyError`** if the label does not exist in DataFrame.

**Example:**

In the below example, after we use the **`DataFrame.at[2,"Age"]`** function, we get 19 as the output because 19 is the value present at row 2 and column Age.

<div>

</div>

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry',], 'Age': [20, 21, 19], 
                'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)

value = student_df.at[2,"Age"]
print(value)  # --> Output: 19
```

**Output:**
```text
19
```

## Set specific value in pandas DataFrame

When we want to update the value of the particular element from DataFrame based on its column label and row index, we can use DataFrame.at property.

**Example:**

In the below example, after we have applied **`DataFrame.at[2,"Age"]=50`** on our DataFrame, the value at that position changed from 19 to 50.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry',], 'Age': [20, 21, 19],
                'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df.at[2,"Age"])

# change the value
student_df.at[2,"Age"] = 50
print(student_df.at[2,"Age"])
```

**Output:**
```text
19
50
```

## Select value using row and column position using DataFrame.iat

We want to access a specific element from a very large DataFrame, but we do not know its column label or row index. We can still access such an element using its column and row positions. For that, we can use **`DataFrame.iat`** property of python pandas. Unlike **`DataFrame.at`** it can work on the row and column index position of the DataFrame.

>**Note:** Index positions starts at 0.

**Example:**

In the below example, we access the second row and the third column using **`DataFrame.iat[1,2]`**.

<div>

</div>

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry',], 'Age': [20, 21, 19],
                'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)

value = student_df.iat[1,2]
print(value) # --> Output: 77.80
```

**Output:**
```text
77.8
```

## Set specific value in pandas DataFrame

When we want to update the value of the particular element from DataFrame based on its column and row position, we can use **`DataFrame.iat`** property.

**Example:**

In the below example, we change the value at the second row and the third column using **`DataFrame.iat[1,2]=90`**.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 
                'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df.iat[1,2])

# change value
student_df.iat[1,2]=90
print(student_df.iat[1,2])
```

**Output:**
```text
77.8
90.0
```

---

## 📘 Python Pandas Exercise 2
*Source: `7. Python Pandas/3. Python Pandas Exercise 2.ipynb`*

# Python Pandas

**[Pandas](https://pandas.pydata.org/)** is an open-source, BSD-licensed Python library. Pandas is a handy and useful data-structure tool for analyzing large and complex data.

In this tutorial we will practice: 

* DataFrame, 
* Data Selection, 
* Group-By, 
* Series, 
* Sorting,  
* Searching,  
* statistics. 

Let us practice Data analysis using Pandas.

In this exercise, we are using **automobile_data.csv** for data analysis. This Dataset has different characteristics of an auto such as body-style, wheel-base, engine-type, price, mileage, horsepower, etc.

**What included in this Pandas exercise?**

It contains 10 questions. The solution is provided for each question.
Each question includes a specific Pandas topic you need to learn.
When you complete each question, you get more familiar with data analysis using pandas.

### Exercise 1: From the given dataset print the first and last five rows

```python
import pandas as pd

df = pd.read_csv("automobile_data.csv")  # just give the name of file only if the file is in the same folder.
df.head(5)
```

**Output:**
```text
index      company   body-style  wheel-base  length engine-type  \
0      0  alfa-romero  convertible        88.6   168.8        dohc   
1      1  alfa-romero  convertible        88.6   168.8        dohc   
2      2  alfa-romero    hatchback        94.5   171.2        ohcv   
3      3         audi        sedan        99.8   176.6         ohc   
4      4         audi        sedan        99.4   176.6         ohc   

  num-of-cylinders  horsepower  average-mileage    price  
0             four         111               21  13495.0  
1             four         111               21  16500.0  
2              six         154               19  16500.0  
3             four         102               24  13950.0  
4             five         115               18  17450.0
```

```python
import pandas as pd

df = pd.read_csv("automobile_data.csv")
df.tail(5)
```

**Output:**
```text
index     company body-style  wheel-base  length engine-type  \
56     81  volkswagen      sedan        97.3   171.7         ohc   
57     82  volkswagen      sedan        97.3   171.7         ohc   
58     86  volkswagen      sedan        97.3   171.7         ohc   
59     87       volvo      sedan       104.3   188.8         ohc   
60     88       volvo      wagon       104.3   188.8         ohc   

   num-of-cylinders  horsepower  average-mileage    price  
56             four          85               27   7975.0  
57             four          52               37   7995.0  
58             four         100               26   9995.0  
59             four         114               23  12940.0  
60             four         114               23  13415.0
```

### Exercise 2: Clean the dataset and update the CSV file

**Hint:** Replace all column values which contain **`?`**, **`n.a`**, or **`NaN`**.

```python
df = pd.read_csv("automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print (df)


df.to_csv("automobile_data1.csv")
```

**Output:**
```text
index      company   body-style  wheel-base  length engine-type  \
0       0  alfa-romero  convertible        88.6   168.8        dohc   
1       1  alfa-romero  convertible        88.6   168.8        dohc   
2       2  alfa-romero    hatchback        94.5   171.2        ohcv   
3       3         audi        sedan        99.8   176.6         ohc   
4       4         audi        sedan        99.4   176.6         ohc   
..    ...          ...          ...         ...     ...         ...   
56     81   volkswagen        sedan        97.3   171.7         ohc   
57     82   volkswagen        sedan        97.3   171.7         ohc   
58     86   volkswagen        sedan        97.3   171.7         ohc   
59     87        volvo        sedan       104.3   188.8         ohc   
60     88        volvo        wagon       104.3   188.8         ohc   

   num-of-cylinders  horsepower  average-mileage    price  
0              four         111               21  13495.0  
1              four         111
... [Output truncated for brevity]
```

### Exercise 3: Find the most expensive car company name

Print most expensive car’s company name and price.

```python
import pandas as pd
df = pd.read_csv("automobile_data1.csv")
df = df [['company','price']][df.price==df['price'].max()]
df

#or

#df=df.groupby(["company"]).sum().sort_values("price", ascending=False)
#df
```

**Output:**
```text
company    price
35  mercedes-benz  45400.0
```

### Exercise 4: Print All Toyota Cars details

```python
import pandas as pd

df = pd.read_csv("automobile_data1.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
toyotaDf

#or

#df[(df.company == 'toyota')]
```

**Output:**
```text
Unnamed: 0  index company body-style  wheel-base  length engine-type  \
48          48     66  toyota  hatchback        95.7   158.7         ohc   
49          49     67  toyota  hatchback        95.7   158.7         ohc   
50          50     68  toyota  hatchback        95.7   158.7         ohc   
51          51     69  toyota      wagon        95.7   169.7         ohc   
52          52     70  toyota      wagon        95.7   169.7         ohc   
53          53     71  toyota      wagon        95.7   169.7         ohc   
54          54     79  toyota      wagon       104.5   187.8        dohc   

   num-of-cylinders  horsepower  average-mileage    price  
48             four          62               35   5348.0  
49             four          62               31   6338.0  
50             four          62               31   6488.0  
51             four          62               31   6918.0  
52             four          62               27   7898.0  
53             four          62    
... [Output truncated for brevity]
```

### Exercise 5: Count total cars per company

```python
import pandas as pd

df = pd.read_csv("automobile_data1.csv")
df['company'].value_counts()
```

**Output:**
```text
toyota           7
bmw              6
nissan           5
mazda            5
volkswagen       4
audi             4
mitsubishi       4
mercedes-benz    4
isuzu            3
alfa-romero      3
honda            3
jaguar           3
chevrolet        3
porsche          3
volvo            2
dodge            2
Name: company, dtype: int64
```

### Exercise 6: Find each company’s Higesht price car

```python
import pandas as pd

df = pd.read_csv("automobile_data1.csv")
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['company','price'].max()
priceDf
```

**Output:**
```text
company    price
company                              
alfa-romero      alfa-romero  16500.0
audi                    audi  18920.0
bmw                      bmw  41315.0
chevrolet          chevrolet   6575.0
dodge                  dodge   6377.0
honda                  honda  12945.0
isuzu                  isuzu   6785.0
jaguar                jaguar  36000.0
mazda                  mazda  18344.0
mercedes-benz  mercedes-benz  45400.0
mitsubishi        mitsubishi   8189.0
nissan                nissan  13499.0
porsche              porsche  37028.0
toyota                toyota  15750.0
volkswagen        volkswagen   9995.0
volvo                  volvo  13415.0
```

### Exercise 7: Find the average mileage of each car making company

```python
import pandas as pd

df = pd.read_csv("automobile_data1.csv")
car_Manufacturers = df.groupby('company')
mileageDf = car_Manufacturers['company','average-mileage'].mean()
mileageDf


#or

#company_grp=df.groupby('company')
#company_grp.agg({
#    'average-mileage':np.mean
#})
```

**Output:**
```text
average-mileage
company                       
alfa-romero          20.333333
audi                 20.000000
bmw                  19.000000
chevrolet            41.000000
dodge                31.000000
honda                26.333333
isuzu                33.333333
jaguar               14.333333
mazda                28.000000
mercedes-benz        18.000000
mitsubishi           29.500000
nissan               31.400000
porsche              17.000000
toyota               28.714286
volkswagen           31.750000
volvo                23.000000
```

### Exercise 8: Sort all cars by Price column

```python
import pandas as pd

carsDf = pd.read_csv("automobile_data1.csv")
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
carsDf.head(5)
```

**Output:**
```text
Unnamed: 0  index        company   body-style  wheel-base  length  \
35          35     47  mercedes-benz      hardtop       112.0   199.2   
11          11     14            bmw        sedan       103.5   193.8   
34          34     46  mercedes-benz        sedan       120.9   208.1   
46          46     62        porsche  convertible        89.5   168.9   
12          12     15            bmw        sedan       110.0   197.0   

   engine-type num-of-cylinders  horsepower  average-mileage    price  
35        ohcv            eight         184               14  45400.0  
11         ohc              six         182               16  41315.0  
34        ohcv            eight         184               14  40960.0  
46        ohcf              six         207               17  37028.0  
12         ohc              six         182               15  36880.0
```

### Exercise 9: Concatenate two data frames using the following conditions

**Hint:** Create two data frames using the following two **[dictionary](http://localhost:8888/notebooks/01_Learn_Python4Data/02_Python_Datatypes/005_Python_Dictionary.ipynb)**.

```python
import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
carsDf1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
carsDf2 = pd.DataFrame.from_dict(japaneseCars)

carsDf = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
carsDf
```

**Output:**
```text
Company   Price
Germany 0         Ford   23845
        1     Mercedes  171995
        2          BMV  135925
        3         Audi   71400
Japan   0       Toyota   29995
        1        Honda   23600
        2       Nissan   61500
        3  Mitsubishi    58900
```

### Exercise 10: Merge two data frames using the following condition

**Hint:** Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.

```python
import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carPriceDf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
carsDf
```

**Output:**
```text
Company   Price  horsepower
0  Toyota   23845         141
1   Honda   17995          80
2     BMV  135925         182
3    Audi   71400         160
```

---

## 📘 Python Pandas Dataframe Drop Columns
*Source: `7. Python Pandas/4. Python Pandas DataFrame drop columns.ipynb`*

# Drop columns in pandas DataFrame

Datasets could be in any shape and form. To optimize the data analysis, we need to remove some data that is redundant or not required. This article aims to discuss all the cases of dropping single or multiple columns from a **Pandas DataFrame**.

The following functions are discussed in this article in detail:

* **`df.drop(columns = ['col1','col2'...])`**
* **`df.pop('col_name')`**
* **`del df['col_name']`**

In the last section, we have shown the comparison of these functions. So stay tuned…

## The `DataFrame.drop()` function

We can use this pandas function to remove the columns or rows from simple as well as multi-index DataFrame.

**Syntax:**
```python
DataFrame.drop(labels=None, axis=1, columns=None, level=None, inplace=False, errors='raise')
```

**Parameters:**

1. **`labels`**: It takes a list of column labels to drop.
2. **`axis`**: It specifies to drop columns or rows. Set a **`axis`** to **1** or **columns** to drop columns. By default, it drops the rows from DataFrame.
3. **`columns`**: It is an alternative to **`axis='columns'`**. It takes a single column label or list of column labels as input.
4. **`level`**: It is used in the case of a MultiIndex DataFrame to specify the level from which the labels should be removed. It takes a level position or level name as input.
5. **`inplace`**: It is used to specify whether to return a new DataFrame or update an existing one. It is a boolean flag with default **`False`**.
6. **`errors`**: It is used to suppress **`KeyError`** error if a column is not present. It takes the following 1. inputs:
    * **`ignore`**: It suppresses the error and drops only existing labels.
    * **`raise`**: Throws the errors if the column does not exist. It is the default case.

**Returns:**

* It returns the DataFrame with dropped columns or None if **`inplace=True`**
* It also raises **`KeyError`** if labels are not found.

## Drop single column

We may need to delete a single or specific column from a DataFrame.

In the below example we drop the **`age`** column from the DataFrame using **`df.drop(columns = 'col_name')`**

<div>

</div>

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)

# drop column
student_df = student_df.drop(columns='age')

print(student_df)
```

**Output:**
```text
name  age  marks
0  Joe   20   85.1
1  Nat   21   77.8
  name  marks
0  Joe   85.1
1  Nat   77.8
```

## Drop multiple columns

Use any of the following two parameters of **`DataFrame.drop()`** to delete multiple columns of DataFrame at once.

* Use the **`column`** parameter and pass the list of column names you want to remove.
* Set the **`axis=1`** and pass the list of column names.

**Example:**

Let’s see how to drop multiple columns from the DataFrame.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80]}

student_df = pd.DataFrame(student_dict)
print(student_df.columns.values)

# drop 2 columns at a time
student_df = student_df.drop(columns=['age', 'marks'])

print(student_df.columns.values)
```

**Output:**
```text
['name' 'age' 'marks']
['name']
```

### Using drop with `axis='columns'` or `axis=1`

Let’s see how to drop using the axis-style convention. This is a new approach. (This approach makes this method match the rest of the pandas API) .

Use the axis parameter of a **`DataFrame.drop()`** to delete columns. The axis can be a row or column. The column axis represented as 1 or ‘columns’.

Set **`axis=1`** or **`axis='columns'`** and pass the list of column names you want to remove..

**Example**

Let’s see how to drop **`age`** and **`marks`** columns.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Original dataframe:\n",student_df)

student_df = student_df.drop(['age', 'marks'], axis='columns')
print("After droping columns in dataframe:\n", student_df)

# alternative both produces same result
#student_df = student_df.drop(['age', 'marks'], axis=1)
#print("After droping columns in dataframe:\n", student_df)
```

**Output:**
```text
Original dataframe:
   name  age  marks
0  Joe   20   85.1
1  Nat   21   77.8
After droping columns in dataframe:
   name
0  Joe
1  Nat
```

## Drop column in place

In the above examples, whenever we executed drop operations, pandas created a new copy of DataFrame because the modification is not in place.

Parameter **`inplace`** is used to indicate if drop column from the existing DataFrame or create a copy of it.

* If the **`inplace=True`** then it updates the existing DataFrame and does not return anything.
* If the **`inplace=False`** then it creates a new DataFrame with updated changes and returns it.

>**Note:** Set **`inplace=True`** when we are doing function chaining to avoid assigning the result back to a variable as we are performing modifications in place.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80]}

student_df = pd.DataFrame(student_dict)
print(student_df.columns.values)

# drop columns in place
student_df.drop(columns=['age', 'marks'], inplace=True)

print(student_df.columns.values)
```

**Output:**
```text
['name' 'age' 'marks']
['name']
```

## Drop column by suppressing errors

By default, The **`DataFrame.drop()`**  throws **`KeyError`** if the column you are trying to delete does not exist in the dataset.

If we want to drop the column only if exists then we can suppress the error by using the parameter **`errors`**.

* Set **`errors='ignore'`** to not throw any errors.
* Set **`errors='raised'`** to throw **`KeyError`** for the unknown columns

**Example:**

In the below example, we are trying to drop the column which does not exist in the DataFrame.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)

# supress error
student_df = student_df.drop(columns='salary', errors='ignore')  # No change in the student_df

# raise error
student_df = student_df.drop(columns='salary')  # KeyError: "['salary'] not found in axis"
```

**Output:**
```text
name  age  marks
0  Joe   20   85.1
1  Nat   21   77.8
```

## Drop column by index position

If there is a case where we want to drop columns in the DataFrame, but we do not know the name of the columns still we can delete the column using its index position.

>**Note:** Column index starts from 0 (zero) and it goes till the last column whose index value will be **`len(df.columns)-1`**.

### Drop the last column

Assume you want to drop the first column or the last column of the DataFrame without using the column name.

In such cases, use the DataFrame.columns attribute to delete a column of the DataFrame based on its index position. Simply pass **`df.columns[index]`** to the columns parameter of the **`DataFrame.drop()`**.

**Example**

In the below example, we are dropping the last column of the DataFrame using **`df.columns[last_index]`**.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df.columns.values)

# find position of the last column and drop
pos = len(student_df.columns) - 1
student_df = student_df.drop(columns=student_df.columns[pos])
print(student_df.columns.values)

# delete column present at index 1
# student_df.drop(columns = student_df.columns[1])
```

**Output:**
```text
['name' 'age' 'marks']
['name' 'age']
```

### Drop range of columns using `iloc`

There could be a case when we need to delete the fourth column from the dataset or need to delete a range of columns. We can use **`DataFrame.iloc`** to select single or multiple columns from the DataFrame.

We can use **`DataFrame.iloc`** in the **`columns`** parameter to specify the index position of the columns which need to drop.

**Example:**

Let’s see how we can drop the range of the columns based on the index position. In the below example, we are dropping columns from index position 1 to 3 (exclusive).

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df.columns.values)

# drop column from 1 to 3
student_df = student_df.drop(columns=student_df.iloc[:, 1:3])

print(student_df.columns.values)
```

**Output:**
```text
['name' 'age' 'marks']
['name']
```

### Drop first n columns

If we need to delete the first ‘n’ columns from a DataFrame, we can use **`DataFrame.iloc`** and the **Python range()** function to specify the columns’ range to be deleted.

We need to use the built-in function **`range()`** with **`columns`** parameter of **`DataFrame.drop()`**.

**Example:**

In the below example, we are dropping the first two columns from a DataFrame.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80], "class": ["A", "B"],
                "city": ["London", "Zurich"]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping: \n", student_df.columns.values)

# drop column 1 and 2
student_df = student_df.drop(columns=student_df.iloc[:, range(2)])

# print only columns
print("\nAfter dropping: \n", student_df.columns.values)
```

**Output:**
```text
Before dropping: 
 ['name' 'age' 'marks' 'class' 'city']

After dropping: 
 ['marks' 'class' 'city']
```

## Drop column from multi-index DataFrame

DataFrame can have multiple column headers, such DataFrame is called a **multi-index** DataFrame. Such headers are divided into the levels where the first header is at level 0, the second header is at level 1, and so on.

We can drop a column from any level of multi-index DataFrame. By default, it drops columns from all the levels, but we can use a parameter **`level`** to drop from a particular level only.

We need to pass a level name or level index as **`level=level_index`**.

Below is the multi-index DataFrame with two column headers.

<div>

</div>

**Example:**

Let’s see how we can drop column **`marks`** from level 1.

>**Note:** If we do not provide a **`level`** parameter then it will drop the column from all the levels if exist.

```python
import pandas as pd

# create column header
col = pd.MultiIndex.from_arrays([['Class A', 'Class A', 'Class B', 'Class B'],
                                 ['Name', 'Marks', 'Name', 'Marks']])
# create dataframe from 2darray
student_df = pd.DataFrame([['Joe', '85.10', 'Nat', '77.80'], ['Harry', '91.54', 'Sam', '68.55']], columns=col)
print("Before dropping column: \n", student_df)

# drop column
student_df = student_df.drop(columns=['Marks'], level=1)
print("\nAfter dropping column: \n", student_df)
```

**Output:**
```text
Before dropping column: 
   Class A        Class B       
     Name  Marks    Name  Marks
0     Joe  85.10     Nat  77.80
1   Harry  91.54     Sam  68.55

After dropping column: 
   Class A Class B
     Name    Name
0     Joe     Nat
1   Harry     Sam
```

## Drop column using a function

We can also use the function to delete columns by applying some logic or based on some condition. We can use built-in as well as user-defined functions to drop columns.

### Drop all the columns using `loc`

If we want to drop all the columns from DataFrame we can easily do that using **`DataFrame.loc`** in the **`columns`** parameter of **`DataFrame.drop()`**.

**`DataFrame.loc`** is used to specify the column labels which need to delete. If we do not specify any column labels like **`df.loc[:]`** then it will drop all the columns in the DataFrame.

**Example:**

In the below example, we are dropping all the columns from the student DataFrame.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping column: \n", student_df.columns.values)

# drop column 1 and 2
student_df = student_df.drop(columns=student_df.loc[:])

# print only columns
print("\nAfter dropping column: \n", student_df.columns.values)
```

**Output:**
```text
Before dropping column: 
 ['name' 'age' 'marks']

After dropping column: 
 []
```

## Drop column using pandas `DataFrame.pop()` function

If we want to delete a single column then we can also do that using **`DataFrame.pop(col_label)`** function. We need to pass a column label that needs to delete.

It removes the column in-place by updating the existing DataFrame. It raises **`KeyError`** if the column is not found.

>**Note:** It can be used to drop a column only. It cannot drop multiple columns or row(s).

**Example:**

Let’s see how we can drop the **`age`** column from a student DataFrame.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping column: \n", student_df)

# drop column
student_df.pop('age')

print("\nAfter dropping column: \n", student_df)
```

**Output:**
```text
Before dropping column: 
   name  age  marks
0  Joe   20   85.1
1  Nat   21   77.8

After dropping column: 
   name  marks
0  Joe   85.1
1  Nat   77.8
```

## Drop column using pandas DataFrame delete

We can also use the pandas inbuilt function **`del`** to drop a single column from a DataFrame. It is a very simplified way of dropping the column from a DataFrame.

We need to select the column of DataFrame which needs to be deleted and pass it as **`del df[col_label]`**.

>**Note:** It can be used to drop a column only. It cannot drop multiple columns or row(s).

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat"], "age": [20, 21], "marks": [85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping column: \n", student_df)

# drop column
del student_df['age']

print("\nAfter dropping column: \n", student_df)
```

**Output:**
```text
Before dropping column: 
   name  age  marks
0  Joe   20   85.1
1  Nat   21   77.8

After dropping column: 
   name  marks
0  Joe   85.1
1  Nat   77.8
```

## Compare DataFrame `drop()` vs. `pop()` vs. `del`

| Features | **`drop()`** | **`pop()`** | **`del`** |
|:---- |:---- |:---- | :---- |
| **Operates on axis**               | **columns and rows** | **only column**   | **only column** |
| **Delete multiple columns**        | **Yes**              | **No**            | **No** |
| **Drop in-place or return a copy** | **Both**             | **Only in-place** | **Only in-place** |
| **Performance**                    | **Fast**             | **Slow**          | **Slow** |

---

## 📘 Python Pandas Dataframe Drop Duplicates
*Source: `7. Python Pandas/5. Python Pandas DataFrame drop duplicates.ipynb`*

# Drop duplicates in pandas DataFrame

In this class, we learn to remove duplicates from the **Pandas DataFrame**.

Data is gathered from various sources. It may not be in the proper form. It contains garbage values and duplicate data. Before analyzing a dataset, it must be clean and precise.

## The `DataFrame.drop_duplicates()` function

This function is used to remove the duplicate rows from a DataFrame.

**Syntax:**
```python
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
```

**Parameters:**

1. **`subset`**: By default, if the rows have the same values in all the columns, they are considered duplicates. This parameter is used to specify the columns that only need to be considered for identifying duplicates.
2. **`keep`**: Determines which duplicates (if any) to keep. It takes inputs as,
    * **first** – Drop duplicates except for the first occurrence. This is the default behavior.
    * **last** – Drop duplicates except for the last occurrence.
    * **False** – Drop all duplicates.
3. **`inplace`**: It is used to specify whether to return a new DataFrame or update an existing one. It is a boolean flag with default False.
4. **`ignore_index`**: It is a boolean flag to indicate if row index should be reset after dropping duplicate rows. **`False`**: It keeps the original row index. **`True`**: It reset the index, and the resulting rows will be labeled 0, 1, …, n – 1.

**Returns:**

* It returns the DataFrame with dropped columns or None if **`inplace=True`**

## Drop duplicates but keep first

When we have the DataFrame with many duplicate rows that we want to remove we use **`DataFrame.drop_duplicates()`**.

The rows that contain the same values in all the columns then are identified as duplicates. If the row is duplicated then by default **`DataFrame.drop_duplicates()`** keeps the first occurrence of that row and drops all other duplicates of it.

**Example:**

<div>

</div>

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry", "Joe", "Nat"], "age": [20, 21, 19, 20, 21],
                "marks": [85.10, 77.80, 91.54, 85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping duplicates: \n", student_df)

# drop duplicate rows
student_df = student_df.drop_duplicates()

print("\nAfter dropping column: \n", student_df)
```

**Output:**
```text
Before dropping duplicates: 
     name  age  marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
3    Joe   20  85.10
4    Nat   21  77.80

After dropping column: 
     name  age  marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
```

## Drop duplicates from defined columns

By default, **`DataFrame.drop_duplicate()`** removes rows with the same values in all the columns. But, we can modify this behavior using a subset parameter.

For example, **`subset=[col1, col2]`** will remove the duplicate rows with the same values in specified columns only, i.e., **`col1`** and **`col2`**.

**Example:**

In the below example, rows for **`Nat`** and **`Sam`** are removed even though their names are different because only **`age`** and **`marks`** columns are considered to check for duplicates.

<div>

</div>

```python
import pandas as pd

student_dict = {"name":["Joe","Nat","Harry","Sam" ], "age":[20,21,19,21], "marks":[85.10, 77.80, 91.54, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping duplicates: \n", student_df)

# drop duplicate rows
student_df = student_df.drop_duplicates(subset=['age','marks'])

print("\nAfter dropping column: \n", student_df)
```

**Output:**
```text
Before dropping duplicates: 
     name  age  marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
3    Sam   21  77.80

After dropping column: 
     name  age  marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
```

## Drop duplicates but keep last

Let’s consider the case where we have a row that is duplicated multiple times in the DataSet. In such a case, To keep only one occurrence of the duplicate row, we can use the **`keep`** parameter of a **`DataFrame.drop_duplicate()`**, which takes the following inputs:

* **first** – Drop duplicates except for the first occurrence of the duplicate row. This is the default behavior.
* **last** – Drop duplicates except for the last occurrence of the duplicate row.
* **False** – Drop all the rows which are duplicate.

**Example:**

In the below example, we are dropping the last occurrence of the duplicate rows using **`keep='last'`**.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry", "Nat"], "age": [20, 21, 19, 21], "marks": [85.10, 77.80, 91.54, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping duplicates: \n", student_df)

# drop duplicate rows
student_df = student_df.drop_duplicates(keep='last')

print("\nAfter dropping column: \n", student_df)
```

**Output:**
```text
Before dropping duplicates: 
     name  age  marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
3    Nat   21  77.80

After dropping column: 
     name  age  marks
0    Joe   20  85.10
2  Harry   19  91.54
3    Nat   21  77.80
```

## Drop all duplicates

As explained in the above section, by default, **`DataFrame.drop_duplicates()`** keeps the duplicate row’s first occurrence and removes all others.

If we need to drop all the duplicate rows, then it can be done by using keep=False, as shown below.

<div>

</div>

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry", "Nat"], "age": [20, 21, 19, 21], "marks": [85.10, 77.80, 91.54, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping duplicates: \n", student_df)

# drop all duplicate rows
student_df = student_df.drop_duplicates(keep=False)

print("\nAfter dropping column: \n", student_df)
```

**Output:**
```text
Before dropping duplicates: 
     name  age  marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
3    Nat   21  77.80

After dropping column: 
     name  age  marks
0    Joe   20  85.10
2  Harry   19  91.54
```

## Drop duplicates in place

By default, **`DataFrame.drop_duplicates()`** removes the duplicates and returns the copy of the DataFrame.

But, if we want to make changes in the existing DataFrame, then set the flag **`inplace=True`**. It can be used when the drop operation is part of the function chaining.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry", "Joe", "Nat"], "age": [20, 21, 19, 20, 21],
                "marks": [85.10, 77.80, 91.54, 85.10, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping duplicates: \n", student_df)

# drop duplicate rows
student_df.drop_duplicates(inplace=True)

print("\nAfter dropping column: \n", student_df)
```

**Output:**
```text
Before dropping duplicates: 
     name  age  marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
3    Joe   20  85.10
4    Nat   21  77.80

After dropping column: 
     name  age  marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
```

## Drop duplicates and reset the index

When we drop the rows from DataFrame, by default, it keeps the original row index as is. But, if we need to reset the index of the resultant DataFrame, we can do that using the **`ignore_index`** parameter of **`DataFrame.drop_duplicate()`**.

* If **`ignore_index=True`**, it reset the row labels of resultant DataFrame to 0, 1, …, n – 1.
* If **`ignore_index=False`** it does not change the original row index. By default, it is **False**.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry", "Nat"], "age": [20, 21, 19, 21], "marks": [85.10, 77.80, 91.54, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict, index=['a', 'b', 'c', 'd'])
print("Before dropping duplicates: \n", student_df)

# drop duplicate rows
student_df = student_df.drop_duplicates(keep=False, ignore_index=True)

print("\nAfter dropping column: \n", student_df)
```

**Output:**
```text
Before dropping duplicates: 
     name  age  marks
a    Joe   20  85.10
b    Nat   21  77.80
c  Harry   19  91.54
d    Nat   21  77.80

After dropping column: 
     name  age  marks
0    Joe   20  85.10
1  Harry   19  91.54
```

---

## 📘 Python Pandas Dataframe Drop Columns With Na
*Source: `7. Python Pandas/6. Python Pandas DataFrame drop columns with NA.ipynb`*

# Drop columns with NA in pandas DataFrame

This article covers all the cases to remove columns from **Pandas DataFrame** that contains missing or NA values.

For multiple reasons, it could happen that data in the Dataset is missing or not available. It is a very usual case where we need to clean the data before start analyzing it.

## The `DataFrame.dropna()` function

We can use this pandas function to remove columns from the DataFrame with values Not Available(NA).

**Syntax:**
```python
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```

**Parameters:**

1. **`axis`**: It determines the axis to remove. Set it to 1 or **`column`** to remove columns containing missing values. By default, it removes rows with NA from DataFrame.
2. **`how`**: It takes the following inputs:
    * **`‘any’`**: This is the default case to drop the column if it has at least one value missing.
    * **`‘all’`**: Drop the column only if it has all the values as NA.
3. **`thresh`**: It applies a condition to drop the columns only if it does not contain the required number of values. It takes an int as input.
4. **`subset`**: While dropping columns, it is used to specify the list of rows to be considered to find NA.
5. **`inplace`**: It is used to specify whether to return a new DataFrame or update an existing one. It is a boolean flag with default **`False`**.

**Returns:**

* It returns the DataFrame with dropped NA or None if **`inplace=True`**

## Drop column where at least one value is missing

There is a case when we cannot process the dataset with missing values. If we need to drop such columns that contain NA, we can use the **`axis=columns`** parameter of **`DataFrame.dropna()`** to specify deleting the columns.

By default, it removes the column where one or more values are missing.

**Example:**

In the below example, it drops column **`marks`** because it contains NaN.

<div>

</div>

```python
import pandas as pd
import numpy as np

student_dict = {"name": ["Joe", "Sam", "Harry"], "age": [20, 21, 19], "marks": [85.10, np.nan, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping column NA: \n", student_df)

# drop column with NaN
student_df = student_df.dropna(axis='columns')

print("\nAfter dropping column NA: \n", student_df)
```

**Output:**
```text
Before dropping column NA: 
     name  age  marks
0    Joe   20  85.10
1    Sam   21    NaN
2  Harry   19  91.54

After dropping column NA: 
     name  age
0    Joe   20
1    Sam   21
2  Harry   19
```

## Drop column where all values are missing

We can drop an empty column from DataFrame using **`DataFrame.dropna()`**.

We need to use how parameter as follows:

* If **`how='all'`**, it drops the column where all the values are NA.
* By default, **`how='any'`**, it removes the columns where one or more values are NA.

**Example**

The below example shows that it only drops the **`age`** column where all values are NaN. Other columns are not dropped even if it contains NaN..

```python
import pandas as pd
import numpy as np

student_dict = {"name": ["Joe", "Sam", np.nan, "Harry"], "age": [np.nan, np.nan, np.nan, np.nan],
                "marks": [85.10, np.nan, np.nan, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping column NA: \n", student_df)

# drop column with NaN
student_df = student_df.dropna(axis='columns', how='all')

print("\nAfter dropping column NA: \n", student_df)
```

**Output:**
```text
Before dropping column NA: 
     name  age  marks
0    Joe  NaN  85.10
1    Sam  NaN    NaN
2    NaN  NaN    NaN
3  Harry  NaN  91.54

After dropping column NA: 
     name  marks
0    Joe  85.10
1    Sam    NaN
2    NaN    NaN
3  Harry  91.54
```

## Drop column with the number of NA

While cleaning the dataset, we can keep the columns with at least some data available in it else drop otherwise.

We need to use the parameter **`thresh=no_of_nonNA_values`** of **`DataFrame.drop()`** to specify the number of values that must be available in the column. Else, drop the column.

**Example**

In the below example, we keep the column where at least three or more values are available and drop the column if the condition is not met.

<div>

</div>

```python
import pandas as pd
import numpy as np

student_dict = {"name": ["Joe", "Sam", np.nan, "Harry"], "age": [np.nan, np.nan, np.nan, np.nan],
                "marks": [85.10, np.nan, np.nan, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping column NA: \n", student_df)

# keep column with 3 or more non-NA values
student_df = student_df.dropna(axis='columns', thresh=3)

print("\nAfter dropping column NA: \n", student_df)
```

**Output:**
```text
Before dropping column NA: 
     name  age  marks
0    Joe  NaN  85.10
1    Sam  NaN    NaN
2    NaN  NaN    NaN
3  Harry  NaN  91.54

After dropping column NA: 
     name
0    Joe
1    Sam
2    NaN
3  Harry
```

## Drop NA from defined rows

Suppose we are interested in dropping the column only if it contains null values in some particular rows. For example, consider when we need to drop a column if it does not have data in its initial rows.

In such a case, we can use **`subset=[row1, row2]`** of **`DataFrame.dropna()`** to specify the list of row indexes so that it drops the columns containing missing values in these rows only, i.e., row1 and row2 in this case.

**Example:**

Let’s see how to delete a column only if it contains the empty value in row 0 or 2, otherwise do not delete the column.

<div>

</div>

```python
import pandas as pd
import numpy as np

student_dict = {"name": ["Joe", "Sam", "Harry"], "age": [np.nan, np.nan, np.nan], "marks": [85.10, np.nan, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping column NA: \n", student_df)

# drop marks column with NaN
student_df = student_df.dropna(axis='columns', subset=[0, 2])

print("\nAfter dropping column NA: \n", student_df)
```

**Output:**
```text
Before dropping column NA: 
     name  age  marks
0    Joe  NaN  85.10
1    Sam  NaN    NaN
2  Harry  NaN  91.54

After dropping column NA: 
     name  marks
0    Joe  85.10
1    Sam    NaN
2  Harry  91.54
```

## Drop column with missing values in place

We can drop columns from the existing DataFrame or by creating a copy of it. For that, we can use a flag **`inplace`** of **`DataFrame.dropna()`**.

* If the **`inplace=True`**, then it updates the DataFrame and returns None.
* If **`inplace=False`**, it returns the updated copy of the DataFrame.

**Example:**

As shown in the below example, we are dropping the column from the existing DataFrame without reassigning it to a new variable.

```python
import pandas as pd
import numpy as np

student_dict = {"name": ["Joe", "Sam", "Harry"], "age": [20, 21, 19], "marks": [85.10, np.nan, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before dropping row NA: \n", student_df)

# drop marks row with NaN
student_df.dropna(inplace=True)

print("\nAfter dropping row NA: \n", student_df)
```

**Output:**
```text
Before dropping row NA: 
     name  age  marks
0    Joe   20  85.10
1    Sam   21    NaN
2  Harry   19  91.54

After dropping row NA: 
     name  age  marks
0    Joe   20  85.10
2  Harry   19  91.54
```

## Drop duplicates and reset the index

When we drop the rows from DataFrame, by default, it keeps the original row index as is. But, if we need to reset the index of the resultant DataFrame, we can do that using the **`ignore_index`** parameter of **`DataFrame.drop_duplicate()`**.

* If **`ignore_index=True`**, it reset the row labels of resultant DataFrame to 0, 1, …, n – 1.
* If **`ignore_index=False`** it does not change the original row index. By default, it is **False**.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry", "Nat"], "age": [20, 21, 19, 21], "marks": [85.10, 77.80, 91.54, 77.80]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict, index=['a', 'b', 'c', 'd'])
print("Before dropping duplicates: \n", student_df)

# drop duplicate rows
student_df = student_df.drop_duplicates(keep=False, ignore_index=True)

print("\nAfter dropping column: \n", student_df)
```

**Output:**
```text
Before dropping duplicates: 
     name  age  marks
a    Joe   20  85.10
b    Nat   21  77.80
c  Harry   19  91.54
d    Nat   21  77.80

After dropping column: 
     name  age  marks
0    Joe   20  85.10
1  Harry   19  91.54
```

---

## 📘 Python Pandas Dataframe Rename Columns
*Source: `7. Python Pandas/7. Python Pandas DataFrame rename columns.ipynb`*

# Rename columns in Pandas DataFrame

In Python, renaming columns label is useful when working with a pandas Dataframe with no column names or want to rename a specific column’s names. This article covers all the cases of renaming column labels of the pandas **Pandas DataFrame**.

You will learn the following functions available in the pandas to rename columns of a simple DataFrame as well as multi-index DataFrame.

| Function | Description |
|:---- |:---- |
| **`df.rename(columns={'old': 'new'})`**    | **Rename column with label ‘old’ to ‘new’** |
| **`df.rename(index={0: 'I'})`**            | **Rename row index 0 (zero) to ‘I’** |
| **`df.add_prefix('$_')`**                  | **Rename all column labels by adding a prefix** |
| **`df.add_suffix('_$')`**                  | **Rename all column labels by adding a suffix** |
| **`df.set_axis(['a', 'b', 'c'], axis=1)`** | **Reassign column names to new names** |
| **`df.rename_axis("Sr.No.")`**             | **Assign a name to column header or row index header** |

## The `DataFrame.rename()` function

This is the most widely used pandas function for renaming columns and row indexes. Let’s see the syntax of it before moving to examples.

**Syntax:**
```python
DataFrame.rename(mapper=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='ignore')
```

**Parameters:**

1. **`mapper`**: It is used to specify new names for columns. It takes a Python dictionary or function as input.
2. **`columns`**: It is used to **specify new names for columns**. It takes to dictionary or function as input.
3. **`axis`**: Alternative to **`columns`**. It is used to specify the axis to apply with the mapper. **Column axis represented as 1 or ‘columns‘**. Default 0.
4. **`copy`**: It allows the copy of underlying data. It is a boolean flag with default True.
5. **`inplace`**: It is used to specify whether to return a new copy of a DataFrame or update existing ones. It is a boolean flag with default False.
6. **`level`**: In the case of a multi-index DataFrame, only rename labels in the specified level. It takes int or level name as input. The default value is None.
7. **`errors`**: It is either ‘ignore’ or ‘raise’. Default is ‘ignore’. If ‘raise’, raise a KeyError if the columns or index are not present. If ‘ignore’, existing keys will be renamed and extra keys will be ignored.

**Return value:**

* It returns a DataFrame with the renamed column and row labels or None if **`inplace=True`**.
* Also, It raises KeyError If any of the labels are not found in the selected axis when **`errors='raise'`**.

## Rename a single column

Sometimes it is required to rename the single or specific column names only.  Use the column parameter of **`DataFrame.rename()`** function and pass the columns to be renamed.

**Syntax:**
```python
df.rename(columns={'column_current_name': 'new_name'})
```

**Example:**

Now, let’s see how to rename the column **`marks`** to **`percentage`**.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
# before rename
print(student_df)

# after rename column
student_df = student_df.rename(columns={'marks': "percentage"})
print(student_df)
```

**Output:**
```text
name  age  marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
    name  age  percentage
0    Joe   20       85.10
1    Nat   21       77.80
2  Harry   19       91.54
```

## Rename multiple columns

Use any of the following two parameters of a **`DataFrame.rename()`** to rename multiple or all column labels at once.

* Use the **`column`** parameter and pass all column names you want to rename as a dictionary (old column name as a key and new column name as a value).
* Set the **`axis=1`** and pass column names you want to rename as a dictionary

**Example:**

Let’s see how to rename all three columns of a dataframe.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
# column names before rename
print("Columns before renaming\n", student_df.columns.values)

# rename all columns using mapping convention
student_df = student_df.rename(columns={'name': "a", 'age': "b", 'marks': "c"})
# after rename
print("\nColumns after renaming\n", student_df.columns.values)
```

**Output:**
```text
Columns before renaming
 ['name' 'age' 'marks']

Columns after renaming
 ['a' 'b' 'c']
```

## Using rename with `axis='columns'` or `axis=1`

Let’s see how to rename using the axis-style convention. This is a **new approach**.( This approach makes this method match the rest of the pandas API) .

Use the **`axis`** parameter of a **`df.rename()`** to rename columns and row index. The **`axis`** can be a row or column. The column axis represented as 1 or ‘columns’.

Set **`axis=1`** and pass column names you want to rename as a dictionary (Key-Value pairs).

**Example**

Let’s see how to rename all three columns.

```python
student_df = student_df.rename({'name': "a", 'age': "b", 'marks': "c"}, axis='columns')
# alternative both produces same result
student_df = student_df.rename({'name': "a", 'age': "b", 'marks': "c"}, axis=1)
```

## Rename columns in place

In the above examples, whenever we executed rename operations, pandas created a new copy of DataFrame because the modification is not-in place.

Specify **`inplace=True`** to rename the existing DataFrame rather than creating a copy of it.

* If the **`inplace=True`** then it updates the existing DataFrame and does not return anything.
* If the **`inplace=False`** then it creates a new DataFrame with updated changes and returns it.

>**Note:** You don’t need to assign the result back to a variable as we are performing modifications in place.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
# column names before rename
print(student_df.columns.values)

# rename columns inplace
student_df.rename(columns={'name': "a"}, inplace=True)
print(student_df.columns.values)
```

**Output:**
```text
['name' 'age' 'marks']
['a' 'age' 'marks']
```

## Rename column using a function

We can also use the function to rename column labels by applying some logic to it. We can use built-in as well as user-defined functions to rename columns.

**Example**

In the below example, we rename all column names to UPPER CASE using the string function **`str.upper`**.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
# before rename
print(student_df.columns.values)

# rename column names using function
student_df.rename(columns=str.upper, inplace=True)
# after rename
print(student_df.columns.values)
```

**Output:**
```text
['name' 'age' 'marks']
['NAME' 'AGE' 'MARKS']
```

## Use lambda expressions to rename

Also, you can use lambda expressions to rename column label or row index. Let’s see how to remove the first character from each column label using lambda.

```python
import pandas as pd

student_dict = {"#name": ["Joe", "Nat", "Harry"], "#age": [20, 21, 19], "#marks": [85.10, 77.80, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
# before rename
print(student_df.columns.values)

# remove first character of column names
student_df.rename(columns=lambda x: x[1:], inplace=True)
# after rename
print(student_df.columns.values)
```

**Output:**
```text
['#name' '#age' '#marks']
['name' 'age' 'marks']
```

## Rename columns by removing leading and trailing spaces

Use lambda expression to rename columns by removing leading and trailing spaces from the column names

**Example:**

```python
import pandas as pd

student_dict = {" name ": ["Joe", "Nat", "Harry"], " age   ": [20, 21, 19], "marks  ": [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
print(student_df.columns.values)
# output [' name ' ' age   ' 'marks  ']

# remove leading and trailing space from column names
student_df.rename(lambda x: x.strip(), axis='columns', inplace=True)
print(student_df.columns.values)
# Output ['name' 'age' 'marks']
```

**Output:**
```text
[' name ' ' age   ' 'marks  ']
['name' 'age' 'marks']
```

## Rename all columns with a list

Suppose we have a list of column names that we need to use to rename the existing DataFrame. In that case, we can pass the list of column labels to a **`DataFrame.columns`**  attributes as shown in the below example.

It will replace the existing names with the new names in the order you provide.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
# before rename
print(student_df.columns.values)

# rename column with list
student_df.columns = ['stud_name', 'stud_age', 'stud_marks']
# after rename
print(student_df.columns.values)
```

**Output:**
```text
['name' 'age' 'marks']
['stud_name' 'stud_age' 'stud_marks']
```

## Rename column by index position

If there is a case where we want to rename the first column or the last column in the DataFrame, but we do not know the column name still we can rename the column using a **`DataFrame.columns`** attribute.

>**Note:** Column index starts from 0 (zero) and it goes till the last column whose index value will be **`len(df.columns)-1`**.

**Example:**

In the below example, we are renaming the second column of the DataFrame using **`df.columns[1]`**.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
print("df.columns[2]:", student_df.columns[2])

# rename column present at index 2
student_df.rename(columns={student_df.columns[2]: 'percentage'}, inplace=True)
print("df.columns[2]:", student_df.columns[2])
```

**Output:**
```text
df.columns[2]: marks
df.columns[2]: percentage
```

## Raise error while renaming a column

By default, The **`DataFrame.rename()`** doesn’t throw any error if column names you tried to rename doesn’t exist in the dataset.

Do you want to throw an error in such cases?

If yes, then use the **`errors`** parameter of **`DataFrame.rename()`**.

* **`Set errors='raised'`** to throws **`KeyError`** for the unknown columns
* **`Set errors='ignore'`** to not throw any errors.

>**Note:** 
* If the new name mapping is not provided for some column label then it isn’t renamed.
* Extra labels in the mapping don’t throw an error.

**Example:**

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)

student_df.rename(columns={'unknownCol': "a"}, inplace=True, errors='raise')
print(student_df)

# Output: KeyError: "['unknownCol'] not found in axis"
```

## Rename column by adding prefix/suffix

We can rename the DataFrame columns using **`DataFrame.add_prefix()`** and **`DataFrame.add_suffix()`** functions. It appends the input string as a prefix or suffix to the column names respectively.

>**Note:** These functions are only applicable to column labels and not row index of the DataFrame.

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
print(student_df.columns.values)

# add prefix and suffix to column names
student_df = student_df.add_prefix("$_")
student_df = student_df.add_suffix("_$")

print(student_df.columns.values)
```

**Output:**
```text
['name' 'age' 'marks']
['$_name_$' '$_age_$' '$_marks_$']
```

## Rename column using `DataFrame.set_axis()`

Use the **`set_axis()`** method you to rename all the index or column labels with a list. Using this function we can reassign column headers or row index of the DataFrame.

This function is useful when working with a data set with no column names.

**Syntax:**
```python
DataFrame.set_axis(labels, axis=0, inplace=False)
```

**Parameters:**

1. **`labels`**: List of column names as an input.
2. **`axis`**: The axis to update. Set **`axis=1`** rename column headers. The default value is 0. (i.e., rename row index)
3. **`inplace`**: It is used to decide whether to return a new DataFrame instance or rename the existing one. It is a boolean flag with the default False. If it is True then it renames the existing DataFrame rather than creating a copy.

**Returns:**

It returns an object of type DataFrame else None if **`inplace=True`**.

>**Note:** Supply a list to the **`set_axis()`** method that is equal in length to the number of columns otherwise you will get an error.

**Example:**

```python
import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

student_df = pd.DataFrame(student_dict)
print(student_df.columns.values)

# reassign column headers
student_df.set_axis(['new_name', 'new_age', 'new_marks'], axis='columns', inplace=True)
print(student_df.columns.values)
```

**Output:**
```text
['name' 'age' 'marks']
['new_name' 'new_age' 'new_marks']
```

## Rename column in multi-index DataFrame

Pandas DataFrame can have single or multiple rows as column labels, i.e., a header to identify the columns. DataFrame with multiple headers is called a **multi-index DataFrame**.

The below diagram shows the multi-index DataFrame where header levels start with 0.

<div>

</div>

## Rename columns in all levels

We can apply **`DataFrame.rename()`** function on multi-index DataFrame.

In the below example, we use **`df.rename(columns={'old_col':'new_col'})`** which rename the column labels in all the levels of multi-index DataFrame.

```python
import pandas as pd

# create column header
col = pd.MultiIndex.from_arrays([['Class A', 'Class A', 'Class B', 'Class B'],
                                 ['Name', 'Marks', 'Name', 'Marks']])
# create dataframe from 2darray
student_df = pd.DataFrame([['Joe', '85.10', 'Nat', '77.80'], ['Harry', '91.54', 'Sam', '68.55']], columns=col)
print(student_df)

# rename column label
student_df = student_df.rename(columns={'Name': 'SName'})
print(student_df)
```

**Output:**
```text
Class A        Class B       
     Name  Marks    Name  Marks
0     Joe  85.10     Nat  77.80
1   Harry  91.54     Sam  68.55
  Class A        Class B       
    SName  Marks   SName  Marks
0     Joe  85.10     Nat  77.80
1   Harry  91.54     Sam  68.55
```

## Rename columns in defined level

It is the case when we have the same column labels in multiple levels of the multi-index DataFrame. But, we need to rename the column in a selected level only. Or we want to rename column labels of a particular level only in such cases we can use the level parameter of **`DataFrame.rename()`**.

This parameter is used to specify the **level name** or **level index** where we need to rename the columns.

**Example:**

In the below example, we rename the column label of only **level 1** to the upper case using the string function **`columns=str.upper`**.

```python
import pandas as pd

# create column header
col = pd.MultiIndex.from_arrays([['Class A', 'Class A', 'Class B', 'Class B'],
                                 ['Name', 'Marks', 'Name', 'Marks']])
# create dataframe from 2darray
student_df = pd.DataFrame([['Joe', '85.10', 'Nat', '77.80'], ['Harry', '91.54', 'Sam', '68.55']], columns=col)
print(student_df)

# rename column label in level 1
student_df = student_df.rename(columns=str.upper, level=1)
print(student_df)
```

**Output:**
```text
Class A        Class B       
     Name  Marks    Name  Marks
0     Joe  85.10     Nat  77.80
1   Harry  91.54     Sam  68.55
  Class A        Class B       
     NAME  MARKS    NAME  MARKS
0     Joe  85.10     Nat  77.80
1   Harry  91.54     Sam  68.55
```

---

## 📘 Python Pandas Dataframe To Python Dictionary
*Source: `7. Python Pandas/8. Python Pandas DataFrame to Python dictionary.ipynb`*

# Convert Pandas DataFrame to Python dictionary

In this class, you will learn how to convert **Pandas DataFrame** into a Python dictionary. It explains creating different kinds of dictionaries from pandas DataFrame.

Data Analyst needs to collect the data from heterogeneous sources like CSV files or SQL tables or Python data structures like a dictionary, list, etc. Such data is converted into pandas DataFrame.

After analyzing the data, we need to convert the resultant DataFrame back to its original format like CSV files or a dictionary. Or sometimes, we need to convert it into some other form.

## The `DataFrame.to_dict()` function

Pandas have a **`DataFrame.to_dict()`** function to create a Python dict object from DataFrame.

**Syntax:**
```python
DataFrame.to_dict(orient='dict', into=<class 'dict'>)
```

**Parameters:**

1. **`into`**: It is used to define the type of resultant **`dict`**. We can give an actual class or an empty instance.
2. **`orient`**: It defines the structure of key-value pairs in the resultant **`dict`**. The below table shows the input parameter, the format in which it creates the **`dict`** and key-value of the resultant **`dict`**.

>**Note:** Abbreviations are allowed. **`s`** indicates series, **`sp`** indicates split, **`r`** indicates record likewise.

| Parameter | Dict format | Key | Value |
|:---- |:---- |:---- | :---- |
| **`'dict'` (Default)** | **`{column_label : {row_index : data}}`** | **column label** | **dict of row index and data** |
| **`'list'`** | **`{column_label : [data]}`** | **column label** | **list of data** |
| **`'series‘`** | **`{column_label : Series(data)}`** | **column label** | **series of data** |
| **`'split'`** | **`{'row_index' : [index], ‘column_label’ : [columns], 'data' : [data]}`** | **row index, column labels, data** | **list of row index, list of columns labels, list of data** |
| **`'records'`** | **`[{column_label : data}, … , {column_label : data}]`** | **column label** | **data** |
| **`'index'`** | **`{row_index : {column_label : data}}`** | **row index** | **dict of column label and data** |

<div>

</div>

### Example to convert pandas DataFrame to dict

In the below example, we read the input from the **student_data.csv** file and create a DataFrame object. It is then converted into the Python dictionary object.

Input CSV file contains a simple dataset of student data with two columns, **`Name`** and **`Marks`**.

<div>

</div>

DataFrame is converted into **`dict`** using the default **`'dict'`** parameter.

```python
import pandas as pd

# create dataframe from csv
studentDf = pd.read_csv("student_data.csv")
print(studentDf)

# create dict from dataframe
studentDict = studentDf.to_dict()
print("\nResult dict: \n", studentDict)
```

**Output:**
```text
Name  Marks
0    Nat  70.88
1  Harry  85.90
2    Joe  91.45

Result dict: 
 {'Name': {0: 'Nat', 1: 'Harry', 2: 'Joe'}, 'Marks': {0: 70.88, 1: 85.9, 2: 91.45}}
```

## DataFrame to dict with a list of values

It is a case when we have DataFrame, which needs to be converted into the dictionary object such that column label should be the keys in the dictionary, and all the columns’ data should be added into the resultant dict as a list of values against each key.

In that case, we can use **`'list'`** parameter of the **`DataFrame.to_dict()`** function.

**Syntax:**
```python
{column_label : [data]}
```

**Example:**

Let’s see how we can use a **`'list'`** parameter to create DataFrame with a list of values.

```python
import pandas as pd

# create dataframe from csv
studentDf = pd.read_csv("student_data.csv")
print(studentDf)

# create dict from dataframe
studentDict = studentDf.to_dict('list')
print("\nResult dict: \n", studentDict)
```

**Output:**
```text
Name  Marks
0    Nat  70.88
1  Harry  85.90
2    Joe  91.45

Result dict: 
 {'Name': ['Nat', 'Harry', 'Joe'], 'Marks': [70.88, 85.9, 91.45]}
```

## DataFrame to dict with pandas series of values

When we need to convert the DataFrame into **`dict`** whereas column name as a key of the **`dict`**. And row index and data as a value in the **`dict`** for the respective keys.

**Syntax:**
```python
{column_label : Series(row_index data)}
```

In that case, we can use the **`'series'`** parameter of **`DataFrame.to_dict()`** function.

**Example:**

In the below example, **`dict`** is created with two entries, one for **`Name`** column and the other for the **`Marks`** column of the DataFrame.

```python
import pandas as pd

# create dataframe from csv
studentDf = pd.read_csv("student_data.csv")
print(studentDf)

# create dict from dataframe
studentDict = studentDf.to_dict('series')
print("\nResult dict: \n", studentDict)
```

**Output:**
```text
Name  Marks
0    Nat  70.88
1  Harry  85.90
2    Joe  91.45

Result dict: 
 {'Name': 0      Nat
1    Harry
2      Joe
Name: Name, dtype: object, 'Marks': 0    70.88
1    85.90
2    91.45
Name: Marks, dtype: float64}
```

## DataFrame to dict without header and index

When we want to collect the data from DataFrame without the column headers or we need to separate the row index and header from the data, we can use the **`'split'`** parameter of **`DataFrame.to_dict()`** function. It splits the input DataFrame into three parts, i.e., row index, column labels, and actual data.

**Syntax:**
```python
{'row_index' : [index], 'column_label' : [columns], 'data' : [data]}
```

**Example:**

We can get the data without index or header from the resultant **`dict`** using key **`data`** as shown below.

```python
import pandas as pd

# create dataframe from csv
studentDf = pd.read_csv("student_data.csv")
print(studentDf)

studentDict = studentDf.to_dict('split')
print("\n", studentDict)

# print only data
print("\nList of values from DF without index and header: \n", studentDict['data'])
```

**Output:**
```text
Name  Marks
0    Nat  70.88
1  Harry  85.90
2    Joe  91.45

 {'index': [0, 1, 2], 'columns': ['Name', 'Marks'], 'data': [['Nat', 70.88], ['Harry', 85.9], ['Joe', 91.45]]}

List of values from DF without index and header: 
 [['Nat', 70.88], ['Harry', 85.9], ['Joe', 91.45]]
```

## DataFrame to dict by row

When we have a DataFrame where **each row** contains data that needs to be store in a **separate dictionary** object, i.e., we need a data row-wise, we can use the **`'records'`** parameter of the **`DataFrame.to_dict()`** function.

It returns a list of dictionary objects. A **`dict`** for each row, where the key is a column label, and the value is column data.

**Syntax:**
```python
{'row_index' : [index], 'column_label' : [columns], 'data' : [data]}
```
**Example:**

In the below example, we created list of dictionary for each student data.

```python
# import pandas library
import pandas as pd

# create dataframe from csv
studentDf = pd.read_csv("student_data.csv")
print(studentDf)

# create dict from dataframe
studentDict = studentDf.to_dict('record')
print(studentDict)
```

**Output:**
```text
Name  Marks
0    Nat  70.88
1  Harry  85.90
2    Joe  91.45
[{'Name': 'Nat', 'Marks': 70.88}, {'Name': 'Harry', 'Marks': 85.9}, {'Name': 'Joe', 'Marks': 91.45}]
```

## DataFrame to dict by row index

When we have a DataFrame with row indexes and if we need to convert the data of each row from DataFrame to **`dict`**, we can use the **`index`** parameter of the **`DataFrame.to_dict()`** function.

It returns a list of dictionary objects. A **`dict`** is created for each row. Where the key is a row index, and the value is **`dict`** of column label and data.

**Syntax:**
```python
{row_index : {column_label : data}}
```

**Example:**

In the below example **`dict`** object is created for each row of student data.

```python
import pandas as pd

# create dataframe from csv
studentDf = pd.read_csv("student_data.csv")
print(studentDf)

# create dict from dataframe
studentDict = studentDf.to_dict('index')
print(studentDict)
```

**Output:**
```text
Name  Marks
0    Nat  70.88
1  Harry  85.90
2    Joe  91.45
{0: {'Name': 'Nat', 'Marks': 70.88}, 1: {'Name': 'Harry', 'Marks': 85.9}, 2: {'Name': 'Joe', 'Marks': 91.45}}
```

## DataFrame to dict with one column as the key

In this section, we target the use case when we need to create a **`dict`** from DataFrame where one column as a key of **`dict`** and other columns as the value of the **`dict`**.

Suppose we have student DataFrame with two columns, student’s **Name**, and student’s **Marks**. And we need to store each student’s data in the **`dict`** where the student name is the Key and their marks as a Value of the **`dict`**.

We can do it in various ways, as shown below:

* Using **`df.set_index('Col1').to_dict()['Col2']`**
* Using **`zip(df.Col1, df.Col2)`**
* Using **`df.set_index('Col1').T.to_dict('list')`**

**Example:**

Below example uses **`df.set_index('Col1').to_dict()['Col2']`** to get the expected output.

```python
import pandas as pd

# create dataframe from csv
studentDf = pd.read_csv("student_data.csv")
print(studentDf)

# create dict with Name as key and marks as value
studentDict = studentDf.set_index('Name').to_dict()['Marks']

print(studentDict)
```

**Output:**
```text
Name  Marks
0    Nat  70.88
1  Harry  85.90
2    Joe  91.45
{'Nat': 70.88, 'Harry': 85.9, 'Joe': 91.45}
```

We can also achieve the same result using **`zip()`** the function.

```python
# create dict with Name as key and marks as value
studentDict = dict(zip(studentDf.Name, studentDf.Marks))
```

If we want to collect the **column data into the list**, it can be done by applying **transpose** operation on the DataFrame and then converting it into dict.

```python
import pandas as pd

# create dataframe from csv
studentDf = pd.read_csv("student_data.csv")
print(studentDf)

# create dict with Name as key and marks as value
studentDict = studentDf.set_index('Name').T.to_dict('list')
print(studentDict)
```

**Output:**
```text
Name  Marks
0    Nat  70.88
1  Harry  85.90
2    Joe  91.45
{'Nat': [70.88], 'Harry': [85.9], 'Joe': [91.45]}
```

## DataFrame to dict using `into` parameter

While converting a DataFrame to **`dict`** if we need output **`dict`** to be of a particular type, we can use the parameter into of **`DataFrame.to_dict()`** function. We can specify the class name or the instance of the class for the resultant **`dict`**.

**Example:**

In the below example, we converted DataFrame to the **`dict`** of type **OrderedDict**.

```python
# import pandas library
from collections import OrderedDict
import pandas as pd

# create dataframe from csv
studentDf = pd.read_csv("student_data.csv")
print(studentDf)

# convert dataframe to ordered dict
studentDict = studentDf.to_dict(into=OrderedDict)
print(studentDict)
```

**Output:**
```text
Name  Marks
0    Nat  70.88
1  Harry  85.90
2    Joe  91.45
OrderedDict([('Name', OrderedDict([(0, 'Nat'), (1, 'Harry'), (2, 'Joe')])), ('Marks', OrderedDict([(0, 70.88), (1, 85.9), (2, 91.45)]))])
```

---

## 📘 Python Pandas Dataframe Set Index
*Source: `7. Python Pandas/9. Python Pandas DataFrame set index.ipynb`*

# Set index in pandas DataFrame

In this class, we learn how to set the index of the **Pandas DataFrame** using existing columns or a list of labels. We cover all the cases of replacing the existing row labels or assign new ones.

DataFrame is the tabular structure in the Python pandas library. It represents each row and column by the label. Row label is called an **index**, whereas column label is called column index/header.

By default, while creating DataFrame, Python pandas assign a range of numbers (starting at 0) as a row index. Row indexes are used to identify each row. We can set a new row index or replace the existing ones using **`DataFrame.set_index()`** function, which we discuss further in more detail.

## The `DataFrame.set_index()` function

This function is used to re-assign a row label using the existing column of the DataFrame. It can assign one or multiple columns as a row index. Let’s see how to use **`DataFrame.set_index()`** function to set row index or replace existing.

**Syntax:**
```python
DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)
```

**Parameters:**

1. **`keys`**: It takes a single or list of column labels to set as an index. It also takes a list of new labels as input.
2. **`drop`**: It is a flag to specify if columns to be used as the new index should be deleted From DataFrame or not. By default value is **`True`**, i.e., assign the column as an index and **delete** it.
3. **`append`**: It is a flag to specify whether to append columns to the existing index. By default, it is **`False`**, i.e., it replaces the current index rather than appending.
4. **`inplace`**: It is used to specify whether to return a new DataFrame or update an existing one. It is a boolean flag with default **`False`**.
5. **`verify_integrity`**: It is a boolean flag,
    * If **`True`**, then it checks the new index for duplicates and throws **`ValueError`**.
    * If **`False`**, then it defers the check until necessary.
    
>**Note:** Setting to **`False`** will improve the performance of this method.

**Return:**

DataFrame with the changed row labels or None if **`inplace=True`**.

## Set index using a column

How to set index in pandas DataFrame?

1. **Create pandas DataFrame**
    * We can create a DataFrame from a CSV file or **`dict`**.


2. **Identify the columns to set as index**
    * We can set a specific column or multiple columns as an index in pandas DataFrame. Create a list of column labels to be used to set an index.
**`['col_label1', 'col_label2'...]`**


3. **Use **`DataFrame.set_index()`** function**
    * We need to pass the column or list of column labels as input to the DataFrame.set_index() function to set it as an index of DataFrame. **By default, these new index columns are deleted from the DataFrame**.
**`df = df.set_index(['col_label1', 'col_label2'…])`**


4. **Set the index in place**
    * We can use the parameter **`inplace`** to set the index in the existing DataFrame rather than create a new copy.
**`df.set_index(inplace=True)`**

**Example:**

Let’s see how we can set a specific column as an index in the DataFrame. In the below example, we have default index as a range of numbers replaced with set index using first column **`Name`** of the student DataFrame.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before set index: \n", student_df)

# set index using column
student_df = student_df.set_index('Name')
print("\nAfter set index: \n", student_df)
```

**Output:**
```text
Before set index: 
     Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54

After set index: 
        Age  Marks
Name             
Joe     20  85.10
Nat     21  77.80
Harry   19  91.54
```

## Set index using a list

As we have seen, we can pass column labels of the DataFrame to assign it as an index of the DataFrame. We can also give a list of labels which can be strings or numbers to **`DataFrame.set_index()`** function to set a new index in the DataFrame.

First, we create a Python **`Index`** object from a list of labels and then pass it as input to the **`DataFrame.set_index()`** function.

**Example:**

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before set index: \n", student_df)

index = pd.Index(['s1', 's2', 's3'])
student_df = student_df.set_index(index)
print("\nAfter set index: \n", student_df)
```

**Output:**
```text
Before set index: 
     Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54

After set index: 
      Name  Age  Marks
s1    Joe   20  85.10
s2    Nat   21  77.80
s3  Harry   19  91.54
```

## Set index using multiple columns

Python pandas have DataFrame with multiple columns or rows as an index, and they are also called **multi-index** DataFrame. If we want to set multiple columns as row labels, we can use **`DataFrame.set_index()`** function.

**Example:**

In the below example, we pass a list of existing column labels **`Name`** and **`Marks`** to set a **multi-level** index in the student DataFrame.

>**Note:** It throws **`KeyError`** for unknown column labels.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before set index: \n", student_df)

# set multi-index
student_df = student_df.set_index(['Name', 'Marks'])
print("\nAfter set index: \n", student_df)
```

**Output:**
```text
Before set index: 
     Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54

After set index: 
              Age
Name  Marks     
Joe   85.10   20
Nat   77.80   21
Harry 91.54   19
```

## Set multi-index using a list and column

If there is a case where we want to create a two-level row index of the DataFrame, where one level is the new list of labels and another level is created from the existing column.

We can use **`DataFrame.set_index()`** to set the multi-level index of pandas DataFrame using a combination of a new list and the existing column.

We need to create a Python **`Index`** object from a list of new labels and pass that **`Index`** object and an existing column label as input to the **`DataFrame.set_index()`** function to create a two-level index.

**Example:**

Here, we are passing two parameters to the DataFrame.set_index() function. The first parameter is the **Python Index** created using multiple strings of size matches to the length of DataFrame. The second parameter is the existing column label **`Name`** of student DataFrame.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before set index: \n", student_df)

index = pd.Index(['s1', 's2', 's3'])
student_df = student_df.set_index([index, 'Name'])
print("\nAfter set index: \n", student_df)
```

**Output:**
```text
Before set index: 
     Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54

After set index: 
           Age  Marks
   Name             
s1 Joe     20  85.10
s2 Nat     21  77.80
s3 Harry   19  91.54
```

## Set multi-index using two Python series

When we want to replace the existing index with the multiple new series rather than the existing columns, we can create such a multi-index DataFrame by assigning new series using **`DataFrame.set_index()`** function.

**Example:**

Let’s see how we can pass two Python **`series`** of numbers as a first and second-level index of the DataFrame.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before set index: \n", student_df)

# set multi-index
s = pd.Series([1, 2, 3])
student_df = student_df.set_index([s, s ** 2])
print("\nAfter set index: \n", student_df)
```

**Output:**
```text
Before set index: 
     Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54

After set index: 
       Name  Age  Marks
1 1    Joe   20  85.10
2 4    Nat   21  77.80
3 9  Harry   19  91.54
```

## Set index using a Python range

Suppose we need to set a sequence of numbers as an index of the DataFrame such that it should start at any number. For example, we want to assign a roll number to the student DataFrame beginning from 1.

It is not feasible to pass all the numbers as a list to the **`DataFrame.set_index()`** function. In such a case, we can use the **Python range()** function.

We can create pandas Index using range() function and pass it to the **`DataFrame.set_index()`** function.

**Example:**

Let’s see how we can use **Python range()** function with **`DataFrame.set_index()`** to assign a sequential index to the DataFrame.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict, index=['s1', 's2', 's3'])
print("Before set index: \n", student_df)

# set index
index = pd.Index(range(1, 4, 1))
student_df = student_df.set_index(index)
print("\nAfter set index: \n", student_df)
```

**Output:**
```text
Before set index: 
      Name  Age  Marks
s1    Joe   20  85.10
s2    Nat   21  77.80
s3  Harry   19  91.54

After set index: 
     Name  Age  Marks
1    Joe   20  85.10
2    Nat   21  77.80
3  Harry   19  91.54
```

## Set index but keep column

By default, **`DataFrame.set_index()`** function takes column name as input which should be used as an index of the DataFrame. After setting the new index, it deletes the column which is used.

If we do not want to delete such a column from DataFrame, then we need to use the drop parameter of **`DataFrame.set_index()`**. It is a boolean flag such that,

* If **`drop=True`** (default case), it deletes the column and uses it as an index.
* If **`drop=False`**, it does not delete the column and uses it as an index.

**Example:**

In the below example, we use the **`Name`** column as an index of the student DataFrame without deleting it.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before set index: \n", student_df)

# set index, keep column
student_df = student_df.set_index('Name', drop=False)
print("\nAfter set index: \n", student_df)
```

**Output:**
```text
Before set index: 
     Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54

After set index: 
         Name  Age  Marks
Name                    
Joe      Joe   20  85.10
Nat      Nat   21  77.80
Harry  Harry   19  91.54
```

## Set index by keeping old index

**`DataFrame.set_index()`** is used to set a new index to the DataFrame. It is also used to extend the existing DataFrame, i.e., we can update the index by append to the existing index.

We need to use the **`append`** parameter of the **`DataFrame.set_index()`** function to append the new index to the existing one. By default, the value of **`append`** is **`False`**.

**Example:**

In the below example, each row has an index like s1, s2, and so on, but we update the index by appending values in the **`Name`** column.

```python
import pandas as pd

student_dict = {'Name':['Joe','Nat','Harry'], 'Age':[20,21,19], 'Marks':[85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict, index = ['s1','s2','s3'])
print("Before set index: \n", student_df)

# set index by append
student_df = student_df.set_index('Name', append=True)
print("\nAfter set index: \n", student_df)
```

**Output:**
```text
Before set index: 
      Name  Age  Marks
s1    Joe   20  85.10
s2    Nat   21  77.80
s3  Harry   19  91.54

After set index: 
           Age  Marks
   Name             
s1 Joe     20  85.10
s2 Nat     21  77.80
s3 Harry   19  91.54
```

## Set index in place

In the above examples, whenever we executed **`DataFrame.set_index()`** operation, pandas created a new copy of DataFrame because the modification is not-in place.

Specify **`inplace=True`** to set index in the existing DataFrame rather than creating a copy of it.

If **`inplace=True`** then it updates the existing DataFrame and does not return anything.
If **`inplace=False`** then it creates a new DataFrame with updated changes and returns it.

>**Note:** You don’t need to assign the result back to a variable as we are performing modifications in place.

**Example:**

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before set index: \n", student_df)

# set index in place
student_df.set_index('Name', inplace=True)
print("\nAfter set index: \n", student_df)
```

**Output:**
```text
Before set index: 
     Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54

After set index: 
        Age  Marks
Name             
Joe     20  85.10
Nat     21  77.80
Harry   19  91.54
```

## Set index using a column with duplicates

As we have discussed, we need to pass a column name that needs to be used to set row index in the DataFrame.

But, the column may contain duplicate values. By default, **`DataFrame.set_index()`** allows duplicate index. If we want to change this behavior, then we can use the **`verify_integrity`** parameter of **`DataFrame.set_index()`**.

* If **`verify_integrity=True`**, then it checks the new index for duplicates and throws **`ValueError`**.
* If **`verify_integrity=False`**, then it defers the check until necessary.

>**Note:** Setting to **`False`** will improve the performance of this method.

**Example:**

In the below example, we set **`verify_integrity=True`** and use the **`Name`** column to set an index that contains duplicate values.

```python
import pandas as pd

student_dict = {'Name':['Joe','Nat','Joe'], 'Age':[20,21,19], 'Marks':[85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before set index: \n", student_df)

# set index error case
student_df = student_df.set_index('Name', verify_integrity=True)
print("\nAfter set index: \n", student_df)
```

**Output:**
```text
Before set index: 
   Name  Age  Marks
0  Joe   20  85.10
1  Nat   21  77.80
2  Joe   19  91.54
```

## Set index by column number

If we need to set single or multiple columns as an index of the DataFrame, but we do not know the column labels to pass to **`DataFrame.set_index()`** function. In such a case, we can use the columns parameter of the DataFrame to retrieve the column index position.

We need to create a list of columns using column position **`df.columns[[0,1]]`** and pass it to the **`DataFrame.set_index()`** function.

**Example:**

In the below example, we set column 0 and 2 as an index of the student DataFrame.

```python
import pandas as pd

student_dict = {'Name':['Joe','Nat','Harry'], 'Age':[20,21,19], 'Marks':[85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print("Before set index: \n", student_df)

# set index
cols = list(student_df.columns[[0,2]])
student_df = student_df.set_index(cols)
print("\nAfter set index: \n", student_df)
```

**Output:**
```text
Before set index: 
     Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54

After set index: 
              Age
Name  Marks     
Joe   85.10   20
Nat   77.80   21
Harry 91.54   19
```

---

## 📘 Python Pandas Dataframe Reset Index
*Source: `7. Python Pandas/10. Python Pandas DataFrame reset index.ipynb`*

# Reset index in pandas DataFrame

In this class, we learn how to reset the index of the **Pandas DataFrame** We discuss all the cases of resetting the row index of a simple and multi-level DataFrame.

DataFrame is the tabular structure in the Python pandas library. It represents each row and column by the label. Row label is called an **index**, whereas column label is called column index/header.

After performing manipulations and filtering on the large dataset, we finally get the precise DataFrame as required. But, it carries the index of the original dataset. In such a case, we need to reset the index of the DataFrame.

## The `DataFrame.reset_index()` function

After dropping and filtering the rows, this function is used to reset the index of the resultant Python DataFrame. Let’s discuss how to use **`DataFrame.reset_index()`** function in detail.

**Syntax:**
```python
DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
```

**Parameters:**

1. **`level`**: In multi-level DataFrame, it takes a **level name or a position** of **Row index** that needs to be reset. By default, it reset all levels in a row index.
2. **`drop: It is a boolean flag,
    * **`True`** – It does not add the current row index as a new column in DataFrame.
    * **`False`** (Default) – It adds the current row index as a new column in DataFrame.
3. **`inplace`**: It is used to specify whether to return a new DataFrame or update an existing one. It is a boolean flag with default **`False`**.
4. **`col_level`**: In multi-level DataFrame, determines which column header level the current row index is inserted into. By default, it is inserted into the first level.
5. **`col_fill`**: In multi-level DataFrame, if the column headers have multiple levels, it determines how the other levels are named. **For example**, if we have a DataFrame with the two-column headers at levels 0 and 1, and if we add the current index as column header at level 0, we can specify the column header at level 1.
    
**Return:**

DataFrame with the new index or None if **`inplace=True`**.

## Reset index to starts at 0

How to reset index in pandas DataFrame?

1. **Create pandas DataFrame**
    * We can create a DataFrame from a CSV file or **`dict`**.


2. **Manipulate the DataFrame**
    * When we manipulate the DataFrame like **drop duplicates** or sort values, we get the new DataFrame, but it carries the original row index.
**`df = df.drop_duplicates()`**


3. **Use `DataFrame.reset_index()` function**
    * We can use **`DataFrame.reset_index()`** to reset the index of the updated DataFrame. By default, it adds the current row index as a new column called **index** in DataFrame, and it will create a new row index as a range of numbers starting at 0.
**`df = df.reset_index()`**


4. **Reset index without adding new column**
    * By default, **`DataFrame.reset_index()`** adds the current row index as a new column in DataFrame. If we do not want to add the new column, we can use the **`drop`** parameter.
**`df = df.reset_index(drop=True)`**


5. **Reset index in place**
    * We can use the parameter **`inplace`** to reset the index in the existing DataFrame rather than create a new copy.
**`df.reset_index(inplace=True)`**

<div>

</div>

**Example:**

We have a student DataFrame with a row index ‘s1’, ‘s2’.. likewise. It contains a row with missing values that we want to remove. After we removed it using **`DataFrame.dropna()`** function, its row index is still the same. But now, the index is not in the sequence.

In such a case, let’s see how to reset the index to the sequence of numbers using **`DataFrame.reset_index()`**.

```python
import numpy as np

student_dict = {'Name': ['Joe', 'Nat', np.NaN, 'Harry'], 'Age': [20, 21, np.NaN, 19],
                'Marks': [85.10, 77.80, np.NaN, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict, index=['s1', 's2', 's3', 's4'])
print("Original DataFrame: \n", student_df)

# drop NA
student_df = student_df.dropna()
print("\nDataFrame after dropping N/A: \n", student_df)

# reset index
student_df = student_df.reset_index()
print("\nDataFrame after resetting index: \n", student_df)
```

**Output:**
```text
Original DataFrame: 
      Name   Age  Marks
s1    Joe  20.0  85.10
s2    Nat  21.0  77.80
s3    NaN   NaN    NaN
s4  Harry  19.0  91.54

DataFrame after dropping N/A: 
      Name   Age  Marks
s1    Joe  20.0  85.10
s2    Nat  21.0  77.80
s4  Harry  19.0  91.54

DataFrame after resetting index: 
   index   Name   Age  Marks
0    s1    Joe  20.0  85.10
1    s2    Nat  21.0  77.80
2    s4  Harry  19.0  91.54
```

## Reset index without new column

By default, **`DataFrame.reset_index()`** adds the current row index as a new **index** column in DataFrame. If we do not want to add the new column, we can use the drop parameter.

* If **`drop=True`** then it does not add the new column of the current row index in the DataFrame.
* If **`drop=False`**, is the default behavior where it adds the new column of the current row index in the DataFrame.

**Example:**

Let’s see how we can reset the index without adding new column.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict, index=['s1', 's2', 's3'])
print("Before reset index: \n", student_df)

# reset index without new column
student_df = student_df.reset_index(drop=True)
print("\nAfter reset index: \n", student_df)
```

**Output:**
```text
Before reset index: 
      Name  Age  Marks
s1    Joe   20  85.10
s2    Nat   21  77.80
s3  Harry   19  91.54

After reset index: 
     Name  Age  Marks
0    Joe   20  85.10
1    Nat   21  77.80
2  Harry   19  91.54
```

## Reset index in place

In the above examples, whenever we executed reset index operation, pandas created a new copy of DataFrame because the modification is not-in place.

Specify **`inplace=True`** to reset index in the existing DataFrame rather than creating a copy of it.

* If the **`inplace=True`** then it updates the existing DataFrame and does not return anything.
* If the **`inplace=False`** then it creates a new DataFrame with an updated index and returns it.

>**Note:** You don’t need to assign the result back to a variable as we are performing modifications in place.

**Example:**

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict, index=['s1', 's2', 's3'])
print("Before reset index: \n", student_df)

# reset index in place
student_df.reset_index(inplace=True)
print("\nAfter reset index: \n", student_df)
```

**Output:**
```text
Before reset index: 
      Name  Age  Marks
s1    Joe   20  85.10
s2    Nat   21  77.80
s3  Harry   19  91.54

After reset index: 
   index   Name  Age  Marks
0    s1    Joe   20  85.10
1    s2    Nat   21  77.80
2    s3  Harry   19  91.54
```

## Reset index starts from 1

Suppose we have a huge dataset which we need to filter. After filtering the DataFrame, it still carries the original index. When we want to reset the index of the DataFrame such that the new index should start with 1, we can do that in two steps,

* Use **`DataFrame.reset_index()`** to reset the row index to start at o.
* Use the **`index`** parameter of the DataFrame to re-assign the index by adding 1 to each row index of the resultant DataFrame.

**Example:**

In the below example, we first reset the index to the sequence of numbers and then added 1 to each index.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict, index=['s1', 's2', 's3'])
print("Before reset index: \n", student_df)

# reset index
student_df = student_df.reset_index()

# add 1 to each index
student_df.index = student_df.index + 1

print("\nAfter reset index: \n", student_df)
```

**Output:**
```text
Before reset index: 
      Name  Age  Marks
s1    Joe   20  85.10
s2    Nat   21  77.80
s3  Harry   19  91.54

After reset index: 
   index   Name  Age  Marks
1    s1    Joe   20  85.10
2    s2    Nat   21  77.80
3    s3  Harry   19  91.54
```

## Reset index to the range of numbers

In our student DataFrame, suppose we want to assign the Identity number to each student starting from 101. We can use the index parameter of DataFrame to change the **`index`** as a range of numbers that begins at a specific number.

First, we need to generate the range of numbers and then assign it to the **`DataFrame.index`** to reset the original index.

**Example:**

In the below example, **[pd.RangeIndex()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.RangeIndex.html)** function is used to generate the range of numbers which starts at 101 till the last row i.e. **`len(df)`**. Assign this range to the **`df.index`**.

```python
import pandas as pd

student_dict = {'Name':['Joe','Nat','Harry'], 'Age':[20,21,19], 'Marks':[85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict, index=['s1','s2','s3'])
print("Before reset index: \n", student_df)

# assign new index from 1 to n
student_df.index = pd.RangeIndex(start=101, stop=101+len(student_df), step=1)

print("\nAfter reset index: \n", student_df)
```

**Output:**
```text
Before reset index: 
      Name  Age  Marks
s1    Joe   20  85.10
s2    Nat   21  77.80
s3  Harry   19  91.54

After reset index: 
       Name  Age  Marks
101    Joe   20  85.10
102    Nat   21  77.80
103  Harry   19  91.54
```

## Reset index and change column name

As we have already discussed, **`DataFrame.reset_index()`** adds the current index as a new column with the name **index** in the DataFrame. If we want to give a name to such a newly added column, then we need to use **`DataFrame.rename()`** function with **`DataFrame.reset_index()`**.

**Example:**

Let’s see how to do the method chaining of **`DataFrame.reset_index()`** and **`DataFrame.rename()`** functions to rename a new **index** column to **ID**.

```python
import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict, index=['s1', 's2', 's3'])
print("Before reset index: \n", student_df)

# reset index and rename
student_df = student_df.reset_index().rename(columns={'index': 'ID'})
print("\nAfter reset index: \n", student_df)
```

**Output:**
```text
Before reset index: 
      Name  Age  Marks
s1    Joe   20  85.10
s2    Nat   21  77.80
s3  Harry   19  91.54

After reset index: 
    ID   Name  Age  Marks
0  s1    Joe   20  85.10
1  s2    Nat   21  77.80
2  s3  Harry   19  91.54
```

## Reset multi-level index

When Python pandas DataFrame has multiple row index or column headers, then are called **multi-level** or **hierarchical** DataFrame. We can apply **`DataFrame.reset index()`** on such multi-index DataFrame.

The below diagram shows hierarchical DataFrame of Student data with two-column headers where column labels **`Name`** and **`Marks`** are at level 0 and **`Surname`** and **`Percentage`** at level 1. Similarly, two-row indexes where index **`Standard`** at level 0 and **`Class`** at level 1 of the DataFrame.

<div>

</div>

**Example:**

The below example show how to create such DataFrame.

```python
import pandas as pd

index = pd.MultiIndex.from_tuples([('Standard 1', 'Class A'),
                                   ('Standard 1', 'Class B'),
                                   ('Standard 2', 'Class A'),
                                   ('Standard 2', 'Class B')],
                                  names=['Standard', 'Class'])
columns = pd.MultiIndex.from_tuples([('Name', 'Surname'),
                                     ('Marks', 'Percentage')])

# create multi-index dataframe
student_df = pd.DataFrame([('Joe', 91.56),
                           ('Nat', 87.90),
                           ('Harry', 70.10),
                           ('Sam', 65.48)],
                          index=index, columns=columns)
print("\nAfter reset index: \n", student_df)
```

**Output:**
```text
After reset index: 
                       Name      Marks
                   Surname Percentage
Standard   Class                     
Standard 1 Class A     Joe      91.56
           Class B     Nat      87.90
Standard 2 Class A   Harry      70.10
           Class B     Sam      65.48
```

Now we see how to reset the index of the multi-level DataFrame using **`DataFrame.reset index()`**. By default, it reset the index of all the levels and add the new range of indexes in the DataFrame.

```python
# reset multi-level index
student_df = student_df.reset_index()
print(student_df)
```

**Output:**
```text
Standard    Class    Name      Marks
                       Surname Percentage
0  Standard 1  Class A     Joe      91.56
1  Standard 1  Class B     Nat      87.90
2  Standard 2  Class A   Harry      70.10
3  Standard 2  Class B     Sam      65.48
```

###  Reset index by level

As we have seen, in the case of a multi-level index, by default **`DataFrame.reset_index()`** applies to the index of all the levels. If we want to reset the index of the specific level only then, we can use the **`level`** parameter of the **`DataFrame.reset_index()`** function.

It takes a **level position** or **level name** as input to reset that particular index only.

**Example:**

In the below example, we reset the index of the **`'Standard'`** level only.

```python
student_df = pd.DataFrame([('Joe', 91.56),
                           ('Nat', 87.90),
                           ('Harry', 70.10),
                           ('Sam', 65.48)],
                          index=index, columns=columns)

# reset multi-level index by level
student_df = student_df.reset_index(level='Standard')
print(student_df)
```

**Output:**
```text
Standard    Name      Marks
                    Surname Percentage
Class                                 
Class A  Standard 1     Joe      91.56
Class B  Standard 1     Nat      87.90
Class A  Standard 2   Harry      70.10
Class B  Standard 2     Sam      65.48
```

### Reset index and creates new column in level

As we have observed in the above section, by default, **`DataFrame.reset_index()`** all the new column at the first level, i.e., level 0. If we want to add the new index column to other levels, we can use the **`col_level`** parameter.

It takes the level name or level position as an input if the columns have multiple levels, so it determines which level the labels are inserted into.

**Example:**

In the below example, it reset the index of level **`Standard`** only and add it as a new column at level 1.

```python
student_df = pd.DataFrame([('Joe', 91.56),
                           ('Nat', 87.90),
                           ('Harry', 70.10),
                           ('Sam', 65.48)],
                          index=index, columns=columns)

# reset multi-level index and add at level 1
student_df = student_df.reset_index(level='Standard', col_level=1)
print(student_df)
```

**Output:**
```text
Name      Marks
           Standard Surname Percentage
Class                                 
Class A  Standard 1     Joe      91.56
Class B  Standard 1     Nat      87.90
Class A  Standard 2   Harry      70.10
Class B  Standard 2     Sam      65.48
```

### Reset index and name other level

As we see in the above section, in multi-level DataFrame, we have added the **`Standard`** index at level 1. If there is a case when we need to rename the other level, we need to use the **`col_fill`** parameter of DataFrame.

We can specify any existing column label under which the new column will be assigned. If we specify the new label, then it will create one.

**Example:**

In the below example, we create a new column from the index **`Standard`** at level 1 and assign a new column label **`New_Header`** at level 0 of this new column.

```python
student_df = pd.DataFrame([('Joe', 91.56),
                           ('Nat', 87.90),
                           ('Harry', 70.10),
                           ('Sam', 65.48)],
                          index=index, columns=columns)

# reset multi-level index
student_df = student_df.reset_index(level='Standard', col_level=1, col_fill='New_Header')
print(student_df)
```

**Output:**
```text
New_Header    Name      Marks
           Standard Surname Percentage
Class                                 
Class A  Standard 1     Joe      91.56
Class B  Standard 1     Nat      87.90
Class A  Standard 2   Harry      70.10
Class B  Standard 2     Sam      65.48
```

---
