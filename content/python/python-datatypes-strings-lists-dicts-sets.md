# Python Data Types: Numbers, Strings, Lists, Tuples, Dictionaries & Sets

Deep dive into Python built-in data types, complete string manipulation methods, list operations, tuple immutability, dictionary key-value methods, set theory operations, and list comprehensions.

---

# 02_Python_Datatypes 

## Introduction 👋

Data types specify the different sizes and values that can be stored in the variable. For example, Python stores numbers, strings, and a list of values using different data types.

Python is a dynamically typed language; therefore, we do not need to specify the variable’s type while declaring it. Whatever value we assign to the variable based on that data type will be automatically assigned. For example, **`name = 'Arthur'`** here Python will store the name variable as a **`str`** data type.

No matter what value is stored in a variable (object), a variable can be any type like **`int`**, **`float`**, **`str`**, **`list`**, **`set`**, **`tuple`**, **`dict`**, **`bool`**, etc.

---

## Table of contents 📋

| **No.** | **Name** | 
| ------- | -------- | 
| 01 | **[Python_Numbers](https://github.com/milaan9/02_Python_Datatypes/blob/main/001_Python_Numbers.ipynb)** |
| 02 | **[Python_String](https://github.com/milaan9/02_Python_Datatypes/blob/main/002_Python_String.ipynb)** |
|    | 2.1 **[Python_String_Methods](https://github.com/milaan9/02_Python_Datatypes/tree/main/002_Python_String_Methods)** |
| 03 | **[Python_List](https://github.com/milaan9/02_Python_Datatypes/blob/main/003_Python_List.ipynb)** |
|    | 3.1 **[Python_List_Methods](https://github.com/milaan9/02_Python_Datatypes/tree/main/003_Python_List_Methods)** |
| 04 | **[Python_Tuple](https://github.com/milaan9/02_Python_Datatypes/blob/main/004_Python_Tuple.ipynb)** |
|    | 4.1 **[Python_Tuple_Methods](https://github.com/milaan9/02_Python_Datatypes/tree/main/004_Python_Tuple_Methods)** |
| 05 | **[Python_Dictionary](https://github.com/milaan9/02_Python_Datatypes/blob/main/005_Python_Dictionary.ipynb)** |
|    | 5.1 **[Python_Dictionary_Methods](https://github.com/milaan9/02_Python_Datatypes/tree/main/005_Python_Dictionary_Methods)** |
| 06 | **[Python_Sets](https://github.com/milaan9/02_Python_Datatypes/blob/main/006_Python_Sets.ipynb)** |
|    | 6.1 **[Python_Sets_Methods](https://github.com/milaan9/02_Python_Datatypes/tree/main/006_Python_Sets_Methods)** |

These are online **read-only** versions. However you can **`Run ▶`**  all the codes **online** by clicking here ➞ 

---

## Frequently asked questions ❔

### How can I thank you for writing and sharing this tutorial? 🌷

You can <img src="https://img.shields.io/static/v1?label=%E2%AD%90 Star &message=if%20useful&style=style=flat&color=blue" alt="Star Badge"/> and <img src="https://img.shields.io/static/v1?label=%E2%B5%96 Fork &message=if%20useful&style=style=flat&color=blue" alt="Fork Badge"/> Starring and Forking is free for you, but it tells me and other people that it was helpful and you like this tutorial.

Go [**`here`**](https://github.com/milaan9/02_Python_Datatypes) if you aren't here already and click ➞ **`✰ Star`** and **`ⵖ Fork`** button in the top right corner. You'll be asked to create a GitHub account if you don't already have one.

---

### How can I read this tutorial without an Internet connection? <img alt="GIF" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/hmm.gif" width="20" />

1. Go [**`here`**](https://github.com/milaan9/02_Python_Datatypes) and click the big green ➞ **`Code`** button in the top right of the page, then click ➞ [**`Download ZIP`**](https://github.com/milaan9/02_Python_Datatypes/archive/refs/heads/main.zip).

    ![Download ZIP](img/dnld_rep.png) 

2. Extract the ZIP and open it. Unfortunately I don't have any more specific instructions because how exactly this is done depends on which operating system you run.
    
3. Launch ipython notebook from the folder which contains the notebooks. Open each one of them
  
    **`Kernel > Restart & Clear Output`**
    
This will clear all the outputs and now you can understand each statement and learn interactively.

If you have git and you know how to use it, you can also clone the repository instead of downloading a zip and extracting it. An advantage with doing it this way is that you don't need to download the whole tutorial again to get the latest version of it, all you need to do is to pull with git and run ipython notebook again.

---

## Authors ✍️

I'm Dr. Milaan Parmar and I have written this tutorial. If you think you can add/correct/edit and enhance this tutorial you are most welcome🙏

See [github's contributors page](https://github.com/milaan9/02_Python_Datatypes/graphs/contributors) for details.

If you have trouble with this tutorial please tell me about it by [Create an issue on GitHub](https://github.com/milaan9/02_Python_Datatypes/issues/new). and I'll make this tutorial better. This is probably the best choice if you had trouble following the tutorial, and something in it should be explained better. You will be asked to create a GitHub account if you don't already have one.

If you like this tutorial, please [give it a ⭐ star](https://github.com/milaan9/02_Python_Datatypes).

---

## Licence 📜

You may use this tutorial freely at your own risk. See [LICENSE](./LICENSE).

---

## 📘 Python Dictionary Clear()
*Source: `2. Python Datatypes/1. Python Dictionary clear().ipynb`*

# Python Dictionary `clear()`

The **`clear()`** method removes all items from the dictionary.

**Syntax**:

```python
dict.clear()
```

## `clear()` Parameters

The **`clear()`** method doesn't take any parameters.

## Return Value from `clear()`

The **`clear()`** method doesn't return any value (returns **`None`**).

```python
# Example 1: How clear() method works for dictionaries?

d = {1: "one", 2: "two"}

d.clear()
print('d =', d)
```

**Output:**
```text
d = {}
```

---

## 📘 Python List Index()
*Source: `2. Python Datatypes/1. Python List index().ipynb`*

# Python List `index()`

The **`index()`** method returns the index of the specified element in the list.

**Syntax**:

```python
list.index(element, start, end)
```

## `index()` Parameters

The list **`index()`** method can take a maximum of three arguments:

* **element** - the element to be searched
* **start (optional)** - start searching from this index
* **end (optional)** - search the element up to this index

## Return Value from `index()`

* The **`index()`** method returns the index of the given element in the list.
* If the element is not found, a **`ValueError`** exception is raised.

>**Note:** The **`index()`** method only returns the first occurrence of the matching element.

```python
# Example 1: Find the index of the element

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

print('The index of i:', index)
```

**Output:**
```text
The index of e: 1
The index of i: 2
```

```python
# Example 2: Index of the Element not Present in the List

# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# index of'p' is vowels
index = vowels.index('p')
print('The index of p:', index)
```

```python
# Example 3: Working of index() With Start and End Parameters

# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# index of 'i' in alphabets
index = alphabets.index('e')   # 2
print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
index = alphabets.index('i', 3, 5)   # Error!
print('The index of i:', index)
```

**Output:**
```text
The index of e: 1
The index of i: 6
```

---

## 📘 Python Numbers
*Source: `2. Python Datatypes/1. Python Numbers.ipynb`*

# Python Numbers, Type Conversion and Mathematics

In this, you'll learn about the different numbers used in Python, how to convert from one data type to the other, and the mathematical operations supported in Python.

## Number Data Type in Python

Integers, floating point numbers and complex numbers fall under Python numbers category. They are defined as **`int`**, **`float`** and **`complex`** classes in Python.

Integers and floating points are separated by the presence or absence of a decimal point. For instance, 5 is an integer whereas 5.0 is a floating-point number.

Complex numbers are written in the form, `x + yj`, where `x` is the real part and `y` is the imaginary part.

We can use the **type()** function to know which class a variable or a value belongs to. Similarly, the **isinstance()** function is used to check if an object belongs to a particular class.

Let's look at an example:

```python
a = 6

print(type(a)) # type integer

print(type(5.0))  # type float

c = 6 + 3j
print(c + 3)

print(isinstance(c, complex))
```

While integers can be of any length, it is only limited by the memory available.

The numbers we deal with every day are of the decimal (base 10) number system. But computer programmers (generally embedded programmers) need to work with binary (base 2), hexadecimal (base 16) and octal (base 8) number systems.

In Python, we can represent these numbers by appropriately placing a prefix before that number. The following table lists these prefixes.

| Number System | Prefix |
|:----| :--- |
| **`Binary`** |   '0b' or '0B' | 
| **`Octal`** |   '0o' or '0O' | 
| **`Hexadecimal`** |   '0x' or '0X' |

```python
# Example 1:

# Output: 1
print(0b0001)  # 0001 in binary is 1 in decimal and i have use prefix '0b'

# Output: 10  
print(0o12)    # 12 in octadecimal is 10 in decimal and i have use prefix '0o'

# Output: 10
print(0x000A)  # 000A in hexadecimal is 10 in decimal and i have use prefix '0x'
```

**Output:**
```text
1
10
10
```

```python
# Example 2:

# Output: 107
print(0b1101011)

# Output: 253 (251 + 2)
print(0xFB + 0b10) # adding Hex numbers with binary numbers.

# Output: 13
print(0o15)
```

**Output:**
```text
107
253
13
```

## Type Conversion

We can convert one type of number into another. This is also known as coercion.

Operations like addition, subtraction coerce integer to float implicitly (automatically), if one of the operands is float.

```python
1 + 3.0  # adding integer number '1' and a float number '3.0'. The answer will be flaot number '4.0'.
```

**Output:**
```text
4.0
```

We can see above that 1 (integer) is coerced into 1.0 (float) for addition and the result is also a floating point number.

We can also use built-in functions like **`int`**, **`float`** and **`complex`** to convert between types explicitly. These functions can even convert from **strings**.

```python
int(6.3)
```

**Output:**
```text
6
```

```python
int(-2.7)
```

**Output:**
```text
-2
```

```python
float(9)
```

**Output:**
```text
9.0
```

```python
a = 1234567890123456789
print (a)

b = 0.1234567890123456789 # total of only 17 numbers after decimal can be printed.
print (b)

c = 1+2j
print (c)
```

**Output:**
```text
1234567890123456789
0.12345678901234568
(1+2j)
```

When converting from float to integer, the number gets truncated (decimal parts are removed).

```python
complex('3+6j')
```

**Output:**
```text
(3+6j)
```

## Python Decimal

Python built-in class float performs some calculations that might amaze us. We all know that the sum of 1.1 and 2.2 is 3.3, but Python seems to disagree.

```python
(1.1 + 2.2) == 3.3  # The answer should be True but...
```

**Output:**
```text
False
```

**What is going on?**

It turns out that floating-point numbers are implemented in computer hardware as binary fractions as the computer only understands binary (0 and 1). Due to this reason, most of the decimal fractions we know, cannot be accurately stored in our computer.

Let's take an example. We cannot represent the fraction 1/3 as a decimal number. This will give 0.33333333... which is infinitely long, and we can only approximate it.

It turns out that the decimal fraction 0.1 will result in an infinitely long binary fraction of 0.000110011001100110011... and our computer only stores a finite number of it.

This will only approximate 0.1 but never be equal. Hence, it is the limitation of our computer hardware and not an error in Python.

```python
1.1 + 2.2
```

**Output:**
```text
3.3000000000000003
```

To overcome this issue, we can use the decimal module that comes with Python. While floating-point numbers have precision up to 15 decimal places, the decimal module has user-settable precision.

Let's see the difference:

```python
import decimal

print(0.1)

print(decimal.Decimal(0.1))
```

**Output:**
```text
0.1
0.1000000000000000055511151231257827021181583404541015625
```

This module is used when we want to carry out decimal calculations as we learned in school.

It also preserves significance. We know 25.50 kg is more accurate than 25.5 kg as it has two significant decimal places compared to one.

```python
from decimal import Decimal as D

print(D('1.1') + D('2.2'))

print(D('1.2') * D('2.50'))
```

**Output:**
```text
3.3
3.000
```

Notice the trailing zeroes in the above example.

We might ask, why not implement **`Decimal`** every time, instead of float? The main reason is efficiency. Floating point operations are carried out must faster than **`Decimal`** operations.

### When to use Decimal instead of float?

We generally use Decimal in the following cases.

1. When we are making financial applications that need exact decimal representation.
2. When we want to control the level of precision required.
3. When we want to implement the notion of significant decimal places.

## Python Fractions

Python provides operations involving fractional numbers through its **`fractions`** module.

A fraction has a numerator and a denominator, both of which are integers. This module has support for rational number arithmetic.

We can create Fraction objects in various ways. Let's have a look at them.

```python
import fractions

print(fractions.Fraction(1.5))

print(fractions.Fraction(9))

print(fractions.Fraction(1,6))
```

**Output:**
```text
3/2
9
1/6
```

While creating **`Fraction`** from **`float`**, we might get some unusual results. This is due to the imperfect binary floating point number representation as discussed in the previous section.

Fortunately, **`Fraction`** allows us to instantiate with string as well. This is the preferred option when using decimal numbers.

```python
import fractions

# As float
# Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1))  # 1.1 is a number

# As string
# Output: 11/10
print(fractions.Fraction('1.1'))  #'1.1' is a string and not a number
```

**Output:**
```text
2476979795053773/2251799813685248
11/10
```

This data type supports all basic operations. Here are a few examples.

```python
from fractions import Fraction as F  # I changed my Fraction module name to "F"

print(F(1.3) + F(1.3))

print(F(1, 3) + F(1, 3))

print(1 / F(5, 6))

print(F(-3, 10) > 0)

print(F(-3, 10) < 0)
```

**Output:**
```text
5854679515581645/2251799813685248
2/3
6/5
False
True
```

## Python Mathematics

Python offers modules like **`math`** and **`random`** to carry out different mathematics like trigonometry, logarithms, probability and statistics, etc.

```python
import math

print(math.pi)

print(math.cos(math.pi)) # cos(pi) = -1

print(math.exp(10))

print(math.log10(1000)) # log10(1000) = 3

print(math.sinh(1))

print(math.factorial(6))
```

**Output:**
```text
3.141592653589793
-1.0
22026.465794806718
3.0
1.1752011936438014
720
```

```python
import random

print(random.randrange(10, 20))

x = ['a', 'b', 'c', 'd', 'e'] # x is a list class of variable and it has 5 elements.

# Get random choice
print(random.choice(x))

# Shuffle x
random.shuffle(x)

# Print the shuffled x
print(x)

# Print random element
print(random.random())
```

**Output:**
```text
15
b
['d', 'c', 'e', 'a', 'b']
0.8036360430009386
```

When we run the above program we get the output as follows. (Values may be different due to the random behavior)

---

## 📘 Python Set Remove()
*Source: `2. Python Datatypes/1. Python Set remove().ipynb`*

# Python Set `remove()`

The **`remove()`** method removes the specified element from the set.

**Syntax**:

```python
set.remove(element)
```

## `remove()` Parameters

The **`remove()`** method takes a single element as an argument and removes it from the **set**.

## Return Value from `remove()`

The **`remove()`** removes the specified element from the set and updates the set. It doesn't return any value.

If the element passed to **`remove()`** doesn't exist, **KeyError** exception is thrown.

```python
# Example 1: Remove an Element From The Set

set1 = {"Welcome", "to", "Python", "course"}
set1.remove("course")
print(set1)
```

**Output:**
```text
{'to', 'Welcome', 'Python'}
```

```python
# Example 2: Remove an Element From The Set

# language set
language = {'English', 'French', 'German'}

# removing 'German' from language
language.remove('German')

# Updated language set
print('Updated language set:', language)
```

**Output:**
```text
Updated language set: {'English', 'French'}
```

```python
# Example 3: Deleting Element That Doesn't Exist

# animal set
animal = {'cat', 'dog', 'rabbit', 'guinea pig'}

# Deleting 'fish' element
animal.remove('fish')

# Updated animal
print('Updated animal set:', animal)
```

You can use the **set discard() method** if you do not want this error.

The **`discard()`** method removes the specified element from the set. However, if the element doesn't exist, the set remains unchanged; you will not get an error.

---

## 📘 Python String Capitalize()
*Source: `2. Python Datatypes/1. Python String capitalize().ipynb`*

# Python String `capitalize()`

In Python, the **`capitalize()`** method converts first character of a string to uppercase letter and lowercases all other characters, if any.

**Syntax**:

```python
string.capitalize()
```

## `capitalize()` Parameters

The **`capitalize()`** function doesn't take any parameter.

## Return Value from `capitalize()`

The **`capitalize()`** function returns a string with the first letter capitalized and all other characters lowercased. It doesn't modify the original string.

```python
# Example 1: Capitalize a Sentence

string = "python is AWesome."

capitalized_string = string.capitalize()

print('Old String: ', string)
print('Capitalized String:', capitalized_string)
```

**Output:**
```text
Old String:  python is AWesome.
Capitalized String: Python is awesome.
```

```python
# Example 2: Non-alphabetic First Character

string = "+ is an operator."

new_string = string.capitalize()

print('Old String:', string)
print('New String:', new_string)
```

**Output:**
```text
Old String: + is an operator.
New String: + is an operator.
```

---

## 📘 Python Tuple Count()
*Source: `2. Python Datatypes/1. Python Tuple count().ipynb`*

# Python Tuple `count()`

The **`count()`** method returns the number of times the specified element appears in the tuple.

**Syntax**:

```python
tuple.count(element)
```

## `count()` Parameters

The tuple **`count()`** method takes a single argument:

* **element** - the element to be counted

## Return Value from `count()`

The **`count()`** method returns the number of times **`element`** appears in the tuple.

```python
# Example 1: Use of Tuple count()

# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)
```

**Output:**
```text
The count of i is: 2
The count of p is: 0
```

```python
# Example 2: Count List and Tuple Elements Inside Tuple

# random tuple
random = ('a', ('a', 'b'), ('a', 'b'), [3, 4])

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("The count of [3, 4] is:", count)
```

**Output:**
```text
The count of ('a', 'b') is: 2
The count of [3, 4] is: 1
```

---

## 📘 Python Dictionary Copy()
*Source: `2. Python Datatypes/2. Python Dictionary copy().ipynb`*

# Python Dictionary `copy()`

The **`copy()`** method returns a shallow copy of the dictionary.

**Syntax**:

```python
dict.copy()
```

## `copy()` Parameters

The **`copy()`** method doesn't take any parameters.

## Return Value from `copy()`

The **`copy()`** method method returns a shallow copy of the dictionary. It doesn't modify the original dictionary.

```python
# Example 1: How copy works for dictionaries?

original = {1:'one', 2:'two'}
new = original.copy()

print('Orignal: ', original)
print('New: ', new)
```

**Output:**
```text
Orignal:  {1: 'one', 2: 'two'}
New:  {1: 'one', 2: 'two'}
```

## Difference in Using `copy()` method, and `=` Operator to Copy Dictionaries

When **`copy()`** method is used, a new dictionary is created which is filled with a copy of the references from the original dictionary.

When **`=`** operator is used, a new reference to the original dictionary is created.

```python
# Example 2: Using = Operator to Copy Dictionaries

original = {1:'one', 2:'two'}
new = original

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)
```

**Output:**
```text
new:  {}
original:  {}
```

**Note:** Here, when **`new`** dictionary is cleared, **`original`** dictionary is also cleared.

```python
# Example 3: Using copy() to Copy Dictionaries

original = {1:'one', 2:'two'}
new = original.copy()

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)
```

**Output:**
```text
new:  {}
original:  {1: 'one', 2: 'two'}
```

**Note:** Here, when **`new`** dictionary is cleared, **`original`** dictionary remains unchanged.

---

## 📘 Python List Append()
*Source: `2. Python Datatypes/2. Python List append().ipynb`*

# Python List `append()`

The **`append()`** method adds an item to the end of the list.

**Syntax**:

```python
list.append(item)
```

## `append()` Parameters

The **`append()`** method takes a single argument

* **item** - an item to be added at the end of the list

The item can be numbers, strings, dictionaries, another list, and so on.

## Return Value from `append()`

The **`append()`** method doesn't return any value (returns **`None`**).

```python
# Example 1: Adding Element to a List

# animals list
animals = ['cat', 'dog', 'rabbit']

# 'guinea pig' is appended to the animals list
animals.append('guinea pig')

# Updated animals list
print('Updated animals list: ', animals)
```

**Output:**
```text
Updated animals list:  ['cat', 'dog', 'rabbit', 'guinea pig']
```

```python
# Example 2: Adding List to a List

# animals list
animals = ['cat', 'dog', 'rabbit']

# list of wild animals
wild_animals = ['tiger', 'fox']

# appending wild_animals list to the animals list
animals.append(wild_animals)

print('Updated animals list: ', animals)
```

**Output:**
```text
Updated animals list:  ['cat', 'dog', 'rabbit', ['tiger', 'fox']]
```

It is important to notice that, a single item (**`wild_animals`** list) is added to the **`animals`** list in the above program.

If you need to add items of a list to another list (rather than the list itself), use the **list extend() method**.

---

## 📘 Python Set Add()
*Source: `2. Python Datatypes/2. Python Set add().ipynb`*

# Python Set `add()`

The **`add()`** method adds a given element to a **set**. If the element is already present, it doesn't add any element.

**Syntax**:

```python
set.add(elem)
```

**`add()`** method doesn't add an element to the set if it's already present in it.

Also, you don't get back a set if you use **`add()`** method when creating a set object.

```python
noneValue = set().add(elem)
```

The above statement doesn't return a reference to the set but **'None'**, because the statement returns the return type of add which is **`None`**.

## `add()` Parameters

The **`add()`** method takes a single parameter:

* **elem** - the element that is added to the set

## Return Value from `add()`

The **`add()`** method doesn't return any value and returns **`None`**.

```python
# Example 1: Add an element to a set

set1 = set() # creating an empty set

# adding two elements into the set
set1.add(20)
set1.add("Hai")
print(set1)
```

**Output:**
```text
{'Hai', 20}
```

```python
# Example 2: Add an element to a set

# set of vowels
vowels = {'a', 'e', 'i', 'u'}

# adding 'o'
vowels.add('o')
print('Vowels are:', vowels)

# adding 'a' again
vowels.add('a')
print('Vowels are:', vowels)
```

**Output:**
```text
Vowels are: {'o', 'e', 'a', 'u', 'i'}
Vowels are: {'o', 'e', 'a', 'u', 'i'}
```

>**Note:** Order of the vowels can be different.

```python
# Example 3: Add tuple to a set

# set of vowels
vowels = {'a', 'e', 'u'}

# a tuple ('i', 'o')
tup = ('i', 'o')

# adding tuple
vowels.add(tup)
print('Vowels are:', vowels)

# adding same tuple again
vowels.add(tup)
print('Vowels are:', vowels)
```

**Output:**
```text
Vowels are: {'e', ('i', 'o'), 'a', 'u'}
Vowels are: {'e', ('i', 'o'), 'a', 'u'}
```

You can also add **tuples** to a set. And like normal elements, you can add the same tuple only once.

---

## 📘 Python String Center()
*Source: `2. Python Datatypes/2. Python String center().ipynb`*

# Python String `center()`

The **`center()`** method returns a string which is padded with the specified character.

**Syntax**:

```python
string.center(width[, fillchar])
```

## `center()` Parameters

The **`center()`** method takes two arguments:

* **width** - length of the string with padded characters
* **fillchar** (optional) - padding character

The **`fillchar`** argument is optional. If it's not provided, space is taken as default argument.

## Return Value from `center()`

The **`center()`** method returns a string padded with specified **`fillchar`**. It doesn't modify the original string.

```python
# Example 1: center() Method With Default fillchar

string = "Python is awesome"

new_string = string.center(24)

print("Centered String: ", new_string)
```

**Output:**
```text
Centered String:     Python is awesome
```

```python
# Example 2: center() Method With * fillchar

string = "Python is awesome"

new_string = string.center(24, '*')

print("Centered String: ", new_string)
```

**Output:**
```text
Centered String:  ***Python is awesome****
```

---

## 📘 Python String
*Source: `2. Python Datatypes/2. Python String.ipynb`*

# Python Strings

In this class you will learn to create, format, modify and delete strings in Python. Also, you will be introduced to various string operations and functions.

## What is String in Python?

A string is a built-in type sequence of characters. It is used to handle **textual data** in python. Python **Strings are immutable sequences** of **Unicode** points. Creating Strings are simplest and easy to use in Python.

### Summary

| Data types     | Type          |         |
| :------------: | :-----------: |:------: |
| **String**     | **immutable** |  |

A character is simply a symbol. For example, the English language has 26 characters.

Computers do not deal with characters, they deal with numbers (binary). Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0s and 1s.

This conversion of character to a number is called encoding, and the reverse process is decoding. ASCII and Unicode are some of the popular encodings used.

In Python, a string is a sequence of Unicode characters. Unicode was introduced to include every character in all languages and bring uniformity in encoding. These Unicodes range from **$0_{hex}$** to **$10FFFF_{hex}$**. Normally, a Unicode is referred to by writing **"U+"** followed by its **hexadecimal** number. Thus strings in Python are a sequence of Unicode values. You can learn about Unicode from **[Python Unicode](https://docs.python.org/3.3/howto/unicode.html)**.

<div>

</div>

## How to create a string in Python?

Strings can be created by enclosing characters inside a **single quote** or **double-quotes**. Even **triple quotes** can be used in Python but generally used to represent multiline strings and docstrings.

```python
# Example:

print(999)          # ▶ 999 ∵ integer number
print(type(999))    # ▶ <class 'int'>

print("999")        # ▶ 999 ∵ Watever we write inside " " it become string
print(type("999"))  # ▶ <class 'str'>
```

**Output:**
```text
999
<class 'int'>
999
<class 'str'>
```

```python
# Example: defining strings in Python

my_string = 'Hello'  # A string could be a single character or a bunch of texts
print(my_string)     # ▶ Hello

my_string = "Hello"
print(my_string)     # ▶ Hello

my_string = '''Hello'''
print(my_string)     # ▶ Hello

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
```

**Output:**
```text
Hello
Hello
Hello
Hello, welcome to
           the world of Python
```

```python
# Multiline String

multiline_string = '''I am a resarcher cum teacher and I enjoy teaching.
I didn't find anything as rewarding as empowering people.
That's why I created this repository.'''
print(multiline_string)
```

**Output:**
```text
I am a resarcher cum teacher and I enjoy teaching.
I didn't find anything as rewarding as empowering people.
That's why I created this repository.
```

```python
# Another way of doing the same thing

multiline_string = """I am a researcher cum teacher and I enjoy teaching.
I didn't find anything as rewarding as empowering people.
That's why I created this repository."""
print(multiline_string)
```

**Output:**
```text
I am a resarcher cum teacher and I enjoy teaching.
I didn't find anything as rewarding as empowering people.
That's why I created this repository.
```

```python
# Unpacking characters 

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # ▶ P
print(b) # ▶ y
print(c) # ▶ t 
print(d) # ▶ h
print(e) # ▶ o
print(f) # ▶ n
print(h) # ▶ NameError: name 'h' is not defined
```

**Output:**
```text
P
y
t
h
o
n
```

## How to access characters in a string?

* In Python, Strings are stored as individual characters in a **contiguous memory location**. 

* The benefit of using String is that it can be accessed from both the **directions** (forward and backward).

* Both forward as well as backward indexing are provided using Strings in Python.

* Forward indexing starts with **`0,1,2,3,.... `**

* Backward indexing starts with **`-1,-2,-3,-4,.... `**

* Trying to access a character out of index range will raise an **`IndexError`**. The index must be an integer. We can't use floats or other types, this will result into **`IndexError`**.

* Strings can be indexed with square brackets. Indexing starts from zero in Python.

* We can access a range of items in a string by using the slicing operator **`:`**(colon).

* And the **`len()`** function provides the length of a string

```python
str[0] = 'P' = str[-6] ,
str[1] = 'Y' = str[-5] ,
str[2] = 'T' = str[-4] ,
str[3] = 'H' = str[-3] ,
str[4] = 'O' = str[-2] , # refers to the second last item
str[5] = 'N' = str[-1].  # refers to the last item
```

<div>

</div>

```python
language = 'Python'

first_letter = language[0]
print(first_letter)   # ▶ P

second_letter = language[1]
print(second_letter)  # ▶ y

last_index = len(language) - 1  # ∵ 6-1=5
last_letter = language[last_index]
print(last_letter)    # ▶ n
```

**Output:**
```text
P
y
n
```

```python
# If we want to start from right end we can use negative indexing. -1 is the last index

language = 'Python'
last_letter = language[-1]
print(last_letter) # ▶ n
second_last = language[-2]
print(second_last) # ▶ o
```

**Output:**
```text
n
o
```

If we try to access an index out of the range or use numbers other than an integer, we will get errors.

```python
# Accessing string characters in Python
str = 'PYTHON'
print('str = ', str)               # ▶ str =  PYTHON

# index must be an integer
# print('str[1.50] = ', str[1.5])  # ▶ TypeError: string indices must be integers

# index must be in range
# print('str[15] = ', str[15])     # ▶ IndexError: string index out of range
```

**Output:**
```text
str =  PYTHON
```

```python
# Here, we are creating a simple program to retrieve String in reverse as well as normal form.

name="Python"
length=len(name)
i=0

for n in range(-1,(-length-1),-1):
    print(name[i],"\t",name[n])
    i+=1
```

**Output:**
```text
P 	 n
y 	 o
t 	 h
h 	 t
o 	 y
n 	 P
```

## How to slice a string in Python?

Python String **slice** can be defined as a **substring** which is the part of the string. Therefore further substring can be obtained from a string.

There can be many forms to slice a string, as string can be accessed or indexed from both the direction and hence string can also be sliced from both the directions.

Slicing can be best visualized by considering the index to be between the elements as shown below.

If we want to access a range, we need the index that will slice the portion from the string.

<div>

</div>

**Syntax** of Slice Operator :

```python
str[start : stop : step ]
```

other syntax of slice:

```python
str[start : stop]  # items start through stop-1

str[start : ]      # items start through the rest of the array

str[ : stop]       # items from the beginning through stop-1

str[ : ]           # a copy of the whole array
```

```python
s = 'Python'

# 0  1  2  3  4  5  <- Index number: POSITIVE
# P  y  t  h  o  n
#-6 -5 -4 -3 -2 -1  <- Index number: NEGATIVE

# access elements in range with jump/skip
#s[x:y:z] # Start: x Stop:y-1 Jump:z

s[0:5:1]  # ▶ 'Pytho' ∵ Start:0  Stop:5  Jump:1
```

**Output:**
```text
'Pytho'
```

```python
s = '123456789' # Indexing strats from 0 to 8

print("The string '%s' string is %d characters long" %(s, len(s)))  
print('First character of',s,'is',s[0]) 
print('Last character of',s,'is',s[8])
print('Last character of',s,'is',s[len(s)-1]) # [9-1] = [8] is 9
```

**Output:**
```text
The string '123456789' string is 9 characters long
First character of 123456789 is 1
Last character of 123456789 is 9
Last character of 123456789 is 9
```

Negative indices can be used to start counting from the back

```python
print('First character of',s,'is',s[-len(s)])
print('First character of',s,'is',s[(-9)])
print('Second character of',s,'is',s[(-8)])
print('Last character of',s,'is',s[-1])
```

**Output:**
```text
First character of 123456789 is 1
First character of 123456789 is 1
Second character of 123456789 is 2
Last character of 123456789 is 9
```

Finally a substring (range of characters) an be specified as using $a:b$ to specify the characters at index $a,a+1,\ldots,b-1$. Note that the last charcter is *not* included.

```python
print("First three characters",s[0:3])
print("Next three characters",s[3:6])
```

**Output:**
```text
First three characters 123
Next three characters 456
```

An empty beginning and end of the range denotes the beginning/end of the string:

```python
s = '123456789' #Indexing strats from 0 to 8
print("First three characters", s[:3])
print("Last three characters", s[-3:])
```

**Output:**
```text
First three characters 123
Last three characters 789
```

```python
# Accessing string characters in Python

str = 'PYTHON'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[3:-1])
```

**Output:**
```text
str =  PYTHON
str[0] =  P
str[-1] =  N
str[1:5] =  YTHO
str[5:-2] =  HO
```

```python
# Example: 

s="Milan Python"

print(s[6:10])
print(s[-12:-7])
print(s[-1: :-1])  #reversed all string
print(s[2: 10: 2]) #step = 2
print(s[ : : -1])  #reversed all string
print(s[ : 5])     #from 0 to 4
print(s[3 : ])     #from 3 to end of the string
print(s[ : ])      #copy all string
```

**NOTE**: Both the operands passed for concatenation must be of same type, else it will show an error.

## Breaking appart strings

When processing text, the ability to split strings appart is particularly useful. 

* `partition(separator)`: breaks a string into three parts based on a separator

* `split()`: breaks string into words separated by white-space (optionally takes a separator as argument)

* `join()`: joins the result of a split using string as separator

```python
s = "one ➡ two ➡ three"
print( s.partition("➡") )
print( s.split() )
print( s.split(" ➡ ") )
print( ";".join( s.split(" ➡ ") ) )
```

**Output:**
```text
('one ', '➡', ' two ➡ three')
['one', '➡', 'two', '➡', 'three']
['one', 'two', 'three']
one;two;three
```

```python
"This will split all words into a list".split()
```

**Output:**
```text
['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
```

```python
' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
```

**Output:**
```text
'This will join all words into a string'
```

```python
'Happy New Year'.find('ew')
```

**Output:**
```text
7
```

```python
'Happy New Year'.replace('Happy','Brilliant')
```

## How to change or delete a string?

Strings are immutable. This means that elements of a string cannot be changed once they have been assigned. We can simply reassign different strings to the same name.

```python
my_string = 'python'
my_string[5] = 'a'
```

```python
s='012345'
sX=s[:2]+'X'+s[3:] # this creates a new string with 2 replaced by X
print("creating new string",sX,"OK")

sX=s.replace('2','X') # the same thing
print(sX,"still OK")

s[2] = 'X' # an error!!!
```

**Output:**
```text
creating new string 01X345 OK
01X345 still OK
```

We cannot delete or remove characters from a string. But deleting the string entirely is possible using the **`del`** keyword.

```python
my_string = 'python'
del my_string[1]  # deleting element of string generates error!
```

```python
my_string = 'python'
del my_string # deleting whole string using 'del' keyword can delete it.
my_string
```

## Python Strings Operations

There are many operations that can be performed with strings which makes it one of the most used data types in Python.

To learn more about the data types available in Python visit: **Python Data Types**.

To perform operation on string, Python provides basically 3 types of Operators that are given below.

* Basic Operators/Concatenation of Two or More Strings.
* Membership Operators.
* Relational Operators.

### 1. Basic Operators for concatenation of two or more strings

There are two types of basic operators in String **`+`** and **`*`**.

The **`+`** (concatenation) operator can be used to concatenates two or more string literals together.

The **`*`** (Replication) operator can be used to repeat the string for a given number of times.

#### String Concatenation Operator (**`+`**)
Joining of two or more strings into a single one is called concatenation.

```python
# String Concatenation

a = "Hello,"
b= 'World!'
print(a+b)
print(a+" "+b)
```

**Output:**
```text
Hello,World!
Hello, World!
```

```python
# String Concatenation

string1='World'
string2='!'
print('Hello,' + " " + string1 + string2)
```

**Output:**
```text
Hello, World!
```

| Expression | Output |
|:----| :--- |
| **`"10" + "50"`** |   **"1050"**  | 
| **`"hello" + "009"`** |   **"hello009"** | 
| **`"hello99" + "world66" `** |   **"hello99world66"** | 

>**Note:** Both the operands passed for concatenation must be of same type, else it will show an error.

```python
# Example:

print("HelloWorld"+99)
```

#### Python String Replication Operator (**`*`**)

**Replication operator** uses two parameters for operation, One is the integer value and the other one is the String argument.

The Replication operator is used to **repeat a string** number of times. The string will be repeated the number of times which is given by the **integer value**.

| Expression | Output |
|:----| :--- |
| **`"ArcX" \* 2`** |   **"ArcXArcX"**  | 
| **`3 *'5'`** |   **"555"** | 
| **`'@'* 5 `** |   **"@@@@@"** | 

>**Note:**: We can use Replication operator in any way i.e., int **`*`** string or string **`*`** **`int`**. Both the parameters passed cannot be of same type.

```python
# Example:

print("HelloWorld" * 5)
print(3 * "Python")
```

```python
print("Hello World! "*5)  #note the space in between 'Hello' and 'World!'
```

**Output:**
```text
Hello World! Hello World! Hello World! Hello World! Hello World!
```

```python
# Python String Operations
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)
```

**Output:**
```text
str1 + str2 =  HelloWorld!
str1 * 3 = HelloHelloHello
```

If we want to concatenate strings in different lines, we can use parentheses **`()`**.

```python
# two string literals together
'Hello ''World!'
```

**Output:**
```text
'Hello World!'
```

```python
# using parentheses
s = ('Hello '
     'World')
s
```

**Output:**
```text
'Hello World'
```

### Iterating Through a string

We can iterate through a string using a **for loop**. Here is an example to count the number of  'l's in a string.

```python
# Iterating through a string
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')
```

**Output:**
```text
3 letters found
```

### 2. Python String Membership Operators

Membership Operators are already discussed in the Operators section. Let see with context of String.

There are two types of Membership operators :

1. **`in`** - "in" operator returns true if a character or the entire substring is present in the specified string, otherwise false.

2. **`not in`** - "not in" operator returns true if a character or entire substring does not exist in the specified string, otherwise false.

```python
# Example:

str1="HelloWorld"
str2="Hello"
str3="World"
str4="Milan"

print('Exmple of in operator ::')
print(str2 in str1)
print(str3 in str1)
print(str4 in str1)
print()
print(str2 not in str1)
print(str3 not in str1)
print(str4 not in str1)
```

**Output:**
```text
Exmple of in operator ::
True
True
False

False
False
True
```

```python
>>> 'a' in 'program'
True
>>> 'at' not in 'battle'
False
```

**Output:**
```text
False
```

### 3. Python Relational Operators 

All the comparison (relational) operators i.e., **(<, ><=, >=, ==, !=, <>)** are also applicable for strings. The Strings are compared based on the **ASCII value** or **Unicode**(i.e., dictionary Order).

```python
# Example:

print("HelloWorld"=="HelloWorld")
print("helloWorld">="HelloWorld")
print("H"<"h")
```

**Output:**
```text
True
True
True
```

**Explanation:**

The ASCII value of a is 97, b is 98, c is 99 and so on. The ASCII value of A is 65, B is 66, C is 67 and so on. The comparison between strings are done on the basis on ASCII value.

The **`%`** operator is used to format a string inserting the value that comes after. It relies on the string containing a format specifier that identifies where to insert the value. The most common types of format specifiers are:

   - **`%s`** ➡ string
   - **`%d`** ➡ Integer
   - **`%f`** ➡ Float
   - **`%o`** ➡ Octal
   - **`%x`** ➡ Hexadecimal
   - **`%e`** ➡ exponential
    
These will be very familiar to anyone who has ever written a C or Java program and follow nearly exactly the same rules as the **printf() function**.

```python
print("Hello %s" % string1)
print("Actual Number = %d" %19)
print("Float of the number = %f" %19)
print("Octal equivalent of the number = %o" %19)
print("Hexadecimal equivalent of the number = %x" %19)
print("Exponential equivalent of the number = %e" %19)
```

**Output:**
```text
Hello World
Actual Number = 19
Float of the number = 19.000000
Octal equivalent of the number = 23
Hexadecimal equivalent of the number = 13
Exponential equivalent of the number = 1.900000e+01
```

When referring to multiple variables parentheses is used. Values are inserted in the order they appear in the parantheses (more on tuples in the next section)

```python
print("Hello %s %s. My name is Bond, you can call me %d" %(string1,string2,99))
```

**Output:**
```text
Hello World !. My name is Bond, you can call me 99
```

We can also specify the width of the field and the number of decimal places to be used. 
For example:

```python
print('Print width 10: |%10s|'%'x')
print('Print width 10: |%-10s|'%'x') # left justified
print("The number pi = %.1f to 1 decimal places"%3.1415)
print("The number pi = %.2f to 2 decimal places"%3.1415)
print("More space pi = %10.2f"%3.1415)
print("Pad pi with 0 = %010.2f"%3.1415) # pad with zeros
```

**Output:**
```text
Print width 10: |         x|
Print width 10: |x         |
The number pi = 3.1 to 1 decimal places
The number pi = 3.14 to 2 decimal places
More space pi =       3.14
Pad pi with 0 = 0000003.14
```

### Built-in functions to Work with Python

Various built-in functions that work with sequence work with strings as well.

Some of the commonly used ones are **`enumerate()`** and **`len()`**. The **enumerate()** function returns an enumerate object. It contains the index and value of all the items in the string as pairs. This can be useful for iteration.

Similarly, **len()** returns the length (number of characters) of the string.

```python
str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))
```

**Output:**
```text
list(enumerate(str) =  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
len(str) =  4
```

## Python String Formatting

### Escape Sequence

If we want to print a text like `He said, "What's there?"`, we can neither use single quotes nor double quotes. This will result in a SyntaxError as the text itself contains both single and double quotes.

```python
print("He said, "What's there?"")
```

One way to get around this problem is to use triple quotes. Alternatively, we can use escape sequences.

An escape sequence starts with a backslash and is interpreted differently. If we use a single quote to represent a string, all the single quotes inside the string must be escaped. Similar is the case with double quotes. Here is how it can be done to represent the above text.

```python
# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")
```

**Output:**
```text
He said, "What's there?"
He said, "What's there?"
He said, "What's there?"
```

### Here is a list of all the escape sequences supported by Python.

| Escape Sequence | Description |
|:----:| :--- |
| **`\newline`** |   Backslash and newline ignored  | 
| **`\\`** |   Backslash | 
| **`\'`** |   Single quote | 
| **`\"`** |   Double quote | 
| **`\a`** |   ASCII Bell | 
| **`\b`** |   ASCII Backspace | 
| **`\f`** |   ASCII Formfeed | 
| **`\n`** |   ASCII Linefeed | 
| **`\r`** |   ASCII Carriage Return |
| **`\t`** |   ASCII Horizontal Tab | 
| **`\v`** |   ASCII Vertical Tab | 
| **`\ooo`** |   Character with octal value ooo | 
| **`\xHH`** |   Character with hexadecimal value HH |

```python
# Escape sequence

print('I hope every one enjoying the python tutorials.\nDo you ?') # '\n' line break
print('Days\tChapters\tTopics')  # '\t' tab space
print('Day 1\tChp 1\tPython Introduction')
print('Day 2\tChp 2\tPython Datatypes')
print('Day 3\tChp 3\tPython Flow Control')
print('Day 4\tChp 4\tPython Functions')
print('Day 5\tChp 5\tPython Files')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')
```

**Output:**
```text
I hope every one enjoying the python tutorials.
Do you ?
Days	Chapters	Topics
Day 1	Chp 1	Python Introduction
Day 2	Chp 2	Python Datatypes
Day 3	Chp 3	Python Flow Control
Day 4	Chp 4	Python Functions
Day 5	Chp 5	Python Files
This is a back slash  symbol (\)
In every programming language it starts with "Hello, World!"
```

```python
# Here are some examples

print("C:\\Python32\\Lib")
#C:\Python32\Lib

print("This is printed\nin two lines")
#This is printed
#in two lines

print("This is \x48\x45\x58 representation")
#This is HEX representation
```

**Output:**
```text
C:\Python32\Lib
This is printed
in two lines
This is HEX representation
```

### Raw String to ignore escape sequence

Sometimes we may wish to ignore the escape sequences inside a string. To do this we can place **`r`** or **`R`** in front of the string. This will imply that it is a raw string and any escape sequence inside it will be ignored.

```python
print("This is \x61 \ngood example")
```

**Output:**
```text
This is a 
good example
```

```python
print(r"This is \x61 \ngood example")
```

**Output:**
```text
This is \x61 \ngood example
```

### The `format()` Method for Formatting Strings

The **`format()`** method that is available with the string object is very versatile and powerful in formatting strings. Format strings contain curly braces **`{}`** as placeholders or replacement fields which get replaced.

We can use positional arguments or keyword arguments to specify the order.

```python
# Python string format() method

# default(implicit) order
default_order = "{}, {} and {}".format('Allan','Bill','Cory')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('Allan','Bill','Cory')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='Allan',b='Bill',s='Cory')
print('\n--- Keyword Order ---')
print(keyword_order)
```

**Output:**
```text
--- Default Order ---
Allan, Bill and Cory

--- Positional Order ---
Bill, Allan and Cory

--- Keyword Order ---
Cory, Bill and Allan
```

The **`format()`** method can have optional format specifications. They are separated from the field name using colon. For example, we can left-justify **`<`**, right-justify **`>`** or center **`^`** a string in the given space.

We can also format integers as binary, hexadecimal, etc. and floats can be rounded or displayed in the exponent format. There are tons of formatting you can use. Visit here for all the **string formatting available with the format()** method.

```python
# formatting integers
"Binary representation of {0} is {0:b}".format(12)
```

**Output:**
```text
'Binary representation of 12 is 1100'
```

```python
# formatting floats
"Exponent representation: {0:e}".format(1966.365)
```

**Output:**
```text
'Exponent representation: 1.966365e+03'
```

```python
# round off
"One third is: {0:.3f}".format(1/3)
```

**Output:**
```text
'One third is: 0.333'
```

```python
# string alignment
"|{:<10}|{:^10}|{:>10}|".format('bread','butter','jam')
```

**Output:**
```text
'|bread     |  butter  |       jam|'
```

### Old style formatting

We can even format strings like the old **`sprintf()`** style used in C programming language. We use the **`%`** operator to accomplish this.

```python
x = 36.3456789
print('The value of x is %3.2f' %x)
```

**Output:**
```text
The value of x is 36.35
```

```python
print('The value of x is %3.4f' %x)
```

**Output:**
```text
The value of x is 36.3457
```

## Common Python String Methods

There are numerous methods available with the string object. The **`format()`** method that we mentioned above is one of them. 

Strings can be tranformed by a variety of functions that are all methods on a string. That is they are called by putting the function name with a **`.`** after the string. They include:

* Upper vs lower case: **`upper()`**, **`lower()`**, **`captialize()`**, **`title()`** and **`swapcase()`**, **`join()`**, **`split()`**, **`find()`**, **`replace()`** etc, with mostly the obvious meaning. Note that `capitalize` makes the first letter of the string a capital only, while **`title`** selects upper case for the first letter of every word.


* Padding strings: **`center(n)`**, **`ljust(n)`** and **`rjust(n)`** each place the string into a longer string of length n  padded by spaces (centered, left-justified or right-justified respectively). **`zfill(n)`** works similarly but pads with leading zeros.


* Stripping strings: Often we want to remove spaces, this is achived with the functions **`strip()`**, **`lstrip()`**, and **`rstrip()`** respectively to remove from spaces from the both end, just left or just the right respectively. An optional argument can be used to list a set of other characters to be removed.

Here is a complete list of all the **built-in methods to work with Strings in Python**.

```python
# Example:

s="heLLo wORLd!"
print(s.capitalize(),"vs",s.title())

print("upper case: '%s'"%s.upper(),"lower case: '%s'"%s.lower(),"and swapped: '%s'"%s.swapcase())

print('|%s|' % "Hello World".center(30)) # center in 30 characters

print('|%s|'% "     lots of space             ".strip()) # remove leading and trailing whitespace

print('%s without leading/trailing d,h,L or ! = |%s|',s.strip("dhL!"))

print("Hello World".replace("World","Class"))
```

**Output:**
```text
Hello world! vs Hello World!
upper case: 'HELLO WORLD!' lower case: 'hello world!' and swapped: 'HEllO WorlD!'
|         Hello World          |
|lots of space|
%s without leading/trailing d,h,L or ! = |%s| eLLo wOR
Hello Class
```

```python
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'Python Datatypes'
print(challenge.capitalize()) # 'Python Datatypes'
```

**Output:**
```text
Python datatypes
```

```python
# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'Python Datatypes'
print(challenge.count('y')) # 2
print(challenge.count('y', 6, 14)) # 1
print(challenge.count('ty')) # 1
```

**Output:**
```text
2
1
1
```

```python
# endswith(): Checks if a string ends with a specified ending

challenge = 'Python Datatypes'
print(challenge.endswith('es'))   # True
print(challenge.endswith('type')) # False
```

**Output:**
```text
True
False
```

```python
# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'Python\tDatatypes'
print(challenge.expandtabs())   # 'Python  Datatypes'
print(challenge.expandtabs(10)) # 'Python    Datatypes'
```

**Output:**
```text
Python  Datatypes
Python    Datatypes
```

```python
# find(): Returns the index of first occurrence of substring

challenge = 'Python Datatypes'
print(challenge.find('y'))  # 1
print(challenge.find('u')) # -1
```

**Output:**
```text
1
-1
```

```python
# format()	formats string into nicer output    
first_name = 'Dr.'
last_name = 'Strange'
job = 'Doctor'
country = 'India'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Milaan Parmar. I am a Lecturer. I live in Finland.
```

**Output:**
```text
I am Dr. Strange. I am a Doctor. I live in India.
```

```python
# index(): Returns the index of substring

challenge = 'Python Datatypes'
print(challenge.find('y'))  # 1
print(challenge.find('th')) # 2
```

**Output:**
```text
1
2
```

```python
# isalnum(): Checks alphanumeric character

challenge = 'PythonDatatypes'
print(challenge.isalnum()) # True

challenge = 'Pyth0nDatatypes'
print(challenge.isalnum()) # True

challenge = 'Python Datatypes'
print(challenge.isalnum()) # False

challenge = 'Python Datatypes 2021'
print(challenge.isalnum()) # False
```

**Output:**
```text
True
True
False
False
```

```python
# isalpha(): Checks if all characters are alphabets

challenge = 'PythonDatatypes'
print(challenge.isalpha()) # True

num = '123'
print(num.isalpha())      # False
```

**Output:**
```text
True
False
```

```python
# isdecimal(): Checks Decimal Characters

challenge = 'Python Datatypes'
print(challenge.find('y'))  # 1
print(challenge.find('th')) # 2
```

**Output:**
```text
1
2
```

```python
# isdigit(): Checks Digit Characters

challenge = 'Ninety'
print(challenge.isdigit()) # False
challenge = '90'
print(challenge.isdigit())   # True
```

**Output:**
```text
False
True
```

```python
# isdecimal():Checks decimal characters

num = '30'
print(num.isdecimal()) # True
num = '30.6'
print(num.isdecimal()) # False
```

**Output:**
```text
True
False
```

```python
# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '2021PythonDatatypes'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'Python_Datatypes'
print(challenge.isidentifier()) # True
```

**Output:**
```text
False
True
```

```python
# islower():Checks if all alphabets in a string are lowercase

challenge = 'python datatypes'
print(challenge.islower()) # True
challenge = 'Python datatypes'
print(challenge.islower()) # False
```

**Output:**
```text
True
False
```

```python
# isupper(): returns if all characters are uppercase characters

challenge = 'python datatypes'
print(challenge.isupper()) #  False
challenge = 'PYTHON DATATYPES'
print(challenge.isupper()) # True
```

**Output:**
```text
False
True
```

```python
# isnumeric():Checks numeric characters

num = '90'
print(num.isnumeric())         # True
print('ninety'.isnumeric())    # False
```

**Output:**
```text
True
False
```

```python
# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
```

**Output:**
```text
HTML#, CSS#, JavaScript#, React
```

```python
# strip(): Removes both leading and trailing characters

challenge = ' python datatypes '
print(challenge.strip('y')) # 5
```

**Output:**
```text
python datatypes
```

```python
# replace(): Replaces substring inside

challenge = 'python datatypes'
print(challenge.replace('datatypes', 'data-types')) # 'thirty days of coding'
```

**Output:**
```text
python data-types
```

```python
# split():Splits String from Left

challenge = 'python datatypes'
print(challenge.split()) # ['python', 'datatypes']
```

**Output:**
```text
['python', 'datatypes']
```

```python
# title(): Returns a Title Cased String

challenge = 'python datatypes'
print(challenge.title()) # Python Datatypes
```

**Output:**
```text
Python Datatypes
```

```python
# swapcase(): Checks if String Starts with the Specified String
  
challenge = 'python datatypes'
print(challenge.swapcase())   # PYTHON DATATYPES
challenge = 'Python Datatypes'
print(challenge.swapcase())  # pYTHON dATATYPES
```

**Output:**
```text
PYTHON DATATYPES
pYTHON dATATYPES
```

```python
# startswith(): Checks if String Starts with the Specified String

challenge = 'python datatypes'
print(challenge.startswith('python')) # True
challenge = '2 python datatypes'
print(challenge.startswith('two')) # False
```

**Output:**
```text
True
False
```

#### Inspecting Strings

There are also lost of ways to inspect or check strings. Examples of a few of these are given here:

* Checking the start or end of a string: **`startswith("string")`** and **`endswith("string")`** checks if it starts/ends with the string given as argument

* Capitalisation: There are boolean counterparts for all forms of capitalisation, such as **`isupper()`**, **`islower()`** and **`istitle()`**

* Character type: does the string only contain the characters:
  * 0-9: **`isdecimal()`**. Note there is also **`isnumeric()`** and **`isdigit()`** which are effectively the same function except for certain unicode characters
  * a-zA-Z: **`isalpha()`** or combined with digits: **`isalnum()`**
  * non-control code: **`isprintable()`** accepts anything except '\n' an other ASCII control codes
  * \t\n \r (white space characters): **`isspace()`**
  * Suitable as variable name: **`isidentifier()`**
  
* Find elements of string: **`s.count(w)`** finds the number of times **`w`** occurs in **`s`**, while **`s.find(w)`** and **`s.rfind(w)`** find the first and last position of the string **`w`** in **`s`**.

```python
# Example:

s="Hello World"
print("The length of '%s' is"%s,len(s),"characters") # len() gives length of the string

s.startswith("Hello") and s.endswith("World") # check start/end

# count strings
print("There are %d 'l's but only %d World in %s" % (s.count('l'),s.count('World'),s))

print('"el" is at index',s.find('el'),"in",s) #index from 0 or -1
```

**Output:**
```text
The length of 'Hello World' is 11 characters
There are 3 'l's but only 1 World in Hello World
"el" is at index 1 in Hello World
```

## 💻 Exercises ➞ <span class='label label-default'>String</span>

1. Concatenate the string **`Python`**, **`4`**, **`Data`**, **`Science`** to a single string, **`Python 4 Data Science`**.

2. Declare a variable named **`course`** and assign it to an initial value **`Python 4 Data Science`**.

3. Print the length of the **`course`** string using **len()** method and **print()**.

4. Change all the characters of variable company to uppercase and lowercase letters using **upper()** and **lower()** method.

5. Use **capitalize()**, **title()**, **swapcase()** methods to format the value of the string **`Python 4 Data Science`**.

6. Cut(slice) out the first word of **`Python 4 Data Science`**.

7. Check if **`Python 4 Data Science`** string contains a word **`Python`** using the method: **index()**, **find()** or other methods.

8. Change **`Python 4 Data Science`** to **`Python 4 Everybody`** using the **replace()** method or other methods.

9. Split the string **`Python 4 Data Science`** using space as the separator (**split()**).

11. **`Google, Facebook, Microsoft, Apple, IBM, Oracle, Amazon`** split the string at the comma.

12. What is the character at index 9 in the string **`Python 4 Data Science`**.

13. What is the second last index of the string **`Python 4 Data Science`**.

14. Create an acronym or an abbreviation for the name **`Python 4 Data Science`**.

15. Use **index()** to determine the position of the first occurrence of **`D`** in **`Python 4 Data Science`**.

16. Use **rfind** to determine the position of the last occurrence of **`e`** in **`Python 4 Data Science`**.

17. Use **index()** or **find()** to find the position of the first occurrence of the word **`because`** in the following sentence: 

    - **`We cannot end the sentence with ‘because’, because ‘because’ is a conjunction.`**.

18. Use **rindex** to find the position of the first and last occurrence of the word **`because`** in the following sentence: 

    - **`We cannot end the sentence with ‘because’, because ‘because’ is a conjunction.`**.

19. Slice out the phrase **`‘because’, because ‘because’`** in the following sentence: 

    - **`We cannot end the sentence with ‘because’, because ‘because’ is a conjunction.`**.

20. Does **`Python 4 Data Science`** start with a substring **`Python`**?

21. Does '**`Python 4 Data Science`** contains with a substring **`Python`**?

22. **`             Python 4 DataScience                                  `** remove the left and right trailing spaces in the given string.

23. The following list contains the names of some of python libraries: **`['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']`**. Join the list with a hash with space string.

24. Which one of the following variables return True when we use the method **isidentifier()**
    - ```py
    2021PythonDataypes
    Python_Dataypes_2021
    ```
25. Make the following using string formatting methods:

    - ```py
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
    ```

26. Use a **new line** and **tab** escape sequence to print the following lines.
    - ```py
    Name      Age     Country   City
    Milaan    96      Finland   Tampere
    ```

## Advanced string processing
For more advanced string processing there are many libraries available in Python including for example:
* **re** for regular expression based searching and splitting of strings
* **html** for manipulating HTML format text
* **textwrap** for reformatting ASCII text
* ... and many more

---

## 📘 Python Tuple Index()
*Source: `2. Python Datatypes/2. Python Tuple index().ipynb`*

# Python Tuple `index()`

The **`index()`** method returns the index of the specified element in the tuple.

**Syntax**:

```python
tuple.index(element, start, end)
```

## `index()` Parameters

The tuple **`index()`** method can take a maximum of three arguments:

* **element** - the element to be searched
* **start (optional)** - start searching from this index
* **end (optional)** - search the element up to this index

## Return Value from `index()`

* The **`index()`** method returns the index of the given element in the tuple.
* If the element is not found, a **`ValueError`** exception is raised.

>**Note:** The **`index()`** method only returns the first occurrence of the matching element.

```python
# Example 1: Find the index of the element

# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

print('The index of i:', index)
```

**Output:**
```text
The index of e: 1
The index of i: 2
```

```python
# Example 2: Index of the Element not Present in the Tuple

# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'u')

# index of'p' is vowels
index = vowels.index('p')
print('The index of p:', index)
```

```python
# Example 3: Working of index() With Start and End Parameters

# alphabets tuple
alphabets = ('a', 'e', 'i', 'o', 'g', 'l', 'i', 'u')

# index of 'i' in alphabets
index = alphabets.index('e')   # 1
print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
index = alphabets.index('i', 3, 5)   # Error!
print('The index of i:', index)
```

**Output:**
```text
The index of e: 1
The index of i: 6
```

---

## 📘 Python Dictionary Fromkeys()
*Source: `2. Python Datatypes/3. Python Dictionary fromkeys().ipynb`*

# Python Dictionary `fromkeys()`

The **`fromkeys()`** method creates a new dictionary from the given sequence of elements with a value provided by the user.

**Syntax**:

```python
dictionary.fromkeys(sequence[, value])
```

## `fromkeys()` Parameters

The **`fromkeys()`** method takes two parameters:

* **sequence** - sequence of elements which is to be used as keys for the new dictionary
* **value (Optional)** - value which is set to each each element of the dictionary

## Return Value from `fromkeys()`

The **`fromkeys()`** method returns a new dictionary with the given sequence of elements as the keys of the dictionary.

If the value argument is set, each element of the newly created dictionary is set to the provided value.

```python
# Example 1: Create a dictionary from a sequence of keys

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print(vowels)
```

**Output:**
```text
{'i': None, 'u': None, 'o': None, 'a': None, 'e': None}
```

```python
# Example 2: Create a dictionary from a sequence of keys with value

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)
```

**Output:**
```text
{'i': 'vowel', 'u': 'vowel', 'o': 'vowel', 'a': 'vowel', 'e': 'vowel'}
```

```python
# Example 3: Create a dictionary from mutable object list

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

# updating the value
value.append(2)
print(vowels)
```

**Output:**
```text
{'i': [1], 'u': [1], 'o': [1], 'a': [1], 'e': [1]}
{'i': [1, 2], 'u': [1, 2], 'o': [1, 2], 'a': [1, 2], 'e': [1, 2]}
```

**Note:** If **`value`** is a mutable object (whose value can be modified) like **list**, **dictionary**, etc., when the mutable object is modified, each element of the sequence also gets updated.

This is because each element is assigned a reference to the same object (points to the same object in the memory).

To avoid this issue, we use dictionary comprehension.

```python
# Example 4:

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = { key : list(value) for key in keys }
# you can also use { key : value[:] for key in keys }
print(vowels)

# updating the value
value.append(2)
print(vowels)
```

**Output:**
```text
{'i': [1], 'u': [1], 'o': [1], 'a': [1], 'e': [1]}
{'i': [1], 'u': [1], 'o': [1], 'a': [1], 'e': [1]}
```

**Note:** Here, for each key in **`keys`**, a new list from **`value`** is created and assigned to it.

In essence, **`value`** isn't assigned to the element but a new list is created from it, which is then assigned to each element in the dictionary.

---

## 📘 Python List Extend()
*Source: `2. Python Datatypes/3. Python List extend().ipynb`*

# Python List `extend()`

The **`extend()`** method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.

**Syntax**:

```python
list1.extend(iterable)
```

Here, all the elements of **`iterable`** are added to the end of **`list1`**.

## `extend()` Parameters

As mentioned, the **`extend()`** method takes an iterable such as list, tuple, string etc.

## Return Value from `extend()`

The **`extend()`** method modifies the original list. It doesn't return any value.

```python
# Example 1: Using extend() Method

# language list
language = ['French', 'English']

# another list of language
language1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
language.extend(language1)

print('Language List:', language)
```

**Output:**
```text
Language List: ['French', 'English', 'Spanish', 'Portuguese']
```

```python
# Example 2: Add Elements of Tuple and Set to List

# language list
language = ['French']

# language tuple
language_tuple = ('Spanish', 'Portuguese')

# language set
language_set = {'Chinese', 'Japanese'}

# appending language_tuple elements to language
language.extend(language_tuple)

print('New Language List:', language)

# appending language_set elements to language
language.extend(language_set)

print('Newer Language List:', language)
```

**Output:**
```text
New Language List: ['French', 'Spanish', 'Portuguese']
Newer Language List: ['French', 'Spanish', 'Portuguese', 'Chinese', 'Japanese']
```

## Other Ways to Extend a List

You can also append all elements of an iterable to the list using:

**1. the `+` operator**

```python
a = [1, 2]
b = [3, 4]

a += b    # a = a + b

# Output: [1, 2, 3, 4]
print('a =', a)
```

**Output:**
```text
a = [1, 2, 3, 4]
```

**2. the list slicing syntax**

```python
a = [1, 2]
b = [3, 4]

a[len(a):] = b

# Output: [1, 2, 3, 4]
print('a =', a)
```

**Output:**
```text
a = [1, 2, 3, 4]
```

## Python `extend()` Vs `append()`

If you need to add an element to the end of a list, you can use the **`append()`** method.

```python
a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

# a1 = [1, 2, 3, 4]
a1.extend(b) 
print(a1)

# a2 = [1, 2, (3, 4)]
a2.append(b)
print(a2)
```

**Output:**
```text
[1, 2, 3, 4]
[1, 2, (3, 4)]
```

---

## 📘 Python List
*Source: `2. Python Datatypes/3. Python List.ipynb`*

# Python List

In this class, we'll learn everything about Python lists, how they are created, slicing of a list, adding or removing elements from them and so on.

Python offers a range of compound data types often referred to as sequences. List is one of the most frequently used and very versatile data types used in Python.

## What is List in Python?

Python list is a **data structure** which is used to store various types of data.In Python, lists are **mutable** i.e., Python will not create a new list if we modify an element of the list.

It works as a container that holds other objects in a given order. We can perform various operations like insertion and deletion on list. A list can be composed by storing a **sequence** of different type of values **separated by commas**.

### Summary

| Data types     | Type          |         |
| :------------: | :-----------: |:------: |
| **String**     | **immutable** |  |
| **List**       | **mutable**   |✎|

## Creating Python List

In Python programming, a list is created by placing all the items (elements) inside **square brackets `[]`**, separated by **commas** **`,`**. All the elements in list are stored in the index basis with starting index **0**.

It can have any number of items and they may be of different types (integer, float, string etc.).

<div>

</div>

**Syantax:** 

```python
<list_name>=[value1,value2,value3,...,valuen] 
```

```python
# Example:

# empty list, no item in the list
my_list = []  
print(my_list)      # ▶ ()
print(len(my_list)) # ▶ 0

# list of integers
my_list1 = [1, 2, 3]  
print(my_list1)     # ▶ [1, 2, 3]

# list with mixed data types
my_list2 = [1, "Hello", 3.4]
print(my_list2)     # ▶ [1, 'Hello', 3.4]

# nested list
my_list3 = ["mouse", [9, 3, 6], ['a']]
print(my_list3)     # ▶ ["mouse", [9, 3, 6], ['a']]

my_list4=['foo','bar','baz','quz','quux','corge']
print(my_list4)     # ▶ ['foo','bar','baz','quz','quux','corge']

my_list5=[1,2,3,4,4.5,'helloworld','X']
print(my_list5)     # ▶ [1,2,3,4,4.5,'helloworld','X']
```

**Output:**
```text
[]
0
[1, 2, 3]
[1, 'Hello', 3.4]
['mouse', [9, 3, 6], ['a']]
['foo', 'bar', 'baz', 'quz', 'quux', 'corge']
[1, 2, 3, 4, 4.5, 'helloworld', 'X']
```

## Access elements from a list

There are various ways in which we can access the elements of a list.

### List Index

We can use the index operator **`[]`** to access an item in a list. In Python, indices start at 0. So, a list having 5 elements will have an index from 0 to 4.

Trying to access indexes other than these will raise an **`IndexError`**. The index must be an integer. We can't use float or other types, this will result in **`TypeError`**.

Nested lists are accessed using nested indexing.

<div>

</div>

```python
# Example: List indexing

my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list[0]) # ▶  p
print(my_list[2]) # ▶  o
print(my_list[4]) # ▶  e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1]) # ▶ a
print(n_list[1][3]) # ▶ 5

print(my_list[4.0]) # ▶ TypeError: list indices must be integers or slices, not float
```

**Output:**
```text
p
o
e
a
5
```

### Negative indexing

Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

```python
# Example: Negative indexing in lists

# Python allows negative indexing for its sequences. 
#The index of -1 refers to the last item, -2 to the second last item and so on.

my_list = ['p','r','o','b','e']

print(my_list[-1])  # ▶ e
print(my_list[-5])  # ▶ p
```

**Output:**
```text
e
p
```

>**Note:** If the index provided in the list slice is outside the list, then it raises an IndexError exception.

### How to slice lists in Python?

We can access a range of items in a list by using the slicing operator **`:`**(colon).

**Syntax:**

```python
<list_name>[start : stop : step]
```

```python
# Example: List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','n','g']
# indes   [ 0   1   2   3   4   5   6   7   8   9 ]
# index   [-10 -9  -8  -7  -6  -5  -4  -3  -2  -1 ]

print(my_list[2:5])   # ▶ ['o', 'g', 'r'] ∵ elements 3rd to 4th
print(my_list[:-5])   # ▶ ['p', 'r', 'o', 'g', 'r'] ∵ elements beginning to 4th
print(my_list[5:])    # ▶ ['a', 'm', 'i', 'n', 'g'] ∵ elements 5th to end

# elements beginning to end
print(my_list[:])     # ▶ ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n','g')
```

**Output:**
```text
['o', 'g', 'r']
['p', 'r', 'o', 'g', 'r']
['a', 'm', 'i', 'n', 'g']
['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n', 'g']
```

Slicing can be best visualized by considering the index to be between the elements as shown below. So if we want to access a range, we need two indices that will slice that portion from the list.

<div>

</div>

>**NOTE:** Internal Memory Organization:

>List do not store the elements directly at the index. In fact a reference is stored at each index which subsequently refers to the object stored somewhere in the memory. This is due to the fact that some objects may be large enough than other objects and hence they are stored at some other memory location.

```python
# Example:

list=['foo','bar','baz','quz','quux','corge']

print(list[2])         # ▶ baz
print(list[0:])        # ▶ ['foo', 'bar', 'baz', 'quz', 'quux', 'corge'] ∵ if we don't set where to stop it takes all the rest
print(list[4:6])       # ▶ ['quux', 'corge']
print(list[-4:-1])     # ▶ ['baz', 'quz', 'quux'] ∵ it does not include the end index
print(list[1:5:2])     # ▶ ['bar', 'quz'] ∵ it does not include the end index
print(list[-1: :-1])   # ▶ ['corge', 'quux', 'quz', 'baz', 'bar', 'foo'] ∵ reverse list
print(list[-1])        # ▶ corge ∵ last element
print(list[-2])        # ▶ quux ∵ second last element
print(len(list)-1)     # ▶ 5 ∵ index of last element

does_exist = 'bar' in list
print(does_exist)      # ▶ True
```

**Output:**
```text
baz
['foo', 'bar', 'baz', 'quz', 'quux', 'corge']
['quux', 'corge']
['baz', 'quz', 'quux']
['bar', 'quz']
['corge', 'quux', 'quz', 'baz', 'bar', 'foo']
corge
quux
5
True
```

## Python List Operations

Apart from creating and accessing elements from the list, Python allows us to perform various other operations on the list. Some common operations are given below:

### Add/Change List Elements

Lists are mutable, meaning their elements can be changed unlike **string** or **tuple**.

We can use the assignment operator (**`=`**) to change an item or a range of items.

```python
# Example: Correcting mistake values in a list

odd = [2, 4, 6, 8]
  
odd[0] = 1            # ▶ [1, 4, 6, 8] ∵ update 1st element         
print(odd)

odd[1:4] = [3, 5, 7]  # ▶ [1, 3, 5, 7] ∵ update 2nd to 4th elements
print(odd)
```

**Output:**
```text
[1, 4, 6, 8]
[1, 3, 5, 7]
```

```python
# Example:

data1=[5,10,15,20,25]
print(data1) # ▶ [5, 10, 15, 20, 25]

data1[2]="Multiple of 5"  # we are modifying the 3rd element using its index [2] 
print(data1) # ▶ [5, 10, 'Multiple of 5', 20, 25]
```

**Output:**
```text
[5, 10, 15, 20, 25]
[5, 10, 'Multiple of 5', 20, 25]
```

We can add one item to a list using the **`append()`** method or add several items using **`extend()`** method.

```python
# Example: Appending and Extending lists in Python

odd = [1, 3, 5]

odd.append(7)
print(odd)  # ▶ [1, 3, 5, 7]

odd.extend([9, 11, 13])
print(odd)  # ▶ [1, 3, 5, 7, 9, 11, 13]
```

**Output:**
```text
[1, 3, 5, 7]
[1, 3, 5, 7, 9, 11, 13]
```

```python
# Example:

list1=['a','b','c']
list1.append(1.5)
list1.append('x')
list1.append(['y','z']) # append list into list as single object
print(list1)  # ▶ ['a', 'b', 'c', 1.5, 'x', ['y', 'z']]
```

**Output:**
```text
['a', 'b', 'c', 1.5, 'x', ['y', 'z']]
```

We can also use **`+`** (concatenation) operator to combine two lists. This is also called concatenation.

```python
# Example: Concatenating and repeating lists

odd = [1, 3, 5]
print(odd + [9, 7, 5]) # ▶ [1, 3, 5, 9, 7, 5]
```

**Output:**
```text
[1, 3, 5, 9, 7, 5]
```

```python
# Example:

list1=['a','b','c']
list2=['x','y','z']
list3=list1+list2
print(list3)  # ▶ ['a', 'b', 'c', 'x', 'y', 'z']
```

**Output:**
```text
['a', 'b', 'c', 'x', 'y', 'z']
```

```python
# Example:

list1=['a','b','c']
a='x'
print(list1+a)  # ▶ TypeError: can only concatenate list (not "str") to list
```

>**NOTE:** **`+`** operator implies that both the operands passed must be list else error will be shown.

The **`'*'`** operator repeats a list for the given number of times.

```python
# Example: Concatenating and repeating lists

odd = [1, 3, 5]

print(odd + [9, 7, 5])  # ▶ [1, 3, 5, 9, 7, 5]
print(["re"] * 3)       # ▶ ['re', 're', 're']
```

**Output:**
```text
[1, 3, 5, 9, 7, 5]
['re', 're', 're']
```

```python
# Example:

list1=['a','b','c']
print(list1*3)    # ▶ quux ∵ 
print(["re"] * 3) # ▶ quux ∵
```

**Output:**
```text
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
['re', 're', 're']
```

Furthermore, we can insert one item at a desired location by using the method **`insert()`** or insert multiple items by squeezing it into an empty slice of a list.

```python
# Example: Demonstration of list insert() method

odd = [1, 9]
odd.insert(1,3)
print(odd)  # ▶ [1, 3, 9] 

odd[2:2] = [5, 7]
print(odd)  # ▶ [1, 3, 5, 7, 9]
```

**Output:**
```text
[1, 3, 9]
[1, 3, 5, 7, 9]
```

### Delete/Remove List Elements

We can delete one or more items from a list using the keyword **`del`**. It can even delete the list entirely.

```python
# Example: Deleting list items

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

del my_list[2]  # delete one item
print(my_list)  # ▶ ['p', 'r', 'b', 'l', 'e', 'm'] 

del my_list[1:5]  # delete multiple items
print(my_list)  # ▶ ['p', 'm']

del my_list      # delete entire list
print(my_list)   # ▶ NameError: name 'my_list' is not defined
```

**Output:**
```text
['p', 'r', 'b', 'l', 'e', 'm']
['p', 'm']
```

```python
# Example:

list1=['a','b','c']
print("data in list : ",list1)      # ▶ data in list :  ['a', 'b', 'c']

del(list1[2])
print("new data in list : ",list1)  # ▶ new data in list :  ['a', 'b']
```

**Output:**
```text
data in list :  ['a', 'b', 'c']
new data in list :  ['a', 'b']
```

We can use **`remove()`** method to remove the given item or **`pop()`** method to remove an item at the given index.

The **`pop()`** method removes and returns the last item if the index is not provided. This helps us implement lists as stacks (first in, last out data structure).

We can also use the **`clear()`** method to empty a list.

```python
# Example:

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

print(my_list)        # ▶ ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list.pop(1)) # ▶ 'o'
print(my_list)        # ▶ ['r', 'b', 'l', 'e', 'm']
print(my_list.pop())  # ▶ 'm'
print(my_list)        # ▶ ['r', 'b', 'l', 'e']

my_list.clear()
print(my_list)        # ▶ []
```

**Output:**
```text
['r', 'o', 'b', 'l', 'e', 'm']
o
['r', 'b', 'l', 'e', 'm']
m
['r', 'b', 'l', 'e']
[]
```

Finally, we can also delete items in a list by assigning an empty list to a slice of elements.

```python
# Example:

my_list = ['p','r','o','b','l','e','m']

my_list[2:3] = []
print(my_list)  # ▶ ['p', 'r', 'b', 'l', 'e', 'm']

my_list[2:-2] = []
print(my_list)  # ▶ ['p', 'r', 'e', 'm']
```

**Output:**
```text
['p', 'r', 'b', 'l', 'e', 'm']
['p', 'r', 'e', 'm']
```

##  Python Built-in List Functions

Built-in functions like **`all()`**, **`any()`**, **`sorted()`**, **`min()`**, **`max()`**, **`len()`**, **`cmp()`**, **`list()`**, etc. are commonly used with dictionaries to perform different tasks.

| Functions | Description |
|:----| :--- |
| **all()** |   Returns **`True`** if all keys of the list are True. | 
| **any()** |   Returns **`True`** if any key of the list is true. If the list is empty, return **`False`**. | 
| **sorted()** |   Returns a new sorted list of elements in the list. | 
| **min()** |   Returns the minimum value from the list given. | 
| **max()** |   Returns the maximum value from the list given. | 
| **len()** |   Returns number of elements in a list. | 
| **cmp()** |   Compares items of two lists. (Not available in Python 3). | 
| **list()** |   Takes sequence types and converts them to lists. |

### **`all(list)`** - The method all() method returns True when all elements in the given iterable are true. If not, it returns False.

```python
# Example: How all() works for lists?

l = [1, 3, 4, 5]
print(all(l))  # ▶ True ∵ all values true

l = [0, False]
print(all(l))  # ▶ False ∵ all values false

l = [1, 3, 4, 0]
print(all(l))  # ▶ False ∵ one false value

l = [0, False, 5]
print(all(l))  # ▶ False ∵ one true value

l = []
print(all(l))  # ▶ True ∵ empty iterable
```

**Output:**
```text
True
False
False
False
True
```

### **`any(list)`** - any() function returns True if any element of an iterable is True. If not, any() returns False.

```python
# Example: True since 1,3 and 4 (at least one) is true

l = [1, 3, 4, 0]
print(any(l))  # ▶ True 

l = [0, False]
print(any(l))  # ▶ False ∵ both are False

l = [0, False, 5]
print(any(l))  # ▶ True ∵ 5 is true

l = []
print(any(l))  # ▶ False ∵ iterable is empty
```

**Output:**
```text
True
False
True
False
```

### **`sorted(dict)`** - The sorted() function sorts the elements of a given iterable in a specific order (either **ascending** or **descending**) and returns the sorted iterable as a list.

```python
# Example: vowels list

py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list))                # ▶ ['a', 'e', 'i', 'o', 'u']
print(sorted(py_list, reverse=True))  # ▶ ['u', 'o', 'i', 'e', 'a']
```

**Output:**
```text
['a', 'e', 'i', 'o', 'u']
['u', 'o', 'i', 'e', 'a']
```

### **`min(list)`** - this method is used to get min value from the list. In Python3 lists element's type should be same otherwise compiler throw type Error.

```python
# Example:

list1 = ['a','b','c']
list2 = [1,2,3]
list3=['a','b','c',1,2,3]

print(min(list1))  # ▶ a 
print(min(list2))  # ▶ 1
print(min(list3))  # ▶ TypeError: '<' not supported between instances of 'int' and 'str'
```

**Output:**
```text
a
1
```

### **`max(list)`** - The max() method returns the elements from the list with maximum value.

```python
# Example:

list1 = ['a','b','c']
list2 = [1,2,3]
list3=['a','b','c',1,2,3]

print(max(list1))  # ▶ c
print(max(list2))  # ▶ 3
print(max(list3))  # ▶ TypeError: '>' not supported between instances of 'int' and 'str'
```

**Output:**
```text
c
3
```

### **`len(list)`** - The len() method returns the number of elements in the list.

```python
# Example:

list1 = ['a','b','c']
list2 = []
list3=['a','b','c',1,2,3]

print(len(list1))  # ▶ 3
print(len(list2))  # ▶ 0
print(len(list3))  # ▶ 6
```

**Output:**
```text
3
0
6
```

## Python List Methods

Methods that are available with list objects in Python programming are tabulated below. Some of the methods have already been used above.

| Method | Description |
|:----| :--- |
| **append()** | Add an element to the end of the list | 
| **extend()** | Add all elements of a list to the another list |
| **insert()** | Insert an item at the defined index |
| **remove()** | Removes an item from the list |
| **pop()** | Removes and returns an element at the given index 
| **clear()** | Removes all items from the list |
| **index()** | Returns the index of the first matched item | 
| **count()** | Returns the count of the number of items passed as an argument |
| **sort()** | Sort items in a list in ascending order |
| **reverse()** |  Reverse the order of items in the list |
| **copy()** | Returns a shallow copy of the list |

### **`append()`** - The `append()` method adds an item to the end of the list.

```python
# Example:

list1 =[1,2,3]
list1.append(4)
list1.append('helloworld')
list1.append(['a','b','c']) #append as single object
print(list1)  # ▶ [1, 2, 3, 4, 'helloworld', ['a', 'b', 'c']]
```

**Output:**
```text
[1, 2, 3, 4, 'helloworld', ['a', 'b', 'c']]
```

### **`extend()`** - The `extend()` method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.

```python
# Example:

list1 =[1,2,3]
list1.extend([4])
list1.extend('helloworld')
list1.extend(['a','b','c'])
print(list1)  # ▶ [1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'a', 'b', 'c']
```

**Output:**
```text
[1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'a', 'b', 'c']
```

### **`insert()`** - The `insert()` method inserts an element to the list at the specified index.

```python
# Example:

list1 =['helloworld','python','java','c++',1,2,3]
list1.insert(3,'C#')
print(list1)  # ▶ ['helloworld', 'python', 'java', 'C#', 'c++', 1, 2, 3]
```

**Output:**
```text
['helloworld', 'python', 'java', 'C#', 'c++', 1, 2, 3]
```

### **`remove()`** - The `remove()` method removes the first matching element (which is passed as an argument) from the list.

```python
# Example:

list1 =['helloworld','python','java','c++',1,2,3]
list1.remove("java")
print(list1)  # ▶ ['helloworld', 'python', 'c++', 1, 2, 3]
list1.remove(2)
print(list1)  # ▶ ['helloworld', 'python', 'c++', 1, 3]
```

**Output:**
```text
['helloworld', 'python', 'c++', 1, 2, 3]
['helloworld', 'python', 'c++', 1, 3]
```

### **`pop()`** - The `pop()` method removes the item at the given index from the list and returns the removed item.

```python
# Example:

list1 =['helloworld','python','java','c++',1,2,3]
list1.pop()   # pop last element
print(list1)  # ▶ ['helloworld', 'python', 'java', 'c++', 1, 2]
list1.pop(2)  # pop element with index 2
print(list1)  # ▶ ['helloworld', 'python', 'c++', 1, 2]
```

**Output:**
```text
['helloworld', 'python', 'java', 'c++', 1, 2]
['helloworld', 'python', 'c++', 1, 2]
```

### **`clear()`** - The `clear()` method removes all items from the list.

```python
list1 =['helloworld','python','java','c++',1,2,3]
list1.clear()
print('list1:', list1)  # ▶ list1: []
```

**Output:**
```text
list1: []
```

### **`index()`** - The `index()` method returns the index of the specified element in the list.

```python
# Example:

list1 =['helloworld','python','java','c++',1,2,3]
print("index of java : ",list1.index('java'))  # ▶ index of java :  2
print("index of 2 : ",list1.index(2))          # ▶ index of 2 :  5
```

**Output:**
```text
index of java :  2
index of 2 :  5
```

### **`count()`** - The `count()` method returns the number of times the specified element appears in the list.

```python
# Example:

list1 =[1,2,3,'a','b','c',1,2,3]

print(list1.count(1))   # ▶ 2
print(list1.count('b')) # ▶ 1
print(list1.count(4))   # ▶ 0
```

**Output:**
```text
2
1
0
```

### **`sort() `** - The `sort()` method sorts the elements of a given list in a specific ascending or descending order.

```python
# Example:

list1 =[22,30,100,300,399]
list2=['z','ab','abc','a','b']
list1.sort()
list2.sort()
print(list1)  # ▶ [22, 30, 100, 300, 399]

list1.sort(reverse=True)
print(list1)  # ▶ [399, 300, 100, 30, 22]
print(list2)  # ▶ ['a', 'ab', 'abc', 'b', 'z']
```

**Output:**
```text
[22, 30, 100, 300, 399]
[399, 300, 100, 30, 22]
['a', 'ab', 'abc', 'b', 'z']
```

```python
# Example:

list3=['a','b',1,2]
list3.sort()
print(list3)  # ▶ TypeError: '<' not supported between instances of 'int' and 'str'
```

### **`reverse() `** - The `reverse()` method reverses the elements of the list.

```python
# Example:

list1 =['helloworld','python','java','c++',1,2,3]
list1.reverse()
print(list1)  # ▶ [3, 2, 1, 'c++', 'java', 'python', 'helloworld']
```

**Output:**
```text
[3, 2, 1, 'c++', 'java', 'python', 'helloworld']
```

### **`copy() `** - The `copy()` method returns a shallow copy of the list.

```python
list1 =['helloworld','python','java','c++',1,2,3]
list2 = list1.copy()
print('list1:', list1)  # ▶ list1: ['helloworld', 'python', 'java', 'c++', 1, 2, 3]
print('list2:', list2)  # ▶ list2: ['helloworld', 'python', 'java', 'c++', 1, 2, 3]
```

**Output:**
```text
list1: ['helloworld', 'python', 'java', 'c++', 1, 2, 3]
list2: ['helloworld', 'python', 'java', 'c++', 1, 2, 3]
```

Here is a complete list of all the **built-in methods to work with List in Python**.

## List Comprehension: Elegant way to create new List

List comprehension is an elegant and concise way to create a new list from an existing list in Python.

A list comprehension consists of an expression followed by **for loop** inside square brackets.

Here is an example to make a list with each item being increasing power of 2.

```python
pow2 = [2 ** x for x in range(10)]
print(pow2)  # ▶ [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

**Output:**
```text
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

This code is equivalent to:

```python
pow2 = []
for x in range(10):
    pow2.append(2 ** x)
print(pow2)  # ▶ [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

**Output:**
```text
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

A list comprehension can optionally contain more **`for`** or **if statements**. An optional **`if`** statement can filter out items for the new list. Here are some examples.

```python
pow2 = [2 ** x for x in range(10) if x > 5]
pow2  # ▶ [64, 128, 256, 512]
```

**Output:**
```text
[64, 128, 256, 512]
```

```python
odd = [x for x in range(20) if x % 2 == 1]
odd  # ▶ [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

**Output:**
```text
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

```python
[x+y for x in ['Python ','C '] for y in ['Language','Programming']]
```

**Output:**
```text
['Python Language', 'Python Programming', 'C Language', 'C Programming']
```

## Other List Operations in Python

### 1. List Membership Test

We can test if an item exists in a list or not, using the keyword **`in`**.

```python
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# Output: True
print('p' in my_list)  # ▶ True

# Output: False
print('a' in my_list)  # ▶ False

# Output: True
print('c' not in my_list)  # ▶ True
```

**Output:**
```text
True
False
True
```

### 2. Iterating Through a List

Using a for loop we can iterate through each item in a list.

```python
for fruit in ['apple','banana','mango']:
    print("I like",fruit)
```

**Output:**
```text
I like apple
I like banana
I like mango
```

### 3. Other List Operations in Python

Using a **`for`** loop we can iterate through each item in a list.

```python
# Example:

list1=['a','b','c',1,2,3]
for x in list1 :
    print(x)
```

**Output:**
```text
a
b
c
1
2
3
```

```python
for fruit in ['apple','banana','mango']:
    print("I like",fruit)
```

**Output:**
```text
I like apple
I like banana
I like mango
```

## 💻 Exercises  ➞ <span class='label label-default'>List</span>

### Exercises ➞ <span class='label label-default'>Level 1</span>

1. Declare a list with more than 5 items with different data types
2. Find the length of your list
3. Get the first item, the middle item and the last item of the list
4. Declare a list **`called my_info`**, put your (name, age, height, marital status, country)
5. Declare a list variable named **`mix_fruits`** and assign initial values Guava, Mango, Apple, Pear, Fig, Orange and Banana and print the list.
6. Print the list using **print()**
7. Print the number of **`mix_fruits`** in the list
8. Print the first, middle and last fruit
9. Print the list after modifying one of the fruit
10. Add an fruit to variable **`mix_fruits`**
11. Insert an fruit in the middle of the **`mix_fruits`** list
12. Change one of the fruit names to uppercase
13. Join the elements in **`mix_fruits`** with a string **`-#-`**
14. Check if a certain fruit exists in the **`mix_fruits`** list.
15. Sort the list using **sort()** method
16. Reverse the list in descending order using **reverse()** method
17. Slice out the first 3 fruits from the list
18. Slice out the last 3 fruits from the list
19. Slice out the middle fruit or fruits from the list
20. Remove the first fruit from the list
21. Remove the middle fruit or companies from the list
22. Remove the last fruit from the list
23. Remove all fruits from the list
24. Delete the fruits list
25. Join the following lists:

    - ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```

26. After joining the lists in question 25. Copy the joined list and assign it to a variable full_stack. Then insert **`'Python'`** and **`'SQL'`** after **`'Redux'`**.

### Exercises ➞ <span class='label label-default'>Level 2</span>

1. The following is a list of 10 students ages:

    - ```py
ages = [19, 23, 19, 25, 21, 20, 25, 26, 25, 24]
    ```

        - Sort the list and find the min and max age
        - Add the min age and the max age again to the list
        - Find the median age (one middle item or two middle items divided by two)
        - Find the average age (sum of all items divided by their number )
        - Find the range of the ages (max - min)
        - Compare the value of (min - average) and (max - average), use **abs()** method

2. Find the middle country(ies) in the **countries list**
3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
4. **`['India', 'Russia', 'China', 'Finland', 'Sweden', 'Norway', 'Denmark']`**. Unpack the first three countries and the rest as scandic countries.

---

## 📘 Python Set Copy()
*Source: `2. Python Datatypes/3. Python Set copy().ipynb`*

# Python Set `copy()`

The **`copy()`** method adds a given element to a set. If the element is already present, it doesn't add any element.

A **set** can be copied using = operator in Python. For example:
```python
numbers = {1, 2, 3, 4}
new_numbers = numbers
```

The problem with copying the set in this way is that if you modify the **`numbers`** set, the **`new_numbers`** set is also modified.

```python
# Example:

numbers = {1, 2, 3, 4}
new_numbers = numbers

new_numbers.add(5)

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)
```

**Output:**
```text
numbers:  {1, 2, 3, 4, 5}
new_numbers:  {1, 2, 3, 4, 5}
```

However, if you need the original set to be unchanged when the new set is modified, you can use the **`copy()`** method.

**Syntax**:

```python
set.copy()
```

## `copy()` Parameters

The **`copy()`** method doesn't take any parameters.

## Return Value from `copy()`

The **`copy()`** method returns a shallow copy of the set.

```python
# Example 1: How the copy() method works for sets?

numbers = {1, 2, 3, 4}
new_numbers = numbers.copy()

new_numbers.add(5)

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)
```

**Output:**
```text
numbers:  {1, 2, 3, 4}
new_numbers:  {1, 2, 3, 4, 5}
```

---

## 📘 Python String Casefold()
*Source: `2. Python Datatypes/3. Python String casefold().ipynb`*

# Python String `casefold()`

The **`casefold()`** method is an aggressive lower() method which converts strings to case folded strings for caseless matching.

The **`casefold()`** method removes all case distinctions present in a **string**. It is used for caseless matching, i.e. ignores cases when comparing.

For example, the German lowercase letter **`ß`** is equivalent to **`ss`**. However, since **`ß`** is already lowercase, the **`lower()`** method does nothing to it. But, **`casefold()`** converts it to **`ss`**.

**Syntax**:

```python
string.casefold()
```

## `casefold()` Parameters

The **`casefold()`** method doesn't take any parameters.

## Return Value from `casefold()`

The **`casefold()`** method returns the case folded string.

```python
# Example 1: Lowercase using casefold()

string = "PYTHON IS AWESOME"

# print lowercase string
print("Lowercase string:", string.casefold())
```

**Output:**
```text
Lowercase string: python is awesome
```

```python
# Example 2: Comparison using casefold()

firstString = "der Fluß"
secondString = "der Fluss"

# ß is equivalent to ss
if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')
```

**Output:**
```text
The strings are equal.
```

---

## 📘 Python Dictionary Get()
*Source: `2. Python Datatypes/4. Python Dictionary get().ipynb`*

# Python Dictionary `get()`

The **`get()`** method returns the value for the specified key if key is in dictionary.

**Syntax**:

```python
dict.get(key[, value]) 
```

## `get()` Parameters

The **`get()`** method takes maximum of two parameters:

* **key** - key to be searched in the dictionary
* **value** (optional) - Value to be returned if the **`key`** is not found. The default value is **`None`**.

## Return Value from `get()`

The **`get()`** method returns:

* the value for the specified **`key`** if **`key`** is in dictionary.
* **`None`** if the **`key`** is not found and **`value`** is not specified.
* **`value`** if the **`key`** is not found and **`value`** is specified.

```python
# Example 1: How get() works for dictionaries?

person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))
```

**Output:**
```text
Name:  Phill
Age:  22
Salary:  None
Salary:  0.0
```

## Python `get()` method Vs `dict[key]` to Access Elements

**`get()`** method returns a default value if the **`key`** is missing.

However, if the **`key`** is not found when you use **`dict[key]`**, **`KeyError`** exception is raised.

```python
# Example 1:

person = {}

# Using get() results in None
print('Salary: ', person.get('salary'))

# Using [] results in KeyError
print(person['salary'])
```

**Output:**
```text
Salary:  None
```

---

## 📘 Python List Insert()
*Source: `2. Python Datatypes/4. Python List insert().ipynb`*

# Python List `insert()`

The list **`insert()`** method inserts an element to the list at the specified index.

**Syntax**:

```python
list.insert(i, elem)
```

Here, **`elem`** is inserted to the list at the **$i_{th}$** index. All the elements after **`elem`** are shifted to the right.

## `insert()` Parameters

The **`insert()`** method takes two parameters:

* **index** - the index where the element needs to be inserted
* **element** - this is the element to be inserted in the list

>**Notes:**
* If **`index`** is 0, the element is inserted at the beginning of the list.
* If **`index`** is 3, the element is inserted after the 3rd element. Its position will be 4th.

## Return Value from `insert()`

The **`insert()`** method doesn't return anything; returns None. It only updates the current list.

```python
# Example 1: Inserting an Element to the List

# vowel list
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3
# the position of 'o' will be 4th
vowel.insert(3, 'o')

print('Updated List:', vowel)
```

**Output:**
```text
Updated List: ['a', 'e', 'i', 'o', 'u']
```

```python
# Example 2: Inserting a Tuple (as an Element) to the List

mixed_list = [{1, 2}, [5, 6, 7]]

# number tuple
number_tuple = (3, 4)

# inserting a tuple to the list
mixed_list.insert(1, number_tuple)

print('Updated List:', mixed_list)
```

**Output:**
```text
Updated List: [{1, 2}, (3, 4), [5, 6, 7]]
```

---

## 📘 Python Set Clear()
*Source: `2. Python Datatypes/4. Python Set clear().ipynb`*

# Python Set `clear()`

The **`clear()`** method removes all elements from the set.

**Syntax**:

```python
set.clear()
```

## `clear()` Parameters

The **`clear()`** ethod doesn't take any parameters.

## Return Value from `clear()`

The **`clear()`** method doesn't return any value and returns **`None`**.

```python
# Example 1: Remove all elements from a Python set using clear()

# set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}
print('Vowels (before clear):', vowels)

# clearing vowels
vowels.clear()
print('Vowels (after clear):', vowels)
```

**Output:**
```text
Vowels (before clear): {'u', 'e', 'i', 'o', 'a'}
Vowels (after clear): set()
```

```python
# Example 2: Remove all elements from a Python set using clear()

set1 = {"Welcome", "to", "Python", "course"}
set1.clear()
print(set1)
```

**Output:**
```text
set()
```

### `del()`

The **del()** keyword deletes the set.

```python
# Example 1:

#deleting a set
set1 = {"Welcome", "to", "Python", "course"}
del set1
print(set1)
```

---

## 📘 Python String Count()
*Source: `2. Python Datatypes/4. Python String count().ipynb`*

# Python String `count()`

The **`count()`** method returns the number of occurrences of a substring in the given string.

In simple words, **`count()`** method searches the substring in the given **string** and returns how many times the substring is present in it.

It also takes optional parameters **`start`** and **`end`** to specify the starting and ending positions in the string respectively.

**Syntax**:

```python
string.count(substring, start=..., end=...)
```

## `count()` Parameters

The **`count()`** method only requires a single parameter for execution. However, it also has two optional parameters:

* **substring** - string whose count is to be found.
* **start (Optional)** - starting index within the string where search starts.
* **end (Optional)** - ending index within the string where search ends.

>**Note:** Index in Python starts from 0, not 1.

## Return Value from `count()`

The **`count()`** method returns the number of occurrences of the substring in the given string.

```python
# Example 1: Count number of occurrences of a given substring

# define string
string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)
```

**Output:**
```text
The count is: 2
```

```python
# Example 2: Count number of occurrences of a given substring using start and end

# define string
string = "Python is awesome, isn't it?"
substring = "i"

# count after first 'i' and before the last 'i'
count = string.count(substring, 8, 25)

# print count
print("The count is:", count)
```

**Output:**
```text
The count is: 1
```

**Explanation:** Here, the counting starts after the first **`i`** has been encountered, i.e. **`7th`** index position.

And, it ends before the last **`i`**, i.e. **`25th`** index position.

```python
# Example 3:

s="I Love Python Tutorial"
print(s.count('o'))      # 3
print(s.count('o',5))    # 2
print(s.count('t'))      # 2
print(s.count('t',2,9))  # 0
```

**Output:**
```text
3
2
2
0
```

---

## 📘 Python Tuple
*Source: `2. Python Datatypes/4. Python Tuple.ipynb`*

# Python Tuple

In this class, you'll learn everything about Python tuples. More specifically, what are tuples, how to create them, when to use them and various methods you should be familiar with.

## What is Tuple in Python?

A tuple in Python is similar to a **list**. 
Only the difference is that list is enclosed between **square bracket** **`[]`**, tuple between **parentheses** **`()`** and we cannot change the elements of a tuple once it is assigned, i.e., **immutable** whereas we can change the elements of a list i.e., **mutable**.

### Summary

| Data types     | Type          |         |
| :------------: | :-----------: |:------: |
| **String**     | **immutable** |  |
| **List**       | **mutable**   |✎|
| **Tuple**      | **immutable** |  |

## Creating Python Tuple

A tuple is created by placing all the items (elements) inside **parentheses `()`**, separated by **commas `,`**. The parentheses are optional, however, it is a good practice to use them.

A tuple can have any number of items and they may be of different types (integer, float, list, **string**, etc.).

<div>

</div>

```python
# Example:

# Different types of tuples

# Empty tuple
my_tuple1 = ()
print(my_tuple1)  # ▶ ()

# Tuple having integers
my_tuple2 = (1, 2, 3)
print(my_tuple2)  # ▶ (1, 2, 3)

# tuple with mixed datatypes
my_tuple3 = (1, "Hello", 3.4)
print(my_tuple3)  # ▶ (1, "Hello", 3.4)

# nested tuple
my_tuple4 = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple4)  # ▶ ("mouse", [8, 4, 6], (1, 2, 3))
len(my_tuple4)    # ▶ 3
```

**Output:**
```text
()
(1, 2, 3)
(1, 'Hello', 3.4)
('mouse', [8, 4, 6], (1, 2, 3))
3
```

A tuple can also be created without using parentheses. This is known as tuple packing.

```python
# Example:

my_tuple = 3, 4.6, "dog"   # ∵ paranthesis () is not mandatory
print(my_tuple)  # ▶ (3, 4.6, 'dog')

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)        # ▶ 3
print(b)        # ▶ 4.6
print(c)        # ▶ dog
```

**Output:**
```text
(3, 4.6, 'dog')
3
4.6
dog
```

```python
# Example:

t1 = ('a b', 1, 2, 3.14, "HelloWorld")
t2 = "a", "b", "c", "d"

#tuple contain other list and tuple
t3 =(1, 2, 3, ['a','b','c'], ('z', 26))

print(t1)  # ▶ ('a b', 1, 2, 3.14, 'HelloWorld')
print(t2)  # ▶ ('a', 'b', 'c', 'd')
print(t3)  # ▶ (1, 2, 3, ['a', 'b', 'c'], ('z', 26))
```

**Output:**
```text
('a b', 1, 2, 3.14, 'HelloWorld')
('a', 'b', 'c', 'd')
(1, 2, 3, ['a', 'b', 'c'], ('z', 26))
```

Creating a tuple with one element is a bit tricky.

Having one element within parentheses **`()`** is not enough. We must need a trailing comma **`,`** to indicate that it is, in fact, a tuple.

```python
# Example:

t1 = 5  # without () and comma ","
print(t1)       # ▶ 5  
print(type(t1)) # ▶ <class 'int'>

t2 = 5, # with ","
print(t2)       # ▶ (5,)
print(type(t2)) # ▶ <class 'tuple'>

t3 = (5) # without ","  That means () is not important, ',' is important
print(t3)       # ▶ 5
print(type(t3)) # ▶ <class 'int'>

t4 = (5,)       
print(t4)       # ▶ 5
print(type(t4)) # ▶ <class 'tuple'>
```

**Output:**
```text
5
<class 'int'>
(5,)
<class 'tuple'>
5
<class 'int'>
(5,)
<class 'tuple'>
```

## Access Tuple Elements

There are various ways in which we can access the elements of a tuple.

### 1. Indexing

We can use the **index operator** **`[]`** to access an item in a tuple, where the index starts from 0.

So, a tuple having 6 elements will have indices from 0 to 5. Trying to access an index outside of the tuple index range(6,7,... in this example) will raise an **`IndexError`**.

The index must be an integer, so we cannot use float or other types. This will result in **`TypeError`**.

```python
# Accessing tuple elements using indexing

my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # ▶ 'p' 
print(my_tuple[5])   # ▶ 't'

print("Last index:", len(my_tuple) - 1)             # ▶ Last index: 5
print("Last element:", my_tuple[len(my_tuple) - 1]) # ▶ Last element: t

# Index must be within range
# print(my_tuple[6]) # ▶ IndexError: list index out of range

# Index must be an integer
# my_tuple[2.0] # ▶ TypeError: tuple indices must be integers or slices, not float
```

**Output:**
```text
p
t
Last index: 5
Last element: t
```

```python
# Example: 

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[2][0])  # ▶ 1  ∵ element with index 2 and within sub-element with index 0
print(n_tuple[0][3])  # ▶ s  ∵ element with index 0 and within sub-element with index 3
```

**Output:**
```text
1
s
```

```python
# Example:

t=("helloworld",'xyz',1,-2,3.6)
for x in t:
    print(x)
```

**Output:**
```text
helloworld
xyz
1
-2
3.6
```

### 2. Negative Indexing

Python allows negative indexing for its sequences.

The index of -1 refers to the last item, -2 to the second last item and so on.

```python
# Example: Negative indexing for accessing tuple elements

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

print(my_tuple[-1])   # ▶ t
print(my_tuple[-6])   # ▶ p
```

**Output:**
```text
t
p
```

<div>

</div>

```python
# Example:

t=(3,7,4,2)

print(t[2])           # ▶ 4
print(t[1:3])         # ▶ (7, 4)
print(t[-3])          # ▶ 7
print(t[-4:-2])       # ▶ (3, 7)
print(t[-1 :  : -1])  # ▶ (2, 4, 7, 3) ∵ start from -1 and step =-1 so its basicly return reverse tuple
```

**Output:**
```text
4
(7, 4)
7
(3, 7)
(2, 4, 7, 3)
```

### 3. Slicing

We can access a range of items in a tuple by using the slicing operator **`:`**(colon).

**Syntax:**

```python
tuple[start : stop : step]
```
by default step is +1

```python
# Example: Accessing tuple elements using slicing

my_tuple = ('p','r','o','g','r','a','m','i','n','g')

# elements 2nd to 4th
print(my_tuple[1:4])   # ▶ ('r', 'o', 'g')

# elements beginning to 2nd
print(my_tuple[:-7])   # ▶ ('p', 'r')

# elements 8th to end
print(my_tuple[7:])    # ▶ ('i', 'z')

# elements beginning to end
print(my_tuple[:])     # ▶ ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n','g')
```

**Output:**
```text
('r', 'o', 'g')
('p', 'r', 'o')
('i', 'n', 'g')
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n', 'g')
```

Slicing can be best visualized by considering the index to be between the elements as shown below. So if we want to access a range, we need the index that will slice the portion from the tuple.

<div>

</div>

## Tuple Operations

### 1. Changing a Tuple

Unlike lists, **tuples are immutable**.

This means that elements of a tuple cannot be changed once they have been assigned. But, if the element is itself a mutable data type like a list, its nested items can be changed.

We can also assign a tuple to different values (reassignment).

```python
# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])

# my_tuple[1] = 9     # ▶ TypeError: 'tuple' object does not support item assignment

# However, item of mutable element can be changed
my_tuple[3][0] = 9    
print(my_tuple)  # ▶ (4, 2, 3, [9, 5])

# Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n', 'g')
print(my_tuple)  # ▶ ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', ''n', 'g')
```

**Output:**
```text
(4, 2, 3, [9, 5])
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n', 'g')
```

We can use **`+`** operator to combine two tuples. This is called **concatenation**.

We can also repeat the elements in a tuple for a given number of times using the **`*`** operator.

Both **`+`** and **`*`** operations result in a new tuple.

```python
# Example 1:

# Concatenation
print((1, 2, 3) + (4, 5, 6))  # ▶ (1, 2, 3, 4, 5, 6)

# Repeat
print(("Repeat",) * 3)       # ▶ ('Repeat', 'Repeat', 'Repeat')
```

**Output:**
```text
(1, 2, 3, 4, 5, 6)
('Repeat', 'Repeat', 'Repeat')
```

```python
# Example 2:

t1=(1,2,3)
t2=('x','y','z')
t3=t1+t2
print(t3)   # ▶ (1, 2, 3, 'x', 'y', 'z')
print(t1*2) # ▶ (1, 2, 3, 1, 2, 3)
print(t2*3) # ▶ ('x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z')
```

**Output:**
```text
(1, 2, 3, 'x', 'y', 'z')
(1, 2, 3, 1, 2, 3)
('x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z')
```

```python
# Example 3:

t1 = (1, 2,3)
t2 = ('abc', 'xyz')

# Following action is not valid for tuples
# t1[0] = 4;
# So let's create a new tuple as follows
t3 = t1 + t2 + ("hey",)  # ∵ () is must when adding or multiply tuples
print (t3)               # ▶ (1, 2, 3, 'abc', 'xyz', 'hey')
```

**Output:**
```text
(1, 2, 3, 'abc', 'xyz', 'hey')
```

### 2. Deleting a Tuple

As discussed above, we cannot change the elements in a tuple. It means that we cannot delete or remove items from a tuple.

Deleting a tuple entirely, however, is possible using the keyword **del**.

```python
# Example 1: Deleting tuples

my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n', 'g')

# can't delete items
del my_tuple[3]  # ▶ TypeError: 'tuple' object doesn't support item deletion

# Can delete an entire tuple
# del my_tuple
# print(my_tuple)   # ▶ NameError: name 'my_tuple' is not defined
```

```python
# Example 2:

t = ('helloWorld', "python", 1, 2.7);
print (t)          # ▶ ('helloWorld', 'python', 1, 2.7)

# can't delete items
del my_tuple[3]  # ▶ TypeError: 'tuple' object doesn't support item deletion

del t
# print ("After deleting t :")  # ▶ After deleting t :
# print (t)                     # ▶ NameError: name 't' is not defined
```

**Output:**
```text
('helloWorld', 'python', 1, 2.7)
```

## Python Built-in Tuple Functions

| Function | Description |
|:----| :--- |
| **len()** |  Returns number of elements in a tuple. | 
| **max()** |  Returns item from the tuple with max value. | 
| **min()** |  Returns item from the tuple with min value.  | 
| **sorted()** |  Returns a new sorted list of sequence in the tuple. | 
| **tuple()** |  Converts a sequence into tuple.  | 
| **cmp()** |  Compares items of two tuples. (Not available in Python 3).  |

### **`len(tuple)`** - The `len()` method returns the number of elements in the tuple.

```python
# Example:

t1= (1,2,3,4,5)
t2 = ('x','y','z',[1,2],3)
print(len(t1))  # ▶ 5
print(len(t2))  # ▶ 5
```

**Output:**
```text
5
5
```

### **`max(tuple)`** - The `max()` method returns the elements from the tuple with maximum value. Type of element should be same otherwise complier throw `TypeError`.

```python
# Example:

t1= (1,2,3,4,5)
t2 = ('x','y','z')
print(max(t1))  # ▶ 5
print(max(t2))  # ▶ z
```

**Output:**
```text
5
z
```

### **`min(tuple)`** - The `min()` method returns the elements from the tuple with minimum value. Type of element should be same otherwise complier throw `TypeError`.

```python
# Example:

t1= (1,2,3,4,5)
t2 = ('x','y','z')
print(min(t1))  # ▶ 1
print(min(t2))  # ▶ x
```

**Output:**
```text
1
x
```

### **`sorted(dict)`** - The `sorted()` function sorts the elements of a given iterable in a specific order (either **ascending** or **descending**) and returns the sorted iterable as a list.

```python
# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))                # ▶ ['a', 'e', 'i', 'o', 'u']
print(sorted(py_tuple, reverse=True))  # ▶ ['u', 'o', 'i', 'e', 'a']
```

**Output:**
```text
['a', 'e', 'i', 'o', 'u']
['u', 'o', 'i', 'e', 'a']
```

### **`tuple(seq)`** - The `tuple()` method converts a list of items into tuples.

```python
# Example:

s="helloworld"
t1=tuple(s)
list=[1,2,3]
t2=tuple(list)

print(t1)  # ▶ ('h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd')
print(t2)  # ▶ (1, 2, 3)
```

**Output:**
```text
('h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd')
(1, 2, 3)
```

## Tuple Methods

Methods that add items or remove items are not available with tuple. Only the following two methods are available.

Some examples of Python tuple methods:

```python
# Example:

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))   # ▶  2
print(my_tuple.index('l'))   # ▶  3
```

**Output:**
```text
2
3
```

## Other Tuple Operations

### 1. Tuple Membership Test

We can test if an item exists in a tuple or not, using the keyword **`in`**.

```python
# Example: Membership test in tuple

my_tuple = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in my_tuple)      # ▶ True
print('b' in my_tuple)      # ▶ False

# Not in operation
print('g' not in my_tuple)  # ▶ True
```

**Output:**
```text
True
False
True
```

### 2. Iterating Through a Tuple

We can use a **`for`** loop to iterate through each item in a tuple.

```python
# Example: Using a for loop to iterate through a tuple

for name in ('John', 'Kate'):
    print("Hello", name)
```

**Output:**
```text
Hello John
Hello Kate
```

## Why should we use Tuple? (Advantages of Tuple)

* Processing of Tuples are **faster** than Lists. 
* It makes the data **safe** as Tuples are **immutable** and hence cannot be changed.
* Tuples are used for **string formatting**.

## Advantages of Tuple over List

Since tuples are quite similar to lists, both of them are used in similar situations. However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:

* We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.

* Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.

* Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.

* If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

## 💻 Exercises ➞ <span class='label label-default'>Tuple</span>

### Exercises ➞ <span class='label label-default'>Level 1</span>

1. Create a tuple containing names of **`fruits`** and **`vegetables`**
2. Join **`fruits`** and **`vegetables`** tuples and assign it to **`fruits_vegetables`**
3. How many **`fruits_vegetables`** do you have?
4. Modify the **`fruits_vegetables`** tuple and add the name of your favorite mushroom and beverage and assign it to **`food_tuple`**

### Exercises ➞ <span class='label label-default'>Level 2</span>

1. Unpack **`fruits_vegetables`** and mushroom and beverage from **`food_tuple`**
2. Change the about **`food_tuple`** tuple to a **`food_list`** list
3. Slice out the middle item or items from the **`food_tuple`** tuple or **`food_list`** list.
4. Slice out the first three items and the last three items from **`food_list`** list
5. Delete the **`food_tuple`** tuple completely
6. Check if an item exists in tuple:
    - Check if **`'Finland'`** is a asian country
    - Check if **`'India'`** is a asian country
    ```python
asian_countries = ('India','China','Singapore','Thailand','Indonesia')
    ```

---

## 📘 Python Dictionary Items()
*Source: `2. Python Datatypes/5. Python Dictionary items().ipynb`*

# Python Dictionary `items()`

The **`items()`** method returns a view object that displays a list of dictionary's (key, value) tuple pairs.

**Syntax**:

```python
dictionary.items() 
```

>**Note:** **`items()`** method is similar to dictionary's **`viewitems()`** method in Python 2.7.

## `items()` Parameters

The **`items()`** method doesn't take any parameters.

## Return Value from `items()`

The **`items()`** method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.

```python
# Example 1: Get all items of a dictionary with items()

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.items())
```

**Output:**
```text
dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
```

```python
# Example 2: How items() works when a dictionary is modified?

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

items = sales.items()
print('Original items:', items)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', items)
```

**Output:**
```text
Original items: dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
Updated items: dict_items([('orange', 3), ('grapes', 4)])
```

**Note:** The view object **`items`** doesn't itself return a list of sales items but it returns a view of **`sales`**'s (key, value) pair.

If the list is updated at any time, the changes are reflected on the view object itself, as shown in the above program.

---

## 📘 Python Dictionary
*Source: `2. Python Datatypes/5. Python Dictionary.ipynb`*

# Python Dictionary

In this class, you'll learn everything about Python dictionaries; how they are created, accessing, adding, removing elements from them and various built-in methods.

## What is Dictionary in Python?

Python dictionary is an unordered collection of items. Each item of a dictionary has a **`key/value`** pair. 

Dictionaries are optimized to retrieve values when the key is known.

<div>

</div>

**Example:**

```python
>>> dict = { }  #empty dictionary
>>> dict = {1:'Python',2:'Java',3:'C++'}
```

* **Dictionary is mutable** i.e., value can be updated.

* Key must be unique and immutable. Value is accessed by key. Value can be updated while key cannot be changed. 

* Dictionary is known as Associative array since the Key works as Index and they are decided by the user.

### Summary

| Data types     | Type          |         |
| :------------: | :-----------: |:------: |
| **String**     | **immutable** |  |
| **List**       | **mutable**   |✎|
| **Tuple**      | **immutable** |  |
| **Dictionary** | **mutable**   |✎|

## Creating Python Dictionary

Creating a dictionary is as simple as placing items inside curly braces **`{}`** separated by commas or the **dict()** built-in function.

An item has a **`key`** and a corresponding **`value`** that is expressed as a pair {**key: value**}.

The **`key`** and the **`value`** is separated by a colon **`:`**. Items are separated from each other by a comma **`,`**.

While the values can be of any data type and can repeat, keys must be of immutable type (**string**, **number** or **tuple** with immutable elements) and must be unique.

```python
# Example: empty dictionary

d = {}; l = []; t = (); s = set(); st = ""
print(d,l,t,s,st)     # ▶ {} [] () set() 
print(type(d),type(l),type(t), type(s), type(st)) 
# ▶ <class 'dict'> <class 'list'> <class 'tuple'> <class 'set'> <class 'str'>

# dictionary with integer keys
my_dict1 = {1: 'apple', 2: 'ball'}
print(my_dict1)        # ▶ {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict2 = {1:"hi", "name":666, 1.5:("yes","very much"), 9: [3, 6, 9]}
print(my_dict2)        # ▶ {1: 'hi', 'name': 666, 1.5: ('yes', 'very much'), 9: [3, 6, 9]}

# from sequence having each item as a pair
my_dict3 = dict([(1,'apple'), (2,'ball')])
print(type([(1,'apple'), (2,'ball')])) # nested list
print(my_dict3)        # ▶ {1: 'apple', 2: 'ball'}
print(len(my_dict3))   # ▶ 2
```

**Output:**
```text
{} [] () set() 
<class 'dict'> <class 'list'> <class 'tuple'> <class 'set'> <class 'str'>
{1: 'apple', 2: 'ball'}
{1: 'hi', 'name': 666, 1.5: ('yes', 'very much'), 9: [3, 6, 9]}
```

```python
dict([(1, 100), ('bar', 200)]), dict(foo=100, bar=200)
```

As you can see from above, we can also create a dictionary using the built-in **`dict()`** function.

## Accessing Elements from Dictionary

While indexing is used with other data types to access values, a dictionary uses **`keys`**. Keys can be used either inside square brackets **`[]`** or with the **`get()`** method.

If we use the square brackets **`[]`**, **`KeyError`** is raised in case a key is not found in the dictionary. On the other hand, the **`get()`** method returns **`None`** if the key is not found.

```python
# Example: get vs [] for retrieving elements

my_dict = {1:'Python', 2:'Java', 3:'C++', 'c': 'Gods language'}

# method: 1
print(my_dict[1])         # ▶ Python

# method: 2
print(my_dict.get('c'))   # ▶ Gods language

# Trying to access keys which doesn't exist in dictionary:
print(my_dict.get(4))     # ▶ None

print(my_dict[4])         # ▶ KeyError!
```

**Output:**
```text
Python
Gods language
None
```

* iterate all elemnet using for loop for **`keys()`** method, **`keys()`** method return list of all keys in dictionary.

```python
# Example:

dict = {1:'Python', 2:'Java', 3:'C++', 'c': 'Gods language'}
print(dict.keys())
for x in dict.keys():
    print(dict[x])
```

**Output:**
```text
dict_keys([1, 2, 3, 'c'])
Python
Java
C++
Gods language
```

## Changing and Adding Dictionary elements

Dictionaries are mutable. We can add new items or change the value of existing items using an assignment operator.

If the key is already present, then the existing value gets updated. In case the key is not present, a new **`(key: value)`** pair is added to the dictionary.

```python
# Example 1: Changing and adding Dictionary Elements

my_dict = {'name':'Arthur', 'age':24}

my_dict['age'] = 25   # update value
print(my_dict)        # ▶ {'age': 25, 'name': 'Arthur'}

my_dict['address'] = 'Downtown'  # add item
print(my_dict)        # ▶ {'name': 'Arthur', 'age': 25, 'address': 'Downtown'}
```

**Output:**
```text
{'name': 'Arthur', 'age': 25}
{'name': 'Arthur', 'age': 25, 'address': 'Downtown'}
```

```python
# Example 2: 

my_dict = {1:'Python', 2:'Java', 3:'C++'}
my_dict[3]="R"     # update value
my_dict[4]="PHP"   # insert new value
print(my_dict)     # ▶ {1: 'Python', 2: 'Java', 3: 'R', 4: 'PHP'}
```

**Output:**
```text
{1: 'Python', 2: 'Java', 3: 'R', 4: 'PHP'}
```

## Removing elements from Dictionary

We can remove a particular item in a dictionary by using the **`pop()`** method. This method removes an item with the provided **`key`** and returns the **`value`**.

The **`popitem()`** method can be used to remove and return an arbitrary **`(key, value)`** item pair from the dictionary. All the items can be removed at once, using the **`clear()`** method.

We can also use the **`del`** keyword to remove individual items or the entire dictionary itself.

```python
# Example: Removing elements from a dictionary


squares = {1:1, 2:4, 3:9, 4:16, 5:25}   # create a dictionary

# remove a particular item, returns its value
print(squares.pop(4))    # ▶ 16
print(squares)           # ▶ {1: 1, 2: 4, 3: 9, 5: 25}

# remove an arbitrary item, return (key,value)
print(squares.popitem()) # ▶ (5, 25)
print(squares)           # ▶ {1: 1, 2: 4, 3: 9}

squares.clear()          # remove all items
print(squares)           # ▶ {}

del squares              # delete the dictionary itself
print(squares)           # ▶ NameError!!!
```

**Output:**
```text
16
{1: 1, 2: 4, 3: 9, 5: 25}
(5, 25)
{1: 1, 2: 4, 3: 9}
{}
```

```python
# Example:

my_dict = {1:'Python', 2:'Java', 3:'C++', 4:'PHP'}
del my_dict[3]    # ▶ {1: 'Python', 2: 'Java', 4: 'PHP'} ∵ remove entry with key '3'
print(my_dict)    # ▶ {}

my_dict.clear()   # remove all entries in dict
print("my_dict : ",my_dict)  # ▶ my_dict :  {}

del my_dict       # delete entire dictionary
print(my_dict[2]) # ▶ NameError!!!
```

**Output:**
```text
{1: 'Python', 2: 'Java', 4: 'PHP'}
my_dict :  {}
```

## Dictionary Built-in Dictionary Functions

Built-in functions like **`all()`**, **`any()`**, **`len()`**, **`cmp()`**, **`sorted()`**, **`str()`**, **`typ()`**, etc. are commonly used with dictionaries to perform different tasks.

| Function | Description |
|:----| :--- |
| **all()** | Returns **`True`** if all keys of the dictionary are true (or if the dictionary is empty). | 
| **any()** | Returns **`True`** if any key of the dictionary is true. If the dictionary is empty, return **`False`**. | 
| **len()** | Returns the length (the number of items) in the dictionary. | 
| **cmp()** | Compares items of two dictionaries. (Not available in Python 3). | 
| **sorted()** | Returns a new sorted list of keys in the dictionary. | 
| **str()** | Produces a printable string representation of a dictionary. | 
| **type(** | Returns the type of the passed variable. If passed variable is dictionary,then it would return a dictionary type. |

Here are some examples that use built-in functions to work with a dictionary.

```python
# Example: Dictionary Built-in Functions

# all will give True if all "Key" is "True". 0 is also consider as False 

squares = {0:0, 1:1, 3:9, 5:25, 7:49, 9:81}

print(all(squares))     # ▶ False
print(any(squares))     # ▶ True
print(len(squares))     # ▶ 6
print(sorted(squares))  # ▶ [0, 1, 3, 5, 7, 9]
```

**Output:**
```text
False
True
6
[0, 1, 3, 5, 7, 9]
```

### `all(dict)` - The `all()` function returns True when all elements in the given iterable are true. If not, it returns False.

In case of dictionaries, if all keys (not values) are true or the dictionary is empty, **`all()`** returns **`True`**. Else, it returns **`false`** for all other cases.

```python
# Example 1: How all() works with Python dictionaries?
# In case of dictionaries, if all keys (not values) are true or the dictionary is empty, 
# all() returns True. Else, it returns false for all other cases.

my_dict = {0:'False', 1:'False'}
print(all(my_dict))   # ▶ False

my_dict = {1:'True', 2:'True'}
print(all(my_dict))   # ▶ True

my_dict = {1:'True', False:0}
print(all(my_dict))   # ▶ False

my_dict = {}
print(all(my_dict))   # ▶ True

# 0 is False
# '0' is True
my_dict = {'0':'True'}
print(all(my_dict))   # ▶ True
```

**Output:**
```text
False
True
False
True
True
```

### `any(dict)` - The `any()` function returns True if any element of an iterable is True. If not, any() returns False.

In the case of dictionaries, if all keys (not values) are false or the dictionary is empty, **`any()`** returns **`False`**. If at least one key is true, **`any()`** returns **`True`**.

```python
# Example 1: How any() works with Python dictionaries?

my_dict = {0:'False'}             
print(any(my_dict))                # ▶ False ∵ 0 is False

my_dict = {0:'False', 1:'True'}  
print(any(my_dict))                # ▶ True ∵ 1 is True

my_dict = {0:'False', False:0}   
print(any(my_dict))                # ▶ False ∵ both 0 and False are False

my_dict = {}                       
print(any(my_dict))                # ▶ False ∵ iterable is empty

# 0 is False
# '0' is True
my_dict = {'0':'False'}           
print(any(my_dict))                # ▶ True
```

**Output:**
```text
False
True
False
False
True
```

### **`len(dict)`** - The `len()` function gives the total length of the dictionary. This would be equal to the number of items in the dictionary.

```python
# Example:

my_dict = {1:'Python', 2:'Java', 3:'C++', 4:'PHP'}
print(len(my_dict))  # ▶ 4
```

**Output:**
```text
4
```

### **`sorted(dict)`** - The `sorted()` function sorts the elements of a given iterable in a specific order (either **ascending** or **descending**) and returns the sorted iterable as a list.

```python
# Example:

my_dict = {'e':1, 'a':2, 'u':3, 'o':4, 'i':5}
print(sorted(my_dict))               # ▶ ['a', 'e', 'i', 'o', 'u']
print(sorted(my_dict, reverse=True)) # ▶ ['u', 'o', 'i', 'e', 'a']
```

**Output:**
```text
['a', 'e', 'i', 'o', 'u']
['u', 'o', 'i', 'e', 'a']
```

### **`str(dict)`** - The `str()` function produces a printable string representation of a dictionary.

```python
# Example:

my_dict = {1:'Python', 2:'Java', 3:'C++', 4:'PHP'}
print(str(my_dict)) # ▶ {1: 'Python', 2: 'Java', 3: 'C++', 4: 'PHP'}
```

**Output:**
```text
{1: 'Python', 2: 'Java', 3: 'C++', 4: 'PHP'}
```

### **`type()`** - The `type()` function returns the type of the passed variable. If passed variable is dictionary then it would return a dictionary type.

```python
# Example:

my_dict = {1:'Python', 2:'Java', 3:'C++', 4:'PHP'}
print(type(my_dict))  # ▶ <class 'dict'>
```

## Python Dictionary Methods

Methods that are available with a dictionary are tabulated below. Some of them have already been used in the above examples.

| Method | Description |
|:----| :--- |
| **clear()** | Removes all items from the dictionary. | 
| **copy()** | Returns a shallow copy of the dictionary. | 
| **fromkeys(seq[, v])** | Returns a new dictionary with keys from **`seq`** and value equal to **`v`** (defaults to **`None`**). | 
| **get(key[,d])** | Returns the value of the **`key`**. If the **`key`** does not exist, returns **`d`** (defaults to **`None`**). | 
| **items()** | Return a new object of the dictionary's items in **`(key, value)`** format. | 
| **keys()** | Returns a new object of the dictionary's keys. | 
| **pop(key[,d])** | Removes the item with the **`key`** and returns its value or **`d`** if **`key`** is not found. If **`d`** is not provided and the **`key`** is not found, it raises **`KeyError`**. | 
| **popitem()** | Removes and returns an arbitrary item **`(key, value)`**. Raises **`KeyError`** if the dictionary is empty. | 
| **setdefault(key[,d])** | Returns the corresponding value if the **`key`** is in the dictionary. If not, inserts the **`key`** with a value of **`d`** and returns **`d`** (defaults to **`None`**). | 
| **update([other])** | Updates the dictionary with the key/value pairs from **`other`**, overwriting existing keys. |  
| **values()** | Returns a new object of the dictionary's values. |

Here are a few example use cases of these methods.

```python
# Example: Dictionary Methods

marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)                        # ▶ {'English': 0, 'Math': 0, 'Science': 0}

for item in marks.items():
    print(item)

print(list(sorted(marks.keys())))   # ▶ ['English', 'Math', 'Science']
```

**Output:**
```text
{'Math': 0, 'English': 0, 'Science': 0}
('Math', 0)
('English', 0)
('Science', 0)
['English', 'Math', 'Science']
```

### **`clear()`** - The method `clear()` removes all items from the dictionary.

```python
# Example:

my_dict = {1:'Python', 2:'Java', 3:'C++', 4:'PHP'}

print(str(my_dict))  # ▶ {1: 'Python', 2: 'Java', 3: 'C++', 4: 'PHP'}
dict.clear()
print(str(my_dict))  # ▶ {}
```

**Output:**
```text
{1: 'Python', 2: 'Java', 3: 'C++', 4: 'PHP'}
{1: 'Python', 2: 'Java', 3: 'C++', 4: 'PHP'}
```

### **`copy()`** - The method `copy()` returns a shallow copy of the dictionary.

```python
# Example:

dict1 = {1:'Python', 2:'Java', 3:'C++', 4:'PHP'}
dict2 = dict1.copy()
print(dict2)  # ▶ {1: 'Python', 2: 'Java', 3: 'C++', 4: 'PHP'}
```

**Output:**
```text
{1: 'Python', 2: 'Java', 3: 'C++', 4: 'PHP'}
```

### **`itmes()`** - The method `items()` returns a list of dict's (key, value) tuple pairs.

```python
# Example:

my_dict = {1:'Python', 2:'Java', 3:'C++', 4:'PHP'}
print(my_dict.items()) # ▶ dict_items([(1, 'Python'), (2, 'Java'), (3, 'C++'), (4, 'PHP')])
```

**Output:**
```text
dict_items([(1, 'Python'), (2, 'Java'), (3, 'C++'), (4, 'PHP')])
```

### **`keys()`** - The method `keys()` returns a list of all the available keys in the dictionary.

```python
# Example:

my_dict = {1:'Python', 2:'Java', 3:'C++', 4:'PHP'}
all_keys=my_dict.keys()
print(all_keys)  # ▶ dict_keys([1, 2, 3, 4])
```

**Output:**
```text
dict_keys([1, 2, 3, 4])
```

### **`fromkeys()`** - The method `fromkeys()` creates a new dictionary with keys from seq and values set to value.

**Syntax:**

```python 
dict.fromkeys(seq[, value])
```

```python
# Example:

seq = ('Python', 'Java', 'C++')
my_dict = my_dict.fromkeys(seq)

print ("new_dict : %s" % str(my_dict)) # ▶ new_dict : {'python': None, 'java': None, 'c++': None}
my_dict = my_dict.fromkeys(seq, 50)
print ("new_dict : %s" % str(my_dict)) # ▶ new_dict : {'python': 50, 'java': 50, 'c++': 50}
```

**Output:**
```text
new_dict : {'Python': None, 'Java': None, 'C++': None}
new_dict : {'Python': 50, 'Java': 50, 'C++': 50}
```

### **`setdefault()`** - The method `setdefault()` is similar to `get` but will set `dict[key] = default` if key is not already in dict.

**Syntax:**

```python
dict.setdefault(key, default = None)
```

* key −> This is the key to be searched. 
* default −> This is the Value to be returned in case key is not found.

```python
# Example:

my_dict={'emp_name':'Milaan', 'age':96, 'emp_id':999}
my_dict.setdefault('company','JLUFE')
print(my_dict['emp_name'])   # ▶ Milaan
print(my_dict['company'])    # ▶ JLUFE
```

**Output:**
```text
Milaan
JLUFE
```

### **`update()`** - The method `update()` adds dictionary dict2's key-values pairs in to dict. This function does not return anything.

**Syntax:**

```python
dict.update(dict2)
```

```python
# Example:

dict1 = {1:'Python', 2:'Java', 3:'C++', 4:'PHP'}
dict2 = {1: 'Python3',5:'C'}  # update Python to Python3
dict1.update(dict2)
print(dict1)   # ▶ {1: 'Python3', 2: 'Java', 3: 'C++', 4: 'PHP', 5: 'C'}
```

**Output:**
```text
{1: 'Python3', 2: 'Java', 3: 'C++', 4: 'PHP', 5: 'C'}
```

### **`value()`** - The method `values()` returns a list of all the values available in a given dictionary.

```python
# Example:

dict1 = {1:'Python', 2:'Java', 3:'C++', 4:'PHP'}
values= dict1.values()
print(values)  # ▶ dict_values(['Python', 'Java', 'C++', 'PHP'])
```

**Output:**
```text
dict_values(['Python', 'Java', 'C++', 'PHP'])
```

## Python Dictionary Comprehension

Dictionary comprehension is an elegant and concise way to create a new dictionary from an iterable in Python.

Dictionary comprehension consists of an expression pair **`(key: value)`** followed by a **`for`** statement inside curly braces **`{}`**.

Here is an example to make a dictionary with each item being a pair of a number and its square.

```python
# Example: Dictionary Comprehension

squares = {x: x*x for x in range(6)}
print(squares)  # ▶ {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**Output:**
```text
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

This code is equivalent to

```python
# Example:

squares = {}
for x in range(6):
    squares[x] = x*x
print(squares)  # ▶ {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**Output:**
```text
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

A dictionary comprehension can optionally contain more **for** or **if** statements.

An optional **`if`** statement can filter out items to form the new dictionary.

Here are some examples to make a dictionary with only odd items.

```python
# Example: Dictionary Comprehension with if conditional

odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares)  # ▶ {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
```

**Output:**
```text
{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
```

## Other Dictionary Operations

### 1. Dictionary Membership Test

We can test if a **`key`** is in a dictionary or not using the keyword **`in`**. Notice that the membership test is only for the **`keys`** and not for the **`values`**.

```python
# Example: Membership Test for Dictionary Keys

squares = {1: 1, 3: 9, 5: 25, 7: 99, 9: 61}

print(1 in squares)      # ▶ True

print(2 not in squares)  # ▶ True

# membership tests for key only not value
print(99 in squares)     # ▶ False
```

**Output:**
```text
True
True
False
```

### 2. Iterating Through a Dictionary

We can iterate through each key in a dictionary using a **`for`** loop.

```python
# Example: Iterating through a Dictionary

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
```

**Output:**
```text
1
9
25
49
81
```

## 💻 Exercises ➞ <span class='label label-default'>Dictionary</span>

1. Create an empty dictionary called **`bird`**
2. Add **`name`**, **`color`**, **`breed`**, **`legs`**, **`age`** to the **`bird`** dictionary
3. Create a **`student`** dictionary and add **`first_name`**, **`last_name`**, **`gender`**, **`age`**, **`marital_status`**, **`skills`**, **`country`**, **`city`** and **`address`** as keys for the dictionary
3. Get the length of the **`student`** dictionary
4. Get the value of **`skills`** and check the data type, it should be a list
5. Modify the **`skills`** values by adding one or two skills
6. Get the dictionary keys as a list
7. Get the dictionary values as a list
8. Change the dictionary to a list of tuples using **`items()`** method
9. Delete one of the items in the dictionary
10. Delete one of the dictionaries

---

## 📘 Python List Remove()
*Source: `2. Python Datatypes/5. Python List remove().ipynb`*

# Python List `remove()`

The list **`remove()`** method removes the first matching element (which is passed as an argument) from the list.

**Syntax**:

```python
list.remove(element)
```

## `remove()` Parameters

* The **`remove()`** method takes a single element as an argument and removes it from the list.
* If the **`element`** doesn't exist, it throws **ValueError: list.remove(x): x not in list exception**.

## Return Value from `remove()`

The **`remove()`** doesn't return any value (returns **`None`**).

```python
# Example 1: Remove element from the list

# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')

# Updated animals List
print('Updated animals list: ', animals)
```

**Output:**
```text
Updated animals list:  ['cat', 'dog', 'guinea pig']
```

```python
# Example 2: remove() method on a list having duplicate elements

# If a list contains duplicate elements, the remove() method only removes 
# the first matching element.

# animals list
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' is removed
animals.remove('dog')

# Updated animals list
print('Updated animals list: ', animals)
```

**Output:**
```text
Updated animals list:  ['cat', 'dog', 'guinea pig', 'dog']
```

Here, only the first occurrence of element **`'dog'`** is removed from the list.

```python
# Example 3: Deleting element that doesn't exist

# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# Deleting 'fish' element
animals.remove('fish')

# Updated animals List
print('Updated animals list: ', animals)
```

Here, we are getting an error because the **`animals`** list doesn't contain **`'fish'`**.

* If you need to delete elements based on the index (like the fourth element), you can use the **list pop() method**.


* Also, you can use the **Python del statement** to remove items from the list.

---

## 📘 Python Set Difference()
*Source: `2. Python Datatypes/5. Python Set difference().ipynb`*

# Python Set `difference()`

The **`difference()`** method returns the set difference of two sets.

If **`A`** and **`B`** are two sets. The set difference of **`A`** and **`B`** is a set of elements that exists only in set **`A`** but not in **`B`**.

```python
If A = {1, 2, 3, 4}
B = {2, 3, 9}

Then,
A - B = {1, 4}
B - A = {9}
```

<div>

</div>

**Syntax**:

```python
A.difference(B)
```

Here, **`A`** and **`B`** are two sets. The following syntax is equivalent to **`A-B`**.

## Return Value from `difference()`

The **`difference()`** method returns the difference between two sets which is also a set. It doesn't modify original sets.

```python
# Example 1: How difference() works in Python?

A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

# Equivalent to A-B
print(A.difference(B))

# Equivalent to B-A
print(B.difference(A))
```

**Output:**
```text
{'b', 'a', 'd'}
{'f', 'g'}
```

You can also find the set difference using **`-`** operator in Python.

```python
# Example 2: Set Difference Using - Operator.

A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

print(A-B)

print(B-A)
```

**Output:**
```text
{'b', 'a', 'd'}
{'f', 'g'}
```

---

## 📘 Python String Endswith()
*Source: `2. Python Datatypes/5. Python String endswith().ipynb`*

# Python String `endswith()`

The **`endswith()`** method returns True if a string ends with the specified suffix. If not, it returns False.

**Syntax**:

```python
str.endswith(suffix[, start[, end]])
```

## `endswith()` Parameters

The **`endswith()`** method takes three parameters:

* **suffix** - String or tuple of suffixes to be checked.
* **start (Optional)** - Beginning position where **suffix** is to be checked within the string.
* **end (Optional)** - Ending position where **suffix** is to be checked within the string.

## Return Value from `endswith()`

The **`endswith()`** method returns a boolean.

* It returns **True** if strings ends with the specified suffix.
* It returns **False** if string doesn't end with the specified suffix.

```python
# Example 1: endswith() Without start and end Parameters

text = "Python is easy to learn."

result = text.endswith('to learn')
# returns False
print(result)

result = text.endswith('to learn.')
# returns True
print(result)

result = text.endswith('Python is easy to learn.')
# returns True
print(result)
```

**Output:**
```text
False
True
True
```

```python
# Example 2: endswith() With start and end Parameters

text = "Python programming is easy to learn."

# start parameter: 7
# "programming is easy to learn." string is searched
result = text.endswith('learn.', 7)
print(result)

# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched

result = text.endswith('is', 7, 26)
# Returns False
print(result)

result = text.endswith('easy', 7, 26)
# returns True
print(result)
```

**Output:**
```text
True
False
True
```

## Passing Tuple to `endswith()`

It's possible to pass a tuple suffixes to the **`endswith()`** method in Python.

If the string ends with any item of the tuple, **`endswith()`** returns **`True`**. If not, it returns **`False`**.

```python
# Example 3: endswith() With Tuple Suffix

text = "programming is easy"
result = text.endswith(('programming', 'python'))

# prints False
print(result)

result = text.endswith(('python', 'easy', 'java'))

#prints True
print(result)

# With start and end parameter
# 'programming is' string is checked
result = text.endswith(('is', 'an'), 0, 14)

# prints True
print(result)
```

**Output:**
```text
False
True
True
```

If you need to check if a string starts with the specified prefix, you can use **startswith() method in Python**.

---

## 📘 Python Dictionary Keys()
*Source: `2. Python Datatypes/6. Python Dictionary keys().ipynb`*

# Python Dictionary `keys()`

The **`keys()`** method returns a view object that displays a list of all the keys in the dictionary

**Syntax**:

```python
dictionary.keys() 
```

## `keys()` Parameters

The **`keys()`** method doesn't take any parameters.

## Return Value from `keys()`

The **`keys()`** method returns a view object that displays a list of all the keys.

When the dictionary is changed, the view object also reflects these changes.

```python
# Example 1: How keys() works?

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.keys())

empty_dict = {}
print(empty_dict.keys())
```

**Output:**
```text
dict_keys(['name', 'age', 'salary'])
dict_keys([])
```

```python
# Example 2: How keys() works when dictionary is updated?

person = {'name': 'Phill', 'age': 22, }

print('Before dictionary is updated')
keys = person.keys()
print(keys)

# adding an element to the dictionary
person.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
print(keys)
```

**Output:**
```text
Before dictionary is updated
dict_keys(['name', 'age'])

After dictionary is updated
dict_keys(['name', 'age', 'salary'])
```

**Note:** Here, when the dictionary is updated, **`keys`** is also automatically updated to reflect changes.

---

## 📘 Python List Count()
*Source: `2. Python Datatypes/6. Python List count().ipynb`*

# Python List `count()`

The **`count()`** method returns the number of times the specified element appears in the list.

**Syntax**:

```python
list.count(element)
```

## `count()` Parameters

The list **`count()`** method takes a single argument:

* **element** - the element to be counted

## Return Value from `count()`

The **`count()`** method returns the number of times **`element`** appears in the list.

```python
# Example 1: Use of List count()

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)
```

**Output:**
```text
The count of i is: 2
The count of p is: 0
```

```python
# Example 2: Count Tuple and List Elements Inside List

# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("The count of [3, 4] is:", count)
```

**Output:**
```text
The count of ('a', 'b') is: 2
The count of [3, 4] is: 1
```

---

## 📘 Python Set Difference Update()
*Source: `2. Python Datatypes/6. Python Set difference update().ipynb`*

# Python Set `difference_update()`

The **`difference_update()`** updates the set calling difference_update() method with the difference of sets.

If **`A`** and **`B`** are two sets. The set difference of **`A`** and **`B`** is a set of elements that exists only in set **`A`** but not in **`B`**.

To learn more, visit **Python set difference()**.

**Syntax**:

```python
A.difference_update(B)
```

Here, **`A`** and **`B`** are two sets. **`difference_update()`** updates set **`A`** with the set difference of **`A-B`**.

## Return Value from `difference_update()`

The **`difference_update()`** returns **`None`** indicating the object (set) is mutated.

Suppose,
```python
result = A.difference_update(B)
```

When you run the code,

* **`result`** will be **`None`**
* **`A`** will be equal to **`A-B`**
* **`B`** will be unchanged

```python
# Example: How difference_update() works?

A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)
```

**Output:**
```text
A =  {'a', 'd'}
B =  {'c', 'g', 'f'}
result =  None
```

---

## 📘 Python Sets
*Source: `2. Python Datatypes/6. Python Sets.ipynb`*

# Python Sets

In this class, you'll learn everything about Python sets; how they are created, adding or removing elements from them, and all operations performed on sets in Python.

## What is Set in Python?

A set is an **unordered collection of items**. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

However, a **set itself is mutable. We can add or remove items from it**.

Sets can also be used to perform mathematical set operations like **union**, **intersection**, **symmetric difference**, etc.

### Summary

| Data types     | Type          |         |
| :------------: | :-----------: |:------: |
| **String**     | **immutable** |  |
| **List**       | **mutable**   |✎|
| **Tuple**      | **immutable** |  |
| **Dictionary** | **mutable**   |✎|
| **Set**        | **immutable** |  |

## How Are Sets Better Than Other DataTypes?

Sets **will not contain multiple occurrences of the same element**, they are very useful in removing duplicate elements from a list or a tuple. Also, they are useful in computing mathematical notations such as union, intersection, etc.

## Creating Python Sets

A set is created by placing all the items (elements) inside curly braces **`{}`**, separated by comma, or by using the built-in **`set()`** function.

It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have mutable elements like **lists**, sets or **dictionaries** as its elements.

```python
# Example 1: Different types of sets in Python

# set of integers
my_set = {5, 7, 1, 2, 3}            
print(my_set)           # ▶ {1, 2, 3, 5, 7}
 
# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}  
print(my_set)           # ▶ {1.0, 'Hello', (1, 2, 3)}
```

**Output:**
```text
{1, 2, 3, 5, 7}
{1.0, (1, 2, 3), 'Hello'}
```

```python
# Example 2: Different types of sets in Python

# set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)             # ▶ {1, 2, 3, 4}

# we can make set from a list
my_set = set([1, 2, 3, 2])
print(my_set)             # ▶ {1, 2, 3}

# set can have immutable items
# here (3, 4) is a immutable list

my_set = {1, 2, (3, 4)}   
print(my_set)            # ▶ {1, 2, (3, 4)} ∵ tuple is immutable

# set cannot have mutable items
# here [3, 4] is a mutable list

my_set = {1, 2, [3, 4]}  # this will cause an error ∵ list is mutable
```

**Output:**
```text
{1, 2, 3, 4}
{1, 2, 3}
{1, 2, (3, 4)}
```

#### Creating an empty set is a bit tricky.

Empty curly braces **`{}`** will make an empty dictionary in Python. To make a set without any elements, we use the **`set()`** function without any argument.

```python
# Example: Distinguish set and dictionary while creating empty set

# initialize a with {}
a = {}

# check data type of a
print(type(a))  # ▶ <class 'dict'> ∵ dict also use {}

# initialize a with set()
a = set()

# check data type of a
print(type(a)) # ▶ <class 'set'>
```

## Modifying a set in Python

Sets are mutable. However, since they are unordered, indexing has no meaning.

We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.

We can add a single element using the **`add()`** method, and multiple elements using the **`update()`** method. The **`update()`** method can take **tuples**, lists, **strings** or other sets as its argument. In all cases, duplicates are avoided.

```python
# Example: 

# initialize my_set
my_set = {1, 3}
print(my_set)      # ▶ {1, 3}

# my_set[0]
# if you uncomment above line, you will get an error
# TypeError: 'set' object does not support indexing

# add an element
my_set.add(2)
print(my_set)     # ▶ {1, 2, 3}

# add multiple elements
my_set.update([2, 3, 4])
print(my_set)     # ▶ {1, 2, 3, 4}

# add list and set
my_set.update([1,7],(8,9,10),{1,5,9,10})
print(my_set)     # ▶ {1, 2, 3, 4, 5, 7, 8, 9, 10}
```

**Output:**
```text
{1, 3}
{1, 2, 3}
{1, 2, 3, 4}
{1, 2, 3, 4, 5, 7, 8, 9, 10}
```

## Removing elements from a set

A particular item can be removed from a set using the methods **`discard()`** and **`remove()`**.

The only difference between the two is that the **`discard()`** function leaves a set unchanged if the element is not present in the set. On the other hand, the **`remove()`** function will raise an error in such a condition (if element is not present in the set).

The following example will illustrate this.

```python
# Example: Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)     # ▶ {1, 3, 4, 5, 6}

# discard an element
my_set.discard(4)
print(my_set)     # ▶ {1, 3, 5, 6}

# remove an element
my_set.remove(6)
print(my_set)     # ▶ {1, 3, 5}

# discard an element not present in my_set
my_set.discard(2)
print(my_set)     # ▶ {1, 3, 5} NO ERROR!

# remove an element not present in my_set you will get an error.
my_set.remove(2)  # ▶ KeyError!!!
```

**Output:**
```text
{1, 3, 4, 5, 6}
{1, 3, 5, 6}
{1, 3, 5}
{1, 3, 5}
```

Similarly, we can remove and return an item using the **`pop()`** method.

Since set is an unordered data type, there is no way of determining which item will be popped. It is completely arbitrary.

We can also remove all the items from a set using the **`clear()`** method.

```python
# Example:

# initialize my_set
my_set = set("HelloWorld")
print(my_set)        # ▶ unorderd set of unique elements

# pop an element
print(my_set.pop())  # ▶ removes a random element

# pop another element
my_set.pop()
print(my_set)

# clear my_set
my_set.clear()
print(my_set)        # ▶ set()
```

**Output:**
```text
{'W', 'H', 'r', 'd', 'e', 'o', 'l'}
W
{'r', 'd', 'e', 'o', 'l'}
set()
```

## Python Set Operations

Sets can be used to carry out mathematical set operations like union, intersection, difference and symmetric difference. We can do this with operators or methods.

Let us consider the following two sets for the following operations.

```python
>>> A = {1, 2, 3, 4, 5}
>>> B = {4, 5, 6, 7, 8}
```

### Set Union

<div>

</div>

Union of **`A`** and **`B`** is a set of all elements from both sets.

Union is performed using **`|`** operator. Same can be accomplished using the **`union()`** method.

```python
# Example 1:

# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
print(A | B)      # ▶ {1, 2, 3, 4, 5, 6, 7, 8}
```

**Output:**
```text
{1, 2, 3, 4, 5, 6, 7, 8}
```

```python
# Example 2:

# use union function
A.union(B)
{1, 2, 3, 4, 5, 6, 7, 8}

# use union function on B
B.union(A)
{1, 2, 3, 4, 5, 6, 7, 8}
```

**Output:**
```text
{1, 2, 3, 4, 5, 6, 7, 8}
```

### Set Intersection

<div>

</div>

Intersection of **`A`** and **`B`** is a set of elements that are common in both the sets.

Intersection is performed using **`&`** operator. Same can be accomplished using the **`intersection()`** method.

```python
# Example 1:

# Intersection of sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
print(A & B)     # ▶ {4, 5}
```

**Output:**
```text
{4, 5}
```

```python
# Example 2:

# use intersection function on A
A.intersection(B) # ▶ {4, 5}

# use intersection function on B
B.intersection(A) # ▶ {4, 5}
```

**Output:**
```text
{4, 5}
```

### Set Difference

<div>

</div>

Difference of the set **`B`** from set **`A`**, **`(A - B)`** is a set of elements that are only in A but not in **`B`**. Similarly, **`B - A`** is a set of elements in **`B`** but not in **`A`**.

Difference is performed using **`-`** operator. Same can be accomplished using the **`difference()`** method.

```python
# Example 1:

# Difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
print(A - B)    # ▶ {1, 2, 3}
print(B - A)    # ▶ {8, 6, 7}
```

**Output:**
```text
{1, 2, 3}
{8, 6, 7}
```

```python
# Example 2:

# use difference function on A
A.difference(B) # ▶ {1, 2, 3}

# use difference function on B
B.difference(A) # ▶ {6, 7, 8}
```

**Output:**
```text
{6, 7, 8}
```

### Set Symmetric Difference

<div>

</div>

Symmetric Difference of **`A`** and **`B`** is a set of elements in **`A`** and **`B`** but not in both (excluding the intersection).

Symmetric difference is performed using **`^`** operator. Same can be accomplished using the method **`symmetric_difference()`**.

```python
# Example 1:

# Symmetric difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
print(A ^ B)    # ▶ {1, 2, 3, 6, 7, 8}
```

**Output:**
```text
{1, 2, 3, 6, 7, 8}
```

```python
# Example 2:

# use symmetric_difference function on A
A.symmetric_difference(B)  # ▶ {1, 2, 3, 6, 7, 8}

# use symmetric_difference function on B
B.symmetric_difference(A)  # ▶ {1, 2, 3, 6, 7, 8}
```

**Output:**
```text
{1, 2, 3, 6, 7, 8}
```

## Built-in Functions with Set

Built-in functions like **`all()`**, **`any()`**, **`enumerate()`**, **`len()`**, **`max()`**, **`min()`**, **`sorted()`**, **`sum()`**, etc. are commonly used with sets to perform different tasks.

| Function | Description | 
|:---- |:---- |
| ****all()**** | Returns **`True`** if all elements of the set are true (or if the set is empty). |
| **any()** | Returns **`True`** if any element of the set is true. If the set is empty, returns **`False`**. |
| **enumerate()** | Returns an enumerate object. It contains the index and value for all the items of the set as a pair. |
| **len()** | Returns the length (the number of items) in the set. |
| **max()** | Returns the largest item in the set. |
| **min()** | Returns the smallest item in the set. |
| **sorted()** | Returns a new sorted list from elements in the set(does not sort the set itself). |
| **sum()** | Returns the sum of all elements in the set. |

## Other Python Set Methods

There are many set methods, some of which we have already used above. Here is a list of all the methods that are available with the set objects:

| Method | Operator | Description |
|:---- |:---- |:--- |
| **add()** |  |  Adds an element to the set. | 
| **copy()** |  |  Returns a copy of the set. | 
| **remove()** |  |  Removes an element from the set. If the element is not a member, raises a **`KeyError`**. |
| **discard()** |  |  Removes an element from the set if it is a member. (Do nothing if the element is not in set). | 
| **pop()** |  |  Removes and returns an arbitrary set element. Raises **`KeyError`** if the set is empty. | 
| **clear()** |  |  Removes all elements from the set. | 
| **union()** | **`A \| B`** |  Returns the union of sets in a new set. | 
| **update()** | **`A \|= B`** |  Updates the set with the union of itself and others. | 
| **intersection()** | **`A & B`** |  Returns the intersection of two sets as a new set. | 
| **intersection_update()** | **`A &= B`** |  Updates the set with the intersection of itself and another. | 
| **isdisjoint()** |  |  Returns **`True`** if two sets have a null intersection. | 
| **difference()** | **`A – B`** |  Returns the difference of two or more sets as a new set. | 
| **difference_update()** | **`A -= B`** |  Removes all elements of another set from this set. | 
| **symmetric_difference()** | **`A ^ B`** |  Returns the symmetric difference of two sets as a new set. | 
| **symmetric_difference_update()** | **`A ^= B`** |  Updates a set with the symmetric difference of itself and another. | 
| **issubset()** | **`A <= B`** |  Returns **`True`** if another set contains this set. | 
| **issuperset()** | **`A >= B`** | Returns **`True`** if this set contains another set. |

## Other Set Operations

### 1. Set Membership Test

We can test if an item exists in a set or not, using the **`in`** keyword.

```python
# Example:

# in keyword in a set
# initialize my_set
my_set = set("apple")

# check if 'a' is present
print('a' in my_set)      # ▶ True

# check if 'p' is present
print('p' not in my_set)  # ▶ False
```

**Output:**
```text
True
False
```

### 2. Iterating Through a Set

We can iterate through each item in a set using a **`for`** loop.

```python
for letter in set("apple"):
    print(letter)  # ▶ ∵ unorderd set of unique elements
```

**Output:**
```text
p
a
e
l
```

## Python Frozenset

Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.

Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.

Frozensets can be created using the **frozenset()** function.

The **`frozenset()`** function returns an immutable frozenset object initialized with elements from the given iterable.

This data type supports methods like **`copy()`**, **`difference()`**, **`intersection()`**, **`isdisjoint()`**, **`issubset()`**, **`issuperset()`**, **`symmetric_difference()`** and **`union()`**. Being immutable, it does not have methods that add or remove elements.

**Syntax:**

```python
frozenset([iterable])
```

```python
# Example:

# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
```

```python
A.isdisjoint(B) # ▶ False ∵ they have common intersection points
```

**Output:**
```text
False
```

```python
A.difference(B) # ▶ frozenset({1, 2})
```

**Output:**
```text
frozenset({1, 2})
```

```python
A | B           # ▶ frozenset({1, 2, 3, 4, 5, 6})
```

**Output:**
```text
frozenset({1, 2, 3, 4, 5, 6})
```

```python
A.add(3)        # ▶ Error!
```

### Frozenset methods

This data type supports methods like **`copy()`**, **`union()`**, **`intersection()`**, **`difference()`**, and **`symmetric_difference()`**. Being immutable, it does not have methods that add or remove elements.

```python
# Example 1: Frozensets

# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()                     # ▶ frozenset({1, 2, 3, 4})
print(C)

# union
print(A.union(B))                # ▶ frozenset({1, 2, 3, 4, 5, 6})

# intersection
print(A.intersection(B))         # ▶ frozenset({3, 4})

# difference
print(A.difference(B))           # ▶ frozenset({1, 2})

# symmetric_difference
print(A.symmetric_difference(B)) # ▶ frozenset({1, 2, 5, 6})
```

**Output:**
```text
frozenset({1, 2, 3, 4})
frozenset({1, 2, 3, 4, 5, 6})
frozenset({3, 4})
frozenset({1, 2})
frozenset({1, 2, 5, 6})
```

### Other Frozenset methods 

Similarly, other set methods like **`isdisjoint()`**, **`issubset()`**, and **`issuperset()`** are also available.

```python
# Example 2: Frozensets

# initialize A, B and C
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

# isdisjoint() method
print(A.isdisjoint(C))  # ▶ True

# issubset() method
print(C.issubset(B))    # ▶ True

# issuperset() method
print(B.issuperset(C))  # ▶ True
```

**Output:**
```text
True
True
True
```

## 💻 Exercises ➞ <span class='label label-default'>Sets</span>

```py
mix_fruits = {'Guava', 'Pear', 'Mango', 'Apple', 'Fig', 'Orange', 'Banana'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
num = [22, 19, 24, 25, 26, 24, 25, 24]
```

### Exercises ➞ <span class='label label-default'>Level 1</span>

1. Find the length of the set **`mix_fruits`**
2. Add **`'Kiwi'`** to **`mix_fruits`**
3. Insert multiple fruits at once to the set **`mix_fruits`**
4. Remove one of the fruit from the set **`mix_fruits`**
5. What is the difference between **remove** and **discard**


### Exercises ➞ <span class='label label-default'>Level 2</span>
Use Imaginary values for Set **`A`** and **`B`**

1. Join **`A`** and **`B`**
2. Find **`A`** intersection **`B`**
3. Is **`A`** subset of **`B`**
4. Are **`A`** and **`B`** disjoint sets
5. Join **`A`** with **`B`** and **`B`** with **`A`**
6. What is the symmetric difference between A and **`B`**
7. Delete the sets completely


### Exercises ➞ <span class='label label-default'>Level 3</span>

1. Convert the **`num`** to a set and compare the length of the list and the set, which one is bigger?
2. Explain the difference between the following data types: **string**, **list**, **tuple** and **set**
3. **`I am a researcher cum teacher and I love to inspire and teach people.`**. How many unique words have been used in the sentence? Use the **`split()`** methods and set to get the unique words.

---

## 📘 Python String Expandtabs()
*Source: `2. Python Datatypes/6. Python String expandtabs().ipynb`*

# Python String `expandtabs()`

The **`expandtabs()`** method returns a copy of string with all tab characters **`'\t'`** replaced with whitespace characters until the next multiple of tabsize parameter.

**Syntax**:

```python
string.expandtabs(tabsize)
```

## `expandtabs()` Parameters

The **`expandtabs()`** method takes an integer **`tabsize`** argument. The default **`tabsize`** is **8**.

## Return Value from `expandtabs()`

The **`expandtabs()`** method returns a string where all **`'\t'`** characters are replaced with whitespace characters until the next multiple of **`tabsize`** parameter.

```python
# Example 1: expandtabs() With no Argument

str = 'xyz\t12345\tabc'

# no argument is passed
# default tabsize is 8
result = str.expandtabs()

print(result)
```

**Output:**
```text
xyz     12345   abc
```

## How `expandtabs()` works in Python?

The **`expandtabs()`** method keeps track of the current cursor position.

The position of first **`'\t'`** character in the above program is **3**. And, the **`tabsize`** is **8** (if argument is not passed).

The **`expandtabs()`** character replaces the **`'\t'`** with whitespace until the next tab stop. The position of **`'\t'`** is **3** and the first tab stop is **8**. Hence, the number of spaces after **'xyz'** is **5**.

The next tab stops are the multiples of **`tabsize`**. The next tab stops are **16**, **24**, **32** and so on.

Now, the position of second **`'\t'`** character is **13**. And, the next tab stop is **16**. Hence, there are 3 spaces after **12345**.

```python
# Example 2: expandtabs() With Different Argument

str = "xyz\t12345\tabc"
print('Original String:', str)

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))

