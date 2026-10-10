# Python datetime & time Module Mastery

Handling dates, times, timedeltas, timestamp conversions, strftime() date formatting, strptime() parsing, time execution profiling, and sleep delays.

---

# 08_Python_Date_Time


## Introduction 👋

### 1. What is Pandas DateTime Module?
Working with dates and times is one of the biggest challenges in programming. Between dealing with time zones, daylight saving time, and different written date formats, it can be tough to keep track of which days and times you’re referencing. Fortunately, the built-in Python datetime module can help you manage the complex nature of dates and times.

In this tutorial, you’ll learn:

* Why programming with dates and times is such a challenge
* Which functions are available in the Python datetime module
* How to print or read a date and time in a specific format
* How to do arithmetic with dates and times

### 2. What is Pandas Time Module?
The Python time module provides many ways of representing time in code, such as objects, numbers, and strings. It also provides functionality other than representing time, like waiting during code execution and measuring the efficiency of your code.

This article will walk you through the most commonly used functions and objects in time.

By the end of this article, you’ll be able to:

* Understand core concepts at the heart of working with dates and times, such as epochs, time zones, and daylight savings time
* Represent time in code using floats, tuples, and struct_time
* Convert between different time representations
* Suspend thread execution
* Measure code performance using perf_counter()

---

## Table of contents 📋

| **No.** | **Name** | 
| ------- | -------- | 
| 01 | **[Python_datetime_Module](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/001_Python_datetime_Module.ipynb)** |
| 02 | **[Python_strftime()](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/002_Python_strftime().ipynb)** |
| 03 | **[Python_strptime](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/003_Python_strptime.ipynb)** |
| 04 | **[Python_current_date_and_time](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/004_Python_current_date_and_time.ipynb)** |
| 05 | **[Python_get_current_time](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/005_Python_get_current_time.ipynb)** |
| 06 | **[Python_timestamp_to_datetime](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/006_Python_timestamp_to_datetime.ipynb)** |
| 07 | **[Python_time_Module](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/007_Python_time_Module.ipynb)** |
| 08 | **[Python_sleep()](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/008_Python_sleep().ipynb)** |

These are online **read-only** versions. However you can **`Run ▶`**  all the codes **online** by clicking here ➞ 

---

## Frequently asked questions ❔

### How can I thank you for writing and sharing this tutorial? 🌷

You can <img src="https://img.shields.io/static/v1?label=%E2%AD%90 Star &message=if%20useful&style=style=flat&color=blue" alt="Star Badge"/> and <img src="https://img.shields.io/static/v1?label=%E2%B5%96 Fork &message=if%20useful&style=style=flat&color=blue" alt="Fork Badge"/> Starring and Forking is free for you, but it tells me and other people that it was helpful and you like this tutorial.

