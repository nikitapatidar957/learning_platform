# Python NumPy: High-Performance Numerical Computing

In-depth guide to NumPy ndarrays, multidimensional indexing, slicing, broadcasting, vectorization, array manipulation, mathematical and statistical functions, and real-world data analysis.

---

# 09_Python_NumPy_Module

## Introduction 👋

### What is NumPy?
[![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=flat&logo=numpy&logoColor=white)](https://numpy.org/) stands for numeric python which is a python package for the computation and processing of the multidimensional and single dimensional array elements.

**Travis Oliphant** created NumPy package in 2005 by injecting the features of the ancestor module Numeric into another module Numarray.

It is an extension module of Python which is mostly written in "C". It provides various functions which are capable of performing the numeric computations with a high speed.

NumPy provides various powerful data structures, implementing multi-dimensional arrays and matrices. These data structures are used for the optimal computations regarding arrays and matrices.

In this tutorial, we will go through the numeric python library NumPy.

### The need of NumPy?
With the revolution of data science, data analysis libraries like NumPy, SciPy, Pandas, etc. have seen a lot of growth. With a much easier syntax than other programming languages, python is the first choice language for the data scientist.

NumPy provides a convenient and efficient way to handle the vast amount of data. NumPy is also very convenient with Matrix multiplication and data reshaping. NumPy is fast which makes it reasonable to work with a large set of data.

There are the following advantages of using NumPy for data analysis.

* NumPy performs array-oriented computing.
* It efficiently implements the multidimensional arrays.
* It performs scientific computations.
* It is capable of performing Fourier Transform and reshaping the data stored in multidimensional arrays.
* NumPy provides the in-built functions for linear algebra and random number generation.

Nowadays, NumPy in combination with SciPy and Mat-plotlib is used as the replacement to MATLAB as Python is more complete and easier programming language than MATLAB.

---

## Table of contents 📋

| **No.** | **Name** | 
| ------- | -------- | 
| 01 | **[Python_NumPy](https://github.com/milaan9/09_Python_NumPy_Module/blob/main/001_Python_NumPy.ipynb)** |
| 02 | **[Python_NumPy_Array_Part1](https://github.com/milaan9/09_Python_NumPy_Module/blob/main/002_Python_NumPy_Array_Part1.ipynb)** |
| 03 | **[Python_NumPy_Array_Part2](https://github.com/milaan9/09_Python_NumPy_Module/blob/main/003_Python_NumPy_Array_Part2.ipynb)** |
| 04 | **[Python_NumPy_Array_Part3](https://github.com/milaan9/09_Python_NumPy_Module/blob/main/004_Python_NumPy_Array_Part3.ipynb)** |
| 05 | **[Python_NumPy_Array_Part4](https://github.com/milaan9/09_Python_NumPy_Module/blob/main/005_Python_NumPy_Array_Part4.ipynb)** |
|    | **[data](https://github.com/milaan9/09_Python_NumPy_Module/blob/main/data.txt)** |
| 06 | **[Python_Numpy_Exercises_with_hints](https://github.com/milaan9/09_Python_NumPy_Module/blob/main/Python_Numpy_Exercises_with_hints.ipynb)** |
| 07 | **[Python_Numpy_Exercises_with_hints](https://github.com/milaan9/09_Python_NumPy_Module/blob/main/Python_Numpy_Exercises_with_hints.ipynb)** |
| 08 | **[NumPy Cheat Sheet Data Analysis in Python.pdf](https://github.com/milaan9/09_Python_NumPy_Module/blob/main/NumPy%20Cheat%20Sheet%20Data%20Analysis%20in%20Python.pdf)** |


These are online **read-only** versions. However you can **`Run ▶`**  all the codes **online** by clicking here ➞ 

---

## Install Numpy Module:

Open your [![Anaconda](https://img.shields.io/badge/Anaconda-342B029.svg?&style=flate&logo=anaconda&logoColor=white)](https://www.anaconda.com/products/individual) Prompt <img alt="propmt" src="https://img.shields.io/badge/-__-000000?style=flat-square&logo=Plex&logoColor=white"> and type and run the following command (individually):

 -       pip install numpy  
 

Once Installed now we can import it inside our python code.

---    

## Frequently asked questions ❔

### How can I thank you for writing and sharing this tutorial? 🌷

You can <img src="https://img.shields.io/static/v1?label=%E2%AD%90 Star &message=if%20useful&style=style=flat&color=blue" alt="Star Badge"/> and <img src="https://img.shields.io/static/v1?label=%E2%B5%96 Fork &message=if%20useful&style=style=flat&color=blue" alt="Fork Badge"/> Starring and Forking is free for you, but it tells me and other people that it was helpful and you like this tutorial.

Go [**`here`**](https://github.com/milaan9/09_Python_NumPy_Module) if you aren't here already and click ➞ **`✰ Star`** and **`ⵖ Fork`** button in the top right corner. You'll be asked to create a GitHub account if you don't already have one.

---

### How can I read this tutorial without an Internet connection? <img alt="GIF" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/hmm.gif" width="20" />

1. Go [**`here`**](https://github.com/milaan9/09_Python_NumPy_Module) and click the big green ➞ **`Code`** button in the top right of the page, then click ➞ [**`Download ZIP`**](https://github.com/milaan9/09_Python_NumPy_Module/archive/refs/heads/main.zip).

    ![Download ZIP](img/dnld_rep.png)

2. Extract the ZIP and open it. Unfortunately I don't have any more specific instructions because how exactly this is done depends on which operating system you run.
    
3. Launch ipython notebook from the folder which contains the notebooks. Open each one of them
  
    **`Kernel > Restart & Clear Output`**
    
This will clear all the outputs and now you can understand each statement and learn interactively.

If you have git and you know how to use it, you can also clone the repository instead of downloading a zip and extracting it. An advantage with doing it this way is that you don't need to download the whole tutorial again to get the latest version of it, all you need to do is to pull with git and run ipython notebook again.

---

## Authors ✍️

I'm Dr. Milaan Parmar and I have written this tutorial. If you think you can add/correct/edit and enhance this tutorial you are most welcome🙏

See [github's contributors page](https://github.com/milaan9/09_Python_NumPy_Module/graphs/contributors) for details.

If you have trouble with this tutorial please tell me about it by [Create an issue on GitHub](https://github.com/milaan9/09_Python_NumPy_Module/issues/new). and I'll make this tutorial better. This is probably the best choice if you had trouble following the tutorial, and something in it should be explained better. You will be asked to create a GitHub account if you don't already have one.

If you like this tutorial, please [give it a ⭐ star](https://github.com/milaan9/09_Python_NumPy_Module).

---

## Licence 📜

You may use this tutorial freely at your own risk. See [LICENSE](./LICENSE).
Copyright (c) 2020 Dr. Milan Parmar

---

## 📘 Python Numpy
*Source: `6. Python NumPy/1. Python NumPy.ipynb`*

# Python NumPy

In this class, you will learn various NumPy concepts like how to install NumPy, arrays, functions, matrix multiplication, etc. This NumPy in Python tutorial will help you learn all Python NumPy basics.

**[Numpy](http://www.numpy.org/)** (‘Numerical Python’) is the core open source library for scientific computing in Python. It is a Linear Algebra Library for Python, it is so important for Finance with Python. It is a very useful library to perform mathematical and statistical operations in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays. In this part, we will review the essential functions that you need to know for the tutorial on 'TensorFlow.'

## Why use NumPy?

NumPy is memory efficiency, meaning it can handle the vast amount of data more accessible than any other library. Besides, NumPy is very convenient to work with, especially for matrix multiplication and reshaping. On top of that, NumPy is fast. In fact, TensorFlow and Scikit learn to use NumPy array to compute the matrix multiplication in the back end.

## Python NumPy Array: 

A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the size of the array along each dimension.

Numpy array is a powerful N-dimensional array object which is in the form of rows and columns. We can initialize NumPy arrays from nested Python lists and access it elements.

## How to Install NumPy?

NumPy is installed by default with Anaconda.

**It is highly recommended you install Python using the Anaconda distribution to make sure all underlying dependencies (such as Linear Algebra libraries like numpy) sync up with the use of a conda install. If you have Anaconda, install NumPy by going to your terminal or command prompt and typing:**
    
`conda install numpy`

### Import NumPy and Check Version

The command to import numpy is

```python
import numpy as np
```
Above code renames the **`numpy`** namespace to **`np`**.

```python
# To check your installed version of Numpy use the command

print (np.__version__)
```

**Output:**
```text
1.20.1
```

# NumPy Basics

### NumPy Basics

| Operator | Description |
|:---- |:---- |
| **`np.array([1,2,3])`**           | **1d array** | 
| **`np.array([(1,2,3),(4,5,6)])`** | **2d array** | 
| **`np.arange(start,stop,step)`**  | **range array**  |

### Placeholders

| Operator | Description |
|:---- |:---- |
| **`np.linspace(0,2,9)`**      | **Add evenly spaced values btw interval to array of length** |
| **`np.zeros((1,2))`**         | **Create and array filled with zeros** |
| **`np.ones((1,2))`**          | **Creates an array filled with ones** |
| **`np.random.random((5,5))`** | **Creates random array** |
| **`np.empty((2,2))`**         | **Creates an empty array** |

### Array

| Operator | Description |
|:---- |:---- |
| **`array.shape`**        | **Dimensions (Rows,Columns)** |
| **`len(array)`**         | **Length of Array** |
| **`array.ndim`**         | **Number of Array Dimensions** |
| **`array.dtype`**        | **Data Type** |
| **`array.astype(type)`** | **Converts to Data Type** |
| **`type(array)`**        | **Type of Array** |

### Copying/Sorting

| Operator | Description |
|:---- |:---- |
| **`np.copy(array)`**       | **Creates copy of array** |
| **`other = array.copy()`** | **Creates deep copy of array** |
| **`array.sort()`**         | **Sorts an array** |
| **`array.sort(axis=0)`**   | **Sorts axis of array** |

## Array Manipulation

### Adding or Removing Elements

| Operator | Description |
|:---- |:---- |
| **`np.append(a,b)`**               | **Append items to array** |
| **`np.insert(array, 1, 2, axis)`** | **Insert items into array at axis 0 or 1** |
| **`np.resize((2,4))`**             | **Resize array to shape(2,4)** |
| **`np.delete(array,1,axis)`**      | **Deletes items from array** |

### Combining Arrays

| Operator | Description |
|:---- |:---- |
| **`np.concatenate((a,b),axis=0)`** | **Split an array into multiple sub-arrays.** |
| **`np.vstack((a,b))`**             | **Split an array in sub-arrays of (nearly) identical size** |
| **`np.hstack((a,b))`**             | **Split the array horizontally at 3rd index** |

### More

| Operator | Description |
|:---- |:---- |
| **`other = ndarray.flatten()`**       | **Flattens a 2d array to 1d** |
| **`array = np.transpose(other)`**     | **Transpose array** |
| **`array.T`**                         | **Transpose array** |
| **`inverse = np.linalg.inv(matrix)`** | **Inverse of a given matrix** |

## Slicing and Subsetting

| Operator | Description |
|:---- |:---- |
| **`array[i]`**        | **1d array at index i** |
| **`array[i,j]`**      | **2d array at index[i][j]** |
| **`array[i<4]`**      | **Boolean Indexing, see Tricks** |
| **`array[0:3]`**      | **Select items of index 0, 1 and 2** |
| **`array[0:2,1]`**    | **Select items of rows 0 and 1 at column 1** |
| **`array[:1]`**       | **Select items of row 0 (equals array[0:1, :])** |
| **`array[1:2, :]`**   | **Select items of row 1** |
| **`[comment]: <> (`** | **array[1,...]** |
| **`array[ : :-1]`**   | **Reverses array** |

## Mathematics

### Operations

| Operator | Description |
|:---- |:---- |
| **`np.add(x,y)`**        | **Addition** |
| **`np.substract(x,y)`**  | **Subtraction** |
| **`np.divide(x,y)`**     | **Division** |
| **`np.multiply(x,y)`**   | **Multiplication** |
| **`np.sqrt(x)`**         | **Square Root** |
| **`np.sin(x)`**          | **Element-wise sine** |
| **`np.cos(x)`**          | **Element-wise cosine** |
| **`np.log(x)`**          | **Element-wise natural log** |
| **`np.dot(x,y)`**        | **Dot product** |
| **`np.roots([1,0,-4])`** | **Roots of a given polynomial coefficients** |

### Comparison

| Operator | Description |
|:----: |:---- |
| **`==`** | **Equal** |
| **`!=`** | **Not equal** |
| **`<`**  | **Smaller than** |
| **`>`**  | **Greater than** |
| **`<=`** | **Smaller than or equal** |
| **`>=`** | **Greater than or equal** |
| **`np.array_equal(x,y)`** | **Array-wise comparison** |

## Basic Statistics

| Operator | Description |
|:---- |:---- |
| **`np.mean(array)`**   | **Mean** |
| **`np.median(array)`** | **Median** |
| **`array.corrcoef()`** | **Correlation Coefficient** |
| **`np.std(array)`**    | **Standard Deviation** |

### More

| Operator | Description |
|:---- |:---- |
| **`array.sum()`**          | **Array-wise sum** |
| **`array.min()`**          | **Array-wise minimum value** |
| **`array.max(axis=0)`**    | **Maximum value of specified axis** |
| **`array.cumsum(axis=0)`** | **Cumulative sum of specified axis** |

---

## 📘 Python Numpy Array Part1
*Source: `6. Python NumPy/2. Python NumPy Array Part1.ipynb`*

# Python NumPy Array: 

A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the size of the array along each dimension.

Numpy array is a powerful N-dimensional array object which is in the form of rows and columns. We can initialize NumPy arrays from nested Python lists and access it elements.

## NumPy Array Types:

<div>

</div>

## Create a NumPy Array

Simplest way to create an array in Numpy is to use Python List

### Load in NumPy Library

```python
import numpy as np
```

```python
my_list = [1,2,3,4]
my_list
```

**Output:**
```text
[1, 2, 3, 4]
```

To convert python list to a numpy array by using the object **`np.array`**.

```python
numpy_array_from_list = np.array(my_list)
numpy_array_from_list
```

**Output:**
```text
array([1, 2, 3, 4])
```

In practice, there is no need to declare a Python List. The operation can be combined.

```python
my_list1  = np.array([1,2,3,4])
my_list1
```

**Output:**
```text
array([1, 2, 3, 4])
```

>**NOTE:** Numpy documentation states use of **`np.ndarray`** to create an array. However, this the recommended method

You can also create a numpy array from a Tuple

```python
my_list2 = np.array (range (1,5))
my_list2
```

**Output:**
```text
array([1, 2, 3, 4])
```

## Numpy Array basics

We can initialize numpy arrays from nested Python lists, and access elements using square brackets **`[]`**:

```python
a = np.array([1,2,3]) # Create a 1D array
print(a) 
print(type(a))  # Prints "<class 'numpy.ndarray'>"
```

**Output:**
```text
[1 2 3]
<class 'numpy.ndarray'>
```

```python
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
```

**Output:**
```text
[[9. 8. 7.]
 [6. 5. 4.]]
```

```python
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix
np.array(my_matrix)
```

**Output:**
```text
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
```

```python
# Get Dimension
a.ndim
```

**Output:**
```text
1
```

```python
# Get Shape
b.shape
```

**Output:**
```text
(2, 3)
```

```python
# Get Size
a.itemsize
```

**Output:**
```text
4
```

```python
# Get Size
b.itemsize
```

**Output:**
```text
8
```

```python
# Get total size
a.nbytes  # a.nbytes = a.size * a.itemsize
```

**Output:**
```text
12
```

```python
# Get number of elements
a.size
```

**Output:**
```text
3
```

```python
c = np.array([[True, False], [False, True]])
c
```

**Output:**
```text
array([[ True, False],
       [False,  True]])
```

```python
print(c.size)
print(c.shape)
```

**Output:**
```text
4
(2, 2)
```

```python
a = np.array([1, 2, 3])   # Create a 1d array
print(a)
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Indexing with 3 elements. Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a 2d array
print(b)
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
```

**Output:**
```text
[1 2 3]
<class 'numpy.ndarray'>
(3,)
1 2 3
[5 2 3]
[[1 2 3]
 [4 5 6]]
(2, 3)
1 2 4
```

## Array datatypes

Every numpy array is a grid of elements of the same type. Numpy provides a large set of numeric datatypes that you can use to construct arrays. The full list of NumPy datatype (dtypes) can be found in the [NumPy documentation](http://docs.scipy.org/doc/numpy/user/basics.types.html).

<div>
<img src="http://docs.scipy.org/doc/numpy/_images/dtype-hierarchy.png" width="600"/>
</div>

The two biggest things to remember are

- Missing values (NaN) cast integer or boolean arrays to floats
- NumPy arrays only have a single dtype for every element
- the object dtype is the fallback

Numpy tries to guess a datatype when you create an array, but functions that construct arrays usually also include an optional argument to explicitly specify the datatype. For example:

```python
a = np.array([1,2,3], dtype='int32') # Create a 1D array with int32 type
print(a)
```

**Output:**
```text
[1 2 3]
```

```python
# Get Type
a.dtype
```

**Output:**
```text
dtype('int32')
```

```python
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
b.dtype
```

**Output:**
```text
[[9. 8. 7.]
 [6. 5. 4.]]
dtype('float64')
```

```python
import numpy as np

x = np.array([1, 2])   # Let numpy choose the datatype
print(x.dtype)         # Prints "int64"

x = np.array([1.0, 2.0])   # Let numpy choose the datatype
print(x.dtype)             # Prints "float64"

x = np.array([1, 2], dtype=np.int64)   # Force a particular datatype
print(x.dtype)                         # Prints "int64"
```

**Output:**
```text
int32
float64
int64
```

* **Does a NumPy array have a single dtype or multiple dtypes?**
  - NumPy arrays are homogenous: they only have a single dtype (unlike DataFrames).
  You can have an array that holds mixed types, e.g. `np.array(['a', 1])`, but the
  dtype of that array is `object`, which you probably want to avoid.

You can read all about numpy datatypes in this **[documentation](https://numpy.org/doc/stable/reference/arrays.dtypes.html)**.

### Random number

#### `rand`
Random values in a given shape from a uniform distribution over [0, 1)

```python
np.random.rand(3)
```

**Output:**
```text
array([0.22672978, 0.55283762, 0.10276143])
```

```python
np.random.rand(3,5)
```

**Output:**
```text
array([[0.2559205 , 0.60786967, 0.83770503, 0.45359369, 0.27764243],
       [0.38209653, 0.44225798, 0.63158859, 0.81893678, 0.79823164],
       [0.69791535, 0.69343173, 0.04763428, 0.1097501 , 0.30920635]])
```

```python
# Random decimal numbers
np.random.rand(4,2)

#or
#np.random.random_sample(a.shape)
```

**Output:**
```text
array([[0.55360672, 0.30668723],
       [0.93102691, 0.05082974],
       [0.23180804, 0.95966987],
       [0.68602648, 0.89632087]])
```

#### `randn`
Return a sample (or samples) from the "standard normal" distribution. Not Uniform.with mean 0 and variance with 1.

```python
np.random.randn(3)
```

**Output:**
```text
array([-1.33142653,  1.54275813,  0.00616708])
```

```python
np.random.randn(4,3)
```

**Output:**
```text
array([[-2.85505447, -0.48048431, -1.98749888],
       [-0.43563027, -1.35266299, -0.65628077],
       [-0.40015831, -1.14770535,  0.61784629],
       [-1.27672348, -0.54777888,  1.51026454]])
```

#### `randint`
Return random integers from **low** (inclusive) to **high** (exclusive).

```python
np.random.randint(2,100)
```

**Output:**
```text
85
```

```python
# Random Integer values
np.random.randint(-4,8, size=(3,3))
```

**Output:**
```text
array([[ 1,  2,  2],
       [ 5,  3,  2],
       [ 6, -1,  2]])
```

```python
x = np.random.randint(0, 10, 10)
y = np.random.randint(0, 10, 10)
x, y
```

**Output:**
```text
(array([9, 3, 3, 7, 5, 8, 4, 0, 0, 7]), array([2, 4, 7, 2, 5, 0, 7, 0, 9, 5]))
```

It's also *sometimes* a more convinient way of writing and thinking about things.

```python
[i + j for i, j in zip(x, y)]
```

**Output:**
```text
[11, 7, 10, 9, 10, 8, 11, 0, 9, 12]
```

```python
x + y
```

**Output:**
```text
array([11,  7, 10,  9, 10,  8, 11,  0,  9, 12])
```

### Array Attributes and Methods

```python
rana = np.random.randint(1,10,8)
rana
```

**Output:**
```text
array([5, 9, 9, 2, 2, 3, 6, 1])
```

#### `max`, `min`, `argmax`, `argmin`

```python
rana
```

**Output:**
```text
array([5, 9, 9, 2, 2, 3, 6, 1])
```

```python
rana.max()
```

**Output:**
```text
9
```

```python
rana.argmax()
```

**Output:**
```text
1
```

```python
rana.min()
```

**Output:**
```text
1
```

```python
rana.argmin()
```

**Output:**
```text
7
```

### Numpy also provides many functions to create arrays:

```python
# Generating Zeros
np.zeros(5)
```

**Output:**
```text
array([0., 0., 0., 0., 0.])
```

```python
# All 0s matrix
np.zeros((2,3))  # pass a tupple
```

**Output:**
```text
array([[0., 0., 0.],
       [0., 0., 0.]])
```

```python
# Generating Zeros
np.ones(3)       # one function
```

**Output:**
```text
array([1., 1., 1.])
```

```python
np.ones(1)*5
```

**Output:**
```text
array([5.])
```

```python
np.ones((3,3))
```

**Output:**
```text
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
```

```python
# All 1s matrix
np.ones((4,2,2), dtype='int32')
```

**Output:**
```text
array([[[1, 1],
        [1, 1]],

       [[1, 1],
        [1, 1]],

       [[1, 1],
        [1, 1]],

       [[1, 1],
        [1, 1]]])
```

```python
# Any other number
np.full((2,2), 99)
```

**Output:**
```text
array([[99, 99],
       [99, 99]])
```

```python
# Any other number (full_like)
np.full_like(a, 4)

#or np.full(a.shape, 4)
```

**Output:**
```text
array([4, 4, 4])
```

```python
# The identity matrix
np.identity(5)
```

**Output:**
```text
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
```

```python
# Repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print(r1)
```

**Output:**
```text
[[1 2 3]
 [1 2 3]
 [1 2 3]]
```

```python
import numpy as np

a = np.zeros((2,2))   # Create an array of all zeros
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

b = np.ones((1,2))    # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)  # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"
```

**Output:**
```text
[[0. 0.]
 [0. 0.]]
[[1. 1.]]
[[7 7]
 [7 7]]
[[1. 0.]
 [0. 1.]]
[[0.53909609 0.12336799]
 [0.93143051 0.39878883]]
```

```python
#Generate matrix

# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 1 1 1 1

output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:-1,1:-1] = z
print(output)
```

**Output:**
```text
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
[[0. 0. 0.]
 [0. 9. 0.]
 [0. 0. 0.]]
[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 9. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
```

You can read about other methods of array creation in this **[documentation](https://numpy.org/doc/stable/user/basics.creation.html#arrays-creation)**.

---

## 📘 Python Numpy Array Part2
*Source: `6. Python NumPy/3. Python NumPy Array Part2.ipynb`*

## Array indexing

Numpy offers several ways to index into arrays and accessing/changing specific elements, rows, columns, etc.

**Slicing:** Similar to Python lists, numpy arrays can be sliced. Since arrays may be multidimensional, you must specify a slice for each dimension of the array:

```python
import numpy as np
a = np.arange(0,11)
a
```

**Output:**
```text
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
```

#### Indexing a 1D array

```python
a[2]           # Get a value at an index
```

**Output:**
```text
2
```

```python
a[1:4]         # Get values in a range / slice notation
```

**Output:**
```text
array([1, 2, 3])
```

```python
a[:6]
```

**Output:**
```text
array([0, 1, 2, 3, 4, 5])
```

```python
a[3:]
```

**Output:**
```text
array([ 3,  4,  5,  6,  7,  8,  9, 10])
```

```python
#Slices
slice_a = a[0:5]
slice_a
```

**Output:**
```text
array([0, 1, 2, 3, 4])
```

```python
slice_a[:]=100
slice_a
```

**Output:**
```text
array([100, 100, 100, 100, 100])
```

```python
a         # Change in original array
```

**Output:**
```text
array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])
```

```python
a_copy = a.copy()   # creat a copy

a_copy
```

**Output:**
```text
array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])
```

```python
a_copy[:]=200
a_copy
```

**Output:**
```text
array([200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200])
```

```python
a
```

**Output:**
```text
array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])
```

##### Be careful when copying arrays!!!

```python
a = np.array([1,2,3])
a
b = a
#b = a.copy()
b[0] = 100

print(a)
```

**Output:**
```text
[100   2   3]
```

#### Indexing a 2D array (matrices)

```python
# mat = [row,col]
# mat = [row][col]
```

```python
mat=np.array(([5,10,20],[20,25,30],[35,40,10]))
mat
```

**Output:**
```text
array([[ 5, 10, 20],
       [20, 25, 30],
       [35, 40, 10]])
```

```python
mat[1] #Indexing row
```

**Output:**
```text
array([20, 25, 30])
```

```python
mat[2]
```

**Output:**
```text
array([35, 40, 10])
```

```python
# Getting individual element value
mat[1][1]
```

**Output:**
```text
25
```

```python
mat[1,2] # use common notaion instaed of 2 brackets
```

**Output:**
```text
30
```

```python
#array slicing
mat
```

**Output:**
```text
array([[ 5, 10, 20],
       [20, 25, 30],
       [35, 40, 10]])
```

```python
#Shape top row
mat[0]
```

**Output:**
```text
array([ 5, 10, 20])
```

```python
#Shape (2,2) from top right corner
mat[:2,1:]
```

**Output:**
```text
array([[10, 20],
       [25, 30]])
```

```python
#Shape (2,2) from bottom left corner
mat[1:,:2]
```

**Output:**
```text
array([[20, 25],
       [35, 40]])
```

```python
#Shape bottom row
mat[2]
```

**Output:**
```text
array([35, 40, 10])
```

```python
#Shape bottom row
mat[2,:]
```

**Output:**
```text
array([35, 40, 10])
```

```python
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
```

**Output:**
```text
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]]
```

```python
# Get a specific element [row, column]

a[1, 5]  # to select element '13' we need row 2 and element 6. Hence r=1, c=5 (index start from 0)

# or a[1,-2]
```

**Output:**
```text
13
```

```python
# Get a specific row 
a[0, :] # all columns
```

**Output:**
```text
array([1, 2, 3, 4, 5, 6, 7])
```

```python
# Get a specific column
a[:, 2] # all rows
```

**Output:**
```text
array([ 3, 10])
```

```python
# Getting a little more fancy [startindex:endindex:stepsize]
a[0, 1:-1:2]
```

**Output:**
```text
array([2, 4, 6])
```

```python
a[1,5] = 20  # row 2 and element 6
print(a)

a[:,2] = [1,2]
print(a)
```

**Output:**
```text
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 20 14]]
[[ 1  2  1  4  5  6  7]
 [ 8  9  2 11 12 20 14]]
```

```python
# 3D example

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
```

**Output:**
```text
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```

```python
# Get specific element (work outside in)
b[0,1,1]
```

**Output:**
```text
4
```

```python
# replace 
b[:,1,:]
print(b)
```

**Output:**
```text
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```

```python
b[:,1,:] = [[9,9,9],[8,8]]
print(b)
```

#### Summary:

```python
import numpy as np

import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
print(b)

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"
```

**Output:**
```text
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
[[2 3]
 [6 7]]
2
77
```

You can also mix **integer indexing** with **slice indexing**. However, doing so will yield an array of lower rank than the original array. 

>**Note:** this is quite different from the way that MATLAB handles array slicing:

```python
import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)  # Prints "[[ 2]
                             #          [ 6]
                             #          [10]] (3, 1)"
```

**Output:**
```text
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
[5 6 7 8] (4,)
[[5 6 7 8]] (1, 4)
[ 2  6 10] (3,)
[[ 2]
 [ 6]
 [10]] (3, 1)
```

### Integer array indexing

When you index into numpy arrays using slicing, the resulting array view will always be a subarray of the original array. In contrast, integer array indexing allows you to construct arbitrary arrays using the data from another array. Here is an example:

```python
import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])
print(a)

# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"

# When using integer array indexing, you can reuse the same
# element from the source array:
print(a[[0, 0], [1, 1]])  # Prints "[2 2]"

# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"
```

**Output:**
```text
[[1 2]
 [3 4]
 [5 6]]
[1 4 5]
[1 4 5]
[2 2]
[2 2]
```

One useful trick with integer array indexing is selecting or mutating one element from each row of a matrix:

```python
import numpy as np

# Create a new array from which we will select elements
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

print(a)  # prints "array([[ 1,  2,  3],
          #                [ 4,  5,  6],
          #                [ 7,  8,  9],
          #                [10, 11, 12]])"

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10

print(a)  # prints "array([[11,  2,  3],
          #                [ 4,  5, 16],
          #                [17,  8,  9],
          #                [10, 21, 12]])
```

**Output:**
```text
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
[ 1  6  7 11]
[[11  2  3]
 [ 4  5 16]
 [17  8  9]
 [10 21 12]]
```

### Quiz time

```python
# Generate matrix:

###    1  2  3  4  5
###    6  7  8  9 10
###   11 12 13 14 15
###   16 17 18 19 20
###   21 22 23 24 25
###   26 27 28 29 30

# Acces 
        11 12
        16 17
    
# Acces  
         2
           8
            14
              20

# Acces        
                4  5



               24 25
               29 30
```

### Boolean array indexing

Boolean array indexing lets you pick out arbitrary elements of an array. Frequently this type of indexing is used to select the elements of an array that satisfy some condition. Here is an example:

```python
a = np.arange(1,11)
a
```

**Output:**
```text
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
```

```python
a > 4
```

**Output:**
```text
array([False, False, False, False,  True,  True,  True,  True,  True,
        True])
```

```python
bool_a = a>4
```

```python
bool_a
```

**Output:**
```text
array([False, False, False, False,  True,  True,  True,  True,  True,
        True])
```

```python
a[bool_a]
```

**Output:**
```text
array([ 5,  6,  7,  8,  9, 10])
```

```python
a[a>2]
```

**Output:**
```text
array([ 3,  4,  5,  6,  7,  8,  9, 10])
```

```python
x = 2
a[a>x]
```

**Output:**
```text
array([ 3,  4,  5,  6,  7,  8,  9, 10])
```

```python
import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])
print(a)

bool_idx = (a > 2)   # Find the elements of a that are bigger than 2;
                     # this returns a numpy array of Booleans of the same
                     # shape as a, where each slot of bool_idx tells
                     # whether that element of a is > 2.

print(bool_idx)      # Prints "[[False False]
                     #          [ True  True]
                     #          [ True  True]]"

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print(a[a > 2])     # Prints "[3 4 5 6]"
```

**Output:**
```text
[[1 2]
 [3 4]
 [5 6]]
[[False False]
 [ True  True]
 [ True  True]]
[3 4 5 6]
[3 4 5 6]
```

For brevity we have left out a lot of details about numpy array indexing; if you want to know more about Array Indexing you should read this **[documentation](https://numpy.org/doc/stable/reference/arrays.indexing.html)**.

---

## 📘 Python Numpy Array Part3
*Source: `6. Python NumPy/4. Python NumPy Array Part3.ipynb`*

## Array math

Basic mathematical functions operate elementwise on arrays, and are available both as operator overloads and as functions in the numpy module:

```python
import numpy as np

a = np.array([0,1,2,3,4,5])
#a = np.arange(0,6)
print(a)
```

**Output:**
```text
[0 1 2 3 4 5]
```

```python
a + 2
```

**Output:**
```text
array([2, 3, 4, 5, 6, 7])
```

```python
a - 2
```

**Output:**
```text
array([-2, -1,  0,  1,  2,  3])
```

```python
a * 2
```

**Output:**
```text
array([ 0,  2,  4,  6,  8, 10])
```

```python
a / 2
```

**Output:**
```text
array([0. , 0.5, 1. , 1.5, 2. , 2.5])
```

```python
a + a
```

**Output:**
```text
array([ 0,  2,  4,  6,  8, 10])
```

```python
a * a
```

**Output:**
```text
array([ 0,  1,  4,  9, 16, 25])
```

```python
a - a
```

**Output:**
```text
array([0, 0, 0, 0, 0, 0])
```

```python
a/a # Warning on division by zero, but not an error!
```

**Output:**
```text
array([nan,  1.,  1.,  1.,  1.,  1.])
```

```python
1/a # Also warning, but not an error instead infinity
```

**Output:**
```text
array([       inf, 1.        , 0.5       , 0.33333333, 0.25      ,
       0.2       ])
```

```python
b = np.array([1,0,1,0,1,0])
a + b
```

**Output:**
```text
array([1, 1, 3, 3, 5, 5])
```

```python
a ** 3
```

**Output:**
```text
array([  0,   1,   8,  27,  64, 125], dtype=int32)
```

### Universal  Array Functions (Mathematical operations)

```python
#Square Roots
np.sqrt(a)
```

**Output:**
```text
array([0.        , 1.        , 1.41421356, 1.73205081, 2.        ,
       2.23606798])
```

```python
#exponential (e^)
np.exp(a)
```

**Output:**
```text
array([  1.        ,   2.71828183,   7.3890561 ,  20.08553692,
        54.59815003, 148.4131591 ])
```

```python
np.max(a) #same as arr.max()
```

**Output:**
```text
5
```

```python
np.min(a)
```

**Output:**
```text
0
```

```python
np.sin(a)
```

**Output:**
```text
array([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ,
       -0.95892427])
```

```python
np.cos(a)
```

**Output:**
```text
array([ 1.        ,  0.54030231, -0.41614684, -0.9899925 , -0.65364362,
        0.28366219])
```

```python
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x)
print(y)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))
```

**Output:**
```text
[[1. 2.]
 [3. 4.]]
[[5. 6.]
 [7. 8.]]
[[ 6.  8.]
 [10. 12.]]
[[ 6.  8.]
 [10. 12.]]
[[-4. -4.]
 [-4. -4.]]
[[-4. -4.]
 [-4. -4.]]
[[ 5. 12.]
 [21. 32.]]
[[ 5. 12.]
 [21. 32.]]
[[0.2        0.33333333]
 [0.42857143 0.5       ]]
[[0.2        0.33333333]
 [0.42857143 0.5       ]]
[[1.         1.41421356]
 [1.73205081 2.        ]]
```

>**Note:** that unlike MATLAB, **`*`** is elementwise multiplication, not matrix multiplication. We instead use the **`dot`** function to compute inner products of vectors, to multiply a vector by a matrix, and to multiply matrices. **`dot`** is available both as a function in the numpy module and as an instance method of array objects:

```python
### Dot product: product of two arrays

f = np.array([1,2])
g = np.array([4,5])
### 1*4+2*5
np.dot(f, g)
```

**Output:**
```text
14
```

```python
import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
```

**Output:**
```text
219
219
[29 67]
[29 67]
[[19 22]
 [43 50]]
[[19 22]
 [43 50]]
```

Numpy provides many useful functions for performing computations on arrays; one of the most useful is **`sum`**:

```python
import numpy as np

x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"
```

**Output:**
```text
10
[4 6]
[3 7]
```

You can find the full list of mathematical functions provided by numpy in this **[documentation](https://numpy.org/doc/stable/reference/routines.math.html)**.

Apart from computing mathematical functions using arrays, we frequently need to reshape or otherwise manipulate data in arrays. The simplest example of this type of operation is transposing a matrix; to transpose a matrix, simply use the **`T`** attribute of an array object:

```python
import numpy as np

x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"
```

**Output:**
```text
[[1 2]
 [3 4]]
[[1 3]
 [2 4]]
[1 2 3]
[1 2 3]
```

Numpy provides many more functions for manipulating arrays; you can see the full list in the **[documentation](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)**.

### Matrix Multiplication

The Numpy **`matmul()`** function is used to return the matrix product of 2 arrays.

```python
a = np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

np.matmul(a,b) # matmul() function is used to return the matrix product of 2 arrays.
```

**Output:**
```text
[[1. 1. 1.]
 [1. 1. 1.]]
[[2 2]
 [2 2]
 [2 2]]
array([[6., 6.],
       [6., 6.]])
```

```python
### Matmul: matruc product of two arrays

h = [[1,2],[3,4]] 
i = [[5,6],[7,8]] 
### 1*5+2*7 = 19
np.matmul(h, i)
```

**Output:**
```text
array([[19, 22],
       [43, 50]])
```

### Determinant

Last but not least, if you need to compute the determinant, you can use **`np.linalg.det()`**. 

>**Note:** numpy takes care of the dimension.

```python
# Find the determinant

c = np.identity(3)
np.linalg.det(c)
```

**Output:**
```text
1.0
```

```python
## Determinant 2*2 matrix

5*8-7*6
np.linalg.det(i)
```

**Output:**
```text
-1.999999999999999
```

```python
## Reference docs (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
# Etc...
```

## Broadcasting

Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations. Frequently we have a smaller array and a larger array, and we want to use the smaller array multiple times to perform some operation on the larger array.

For example, suppose that we want to add a constant vector to each row of a matrix. We could do it like this:

```python
import numpy as np

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)
```

**Output:**
```text
[[ 2  2  4]
 [ 5  5  7]
 [ 8  8 10]
 [11 11 13]]
```

This works; however when the matrix **`x`** is very large, computing an explicit loop in Python could be slow. Note that adding the vector **`v`** to each row of the matrix **`x`** is equivalent to forming a matrix **`vv`** by stacking multiple copies of **`v`** vertically, then performing elementwise summation of **`x`** and **`vv`**. We could implement this approach like this:

```python
import numpy as np

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))   # Stack 4 copies of v on top of each other
print(vv)                 # Prints "[[1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]]"
y = x + vv  # Add x and vv elementwise
print(y)  # Prints "[[ 2  2  4
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"
```

**Output:**
```text
[[1 0 1]
 [1 0 1]
 [1 0 1]
 [1 0 1]]
[[ 2  2  4]
 [ 5  5  7]
 [ 8  8 10]
 [11 11 13]]
```

Numpy broadcasting allows us to perform this computation without actually creating multiple copies of **`v`**. Consider this version, using broadcasting:

```python
import numpy as np

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print(y)  # Prints "[[ 2  2  4]
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"
```

**Output:**
```text
[[ 2  2  4]
 [ 5  5  7]
 [ 8  8 10]
 [11 11 13]]
```

**Explanation:** 

The line **`y = x + v`** works even though **`x`** has shape **(4, 3)** and **`v`** has shape **(3,)** due to broadcasting; this line works as if **`v`** actually had shape **(4, 3)**, where each row was a copy of **`v`**, and the sum was performed elementwise.

Broadcasting two arrays together follows these rules:

* If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.


* The two arrays are said to be compatible in a dimension if they have the same size in the dimension, or if one of the arrays has size 1 in that dimension.


* The arrays can be broadcast together if they are compatible in all dimensions.


* After broadcasting, each array behaves as if it had shape equal to the elementwise maximum of shapes of the two input arrays.


* In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension

If this explanation does not make sense, try reading the explanation from this **[documentation](https://numpy.org/doc/stable/user/basics.broadcasting.html)** or this **[explanation](http://scipy.github.io/old-wiki/pages/EricsBroadcastingDoc)**.

Functions that support broadcasting are known as universal functions. You can find the list of all universal functions in this **[documentation](https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs)**.

Here are some applications of broadcasting:

```python
import numpy as np

# Compute outer product of vectors
v = np.array([1,2,3])  # v has shape (3,)
w = np.array([4,5])    # w has shape (2,)
# To compute an outer product, we first reshape v to be a column
# vector of shape (3, 1); we can then broadcast it against w to yield
# an output of shape (3, 2), which is the outer product of v and w:
# [[ 4  5]
#  [ 8 10]
#  [12 15]]
print(np.reshape(v, (3, 1)) * w)

# Add a vector to each row of a matrix
x = np.array([[1,2,3], [4,5,6]])
# x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3),
# giving the following matrix:
# [[2 4 6]
#  [5 7 9]]
print(x + v)

# Add a vector to each column of a matrix
# x has shape (2, 3) and w has shape (2,).
# If we transpose x then it has shape (3, 2) and can be broadcast
# against w to yield a result of shape (3, 2); transposing this result
# yields the final result of shape (2, 3) which is the matrix x with
# the vector w added to each column. Gives the following matrix:
# [[ 5  6  7]
#  [ 9 10 11]]
print((x.T + w).T)
# Another solution is to reshape w to be a column vector of shape (2, 1);
# we can then broadcast it directly against x to produce the same
# output.
print(x + np.reshape(w, (2, 1)))

# Multiply a matrix by a constant:
# x has shape (2, 3). Numpy treats scalars as arrays of shape ();
# these can be broadcast together to shape (2, 3), producing the
# following array:
# [[ 2  4  6]
#  [ 8 10 12]]
print(x * 2)
```

**Output:**
```text
[[ 4  5]
 [ 8 10]
 [12 15]]
[[2 4 6]
 [5 7 9]]
[[ 5  6  7]
 [ 9 10 11]]
[[ 5  6  7]
 [ 9 10 11]]
[[ 2  4  6]
 [ 8 10 12]]
```

* **Why is broadcasting useful?**
  - Broadcasting typically makes your code more concise and faster, so you should strive to use it where possible. It lets you perform operations between arrays that are compatable, but not nescessarily identical, in shape. This makes your code cleaner.

---

## 📘 Python Numpy Array Part4
*Source: `6. Python NumPy/5. Python NumPy Array Part4.ipynb`*

## Arrays reorganizing

### `asarray()`

The **`asarray()`** function is used when you want to convert an input to an array. The input could be a lists, tuple, ndarray, etc.

**Syntax:**
```python
numpy.asarray(data, dtype=None, order=None)[source]
```

* **`data`**: Data that you want to convert to an array

* **`dtype`**: This is an optional argument. If not specified, the data type is inferred from the input data

* **`Order`**: Default is **`C`** which is an essential row style. Other option is **`F`** (Fortan-style)

```python
# Consider the following 2-D matrix with four rows and four columns filled by 1

import numpy as np

a = np.matrix(np.ones((4,4)))
```

If you want to change the value of the matrix, you cannot. The reason is, it is not possible to change a copy.

```python
np.array(a)[2]=3
print(a)  # value won't change in result
```

**Output:**
```text
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
```

Matrix is immutable. You can use asarray if you want to add modification in the original array. Let's see if any change occurs when you want to change the value of the third rows with the value 2

```python
np.asarray(a)[2]=2 # np.asarray(A): converts the matrix A to an array
print(a)
```

**Output:**
```text
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [2. 2. 2. 2.]
 [1. 1. 1. 1.]]
```

### `arange()`

The **`arange()`** is an inbuilt numpy function that returns an ndarray object containing evenly spaced values within a defined interval. For instance, you want to create values from 1 to 10; you can use **`arange()`** function.

**Syntax:**
```python
numpy.arange(start, stop,step) 
```
* **`start`**: Start of interval
* **`stop`**: End of interval
* **`step`**: Spacing between values. Default step is 1

```python
# Example 1:

import numpy as np
np.arange(1, 11)
```

**Output:**
```text
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
```

If you want to change the step, you can add a third number in the parenthesis. It will change the step.

```python
# Example 2:

import numpy as np
np.arange(1, 14, 4)
```

**Output:**
```text
array([ 1,  5,  9, 13])
```

```python
np.arange(0,11,2)   # even no by adding a step size
```

**Output:**
```text
array([ 0,  2,  4,  6,  8, 10])
```

```python
np.arange(1,11,2)   # odd no
```

**Output:**
```text
array([1, 3, 5, 7, 9])
```

### Reshape Data

In some occasions, you need to reshape the data from wide to long. You can use the reshape function for this. 

**Syntax:** 
```python
numpy.reshape(a, newShape, order='C')
```
* **`a: Array`** that you want to reshape
* **`newShape`**: The new desires shape
* **`order`**: Default is **`C`** which is an essential row style.

```python
import numpy as np

e  = np.array([(1,2,3), (4,5,6)])
print(e)
e.reshape(3,2)
```

**Output:**
```text
[[1 2 3]
 [4 5 6]]
array([[1, 2],
       [3, 4],
       [5, 6]])
```

### Broadcasting with array reorganizing 

It's super cool and super useful. The one-line explanation is that when doing elementwise operations, things expand to the "correct" shape.

```python
# add a scalar to a 1-d array
x = np.arange(5)
print('x:  ', x)
print('x+1:', x + 1, end='\n\n')

y = np.random.uniform(size=(2, 5))
print('y:  ', y,  sep='\n')
print('y+1:', y + 1, sep='\n')
```

**Output:**
```text
x:   [0 1 2 3 4]
x+1: [1 2 3 4 5]

y:  
[[0.20040757 0.96248829 0.29534113 0.14204329 0.00786338]
 [0.68572271 0.22357762 0.88618684 0.91174698 0.87380356]]
y+1:
[[1.20040757 1.96248829 1.29534113 1.14204329 1.00786338]
 [1.68572271 1.22357762 1.88618684 1.91174698 1.87380356]]
```

Since `x` is shaped `(5,)` and `y` is shaped `(2,5)` we can do operations between them.

```python
x * y
```

**Output:**
```text
array([[0.        , 0.96248829, 0.59068226, 0.42612988, 0.03145352],
       [0.        , 0.22357762, 1.77237368, 2.73524094, 3.49521424]])
```

Without broadcasting we'd have to manually reshape our arrays, which quickly gets annoying.

```python
x.reshape(1, -1).repeat(2, axis=0) * y
```

**Output:**
```text
array([[0.        , 0.96248829, 0.59068226, 0.42612988, 0.03145352],
       [0.        , 0.22357762, 1.77237368, 2.73524094, 3.49521424]])
```

```python
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((2,4))
print(after)
```

**Output:**
```text
[[1 2 3 4]
 [5 6 7 8]]
[[1 2 3 4]
 [5 6 7 8]]
```

### Flatten Data

When you deal with some neural network like convnet, you need to flatten the array. You can use **`flatten()`**.

**Syntax:** 
```python
numpy.flatten(order='C')
```
* **`a: Array`** that you want to reshape
* **`newShape`**: The new desires shape
* **`order`**: Default is **`C`** which is an essential row style.

```python
e.flatten()
```

**Output:**
```text
array([1, 2, 3, 4, 5, 6])
```

### What is `hstack`?

With **`hstack`** you can appened data horizontally. This is a very convinient function in Numpy. Lets study it with an example:

```python
## Horitzontal Stack

import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6])

print('Horizontal Append:', np.hstack((f, g)))
```

**Output:**
```text
Horizontal Append: [1 2 3 4 5 6]
```

```python
# Horizontal  stack

h1 = np.ones((2,4))
h2 = np.zeros((2,2))

np.hstack((h1,h2))
```

**Output:**
```text
array([[1., 1., 1., 1., 0., 0.],
       [1., 1., 1., 1., 0., 0.]])
```

### What is `vstack`?

With **`vstack`** you can appened data vertically. Lets study it with an example:

```python
## Vertical Stack

import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6])

print('Vertical Append:', np.vstack((f, g)))
```

**Output:**
```text
Vertical Append: [[1 2 3]
 [4 5 6]]
```

```python
# Vertically stacking vectors

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1,v2,v1,v2])
```

**Output:**
```text
array([[1, 2, 3, 4],
       [5, 6, 7, 8],
       [1, 2, 3, 4],
       [5, 6, 7, 8]])
```

### Generate Random Numbers

To generate random numbers for Gaussian distribution use:

**Syntax:**
```python
numpy.random.normal(loc, scale, size)
```
* **`loc`**: the mean. The center of distribution
* **`scale`**: standard deviation.
* **`size`**: number of returns

```python
## Generate random number from normal distribution

normal_array = np.random.normal(5, 0.5, 10)
print(normal_array)
```

**Output:**
```text
[4.73370838 5.02319487 5.03247675 4.63238643 5.20491465 4.23379671
 4.65235094 4.03461004 4.81788758 5.40603744]
```

### Linspace

Linspace gives evenly spaced samples.

**Syntax:**
```python
numpy.linspace(start, stop, num, endpoint)
```
* **`start`**: Start of sequence
* **`stop`**: End of sequence
* **`num`**: Number of samples to generate. Default is 50
* **`endpoint`**: If **`True`** (default), stop is the last value. If **`False`**, stop value is not included.

```python
# Example:

import numpy as np
np.linspace(0,10,6)
```

**Output:**
```text
array([ 0.,  2.,  4.,  6.,  8., 10.])
```

```python
# Example: For instance, it can be used to create 10 values from 1 to 5 evenly spaced.

import numpy as np
np.linspace(1.0, 5.0, num=10)
```

**Output:**
```text
array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
       3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
```

If you do not want to include the last digit in the interval, you can set endpoint to **`False`**

```python
np.linspace(1.0, 5.0, num=5, endpoint=False)
```

**Output:**
```text
array([1. , 1.8, 2.6, 3.4, 4.2])
```

### LogSpace

LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as **`np.linspace`**.

**Syntax:**
```python
numpy.logspace(start, stop, num, endpoint)
```
* **`start`**: Start of sequence
* **`stop`**: End of sequence
* **`num`**: Number of samples to generate. Default is 50
* **`endpoint`**: If **`True`** (default), stop is the last value. If **`False`**, stop value is not included.

```python
# Example:

np.logspace(3.0, 4.0, num=4)
```

**Output:**
```text
array([ 1000.        ,  2154.43469003,  4641.58883361, 10000.        ])
```

Finaly, if you want to check the memory size of an element in an array, you can use **`.itemsize`**

```python
x = np.array([1,2,3], dtype=np.complex128)
x.itemsize
```

**Output:**
```text
16
```

## Statistics

NumPy has quite a few useful statistical functions for finding minimum, maximum, percentile standard deviation and variance, etc from the given elements in the array. The functions are explained as follows −

Numpy is equipped with the robust statistical function as listed below:

| Function | Numpy |
|:----: |:---- |
| **`Min`**                | **np.min()** | 
| **`Max`**                | **np.max()** | 
| **`Mean`**               | **np.mean()** | 
| **`Median`**             | **np.median()** | 
| **`Standard deviation`** | **np.std()** |

```python
# Consider the following Array

import numpy as np

normal_array = np.random.normal(5, 0.5, 10)
print(normal_array)
```

**Output:**
```text
[4.57057605 5.76249894 4.09935016 5.38336447 4.96652011 5.29402596
 4.79025614 6.00232788 5.49574452 5.60059908]
```

```python
# Example:Statistical function

### Min 
print(np.min(normal_array))

### Max 
print(np.max(normal_array))

### Mean 
print(np.mean(normal_array))

### Median
print(np.median(normal_array))

### Sd
print(np.std(normal_array))
```

**Output:**
```text
4.099350157876355
6.002327879593869
5.196526332130161
5.338695217273813
0.5550161930871431
```

```python
stats = np.array([[1,2,3],[4,5,6]])
stats
```

**Output:**
```text
array([[1, 2, 3],
       [4, 5, 6]])
```

```python
np.min(stats)
```

**Output:**
```text
1
```

```python
np.max(stats, axis=1)
```

**Output:**
```text
array([3, 6])
```

```python
np.sum(stats, axis=0)
```

**Output:**
```text
array([5, 7, 9])
```

## Miscellaneous

### Load Data from File

```python
filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32') # you can also change type to 'int64'
print(filedata)
```

**Output:**
```text
[[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5]
 [  3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12]
 [  1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]]
```

### Boolean Masking and Advanced Indexing

```python
filedata >50
```

**Output:**
```text
array([[False, False, False, False,  True,  True, False, False, False,
        False, False, False, False, False, False, False, False, False],
       [False, False, False, False,  True,  True, False,  True, False,
        False, False, False, False, False, False, False, False, False],
       [False, False, False, False,  True, False, False, False,  True,
        False, False, False, False, False, False, False,  True,  True]])
```

```python
print(filedata)
filedata[filedata >50] # '[]' will display the value of data point from the dataset
```

**Output:**
```text
[[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5]
 [  3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12]
 [  1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]]
array([196,  75, 766,  75,  55, 999,  78,  76,  88])
```

```python
print(filedata)
np.any(filedata > 50, axis = 0) # axis=0 refers to columns and axis=1 refers to rows in this dataset
```

**Output:**
```text
[[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5]
 [  3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12]
 [  1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]]
array([False, False, False, False,  True,  True, False,  True,  True,
       False, False, False, False, False, False, False,  True,  True])
```

```python
print(filedata)
np.all(filedata > 50, axis = 0) # '.all' refers to all the data points in row/column (based on axis=0 or axis=1).
```

**Output:**
```text
[[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5]
 [  3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12]
 [  1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]]
array([False, False, False, False,  True, False, False, False, False,
       False, False, False, False, False, False, False, False, False])
```

```python
print(filedata)
(((filedata > 50) & (filedata < 100)))
```

**Output:**
```text
[[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5]
 [  3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12]
 [  1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]]
array([[False, False, False, False, False,  True, False, False, False,
        False, False, False, False, False, False, False, False, False],
       [False, False, False, False, False,  True, False,  True, False,
        False, False, False, False, False, False, False, False, False],
       [False, False, False, False, False, False, False, False,  True,
        False, False, False, False, False, False, False,  True,  True]])
```

```python
print(filedata)
(~((filedata > 50) & (filedata < 100)))  # '~' means not
```

**Output:**
```text
[[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5]
 [  3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12]
 [  1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]]
array([[ True,  True,  True,  True,  True, False,  True,  True,  True,
         True,  True,  True,  True,  True,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True, False,  True, False,  True,
         True,  True,  True,  True,  True,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True,  True,  True,  True, False,
         True,  True,  True,  True,  True,  True,  True, False, False]])
```

```python
### You can index with a list in NumPy
a = np.array([1,2,3,4,5,6,7,8,9])
a [[1,2,8]] #indexes
```

**Output:**
```text
array([2, 3, 9])
```

## Numpy Documentation

This brief overview has touched on many of the important things that you need to know about numpy, but is far from complete. Check out the **[numpy reference](https://numpy.org/doc/stable/reference/)** to find out much more about numpy.

---

## 📘 Python Numpy Exercises With Hints
*Source: `6. Python NumPy/Python Numpy Exercises with Hints.ipynb`*

# Python NumPy Exercises

This is a collection of exercises that have been collected in the numpy mailing list, on stack overflow
and in the numpy documentation. The goal of this collection is to offer a quick reference for both old
and new users but also to provide a set of exercises for those who teach.

#### 1. Import the numpy package under the name `np` and print the numpy version and the configuration (★☆☆)

`Hint: import … as` and `np.__version__, np.show_config)`

#### 2. Convert a list of numeric value into a one-dimensional NumPy array (★☆☆)
`💡 hint: numpy.array`

#### 3. Create a null vector of size 9 (★☆☆)
`💡 hint: np.zeros`

#### 4. How to find the memory size of any array (★☆☆)
`💡 hint: size, itemsize`

#### 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
`💡hint: np.info`

#### 6. Create a null vector of size 12 but the sixth value which is 1 (★☆☆)
`💡hint: array[12]`

#### 7. Create a vector with values ranging from 20 to 59 (★☆☆)
`💡hint: arange`

#### 8. Reverse a vector (first element becomes last) (★☆☆)
`💡hint: array[::-1]`

#### 9. Create a 3x3 matrix with values ranging from 12 to 20 (★☆☆)
`💡hint: reshape`

#### 10. Find indices of non-zero elements from [3,7,0,0,9,0] (★☆☆)
`💡hint: np.nonzero`

#### 11. Create a 4x4 identity matrix (★☆☆)
`💡hint: np.eye`

#### 12. Create a 2x2x2 array with random values (★☆☆)
`💡hint: np.random.random`

#### 13. Create a 9x9 array with random values and find the minimum and maximum values (★☆☆)
`💡hint: min, max`

#### 14. Create a random vector of size 20 and find the mean value (★☆☆)
`💡hint: mean`

#### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
`💡hint: array[1:-1, 1:-1]`

#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
`💡hint: np.pad`

#### 17. What is the result of the following expression? (★☆☆)
```python
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.7 == 7 * 0.1
```
`💡hint: NaN = not a number, inf = infinity`

#### 18. Create a 6x6 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
`💡hint: np.diag`

#### 19. Create a 6x6 matrix and fill it with a checkerboard pattern (★☆☆)
`💡hint: array[::2]`

#### 20. Consider a (8,9,10) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)
`💡hint: np.unravel_index`

#### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
`💡hint: np.tile`

#### 22. Normalize a 6x6 random matrix (★☆☆)
`💡hint: (x -mean)/std`

#### 23. find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements. (★☆☆)

#### 24. Multiply a 6x3 matrix by a 3x4 matrix (real matrix product) (★☆☆)
`💡hint: np.dot` or `np.ones`

#### 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
`💡hint: >, <`

#### 26. What is the output of the following script? (★☆☆)
```python

print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
```

#### 27. Write a Python program compare two arrays using numpy (★☆☆)
```python
Array a: [1 2]
Array b: [4 5]
a > b 
[False False]
a >= b 
[False False] 
a < b 
[ True True] 
a <= b 
[ True True]
```

#### 28. What are the result of the following expressions? (★☆☆)
```python
np.array(0) / np.array(0)
np.array(0) // np.array(0)
np.array([np.nan]).astype(int).astype(float)
```
Consider an integer vector a
```python
a**a
a << a >> 2
a <- a
1j*a
a/1/1
a<a>a
```

#### 29. How to round away from zero a float array ? (★☆☆)
`💡hint: np.uniform, np.copysign, np.ceil, np.abs, np.where`

#### 30. How to find common values between two arrays? (★☆☆)
`💡hint: np.intersect1d`

#### 31. How to ignore all numpy warnings (not recommended)? (★☆☆)
`💡hint: np.seterr, np.errstate`

#### 32. Is the following expressions true? (★☆☆)
```python
np.sqrt(-1) == np.emath.sqrt(-1)
```
`💡hint: imaginary number`

#### 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
`💡hint: np.datetime64, np.timedelta64`

#### 34. How to get all the dates corresponding to the month of January 2016? (★★☆)
`💡hint: np.arange(dtype=datetime64['D'])`

#### 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
`💡hint: np.add(out=), np.negative(out=), np.multiply(out=), np.divide(out=)`

#### 36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)
`💡hint: %, np.floor, astype, np.trunc`

#### 37. Create a 3x3 matrix with row values ranging from 0 to 2 (★★☆)
`💡hint: np.arange`

#### 38. Consider a generator function that generates 9 integers and use it to build an array (★☆☆)
`💡hint: np.fromiter`

#### 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
`💡hint: np.linspace`

#### 40. Create a random vector of size 10 and sort it (★★☆)
`💡hint: sort`

#### 41. How to sum a small array faster than np.sum? (★★☆)
`💡hint: np.add.reduce`

#### 42. Consider two random array A and B, check if they are equal (★★☆)
`💡hint: np.allclose, np.array_equal`

#### 43. Make an array immutable (read-only) (★★☆)
`💡hint: flags.writeable`

#### 44. Consider a random 5x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)
`💡hint: np.sqrt, np.arctan2`

#### 45. Create random vector of size 5 and replace the maximum value by 0 (★★☆)
`💡hint: argmax`

#### 46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)
`💡hint: np.meshgrid`

#### 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)
`💡hint: np.subtract.outer`

#### 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)
`💡hint: np.iinfo, np.finfo, eps`

#### 49. How to print all the values of an array? (★★☆)
`💡hint: np.set_printoptions`

#### 50. How to find the closest value (to a given scalar) in a vector? (★★☆)
`💡hint: argmin`

#### 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)
`💡hint: dtype`

#### 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)
`💡hint: np.atleast_2d, T, np.sqrt`

#### 53. How to convert a float (32 bits) array into an integer (32 bits) in place?
`💡hint: view and [:] =`

#### 54. How to read the following file? (★★☆)
```
1, 2, 3, 4, 5
6,  ,  , 7, 8
 ,  , 9,10,11
```
`💡hint: np.genfromtxt`

#### 55. What is the equivalent of enumerate for numpy arrays? (★★☆)
`💡hint: np.ndenumerate, np.ndindex`

#### 56. Generate a generic 2D Gaussian-like array (★★☆)
`💡hint: np.meshgrid, np.exp`

#### 57. How to randomly place e elements in a 2D array? (★★☆)
`💡hint: np.put, np.random.choice`

#### 58. Subtract the mean of each row of a matrix (★★☆)
`💡hint: mean(axis=,keepdims=)`

#### 59. How to sort an array by the nth column? (★★☆)
`💡hint: argsort`

#### 60. How to tell if a given 2D array has null columns? (★★☆)
`💡hint: any, ~`

#### 61. Find the nearest value from a given value in an array (★★☆)
`💡hint: np.abs, argmin, flat`

#### 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)
`💡

#### 63. Create an array class that has a name attribute (★★☆)
`💡hint: class method`

#### 64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)
`💡hint: np.bincount | np.add.at`

#### 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)
`💡hint: np.bincount`

#### 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★☆)
`💡hint: np.unique`

#### 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)
`💡hint: sum(axis=(-2,-1))`

#### 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset  indices? (★★★)
`💡hint: np.bincount`

#### 69. How to get the diagonal of a dot product? (★★★)
`💡hint: np.diag`

#### 70. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)
`💡hint: array[::4]`

#### 71. Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)? (★★★)
`💡hint: array[:, :, None]`

#### 72. How to swap two rows of an array? (★★★)
`💡hint: array[[]] = array[[]]`

#### 73. Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the  triangles (★★★)
`💡hint: repeat, np.roll, np.sort, view, np.unique`

#### 74. Given a sorted array C that corresponds to a bincount, how to produce an array A such that np.bincount(A) == C? (★★★)
`💡hint: np.repeat`

#### 75. How to compute averages using a sliding window over an array? (★★★)
`💡hint: np.cumsum`

#### 76. Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z[0],Z[1],Z[2]) and each subsequent row is  shifted by 1 (last row should be (Z[-3],Z[-2],Z[-1]) (★★★)
`💡hint: from numpy.lib import stride_tricks`

#### 77. How to negate a boolean, or to change the sign of a float inplace? (★★★)
`💡hint: np.logical_not, np.negative`

#### 78. Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i (P0[i],P1[i])? (★★★)

#### 79. Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j (P[j]) to each line i (P0[i],P1[i])? (★★★)

#### 80. Consider an arbitrary array, write a function that extract a subpart with a fixed shape and centered on a given element (pad with a `fill` value when necessary) (★★★)
`💡hint: minimum maximum`

#### 81. Consider an array a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], how to generate an array b = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ..., [11,12,13,14]]? (★★★)
`💡hint: stride_tricks.as_strided`

#### 82. Compute a matrix rank (★★★)
`💡hint: np.linalg.svd`

#### 83. How to find the most frequent value in an array?
`💡hint: np.bincount, argmax`

#### 84. Extract all the contiguous 3x3 blocks from a random 10x10 matrix (★★★)
`💡hint: stride_tricks.as_strided`

#### 85. Create a 2D array subclass such that a[i,j] == a[j,i] (★★★)
`💡hint: class method`

#### 86. Consider a set of p matrices wich shape (n,n) and a set of p vectors with shape (n,1). How to compute the sum of of the p matrix products at once? (result has shape (n,1)) (★★★)
`💡hint: np.tensordot`

#### 87. Consider a 16x16 array, how to get the block-sum (block size is 4x4)? (★★★)
`💡hint: np.add.reduceat`

#### 88. How to implement the Game of Life using numpy arrays? (★★★)

#### 89. How to get the n largest values of an array (★★★)
`💡hint: np.argsort | np.argpartition`

#### 90. Given an arbitrary number of vectors, build the cartesian product (every combinations of every item) (★★★)
`💡hint: np.indices`

#### 91. How to create a record array from a regular array? (★★★)
`💡hint: np.core.records.fromarrays`

#### 92. Consider a large vector A, compute A to the power of 3 using 3 different methods (★★★)
`💡hint: np.power, *, np.einsum`

#### 93. Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain elements of each row of B regardless of the order of the elements in B? (★★★)
`💡hint: np.where`

#### 94. Considering a 10x3 matrix, extract rows with unequal values (e.g. [2,2,3]) (★★★)

#### 95. Convert a vector of ints into a matrix binary representation (★★★)
`💡hint: np.unpackbits`

#### 96. Given a two dimensional array, how to extract unique rows? (★★★)
`💡hint: np.ascontiguousarray | np.unique`

#### 97. Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function (★★★)
`💡hint: np.einsum`

#### 98. Considering a path described by two vectors (X,Y), how to sample it using equidistant samples (★★★)?
`💡hint: np.cumsum, np.interp`

```python
import numpy as np

# example X and Y vectors
X = [1, 2, 3, 4, 5]
Y = [5, 4, 3, 2, 1]

# calculate the distance between each pair of consecutive points
distances = np.sqrt(np.diff(X)**2 + np.diff(Y)**2)

# set the desired distance between samples
sample_distance = 0.5

# determine the number of samples to take between each pair of points
n_samples = np.floor(distances / sample_distance).astype(int)

# initialize an empty array to store the samples
samples = []

# iterate through the X and Y vectors, and take equidistant samples
for i in range(len(X)-1):
    x_samples = np.linspace(X[i], X[i+1], n_samples[i]+1)
    y_samples = np.linspace(Y[i], Y[i+1], n_samples[i]+1)
    samples.extend(list(zip(x_samples, y_samples)))

#print samples
print(samples)
```

#### 99. Given an integer n and a 2D array X, select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees, i.e., the rows which only contain integers and which sum to n. (★★★)
`💡hint: np.logical_and.reduce, np.mod`

```python
import numpy as np

# example 2D array
X = np.array([[1, 2, 3], [4, 5, 1], [2, 1, 3], [0, 2, 8], [1, 1, 1]])
n = 6

# select the valid rows
valid_rows = [row for row in X if all(isinstance(i, int) for i in row) and sum(row) == n]

#print valid rows
print(valid_rows)
```

#### 100. Compute bootstrapped 95% confidence intervals for the mean of a 1D array X (i.e., resample the elements of an array with replacement N times, compute the mean of each sample, and then compute percentiles over the means). (★★★)
`💡hint: np.percentile`

```python
import numpy as np

# Create an example 1D array
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Set the number of bootstrap samples
n_samples = 1000

# Initialize an empty array to store the bootstrap sample means
bootstrap_means = np.empty(n_samples)

# Perform the bootstrap sampling and calculate the means
for i in range(n_samples):
    bootstrap_sample = np.random.choice(X, size=len(X), replace=True)
    bootstrap_means[i] = np.mean(bootstrap_sample)

# Compute the 95% confidence intervals
conf_int = np.percentile(bootstrap_means, [2.5, 97.5])
print("95% Confidence interval for the mean:", conf_int)
```

---