# tabsize is set to 3
print('Tabsize 3:', str.expandtabs(3))

# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))

# tabsize is set to 5
print('Tabsize 5:', str.expandtabs(5))

# tabsize is set to 6
print('Tabsize 6:', str.expandtabs(6))
```

**Output:**
```text
Original String: xyz	12345	abc
Tabsize 2: xyz 12345 abc
Tabsize 3: xyz   12345 abc
Tabsize 4: xyz 12345   abc
Tabsize 5: xyz  12345     abc
Tabsize 6: xyz   12345 abc
```

**Explanation:** 

* The default **`tabsize`** is **8**. The tab stops are **8**, **16** and so on. Hence, there is **5** spaces after **'xyz'** and **3** after **'12345'** when you print the original string.


* When you set the **`tabsize`** to **2**. The tab stops are **2**, **4**, **6**, **8** and so on. For **'xyz'**, the tab stop is **4**, and for **'12345'**, the tab stop is **10**. Hence, there is **1** space after **'xyz'** and **1** space after **'12345'**.


* When you set the **`tabsize`** to **3**. The tab stops are **3**, **6**, **9** and so on. For **'xyz'**, the tab stop is **6**, and for **'12345'**, the tab stop is **12**. Hence, there are **3** spaces after **'xyz'** and **1** space after **'12345'**.


* When you set the **`tabsize`** to **4**. The tab stops are **4**, **8**, **12** and so on. For **'xyz'**, the tab stop is **4** and for **'12345'**, the tab stop is **12**. Hence, there is **1** space after **'xyz'** and **3** spaces after **'12345'**.


* When you set the **`tabsize`** to **5v. The tab stops are **5**, **10**, **15** and so on. For **'xyz'**, the tab stop is **5** and for **'12345'**, the tab stop is **15**. Hence, there are **2** spaces after **'xyz'** and **5** spaces after **'12345'**.


* When you set the **`tabsize`** to **6**. The tab stops are **6**, **12**, **18** and so on. For **'xyz'**, the tab stop is **6** and for **'12345'**, the tab stop is **12**. Hence, there are **3** spaces after **'xyz'** and **1** space after **'12345'**.

---

## 📘 Python Dictionary Pop()
*Source: `2. Python Datatypes/7. Python Dictionary pop().ipynb`*

# Python Dictionary `pop()`

The **`pop()`** method removes and returns an element from a dictionary having the given key.

**Syntax**:

```python
dictionary.pop(key[, default])
```

## `pop()` Parameters

The **`pop()`** method takes two parameters:

* **key** - key which is to be searched for removal
* **default** - value which is to be returned when the key is not in the dictionary

## Return Value from `pop()`

The **`pop()`** method returns:

* If **`key`** is found - removed/popped element from the dictionary
* If **`key`** is not found - value specified as the second argument (default)
* If **`key`** is not found and default argument is not specified - **`KeyError`** exception is raised

```python
# Example 1: Pop an element from the dictionary

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)
```

**Output:**
```text
The popped element is: 2
The dictionary is: {'orange': 3, 'grapes': 4}
```

```python
# Example 2: Pop an element not present from the dictionary

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('guava')
```

```python
# Example 3: Pop an element not present from the dictionary, provided a default value

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('guava', 'banana')
print('The popped element is:', element)
print('The dictionary is:', sales)
```

**Output:**
```text
The popped element is: banana
The dictionary is: {'apple': 2, 'orange': 3, 'grapes': 4}
```

---

## 📘 Python List Comprehension
*Source: `2. Python Datatypes/7. Python List Comprehension.ipynb`*

# Python List Comprehension

In this class, we will learn about Python list comprehensions, and how to use it.

List comprehension is an elegant and concise way to create a new list from an existing list in Python. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the **`for loop`**.

## List Comprehension vs String vs For Loop in Python

Suppose, we want to separate the letters of the word **`python`** and add the letters as items of a list. 

The first thing that comes in mind would be using **String**.

```python
# Example 1: Converting string to a list
# Method 1:

language = 'python'
lst = list(language) # changing the string to list

print(lst)           # ['p', 'y', 't', 'h', 'o', 'n']
print(type(lst))     # list
```

**Output:**
```text
['p', 'y', 't', 'h', 'o', 'n']
<class 'list'>
```

The second thing that comes in mind would be using **for loop**.

```python
# Example 1: Iterating through a string Using for Loop
# Method 2:

p_letters = []

for letter in 'python':
    p_letters.append(letter)

print(p_letters)       # ['p', 'y', 't', 'h', 'o', 'n']
print(type(p_letters)) # List
```

**Output:**
```text
['p', 'y', 't', 'h', 'o', 'n']
<class 'list'>
```

**Explanation:** 

However, Python has an easier way to solve this issue using List Comprehension. List comprehension is an elegant way to define and create lists based on existing lists.

Let’s see how the above program can be written using **list comprehension**.

```python
# Example 1: Iterating through a string Using List Comprehension
# Method 3:

p_letters = [ letter for letter in 'python' ]
print(p_letters)       # ['p', 'y', 't', 'h', 'o', 'n']
print(type(p_letters)) # List
```

**Output:**
```text
['p', 'y', 't', 'h', 'o', 'n']
<class 'list'>
```

**Explanation:**

In the above example, a new list is assigned to variable **`p_letters`**, and list contains the items of the iterable string 'human'. We call **`print()`** function to receive the output.

## Syntax of List Comprehension

```python
[expression for item in list]
```

<div>

</div>

We can now identify where list comprehensions are used.

If you noticed, **`python`** is a string, not a list. This is the power of list comprehension. It can identify when it receives a string or a tuple and work on it like a **list**.

You can do that using loops. However, not every loop can be rewritten as list comprehension. But as you learn and get comfortable with list comprehensions, you will find yourself replacing more and more loops with this elegant syntax.

## Conditionals in List Comprehension

List comprehensions can utilize conditional statement to modify existing list (or other tuples). We will create list that uses mathematical operators, integers, and **range()**.

```python
# Example 4: regular program to generate power for the numbers