Go [**`here`**](https://github.com/milaan9/08_Python_Date_Time_Module) if you aren't here already and click ➞ **`✰ Star`** and **`ⵖ Fork`** button in the top right corner. You will be asked to create a GitHub account if you don't already have one.

---

### How can I read this tutorial without an Internet connection? <img alt="GIF" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/hmm.gif" width="20" />

1. Go [**`here`**](https://github.com/milaan9/08_Python_Date_Time_Module) and click the big green ➞ **`Code`** button in the top right of the page, then click ➞ [**`Download ZIP`**](https://github.com/milaan9/08_Python_Date_Time_Module/archive/refs/heads/main.zip).

    ![Download ZIP](img/dnld_rep.png)

2. Extract the ZIP and open it. Unfortunately I don't have any more specific instructions because how exactly this is done depends on which operating system you run.
    
3. Launch ipython notebook from the folder which contains the notebooks. Open each one of them
  
    **`Kernel > Restart & Clear Output`**
    
This will clear all the outputs and now you can understand each statement and learn interactively.

If you have git and you know how to use it, you can also clone the repository instead of downloading a zip and extracting it. An advantage with doing it this way is that you don't need to download the whole tutorial again to get the latest version of it, all you need to do is to pull with git and run ipython notebook again.

---

## Authors ✍️

I'm Dr. Milaan Parmar and I have written this tutorial. If you think you can add/correct/edit and enhance this tutorial you are most welcome🙏

See [github's contributors page](https://github.com/milaan9/08_Python_Date_Time_Module/graphs/contributors) for details.

If you have trouble with this tutorial please tell me about it by [Create an issue on GitHub](https://github.com/milaan9/10_Python_Pandas_Module/issues/new). and I'll make this tutorial better. This is probably the best choice if you had trouble following the tutorial, and something in it should be explained better. You will be asked to create a GitHub account if you don't already have one.

If you like this tutorial, please [give it a ⭐ star](https://github.com/milaan9/08_Python_Date_Time_Module).

---

## Licence 📜

You may use this tutorial freely at your own risk. See [LICENSE](./LICENSE).

---

## 📘 Python Datetime Module
*Source: `9. Python Date Time Module/1. Python datetime Module.ipynb`*

<small><small><i>
All the IPython Notebooks in **Python Date Time Module** lecture series by Dr. Milaan Parmar are available @ **[GitHub](https://github.com/milaan9/08_Python_Date_Time_Module)**
</i></small></small>

# Python datetime

In this class, you will learn to manipulate date and time in Python with the help of examples.

Python has a module named **datetime** to work with dates and times. Let's create a few simple programs related to date and time before we dig deeper.

### Example 1: Get Current Date and Time

```python
# Example 1: Get Current Date and Time

import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)

# When you run the program, the output will be something like below:
```

**Output:**
```text
2021-06-22 18:01:47.527393
```

>**Note:** Here, we have imported datetime module using **`import datetime`** statement.

One of the classes defined in the **`datetime`** module is **`datetime`** class. We then used **`now()`** method to create a **`datetime`** object containing the current local date and time.

### Example 2: Get Current Date

```python
# Example 2: Get Current Date

import datetime

date_object = datetime.date.today()
print(date_object)

# When you run the program, the output will be something like below:
```

**Output:**
```text
2021-06-22
```

>**Note:** In this program, we have used **`today()`** method defined in the **`date`** class to get a **`date`** object containing the current local date.

### What's inside **`datetime`**?

We can use **[dir()](https://github.com/milaan9/04_Python_Functions/blob/main/002_Python_Functions_Built_in/016_Python_dir%28%29.ipynb)** function to get a list containing all attributes of a module.

```python
import datetime

print(dir(datetime))

# When you run the program, the output will be something like below:
```

**Output:**
```text
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

Commonly used classes in the datetime module are:

* date Class
* time Class
* datetime Class
* timedelta Class

## `datetime.date` Class

You can instantiate date objects from the **`date`** class. A **`date`** object represents a date (year, month and day).

### Example 3: Date object to represent a date

```python
# Example 3: Date object to represent a date

import datetime

d = datetime.date(2019, 4, 13)
print(d)

# When you run the program, the output will be something like below:
```

**Output:**
```text
2019-04-13
```

If you are wondering, **`date()`** in the above example is a constructor of the **`date`** class. The constructor takes three arguments: year, month and day.

The variable **`a`** is a **`date`** object.

We can only import **`date`** class from the **`datetime`** module. Here's how:

```python
from datetime import date

a = date(2019, 4, 13)
print(a)
```

**Output:**
```text
2019-04-13
```

### Example 4: Get current date

You can create a **`date`** object containing the current date by using a classmethod named **`today()`**. Here's how:

```python
# Example 4: Get current date

from datetime import date

today = date.today()

print("Current date =", today)
```

**Output:**
```text
Current date = 2021-06-22
```

We can also create **`date`** objects from a timestamp. A Unix timestamp is the number of seconds between a particular date and January 1, 1970 at UTC. You can convert a timestamp to date using **`fromtimestamp()`** method.

### Example 5: Get date from a timestamp

```python
# Example 5: Get date from a timestamp

from datetime import date

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

# When you run the program, the output will be something like below:
```

**Output:**
```text
Date = 2012-01-11
```

### Example 6: Print today's year, month and day

We can get year, month, day, day of the week etc. from the date object easily. Here's how:

```python
# Example 6: Print today's year, month and day

from datetime import date

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
```

**Output:**
```text
Current year: 2021
Current month: 6
Current day: 22
```

## `datetime.time`

A time object instantiated from the **`time`** class represents the local time.

### Example 7: Time object to represent time

```python
# Example 7: Time object to represent time

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

# When you run the program, the output will be like below:
```

**Output:**
```text
a = 00:00:00
b = 11:34:56
c = 11:34:56
d = 11:34:56.234566
```

### Example 8: Print hour, minute, second and microsecond

Once you create a **`time`** object, you can easily print its attributes such as **`hour`**, **`minute`** etc.

```python
# Example 8: Print hour, minute, second and microsecond

from datetime import time

a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)

# When you run the program, the output will be like below:
```

**Output:**
```text
hour = 11
minute = 34
second = 56
microsecond = 0
```

> **Note:** Notice that we haven't passed **`microsecond`** argument. Hence, its default value **`0`** is printed.

## `datetime.datetime`

The **`datetime`** module has a class named **`dateclass`** that can contain information from both **date** and **time** objects.

### Example 9: Python datetime object

```python
# Example 9: Python datetime object

from datetime import datetime

#datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

# When you run the program, the output will be like below:
```

**Output:**
```text
2018-11-28 00:00:00
2017-11-28 23:55:59.342380
```

> **Note:** The first three arguments **`year`**, **`month`** and **`day`** in the **`datetime()`** constructor are mandatory.

### Example 10: Print year, month, hour, minute and timestamp

```python
# Example 10: Print year, month, hour, minute and timestamp

from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

# When you run the program, the output will be like below:
```

**Output:**
```text
year = 2017
month = 11
hour = 23
minute = 55
timestamp = 1511893559.34238
```

## `datetime.timedelta`

A **`timedelta`** object represents the difference between two dates or times.

### Example 11: Difference between two dates and times

```python
# Example 11: Difference between two dates and times

from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))  

# When you run the program, the output will be like below:
```

**Output:**
```text
t3 = 201 days, 0:00:00
t6 = -333 days, 1:14:20
type of t3 = <class 'datetime.timedelta'>
type of t6 = <class 'datetime.timedelta'>
```

> **Note:** Notice, both **`t3`** and **`t6`** are of **`<class 'datetime.timedelta'>`** type.

### Example 12: Difference between two timedelta objects

```python
# Example 12: Difference between two timedelta objects

from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)

# When you run the program, the output will be like below:
```

**Output:**
```text
t3 = 14 days, 13:55:39
```

> **Note:** Here, we have created two timedelta objects **`t1`** and **`t2`**, and their difference is printed on the screen.

### Example 13: Printing negative timedelta object

```python
# Example 13: Printing negative timedelta object

from datetime import timedelta

t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2

print("t3 =", t3)
print("t3 =", abs(t3))

# When you run the program, the output will be like below:
```

**Output:**
```text
t3 = -1 day, 23:59:39
t3 = 0:00:21
```

### Example 14: Time duration in seconds

You can get the total number of seconds in a **`timedelta`** object using **`total_seconds()`** method.

```python
# Example 14: Time duration in seconds

from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("total seconds =", t.total_seconds())

# When you run the program, the output will be like below:
```

**Output:**
```text
total seconds = 435633.233423
```

You can also find sum of two dates and times using **`+`** operator. Also, you can multiply and divide a **`timedelta`** object by integers and floats.

## Python format datetime

The way date and time is represented may be different in different places, organizations etc. It's more common to use **`mm/dd/yyyy`** in the US, whereas **`dd/mm/yyyy`** is more common in the UK.

Python has **`strftime()`** and **`strptime()`** methods to handle this.

### Python `strftime()` - datetime object to string

The **`strftime()`** method is defined under classes **`date`**, **`datetime`** and **`time`**. The method creates a formatted string from a given **`date`**, **`datetime`** or **`time`** object.

### Example 15: Format date using `strftime()`

```python
# Example 15: Format date using strftime()

from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

# When you run the program, the output will be like below:
```

**Output:**
```text
time: 18:12:42
s1: 06/22/2021, 18:12:42
s2: 22/06/2021, 18:12:42
```

Here, **`%Y`**, **`%m`**, **`%d`**, **`%H`** etc. are format codes. The **`strftime()`** method takes one or more format codes and returns a formatted string based on it.

In the above program, t, s1 and s2 are strings.

| Directive | Meaning | Example |
|:---- |:---- |:---- |
| **`%Y`** | **year**   | **[0001,..., 2018, 2019,..., 9999]** |  
| **`%m`** | **month**  | **[01, 02, ..., 11, 12]** |  
| **`%d`** | **day**    | **[01, 02, ..., 30, 31]** |  
| **`%H`** | **hour**   | **[00, 01, ..., 22, 23]** |  
| **`%M`** | **minute** | **[00, 01, ..., 58, 59]** |  
| **`%S`** | **second** | **[00, 01, ..., 58, 59]** |  


To learn more about **`strftime()`** and format codes, visit: **[Python strftime()](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/002_Python_strftime%28%29.ipynb)**.

### Python `strptime()` - string to datetime

The **`strptime()`** method creates a **`datetime`** object from a given string (representing date and time).

### Example 16: `strptime()`

```python
# Example 16: strptime()

from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# When you run the program, the output will be like below:
```

**Output:**
```text
date_string = 21 June, 2018
date_object = 2018-06-21 00:00:00
```

**Explanation:**

The **`strptime()`** method takes two arguments:

1. a string representing date and time
2. format code equivalent to the first argument

By the way, **`%d`**, **`%B`** and **`%Y`** format codes are used for **`day`**, **`month`**(full name) and **`year`** respectively.

Visit **[Python strptime()](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/003_Python_strptime%28%29.ipynb)** to learn more.

## Handling timezone in Python

Suppose, you are working on a project and need to display date and time based on their timezone.

Rather than trying to handle timezone yourself, we suggest you to use a third-party **[pytZ module](http://pytz.sourceforge.net/)**

```python
from datetime import datetime
import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

# When you run the program, the output will be like below:
```

**Output:**
```text
Local: 06/22/2021, 18:12:47
NY: 06/22/2021, 08:42:48
London: 06/22/2021, 13:42:48
```

>**Note:** Here, **`datetime_NY`** and **`datetime_London`** are datetime objects containing the current date and time of their respective timezone.

---

## 📘 Python Strftime()
*Source: `9. Python Date Time Module/2. Python strftime().ipynb`*

<small><small><i>
All the IPython Notebooks in **Python Date Time Module** lecture series by Dr. Milaan Parmar are available @ **[GitHub](https://github.com/milaan9/08_Python_Date_Time_Module)**
</i></small></small>

# Python `strftime()`

In this class, you will learn to convert date, time and datetime objects to its equivalent string (with the help of examples).

The **[strftime()](https://strftime.org/)** method returns a string representing date and time using **[date (@ Example 3), time (@ Example 7) or datetime (@ Example 9)](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/001_Python_datetime_Module.ipynb)** object.

### Example 1: datetime to string using `strftime()`

The program below converts a **`datetime`** object containing current date and time to different string formats.

```python
# Example 1: datetime to string using strftime()

from datetime import datetime

now = datetime.now() # current date and time
print(now)

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time1)

date_time2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("date and time:",date_time2)

# When you run the program, the output will be something like below:
```

**Output:**
```text
2021-10-18 18:01:58.168321
year: 2021
month: 10
day: 18
time: 18:01:58
date and time: 10/18/2021, 18:01:58
date and time: 18/10/2021, 18:01:58
```

>**Note:** Here, **`year`**, **`day`**, **`time`** and **`date_time`** are strings, whereas **`now`** is a **`datetime`** object.

## How `strftime()` works?

In the above program, **`%Y`**, **`%m`**, **`%d`** etc. are format codes. The **`strftime()`** method takes one or more format codes as an argument and returns a formatted string based on it.

1. We imported **`datetime`** class from the **`datetime`** module. It's because the object of **`datetime`** class can access **`strftime()`** method.

<div>

</div>

2. The **`datetime`** object containing current date and time is stored in **`now`** variable.

<div>

</div>

3. The **`strftime()`** method can be used to create formatted strings.

<div>

</div>

4. The string you pass to the **`strftime()`** method may contain more than one format codes.

<div>

</div>

### Example 2: Creating string from a timestamp

```python
# Example 2: Creating string from a timestamp

from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)	

d = date_time.strftime("%d %b, %Y")
print("Output 3:", d)

d = date_time.strftime("%d %B, %Y")
print("Output 4:", d)

d = date_time.strftime("%I%p")
print("Output 5:", d)

# When you run the program, the output will be something like below:
```

**Output:**
```text
Date time object: 2018-06-12 15:25:22
Output 2: 06/12/2018, 15:25:22
Output 3: 12 Jun, 2018
Output 4: 12 June, 2018
Output 5: 03PM
```

## Format Code List

The table below shows all the codes that you can pass to the **`strftime()`** method.

| Directive | Meaning | Example |
|:----: |:---- |:---- |
| **`%a`**  | **Abbreviated weekday name.**   | **Sun, Mon, ...** |  
| **`%A`**  | **Full weekday name.**   | **Sunday, Monday, ...** |  
| **`%w`**  | **Weekday as a decimal number.**   | **0, 1, ..., 6** |  
| **`%d`**  | **Day of the month as a zero-padded decimal.**   | **01, 02, ..., 31** |  
| **`%-d`** | **Day of the month as a decimal number.**   | **1, 2, ..., 30** |  
| **`%b`**  | **Abbreviated month name.**   | **Jan, Feb, ..., Dec** |  
| **`%B`**  | **Full month name.**   | **January, February, ...** |  
| **`%m`**  | **Month as a zero-padded decimal number.**   | **01, 02, ..., 12** |  
| **`%-m`** | **Month as a decimal number.**   | **1, 2, ..., 12** |  
| **`%y`**  | **Year without century as a zero-padded decimal number.**   | **00, 01, ..., 99** |  
| **`%-y`** | **Year without century as a decimal number.**   | **0, 1, ..., 99** |  
| **`%Y`**  | **Year with century as a decimal number.**   | **2013, 2019 etc.** |  
| **`%H`**  | **Hour (24-hour clock) as a zero-padded decimal number.**   | **00, 01, ..., 23** |  
| **`%-H`** | **Hour (24-hour clock) as a decimal number.**   | **0, 1, ..., 23** |  
| **`%I`**  | **Hour (12-hour clock) as a zero-padded decimal number.**   | **01, 02, ..., 12** |  
| **`%-I`** | **Hour (12-hour clock) as a decimal number.**   | **1, 2, ... 12** |  
| **`%p`**  | **Locale’s AM or PM.**   | **AM, PM** |  
| **`%M`**  | **Minute as a zero-padded decimal number.**   | **00, 01, ..., 59** |  
| **`%-M`** | **Minute as a decimal number.**   | **0, 1, ..., 59** |  
| **`%S`**  | **Second as a zero-padded decimal number.**   | **00, 01, ..., 59** |  
| **`%-S`** | **Second as a decimal number.**   | **0, 1, ..., 59** |  
| **`%f`**  | **Microsecond as a decimal number, zero-padded on the left.**   | **000000 - 999999** |  
| **`%z`**  | **UTC offset in the form +HHMM or -HHMM.**   |  |  
| **`%Z`**  | **Time zone name.**   |  |  
| **`%j`**  | **Day of the year as a zero-padded decimal number.**   | **001, 002, ..., 366** |  
| **`%-j`** | **Day of the year as a decimal number.**   | **1, 2, ..., 366** |  
| **`%U`**  | **Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.**   | **00, 01, ..., 53** |  
| **`%U`**  | **Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.**   | **00, 01, ..., 53** |  
| **`%c`**  | **Locale’s appropriate date and time representation.**   | **Mon Sep 30 07:06:05 2013** |  
| **`%x`**  | **Locale’s appropriate date representation.**   | **09/30/13** |  
| **`%X`**  | **Locale’s appropriate time representation.**   | **07:06:05** |  
| **`%%`**  | **A literal '%' character.**   | **%** |

### Example 3: Locale's appropriate date and time

```python
# Example 3: Locale's appropriate date and time

from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

d = date_time.strftime("%c")
print("Output 1:", d)	

d = date_time.strftime("%x")
print("Output 2:", d)

d = date_time.strftime("%X")
print("Output 3:", d)

# When you run the program, the output will be something like below:
```

**Output:**
```text
Output 1: Tue Jun 12 15:25:22 2018
Output 2: 06/12/18
Output 3: 15:25:22
```

>**Note:** Format codes **`%c`**, **`%x`** and **`%X`** are used for locale's appropriate date and time representation.

We also recommend you to check **[Python strptime()](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/003_Python_strptime%28%29.ipynb)**. The **`strptime()`** method creates a **`datetime`** object from a string.

---

## 📘 Python Strptime()
*Source: `9. Python Date Time Module/3. Python strptime().ipynb`*

<small><small><i>
All the IPython Notebooks in **Python Date Time Module** lecture series by Dr. Milaan Parmar are available @ **[GitHub](https://github.com/milaan9/08_Python_Date_Time_Module)**
</i></small></small>

# Python `strptime()`

In this class, you will learn to create a datetime object from a string (with the help of examples).

The **`strptime()`** method creates a **[datetime (@ Example 9)](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/001_Python_datetime_Module.ipynb)** object from the given string.

>**Note:** You cannot create **`datetime`** object from every string. The string needs to be in a certain format.

### Example 1: string to datetime object

```python
# Example 1: string to datetime object

from datetime import datetime

date_string = "21 June, 2018"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))