pow2 = [2 ** x for x in range(10)]
print(pow2)
```

**Output:**
```text
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

Above code is equivalent to:

```python
# Example 4: with list comprehension

pow2 = []
for x in range(10):
    pow2.append(2 ** x)
print(pow2)
```

**Output:**
```text
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

A list comprehension can optionally contain more **`for`** or **if statements)**. An optional **`if`** statement can filter out items for the new list. Here are some examples.

### For instance if you want to generate a list of numbers

```python
# Example 2:
# Method 1: Generating numbers

numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Output:**
```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```python
# Example 2:
# Method 2: It is possible to do mathematical operations during iteration

squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**Output:**
```text
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

```python
# Example 2:
# Method 3: It is also possible to make a list of tuples

numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

**Output:**
```text
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
```

```python
# Example 4:

pow2 = [2 ** x for x in range(10) if x > 5]
pow2
```

**Output:**
```text
[64, 128, 256, 512]
```

### List comprehension can be combined with if statement

```python
# Example 7: Using 'if' with List Comprehension

number_list = [ x for x in range(30) if x % 2 == 0]
print(number_list)
```

**Output:**
```text
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
```

**Explanation:**

The list, **`number_list`**, will be populated by the items in range from 0-27 if the item's value is divisible by 2.

```python
# Generating even numbers

even_numbers = [x for x in range(30) if x % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                                  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

**Output:**
```text
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
```

```python
# Generating odd numbers