# When you run the program, the output will be something like below:
```

**Output:**
```text
date_string = 21 June, 2018
type of date_string = <class 'str'>
date_object = 2018-06-21 00:00:00
type of date_object = <class 'datetime.datetime'>
```

### How `strptime()` works?

The **`strftime()`** class method takes two arguments:

1. string (that be converted to datetime)
2. format code

Based on the string and format code used, the method returns its equivalent **`datetime`** object.

In the above example:

<div>

</div>

Here,

* **`%d`** - Represents the day of the month. **Example:** 01, 02, ..., 31
* **`%B`** - Month's name in full. **Example:** January, February etc.
* **`%Y`** - Year in four digits. **Example:** 2018, 2019 etc.

### Example 2: string to datetime object

```python
# Example 2: string to datetime object

from datetime import datetime

dt_string = "12/11/2018 09:15:32"

# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)

# Considering date is in mm/dd/yyyy format
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)

# When you run the program, the output will be something like below:
```

**Output:**
```text
dt_object1 = 2018-11-12 09:15:32
dt_object2 = 2018-12-11 09:15:32
```

## Format Code List

The table below shows all the codes that you can pass to the **`strptime()`** method.

| Directive | Meaning | Example |
|:----: |:---- |:---- |
| **`%a`**  | **Abbreviated weekday name.**   | **Sun, Mon, ...** |  
| **`%A`**  | **Full weekday name.**   | **Sunday, Monday, ...** |  
| **`%w`**  | **Weekday as a decimal number.**   | **0, 1, ..., 6** |  
| **`%d`**  | **Day of the month as a zero-padded decimal.**   | **01, 02, ..., 31** |  
| **`%-d`** | **Day of the month as a decimal number.**   | **1, 2, ..., 30** |  
| **`%b`**  | **Abbreviated month name.**   | **Jan, Feb, ..., Dec** |  
| **`%B`**  | **Full month name.**   | **January, February, ...** |  
| **`%m`**  | **Month as a zero-padded decimal number.**   | **01, 02, ..., 12** |  
| **`%-m`** | **Month as a decimal number.**   | **1, 2, ..., 12** |  
| **`%y`**  | **Year without century as a zero-padded decimal number.**   | **00, 01, ..., 99** |  
| **`%-y`** | **Year without century as a decimal number.**   | **0, 1, ..., 99** |  
| **`%Y`**  | **Year with century as a decimal number.**   | **2013, 2019 etc.** |  
| **`%H`**  | **Hour (24-hour clock) as a zero-padded decimal number.**   | **00, 01, ..., 23** |  
| **`%-H`** | **Hour (24-hour clock) as a decimal number.**   | **0, 1, ..., 23** |  
| **`%I`**  | **Hour (12-hour clock) as a zero-padded decimal number.**   | **01, 02, ..., 12** |  
| **`%-I`** | **Hour (12-hour clock) as a decimal number.**   | **1, 2, ... 12** |  
| **`%p`**  | **Locale’s AM or PM.**   | **AM, PM** |  
| **`%M`**  | **Minute as a zero-padded decimal number.**   | **00, 01, ..., 59** |  
| **`%-M`** | **Minute as a decimal number.**   | **0, 1, ..., 59** |  
| **`%S`**  | **Second as a zero-padded decimal number.**   | **00, 01, ..., 59** |  
| **`%-S`** | **Second as a decimal number.**   | **0, 1, ..., 59** |  
| **`%f`**  | **Microsecond as a decimal number, zero-padded on the left.**   | **000000 - 999999** |  
| **`%z`**  | **UTC offset in the form +HHMM or -HHMM.**   |  |  
| **`%Z`**  | **Time zone name.**   |  |  
| **`%j`**  | **Day of the year as a zero-padded decimal number.**   | **001, 002, ..., 366** |  
| **`%-j`** | **Day of the year as a decimal number.**   | **1, 2, ..., 366** |  
| **`%U`**  | **Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.**   | **00, 01, ..., 53** |  
| **`%U`**  | **Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.**   | **00, 01, ..., 53** |  
| **`%c`**  | **Locale’s appropriate date and time representation.**   | **Mon Sep 30 07:06:05 2013** |  
| **`%x`**  | **Locale’s appropriate date representation.**   | **09/30/13** |  
| **`%X`**  | **Locale’s appropriate time representation.**   | **07:06:05** |  
| **`%%`**  | **A literal '%' character.**   | **%** |

### `ValueError` in `strptime()`

If the string (first argument) and the format code (second argument) passed to the **`strptime()`** doesn't match, you will get **`ValueError`**. For example:

```python
from datetime import datetime

date_string = "12/11/2018"
date_object = datetime.strptime(date_string, "%d %m %Y")

print("date_object =", date_object)

# When you run the program, the output will be something like below:
```

We also recommend you to check **[Python strftime()](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/002_Python_strftime%28%29.ipynb)**.

---

## 📘 Python Current Date And Time
*Source: `9. Python Date Time Module/4. Python current date and time.ipynb`*

<small><small><i>
All the IPython Notebooks in **Python Date Time Module** lecture series by Dr. Milaan Parmar are available @ **[GitHub](https://github.com/milaan9/08_Python_Date_Time_Module)**
</i></small></small>

# How to get current date and time in Python?

In this class, you will learn to get today's date and current date and time in Python. We will also format the date and time in different formats using **`strftime()`** method.

There are a number of ways you can take to get the current date. We will use the **`date`** class of the **[datetime](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/001_Python_datetime_Module.ipynb)** module to accomplish this task.

### Example 1: Python get today's date

```python
# Example 1: Python get today's date
from datetime import date

today = date.today()
print("Today's date:", today)

# When you run the program, the output will be something like below:
```

**Output:**
```text
Today's date: 2021-06-22
```

> **Note:** Here, we imported the **`date`** class from the **`datetime`** module. Then, we used the **`date.today()`** method to get the current local date.

By the way, **`date.today()`** returns a **`date`** object, which is assigned to the today variable in the above program. Now, you can use the **[strftime()](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/002_Python_strftime%28%29.ipynb)** method to create a string representing date in different formats.

### Example 2: Current date in different formats

```python
# Example 2: Current date in different formats