odd_numbers = [x for x in range(21) if x % 2 != 0]  # to generate odd numbers in range 0 to 21
# odd_numbers = [x for x in range(21) x % 2 == 1]   # this would also work!
print(odd_numbers)                                  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

**Output:**
```text
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

```python
# Filter numbers: let's filter out positive even numbers from the list below

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [x for x in range(21) if x % 2 == 0 and x > 0]
print(positive_even_numbers)                       # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

**Output:**
```text
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

```python
# Flattening a three dimensional array

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)                             # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Output:**
```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
# Example 9:

[x+y for x in ['Python ','C '] for y in ['Language','Programming']]
```

**Output:**
```text
['Python Language', 'Python Programming', 'C Language', 'C Programming']
```

```python
# Example 10: Nested 'if' with List Comprehension

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
```

**Output:**
```text
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
```

**Explanation:**

Here, list comprehension checks:

* Is **`y`** divisible by 2 or not?
* Is **`y`** divisible by 5 or not?

If **`y`** satisfies both conditions, **`y`** is appended to **`num_list`**.

```python
# Example 11: if...else With List Comprehension

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)
```

**Output:**
```text
['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
```

**Explanation:**

Here, list comprehension will check the 10 numbers from 0 to 9. If **`i`** is divisible by 2, then **`Even`** is appended to the **`obj`** list. If not, **`Odd`** is appended.

## List Comprehensions vs Lambda functions

List comprehensions aren't the only way to work on lists. Various built-in functions and lambda functions can create and modify lists in less lines of code.

### Lambda Function

**Lambda function** is a small anonymous function without a name. It can take any number of arguments, but can only have one expression. Lambda function is similar to anonymous functions in JavaScript. We need it when we want to write an anonymous function inside another function.

### Creating a Lambda Function

To create a lambda function we use **`lambda`** keyword followed by a parameter(s), followed by an expression. See the syntax and the example below. Lambda function does not use return but it explicitly returns the expression.

**Syntax:**
```py
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
```

```python
# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
```

**Output:**
```text
5
```

Lets change the above function to a lambda function

```python
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5
```

**Output:**
```text
5
```

```python
# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5
```

**Output:**
```text
5
```

```python
square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27
```

**Output:**
```text
9
27
```

```python
# Multiple variables

multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

**Output:**
```text
22
```

```python
### Lambda Function Inside Another Function

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(4) 
print(two_power_of_five)  # 16
```

**Output:**
```text
8
16
```

```python
# Example 3: Using Lambda functions inside List

letters = list(map(lambda x: x, 'python'))
print(letters)
```

**Output:**
```text
['p', 'y', 't', 'h', 'o', 'n']
```

**Explanation:**

However, list comprehensions are usually more human readable than lambda functions. It is easier to understand what the programmer was trying to accomplish when list comprehensions are used.

## Nested Loops in List Comprehension

Suppose, we need to compute the transpose of a matrix that requires nested for loop. Let's see how it is done using normal for loop first.

```python
# Example 12: Transpose of Matrix using Nested Loops