from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

# When you run the program, the output will be something like below:
```

**Output:**
```text
d1 = 22/06/2021
d2 = June 22, 2021
d3 = 06/22/21
d4 = Jun-22-2021
```

If you need to get the current date and time, you can use **`datetime`**  class of the **`datetime`** module.

### Example 3: Get the current date and time

```python
# Example 3: Get the current date and time

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
```

**Output:**
```text
now = 2021-06-22 18:35:14.331191
date and time = 22/06/2021 18:35:14
```

**Explanation:** 

Here, we have used **`datetime.now()`** to get the current date and time. Then, we used **`strftime()`** to create a string representing date and time in another format.

---

## 📘 Python Get Current Time
*Source: `9. Python Date Time Module/5. Python get current time.ipynb`*

<small><small><i>
All the IPython Notebooks in **Python Date Time Module** lecture series by Dr. Milaan Parmar are available @ **[GitHub](https://github.com/milaan9/08_Python_Date_Time_Module)**
</i></small></small>

# Python Get Current time

In this article, you will learn to get current time of your locale as well as different time zones in Python.

There are a number of ways you can take to get current time in Python.

### Example 1: Current time using datetime object

```python
# Example 1: Current time using datetime object

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# When you run the program, the output will be something like below:
```

**Output:**
```text
Current Time = 18:08:06
```

> **Note:** In the above example, we have imported the **`datetime`** class from the **[datetime](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/001_Python_datetime_Module.ipynb)** module. Then, we used **`now`** method to get a **`datetime`** object containing current date and time.

Using **[datetime.strftime()](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/002_Python_strftime%28%29.ipynb)** method, we then created a string representing current time.

If you need to create a **`time`** object containing current time, you can do something like this.

```python
# from datetime import datetime

now = datetime.now().time() # time object

print("now =", now)
print("type(now) =", type(now))	

# When you run the program, the output will be something like below:
```

**Output:**
```text
now = 18:08:06.994177
type(now) = <class 'datetime.time'>
```

### Example 2: Current time using time module

You can also get the current time using **`time`** module.

```python
# Example 2: Current time using time module

import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

# When you run the program, the output will be something like below:
```

**Output:**
```text
18:08:07
```

### Example 3: Current time of a timezone

If you need to find current time of a certain timezone, you can use **[pytZ module](http://pytz.sourceforge.net/)**.

```python
# Example 3: Current time of a timezone

from datetime import datetime
import pytz

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))
```

**Output:**
```text
NY time: 08:38:07
London time: 13:38:07
```

### Example 4: Time Objects to Represent Time

```python
# Example 4: Time Objects to Represent Time

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
```

**Output:**
```text
a = 00:00:00
b = 10:30:50
c = 10:30:50
d = 10:30:50.200555
```

### Example 5: Difference Between Two Points in Time Using

```python
# Example 5: Difference Between Two Points in Time Using

from datetime import date

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
```

**Output:**
```text
Time left for new year:  27 days, 0:00:00
Time left for new year: 26 days, 23:01:00
```

### Example 6: Difference Between Two Points in Time Using `timedelata`

```python
# Example 6: Difference Between Two Points in Time Using `timedelata`

from datetime import timedelta

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
```

**Output:**
```text
t3 = 86 days, 22:56:50
```

---

## 📘 Python Timestamp To Datetime
*Source: `9. Python Date Time Module/6. Python timestamp to datetime.ipynb`*

<small><small><i>
All the IPython Notebooks in **Python Date Time Module** lecture series by Dr. Milaan Parmar are available @ **[GitHub](https://github.com/milaan9/08_Python_Date_Time_Module)**
</i></small></small>

# Python timestamp to datetime and vice-versa

In this article, you will learn to convert timestamp to datetime object and datetime object to timestamp (with the help of examples).

It's pretty common to store date and time as a timestamp in a database. A Unix timestamp is the number of seconds between a particular date and January 1, 1970 at UTC.

### Example 1: Python timestamp to datetime

```python
# Example 1: Python timestamp to datetime

from datetime import datetime

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

# When you run the program, the output will be something like below:
```

**Output:**
```text
dt_object = 2018-12-25 14:57:53
type(dt_object) = <class 'datetime.datetime'>
```

**Explanation:** 

Here, we have imported **[datetime](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/001_Python_datetime_Module.ipynb)** class from the datetime module. Then, we used **`datetime.fromtimestamp()`** classmethod which returns the local date and time (datetime object). This object is stored in **`dt_object`** variable.

> **Note:** You can easily create a string representing date and time from a **`datetime`** object using **[strftime()](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/002_Python_strftime%28%29.ipynb)** method.

### Example 2: Python datetime to timestamp

You can get timestamp from a datetime object using **`datetime.timestamp()`** method.

```python
# Example 2: Python datetime to timestamp

from datetime import datetime

# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)

# When you run the program, the output will be something like below:
```

**Output:**
```text
timestamp = 1624370069.654593
```

## 💻 Exercises ➞ <span class='label label-default'>Date and Time</span>

### Exercises ➞ <span class='label label-default'>Level 1</span>

1. Get the current day, month, year, hour, minute and **`timestamp`** from **`datetime`** module
2. Format the current date using this format: **`"%m/%d/%Y, %H:%M:%S"`**)
3. Today is 5 December, 2019. Change this time string to time.
4. Calculate the time difference between now and new year.
5. Calculate the time difference between 1 January 1970 and now.
6. Think, what can you use the **`datetime`** module for? Examples:
   - Time series analysis
   - To get a **`timestamp`** of any activities in an application
   - Adding posts on a blog

---

## 📘 Python Time Module
*Source: `9. Python Date Time Module/7. Python time Module.ipynb`*

<small><small><i>
All the IPython Notebooks in **Python Date Time Module** lecture series by Dr. Milaan Parmar are available @ **[GitHub](https://github.com/milaan9/08_Python_Date_Time_Module)**
</i></small></small>

# Python time Module

In this article, we will explore time module in detail. We will learn to use different time-related functions defined in the time module with the help of examples.

Python has a module named **`time`** to handle time-related tasks. To use functions defined in the module, we need to import the module first. Here's how:

``` python
import time
```

Here are commonly used time-related functions.

### Python `time.time()`

The **`time()`** function returns the number of seconds passed since epoch.

For Unix system, **`January 1, 1970, 00:00:00`** at **UTC** is epoch (the point where time begins).

```python
import time
seconds = time.time()
print("Seconds since epoch =", seconds)	