transposed = []
matrix = [[1, 2, 3, 4], [5, 6, 8, 9]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
```

**Output:**
```text
[[1, 5], [2, 6], [3, 8], [4, 9]]
```

**Explanation:**

The above code use two for loops to find transpose of the matrix.

We can also perform nested iteration inside a list comprehension. In this section, we will find transpose of a matrix using nested loop inside list comprehension.

```python
# Example 13: Transpose of a Matrix using List Comprehension

matrix = [[1,2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)
```

**Output:**
```text
[[1, 3, 5, 7], [2, 4, 6, 8]]
```

**Explanation:**

In above program, we have a variable **`matrix`** which have **`4`** rows and **`2`** columns. We need to find transpose of the **`matrix`**. For that, we used list comprehension.

>**Note:** The nested loops in list comprehension don't work like normal nested loops. In the above program, **`for i in range(2)`** is executed before **`row[i] for row in matrix`**. Hence at first, a value is assigned to **`i`** then item directed by **`row[i]`** is appended in the **`transpose`** variable.

## Key Points to Remember

* List comprehension is an elegant way to define and create lists based on existing lists.
* List comprehension is generally more compact and faster than normal functions and loops for creating list.
* However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
* Remember, every list comprehension can be rewritten in for loop, but every for loop can't be rewritten in the form of list comprehension.

## 💻 Exercises ➞ <span class='label label-default'>List Comprehension</span>

1. Filter only negative and zero in the list using list comprehension

    - ```py
numbers = [-4, -3, -2, -1, 0, 3, 6, 9, 12]
    ```

2. Flatten the following list of lists of lists to a one dimensional list :

    - ```py
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

3. Using list comprehension create the following list of tuples:

    - ```py
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
    ```

4. Flatten the following list to a new list:

    - ```py
countries = [[('INDIA', 'MUMBAI')], [('CHINA', 'SHANGHAI')], [('FINLAND', 'TAMPERE')]]
output:
[['INDIA','IN', 'MUMBAI'], ['CHINA', 'CH', 'SHANGHAI'], ['FINLAND','FI', 'TAMPERE']]
    ```

5. Change the following list to a list of dictionaries:

    - ```py
countries = [[('India', 'Mumbai')], [('China', 'Shanghai')], [('Finland', 'Tampere')]]
output:
[{'country': 'INDIA', 'city': 'MUMBAI'},
{'country': 'CHINA', 'city': 'SHANGHAI'},
{'country': 'FINLAND', 'city': 'TAMPERE'}]
    ```

6. Change the following list of lists to a list of concatenated strings:

    - ```py
names = [[('Milaan', 'Parmar')], [('Arthur', 'Curry')], [('Bill', 'Gates')], [('Ethan', 'Hunt')]]
output
['Milaan Parmar', 'Arthur Curry', 'Bill Gates', 'Ethan Hunt']
    ```

7. Write a lambda function which can solve a slope or y-intercept of linear functions.

---

## 📘 Python List Pop()
*Source: `2. Python Datatypes/7. Python List pop().ipynb`*

# Python List `pop()`

The **`pop()`** method removes the item at the given index from the list and returns the removed item.

**Syntax**:

```python
list.pop(index)
```

## `pop()` Parameters

* The **`pop()`** method takes a single argument (index).
* The argument passed to the method is optional. If not passed, the default index **-1** is passed as an argument (index of the last item).
* If the index passed to the method is not in range, it throws **IndexError: pop index out of range exception**.

## Return Value from `pop()`

The **`pop()`** method returns the item present at the given index. This item is also removed from the list.

```python
# Example 1: Pop item at the given index from the list

# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)
```

**Output:**
```text
Return Value: French
Updated List: ['Python', 'Java', 'C++', 'C']
```

>**Note:** Index in Python starts from 0, not 1.

If you need to pop the 4th element, you need to pass **3** to the **`pop()`** method.

```python
# Example 2: pop() without an index, and for negative indices

# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:') 
print('Return Value:', languages.pop())
print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:') 
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:') 
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)
```

**Output:**
```text
When index is not passed:
Return Value: C
Updated List: ['Python', 'Java', 'C++', 'Ruby']

When -1 is passed:
Return Value: Ruby
Updated List: ['Python', 'Java', 'C++']

When -3 is passed:
Return Value: Python
Updated List: ['Java', 'C++']
```

* If you need to remove the given item from the list, you can to use the **list remove() method**.


* And, you can use the **`del`** statement to **remove an item or slices from the list**.

---

## 📘 Python Set Discard()
*Source: `2. Python Datatypes/7. Python Set discard().ipynb`*

# Python Set `discard()`

The **`discard()`** method removes a specified element from the set (if present).

**Syntax**:

```python
s.discard(x)
```

## `discard()` Parameters

The **`discard()`** method takes a single element **`x`** and removes it from the set (if present).

## Return Value from `discard()`

The **`discard()`** removes element **`x`** from the set if the element is present.

This method returns **`None`** (meaning, absence of a return value).

```python
# Example 1: How discard() works?

numbers = {2, 3, 4, 5}

numbers.discard(3)
print('numbers = ', numbers)

numbers.discard(10)
print('numbers = ', numbers)
```

**Output:**
```text
numbers =  {2, 4, 5}
numbers =  {2, 4, 5}
```

```python
# Example 2: How discard() works?

numbers = {2, 3, 5, 4}

# Returns None
# Meaning, absence of a return value 
print(numbers.discard(3))

print('numbers =', numbers)
```

**Output:**
```text
None
numbers = {2, 4, 5}
```

```python
# Example 3: How discard() works?

set1 = {"Welcome", "to", "Python", "course"}
set1.discard(20)   # 20 is not an element in set1
print(set1)
```

**Output:**
```text
{'course', 'Python', 'Welcome', 'to'}
```

---

## 📘 Python String Encode()
*Source: `2. Python Datatypes/7. Python String encode().ipynb`*

# Python String `encode()`

The **`encode()`** method returns encoded version of the given string.

Since Python 3.0, **string** are stored as Unicode, i.e. each character in the string is represented by a code point. So, each string is just a sequence of Unicode code points.

For efficient storage of these strings, the sequence of code points is converted into a set of bytes. The process is known as **encodings**.

There are various encodings present which treats a string differently. The popular encoding being **utf-8**, **ascii**, etc.

Using string's **`encode()`** method, you can convert unicoded strings into any **encodings supported by Python**. By default, Python uses **utf-8** encoding.

**Syntax**:

```python
string.encode(encoding='UTF-8',errors='strict')
```

## `encode()` Parameters

By default, **`encode()`** method doesn't require any parameters.

It returns **utf-8** encoded version of the string. In case of failure, it raises a **`UnicodeDecodeError`** exception.

However, it takes two parameters:

* **encoding** - the encoding type a string has to be encoded to
* **errors** - response when encoding fails. There are six types of error response
    - **strict** - default response which raises a UnicodeDecodeError exception on failure
    - **ignore** - ignores the unencodable unicode from the result
    - **replace** - replaces the unencodable unicode to a question mark **?**
    - **xmlcharrefreplace** - inserts XML character reference instead of unencodable unicode
    - **backslashreplace** - inserts a **\uNNNN** escape sequence instead of unencodable unicode
    - **namereplace** - inserts a **\N{...}** escape sequence instead of unencodable unicode

```python
# Example 1: Encode to Default Utf-8 Encoding

# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)
```

**Output:**
```text
The string is: pythön!
The encoded version is: b'pyth\xc3\xb6n!'
```

```python
# Example 2: Encoding with error parameter

# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))

# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))
```

**Output:**
```text
The string is: pythön!
The encoded version (with ignore) is: b'pythn!'
The encoded version (with replace) is: b'pyth?n!'
```

>**Note:** Try different encoding and error parameters as well.

---

## 📘 Python Dictionary Popitem()
*Source: `2. Python Datatypes/8. Python Dictionary popitem().ipynb`*

# Python Dictionary `popitem()`

The **`popitem()`** method removes and returns the last element (key, value) pair inserted into the dictionary.

**Syntax**:

```python
dictionary.popitem() 
```

## `popitem()` Parameters

The **`popitem()`** method doesn't take any parameters.

## Return Value from `popitem()`

The **`popitem()`** method removes and returns the **(key, value)** pair from the dictionary in the **Last In, First Out (LIFO)** order.

* Returns the latest inserted element **(key,value)** pair from the dictionary.
* Removes the returned element pair from the dictionary.

>**Note:** Before Python 3.7, the **`popitem()`** method returned and removed an arbitrary element (key, value) pair from the dictionary.

```python
# Example: Working of popitem() method

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

# ('salary', 3500.0) is inserted at the last, so it is removed.
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)

# inserting a new element pair
person['profession'] = 'Plumber'

# now ('profession', 'Plumber') is the latest element
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)
```

**Output:**
```text
Return Value =  ('salary', 3500.0)
person =  {'name': 'Phill', 'age': 22}
Return Value =  ('profession', 'Plumber')
person =  {'name': 'Phill', 'age': 22}
```

> **Note:** The **`popitem()`** method raises a **`KeyError`** error if the dictionary is empty.

---

## 📘 Python List Reverse()
*Source: `2. Python Datatypes/8. Python List reverse().ipynb`*

# Python List `reverse()`

The **`reverse()`** method reverses the elements of the list.

**Syntax**:

```python
list.reverse()
```

## `reverse()` Parameters

The **`reverse()`** method doesn't take any arguments.

## Return Value from `reverse()`

The **`reverse()`** method doesn't return any value. It updates the existing list.

```python
# Example 1: Reverse a List

# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# List Reverse
systems.reverse()

# updated list
print('Updated List:', systems)
```

**Output:**
```text
Original List: ['Windows', 'macOS', 'Linux']
Updated List: ['Linux', 'macOS', 'Windows']
```

There are other several ways to reverse a list.

```python
# Example 2: Reverse a List Using Slicing Operator

# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list	
#Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[::-1]

# updated list
print('Updated List:', reversed_list)
```

**Output:**
```text
Original List: ['Windows', 'macOS', 'Linux']
Updated List: ['Linux', 'macOS', 'Windows']
```

```python
# Example 3: Accessing Elements in Reversed Order
# If you need to access individual elements of a list in the reverse order, 
# it's better to use reversed() function.

# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)
```

**Output:**
```text
Linux
macOS
Windows
```

---

## 📘 Python Set Intersection()
*Source: `2. Python Datatypes/8. Python Set intersection().ipynb`*

# Python Set `intersection()`

The **`intersection()`** method returns a new set with elements that are common to all sets.

The intersection of two or more sets is the set of elements that are common to all sets. For example:
```python
A = {1, 2, 3, 4}
B = {2, 3, 4,  9}
C = {2, 4, 9 10}

Then,
A∩B = B∩A ={2, 3, 4}
A∩C = C∩A ={2, 4}
B∩C = C∩B ={2, 4, 9}

A∩B∩C = {2, 4}
```
<div>

</div>

**Syntax**:

```python
A.intersection(*other_sets)
```

## `intersection()` Parameters

The **`intersection()`** method allows arbitrary number of arguments (sets).

>**Note:** __`*`__ is not part of the syntax. It is used to indicate that the method allows arbitrary number of arguments.

## Return Value from `intersection()`

The **`intersection()`** method returns the intersection of set A with all the sets (passed as argument).

If the argument is not passed to **`intersection()`**, it returns a shallow copy of the set **`(A)`**.

```python
# Example 1: How intersection() works?

A = {2, 3, 5, 4}
B = {2, 5, 100}
C = {2, 3, 8, 9, 10}

print(B.intersection(A))
print(B.intersection(C))
print(A.intersection(C))
print(C.intersection(A, B))
```

**Output:**
```text
{2, 5}
{2}
{2, 3}
{2}
```

```python
# Example 2:

A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

print(A.intersection(D))
print(B.intersection(D))
print(C.intersection(D))
print(A.intersection(B, C, D))
```

**Output:**
```text
{100}
{200}
{300}
set()
```

You can also find the intersection of sets using **`&`** operator.

```python
# Example 3: Set Intersection Using & operator

A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3, 7}
D = {100, 200, 300}

print(A & C)
print(A & D)


print(A & C & D)
print(A & B & C & D)
```

**Output:**
```text
{7}
{100}
set()
set()
```

---

## 📘 Python String Find()
*Source: `2. Python Datatypes/8. Python String find().ipynb`*

# Python String `find()`

The **`find()`** method returns the index of first occurrence of the substring (if found). If not found, it returns **-1**.

**Syntax**:

```python
str.find(sub[, start[, end]] )
```

## `find()` Parameters

The **`find()`** method takes maximum of three parameters:

* **sub** - It is the substring to be searched in the **`str`** string.
* **start** and **end** (optional) - The range **`str[start:end]`** within which substring is searched.

## Return Value from `find()`

The **`find()`** method returns an integer value:

* If the substring exists inside the string, it returns the index of the first occurence of the substring.
* If substring doesn't exist inside the string, it returns **-1**.

## Working of `find()` method

<div>

</div>

```python
# Example 1: find() With No start and end Argument

quote = 'Let it be, let it be, let it be'

# first occurance of 'let it'(case sensitive)
result = quote.find('let it')
print("Substring 'let it':", result)

# find returns -1 if substring not found
result = quote.find('small')
print("Substring 'small ':", result)

# How to use find()
if (quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")
```

**Output:**
```text
Substring 'let it': 11
Substring 'small ': -1
Contains substring 'be,'
```

```python
# Example 2: find() With start and end Arguments

quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))

# Substring is searched in ' small things with great love' 
print(quote.find('small things', 2))

# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))
```

**Output:**
```text
-1
3
-1
9
```

```python
# Example 3:

s="I Love Python Tutorial"
print(s.find('I'))
print(s.find('I',2))
print(s.find('Love'))
print(s.find('t',2,10))
```

**Output:**
```text
0
-1
2
9
```

---

## 📘 Python Dictionary Setdefault()
*Source: `2. Python Datatypes/9. Python Dictionary setdefault().ipynb`*

# Python Dictionary `setdefault()`

The **`setdefault()`** method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.

**Syntax**:

```python
dict.setdefault(key[, default_value])
```

## `setdefault()` Parameters

The **`setdefault()`** method takes a maximum of two parameters:

* **key** - the key to be searched in the dictionary
* **default_value** (optional) - **`key`**  with a value **`default_value`** is inserted to the dictionary if the key is not in the dictionary.

If not provided, the **`default_value`** will be **`None`**.

## Return Value from `setdefault()`

The **`setdefault()`** method returns:

* value of the **`key`** if it is in the dictionary
* None if the key is not in the dictionary and **`default_value`** is not specified
* **`default_value`** if **`key`** is not in the dictionary and **`default_value`** is specified

```python
# Example 1: How setdefault() works when key is in the dictionary?

person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)
```

**Output:**
```text
person =  {'name': 'Phill', 'age': 22}
Age =  22
```

```python
# Example 2: How setdefault() works when key is not in the dictionary?

person = {'name': 'Phill'}

# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ',person)
print('salary = ',salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ',person)
print('age = ',age)
```

**Output:**
```text
person =  {'name': 'Phill', 'salary': None}
salary =  None
person =  {'name': 'Phill', 'salary': None, 'age': 22}
age =  22
```

---

## 📘 Python List Sort()
*Source: `2. Python Datatypes/9. Python List sort().ipynb`*

# Python List `sort()`

The **`sort()`** method sorts the elements of a given list in a specific ascending or descending order.

**Syntax**:

```python
list.sort(key=..., reverse=...)
```

Alternatively, you can also use Python's built-in **sorted()** function for the same purpose.

```python
sorted(list, key=..., reverse=...)
```

>**Note:** The simplest difference between **`sort()`** and **`sorted()`** is: **`sort()`** changes the list directly and doesn't return any value, while **`sorted()`** doesn't change the list and returns the sorted list.

## `sort()` Parameters

By default, **`sort()`** doesn't require any extra parameters. However, it has two optional parameters:

* **reverse** - If **`True`**, the sorted list is reversed (or sorted in Descending order)
* **key** - function that serves as a key for the sort comparison

## Return Value from `sort()`

The **`sort()`** method doesn't return any value. Rather, it changes the original list.

If you want a function to return the sorted list rather than change the original list, use **`sorted()`**.

```python
# Example 1: Sort a given list

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)
```

**Output:**
```text
Sorted list: ['a', 'e', 'i', 'o', 'u']
```

## Sort in Descending order

The **`sort()`** method accepts a **`reverse`** parameter as an optional argument.

Setting **`reverse = True`** sorts the list in the descending order.

```python
list.sort(reverse=True)
```

Alternately for **`sorted()`**, you can use the following code.

```python
sorted(list, reverse=True)
```

```python
# Example 2: Sort the list in Descending order

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

# print vowels
print('Sorted list (in Descending):', vowels)
```

**Output:**
```text
Sorted list (in Descending): ['u', 'o', 'i', 'e', 'a']
```

## Sort with custom function using key

If you want your own implementation for sorting, the **`sort()`** method also accepts a **`key`** function as an optional parameter.

Based on the results of the key function, you can sort the given list.

```python
list.sort(key=len)
```

Alternatively for sorted:

```python
sorted(list, key=len)
```

Here, **`len`** is the Python's in-built function to count the length of an element.

The list is sorted based on the length of each element, from lowest count to highest.

We know that a tuple is sorted using its first parameter by default. Let's look at how to customize the **`sort()`** method to sort using the second element.

```python
# Example 3: Sort the list using key

# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)
```

**Output:**
```text
Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]
```

Let's take another example. Suppose we have a list of information about the employees of an office where each element is a dictionary.

We can sort the list in the following way:

```python
# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')
```

**Output:**
```text
[{'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}]

[{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]

[{'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}]
```

Here, for the first case, our custom function returns the name of each employee. Since the name is a **`string`**, Python by default sorts it using the alphabetical order.

For the second case, age (**`int`**) is returned and is sorted in ascending order.

For the third case, the function returns the salary (**`int`**), and is sorted in the descending order using **`reverse = True`**.

It is a good practice to use the lambda function when the function can be summarized in one line. So, we can also write the above program as:

```python
# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')
```

**Output:**
```text
[{'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}]

[{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]

[{'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}]
```

---

## 📘 Python Set Intersection Update()
*Source: `2. Python Datatypes/9. Python Set intersection update().ipynb`*

# Python Set `intersection_update()`

The **`intersection_update()`** updates the set calling **`intersection_update()`** method with the intersection of sets.

The intersection of two or more sets is the set of elements which are common to all sets.

To learn more, visit **Python set Intersection()**.

**Syntax**:

```python
A.intersection_update(*other_sets)
```

## `intersection_update()` Parameters

The **`intersection_update()`** method allows an arbitrary number of arguments (sets).

>**Note:** __`*`__ is not part of the syntax. It is used to indicate that the method allows an arbitrary number of arguments.

## Return Value from `intersection_update()`

The **`intersection_update()`** method returns **`None`** (meaning it does not have a return value). It only updates the set calling the **`intersection_update()`** method.

For example:
```python
result = A.intersection_update(B, C)
```

When you run the code,

* **`result`** will be **`None`**
* **`A`** will be equal to the intersection of **`A`**,**`B`**, and **`C`**
* **`B`** remains unchanged
* **`C`** remains unchanged

```python
# Example 1: How intersection_update() Works?

A = {1, 2, 3, 4}
B = {2, 3, 4, 5}

result = A.intersection_update(B)

print('result =', result)
print('A =', A)
print('B =', B)
```

**Output:**
```text
result = None
A = {2, 3, 4}
B = {2, 3, 4, 5}
```

```python
# Example 2: intersection_update() with Two Parameters

A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}

result = C.intersection_update(B, A)

print('result =', result)
print('C =', C)
print('B =', B)
print('A =', A)
```

**Output:**
```text
result = None
C = {4}
B = {2, 3, 4, 5, 6}
A = {1, 2, 3, 4}
```

---

## 📘 Python String Format()
*Source: `2. Python Datatypes/9. Python String format().ipynb`*

# Python String `format()`

The string **`format()`** method formats the given string into a nicer output in Python.

**Syntax**:

```python
template.format(p0, p1, ..., k0=v0, k1=v1, ...)
```

Here, **`p0, p1,...`** are positional arguments and, **`k0, k1,...`** are keyword arguments with values **`v0, v1,...`** respectively.

And, **`template`** is a mixture of format codes with placeholders for the arguments

## `format()` Parameters

The **`format()`** method takes any number of parameters. But, is divided into two types of parameters:

* **Positional parameters** - list of parameters that can be accessed with index of parameter inside curly braces **`{index}`**
* **Keyword parameters** - list of parameters of type key=value, that can be accessed with key of parameter inside curly braces **`{key}`**

## Return Value from `format()`

The **`format()`** method returns the formatted string.

## How String `format()` works?

The **`format()`** reads the type of arguments passed to it and formats it according to the format codes defined in the string.

### For positional arguments

<div>

</div>

Here, Argument **0** is a string **"Adam"** and Argument **1** is a floating number **230.2346**.

>**Note:** Argument list starts from **0** in Python.

The string **`"Hello {0}, your balance is {1:9.3f}"`** is the template string. This contains the format codes for formatting.

The curly braces are just placeholders for the arguments to be placed. In the above example, **`{0}`** is placeholder for **`"Adam"`** and **`{1:9.3f}`** is placeholder for **`230.2346`**.

Since the template string references **`format()`** arguments as **`{0}`** and **`{1}`**, the arguments are positional arguments. They both can also be referenced without the numbers as **`{}`** and Python internally converts them to numbers.

Internally,

* Since **`"Adam"`** is the 0th argument, it is placed in place of **`{0}`**. Since, **`{0}`** doesn't contain any other format codes, it doesn't perform any other operations.


* However, it is not the case for 1st argument **`230.2346`**. Here, **`{1:9.3f}`** places **`230.2346`** in its place and performs the operation **9.3f**.


* **f** specifies the format is dealing with a float number. If not correctly specified, it will give out an error.


* The part before the **"." (9)** specifies the minimum width/padding the number **(230.2346)** can take. In this case, **230.2346** is allotted a minimum of **9** places including the **"."**.


* If no alignment option is specified, it is aligned to the right of the remaining spaces. (For strings, it is aligned to the left.)


* The part after the **"." (3)** truncates the decimal part **(2346)** upto the given number. In this case, **2346** is truncated after 3 places.


* Remaining numbers **(46)** is rounded off outputting **235**.

### For keyword arguments

<div>

</div>

We've used the same example from above to show the difference between keyword and positional arguments.

Here, instead of just the parameters, we've used a key-value for the parameters. Namely, **`name="Adam"`** and **`blc=230.2346`**.

Since these parameters are referenced by their keys as **`{name}`** and **`{blc:9.3f}`**, they are known as keyword or named arguments.

Internally,

* The placeholder **`{name}`** is replaced by the value of name - "Adam". Since it doesn't contain any other format codes, "Adam" is placed.


* For the argument **blc=230.2346**, the placeholder **`{blc:9.3f}`** is replaced by the value 230.2346. But before replacing it, like previous example, it performs 9.3f operation on it. 


This outputs **230.235**. The decimal part is truncated after **3** places and remaining digits are rounded off. Likewise, the total width is assigned 9 leaving two spaces to the left.

## Basic formatting with `format()`

The **`format()`** method allows the use of simple placeholders for formatting.

```python
# Example 1: Basic formatting for default, positional and keyword arguments

# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))
```

**Output:**
```text
Hello Adam, your balance is 230.2346.
Hello Adam, your balance is 230.2346.
Hello Adam, your balance is 230.2346.
Hello Adam, your balance is 230.2346.
```

>**Note:** In case of mixed arguments, keyword arguments has to always follow positional arguments.

## Numbers formatting with `format()`

You can format numbers using the format specifier given below:

| Type | Meaning |
|:----| :--- |
| **`d`** | **Decimal integer** | 
| **`c`** | **Corresponding Unicode character** | 
| **`b`** | **Binary format** | 
| **`o`** | **Octal format** | 
| **`x`** | **Hexadecimal format (lower case)** | 
| **`X`** | **Hexadecimal format (upper case)** | 
| **`n`** | **Same as 'd'. Except it uses current locale setting for number separator** | 
| **`e`** | **Exponential notation. (lowercase e)** | 
| **`E`** | **Exponential notation (uppercase E)** | 
| **`f`** | **Displays fixed point number (Default: 6)** | 
| **`F`** | **Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'** | 
| **`g`** | **General format. Rounds number to p significant digits. (Default precision: 6)** | 
| **`G`** | **Same as 'g'. Except switches to 'E' if the number is large.** | 
| **`%`** | **Percentage. Multiples by 100 and puts % at the end.** |

```python
# Example 2: Simple number formatting

# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.4567898))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))
```

**Output:**
```text
The number is:123
The float number is:123.456790
bin: 1100, oct: 14, hex: c
```

```python
# Example 3: Number formatting with padding for int and floats
    
# integer numbers with minimum width
print("{:5d}".format(12))

# width doesn't work for numbers longer than padding
print("{:2d}".format(1234))

# padding for float numbers
print("{:8.3f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))
```

**Output:**
```text
12
1234
  12.235
00012
0012.235
```

**Explanation:** Here,

* in the first statement, **`{:5d}`** takes an integer argument and assigns a minimum width of 5. Since, no alignment is specified, it is aligned to the right.

* In the second statement, you can see the width (2) is less than the number (1234), so it doesn't take any space to the left but also doesn't truncate the number.

* Unlike integers, floats has both integer and decimal parts. And, the mininum width defined to the number is for both parts as a whole including **"."**.

* In the third statement, **`{:8.3f}`** truncates the decimal part into 3 places rounding off the last 2 digits. And, the number, now 12.235, takes a width of 8 as a whole leaving 2 places to the left.

* If you want to fill the remaining places with zero, placing a zero before the format specifier does this. It works both for integers and floats: **`{:05d}`** and **`{:08.3f}`**.

```python
# Example 4: Number formatting for signed numbers

# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))
```

**Output:**
```text
+12.230000 -12.230000
12.230000 -12.230000
 12.230000 -12.230000
```

## Number formatting with alignment

The operators **`<`**, **`^`**, **`>`** and **`=`** are used for alignment when assigned a certain width to the numbers.

| Type | Meaning |
|:----| :--- |
| **`<`** | **Left aligned to the remaining space** | 
| **`^`** | **Center aligned to the remaining space** | 
| **`>`** | **Right aligned to the remaining space** | 
| **`=`** | **Forces the signed (+) (-) to the leftmost position** |

```python
# Example 5: Number formatting with left, right and center alignment

# integer numbers with right alignment
print("{:5d}".format(12))

# float numbers with center alignment
print("{:^10.3f}".format(12.2346))

# integer left alignment filled with zeros
print("{:<05d}".format(12))

# float numbers with center alignment
print("{:=8.3f}".format(-12.2346))
```

**Output:**
```text
12
  12.235  
12000
- 12.235
```

>**Note:** Left alignment filled with zeros for integer numbers can cause problems as the 3rd example which returns 12000, rather than 12.

## String formatting with `format()`

As numbers, string can be formatted in a similar way with **`format()`**.

```python
# Example 6: String formatting with padding and alignment

# string padding with left alignment
print("{:5}".format("cat"))

# string padding with right alignment
print("{:>5}".format("cat"))

# string padding with center alignment
print("{:^5}".format("cat"))

# string padding with center alignment
# and '*' padding character
print("{:*^5}".format("cat"))
```

**Output:**
```text
cat  
  cat
 cat 
*cat*
```

```python
# Example 7: Truncating strings with format()

# truncating strings to 3 letters
print("{:.3}".format("caterpillar"))

# truncating strings to 3 letters
# and padding
print("{:5.3}".format("caterpillar"))

# truncating strings to 3 letters,
# padding and center alignment
print("{:^5.3}".format("caterpillar"))
```

**Output:**
```text
cat
cat  
 cat
```

## Formatting class and dictionary members using `format()`

Python internally uses **`getattr()`** for class members in the form ".age". And, it uses **`__getitem__()`** lookup for dictionary members in the form "[index]".

```python
# Example 8: Formatting class members using format()

# define Person class
class Person:
    age = 23
    name = "Adam"

# format age
print("{p.name}'s age is: {p.age}".format(p=Person()))
```

**Output:**
```text
Adam's age is: 23
```

**Explanation:** Here, Person **`object`** is passed as a keyword argument **`p`**.

Inside the template string, Person's **`name`** and **`age`** are accessed using **`.name`** and **`.age`** respectively.

```python
# Example 9: Formatting dictionary members using format()

# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{p[name]}'s age is: {p[age]}".format(p=person))
```

**Output:**
```text
Adam's age is: 23
```

**Explanation:** Similar to class, **`person`** dictionary is passed as a keyword argument **`p`**.

Inside the template string, person's **`name`** and **`age`** are accessed using **`[name]`** and **`[age]`** respectively.

There's an easier way to format dictionaries in Python using __`str.format(**mapping)`__.

```python
# define Person dictionary

person = {'age': 23, 'name': 'Adam'}

# format age
print("{name}'s age is: {age}".format(**person))
```

**Output:**
```text
Adam's age is: 23
```

__`**`__ is a format parameter (minimum field width).

## Arguments as format codes using `format()`

You can also pass format codes like precision, alignment, fill character as positional or keyword arguments dynamically.

```python
# Example 10: Dynamic formatting using format()

# dynamic string format template
string = "{:{fill}{align}{width}}"

# passing format codes as arguments
print(string.format('cat', fill='*', align='^', width=5))

# dynamic float format template
num = "{:{align}{width}.{precision}f}"

# passing format codes as arguments
print(num.format(123.236, align='<', width=8, precision=2))
```

**Output:**
```text
*cat*
123.24
```

**Explanation:** Here,

* In the first example, 'cat' is the positional argument is to be formatted. Likewise, **`fill='*'`**, **`align='^'`** and **`width=5`** are keyword arguments.

* In the template string, these keyword arguments are not retrieved as normal strings to be printed but as the actual format codes **`fill`**, **`align`** and **`width`**. The arguments replaces the corresponding named placeholders and the string **'cat'** is formatted accordingly.

* Likewise, in the second example, **123.236** is the positional argument and, align, width and precision are passed to the template string as format codes.

## Extra formatting options with `format()`

**`format()`** also supports type-specific formatting options like datetime's and complex number formatting.

**`format()`** internally calls **`__format__()`** for datetime, while **`format()`** accesses the attributes of the complex number.

You can easily override the **`__format__()`** method of any object for custom formatting.

```python
# Example 11: Type-specific formatting with format() and overriding __format__() method

import datetime
# datetime formatting
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

# complex number formatting
complexNumber = 1+2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))

# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

print("Adam's age is: {:age}".format(Person()))
```

**Output:**
```text
It's now: 2021/06/10 23:36:57
Real part: 1.0 and Imaginary part: 2.0
Adam's age is: 23
```

**Explanation:** Here,

* **For datetime:**
    - Current datetime is passed as a positional argument to the **`format()`** method.
    - And, internally using **`__format__()`** method, **`format()`** accesses the year, month, day, hour, minutes and seconds.

* **For complex numbers:**
    - 1+2j is internally converted to a ComplexNumber object.
    - Then accessing its attributes **`real`** and **`imag`**, the number is formatted.

* **Overriding __format__():**
    - Like datetime, you can override your own **`__format__()`** method for custom formatting which returns age when accessed as **`{:age}`**

You can also use object's **`__str__()`** and **`__repr__()`** functionality with shorthand notations using **`format()`**.

Like **`__format__()`**, you can easily override object's **`__str__()`** and **`__repr_()`** methods.

```python
# Example 12: __str()__ and __repr()__ shorthand !r and !s using format()

# __str__() and __repr__() shorthand !r and !s
print("Quotes: {0!r}, Without Quotes: {0!s}".format("cat"))

# __str__() and __repr__() implementation for class
class Person:
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPR"

print("repr: {p!r}, str: {p!s}".format(p=Person()))
```

**Output:**
```text
Quotes: 'cat', Without Quotes: cat
repr: REPR, str: STR
```

---

## 📘 Python Dictionary Update()
*Source: `2. Python Datatypes/10. Python Dictionary update().ipynb`*

# Python Dictionary `update()`

The **`update()`** method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.

The **`update()`** method adds element(s) to the dictionary if the key is not in the dictionary. If the key is in the dictionary, it updates the key with the new value.

**Syntax**:

```python
dict.update([other])
```

## `update()` Parameters

The **`update()`** method takes either a **dictionary** or an iterable object of key/value pairs (generally **tuples**).

If **`update()`** is called without passing parameters, the dictionary remains unchanged.

## Return Value from `update()`

The **`update()`** method updates the dictionary with elements from a dictionary object or an iterable object of key/value pairs.

It doesn't return any value (returns **`None`**).

```python
# Example 1: Working of update()

d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)
```

**Output:**
```text
{1: 'one', 2: 'two'}
{1: 'one', 2: 'two', 3: 'three'}
```

```python
# Example 2: update() When Tuple is Passed

d = {'x': 2}

d.update(y = 3, z = 0)
print(d)
```

**Output:**
```text
{'x': 2, 'y': 3, 'z': 0}
```

**Explanation:** 

The view object **`values`** doesn't itself return a list of **`sales`** item values but it returns a view of all values of the dictionary.

If the list is updated at any time, the changes are reflected on the view object itself, as shown in the above program.

---

## 📘 Python List Copy()
*Source: `2. Python Datatypes/10. Python List copy().ipynb`*

# Python List `copy()`

The **`copy()`** method returns a shallow copy of the list.

A **list** can be copied using the **`=`** operator. For example,

```python
old_list = [1, 2, 3]
new_list = old_list
print('old_list:', old_list)
print('new_list:', new_list)
```

**Output:**
```text
old_list: [1, 2, 3]
new_list: [1, 2, 3]
```

The problem with copying lists in this way is that if you modify **`new_list`**, **`old_list`** is also modified. It is because the new list is referencing or pointing to the same **`old_list`** object.

```python
old_list = [1, 2, 3]
new_list = old_list

# add an element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)
```

**Output:**
```text
New List: [1, 2, 3, 'a']
Old List: [1, 2, 3, 'a']
```

However, if you need the original list unchanged when the new list is modified, you can use the **`copy()`** method.

**Syntax**:

```python
new_list = list.copy()
```

## `copy()` Parameters

The **`copy()`** method doesn't take any parameters.

## Return Value from `copy()`

The **`copy()`** method returns a new list. It doesn't modify the original list.

```python
# Example 1: Copying a List

# mixed list
my_list = ['cat', 0, 6.7]

# copying a list
new_list = my_list.copy()

print('Copied List:', new_list)
```

**Output:**
```text
Copied List: ['cat', 0, 6.7]
```

If you modify the **`new_list`** in the above example, **`my_list`** will not be modified.

```python
# Copy List Using Slicing Syntax

# shallow copy using the slicing syntax

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)
```

**Output:**
```text
Old List: ['cat', 0, 6.7]
New List: ['cat', 0, 6.7, 'dog']
```

---

## 📘 Python Set Isdisjoint()
*Source: `2. Python Datatypes/10. Python Set isdisjoint().ipynb`*

# Python Set `isdisjoint()`

The **`isdisjoint()`** method returns **`True`** if two sets are disjoint sets. If not, it returns **`False`**.

Two sets are said to be disjoint sets if they have no common elements. For example:
```python
A = {1, 5, 9, 0}
B = {2, 4, -5}
```

<div>

</div>

**Syntax**:

```python
set_a.isdisjoint(set_b)
```

## `isdisjoint()` Parameters

The **`isdisjoint()`** method takes a single argument (a set).

You can also pass an iterable (list, tuple, dictionary, and string) to **`disjoint()`**. **`isdisjoint()`** method will automatically convert iterables to set and checks whether the sets are disjoint or not.

## Return Value from `isdisjoint()`

The **`isdisjoint()`** method returns

* **`True`** if two sets are disjoint sets (if **`set_a`** and **`set_b`** are disjoint sets in above syntax)
* **`False`** if two sets are not disjoint sets

```python
# Example 1: How isdisjoint() works?

A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))
```

**Output:**
```text
Are A and B disjoint? True
Are A and C disjoint? False
```

```python
# Example 2: isdisjoint() with Other Iterables as arguments

A = {'a', 'b', 'c', 'd'}
B = ['b', 'e', 'f']
C = '5de4'
D ={1 : 'a', 2 : 'b'}
E ={'a' : 1, 'b' : 2}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))
print('Are A and D disjoint?', A.isdisjoint(D))
print('Are A and E disjoint?', A.isdisjoint(E))
```

**Output:**
```text
Are A and B disjoint? False
Are A and C disjoint? False
Are A and D disjoint? True
Are A and E disjoint? False
```

You can also find the intersection of sets using **`&`** operator.

```python
# Example 3: Set Intersection Using & operator

A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3, 7}
D = {100, 200, 300}

print(A & C)
print(A & D)


print(A & C & D)
print(A & B & C & D)
```

**Output:**
```text
{7}
{100}
set()
set()
```

---

## 📘 Python String Index()
*Source: `2. Python Datatypes/10. Python String index().ipynb`*

# Python String `index()`

The string **`index()`** method returns the index of a substring inside the **string** (if found). If the substring is not found, it raises an exception.

**Syntax**:

```python
str.index(sub[, start[, end]] )
```

## `index()` Parameters

The **`index()`** method takes three parameters:

* **sub** - substring to be searched in the string **`str`**.
* **start** and **`end`** (optional) - substring is searched within **`str[start:end]`**.

## Return Value from `index()`

* If substring exists inside the string, it returns the lowest index in the string where substring is found.
* If substring doesn't exist inside the string, it raises a **ValueError** exception.

The **`index()`** method is similar to **find() method for strings**.

The only difference is that **`find()`** method returns -1 if the substring is not found, whereas **`index()`** throws an exception.

```python
# Example 1: index() With Substring argument Only

sentence = 'Python programming is fun.'

result = sentence.index('is fun')
print("Substring 'is fun':", result)

result = sentence.index('Java')
print("Substring 'Java':", result)
```

**Output:**
```text
Substring 'is fun': 19
```

>**Note:** Index in Python starts from 0 and not 1. So the occurrence is 19 and not 20.

```python
# Example 2: index() With start and end Arguments

sentence = 'Python programming is fun.'

# Substring is searched in 'gramming is fun.'
print(sentence.index('ing', 10))

# Substring is searched in 'gramming is '
print(sentence.index('g is', 10, -4))

# Substring is searched in 'programming'
print(sentence.index('fun', 7, 18))
```

**Output:**
```text
15
17
```

```python
# Example 3:

s="I Love Python Tutorial"
print(s.index('i'))
print(s.index('i',2))
print(s.index('Love'))
print(s.index('Love',7))
print(s.index('i',0,10))
```

**Output:**
```text
19
19
2
```

---

## 📘 Python Dictionary Values()
*Source: `2. Python Datatypes/11. Python Dictionary values().ipynb`*

# Python Dictionary `values()`

The **`values()`** method returns a view object that displays a list of all the values in the dictionary.

**Syntax**:

```python
dictionary.values()
```

## `values()` Parameters

The **`values()`** method doesn't take any parameters.

## Return Value from `values()`

The **`values()`** method returns a view object that displays a list of all values in a given dictionary.

```python
# Example 1: Get all values from the dictionary

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.values())
```

**Output:**
```text
dict_values([2, 3, 4])
```

```python
# Example 2: How values() works when dictionary is modified?

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

values = sales.values()
print('Original items:', values)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', values)
```

**Output:**
```text
Original items: dict_values([2, 3, 4])
Updated items: dict_values([3, 4])
```

**Explanation:** 

The view object **`values`** doesn't itself return a list of **`sales`** item values but it returns a view of all values of the dictionary.

If the list is updated at any time, the changes are reflected on the view object itself, as shown in the above program.

---

## 📘 Python List Clear()
*Source: `2. Python Datatypes/11. Python List clear().ipynb`*

# Python List `clear()`

The **`clear()`** method removes all items from the list.

**Syntax**:

```python
list.clear()
```

## `pop()` Parameters

The **`clear()`** method doesn't take any parameters.

## Return Value from `clear()`

The **`clear()`** method only empties the given **list**. It doesn't return any value.

```python
# Example 1: Working of clear() method

# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()

print('List:', list)
```

**Output:**
```text
List: []
```

>**Note:** If you are using Python 2 or Python 3.2 and below, you cannot use the **`clear()`** method. You can use the del operator instead.

```python
# Example 2: Emptying the List Using del

# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]

print('List:', list)
```

**Output:**
```text
List: []
```

Visit **Python del statement** to learn how **`del`** operator works in Python.

---

## 📘 Python Set Issubset()
*Source: `2. Python Datatypes/11. Python Set issubset().ipynb`*

# Python Set `issubset()`

The **`issubset()`** method returns **`True`** if all elements of a set are present in another set (passed as an argument). If not, it returns **`False`**.

Set **`A`** is said to be the subset of set **`B`** if all elements of **`A`** are in **`B`**.

<div>

</div>

Here, set **`A`** is a subset of **`B`**.

**Syntax**:

```python
A.issubset(B)
```
The above code checks if **`A`** is a subset of **`B`**.

## Return Value from `issubset()`

The **`issubset()`** returns

* **`True`** if **`A`** is a subset of **`B`**
* **`False`** if **`A`** is not a subset of **`B`**

```python
# Example: How issubset() works?

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

# Returns True
print(A.issubset(B))

# Returns False
# B is not subset of A
print(B.issubset(A))

# Returns False
print(A.issubset(C))

# Returns True
print(C.issubset(B))
```

**Output:**
```text
True
False
False
True
```

If you need to check if a set is a superset of another set, you can use **issuperset() in Python**.

---

## 📘 Python String Isalnum()
*Source: `2. Python Datatypes/11. Python String isalnum().ipynb`*

# Python String `isalnum()`

The string **`isalnum()`** method returns **`True`** if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns **`False`**.

**Syntax**:

```python
string.isalnum()
```

## `isalnum()` Parameters

The **`isalnum()`** method doesn't take any parameters.

## Return Value from `isalnum()`

The **`isalnum()`** returns:

* **`True`** if all characters in the string are alphanumeric
* **`False`** if at least one character is not alphanumeric

```python
# Example 1: Working of isalnum()

name = "M234onica"
print(name.isalnum())

# contains whitespace
name = "M3onica Gell22er "
print(name.isalnum())

name = "Mo3nicaGell22er"
print(name.isalnum())

name = "133"
print(name.isalnum())
```

**Output:**
```text
True
False
True
True
```

```python
# Example 2: Working of isalnum()

name = "M0n1caG3ll3r"

if name.isalnum() == True:
    print("All characters of string (name) are alphanumeric.")
else:
    print("All characters are not alphanumeric.")
```

**Output:**
```text
All characters of string (name) are alphanumeric.
```

```python
# Example 3:

s="I Love Python 3 Tutorial"
print(s.isalnum())

s="Python" # No space
print(s.isalnum())
```

**Output:**
```text
False
True
```

---

## 📘 Python Dictionary Comprehension
*Source: `2. Python Datatypes/12. Python Dictionary Comprehension.ipynb`*

# Python Dictionary Comprehension

In this tutorial, we will learn about Python dictionary comprehension and how to use it with the help of examples.

Dictionaries are data types in Python which allows us to store data in **key:value pair**. For example:

**Syntax**:

```python
my_dict = {1: 'apple', 2: 'ball'}
```
To learn more about them visit: **Python Dictionary**

## What is Dictionary Comprehension in Python?

Dictionary comprehension is an elegant and concise way to create dictionaries.

```python
# Example 1: Dictionary Comprehension

square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)
```

**Output:**
```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

Now, let's create the dictionary in the above program using dictionary comprehension.

```python
# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)
```

**Output:**
```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

In both programs, we have created a dictionary **`square_dict`** with **number-square key/value pair**.

However, using dictionary comprehension allowed us to **create a dictionary in a single line**.

## Using Dictionary Comprehension

From the above example, we can see that dictionary comprehension should be written in a specific pattern.

**Syntax**:

```python
dictionary = {key: value for vars in iterable}
```
Let's compare this syntax with dictionary comprehension from the above example.

<div>

</div>

Now, let's see how we can use dictionary comprehension using data from another dictionary.

```python
# Example 3: How to use Dictionary Comprehension

#item price in dollars
old_price = {'milk': 2.03, 'bread': 2.6, 'butter': 2.6}

dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)
```

**Output:**
```text
{'milk': 1.5428, 'bread': 1.9760000000000002, 'butter': 1.9760000000000002}
```

**Explanation:**

Here, we can see that we retrieved the item prices in dollars and converted them to pounds. Using dictionary comprehension makes this task much simpler and shorter.

## Conditionals in Dictionary Comprehension

We can further customize dictionary comprehension by adding conditions to it. Let's look at an example.

```python
# Example 4: If Conditional Dictionary Comprehension
    
original_dict = {'Allan': 36, 'Bill': 48, 'Cory': 57, 'Dave': 33}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)
```

**Output:**
```text
{'Allan': 36, 'Bill': 48}
```

**Explanation:**

As we can see, only the items with even value have been added, because of the **`if`** clause in the dictionary comprehension.

```python
# Example 5: Multiple if Conditional Dictionary Comprehension

original_dict = {'Allan': 36, 'Bill': 48, 'Cory': 57, 'Dave': 33}

new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)
```

**Output:**
```text
{'Dave': 33}
```

**Explanation:**

In this case, only the items with an odd value of less than 40 have been added to the new dictionary.

It is because of the multiple **`if`** clauses in the dictionary comprehension. They are equivalent to **`and`** operation where both conditions have to be true.

```python
# Example 6: if-else Conditional Dictionary Comprehension

original_dict = {'Allan': 36, 'Bill': 48, 'Cory': 57, 'Dave': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()}
print(new_dict_1)
```

**Output:**
```text
{'Allan': 'young', 'Bill': 'old', 'Cory': 'old', 'Dave': 'young'}
```

**Explanation:**
    
In this case, a new dictionary is created via dictionary comprehension.
The items with a value of 40 or more have the value of 'old' while others have the value of 'young'.

## Nested Dictionary Comprehension

Like how a Dictionary is a collection of **key-value** pairs, Python nested dictionaries are an unordered collection of one or two dictionaries. These can be represented as shown below.

**Syntax:**

```python
nested_dict = { 'dict1': {'key1': 'value1'}, 'dict2': {'key2': 'value2'}}
```
Here, nested_dict is a nested dictionary which has two dictionaries with keys **`dict1`** and **`dict2`**. The values of those two keys (**`dict1`**, **`dict2`**) are in-turn dictionaries.

In Python, Nested dictionaries can be created by placing the comma-separated dictionaries enclosed within curly brackets. For example:

```python
# Example 7: creating a nested dictionary

nes_dict = {'dict1': {'Color': 'Red', 'Shape': 'Square'}, 'dict2': {'Color': 'Pink', 'Shape': 'Round'}}
print (nes_dict)
```

**Output:**
```text
{'dict1': {'Color': 'Red', 'Shape': 'Square'}, 'dict2': {'Color': 'Pink', 'Shape': 'Round'}}
```

<div>

</div>

```python
# Example 8: Nested Dictionary with Two Dictionary Comprehensions

dictionary = {k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)}
print(dictionary)
```

**Output:**
```text
{2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}, 3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}, 4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}}
```

**Explanation:**

As you can see, we have constructed a multiplication table in a nested dictionary, for numbers from 2 to 4.

Whenever nested dictionary comprehension is used, Python first starts from the outer loop and then goes to the inner one.

So, the above code would be equivalent to:

```python
# Example 8:

dictionary = dict()
for k1 in range(11, 16):
    dictionary[k1] = {k2: k1*k2 for k2 in range(1, 6)}
print(dictionary)
```

**Output:**
```text
{11: {1: 11, 2: 22, 3: 33, 4: 44, 5: 55}, 12: {1: 12, 2: 24, 3: 36, 4: 48, 5: 60}, 13: {1: 13, 2: 26, 3: 39, 4: 52, 5: 65}, 14: {1: 14, 2: 28, 3: 42, 4: 56, 5: 70}, 15: {1: 15, 2: 30, 3: 45, 4: 60, 5: 75}}
```

It can further be unfolded:

```python
# Example 8:

dictionary = dict()
for k1 in range(11, 16):
    dictionary[k1] = dict()
    for k2 in range(1, 6):
        dictionary[k1][k2] = k1*k2
print(dictionary)
```

**Output:**
```text
{11: {1: 11, 2: 22, 3: 33, 4: 44, 5: 55}, 12: {1: 12, 2: 24, 3: 36, 4: 48, 5: 60}, 13: {1: 13, 2: 26, 3: 39, 4: 52, 5: 65}, 14: {1: 14, 2: 28, 3: 42, 4: 56, 5: 70}, 15: {1: 15, 2: 30, 3: 45, 4: 60, 5: 75}}
```

All these three programs give us the same output.

### How to Add a Dictionary to a Nested Dictionary

Another way to add a dictionary to an existing nested dictionary is shown below.

```python
# Example 9: adding a dictionary to nested dictionary

nes_dict = {'dict1': {'Color': 'Red', 'Shape': 'Square'}, 'dict2': {'Color': 'Pink', 'Shape': 'Round'}}
nes_dict['dict3'] = {'Color': 'Blue', 'Shape': 'Rectangle'}
print(nes_dict)
```

**Output:**
```text
{'dict1': {'Color': 'Red', 'Shape': 'Square'}, 'dict2': {'Color': 'Pink', 'Shape': 'Round'}, 'dict3': {'Color': 'Blue', 'Shape': 'Rectangle'}}
```

### How to Access Values of a Nested Dictionary

Values of a nested dictionary can simply be accessed using their respective keys.

```python
# Example 10: accessing a value in nested dictionary

nes_dict = {'dict1': {'Color': 'Red', 'Shape': 'Square'}, 'dict2': {'Color': 'Pink', 'Shape': 'Round'}}
print(nes_dict['dict1']['Color'])
print(nes_dict['dict2']['Shape'])
```

**Output:**
```text
Red
Round
```

### How to Delete Elements from a Nested Dictionary

The key-value pairs in Python nested dictionaries can be deleted using the **`del()`** method. This method can be used to delete either the entire dictionary or a particular key-value pair from a nested dictionary.

```python
# Example 11: deleting the entire nested dictionary

nes_dict = {'dict1': {'Color': 'Red', 'Shape': 'Square'}, 'dict2': {'Color': 'Pink', 'Shape': 'Round'}}
del nes_dict['dict1']
print(nes_dict)

# deleting the a key-value from nested dictionary
nes_dict = {'dict1': {'Color': 'Red', 'Shape': 'Square'}, 'dict2': {'Color': 'Pink', 'Shape': 'Round'}}
del nes_dict['dict1']
del nes_dict['dict2']['Shape']
print (nes_dict)
```

**Output:**
```text
{'dict2': {'Color': 'Pink', 'Shape': 'Round'}}
{'dict2': {'Color': 'Pink'}}
```

## Advantages of Using Dictionary Comprehension

As we can see, dictionary comprehension shortens the process of dictionary initialization by a lot. It makes the code more pythonic.

Using dictionary comprehension in our code can shorten the lines of code while keeping the logic intact.

## Warnings on Using Dictionary Comprehension

Even though dictionary comprehensions are great for writing elegant code that is easy to read, they are not always the right choice.

We must be careful while using them as :

* They can sometimes make the code run slower and consume more memory.
* They can also decrease the readability of the code.

We must not try to fit a difficult logic or a large number of dictionary comprehension inside them just for the sake of making the code single lined. In these cases, It is better to choose other alternatives like loops.

---

## 📘 Python Set Issuperset()
*Source: `2. Python Datatypes/12. Python Set issuperset().ipynb`*

# Python Set `issuperset()`

The **`issuperset()`** method returns **`True`** if a set has every elements of another set (passed as an argument). If not, it returns **`False`**.

Set **`A`** is said to be the subset of set **`B`** if all elements of **`A`** are in **`B`**.

<div>

</div>

Here, set **`B`** is a superset of set **`A`** and **`A`** is a subset of set **`B`**.

**Syntax**:

```python
A.issuperset(B)
```
The above code checks if **`A`** is a superset of **`B`**.

## Return Value from `issuperset()`

The **`issuperset()`** returns

* **`True`** if **`A`** is a superset of **`B`**
* **`False`** if **`A`** is not a superset of **`B`**

```python
# Example: How issuperset() works?

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}

# Returns True
print(A.issuperset(B))

# Returns False
print(B.issuperset(A))

# Returns True
print(C.issuperset(B))
```

**Output:**
```text
True
False
True
```

If you need to check if a set is a superset of another set, you can use **issubset() in Python**.

---

## 📘 Python String Isalpha()
*Source: `2. Python Datatypes/12. Python String isalpha().ipynb`*

# Python String `isalpha()`

The string **`isalpha()`** method returns **`True`** if all characters in the string are alphabets. If not, it returns **`False`**.

**Syntax**:

```python
string.isalpha()
```

## `isalpha()` Parameters

The **`isalpha()`** method doesn't take any parameters.

## Return Value from `isalpha()`

The **`isalpha()`** returns:

* **`True`** if all characters in the string are alphabets (can be both lowercase and uppercase).
* **`False`** if at least one character is not alphabet.

```python
# Example 1: Working of isalpha()

name = "Monica"
print(name.isalpha())

# contains whitespace
name = "Monica Geller"
print(name.isalpha())

# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())
```

**Output:**
```text
True
False
False
```

```python
# Example 2: Working of isalpha()

name = "MonicaGeller"

if name.isalpha() == True:
    print("All characters are alphabets")
else:
    print("All characters are not alphabets.")
```

**Output:**
```text
All characters are alphabets
```

```python
# Example 3:

s="I Love Python 3 Tutorial"
print(s.isalpha())
s="Python" # No space & digit in this string
print(s.isalpha())
```

**Output:**
```text
False
True
```

---

## 📘 Python Set Pop()
*Source: `2. Python Datatypes/13. Python Set pop().ipynb`*

# Python Set `pop()`

The **`pop()`** method removes an arbitrary element from the set and returns the element removed.

**Syntax**:

```python
set.pop()
```

## `pop()` Parameters

The **`pop()`** method doesn't take any arguments.

## Return Value from `pop()`

The **`pop()`** method returns an arbitrary (random) element from the set. Also, the set is updated and will not contain the element (which is returned).

If the set is empty, **`TypeError`** exception is raised.

```python
# Example 1: How pop() works for Python Sets?

A ={'a', 'b', 'c', 'd'}

print('Return Value is', A.pop())
print('A = ', A)

# When you run the program, we got the following output as below:
```

**Output:**
```text
Return Value is c
A =  {'a', 'd', 'b'}
```

>**Note:** You may get different output as **`pop()`** returns and removes a random element.

```python
# Example 2: How pop() works for Python Sets?

set1 = {"Welcome", "to", "Python", "course"}
print(set1.pop())
print(set1)
```

**Output:**
```text
course
{'Welcome', 'to', 'Python'}
```

---

## 📘 Python String Isdecimal()
*Source: `2. Python Datatypes/13. Python String isdecimal().ipynb`*

# Python String `isdecimal()`

The string **`isdecimal()`** method returns **`True`** if all characters in the string are decimal characters. If not, it returns **`False`**.

**Syntax**:

```python
string.isdecimal()
```

## `isdecimal()` Parameters

The **`isdecimal()`** method doesn't take any parameters.

## Return Value from `isdecimal()`

The **`isdecimal()`** returns:

* **`True`** if all characters in the string are decimal characters.
* **`False`** if at least one character is not decimal characters.

```python
# Example 1: Working of isdecimal()

s = "28212"
print(s.isdecimal())

# contains alphabets
s = "32ladk3"
print(s.isdecimal())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())
```

**Output:**
```text
True
False
False
```

**Explanation:**

The superscript and subscripts are considered digit characters but not decimals. If the string contains these characters (usually written using unicode), **`isdecimal()`** returns **`False`**.

Similarly, roman numerals, currency numerators and fractions are considered numeric numbers (usually written using unicode) but not decimals. The **`isdecimal()`** also returns **`False`** in this case.

There are two methods **`isdigit()`** and **`isnumeric()`** that checks whether the string contains digit characters and numeric characters respectively.

```python
# Example 2: String Containing digits and Numeric Characters

s = '23455'
print(s.isdecimal())

#s = '²3455'
s = '\u00B23455'
print(s.isdecimal())

# s = '½'
s = '\u00BD'
print(s.isdecimal())
```

**Output:**
```text
True
False
False
```

---

## 📘 Python Set Symmetric Difference()
*Source: `2. Python Datatypes/14. Python Set symmetric difference().ipynb`*

# Python Set `symmetric_difference()`

The **`symmetric_difference()`** method returns the symmetric difference of two sets.

The symmetric difference of two sets **`A`** and **`B`** is the set of elements that are in either **`A`** or **`B`**, but not in their intersection.

<div>

</div>

Here, set **`B`** is a superset of set **`A`** and **`A`** is a subset of set **`B`**.

**Syntax**:

```python
A.symmetric_difference(B)
```

```python
# Example 1: Working of symmetric_difference()

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

print(A.symmetric_difference(C))
print(B.symmetric_difference(C))
```

**Output:**
```text
{'a', 'e', 'b'}
{'a', 'e', 'b'}
{'a', 'b', 'd', 'c'}
{'e', 'd', 'c'}
```

## Symmetric difference using `^` operator

In Python, we can also find the symmetric difference using the **`^`** operator.

```python
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

print(A ^ B)
print(B ^ A)

print(A ^ A)
print(B ^ B)
```

**Output:**
```text
{'a', 'e', 'b'}
{'a', 'e', 'b'}
set()
set()
```

---

## 📘 Python String Isdigit()
*Source: `2. Python Datatypes/14. Python String isdigit().ipynb`*

# Python String `isdigit()`

The string **`isdigit()`** method returns **`True`** if all characters in the string are digits. If not, it returns **`False`**.

**Syntax**:

```python
string.isdigit()
```

## `isdigit()` Parameters

The **`isdigit()`** method doesn't take any parameters.

## Return Value from `isdigit()`

The **`isdigit()`** returns:

* **`True`** if all characters in the string are digits.
* **`False`** if at least one character is not digits.

```python
# Example 1: Working of isdigit()

s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())
```

**Output:**
```text
True
False
```

**Explanation:**

A digit is a character that has property value:

* **`Numeric_Type = Digit`**
* **`Numeric_Type = Decimal`**

In Python, superscript and subscripts (usually written using unicode) are also considered digit characters. Hence, if the string contains these characters along with decimal characters, **`isdigit()`** returns **`True`**.

The roman numerals, currency numerators and fractions (usually written using unicode) are considered numeric characters but not digits. The **`isdigit()`** returns **`False`** if the string contains these characters.

To check whether a character is a numeric character or not, you can use **isnumeric()** method.

```python
# Example 2: String Containing digits and Numeric Characters

s = '23455'
print(s.isdigit())

#s = '²3455'
# subscript is a digit
s = '\u00B23455'
print(s.isdigit())

# s = '½'
# fraction is not a digit
s = '\u00BD'
print(s.isdigit())
```

**Output:**
```text
True
True
False
```

```python
# Example 3:

s="I Love 3 Python Tutorial"

print(s.isdigit())
s="123" # Only digit in this string
print(s.isdigit())
```

**Output:**
```text
False
True
```

---

## 📘 Python Set Symmetric Difference Update()
*Source: `2. Python Datatypes/15. Python Set symmetric difference update().ipynb`*

# Python Set `symmetric_difference_update()`

The **`symmetric_difference_update()`** method finds the symmetric difference of two sets and updates the set calling it.

The symmetric difference of two sets **`A`** and **`B`** is the set of elements that are in either **`A`** or **`B`**, but not in their intersection.

<div>

</div>

**Syntax**:

```python
A.symmetric_difference_update(B)
```

## Return Value from `symmetric_difference_update()`

The **`symmetric_difference_update()`** returns None (returns nothing). Rather, it updates the set calling it.

```python
# Example: Working of symmetric_difference_update()

A = {'a', 'c', 'd'}
B = {'c', 'd', 'e' }

result = A.symmetric_difference_update(B)

print('A =', A)
print('B =', B)
print('result =', result)
```

**Output:**
```text
A = {'a', 'e'}
B = {'d', 'e', 'c'}
result = None
```

Here, the set **`A`** is updated with the symmetric difference of set **`A`** and **`B`**. However, the set **`B`** is unchanged.

---

## 📘 Python String Isidentifier()
*Source: `2. Python Datatypes/15. Python String isidentifier().ipynb`*

# Python String `isidentifier()`

The string **`isidentifier()`** method returns **`True`**  if the string is a valid identifier in Python. If not, it returns **`False`**.

**Syntax**:

```python
string.isidentifier()
```

## `isidentifier()` Parameters

The **`isidentifier()`** method doesn't take any parameters.

## Return Value from `isidentifier()`

The **`isidentifier()`** returns:

* **`True`** is a valid identifier.
* **`False`** if the string is not a invalid identifier.

```python
# Example 1: How isidentifier() works?

str = 'Python'
print(str.isidentifier())

str = 'Py thon'
print(str.isidentifier())

str = '22Python'
print(str.isidentifier())

str = ''
print(str.isidentifier())
```

**Output:**
```text
True
False
False
False
```

Visit this page to learn what is **[valid identifier in Python?](https://docs.python.org/3.1/reference/lexical_analysis.html#identifiers)**

```python
# Example 2: More Example of isidentifier()

str = 'root33'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')
  
str = '33root'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')
  
str = 'root 33'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')
```

**Output:**
```text
root33 is a valid identifier.
33root is not a valid identifier.
root 33 is not a valid identifier.
```

---

## 📘 Python Set Union()
*Source: `2. Python Datatypes/16. Python Set union().ipynb`*

# Python Set `union()`

The **`union()`** method returns a new set with distinct elements from all the sets.

The union of two or more sets is the set of all distinct elements present in all the sets. For example:

```python
A = {1, 2}
B = {2, 3, 4}
C = {5}

Then,
A∪B = B∪A = {1, 2, 3, 4}
A∪C = C∪A = {1, 2, 5}
B∪C = C∪B = {2, 3, 4, 5}

A∪B∪C = {1, 2, 3, 4, 5}
```

<div>

</div>

**Syntax**:

```python
A.union(*other_sets)
```

>**Note:** **`*`** is not part of the syntax. It is used to indicate that the method can take 0 or more arguments.

## Return Value from `union()`

* The **`union()`** method returns a new set with elements from the set and all other sets (passed as an argument).
* If the argument is not passed to **`union()`**, it returns a shallow copy of the set.

```python
# Example 1: Working of union()

A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}

print('A U B =', A.union(B))
print('B U C =', B.union(C))
print('A U B U C =', A.union(B, C))
print('A.union() =', A.union())
```

**Output:**
```text
A U B = {'a', 2, 'd', 'c'}
B U C = {1, 2, 3, 'd', 'c'}
A U B U C = {1, 'a', 2, 3, 'd', 'c'}
A.union() = {'a', 'd', 'c'}
```

You can also find the union of sets using the **`|`** operator.

```python
# Example 2: Set Union Using the | Operator

A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}

print('A U B =', A| B)
print('B U C =', B | C)
print('A U B U C =', A | B | C)
```

**Output:**
```text
A U B = {'a', 2, 'd', 'c'}
B U C = {1, 2, 3, 'd', 'c'}
A U B U C = {1, 'a', 2, 3, 'd', 'c'}
```

---

## 📘 Python String Islower()
*Source: `2. Python Datatypes/16. Python String islower().ipynb`*

# Python String `islower()`

The string **`islower()`** method returns **`True`** if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns **`False`**.

**Syntax**:

```python
string.islower()
```

## `islower()` Parameters

The **`islower()`** method doesn't take any parameters.

## Return Value from `islower()`

The **`islower()`** returns:

* **`True`** if all alphabets that exist in the string are lowercase alphabets.
* **`False`** if the string contains at least one uppercase alphabet.

```python
# Example 1: Return Value from islower()

s = 'this is good'
print(s.islower())

s = 'th!s is a1so g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())
```

**Output:**
```text
True
True
False
```

```python
# Example 2: How to use islower() in a program?

s = 'this is good'
if s.islower() == True:
    print('Does not contain uppercase letter.')
else:
    print('Contains uppercase letter.')
  
s = 'this is Good'
if s.islower() == True:
    print('Does not contain uppercase letter.')
else:
    print('Contains uppercase letter.')
```

**Output:**
```text
Does not contain uppercase letter.
Contains uppercase letter.
```

```python
# Example:

s="I Love Python 3 Tutorial"

print(s.islower())
p="python"
print(p.islower())
```

**Output:**
```text
False
True
```

---

## 📘 Python Set Update()
*Source: `2. Python Datatypes/17. Python Set update().ipynb`*

# Python Set `update()`

The **`update()`** method returns a new set with distinct elements from all the sets.

**Syntax**:

```python
A.update(iterable)
```

Here, **`A`** is a set, and **`iterable`** can be any iterable such as list, set, dictionary, string, etc. The elements of the iterable are added to the set **`A`**.

Let's take another example:

```python
A.update(iter1, iter2, iter3)
```

Here, the elements of iterables **`iter1`**, **`iter2`**, and **`iter3`** are added to set **`A`**.

## Return Value from `update()`

The **`update()`** method method returns **`None`** (returns nothing).

```python
# Example 1: Python set update()

A = {'a', 'b'}
B = {1, 2, 3}

result = A.update(B)

print('A =', A)
print('result =', result)
```

**Output:**
```text
A = {'a', 1, 2, 3, 'b'}
result = None
```

```python
# Example 2: Add elements of string and dictionary to Set

string_alphabet = 'abc'
numbers_set = {1, 2}

# add elements of the string to the set
numbers_set.update(string_alphabet)

print('numbers_set =', numbers_set)

info_dictionary = {'key': 1, 'lock' : 2}
numbers_set = {'a', 'b'}

# add keys of dictionary to the set
numbers_set.update(info_dictionary)
print('numbers_set =', numbers_set)
```

**Output:**
```text
numbers_set = {1, 2, 'a', 'c', 'b'}
numbers_set = {'a', 'b', 'key', 'lock'}
```

>**Note:** If dictionaries are passed to the **`update()`** method, the keys of the dictionaries are added to the set.

```python
# Example 3: adding multiple elements to a new set

set1 = set() # creating an empty set
set1.update({20, 30.45, "Learn with", "Python"})
print(set1)

#adding multiple elements to an existing set
set2 = {"Welcome", "to", "Python", "course"}
set2.update({20, 30.45, "Hi"})
print(set2)
```

**Output:**
```text
{'Python', 20, 30.45, 'Learn with'}
{'Welcome', 'Hi', 20, 'to', 'course', 30.45, 'Python'}
```

---

## 📘 Python String Isnumeric()
*Source: `2. Python Datatypes/17. Python String isnumeric().ipynb`*

# Python String `isnumeric()`

The string **`isnumeric()`** method returns **`True`** if all characters in a string are numeric characters. If not, it returns **`False`**.

A numeric character has following properties:

* **`Numeric_Type=Decimal`**
* **`Numeric_Type=Digit`**
* **`Numeric_Type=Numeric`**

In Python, decimal characters (like: 0, 1, 2..), digits (like: subscript, superscript), and characters having Unicode numeric value property (like: fraction, roman numerals, currency numerators) are all considered numeric characters.

You can write the digit and numeric characters using unicode in the program. For example:

```python
# s = '½'
>>>s = '\u00BD'
```

**Syntax**:

```python
string.isnumeric()
```

## `isnumeric()` Parameters

The **`isnumeric()`** method doesn't take any parameters.

## Return Value from `isnumeric()`

The **`isnumeric()`** returns:

* **`True`** if all characters in the string are numeric characters.
* **`False`** if at least one character is not a numeric character.

```python
# Example 1: Working of isnumeric()

s = '1242323'
print(s.isnumeric())

#s = '²3455'
s = '\u00B23455'
print(s.isnumeric())

# s = '½'
s = '\u00BD'
print(s.isnumeric())

s = '1242323'
s='python12'
print(s.isnumeric())
```

**Output:**
```text
True
True
True
False
```

```python
# Example 2: How to use isnumeric()?
    
#s = '²3455'
s = '\u00B23455'

if s.isnumeric() == True:
    print('All characters are numeric.')
else:
    print('All characters are not numeric.')
```

**Output:**
```text
All characters are numeric.
```

```python
# Example 3:

str = "helloworld99"

print (str.isnumeric())
str = "10121997"
print (str.isnumeric())
```

**Output:**
```text
False
True
```

---

## 📘 Python String Isprintable()
*Source: `2. Python Datatypes/18. Python String isprintable().ipynb`*

# Python String `isprintable()`

The string **`isprintable()`** method returns **`True`** if all characters in a string are printable or the string is empty. If not, it returns **`False`**.

Characters that occupy printing space on the screen are known as printable characters. For example:

1. letters and symbols
2. digits
3. punctuation
4. whitespace

**Syntax**:

```python
string.isprintable()
```

## `isprintable()` Parameters

The **`isprintable()`** method doesn't take any parameters.

## Return Value from `isprintable()`

The **`isprintable()`** returns:

* **`True`** if all characters in the string are printable.
* **`False`** if the string contains at least one non-printable character.

```python
# Example 1: Working of isprintable()

s = 'Space is a printable'
print(s)
print(s.isprintable())

s = '\nNew Line is printable'
print(s)
print(s.isprintable())

s = ''
print('\nEmpty string printable?', s.isprintable())
```

**Output:**
```text
Space is a printable
True

New Line is printable
False

Empty string printable? True
```

```python
# Example 2: How to use isprintable()?

# written using ASCII
# chr(27) is escape character
# char(97) is letter 'a'
s = chr(27) + chr(97)

if s.isprintable() == True:
    print('Printable')
else:
    print('Not Printable')
  
s = '2+2 = 4'

if s.isprintable() == True:
    print('Printable')
else:
    print('Not Printable')
```

**Output:**
```text
Not Printable
Printable
```

---

## 📘 Python String Isspace()
*Source: `2. Python Datatypes/19. Python String isspace().ipynb`*

# Python String `isspace()`

The string **`isspace()`** method returns **`True`** if there are only whitespace characters in the string. If not, it returns **`False`**.

Characters that are used for spacing are called whitespace characters. For example: 

1. tabs
2. spaces 
3. newline, etc.

**Syntax**:

```python
string.isspace()
```

## `isspace()` Parameters

The **`isspace()`** method doesn't take any parameters.

## Return Value from `isspace()`

The **`isspace()`** returns:

* **`True`** if all characters in the string are whitespace characters.
* **`False`** if the string is empty or contains at least one non-printable character.

```python
# Example 1: Working of isspace()

s = '   \t'
print(s.isspace())

s = ' a '
print(s.isspace())

s = ''
print(s.isspace())
```

**Output:**
```text
True
False
False
```

```python
# Example 2: How to use isspace()?

s = '\t  \n'
if s.isspace() == True:
    print('All whitespace characters')
else:
    print('Contains non-whitespace characters')
  
s = '2+2 = 4'

if s.isspace() == True:
    print('All whitespace characters')
else:
    print('Contains non-whitespace characters.')
```

**Output:**
```text
All whitespace characters
Contains non-whitespace characters.
```

```python
# Example 3:

str = " "

print (str.isspace())
str = "helloworld"
print (str.isspace())
```

**Output:**
```text
True
False
```

---

## 📘 Python String Istitle()
*Source: `2. Python Datatypes/20. Python String istitle().ipynb`*

# Python String `istitle()`

The string **`istitle()`** method returns **`True`** if the string is a titlecased string. If not, it returns **`False`**.

**Syntax**:

```python
string.istitle()
```

## `istitle()` Parameters

The **`istitle()`** method doesn't take any parameters.

## Return Value from `istitle()`

The **`istitle()`** returns:

* **`True`** if the string is a titlecased string.
* **`False`** if the string is not a titlecased string or an empty string.

```python
# Example 1: Working of istitle()

s = 'Python Is Good.'
print(s.istitle())

s = 'Python is good'
print(s.istitle())

s = 'This Is @ Symbol.'
print(s.istitle())

s = '99 Is A Number'
print(s.istitle())

s = 'PYTHON'
print(s.istitle())
```

**Output:**
```text
True
False
True
True
False
```

```python
# Example 2: How to use istitle()?

s = 'I Love Python.'
if s.istitle() == True:
    print('Titlecased String')
else:
    print('Not a Titlecased String')
  
s = 'PYthon'
if s.istitle() == True:
    print('Titlecased String')
else:
    print('Not a Titlecased String')
```

**Output:**
```text
Titlecased String
Not a Titlecased String
```

```python
# Example 3:

s1='I Love Python Tutorial'

print(s1.istitle())
s2='I love python 3'
print(s2.istitle())
```

**Output:**
```text
True
False
```

---

## 📘 Python String Isupper()
*Source: `2. Python Datatypes/21. Python String isupper().ipynb`*

# Python String `isupper()`

The string **`isupper()`** method returns **`True`** if all alphabets in a string are uppercase alphabets. If the string contains at least one lowercase alphabet, it returns **`False`**.

**Syntax**:

```python
string.isupper()
```

## `isupper()` Parameters

The **`isupper()`** method doesn't take any parameters.

## Return Value from `isupper()`

The **`isupper()`** returns:

* **`True`** if all characters in a string are uppercase characters.
* **`False`**  if any characters in a string are lowercase characters.

```python
# Example 1: Return value of isupper()

# example string
string = "THIS IS GOOD!"
print(string.isupper());

# numbers in place of alphabets
string = "THIS IS ALSO G00D!"
print(string.isupper());

# lowercase string
string = "THIS IS not GOOD!"
print(string.isupper());
```

**Output:**
```text
True
True
False
```

```python
# Example 2: How to use isupper() in a program?

string = 'THIS IS GOOD'
if string.isupper() == True:
    print('Does not contain lowercase letter.')
else:
    print('Contains lowercase letter.')

string = 'THIS IS gOOD'
if string.isupper() == True:
    print('Does not contain lowercase letter.')
else:
    print('Contains lowercase letter.')
```

**Output:**
```text
Does not contain lowercase letter.
Contains lowercase letter.
```

---

## 📘 Python String Join()
*Source: `2. Python Datatypes/22. Python String join().ipynb`*

# Python String `join()`

The string **`join()`** method returns a string by joining all the elements of an iterable, separated by a string separator.

The **`join()`** method provides a flexible way to create strings from iterable objects. It joins each element of an iterable (such as list, string, and tuple) by a string separator (the string on which the **`join()`** method is called) and returns the concatenated string.

**Syntax**:

```python
string.join(iterable)
```

## `join()` Parameters

The **`join()`** takes an iterable (objects capable of returning its members one at a time) as its parameter.

Some of the example of iterables are:

* **Native data types** - **List**, **Tuple**, **String**, **Dictionary** and **Set**.
* File objects and objects you define with an `**__ iter __()**` or **`__getitem()__`** method.

## Return Value from `join()` method

The **`join()`** returns a string created by joining the elements of an iterable by string separator.

If the iterable contains any non-string values, it raises a **`TypeError`** exception.

```python
# Example 1: Working of the join() method

# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))

s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))
```

**Output:**
```text
1, 2, 3, 4
1, 2, 3, 4
s1.join(s2): 1abc2abc3
s2.join(s1): a123b123c
```

```python
# Example 2: The join() method with sets

# .join() with sets
test = {'2', '1', '3'}
s = ', '
print(s.join(test))

test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))
```

**Output:**
```text
1, 3, 2
Python->->Ruby->->Java
```

>**Note:** A set is an unordered collection of items, so you may get different output (order is random).

```python
# Example 3: The join() method with dictionaries

# .join() with dictionaries
test = {'mat': 1, 'that': 2}
s = '->'

# joins the keys only
print(s.join(test))

test = {1: 'mat', 2: 'that'}
s = ', '

# this gives error since key isn't string
print(s.join(test))
```

**Output:**
```text
mat->that
```

**Explanation:** 

The **`join()`** method tries to join the keys (not values) of the dictionary with the string separator.

>**Note:** If the key of the string is not a string, it raises a TypeError exception.

---

## 📘 Python String Ljust()
*Source: `2. Python Datatypes/23. Python String ljust().ipynb`*

# Python String `ljust()`

The string **`ljust()`** method returns a left-justified string of a given minimum width.

**Syntax**:

```python
string.ljust(width[, fillchar])
```

>**Note:** Here, **`fillchar`** is an optional parameter.

## `ljust()` Parameters

The **`ljust()`** method takes two parameters:

* **`width`** - width of the given string. If width is less than or equal to the length of the string, the original string is returned.

* **`fillchar`** (Optional) - character to fill the remaining space of the width

## Return Value from `ljust()`

The **`ljust()`** method returns the left-justified string within the given minimum **`width`**.

If **`fillchar`** is defined, it also fills the remaining space with the defined character.

```python
# Example 1: Left justify string of minimum width

# example string
string = 'cat'
width = 5

# print left justified string
print(string.ljust(width))
```

**Output:**
```text
cat
```

**Explanation:**

Here, the minimum **`width`** defined is 5. So, the resultant string is of minimum length 5.

And, the string **`cat`** is aligned to the left which makes leaves two spaces on the right of the word.

```python
# Example 2: Left justify string and fill the remaining spaces

# example string
string = 'cat'
width = 5
fillchar = '*'

# print left justified string
print(string.ljust(width, fillchar))
```

**Output:**
```text
cat**
```

**Explanation:**

Here, the string **`cat`** is aligned to the left, and the remaining two spaces on the right is filled with the character **`*`**.

>**Note:** If you want to right justify the string, use **rjust()**. You can also use **format()** method for the formatting of strings.

---

## 📘 Python String Rjust()
*Source: `2. Python Datatypes/24. Python String rjust().ipynb`*

# Python String `rjust()`

The string **`rjust()`** method returns a right-justified string of a given minimum width.

**Syntax**:

```python
string.rjust(width[, fillchar])
```

>**Note:** Here, **`fillchar`** is an optional parameter.

## `rjust()` Parameters

The **`ljust()`** method takes two parameters:

* **`width`** - width of the given string. If width is less than or equal to the length of the string, the original string is returned.

* **`fillchar`** (Optional) - character to fill the remaining space of the width

## Return Value from `rjust()`

The **`rjust()`** method returns the right-justified string within the given minimum **`width`**.

If **`fillchar`** is defined, it also fills the remaining space with the defined character.

```python
# Example 1: Right justify string of minimum width

# example string
string = 'cat'
width = 5

# print right justified string
print(string.rjust(width))
```

**Output:**
```text
cat
```

**Explanation:**

Here, the minimum **`width`** defined is 5. So, the resultant string is at least of length 5.

Now, **`rjust()`** aligns the string **`cat`** to the right leaving two spaces to the left of the word.

```python
# Example 2: Right justify string and fill the remaining spaces

# example string
string = 'cat'
width = 5
fillchar = '*'

# print right justified string
print(string.rjust(width, fillchar))
```

**Output:**
```text
**cat
```

**Explanation:**

Here, the string **`cat`** is aligned to the right, and the remaining two spaces on the left is filled with the character **`*`**.

>**Note:** If you want to right justify the string, use **ljust()**. You can also use **format()** method for the formatting of strings.

---

## 📘 Python String Lower()
*Source: `2. Python Datatypes/25. Python String lower().ipynb`*

# Python String `lower()`

The string **`lower()`** method converts all uppercase characters in a string into lowercase characters and returns it.

**Syntax**:

```python
string.lower()
```

## `lower()` Parameters

The **`lower()`** method doesn't take any parameters.

## Return Value from `lower()`

The **`lower()`** method returns the lowercased string from the given string. It converts all uppercase characters to lowercase.

If no uppercase characters exist, it returns the original string.

```python
# Example 1: Convert a string to lowercase

# example string
string = "THIS SHOULD BE LOWERCASE!"
print(string.lower())

# string with numbers
# all alphabets whould be lowercase
string = "Th!s Sh0uLd B3 L0w3rCas3!"
print(string.lower())
```

**Output:**
```text
this should be lowercase!
th!s sh0uld b3 l0w3rcas3!
```

```python
# Example 2: How lower() is used in a program?

# first string
firstString = "PYTHON IS AWESOME!"

# second string
secondString = "PyThOn Is AwEsOmE!"

if(firstString.lower() == secondString.lower()):
    print("The strings are same.")
else:
    print("The strings are not same.")
```

**Output:**
```text
The strings are same.
```

>**Note:** Note: If you want to convert to uppercase string, use **upper()**. You can also use **swapcase()** to swap between lowercase to uppercase.

---

## 📘 Python String Upper()
*Source: `2. Python Datatypes/26. Python String upper().ipynb`*

# Python String `upper()`

The string **`upper()`** method converts all lowercase characters in a string into uppercase characters and returns it.

**Syntax**:

```python
string.upper()
```

## `upper()` Parameters

The **`upper()`** method doesn't take any parameters.

## Return Value from `upper()`

The **`upper()`** method returns the uppercased string from the given string. It converts all lowercase characters to uppercase.

If no lowercase characters exist, it returns the original string.

```python
# Example 1: Convert a string to uppercase

# example string
string = "this should be uppercase!"
print(string.upper())

# string with numbers
# all alphabets whould be lowercase
string = "Th!s Sh0uLd B3 uPp3rCas3!"
print(string.upper())
```

**Output:**
```text
THIS SHOULD BE UPPERCASE!
TH!S SH0ULD B3 UPP3RCAS3!
```

```python
# Example 2: How upper() is used in a program?

# first string
firstString = "python is awesome!"

# second string
secondString = "PyThOn Is AwEsOmE!"

if(firstString.upper() == secondString.upper()):
    print("The strings are same.")
else:
    print("The strings are not same.")
```

**Output:**
```text
The strings are same.
```

>**Note:** Note: If you want to convert to lowercase string, use **lower()**. You can also use **swapcase()** to swap between uppercase to lowercase.

---

## 📘 Python String Swapcase()
*Source: `2. Python Datatypes/27. Python String swapcase().ipynb`*

# Python String `swapcase()`

The string **`swapcase()`** method converts all uppercase characters to lowercase and all lowercase characters to uppercase characters of the given string, and returns it.

**Syntax**:

```python
string.swapcase()
```

>**Note:** Not necessarily, **`string.swapcase().swapcase() == string`**

## `swapcase()` Parameters

The **`swapcase()`** method doesn't take any parameters.

## Return Value from `swapcase()`

The **`swapcase()`** method returns the string where all uppercase characters are converted to lowercase, and lowercase characters are converted to uppercase.

```python
# Example 1: Swap lowercase to uppercase and vice versa using swapcase()

# example string
string = "THIS SHOULD ALL BE LOWERCASE."
print(string.swapcase())

string = "this should all be uppercase."
print(string.swapcase())

string = "ThIs ShOuLd Be MiXeD cAsEd."
print(string.swapcase())
```

**Output:**
```text
this should all be lowercase.
THIS SHOULD ALL BE UPPERCASE.
tHiS sHoUlD bE mIxEd CaSeD.
```

>**Note:** If you want to convert string to lowercase only, use **lower()**. Likewise, if you want to convert string to uppercase only, use **upper()**.

---

## 📘 Python String Lstrip()
*Source: `2. Python Datatypes/28. Python String lstrip().ipynb`*

# Python String `lstrip()`

The string **`lstrip()`** method returns a copy of the string with leading characters removed (based on the string argument passed).

The **`lstrip()`** removes characters from the left based on the argument (a string specifying the set of characters to be removed).

**Syntax**:

```python
string.lstrip([chars])
```

## `lstrip()` Parameters

The **`lstrip()`** method takes one parameter:

* **`chars`** (optional) - a string specifying the set of characters to be removed.

If **`chars`** argument is not provided, all leading whitespaces are removed from the string.

## Return Value from `lstrip()`

The **`lstrip()`** method returns a copy of the string with leading characters stripped.

All combinations of characters in the **`chars`** argument are removed from the left of the string until the first mismatch.

```python
# Example 1: Working of lstrip()

random_string = '   this is good '

# Leading whitepsace are removed
print(random_string.lstrip())

# Argument doesn't contain space
# No characters are removed.
print(random_string.lstrip('sti'))

print(random_string.lstrip('s ti'))

website = 'https://www.github.com/' 
print(website.lstrip('htps:/.'))
```

**Output:**
```text
this is good 
   this is good 
his is good 
www.github.com/
```

```python
# Example 2:

s1=' I Love Python Tutorial '
print(s1.lstrip())

s2='###HelloWorld###'
print(s2.lstrip('#'))
```

**Output:**
```text
I Love Python Tutorial 
HelloWorld###
```

---

## 📘 Python String Rstrip()
*Source: `2. Python Datatypes/29. Python String rstrip().ipynb`*

# Python String `rstrip()`

The string **`rstrip()`** method returns a copy of the string with trailing characters removed (based on the string argument passed).

The **`rstrip()`** removes characters from the right based on the argument (a string specifying the set of characters to be removed).

**Syntax**:

```python
string.rstrip([chars])
```

## `rstrip()` Parameters

The **`rstrip()`** method takes one parameter:

* **`chars`** (optional) - a string specifying the set of characters to be removed.

If **`chars`** argument is not provided, all leading whitespaces on the right are removed from the string.

## Return Value from `rstrip()`

The **`rstrip()`** method returns a copy of the string with trailing characters stripped.

All combinations of characters in **`chars`** argument are removed from the right of the string until first mismatch.

```python
# Example 1: Working of rstrip()

random_string = 'this is good    '

# Trailing whitepsace are removed
print(random_string.rstrip())

# Argument doesn't contain 'd'
# No characters are removed.
print(random_string.rstrip('si oo'))

print(random_string.rstrip('sid oo'))

website = 'www.github.com/'
print(website.rstrip('m/.'))
```

**Output:**
```text
this is good
this is good
this is g
www.github.co
```

```python
# Example 2:

s1=' I Love Python Tutorial '
print(s1.rstrip())

s2='###HelloWorld###'
print(s2.rstrip('#'))
```

**Output:**
```text
I Love Python Tutorial
###HelloWorld
```

---

## 📘 Python String Strip()
*Source: `2. Python Datatypes/30. Python String strip().ipynb`*

# Python String `strip()`

The string **`strip()`** method returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed).

The **`strip()`** method removes characters from both left and right based on the argument (a string specifying the set of characters to be removed).

**Syntax**:

```python
string.strip([chars])
```

## `strip()` Parameters

The **`strip()`** method takes one parameter:

* **`chars`** (optional) - a string specifying the set of characters to be removed from the left and right part of the string.

If **`chars`** argument is not provided, all leading and trailing whitespaces are removed from the string.

## Return Value from `strip()`

The **`strip()`** method returns a copy of the string with both leading and trailing characters stripped.

## Working of the `strip()` method

* When the character of the string in the left mismatches with all the characters in the **`chars`** argument, it stops removing the leading characters.
* Similarly, when the character of the string in the right mismatches with all the characters in the **`chars`** argument, it stops removing the trailing characters.

```python
# Example 1: Working of the strip() method

string = '  xoxo love xoxo   '

# Leading and trailing whitespaces are removed
print(string.strip())

# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' xoe'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))

string = 'android is awesome'
print(string.strip('an'))
```

**Output:**
```text
xoxo love xoxo
lov
  xoxo love xoxo   
droid is awesome
```

**Explanation:** 

Here, we can see that the first expression **`string.strip()`** without any arguments removed the whitespaces from the left and right of **`string`**.

**`string.strip(' xoe')`** removed all whitespace, **`x`**, **`o`**, and **`e`** that lead or trailed the string.

Since **`string`** has whitespace at the beginning and end, the expression **`string.strip('stx')`** does not change the string. **`x`** is not removed since it is at the middle of the string (whitespaces lead and trail the string)

**`string.strip('an')`** removed **`an`** leading the string.

---

## 📘 Python String Partition()
*Source: `2. Python Datatypes/31. Python String partition().ipynb`*

# Python String `partition()`

The string **`partition()`** method splits the string at the first occurrence of the argument string and returns a tuple containing the part the before separator, argument string and the part after the separator.

**Syntax**:

```python
string.partition(separator)
```

## `partition()` Parameters

The **`partition()`** method takes a string parameter **`separator`** that separates the string at the first occurrence of it.

## Return Value from `partition()`

The **`partition()`** method returns a 3-tuple containing:

* the part before the separator, separator parameter, and the part after the separator if the separator parameter is found in the string.
* the string itself and two empty strings if the separator parameter is not found.

```python
# Example 1: How partition() works?

string = "Python is fun"

# 'is' separator is found
print(string.partition('is '))

# 'not' separator is not found
print(string.partition('not '))

string = "Python is fun, isn't it"

# splits at first occurence of 'is'
print(string.partition('is'))
```

**Output:**
```text
('Python ', 'is ', 'fun')
('Python is fun', '', '')
('Python ', 'is', " fun, isn't it")
```

---

## 📘 Python String Maketrans()
*Source: `2. Python Datatypes/32. Python String maketrans().ipynb`*

# Python String `maketrans()`

The string **`maketrans()`** method returns a mapping table for translation usable for **`translate()`** method.

In simple terms, **`maketrans()`** method is a static method that creates a one to one mapping of a character to its translation/replacement.

It creates a Unicode representation of each character for translation.

This translation mapping is then used for replacing a character to its mapped character when used in **translate()** method.

**Syntax**:

```python
string.maketrans(x[, y[, z]])
```

>**Note:** Here, **`y`** and **`z`** are optional arguments.

## `maketrans()` Parameters

The **`maketrans()`** method takes 3 parameters:

* **`x`** - If only one argument is supplied, it must be a dictionary. The dictionary should contain a 1-to-1 mapping from a single character string to its translation OR a Unicode number (97 for 'a') to its translation.


* **`y`** - If two arguments are passed, it must be two strings with equal length. Each character in the first string is a replacement to its corresponding index in the second string.


* **`z`** - If three arguments are passed, each character in the third argument is mapped to None.

## Return Value from `maketrans()`

The **`maketrans()`** method returns a translation table with a 1-to-1 mapping of a Unicode ordinal to its translation/replacement.

```python
# Example 1: Translation table using a dictionary with maketrans()

# example dictionary
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))

# example dictionary
dict = {97: "123", 98: "456", 99: "789"}
string = "abc"
print(string.maketrans(dict))
```

**Output:**
```text
{97: '123', 98: '456', 99: '789'}
{97: '123', 98: '456', 99: '789'}
```

**Explanation:**

Here, a dictionary **`dict`** is defined. It contains a mapping of characters a,b and c to 123, 456, and 789 respectively.

**`maketrans()`** creates a mapping of the character's Unicode ordinal to its corresponding translation.

So, 97 ('**`a`**') is mapped to '123', 98 '**`b`**' to 456 and 99 '**`c`**' to 789. This can be demonstrated from the output of both dictionaries.

Also, if two or more characters are mapped in the dictionary, it raises an exception.

```python
# Example 2: Translation table using two strings with maketrans()

# first string
firstString = "abc"
secondString = "def"
string = "abc"
print(string.maketrans(firstString, secondString))

# example dictionary
firstString = "abc"
secondString = "defghi"
string = "abc"
print(string.maketrans(firstString, secondString))
```

**Output:**
```text
{97: 100, 98: 101, 99: 102}
```

**Explanation:**

Here first, two strings of equal length **`abc`** and **`def`** are defined. And the corresponding translation is created.

Printing only the first translation gives you a 1-to-1 mapping to each character's Unicode ordinal in **`firstString`** to the same indexed character on **`secondString`**.

In this case, 97 ('**`a`**') is mapped to 100 ('**`d`**'), 98 ('**`b`**') to 101 ('**`e`**') and 99 ('**`c`**') to 102 ('**`f`**').

Trying to create a translation table for unequal length strings raises a **`ValueError`** exception indicating that the strings must have equal length.

```python
# Example 3: Translational table with removable string with maketrans()

# first string
firstString = "abc"
secondString = "def"
thirdString = "abd"
string = "abc"
print(string.maketrans(firstString, secondString, thirdString))
```

**Output:**
```text
{97: None, 98: None, 99: 102, 100: None}
```

**Explanation:**

Here, first, the mapping between the two strings **`firstString`** and **`secondString`** are created.

Then, the third argument **`thirdString`** resets the mapping of each character in it to **`None`** and also creates a new mapping for non-existent characters.

In this case, **`thirdString`** resets the mapping of 97 ('**`a`**') and 98 ('**`b`**') to **`None`**, and also creates a new mapping for 100 ('**`d`**') mapped to **`None`**.

---

## 📘 Python String Rpartition()
*Source: `2. Python Datatypes/33. Python String rpartition().ipynb`*

# Python String `rpartition()`

The string **`rpartition()`** method splits the string at the last occurrence of the argument string and returns a tuple containing the part the before separator, argument string and the part after the separator.

**Syntax**:

```python
string.rpartition(separator)
```

## `rpartition()` Parameters

The **`rpartition()`** method takes a string parameter **`separator`** that separates the string at the last occurrence of it.

## Return Value from `rpartition()`

The **`rpartition()`** method returns a 3-tuple containing:

* the part before the separator, separator parameter, and the part after the separator if the separator parameter is found in the string
* two empty strings, followed by the string itself if the separator parameter is not found

```python
# Example 1: How rpartition() works?

string = "Python is fun"

# 'is' separator is found
print(string.rpartition('is '))

# 'not' separator is not found
print(string.rpartition('not '))

string = "Python is fun, isn't it"

# splits at last occurence of 'is'
print(string.rpartition('is'))
```

**Output:**
```text
('Python ', 'is ', 'fun')
('', '', 'Python is fun')
('Python is fun, ', 'is', "n't it")
```

---

## 📘 Python String Translate()
*Source: `2. Python Datatypes/34. Python String translate().ipynb`*

# Python String `translate()`

The string **`translate()`** method returns a string where each character is mapped to its corresponding character in the translation table.

**`translate()`** method takes the translation table to replace/translate characters in the given string as per the mapping table.

The translation table is created by the static method **maketrans()**.

**Syntax**:

```python
string.translate(table)
```

## `translate()` Parameters

The **`translate()`** method takes a single parameter:

* **`table`** - a translation table containing the mapping between two characters; usually created by **`maketrans()`**.

## Return Value from `translate()`

The **`translate()`** method returns a string where each character is mapped to its corresponding character as per the translation table.

```python
# Example 1: Translation/Mapping using a translation table with translate()

# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))
```

**Output:**
```text
Original string: abcdef
Translated string: idef
```

**Explanation:**

Here, the translation mapping **`translate()`** contains the mapping from **`a`**, **`b`** and **`c`** to **`g`**, **`h`** and **`i`** respectively.

But, the removal string **`thirdString`** resets the mapping to **`a`** and **`b`** to **`None`**.

So, when the string is translated using **`translate()`**, **`a`** and **`b`** are removed, and **`c`** is replaced **`i`** outputting **`idef`**.

>**Note:** If you cannot understand what's going inside **`maketrans()`**, please refer to **String maketrans()**.

```python
# Example 2: Translation/Mapping with translate() with manual translation table

# translation table - a dictionary
translation = {97: None, 98: None, 99: 105}

string = "abcdef"
print("Original string:", string)

# translate string
print("Translated string:", string.translate(translation))
```

**Output:**
```text
Original string: abcdef
Translated string: idef
```

**Explanation:**

Here, we don't create a translation table from **`maketrans()`** but, we manually create the mapping dictionary **`translation`**.

This translation is then used to translate **`string`** to get the same output as the previous example.

---

## 📘 Python String Replace()
*Source: `2. Python Datatypes/35. Python String replace().ipynb`*

# Python String `replace()`

The string **`replace()`** method returns a copy of the string where all occurrences of a substring is replaced with another substring.

**Syntax**:

```python
str.replace(old, new [, count]) 
```

## `replace()` Parameters

The **`replace()`** method can take maximum of 3 parameters:

* **`old`** - old substring you want to replace
* **`new`** - new substring which will replace the old substring
* **`count`** (optional) - the number of times you want to replace the **`old`** substring with the **`new`** substring

>**Note:** If **`count`** is not specified, the **`replace()`** method replaces all occurrences of the **`old`** substring with the **`new`** substring.

## Return Value from `replace()`

The **`replace()`** method returns a copy of the string where the **`old`** substring is replaced with the **`new`** substring. The original string is unchanged.

If the **`old`** substring is not found, it returns the copy of the original string.

```python
# Example 1: Using replace()

song = 'cold, cold heart'

# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurences of 'let'
print(song.replace('let', "don't let", 2))
```

**Output:**
```text
hurt, hurt heart
Let it be, don't let it be, don't let it be, let it be
```

```python
# Example 2: Using replace()

song = 'cold, cold heart'
replaced_song = song.replace('o', 'e')

# The original string is unchanged
print('Original string:', song)

print('Replaced string:', replaced_song)

song = 'let it be, let it be, let it be'

# maximum of 0 substring is replaced
# returns copy of the original string
print(song.replace('let', 'so', 0))
```

**Output:**
```text
Original string: cold, cold heart
Replaced string: celd, celd heart
let it be, let it be, let it be
```

```python
# Example 3:

s1='I Love Python Tutorial, I Love Life, I Love Coding'
print(s1.replace('Love','Like'))
print(s1.replace('I','He',2))
```

**Output:**
```text
I Like Python Tutorial, I Like Life, I Like Coding
He Love Python Tutorial, He Love Life, I Love Coding
```

---

## 📘 Python String Rfind()
*Source: `2. Python Datatypes/36. Python String rfind().ipynb`*

# Python String `rfind()`

The string **`rfind()`** method returns the highest index of the substring (if found). If not found, it returns -1.

**Syntax**:

```python
str.rfind(sub[, start[, end]] )
```

## `rfind()` Parameters

The **`rfind()`** method takes a maximum of three parameters:

* **`sub`** - It's the substring to be searched in the **`str`** string.
* **`start`** and **`end`** (optional) - substring is searched within **`str[start:end]`**

## Return Value from `rfind()`

The **`rfind()`** method method returns an integer value.

* If substring exists inside the string, it returns the highest index where substring is found.
* If substring doesn't exist inside the string, it returns -1.

<div>

</div>

```python
# Example 1: rfind() With No start and end Argument

quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it':", result)

result = quote.rfind('small')
print("Substring 'small ':", result)

result = quote.rfind('be,')
if  (result != -1):
    print("Highest index where 'be,' occurs:", result)
else:
    print("Doesn't contain substring")
```

**Output:**
```text
Substring 'let it': 22
Substring 'small ': -1
Highest index where 'be,' occurs: 18
```

```python
# Example 2: rfind() With start and end Arguments

quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.rfind('things', 10))

# Substring is searched in ' small things with great love' 
print(quote.rfind('t', 2))

# Substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.rfind('th', 6, 20))
```

**Output:**
```text
-1
25
-1
18
```

---

## 📘 Python String Rindex()
*Source: `2. Python Datatypes/37. Python String rindex().ipynb`*

# Python String `rindex()`

The string **`rindex()`** method returns the highest index of the substring inside the string (if found). If the substring is not found, it raises an exception.

**Syntax**:

```python
str.rindex(sub[, start[, end]] )
```

## `rindex()` Parameters

The **`rindex()`** method takes three parameters:

* **`sub`** - It's the substring to be searched in the **`str`** string.
* **`start`** and **`end`** (optional) - substring is searched within **`str[start:end]`**

## Return Value from `rindex()`

* If substring exists inside the string, it returns the highest index in the string where the substring is found.
* If substring doesn't exist inside the string, it raises a **`ValueError`** exception.

**`rindex()`** method is similar to **rfind() method for strings**.

The only difference is that **`rfind()`** returns **`-1`** if the substring is not found, whereas **`rindex()`** throws an exception.

```python
# Example 1: rindex() With No start and end Argument

quote = 'Let it be, let it be, let it be'

result = quote.rindex('let it')
print("Substring 'let it':", result)
  
result = quote.rindex('small')
print("Substring 'small ':", result)
```

**Output:**
```text
Substring 'let it': 22
```

>**Note:** Index in Python starts from 0 and not 1.

```python
# Example 2: rindex() With start and end Arguments

quote = 'Do small things with great love'

# Substring is searched in ' small things with great love' 
print(quote.rindex('t', 2))

# Substring is searched in 'll things with'
print(quote.rindex('th', 6, 20))

# Substring is searched in 'hings with great lov'
print(quote.rindex('o small ', 10, -1))
```

**Output:**
```text
25
18
```

---

## 📘 Python String Split()
*Source: `2. Python Datatypes/38. Python String split().ipynb`*

# Python String `split()`

The string **`split()`** method breaks up a string at the specified separator and returns a list of strings.

**Syntax**:

```python
str.split([separator [, maxsplit]])
```

## `split()` Parameters

The **`split()`** method takes a maximum of 2 parameters:

* **`separator`** (optional)- It is a delimiter. The string splits at the specified **`separator`**.
If the **`separator`** is not specified, any whitespace (space, newline etc.) string is a separator.

* **`maxsplit`** (optional) - The **`maxsplit`** defines the maximum number of splits.
The default value of **`maxsplit`** is -1, meaning, no limit on the number of splits.

## Return Value from `split()`

The **`split()`** method breaks the string at the **`separator`** and returns a list of strings.

```python
# Example 1: How split() works in Python?

text= 'Love thy neighbor'

# splits at space
print(text.split())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.split(', '))

# Splitting at ':'
print(grocery.split(':'))
```

**Output:**
```text
['Love', 'thy', 'neighbor']
['Milk', 'Chicken', 'Bread']
['Milk, Chicken, Bread']
```

```python
# Example 2: How split() works when maxsplit is specified?

grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.split(', ', 2))

# maxsplit: 1
print(grocery.split(', ', 1))

# maxsplit: 5
print(grocery.split(', ', 5))

# maxsplit: 0
print(grocery.split(', ', 0))
```

**Output:**
```text
['Milk', 'Chicken', 'Bread, Butter']
['Milk', 'Chicken, Bread, Butter']
['Milk', 'Chicken', 'Bread', 'Butter']
['Milk, Chicken, Bread, Butter']
```

>**Note:** If **`maxsplit`** is specified, the list will have the maximum of **`maxsplit+1`** items.

---

## 📘 Python String Rsplit()
*Source: `2. Python Datatypes/39. Python String rsplit().ipynb`*

# Python String `rsplit()`

The string **`rsplit()`** method splits string from the right at the specified separator and returns a list of strings.

**Syntax**:

```python
str.rsplit([separator [, maxsplit]])
```

## `rsplit()` Parameters

The **`rsplit()`** method takes a maximum of 2 parameters:

* **`separator`** (optional)- It is a delimiter. **`rsplit()`** method splits string starting from the right at the specified **`separator`**.
If the **`separator`** is not specified, any whitespace (space, newline etc.) string is a separator.

* **`maxsplit`** (optional) - The **`maxsplit`** defines the maximum number of splits.
The default value of **`maxsplit`** is -1, meaning, no limit on the number of splits.

## Return Value from `rsplit()`

The **`rsplit()`** method breaks the string at the **`separator`** starting from the right and returns a list of strings.

```python
# Example 1: How rsplit() works in Python?

text= 'Love thy neighbor'

# splits at space
print(text.rsplit())

grocery = 'Milk, Coffee, Bread'

# splits at ','
print(grocery.rsplit(', '))

# Splitting at ':'
print(grocery.rsplit(':'))
```

**Output:**
```text
['Love', 'thy', 'neighbor']
['Milk', 'Coffee', 'Bread']
['Milk, Coffee, Bread']
```

>**Note:** When **`maxsplit`** is not specified, **`rsplit()`** behaves like **`split()`**.

```python
# Example 2: How split() works when maxsplit is specified?

grocery = 'Milk, Coffee, Bread, Butter'

# maxsplit: 2
print(grocery.rsplit(', ', 2))

# maxsplit: 1
print(grocery.rsplit(', ', 1))

# maxsplit: 5
print(grocery.rsplit(', ', 5))

# maxsplit: 0
print(grocery.rsplit(', ', 0))
```

**Output:**
```text
['Milk, Coffee', 'Bread', 'Butter']
['Milk, Coffee, Bread', 'Butter']
['Milk', 'Coffee', 'Bread', 'Butter']
['Milk, Coffee, Bread, Butter']
```

>**Note:** If **`maxsplit`** is specified, the list will have the maximum of **`maxsplit+1`** items.

---

## 📘 Python String Splitlines()
*Source: `2. Python Datatypes/40. Python String splitlines().ipynb`*

# Python String `splitlines()`

The string **`splitlines()`** method splits the string at line breaks and returns a list of lines in the string.

**Syntax**:

```python
str.splitlines([keepends])
```

## `splitlines()` Parameters

The **`splitlines()`** method takes maximum of 1 parameter:

* **`keepends`** (optional)- If **`keepends`** is provided and **`True`**, line breaks are also included in items of the list.

By default, the line breaks are not included.

## Return Value from `splitlines()`

The **`splitlines()`** method returns a list of lines in the string.

If there are not line break characters, it returns a list with a single item (a single line).

| Representation | Description |
|:----| :--- |
| **`\n`**               | **Line Feed** | 
| **`\r`**               | **Carriage Return** | 
| **`\r\n`**             | **Carriage Return + Line Feed** | 
| **`\v`** or **`\x0b`** | **Line Tabulation** | 
| **`\f`** or **`\x0c`** | **Form Feed** | 
| **`\x1c`**             | **File Separator** | 
| **`\x1d`**             | **Group Separator** | 
| **`\x1e`**             | **Record Separator** | 
| **`\x85`**             | **Next Line (C1 Control Code)** | 
| **`\u2028`**           | **Line Separator** | 
| **`\u2029`**           | **Paragraph Separator** |

```python
# Example 1: How splitlines() works?

grocery = 'Milk\nCoffee\r\nBread\rButter'

print(grocery.splitlines())
print(grocery.splitlines(True))

grocery = 'Milk Coffee Bread Butter'
print(grocery.splitlines())
```

**Output:**
```text
['Milk', 'Coffee', 'Bread', 'Butter']
['Milk\n', 'Coffee\r\n', 'Bread\r', 'Butter']
['Milk Coffee Bread Butter']
```

---

## 📘 Python String Startswith()
*Source: `2. Python Datatypes/41. Python String startswith().ipynb`*

# Python String `startswith()`

The string **`startswith()`** method returns **`True`** if a string starts with the specified prefix(string). If not, it returns **`False`**.

**Syntax**:

```python
str.startswith(prefix[, start[, end]])
```

## `startswith()` Parameters

The **`startswith()`** method takes a maximum of three parameters:

* **`prefix`** - String or tuple of strings to be checked
* **`start`** (optional) - Beginning position where **`prefix`** is to be checked within the string.
* **`end`** (optional) - Ending position where **`prefix`** is to be checked within the string.

## Return Value from `startswith()`

The **`startswith()`** method returns a boolean.

* It returns **`True`** if the string starts with the specified prefix.
* It returns **`False`** if the string doesn't start with the specified prefix.

```python
# Example 1: startswith() Without start and end Parameters

text = "Python is easy to learn."

result = text.startswith('is easy')
# returns False
print(result)

result = text.startswith('Python is ')
# returns True
print(result)

result = text.startswith('Python is easy to learn.')
# returns True
print(result)
```

**Output:**
```text
False
True
True
```

```python
# Example 2: startswith() With start and end Parameters

text = "Python programming is easy."

# start parameter: 7
# 'programming is easy.' string is searched
result = text.startswith('programming is', 7)
print(result)

# start: 7, end: 18
# 'programming' string is searched
result = text.startswith('programming is', 7, 18)
print(result)

result = text.startswith('program', 7, 18)
print(result)
```

**Output:**
```text
True
False
True
```

## Passing Tuple to `startswith()`

It's possible to pass a tuple of prefixes to **`startswith()`** method in Python.

If the string starts with any item of the tuple, **`startswith()`** returns **`True`**. If not, it returns **`False`**

```python
# Example 3: startswith() With Tuple Prefix

text = "programming is easy"
result = text.startswith(('python', 'programming'))

# prints True
print(result)

result = text.startswith(('is', 'easy', 'java'))

# prints False
print(result)

# With start and end parameter
# 'is easy' string is checked
result = text.startswith(('programming', 'easy'), 12, 19)

# prints False
print(result)
```

**Output:**
```text
True
False
False
```

If you need to check if a string ends with the specified suffix, you can use **endswith() method in Python**.

---

## 📘 Python String Title()
*Source: `2. Python Datatypes/42. Python String title().ipynb`*

# Python String `title()`

The string **`title()`** method returns a string with first letter of each word capitalized; a title cased string.

**Syntax**:

```python
str.title()
```

## `title()` Parameters

The **`title()`** method doesn't take any parameters.

## Return Value from `title()`

The **`title()`** method returns a title cased version of the string. Meaning, the first character of each word is capitalized (if the first character is a letter).

```python
# Example 1: How Python title() works?

text = 'My favorite number is 99.'
print(text.title())

text = '963 k3l2 *63 fun'
print(text.title())
```

**Output:**
```text
My Favorite Number Is 99.
963 K3L2 *63 Fun
```

```python
# Example 2: title() with apostrophes

text = "He's an engineer, isn't he?"
print(text.title())
```

**Output:**
```text
He'S An Engineer, Isn'T He?
```

>**Note:** **`title()`** capitalizes the first letter after apostrophes as well.

To solve this issue, you can use regex as follows:

```python
# Example 3: Using Regex to Title Case String

import re

def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
     lambda mo: mo.group(0)[0].upper() +
     mo.group(0)[1:].lower(),
     s)

text = "He's an engineer, isn't he?"
print(titlecase(text))
```

**Output:**
```text
He's An Engineer, Isn't He?
```

---

## 📘 Python String Zfill()
*Source: `2. Python Datatypes/43. Python String zfill().ipynb`*

# Python String `zfill()`

The string **`zfill()`** method returns a copy of the string with '0' characters padded to the left.

**Syntax**:

```python
str.zfill(width)
```

## `zfill()` Parameters

The **`zfill()`** method takes a single character width.

The **`width`** specifies the length of the returned string from **`zfill()`** with **`0`** digits filled to the left.

## Return Value from `zfill()`

The **`zfill()`** method returns a copy of the string with **`0`** filled to the left. The length of the returned string depends on the **`width`** provided.

* Suppose, the initial length of the string is 10. And, the **`width`** is specified 15. In this case, **`zfill()`** returns a copy of the string with five '0' digits filled to the left.
* Suppose, the initial length of the string is 10. And, the **`width`** is specified 8. In this case, **`zfill()`** doesn't fill '0' digits to the left and returns a copy of the original string. The length of the returned string in this case will be 10.

```python
# Example 1: How zfill() works in Python?

text = "program is fun"
print(text.zfill(15))
print(text.zfill(20))
print(text.zfill(10))
```

**Output:**
```text
0program is fun
000000program is fun
program is fun
```

>**Note:** If a string starts with the sign prefix **`('+', '-')`**, **`0`** digits are filled after the first sign prefix character.

```python
# Example 2: How zfill() works with Sign Prefix?

number = "-690"
print(number.zfill(8))

number = "+690"
print(number.zfill(8))

text = "--random+text"
print(text.zfill(20))
```

**Output:**
```text
-0000690
+0000690
-0000000-random+text
```

---

## 📘 Python String Format Map()
*Source: `2. Python Datatypes/44. Python String format map().ipynb`*

# Python String `format_map()`

The string **`format_map()`** method is similar to __`str.format(**mapping)`__ except that __`str.format(**mapping)`__ creates a new dictionary whereas **`str.format_map(mapping)`** doesn't.

Before talking about **`format_map()`**. Let's see how __`str.format(**mapping)`__ works for **Python Dictionaries**.

```python
point = {'x':9,'y':-6}
print('{x} {y}'.format(**point))
```

**Output:**
```text
9 -6
```

The **`format_map(mapping)`** is similar to __`str.format(**mapping)`__ method.

The only difference is that __`str.format(**mapping)`__ copies the **`dict`** whereas __`str.format(**mapping)`__ makes a new dictionary during method call. This can be useful if you are working with a **`dict`** subclass.

**Syntax**:

```python
str.format_map(mapping)
```

## `format_map()` Parameters

The **`format_map()`** method takes a single argument **`mapping(dictionary)`**.

## Return Value from `format_map()`

The **`format_map()`** method formats the given string and returns it.

```python
# Example 1: How format_map() works?

point = {'x':9,'y':-6}
print('{x} {y}'.format_map(point))

point = {'x':9,'y':-6, 'z': 0}
print('{x} {y} {z}'.format_map(point))
```

**Output:**
```text
9 -6
9 -6 0
```

```python
# Example 2: How format_map() works with dict subclass?

class Coordinate(dict):
    def __missing__(self, key):
        return key


print('({x}, {y})'.format_map(Coordinate(x='9')))
print('({x}, {y})'.format_map(Coordinate(y='5')))
print('({x}, {y})'.format_map(Coordinate(x='9', y='6')))
```

**Output:**
```text
(9, y)
(x, 5)
(9, 6)
```

>**Note:** **`format_map(mapping)`** is more flexible than __`format(**mapping)`__ as you can have missing keys.

---

## 📘 Python Del Statement
*Source: `2. Python Datatypes/Python Del Statement.ipynb`*

# Python del Statement

In this class, you will learn to use the **`del`**  keyword with the help of examples.

**Syntax**:

```python
del obj_name
```

Here, **`del`** is a Python keyword. And, **`obj_name`** can be variables, user-defined objects, lists, items within lists, dictionaries etc.

```python
# Example 1: Delete an user-defined object

class MyClass:
    a = 10
    def func(self):
        print('Hello')

print(MyClass)   # Output: <class '__main__.MyClass'>
```

```python
del MyClass     # deleting MyClass

print(MyClass)  # Error: MyClass is not defined
```

In the program, we have deleted **`MyClass`** using **`del MyClass`** statement.

```python
# Example 2: Delete variable, list, and dictionary

my_var = 5
my_tuple = ('Arthur', 33)
my_dict = {'name': 'Arthur', 'age': 33}

del my_var
del my_tuple
del my_dict
```

```python
# Example 3: Remove items, slices from a list

# The `del` statement can be used to delete an item at a given index. 
# Also, it can be used to remove slices from a list.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# deleting the third item
del my_list[2]

# Output: [1, 2, 4, 5, 6, 7, 8, 9]
print(my_list)

# deleting items from 2nd to 4th
del my_list[1:4]

# Output: [1, 6, 7, 8, 9]
print(my_list)

# deleting all elements
del my_list[:]

# Output: []
print(my_list)
```

**Output:**
```text
[1, 2, 4, 5, 6, 7, 8, 9]
[1, 6, 7, 8, 9]
[]
```

```python
# Error: my_var is not defined
print(my_var)
```

```python
# Error: my_tuple is not defined
print(my_tuple)
```

```python
# Error: my_dict is not defined
print(my_dict)
```

```python
# Example 4: Remove a key:value pair from a dictionary

person = { 'name': 'Arthur',
  'age': 33,
  'profession': 'Programmer'
}

del person['profession']
print(person)   # Output: {'name': 'Arthur', 'age': 33}
```

**Output:**
```text
{'name': 'Arthur', 'age': 33}
```

You can't delete items of tuples and strings. It's because tuples and strings are immutables; objects that can't be changed after its creation.

```python
my_tuple = (1, 2, 3)

del my_tuple[1]    # Error: 'tuple' object doesn't support item deletion
```

However, you can delete an entire tuple or string.

```python
my_tuple = (1, 2, 3)

del my_tuple    # deleting tuple
my_tuple
```

---

## 📘 Python Shallow Copy And Deep Copy
*Source: `2. Python Datatypes/Python Shallow Copy and Deep Copy.ipynb`*

# Python Shallow Copy and Deep Copy

In this class, you’ll learn about shallow copy and deep copy in Python with the help of examples.

## Copy an Object in Python

In Python, we use **`=`** operator to create a copy of an object. You may think that this creates a new object; it doesn't. It only creates a new variable that shares the reference of the original object.

Let's take an example where we create a list named **`old_list`** and pass an object reference to **`new_list`** using **`=`** operator.

```python
# Example 1: Copy using = operator

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))
```

As you can see from the output both variables **`old_list`** and **`new_list`** shares the same id i.e **`140673303268168`**.

So, if you want to modify any values in **`new_list`** or **`old_list`**, the change is visible in both.

Essentially, sometimes you may want to have the original values unchanged and only modify the new values or vice versa. In Python, there are two ways to create copies:

1. Shallow Copy
2. Deep Copy

To make these copy work, we use the **`copy`** module.

## Copy Module

We use the **`copy()`** module of Python for shallow and deep copy operations. Suppose, you need to copy the compound list say **`x`**. For example:

```python
import copy
copy.copy(x)
copy.deepcopy(x)
```

Here, the **`copy()`** return a shallow copy of **`x`**. Similarly, **`deepcopy()`** return a deep copy of **`x`**.

## Shallow Copy

A shallow copy creates a new object which stores the reference of the original elements.

So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.

```python
# Example 2: Create a copy using shallow copy

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
```

In above program, we created a nested list and then shallow copy it using **`copy()`** method.

This means it will create new and independent object with same content. To verify this, we print the both **`old_list`** and **`new_list`**.

To confirm that **`new_list`** is different from **`old_list`**, we try to add new nested object to original and check it.

```python
# Example 3: Adding [4, 4, 4] to old_list, using shallow copy

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)
```

In the above program, we created a shallow copy of **`old_list`**. The **`new_list`** contains references to original nested objects stored in **`old_list`**. Then we add the new list i.e **`[4, 4, 4]`** into **`old_list`**. This new sublist was not copied in **`new_list`**.

However, when you change any nested objects in **`old_list`**, the changes appear in **`new_list`**.

```python
# Example 4: Adding new nested object using Shallow copy

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)
```

In the above program, we made changes to **`old_list`** i.e **`old_list[1][1] = 'AA'`**. Both sublists of **`old_list`** and **`new_list`** at index **`[1][1]`** were modified. This is because, both lists share the reference of same nested objects.

## Deep Copy

A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.

Let’s continue with example 2. However, we are going to create deep copy using **`deepcopy()`** function present in copy module. The deep copy creates independent **`copy`** of original object and all its nested objects.

```python
# Example 5: Copying a list using deepcopy()

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
```

In the above program, we use **`deepcopy()`** function to create copy which looks similar.

However, if you make changes to any nested objects in original object **`old_list`**, you’ll see no changes to the copy **`new_list`**.

```python
# Example 6: Adding a new nested object in the list using Deep copy

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)
```

In the above program, when we assign a new value to **`old_list`**, we can see only the **`old_list`** is modified. This means, both the **`old_list`** and the **`new_list`** are independent. This is because the **`old_list`** was recursively copied, which is true for all its nested objects.

---