# When you run the program, the output will be something like below:
```

**Output:**
```text
Seconds since epoch = 1624370297.5828025
```

### Python **`time.ctime()`**

The **`time.ctime()`** function takes seconds passed since epoch as an argument and returns a string representing local time.

```python
import time

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)

# When you run the program, the output will be something like below:
```

**Output:**
```text
Local time: Thu Dec 27 21:19:29 2018
```

### Python `time.sleep()`

The **`sleep()`** function suspends (delays) execution of the current thread for the given number of seconds.

```python
import time

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")

# When you run the program, the output will be something like below:
```

**Output:**
```text
This is printed immediately.
This is printed after 2.4 seconds.
```

To learn more, visit: **[Python sleep()](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/008_Python_sleep%28%29.ipynb)**.

Before we talk about other time-related functions, let's explore **`time.struct_time`** class in brief.

## `time.struct_time` Class

Several functions in the time module such as **`gmtime()`**, **`asctime()`** etc. either take **`time.struct_time`** object as an argument or return it.

Here's an example of **`time.struct_time`** object.

```python
time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, 
                    tm_hour=6, tm_min=35, tm_sec=17, 
                    tm_wday=3, tm_yday=361, tm_isdst=0)
```

| Index | Attribute | Values |
|:----: |:---- |:---- |
| **0** | **tm_year**  | **0000, ...., 2018, ..., 9999** |  
| **1** | **tm_mon**   | **1, 2, ..., 12** | 
| **2** | **tm_mday**  | **1, 2, ..., 31** | 
| **3** | **tm_hour**  | **0, 1, ..., 23** | 
| **4** | **tm_min**   | **0, 1, ..., 59** | 
| **5** | **tm_sec**   | **0, 1, ..., 61** | 
| **6** | **tm_wday**  | **0, 1, ..., 6; Monday is 0** | 
| **7** | **tm_yday**  | **1, 2, ..., 366** | 
| **8** | **tm_isdst** | **0, 1 or -1** | 

The values (elements) of the **`time.struct_time`** object are accessible using both indices and attributes.

### Python `time.localtime()`

The **`localtime()`** function takes the number of seconds passed since epoch as an argument and returns **`struct_time`** in **local time**.

```python
import time

result = time.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

# When you run the program, the output will be like below:
```

**Output:**
```text
result: time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, tm_hour=21, tm_min=19, tm_sec=29, tm_wday=3, tm_yday=361, tm_isdst=0)

year: 2018
tm_hour: 21
```

>**Note:** If no argument or **`None`** is passed to **`localtime()`**, the value returned by **`time()`** is used.

### Python `time.gmtime()`

The **`gmtime()`** function takes the number of seconds passed since epoch as an argument and returns **`struct_time`** in **UTC**.

```python
import time

result = time.gmtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

# When you run the program, the output will be like below:
```

**Output:**
```text
result: time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, tm_hour=15, tm_min=49, tm_sec=29, tm_wday=3, tm_yday=361, tm_isdst=0)

year: 2018
tm_hour: 15
```

>**Note:** If no argument or **`None`** is passed to **`gmtime()`**, the value returned by **`time()`** is used.

### Python `time.mktime()`

The **`mktime()`** function takes **`struct_time`** (or a tuple containing 9 elements corresponding to **`struct_time`**) as an argument and returns the seconds passed since epoch in local time. Basically, it's the inverse function of **`localtime()`**.

```python
import time

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

local_time = time.mktime(t)
print("Local time:", local_time)

# When you run the program, the output will be something like below:
```

**Output:**
```text
Local time: 1545966844.0
```

The example below shows how **`mktime()`** and **`localtime()`** are related.

```python
import time

seconds = 1545925769

# returns struct_time
t = time.localtime(seconds)
print("t1: ", t)

# returns seconds from struct_time
s = time.mktime(t)
print("\s:", seconds)

# When you run the program, the output will be like below:
```

**Output:**
```text
t1:  time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, tm_hour=21, tm_min=19, tm_sec=29, tm_wday=3, tm_yday=361, tm_isdst=0)
\s: 1545925769
```

### Python `time.asctime()`

The **`asctime()`** function takes **`struct_time`** (or a tuple containing 9 elements corresponding to **`struct_time`**) as an argument and returns a string representing it. Here's an example:

```python
import time

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)

# When you run the program, the output will be like below:
```

**Output:**
```text
Result: Fri Dec 28 08:44:04 2018
```

### Python `time.strftime()`

The **`strftime()`** function takes **`struct_time`** (or tuple corresponding to it) as an argument and returns a string representing it based on the format code used. For example,

```python
import time

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)

# When you run the program, the output will be something like below:
```

**Output:**
```text
06/22/2021, 19:28:41
```

>**Note:** Here, **`%Y,`**, **`%m`**, **`%d`**, **`%H`** etc. are format codes.

| Directive | Meaning | Example |
|:----: |:---- |:---- |
| **`%Y`** | **year**   | **[0001,..., 2018, 2019,..., 9999]** |  
| **`%m`** | **month**  | **[01, 02, ..., 11, 12]** |  
| **`%d`** | **day**    | **[01, 02, ..., 30, 31]** |  
| **`%H`** | **hour**   | **[00, 01, ..., 22, 23]** |  
| **`%M`** | **minute** | **[00, 01, ..., 58, 59]** |  
| **`%S`** | **second** | **[00, 01, ..., 58, 61]** |

To learn more, visit: **[time.strftime()](https://docs.python.org/3/library/time.html#time.strftime)**.

### Python `time.strptime()`

The **`strptime()`** function parses a string representing time and returns **`struct_time`**.

```python
import time

time_string = "21 June, 2018"
result = time.strptime(time_string, "%d %B, %Y")

print(result)

# When you run the program, the output will be like below:
```

**Output:**
```text
time.struct_time(tm_year=2018, tm_mon=6, tm_mday=21, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=172, tm_isdst=-1)
```

---

## 📘 Python Sleep()
*Source: `9. Python Date Time Module/8. Python sleep().ipynb`*

<small><small><i>
All the IPython Notebooks in **Python Date Time Module** lecture series by Dr. Milaan Parmar are available @ **[GitHub](https://github.com/milaan9/08_Python_Date_Time_Module)**
</i></small></small>

# Python `sleep()`

The **`sleep()`** function suspends (waits) execution of the current thread for a given number of seconds.

Python has a module named **[time](https://github.com/milaan9/08_Python_Date_Time_Module/blob/main/007_Python_time_Module.ipynb)** which provides several useful functions to handle time-related tasks. One of the popular functions among them is **`sleep()`**.

The **`sleep()`** function suspends execution of the current thread for a given number of seconds.

### Example 1: Python `sleep()`

```python
# Example 1: Python sleep()

import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")

# When you run the program, the output will be like below:
```

**Output:**
```text
Printed immediately.
Printed after 2.4 seconds.
```

**Explanation:** 

* **`"Printed immediately"`** is printed
* Suspends (Delays) execution for 2.4 seconds.
* **`"Printed after 2.4 seconds"`** is printed.

As you can see from the above example, **`sleep()`** takes a floating-point number as an argument.

**Before Python 3.5**, the actual suspension time may be less than the argument specified to the **`time()`** function.

**Since Python 3.5**, the suspension time will be at least the seconds specified.

In the below program, we computed and printed the current local time inside the infinite **[while loop](https://github.com/milaan9/03_Python_Flow_Control/blob/main/006_Python_while_Loop.ipynb)**. Then, the program waits for 1 second. Again, the current local time is computed and printed. This process goes on.

### Example 2: Python create a digital clock

```python
# Example 2: Python create a digital clock

import time

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    time.sleep(1)

# When you run the program, the output will be something like below:
```

**Output:**
```text
07:33:39 PM
07:33:40 PM
07:33:41 PM
07:33:42 PM
07:33:43 PM
07:33:44 PM
07:33:45 PM
07:33:46 PM
07:33:47 PM
07:33:48 PM
07:33:49 PM
07:33:50 PM
07:33:51 PM
07:33:52 PM
07:33:53 PM
07:33:54 PM
07:33:55 PM
07:33:56 PM
07:33:57 PM
07:33:58 PM
07:33:59 PM
07:34:00 PM
07:34:01 PM
07:34:02 PM
07:34:03 PM
07:34:04 PM
07:34:05 PM
07:34:06 PM
07:34:07 PM
07:34:08 PM
07:34:09 PM
07:34:10 PM
07:34:11 PM
07:34:12 PM
07:34:13 PM
07:34:14 PM
07:34:15 PM
07:34:16 PM
07:34:17 PM
07:34:18 PM
07:34:19 PM
07:34:20 PM
07:34:21 PM
07:34:22 PM
07:34:23 PM
07:34:24 PM
07:34:25 PM
07:34:26 PM
```

Here is a slightly modified better version of the above program.

```python
import time

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result, end="", flush=True)
    print("\r", end="", flush=True)
    time.sleep(1)
```

**Output:**
```text
07:34:55 PM
```

To learn more, visit **[digital clock in Python shell](https://stackoverflow.com/questions/37515587/run-a-basic-digital-clock-in-the-python-shell)**.

## Multithreading in Python

Before talking about **`sleep()`** in multithreaded programs, let's talk about processes and threads.

A computer program is a collection of instructions. A process is the execution of those instructions.

A thread is a subset of the process. A process can have one or more threads.

All the programs above in this article are single-threaded programs. Here's an example of a multithreaded Python program.

### Example 3: Python multithreading

```python
# Example 3: Python multithreading

import threading 
  
def print_hello_three_times():
    for i in range(3):
        print("Hello")

def print_hi_three_times(): 
    for i in range(3): 
        print("Hi") 

t1 = threading.Thread(target=print_hello_three_times)  
t2 = threading.Thread(target=print_hi_three_times)  

t1.start()
t2.start()

# When you run the program, the output will be something like below:
```

**Output:**
```text
Hello
Hello
Hello
Hi
Hi
Hi
```

**Explanation:** The above program has two threads **`t1`** and **`t2`**. These threads are run using **`t1.start()`** and **`t2.start()`** statements.

>**Note:** that, **`t1`** and **`t2`** run concurrently and you might get different output.

Visit this page to learn more about **[Multithreading in Python](https://stackoverflow.com/questions/2846653/how-can-i-use-threading-in-python)**.

## `time.sleep()` in multithreaded programs

The **`sleep()`** function suspends execution of the current thread for a given number of seconds.

In case of single-threaded programs, **`sleep()`** suspends execution of the thread and process. However, the function suspends a thread rather than the whole process in multithreaded programs.

### Example 4: `sleep()` in a multithreaded program

```python
# Example 4: sleep() in a multithreaded program

import threading 
import time
  
def print_hello():
    for i in range(4):
        time.sleep(0.5)
        print("Hello")

def print_hi(): 
    for i in range(4): 
        time.sleep(0.7)
        print("Hi") 

t1 = threading.Thread(target=print_hello)  
t2 = threading.Thread(target=print_hi)  
t1.start()
t2.start()
```

**Explanation:** The above program has two threads. We have used **`time.sleep(0.5)`** and **`time.sleep(0.75)`** to suspend execution of these two threads for **0.5** seconds and **0.7** seconds respectively.

**Recommended Reading:** **[Python time.sleep() sleeps thread](https://stackoverflow.com/questions/92928/time-sleep-sleeps-thread-or-process)**

---
