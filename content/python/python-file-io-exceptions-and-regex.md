# Python File I/O, Exception Handling & Regular Expressions

Working with files (reading, writing, appending, modes), directory manipulation with the os module, exception handling (try, except, else, finally, raise), and regex pattern matching.

---

# 05_Python_Files

## Introduction 👋

Python file I/O (a.k.a File handling) is one of the essential topics for programmers and automation testers. It is required to work with files for either writing to a file or read data from it.

Also, if you are not already aware, I/O operations are the costliest operations where a program can stumble. Hence, you should be quite careful while implementing file handling for reporting or any other purpose. Optimizing a single file operation can help you produce a high-performing application or a robust solution for automated software testing.

In Python, file processing takes place in the following order.

* Open a file that returns a filehandle.
* Use the handle to perform read or write action.
* Close the filehandle.

Before you do a read or write operation to a file in Python, you need to open it first. And as the read/write transaction completes, you should close it to free the resources tied with the file.

---

## Table of contents 📋

| **No.** | **Name** | 
| ------- | -------- | 
| 01 | **[Python_File_Input_Output](https://github.com/milaan9/05_Python_Files/blob/main/001_Python_File_Input_Output.ipynb)** |
| 02 | **[Python_File_Directory](https://github.com/milaan9/05_Python_Files/blob/main/002_Python_File_Directory.ipynb)** |
| 03 | **[Python_File_Exception](https://github.com/milaan9/05_Python_Files/blob/main/003_Python_File_Exception.ipynb)** |
| 04 | **[Python_Exceptions_Handling](https://github.com/milaan9/05_Python_Files/blob/main/004_Python_Exceptions_Handling.ipynb)** |
| 05 | **[Python_User_defined_Exceptions](https://github.com/milaan9/05_Python_Files/blob/main/005_Python_User_defined_Exceptions.ipynb)** |

These are online **read-only** versions. However you can **`Run ▶`**  all the codes **online** by clicking here ➞ 

---

## Frequently asked questions ❔

### How can I thank you for writing and sharing this tutorial? 🌷

You can <img src="https://img.shields.io/static/v1?label=%E2%AD%90 Star &message=if%20useful&style=style=flat&color=blue" alt="Star Badge"/> and <img src="https://img.shields.io/static/v1?label=%E2%B5%96 Fork &message=if%20useful&style=style=flat&color=blue" alt="Fork Badge"/> Starring and Forking is free for you, but it tells me and other people that it was helpful and you like this tutorial.

Go [**`here`**](https://github.com/milaan9/05_Python_Files) if you aren't here already and click ➞ **`✰ Star`** and **`ⵖ Fork`** button in the top right corner. You'll be asked to create a GitHub account if you don't already have one.

---

### How can I read this tutorial without an Internet connection? <img alt="GIF" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/hmm.gif" width="20" />

1. Go [**`here`**](https://github.com/milaan9/05_Python_Files) and click the big green ➞ **`Code`** button in the top right of the page, then click ➞ [**`Download ZIP`**](https://github.com/milaan9/05_Python_Files/archive/refs/heads/main.zip).

    ![Download ZIP](img/dnld_rep.png)

2. Extract the ZIP and open it. Unfortunately I don't have any more specific instructions because how exactly this is done depends on which operating system you run.
    
3. Launch ipython notebook from the folder which contains the notebooks. Open each one of them
  
    **`Kernel > Restart & Clear Output`**
    
This will clear all the outputs and now you can understand each statement and learn interactively.

If you have git and you know how to use it, you can also clone the repository instead of downloading a zip and extracting it. An advantage with doing it this way is that you don't need to download the whole tutorial again to get the latest version of it, all you need to do is to pull with git and run ipython notebook again.

---

## Authors ✍️

I'm Dr. Milaan Parmar and I have written this tutorial. If you think you can add/correct/edit and enhance this tutorial you are most welcome🙏

See [github's contributors page](https://github.com/milaan9/05_Python_Files/graphs/contributors) for details.

If you have trouble with this tutorial please tell me about it by [Create an issue on GitHub](https://github.com/milaan9/05_Python_Files/issues/new). and I'll make this tutorial better. This is probably the best choice if you had trouble following the tutorial, and something in it should be explained better. You will be asked to create a GitHub account if you don't already have one.

If you like this tutorial, please [give it a ⭐ star](https://github.com/milaan9/05_Python_Files).

---

## Licence 📜

You may use this tutorial freely at your own risk. See [LICENSE](./LICENSE).

---

## 📘 Python File Input Output
*Source: `5. Python Files/1. Python File Input Output.ipynb`*

# Python File I/O

In this class, you'll learn about Python file operations. More specifically, opening a file, reading from it, writing into it, closing it, and various file methods that you should be aware of.

## Files

Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk).

Since Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off), we use files for future use of the data by permanently storing them.

When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order:
<b>
1. Open a file
2. Close the file
3. Write into files (perform operation)
4. Read contents of files (perform operation)
</b>

## 1. Opening Files in Python

Python has a built-in **`open()`** function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.

```python
>>> f = open("test.txt")  # open file in current directory
>>> f = open("C:/Python99/README.txt")   # specifying full path
```

We can specify the mode while opening a file. In mode, we specify whether we want to read **`r`**, write **`w`** or append **`a`** to the file. We can also specify if we want to open the file in text mode or binary mode.

The default is reading in text mode. In this mode, we get strings when reading from the file.

On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like images or executable files.

| Mode | Description |
|:----:| :--- |
| **`r`** | **Read** -Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.   | 
| **`t`** | **Text** - Opens in text mode. (default).   | 
| **`b`** | **Binary** - Opens in binary mode (e.g. images).  | 
| **`x`** | **Create** - Opens a file for exclusive creation. If the file already exists, the operation fails.   | 
| **`rb`** | Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.   | 
| **`r+`** | Opens a file for both reading and writing. The file pointer placed at the beginning of the file.   | 
| **`rb+`** | Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.   |  
| **`w`** | **Write** - Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.   | 
| **`wb`** | Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.   | 
| **`w+`** | Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.   | 
| **`wb+`** | Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.   | 
| **`a`** | **Append** - Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.   | 
| **`ab`** | Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.   | 
| **`a+`** | Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.   |
| **`ab+`** | Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.   |

```python
f = open("test.txt")   # equivalent to 'r' or 'rt'
print(f)               # <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>
```

As you can see in the example above, I printed the opened file and it gave  some information about it. Opened file has different reading methods: **`read()`**, **`readline`**, **`readlines`**. An opened file has to be closed with **`close()`** method.

```python
f = open("test.txt",'w')  # write in text mode
print(f)
```

```python
f = open("logo.png",'r+b')  # read and write in binary mode
```

Unlike other languages, the character **`a`** does not imply the number 97 until it is encoded using **`ASCII`** (or other equivalent encodings).

Moreover, the default encoding is platform dependent. In windows, it is **`cp1252`** but **`utf-8`** in Linux.

So, we must not also rely on the default encoding or else our code will behave differently in different platforms.

Hence, when working with files in text mode, it is highly recommended to specify the encoding type.

```python
f = open("test.txt", mode='r', encoding='utf-8')
```

## 2. Closing Files in Python

When we are done with performing operations on the file, we need to properly close the file.

Closing a file will free up the resources that were tied with the file. It is done using the **`close()`** method available in Python.

Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.

```python
f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()
```

This method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.

A safer way is to use a **try-finally** block.

```python
try:
    f = open("test.txt", encoding = 'utf-8')
    # perform file operations
finally:
    f.close()
```

This way, we are guaranteeing that the file is properly closed even if an exception is raised that causes program flow to stop.

The best way to close a file is by using the **`with`** statement. This ensures that the file is closed when the block inside the **`with`** statement is exited.

We don't need to explicitly call the **`close()`** method. It is done internally.

```python
>>>with open("test.txt", encoding = 'utf-8') as f:
   # perform file operations
```

### The file Object Attributes

* **file.closed** - Returns true if file is closed, false otherwise.
* **file.mode** - Returns access mode with which file was opened.
* **file.name** - Returns name of the file.

```python
# Open a file
data = open("data.txt", "wb")
print ("Name of the file: ", data.name)
print ("Closed or not : ", data.closed)
print ("Opening mode : ", data.mode)
data.close()  #closed data.txt file
```

**Output:**
```text
Name of the file:  data.txt
Closed or not :  False
Opening mode :  wb
```

## 3. Writing to Files in Python

In order to write into a file in Python, we need to open it in write **`w`**, append **`a`** or exclusive creation **`x`** mode.

We need to be careful with the **`w`** mode, as it will overwrite into the file if it already exists. Due to this, all the previous data are erased.

Writing a string or sequence of bytes (for binary files) is done using the **`write()`** method. This method returns the number of characters written to the file.

```python
with open("test_1.txt",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
```

This program will create a new file named **`test_1.txt`** in the current directory if it does not exist. If it does exist, it is overwritten.

We must include the newline characters ourselves to distinguish the different lines.

```python
with open("test_2.txt",'w',encoding = 'utf-8') as f:
    f.write("This is file\n")
    f.write("my\n")
    f.write("first file\n")
```

Let us append **`a`** some text to the file we have been reading:

```python
with open("test_2.txt",'a',encoding = 'utf-8') as f:
    f.write('This text has to be appended at the end')
```

```python
# open a file in current directory
data = open("data_1.txt", "w") # "w" write in text mode,
data.write("Welcome to Dr. Milan Parmar's Python Tutorial")
print("done")
data.close()
```

**Output:**
```text
done
```

<div>

</div>

## 4. Reading Files in Python

To read a file in Python, we must open the file in reading **`r`** mode.

There are various methods available for this purpose. We can use the **`read(size)`** method to read in the **`size`** number of data. If the **`size`** parameter is not specified, it reads and returns up to the end of the file.

We can read the **`text_1.txt`** file we wrote in the above section in the following way:

```python
f = open("test.txt",'r',encoding = 'utf-8')
txt = f.read()  # read all the characters in the file
print(type(txt))
print(txt)
f.close()
```

```python
f = open("test_1.txt",'r',encoding = 'utf-8')
f.read(8)  # read the first 8 data characters
```

**Output:**
```text
'my first'
```

```python
f.read(5)  # read the next 5 data characters
```

**Output:**
```text
' file'
```

```python
f.read()  # read in the rest till end of file
```

**Output:**
```text
'\nThis file\n\ncontains three lines\n'
```

```python
f.read()  # further reading returns empty sting
```

**Output:**
```text
''
```

We can see that the **`read()`** method returns a newline as **`'\n'`**. Once the end of the file is reached, we get an empty string on further reading.

We can change our current file cursor (position) using the **`seek()`** method. Similarly, the **`tell()`** method returns our current position (in number of bytes).

```python
f.tell()    # get the current file position
```

**Output:**
```text
50
```

```python
f.seek(0)   # bring file cursor to initial position
```

**Output:**
```text
0
```

```python
print(f.read())  # read the entire file
```

**Output:**
```text
my first file
This file

contains three lines
```

We can read a file line-by-line using a **for loop**. This is both efficient and fast.

```python
f = open("test_1.txt",'r',encoding = 'utf-8')
for line in f:
    print(line, end = '')
```

**Output:**
```text
my first file
This file

contains three lines
```

In this program, the lines in the file itself include a newline character **`\n`**. So, we use the end parameter of the **`print()`** function to avoid two newlines when printing.

Alternatively, we can use the **`readline()`** method to read individual lines of a file. This method reads a file till the newline, including the newline character.

```python
f.seek(0)  # bring file cursor to initial position
f.readline()
```

**Output:**
```text
'my first file\n'
```

```python
f.readline()
```

**Output:**
```text
'This file\n'
```

```python
f.readline()
```

**Output:**
```text
'\n'
```

```python
f.readline()
```

**Output:**
```text
'contains three lines\n'
```

Lastly, the **`readlines()`** method returns a list of remaining lines of the entire file. All these reading methods return empty values when the end of file **(EOF)** is reached.

```python
f.seek(0)  # bring file cursor to initial position
f.readlines()
```

**Output:**
```text
['my first file\n', 'This file\n', '\n', 'contains three lines\n']
```

Another way to get all the lines as a list is using **`splitlines()`**

```python
f.seek(0)  # bring file cursor to initial position
f.read().splitlines()
```

**Output:**
```text
['my first file', 'This file', '', 'contains three lines']
```

```python
# Open a file
data = open("data_1.txt", "r+")
file_data = data.read(27) # read 3.375 byte only
full_data = data.read()   # read all byte into file from last cursor
print(file_data)
print(full_data)
data.close()
```

**Output:**
```text
Welcome to Dr. Milan Parmar
's Python Tutorial
```

## File Positions

The **`tell()`** method tells you the current position within the file; in other words, the next read or write will occur at that many bytes from the beginning of the file.

The **`seek(offset[, from])`** method changes the current file position. The offset argument indicates the number of bytes to be moved. The from argument specifies the reference position from where the bytes are to be moved.

If from is set to 0, the beginning of the file is used as the reference position. If it is set to 1, the current position is used as the reference position. If it is set to 2 then the end of the file would be taken as the reference position.

```python
# Open a file
data = open("data_1.txt", "r+")
file_data = data.read(27) # read 18 byte only
print("current position after reading 27 byte :",data.tell())
data.seek(0) #here current position set to 0 (starting of file)
full_data = data.read() #read all byte
print(file_data)
print(full_data)
print("position after reading file : ",data.tell())
data.close()
```

**Output:**
```text
current position after reading 27 byte : 27
Welcome to Dr. Milan Parmar
Welcome to Dr. Milan Parmar's Python Tutorial
position after reading file :  45
```

## Python File Methods

There are various methods available with the file object. Some of them have been used in the above examples.

Here is the complete list of methods in text mode with a brief description:

| Method | Description |
|:----| :--- |
| **`close()`** |   Closes an opened file. It has no effect if the file is already closed.   | 
| **`detach()`** |   Separates the underlying binary buffer from the **`TextIOBase`** and returns it.   | 
| **`fileno()`** |   Returns an integer number (file descriptor) of the file.   | 
| **`flush()`** |   Flushes the write buffer of the file stream.   | 
| **`isatty()`** |   Returns **`True`** if the file stream is interactive.   | 
| **`read(n)`** |   Reads at most `n` characters from the file. Reads till end of file if it is negative or `None`.   | 
| **`readable()`** |   Returns **`True`** if the file stream can be read from.   | 
| **`readline(n=-1)`** |   Reads and returns one line from the file. Reads in at most **`n`** bytes if specified.   | 
| **`readlines(n=-1)`** |   Reads and returns a list of lines from the file. Reads in at most **`n`** bytes/characters if specified.   | 
| **`seek(offset,from=SEEK_SET)`** |   Changes the file position to **`offset`** bytes, in reference to `from` (start, current, end).   | 
| **`seekable()`** |   Returns **`True`** if the file stream supports random access.   | 
| **`tell()`** |   Returns the current file location.   | 
| **`truncate(size=None)`** |   Resizes the file stream to **`size`** bytes. If **`size`** is not specified, resizes to current location..   | 
| **`writable()`** |   Returns **`True`** if the file stream can be written to.   | 
| **`write(s)`** |   Writes the string **`s`** to the file and returns the number of characters written..   | 
| **`writelines(lines)`** |   Writes a list of **`lines`** to the file..   |

## Deleting Files

We have seen in previous section, how to make and remove a directory using **os** module (04_Python_Functions ➞ 007_Python_Function_Module ➞ Python Built-In Modules). Again now, if we want to remove a file we use **`os`** module.

```python
import os
os.remove('example.txt')
```

If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:

```python
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

**Output:**
```text
The file does not exist
```

## File Types

### File with txt Extension

File with **txt** extension is a very common form of data and we have covered it in the previous section. Let us move to the JSON file.

### File with json Extension

**JSON** stands for **J**ava**S**cript **O**bject **N**otation. Actually, it is a stringified JavaScript object or Python dictionary.

```python
# dictionary
person_dct= {
    "name":"Milaan",
    "country":"England",
    "city":"London",
    "skills":["Python", "MATLAB","R"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Milaan', 'country': 'England', 'city': 'London', 'skills': ['Python', 'MATLAB','R']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Milaan",
    "country":"England",
    "city":"London",
    "skills":["Python", "MATLAB","R"]
}'''
```

### Changing JSON to Dictionary

To change a JSON to a dictionary, first we import the json module and then we use **`loads`** method.

```python
import json
# JSON
person_json = '''{
    "name":"Milaan",
    "country":"England",
    "city":"London",
    "skills":["Python", "MATLAB","R"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

### Changing Dictionary to JSON

To change a dictionary to a JSON we use **`dumps`** method from the json module.

```python
import json
# python dictionary
person = {
    "name":"Milaan",
    "country":"England",
    "city":"London",
    "skills":["Python", "MATLAB","R"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

# when you print it, it does not have the quote, but actually it is a string
# JSON does not have type, it is a string type.
```

### Saving as JSON File

We can also save our data as a json file. Let us save it as a json file using the following steps. For writing a json file, we use the **`json.dump()`** method, it can take dictionary, output file, **`ensure_ascii`** and **`indent`**.

```python
import json
# python dictionary
person = {
    "name":"Milaan",
    "country":"England",
    "city":"London",
    "skills":["Python", "MATLAB","R"]
}
with open('json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

In the code above, we use encoding and indentation. Indentation makes the json file easy to read.

### File with csv Extension

**CSV** stands for **C**omma **S**eparated **V**alues. CSV is a simple file format used to store tabular data, such as a spreadsheet or database. CSV is a very common data format in data science.

For example, create **csv_example.csv** in your working directory with the following contents:

```csv
"name","country","city","skills"
"Milaan","England","London","Python"
```

```python
import csv
with open('csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
```

**Output:**
```text
Column names are :name, country, city, skills
	Milaan is a teachers. He lives in England, London.
Number of lines:  2
```

### File with xlsx Extension

To read excel files we need to install **`xlrd`** package. We will cover this after we cover package installing using **pip**.

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls)
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### File with xml Extension

**XML** is another structured data format which looks like HTML. In XML the tags are not predefined. The first line is an XML declaration. The person tag is the root of the XML. The person has a gender attribute.

```xml
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```

For more information on how to read an XML file check the **[documentation](https://docs.python.org/2/library/xml.etree.elementtree.html)**

```python
import xml.etree.ElementTree as ET
tree = ET.parse('xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
```

**Output:**
```text
Root tag: person
Attribute: {'gender': 'male'}
field:  name
field:  country
field:  city
field:  skills
```

## 💻 Exercises ➞ <span class='label label-default'>Files</span>

### Exercises ➞ <span class='label label-default'>Level 1</span>

1. Write a function which count number of lines and number of words in a text.
  - a) Read **speech_barack_obama.txt** file and count number of lines and words
  - b) Read **speech_michelle_obama.txt** file and count number of lines and words
  - c) Read **speech_donald_trump.txt** file and count number of lines and words
  - d) Read **speech_melina_trump.txt** file and count number of lines and words
    
2. Read the **countries_data.json** data file in data directory, create a function that finds the ten most spoken languages

    - ```py
   # Your output should look like this:
   print(most_spoken_languages(filename='./countries_data.json', 10))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic'),
   (24, 'Spanish'),
   (9, 'Russian'),
   (9, 'Portuguese'),
   (8, 'Dutch'),
   (7, 'German'),
   (5, 'Chinese'),
   (4, 'Swahili'),
   (4, 'Serbian')]
   # Your output should look like this:
   print(most_spoken_languages(filename='./countries_data.json', 3))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic')]
   ```

3. Read the **countries_data.json** data file and create a function that creates a list of the ten most populated countries

    - ```py
   # Your output should look like this:
   print(most_populated_countries(filename='./countries_data.json', 10))
   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000},
   {'country': 'Indonesia', 'population': 258705000},
   {'country': 'Brazil', 'population': 206135893},
   {'country': 'Pakistan', 'population': 194125062},
   {'country': 'Nigeria', 'population': 186988000},
   {'country': 'Bangladesh', 'population': 161006790},
   {'country': 'Russian Federation', 'population': 146599183},
   {'country': 'Japan', 'population': 126960000}
   ]
   # Your output should look like this:
   print(most_populated_countries(filename='./countries_data.json', 3))
   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000}
   ]
   ```


### Exercises ➞ <span class='label label-default'>Level 2</span>

1. Extract all incoming email addresses as a list from the **email_exchanges_big.txt** file.

2. Find the most common words in the English language. Call the name of your function **`find_most_common_words`**, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

    - ```py
    # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
    ```

3. Use the function, find_most_frequent_words to find:
  - a) The ten most frequent words used in **[Barack Obama's Speech.txt](https://github.com/milaan9/05_Python_Files/blob/main/speech_barack_obama.txt)**
  - b) The ten most frequent words used in **[Michelle Obama's Speech.txt ](https://github.com/milaan9/05_Python_Files/blob/main/speech_michelle_obama.txt)**
  - c) The ten most frequent words used in **[Donald Trump's Speech.txt](https://github.com/milaan9/05_Python_Files/blob/main/speech_donald_trump.txt)**
  - d) The ten most frequent words used in **[Melina Trump's Speech.txt](https://github.com/milaan9/05_Python_Files/blob/main/speech_melina_trump.txt)**
  
4. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of **Michelle Obama's Speech.txt** and **Melina Trump's Speech.txt** speech. You may need a couple of functions, function to clean the text (**`clean_text`**), function to remove support words (**`remove_support_words`**) and finally to check the similarity (**`check_text_similarity`**). List of **support_words**.

5. Find the 10 most repeated words in the **romeo_and_juliet.txt**.

6. Read the **hacker_news.csv** file and find out:
  - a) Count the number of lines containing **`python`** or **`Python`**
  - b) Count the number lines containing **`JavaScript`**, **`javascript`** or **`Javascript`**
  - c) Count the number lines containing **`Java`** and not **`JavaScript`**

---

## 📘 Python File Directory
*Source: `5. Python Files/2. Python File Directory.ipynb`*

# Python Directory and Files Management

In this class, you'll learn about file and directory management in Python, i.e. creating a directory, renaming it, listing all directories, and working with them.

## Python Directory

If there are a large number of **files** to handle in our Python program, we can arrange our code within different directories to make things more manageable.

A directory or folder is a collection of files and subdirectories. Python has the **`os`** **module** that provides us with many useful methods to work with directories (and files as well).

### Get Current Directory `getcwd()` - 

We can get the present working directory using the **`getcwd()`** method of the os module.

This method returns the current working directory in the form of a string. We can also use the **`getcwd()`** method to get it as bytes object.

```python
import os
print(os.getcwd())
```

**Output:**
```text
C:\Users\Deepak\01_Learn_Python4Data\05_Python_Files
```

```python
import os
os.getcwdb()
```

**Output:**
```text
b'C:\\Users\\Deepak\\01_Learn_Python4Data\\05_Python_Files'
```

The extra backslash implies an escape sequence. The **`print()`** function will render this properly.

### Changing Directory `chdir()` - 

We can change the current working directory by using the **`chdir()`** method.

The new path that we want to change into must be supplied as a string to this method. We can use both the forward-slash **`/`** or the backward-slash **`\`** to separate the path elements.

It is safer to use an escape sequence when using the backward slash.

**Syntax:**

**`os.chdir("newdir")`**

>**Remember to**: 
1. First copy the path for current working directory 
2. Windows user and MacOS users, first create an empty folder with name "**xyz**" on your desktop.

```python
import os

# Changing a directory to "C:\Users\Deepak\OneDrive\Desktop\xyz"
os.chdir(r"C:\Users\Deepak\OneDrive\Desktop\xyz") 
  
print("Directory changed") 

print(os.getcwd())
```

**Output:**
```text
Directory changed
C:\Users\Deepak\OneDrive\Desktop\xyz
```

```python
import os
print(os.getcwd())
```

**Output:**
```text
C:\Users\Deepak\OneDrive\Desktop\xyz
```

```python
import os

# Changing a directory back to original directory "C:\Users\Deepak\01_Learn_Python4Data\05_Python_Files"
os.chdir(r"C:\Users\Deepak\01_Learn_Python4Data\05_Python_Files") 
  
print("Directory changed")
```

**Output:**
```text
Directory changed
```

```python
import os
print(os.getcwd())
```

**Output:**
```text
C:\Users\Deepak\01_Learn_Python4Data\05_Python_Files
```

### List Directories and Files `listdir()` - 

The **`listdir()`** method displays all files and sub-directories inside a directory.

This method takes in a path and returns a list of subdirectories and files in that path. If no path is specified, it returns the list of subdirectories and files from the current working directory.

```python
print(os.getcwd())

os.listdir()
```

**Output:**
```text
C:\Users\Deepak\01_Learn_Python4Data\05_Python_Files
['.ipynb_checkpoints',
 '001_Python_File_Input_Output.ipynb',
 '002_Python_File_Directory.ipynb',
 '003_Python_File_Exception.ipynb',
 '004_Python_Exceptions_Handling.ipynb',
 '005_Python_User_defined_Exceptions.ipynb',
 'data.txt',
 'data_1.txt',
 'img',
 'logo.png',
 'logo1.png',
 'test.txt',
 'testfile',
 'test_1.txt',
 'test_2.txt']
```

```python
os.listdir('C:\\')
```

**Output:**
```text
['$Recycle.Bin',
 '$WinREAgent',
 '$WINRE_BACKUP_PARTITION.MARKER',
 'bootTel.dat',
 'Documents and Settings',
 'DumpStack.log',
 'DumpStack.log.tmp',
 'hiberfil.sys',
 'ImDisk',
 'OneDriveTemp',
 'pagefile.sys',
 'PerfLogs',
 'Program Files',
 'Program Files (x86)',
 'ProgramData',
 'Python99',
 'Recovery',
 'swapfile.sys',
 'System Volume Information',
 'Users',
 'Windows']
```

### Making a New Directory `mkdir()` - 

You can use the **`mkdir()`** method of the os module to create directories in the current directory. You need to supply an argument to this method, which contains the name of the directory to be created.

This method takes in the path of the new directory. If the full path is not specified, the new directory is created in the current working directory.

**Syntax:**

**`os.mkdir("dir_name")`**

```python
import os
os.mkdir('python_study')
print("Directory created") 

os.listdir()
```

**Output:**
```text
Directory created
['.ipynb_checkpoints',
 '001_Python_File_Input_Output.ipynb',
 '002_Python_File_Directory.ipynb',
 '003_Python_File_Exception.ipynb',
 '004_Python_Exceptions_Handling.ipynb',
 '005_Python_User_defined_Exceptions.ipynb',
 'data.txt',
 'data_1.txt',
 'img',
 'logo.png',
 'logo1.png',
 'python_study',
 'test.txt',
 'testfile',
 'test_1.txt',
 'test_2.txt']
```

### Renaming a Directory or a File `rename()` - 

The **`rename()`** method can rename a directory or a file.

**Syntax:**

**`os.rename(current_file_name, new_file_name)`**

```python
os.listdir()

os.rename('python_study','python_learning')
print("Directory renamed") 

os.listdir()
```

**Output:**
```text
Directory renamed
['.ipynb_checkpoints',
 '001_Python_File_Input_Output.ipynb',
 '002_Python_File_Directory.ipynb',
 '003_Python_File_Exception.ipynb',
 '004_Python_Exceptions_Handling.ipynb',
 '005_Python_User_defined_Exceptions.ipynb',
 'data.txt',
 'data_1.txt',
 'img',
 'logo.png',
 'logo1.png',
 'python_learning',
 'test.txt',
 'testfile',
 'test_1.txt',
 'test_2.txt']
```

```python
import os
os.rename('data_1.txt','my_data.txt')
print("file renamed")
```

**Output:**
```text
file renamed
```

<div>

</div>

### Removing a Directory or a File `remove()` and `rmdir()` - 

A file can be removed (deleted) using the **`remove()`** method.
Similarly, the **`rmdir()`** method removes an empty directory. Before removing a directory, all the contents in it should be removed.

```python
import os

# This would remove "C:\Users\Deepak\OneDrive\Desktop\xyz" directory.
os.rmdir(r"C:\Users\Deepak\OneDrive\Desktop\xyz")
print("Directory deleted") 

os.listdir()
```

**Output:**
```text
Directory deleted
['.ipynb_checkpoints',
 '001_Python_File_Input_Output.ipynb',
 '002_Python_File_Directory.ipynb',
 '003_Python_File_Exception.ipynb',
 '004_Python_Exceptions_Handling.ipynb',
 '005_Python_User_defined_Exceptions.ipynb',
 'data.txt',
 'img',
 'logo.png',
 'logo1.png',
 'my_data.txt',
 'python_learning',
 'test.txt',
 'testfile',
 'test_1.txt',
 'test_2.txt']
```

```python
import os
os.remove('my_data.txt')
print("file deleted")
```

**Output:**
```text
file deleted
```

>**Note**: The **`rmdir()`** method can only remove empty directories.

In order to remove a non-empty directory, we can use the **`rmtree()`** method inside the **`shutil`** module.

```python
import shutil

shutil.rmtree('python_learning')
os.listdir()
```

**Output:**
```text
['.ipynb_checkpoints',
 '001_Python_File_Input_Output.ipynb',
 '002_Python_File_Directory.ipynb',
 '003_Python_File_Exception.ipynb',
 '004_Python_Exceptions_Handling.ipynb',
 '005_Python_User_defined_Exceptions.ipynb',
 'data.txt',
 'img',
 'logo.png',
 'logo1.png',
 'test.txt',
 'testfile',
 'test_1.txt',
 'test_2.txt']
```

---

## 📘 Python File Exception
*Source: `5. Python Files/3. Python File Exception.ipynb`*

# Python Errors and Built-in Exceptions

In this class, you will learn about different types of errors and exceptions that are built-in to Python. They are raised whenever the Python interpreter encounters errors.

We can make certain mistakes while writing a program that lead to errors when we try to run it. A python program terminates as soon as it encounters an unhandled error. These errors can be broadly classified into two classes:

1. Syntax errors
2. Logical errors (Exceptions)

## 1. Python Syntax Errors

Error caused by not following the proper structure (syntax) of the language is called **syntax error** or **parsing error**.

```python
# Example 1:

if a < 3
```

**Exaplanation:**

As shown in the example, an arrow indicates where the parser ran into the syntax error.

We can notice here that a colon **`:`** is missing in the **`if`** statement.

```python
# Example 2:

print 'hello world'
```

**Exaplanation:**

As you can see we made a syntax error because we forgot to enclose the string with parenthesis **`()`** and Python already suggests the solution. Let us fix it.

## 2. Python Logical Errors (Exceptions)

Errors that occur at runtime (after passing the syntax test) are called **exceptions** or **logical errors**.

For instance, they occur when we try to open a file(for reading) that does not exist (**`FileNotFoundError`**), try to divide a number by zero (**`ZeroDivisionError`**), or try to import a module that does not exist (**`ImportError`**).

Whenever these types of runtime errors occur, Python creates an exception object. If not handled properly, it prints a traceback to that error along with some details about why that error occurred.

Let's look at how Python treats these errors:

```python
# Example 1: ZeroDivisionError

1 / 0
```

```python
# Example 2: FileNotFoundError

open("imaginary.txt")
```

```python
# Example 3: ImportError

from math import power
```

**Exaplanation:**

There is no function called **`power`** in the **`math`** module, it goes with a different name: **`pow`**.

## 3. Python NameError

We debugged the error by defining the variable name.

```python
# Example 1:

print(age)
```

**Exaplanation:**

As you can see from the message above, name **`age`** is not defined. Yes, it is true that we did not define an **`age`** variable but we were trying to print it out as if we had had declared it. Now, lets fix this by declaring it and assigning with a value.

## 4. Python IndexError

We debugged the error by defining the variable name.

```python
# Example 1:

numbers = [1, 2, 3, 4, 5]
numbers[5]
```

**Exaplanation:**

In the example above, Python raised an **`IndexError`**, because the list has only indexes from 0 to 4 , so it was out of range.

## 5. Python ModuleNotFoundError

```python
# Example 1:

import maths
```

**Exaplanation:**

In the example above, I added an extra **`s`** to math deliberately and **`ModuleNotFoundError`** was raised. Lets fix it by removing the extra **`s`** from math.

## 6. Python AttributeError

```python
# Example 1:

import math
math.PI
```

**Exaplanation:**

As you can see, I made a mistake again! Instead of **`pi`**, I tried to call a **`PI`** function from **`math`** module. It raised an **`AttributeError`**, it means, that the function does not exist in the module. Lets fix it by changing from **`PI`** to **`pi`**.

## 7. Python KeyError

```python
# Example 1:

users = {'name':'Milaan', 'age':96, 'country':'England'}
users['name']
```

**Output:**
```text
'Milaan'
```

```python
users['county']
```

**Exaplanation:**

As you can see, there was a typo in the key used to get the dictionary value. so, this is a **`KeyError`** and the fix is quite straight forward. Let's do this!

## 8. Python TypeError

```python
# Example 1:

6 + '3'
```

**Exaplanation:**

In the example above, a **`TypeError`** is raised because we cannot add a number to a string. First solution would be to convert the string to **int** or **float**. Another solution would be converting the number to a string (the result then would be '63'). Let us follow the first fix.

## 9. Python ValueError

```python
# Example 1:

int('19a')
```

**Exaplanation:**

In this case we cannot change the given string to a number, because of the **`a`** letter in it.

## Python Built-in Exceptions

Illegal operations can raise exceptions. There are plenty of built-in exceptions in Python that are raised when corresponding errors occur. We can view all the built-in exceptions using the built-in **`local()`** function as follows:

```python
print(dir(locals()['__builtins__']))
```

**`locals()['__builtins__']`** will return a module of built-in exceptions, functions, and attributes. **`dir`** allows us to list these attributes as strings.

Some of the common built-in exceptions in Python programming along with the error that cause them are listed below:

| Exception | Cause of Error |
|:----| :--- |
| **`AssertionError`** |   Raised when an **`assert`** statement fails.   | 
| **`AttributeError`** |   Raised when attribute assignment or reference fails.   | 
| **`EOFError`** |   Raised when the **`input()`** function hits end-of-file condition.   | 
| **`FloatingPointError`** |   Raised when a floating point operation fails.   | 
| **`GeneratorExit`** |   Raise when a generator's **`close()`** method is called.   | 
| **`ImportError`** |   Raised when the imported module is not found.   | 
| **`IndexError`** |   Raised when the index of a sequence is out of range.   | 
| **`KeyError`** |   Raised when a key is not found in a dictionary.   | 
| **`KeyboardInterrupt`** |   Raised when the user hits the interrupt key (**`Ctrl+C`** or **`Delete`**).   | 
| **`MemoryError`** |   Raised when an operation runs out of memory.   | 
| **`NameError`** |   Raised when a variable is not found in local or global scope.   | 
| **`NotImplementedError`** |   Raised by abstract methods.   | 
| **`OSError`** |   Raised when system operation causes system related error.   | 
| **`OverflowError`** |   Raised when the result of an arithmetic operation is too large to be represented.   | 
| **`ReferenceError`** |   Raised when a weak reference proxy is used to access a garbage collected referent.   | 
| **`RuntimeError`** |   Raised when an error does not fall under any other category.   | 
| **`StopIteration`** |   Raised by **`next()`** function to indicate that there is no further item to be returned by iterator.   | 
| **`SyntaxError`** |   Raised by parser when syntax error is encountered.   | 
| **`IndentationError`** |   Raised when there is incorrect indentation.   | 
| **`TabError`** |   Raised when indentation consists of inconsistent tabs and spaces.   | 
| **`SystemError`** |   Raised when interpreter detects internal error.   | 
| **`SystemExit`** |   Raised by **`sys.exit()`** function.   | 
| **`TypeError`** |   Raised when a function or operation is applied to an object of incorrect type.   | 
| **`UnboundLocalError`** |   Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.   | 
| **`UnicodeError`** |   Raised when a Unicode-related encoding or decoding error occurs.   | 
| **`UnicodeEncodeError`** |   Raised when a Unicode-related error occurs during encoding.   | 
| **`UnicodeDecodeError`** |   Raised when a Unicode-related error occurs during decoding.   | 
| **`UnicodeTranslateError`** |   Raised when a Unicode-related error occurs during translating.   | 
| **`ValueError`** |   Raised when a function gets an argument of correct type but improper value.   | 
| **`ZeroDivisionError`** |   Raised when the second operand of division or modulo operation is zero.   |

If required, we can also define our own exceptions in Python. To learn more about them, visit Python **User-defined Exceptions**.

We can handle these built-in and user-defined exceptions in Python using **`try`**, **`except`** and **`finally`** statements. To learn more about them, visit **Python try, except and finally statements**.

## 💻 Exercises ➞ <span class='label label-default'>Python Errors</span>

1. Open you Jupyter Notebook and try all the examples covered in this section.

---

## 📘 Python Exceptions Handling
*Source: `5. Python Files/4. Python Exceptions Handling.ipynb`*

# Python Exceptions Handling Using `try`, `except` and `finally` statement

In this class, you'll learn how to handle exceptions in your Python program using try, except and finally statements with the help of examples.

## Exceptions in Python

An **exception** is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. An exception is a Python object that **represents an error**.

Python has many **built-in exceptions** that are raised when your program encounters an error (something in the program goes wrong).

When a Python script raises an exception, it must either handle the exception immediately otherwise it **terminates** and **quits**.

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

For example, let us consider a program where we have a function **`A`** that calls **function** **`B`**, which in turn calls function **`C`**. If an exception occurs in function **`C`** but is not handled in **`C`**, the exception passes to **`B`** and then to **`A`**.

If never handled, an error message is displayed and our program comes to a sudden unexpected halt.

## Catching Exceptions in Python

In Python, exceptions can be handled using a **`try`** statement.

The critical operation which can raise an exception is placed inside the **`try`** clause. The code that handles the exceptions is written in the **`except`** clause.

We can thus choose what operations to perform once we have caught the exception. Here is a simple example.

```python
# Example 1:

try:
    print(10 + '5')
except:
    print('Something went wrong')
```

**Output:**
```text
Something went wrong
```

**Explanation:**

In the example above the second operand is a string. We could change it to float or int to add it with the number to make it work. But without any changes, the second block, **`except`**, will be executed.

```python
# Example 2:

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)
```

**Output:**
```text
The entry is a
Oops! <class 'ValueError'> occurred.
Next entry.

The entry is 0
Oops! <class 'ZeroDivisionError'> occurred.
Next entry.

The entry is 2
The reciprocal of 2 is 0.5
```

**Explanation:**

In this program, we loop through the values of the **`randomList`** list. As previously mentioned, the portion that can cause an exception is placed inside the **`try`** block.

If no exception occurs, the **`except`** block is skipped and normal flow continues(for last value). But if any exception occurs, it is caught by the **`except`** block (first and second values).

Here, we print the name of the exception using the **`exc_info()`** function inside sys module. We can see that a causes **`ValueError`** and **`0`** causes **`ZeroDivisionError`**.

Since every exception in Python inherits from the base **`Exception`** class, we can also perform the above task in the following way:

```python
# Example 3:

# This program has the same output as the above program.

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)
```

**Output:**
```text
The entry is a
Oops! <class 'ValueError'> occurred.
Next entry.

The entry is 0
Oops! <class 'ZeroDivisionError'> occurred.
Next entry.

The entry is 2
The reciprocal of 2 is 0.5
```

```python
# Example 4:

try:
    name = input('Enter your name: ')
    year_born = input('Year you were born: ')
    age = 2022 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
```

**Output:**
```text
Enter your name: Milaan
Year you were born: 1926
Something went wrong
```

**Explanation:**

In the above example, the exception block will run and we do not know exactly the problem. To analyze the problem, we can use the different error types with except.

In the following example, it will handle the error and will also tell us the kind of error raised.

```python
# Example 5:

try:
    name = input('Enter your name: ')
    year_born = input('Year you were born: ')
    age = 2022 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
```

**Output:**
```text
Enter your name: Milaan
Year you were born: 1926
Type error occured
```

## Catching Specific Exceptions in Python

In the above example, we did not mention any specific exception in the **`except`** clause.

This is not a good programming practice as it will catch all exceptions and handle every case in the same way. We can specify which exceptions an **`except`** clause should catch.

A **`try`** clause can have any number of **`except`** clauses to handle different exceptions, however, only one will be executed in case an exception occurs.

We can use a tuple of values to specify multiple exceptions in an **`except`** clause. Here is an example pseudo code.

```python
>>> try:
>>>    # do something
>>>    pass

>>> except ValueError:
>>>    # handle ValueError exception
>>>    pass

>>> except (TypeError, ZeroDivisionError):
>>>    # handle multiple exceptions
>>>    # TypeError and ZeroDivisionError
>>>    pass

>>> except:
>>>    # handle all other exceptions
>>>    pass
```

## Raising Exceptions in Python

In Python programming, exceptions are raised when errors occur at runtime. We can also manually **`raise`** exceptions using the raise keyword.

We can optionally pass values to the exception to clarify why that exception was raised.

```python
raise KeyboardInterrupt
```

```python
raise MemoryError("This is an argument")
```

```python
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
```

**Output:**
```text
Enter a positive integer: 9
```

### Python `try` with `else` clause

In some situations, you might want to run a certain block of code if the code block inside `try` ran without any errors. For these cases, you can use the optional `else` keyword with the `try` statement.

>**Note**: Exceptions in the else clause are not handled by the preceding except clauses.

```python
>>> try:
>>>    You do your operations here
>>>    ......................
>>> except ExceptionI:
>>>    If there is ExceptionI, then execute this block.
>>> except ExceptionII:
>>>    If there is ExceptionII, then execute this block.
>>>    ......................
>>> else:
>>>    If there is no exception then execute this block.
```

With our **“Hello, World!”** program written, we are ready to run the program. We’ll use the python3 command along with the name of our program file. Let’s run the program:

* A single try statement can have multiple except statements. This is useful when the **try block** contains statements that may throw different types of exceptions.

* You can also provide a **generic except** clause, which handles any exception. 

* After the **except** clause(s), you can include an else-clause. The code in the else-block executes if the code in the try: block does not raise an exception. 

* The **else-block** is a good place for code that does not need the try: block's protection.

```python
# Example 1:

try:
    fh = open("testfile.txt", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print ("Error: can\'t find file or read data")
else:
    print ("Written content in the file successfully")
    fh.close()
```

**Output:**
```text
Written content in the file successfully
```

<div>

</div>

```python
# Example 2: program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
```

**Output:**
```text
Enter a number: 63
Not an even number!
```

**Explanation**:

If we pass an odd number:

```python
Enter a number: 1
Not an even number!
```

If we pass an even number, the reciprocal is computed and displayed.

```python
Enter a number: 4
0.25
```

However, if we pass 0, we get **`ZeroDivisionError`** as the code block inside else is not handled by preceding except.

```python
Enter a number: 0
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    reciprocal = 1/num
ZeroDivisionError: division by zero
```

## The `except` Clause with No Exceptions

You can also use the except statement with no exceptions defined as follows

```python
>>> try:
>>>    You do your operations here
>>>    ......................
>>> except:
>>>    If there is any exception, then execute this block.
>>>    ......................
>>> else:
>>>    If there is no exception then execute this block
```

This kind of a **try-except** statement catches all the exceptions that occur. Using this kind of try-except statement is not considered a good programming practice though, because it catches all exceptions but does not make the programmer identify the root cause of the problem that may occur.

## The `except` Clause with Multiple Exceptions

You can also use the same except statement to handle multiple exceptions as follows −

```python
>>>try:
>>>   You do your operations here
>>>   ......................
>>>except(Exception1[, Exception2[,...ExceptionN]]]):
>>>   If there is any exception from the given exception list,
>>>   then execute this block.
>>>   ......................
>>>else:
>>>   If there is no exception then execute this block.
```

## Python `try`-`finally` Clause

The **`try`** statement in Python can have an optional **`finally`** clause. This clause is executed no matter what, and is generally used to release external resources.

For example, we may be connected to a remote data center through the network or working with a file or a Graphical User Interface (GUI).

In all these circumstances, we must clean up the resource before the program comes to a halt whether it successfully ran or not. These actions (closing a file, GUI or disconnecting from network) are performed in the **`finally`** clause to guarantee the execution.

You can use a **finally: block** along with a try: block. The finally: block is a place to put any code that must execute, whether the **try-block** raised an exception or not. The syntax of the **try-finally** statement is this −

```python
>>> try:
>>>    You do your operations here;
>>>     ......................
>>>    Due to any exception, this may be skipped.
>>> finally:
>>>    This would always be executed.
>>>    ......................
```

>**Note**: You can provide except clause(s), or a finally clause, but not both. You cannot use else clause as well along with a **finally clause**.

```python
try:
    fh = open("testfile.txt", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print ("Error: can\'t find file or read data")
    fh.close()
    
# If you do not have permission to open the file in writing mode, 
# then this will produce the following result −
```

**Output:**
```text
Error: can't find file or read data
```

```python
try:
    f = open("testfile.txt",encoding = 'utf-8')
    # perform file operations
finally:
    f.close()
```

**Explanation**:

This type of construct makes sure that the file is closed even if an exception occurs during the program execution.

In the **# Example 5:** code above the output is going to be **`TypeError`**.
Now, let's add an additional block:

```python
# Example:

try:
    name = input('Enter your name: ')
    year_born = input('Year you born: ')
    age = 2022 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
```

**Output:**
```text
Enter your name: Milaan
Year you born: 1926
You are Milaan. And your age is 96.
I usually run with the try block
I alway run.
```

It is also shorten the above code as follows:

```python
try:
    name = input('Enter your name: ')
    year_born = input('Year you born: ')
    age = 2022 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
```

**Output:**
```text
Enter your name: Milaan
Year you born: 1926
You are Milaan. And your age is 96.
```

## Argument of an Exception

An exception can have an **argument**, which is a value that gives additional information about the problem. The contents of the argument vary by exception. You capture an exception's argument by supplying a variable in the except clause as follows −

```python
# Define a function here.
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz")
```

**Output:**
```text
The argument does not contain numbers
 invalid literal for int() with base 10: 'xyz'
```

## Raising an Exception

You can raise exceptions in several ways by using the **`raise`** statement. 

The general syntax for the **`raise`** statement is as follows:

```python
raise [Exception [, args [, traceback]]]
```

Here, Exception is the type of exception (for example, **NameError**) and argument is a value for the exception argument. The argument is optional; if not supplied, the exception argument is None.

The final argument, traceback, is also optional (and rarely used in practice), and if present, is the traceback object used for the exception.

```python
def functionName( level ):
    if level < 1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception
    return level

try:
    l = functionName(-10)
    print ("level = ",l)
except Exception as e:
    print ("error in level argument",e.args[0])
```

**Output:**
```text
error in level argument -10
```

## Writing the “Hello, World!” Program

Python also allows you to create your own exceptions by deriving classes from the standard **built-in exceptions**.

Here is an example related to **RuntimeError**. Here, a class is created that is subclassed from RuntimeError. This is useful when you need to display more **specific information** when an exception is caught.

In the try block, the user-defined exception is raised and caught in the except block. The variable e is used to create an instance of the class **Networkerror**.

```python
>>> class Networkerror(RuntimeError):
>>>     def _init_(self, arg):
>>>        self.args = arg
```
       
So once you have defined the above class, you can raise the exception as follows −

```python
>>> try:
>>>    raise Networkerror("Bad hostname")
>>> except Networkerror,e:
>>>    print(e.args)
```

## Packing and Unpacking Arguments in Python

We use two operators:

- **`*`** for tuples
- __`**`__ for dictionaries

Let us take as an example below. It takes only arguments but we have list. We can unpack the list and changes to argument.

### Unpacking

#### Unpacking Lists

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

When we run the above code, it raises an error, because this function takes numbers (not a list) as arguments. Let us unpack/destructure the list.

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

**Output:**
```text
15
```

We can also use unpacking in the **range()** built-in function that expects a start and an end.

```python
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]
```

**Output:**
```text
[2, 3, 4, 5, 6]
range(2, 7)
```

#### Unpacking List or a Tuple

```python
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

**Output:**
```text
Finland Sweden Norway ['Denmark', 'Iceland']
1 [2, 3, 4, 5, 6] 7
```

#### Unpacking Dictionaries

```python
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Milaan', 'country':'England', 'city':'London', 'age':96}
print(unpacking_person_info(**dct)) # Milaan lives in England, London. He is 96 year old.
```

**Output:**
```text
Milaan lives in England, London. He is 96 year old.
```

### Packing

Sometimes we never know how many arguments need to be passed to a python function. We can use the packing method to allow our function to take unlimited number or arbitrary number of arguments.

#### Packing Lists

```python
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

**Output:**
```text
6
28
```

#### Packing Dictionaries

```python
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
        # Printing dictionary items
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Milaan",
      country="England", city="London", age=96))
```

**Output:**
```text
{key} = {kwargs[key]}
{key} = {kwargs[key]}
{key} = {kwargs[key]}
{key} = {kwargs[key]}
{'name': 'Milaan', 'country': 'England', 'city': 'London', 'age': 96}
```

## Spreading in Python

Like in JavaScript, spreading is possible in Python. Let us check it in an example below:

```python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

**Output:**
```text
[0, 1, 2, 3, 4, 5, 6, 7]
['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

## Enumerate

If we are interested in an index of a list, we use *enumerate* built-in function to get the index of each item in the list.

```python
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

**Output:**
```text
0 20
1 30
2 40
```

```python
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print('The country {i} has been found at index {index}')
```

**Output:**
```text
hi
The country {i} has been found at index {index}
hi
hi
hi
hi
```

## Zip

Sometimes we would like to combine lists when looping through them. See the example below:

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

**Output:**
```text
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

## 💻 Exercises ➞ <span class='label label-default'>Exceptions Handling</span>

### Exercises ➞ <span class='label label-default'>Level 1</span>

1. names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable **`nordic_countries`**, store Estonia and Russia in es, and ru respectively.

---

## 📘 Python Regex
*Source: `5. Python Files/5. Python Regex.ipynb`*

# Python RegEx

In this class, you will learn about regular expressions (RegEx), and use Python's re module to work with RegEx (with the help of examples).

A **Reg**ular **Ex**pression (RegEx) is a sequence of characters that defines a search pattern. For example,

```python
>>> ^a...s$
```

The above code defines a RegEx pattern. The pattern is: **any five letter string starting with `a` and ending with `s`**.

A pattern defined using RegEx can be used to match against a string.

| Expression | String | Matched? | 
|:----| :--- |:--- |
|               |  **`abs`** | No match | 
|               |  **`alias`** | Match |
| **`^a...s$`** |  **`abyss`** | Match |
|               |  **`Alias`** | No match |
|               |  **`An abacus`** | No match |

Python has a module named **`re`** to work with RegEx. Here's an example:

```python
import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
    print("Search successful.")
else:
    print("Search unsuccessful!")
```

**Output:**
```text
Search successful.
```

Here, we used **`re.match()`** function to search **`pattern`** within the **`test_string`**. The method returns a match object if the search is successful. If not, it returns **`None`**.

There are other several functions defined in the **`re`** module to work with RegEx. Before we explore that, let's learn about regular expressions themselves.

## Specify Pattern Using RegEx

To specify regular expressions, metacharacters are used. In the above example, **`^`** and **`$`** are metacharacters.

## MetaCharacters

Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:

###  **`[] . ^ $ * + ? {} () \ |`**

### 1. `[]` - Square brackets

Square brackets specifies a set of characters you wish to match.

| Expression | String | Matched? | 
|:----| :--- |:--- |
|             |  **`a`** | 1 match | 
|             |  **`ac`** | 2 matches |
| **`[abc]`** |  **`Hey Jude`** | No match |
|             |  **`abc de ca`** | 5 matches |

Here, **`[abc]`** will match if the string you are trying to match contains any of the **`a`**, **`b`** or **`c`**.

You can also specify a range of characters using **`-`** inside square brackets.

* **`[a-c]`** means, a or b or c
* **`[a-z]`** means, any letter from a to z
* **`[A-Z]`** means, any character from A to Z
* **`[0-3]`** means, 0 or 1 or 2 or 3
* **`[0-9]`** means any number from 0 to 9
* **`[A-Za-z0-9]`** any single character, that is a to z, A to Z or 0 to 9

You can complement (invert) the character set by using caret **`^`** symbol at the start of a square-bracket.

* **`[^abc]`** means any character except **`a`** or **`b`** or **`c`**.
* **`[^0-9]`** means any non-digit character.

### 2. `.` - Period

A period matches any single character (except newline **`'\n'`**).

| Expression | String | Matched? | 
|:----| :--- |:--- |
|          |  **`a`** | No match | 
|          |  **`ac`** | 1 match |
| **`..`** |  **`acd`** | 1 match |
|          |  **`acde`** | 2 matches (contains 4 characters) |

### 3. `^` - Caret

The caret symbol **`^`** is used to check if a string **starts with** a certain character.

  * **`r'^substring'`** eg **`r'^love'`**, a sentence that starts with a word love
  * **`r'[^abc]`** means not a, not b, not c.

| Expression | String | Matched? | 
|:----| :--- |:--- |
|          |  **`a`** | 1 match | 
| **`^a`** |  **`abc`** | 1 match |
|          |  **`bac`** | No match |
|----------|------------|------------------------------------------------------------|
| **`^a`** |  **`abc`** | 1 match |
|          |  **`acd`** | No match (starts with **`a`** but not followed by **`b`**) |

### 4. `$` - Dollar

The dollar symbol **`$`** is used to check if a string **ends with** a certain character.

| Expression | String | Matched? | 
|:----| :--- |:--- |
|          |  **`a`** | 1 match | 
| **`a$`** |  **`formula`** | 1 match |
|          |  **`cab`** | No result |

### 5. `*` - Star

The star symbol **`*`** matches **zero or more occurrences** of the pattern left to it.

| Expression | String | Matched? | 
|:----| :--- |:--- |
|            |  **`mn`** | 1 match | 
|            |  **`man`** | 1 match |
| **`ma*n`** |  **`maaan`** | 1 match |
|            |  **`main`** | No match (**`a`** is not followed by **`n`**) |
|            |  **`woman`** | 1 match |

### 6. `+` - Plus

The plus symbol **`+`** matches **zero or more occurrences** of the pattern left to it.

| Expression | String | Matched? | 
|:----| :--- |:--- |
|            |  **`mn`** | No match (no **`a`** character) | 
|            |  **`man`** | 1 match |
| **`ma+n`** |  **`maaan`** | 1 match |
|            |  **`main`** | No match (**`a`** is not followed by **`n`**) |
|            |  **`woman`** | 1 match |

### 7. `?` - Question Mark

The question mark symbol **`?`** matches **zero or more occurrences** of the pattern left to it.

| Expression | String | Matched? | 
|:----| :--- |:--- |
|            |  **`mn`** | 1 match | 
|            |  **`man`** | 1 match |
| **`ma?n`** |  **`maaan`** | No match (more than one **`a`** character) |
|            |  **`main`** | No match (**`a`** is not followed by **`n`**) |
|            |  **`woman`** | 1 match |

### 8. `{}` - Braces

We can specify the length of the substring we are looking for in a text, using a curly brackets **`{}`**.

Consider this code: **`{n,m}`**. This means at least **`n`**, and at most **`m`** repetitions of the pattern left to it.

* **`{3}`**: Exactly 3 characters
* **`{3,}`**: At least 3 characters
* **`{3,8}`**: 3 to 8 characters

| Expression | String | Matched? | 
|:----| :--- |:--- |
|              |  **`abc dat`** | No match | 
|              |  **`abc daat`** | 1 match (at **`daat`**) |
| **`a{2,3}`** |  **`aabc daaat`** | 2 matches (at **`aabc`** and **`daaat`**) |
|              |  **`aabc daaaat`** | 2 matches (at **`aabc`** and **`daaaat`**) |

Let's try one more example. This RegEx **`[0-9]{2, 4}`** matches at least 2 digits but not more than 4 digits

| Expression | String | Matched? | 
|:----| :--- |:--- |
|                  |  **`ab123csde`** | 1 match (match at **`ab123csde`**) | 
| **`[0-9]{2,4}`** |  **`12 and 345673`** | 3 matches (**`12`**, **`3456`**, **`73`**) |
|                  |  **`1 and 2`** | No match |

### 9. `|` - Alternation

Vertical bar **`|`** is used for alternation (**`or`** operator).

| Expression | String | Matched? | 
|:----| :--- |:--- |
|           |  **`cde`** | No match | 
| **`a\|b`** |  **`ade`** | 1 match (match at **`ade`**) |
|           |  **`acdbea`** | 3 matches (at **`acdbea`**) |

Here, **`a|b`** match any string that contains either **`a`** or **`b`**

### 10. `()` - Group

Parentheses **`()`** is used to group sub-patterns. For example, **`(a|b|c)xz`** match any string that matches either **`a`** or **`b`** or **`c`**. followed by **`xz`**.

| Expression | String | Matched? | 
|:----| :--- |:--- |
|                 |  **`ab xz`** | No match | 
| **`(a\|b\|c)xz`** |  **`abxz`** | 1 match (match at **`abxz`**) |
|                 |  **`axz cabxz`** | 2 matches (at **`axz cabxz`**) |

### 11. `\` - Backslash

Backlash **`\`** is used to escape various characters including all metacharacters. For example,

**`\$a`** match if a string contains **`$`** followed by **`a`**. Here, **`$`** is not interpreted by a RegEx engine in a special way.

If you are unsure if a character has special meaning or not, you can put **`\`** in front of it. This makes sure the character is not treated in a special way.

### Special Sequences

Special sequences make commonly used patterns easier to write. Here's a list of special sequences:

#### `\A` - Matches if the specified characters are at the start of a string.

| Expression | String | Matched? | 
|:----| :--- |:--- |
| **`\Athe`** |  **`the sun`** | Match | 
|             |  **`In the sun`** | No match |

#### `\b` - Matches if the specified characters are at the beginning or end of a word.

| Expression | String | Matched? | 
|:----| :--- |:--- |
|             |  **`football`** | Match | 
| **`\bfoo`** |  **`a football`** | Match |
|             |  **`afootball`** | No match |
|-------------|------------|-----------|
| **`foo\b`** |  **`the foo`** | Match |
|             |  **`the afoo test`** | Match |
|             |  **`the afootest`** | No match |

#### `\B` - Opposite of `\b`. Matches if the specified characters are not at the beginning or end of a word.

| Expression | String | Matched? | 
|:----| :--- |:--- |
|             |  **`football`** | No match | 
| **`\Bfoo`** |  **`a football`** | No match |
|             |  **`afootball`** | Match |
|-------------|------------|-----------|
| **`foo\B`** |  **`the foo`** | No match |
|             |  **`the afoo test`** | No match |
|             |  **`the afootest`** | Match |

#### `\d` - Matches any non-decimal digit. Equivalent to `[^0-9]`

- **`\d`** means: match where the string contains digits (numbers from 0-9)
- **`\D`** means: match where the string does not contain digits
    
| Expression | String | Matched? | 
|:----| :--- |:--- |
| **`\d`** |  **`1ab34"50`** | 3 matches (at **`1ab34"50`**) | 
|          |  **`1345`** | No match |

#### `\s` - Matches where a string contains any whitespace character. Equivalent to `[ \t\n\r\f\v]`.

| Expression | String | Matched? | 
|:----| :--- |:--- |
| **`\s`** |  **`Python RegEx`** | 1 match | 
|          |  **`PythonRegEx`** | No match |

#### `\S` - Matches where a string contains any non-whitespace character. Equivalent to `[^ \t\n\r\f\v]`.

| Expression | String | Matched? | 
|:----| :--- |:--- |
| **`\S`** |  **`a b`** | 2 matches (at  **`a b`**) | 
|          |  **` `** | No match |

#### `\w` - Matches any alphanumeric character (digits and alphabets). Equivalent to `[a-zA-Z0-9_]`. By the way, underscore `_` is also considered an alphanumeric character.

| Expression | String | Matched? | 
|:----| :--- |:--- |
| **`\w`** |  **`12&": ;c`** | 3 matches (at **`12&": ;c`**) | 
|          |  **`%"> !`** | No match |

#### `\W` - Matches any non-alphanumeric character. Equivalent to `[^a-zA-Z0-9_]`.

| Expression | String | Matched? | 
|:----| :--- |:--- |
| **`\W`** |  **`1a2%c`** | 1 match (at **`1a2%c`**) | 
|          |  **`Python`** | No match |

#### `\Z` - Matches if the specified characters are at the end of a string.

| Expression | String | Matched? | 
|:----| :--- |:--- |
|                |  **`I like Python`** | 1 match |
| **`Python\Z`** |  **`I like Python Programming`** | No match | 
|                |  **`Python is fun.`** | No match |

### Summary - MetaCharacters

<div>
<img src="regex.png" width="1000"/>
</div>

>**Tip**: To build and test regular expressions, you can use RegEx tester tools such as **[regex101](https://regex101.com/)**. This tool not only helps you in creating regular expressions, but it also helps you learn it.

Now you understand the basics of RegEx, let's discuss how to use RegEx in your Python code.

A **Reg**ular **Ex**pression or **RegEx** is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called **`re`**.

### Python RegEx Methods

To find a pattern we use different set of **`re`** character sets that allows to search for a match in a string.

* **`re.findall`**: Returns a list containing all matches
* **`re.split`**:	Takes a string, splits it at the match points, returns a list
* **`re.sub`**:  Replaces one or many matches within a string
* **`re.search`**: Returns a match object if there is one anywhere in the string, including multiline strings.
* **`re.match()`**: searches only in the beginning of the first line of the string and returns matched objects if found, else returns **`None`**.

To use it, we need to import the module.

```python
import re
```

The module defines several functions and constants to work with RegEx.

### 1. `re.findall()`

The **`re.findall()`** method returns a list of strings containing all matches.

```python
# Example 1: re.findall()

# Program to extract numbers from a string

import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

# Output: ['12', '89', '34']
```

**Output:**
```text
['12', '89', '34']
```

If the pattern is not found, **`re.findall()`** returns an empty list.

```python
# Example 2: re.findall()

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

**Output:**
```text
['language', 'language']
```

As you can see, the word **`language`** was found two times in the string. Let us practice some more.
Now we will look for both **`Python`** and **`python`** words in the string:

```python
# Example 3: re.findall()

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']
```

**Output:**
```text
['Python', 'python']
```

Since we are using **`re.I`** both lowercase and uppercase letters are included. If we do not have the **`re.I`** flag, then we will have to write our pattern differently. Let us check it out:

```python
# Example 4: re.findall()

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']
```

**Output:**
```text
['Python', 'python']
['Python', 'python']
```

### 2. `re.split()`

The **`re.split`** method splits the string where there is a match and returns a list of strings where the splits have occurred.

```python
# Example 1: re.split()

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol
```

**Output:**
```text
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

```python
# Example 2: re.split()

import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']
```

**Output:**
```text
['Twelve:', ' Eighty nine:', '.']
```

If the pattern is not found, **`re.split`** returns a list containing the original string.

You can pass **`maxsplit`** argument to the **`re.split`** method. It's the maximum number of splits that will occur.

```python
# Example 3: re.split()

import re

string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# maxsplit = 1
# split only at the first occurrence
result = re.split(pattern, string, 1) 
print(result)

# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']
```

**Output:**
```text
['Twelve:', ' Eighty nine:89 Nine:9.']
```

By the way, the default value of **`maxsplit`** is 0; meaning all possible splits.

### 3. `re.sub()`

**Syntax:**

```python
re.sub(pattern, replace, string)
```

The method returns a string where matched occurrences are replaced with the content of **`replace`** variable.

```python
# Example 1: re.sub()

# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)

# Output: abc12de23f456
```

**Output:**
```text
abc12de23f456
```

If the pattern is not found, **`re.sub()`** returns the original string.

You can pass **`count`** as a fourth parameter to the **`re.sub()`** method. If omited, it results to 0. This will replace all occurrences.

```python
# Example 2: re.sub()

import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'
replace = ''

new_string = re.sub(r'\s+', replace, string, 1) 
print(new_string)

# Output:
# abc12de 23
# f45 6
```

**Output:**
```text
abc12de 23 
 f45 6
```

```python
# Example 3: re.sub()

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
```

**Output:**
```text
JavaScript is the most beautiful language that a human being has ever created.
I recommend JavaScript for a first programming language
JavaScript is the most beautiful language that a human being has ever created.
I recommend JavaScript for a first programming language
```

Let us add one more example. The following string is really hard to read unless we remove the **`%`** symbol. Replacing the **`%`** with an empty string will clean the text.

```python
# Example 4: re.sub()

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
```

**Output:**
```text
I am teacher and  I love teaching. 
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs. 
Does this motivate you to be a teacher?
```

### 4. `re.subn()`

The **`re.subn()`** is similar to **`re.sub()`** expect it returns a tuple of 2 items containing the new string and the number of substitutions made.

```python
# Example 1: re.subn()

# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.subn(pattern, replace, string) 
print(new_string)

# Output: ('abc12de23f456', 4)
```

**Output:**
```text
('abc12de23f456', 4)
```

### 5. `re.search()`

The **`re.search()`** method takes two arguments: a pattern and a string. The method looks for the first location where the RegEx pattern produces a match with the string.

If the search is successful, **`re.search()`** returns a match object; if not, it returns **`None`**.

```python
match = re.search(pattern, str)
```

```python
# Example 1: re.search()

import re

string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
    print("pattern found inside the string")
else:
    print("pattern not found")  

# Output: pattern found inside the string
```

**Output:**
```text
pattern found inside the string
```

Here, **`match`** contains a match object.

```python
# Example 2: re.search()

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
```

## Match object

You can get methods and attributes of a match object using **dir()** function.

Some of the commonly used methods and attributes of match objects are:

```python
import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach
```

As you can see from the example above, the pattern we are looking for (or the substring we are looking for) is **`I love to teach`**. The match function returns an object **only** if the text starts with the pattern.

```python
import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None
```

**Output:**
```text
None
```

The string does not string with **`I like to teach`**, therefore there was no match and the match method returned **`None`**.

### 1. `match.group()`

The **`group()`** method returns the part of the string where there is a match.

```python
# Example 6: Match object

import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
    print(match.group())
else:
    print("pattern not found")

# Output: 801 35
```

**Output:**
```text
801 35
```

Here, match variable contains a match object.

Our pattern **`(\d{3}) (\d{2})`** has two subgroups **`(\d{3})`** and **`(\d{2})`**. You can get the part of the string of these parenthesized subgroups. Here's how:

```python
match.group(1)
```

**Output:**
```text
'801'
```

```python
match.group(2)
```

**Output:**
```text
'35'
```

```python
match.group(1, 2)
```

**Output:**
```text
('801', '35')
```

```python
match.groups()
```

**Output:**
```text
('801', '35')
```

### 2. `match.start(), match.end() and match.span()`

The **`start()`** function returns the index of the start of the matched substring. Similarly, **`end()`** returns the end index of the matched substring.

```python
match.start()
```

**Output:**
```text
2
```

```python
match.end()
```

**Output:**
```text
8
```

The **`span()`** function returns a tuple containing start and end index of the matched part.

```python
match.span()
```

**Output:**
```text
(2, 8)
```

### 3. `match.re and match.string`

The **`re`** attribute of a matched object returns a regular expression object. Similarly, **`string`** attribute returns the passed string.

```python
match.re
```

**Output:**
```text
re.compile(r'(\d{3}) (\d{2})', re.UNICODE)
```

```python
match.string
```

**Output:**
```text
'39801 356, 2102 1111'
```

We have covered all commonly used methods defined in the **`re`** module.

If you want to learn more, visit **[Python 3 re module](https://docs.python.org/3/library/re.html)**.

## Using `r` prefix before RegEx

When **`r`** or **`R`** prefix is used before a regular expression, it means raw string. For example, **`'\n'`** is a new line whereas **`r'\n'`** means two characters: a backslash **`\`** followed by **`n`**.

Backlash **`\`** is used to escape various characters including all metacharacters. However, using **`r`** prefix makes **`\`** treat as a normal character.

```python
# Example 7: Raw string using r prefix

import re

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) 
print(result)

# Output: ['\n', '\r']
```

**Output:**
```text
['\n', '\r']
```

## Example of RegEx with Metacharacters

Let us use examples to clarify the meta characters with RegEx methods:

### Square Brackets `[]`

Let us use square bracket to include lower and upper case

```python
# Example 1:

regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```

**Output:**
```text
['Apple', 'apple']
```

If we want to look for the both apple and banana, we write the pattern as follows:

```python
# Example 2:

regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```

**Output:**
```text
['Apple', 'banana', 'apple', 'banana']
```

Using the square brackets **`[]`** and or operator **`|`** , we manage to extract Apple, apple, Banana

### Escape character `\`

```python
# Example 1:

regex_pattern = r'\d'  # d is a special character which means digits
txt = "Hawking born on 8 January 1942 and died on 14 March 2018 Einstein's birth anniversary (Pi-Day) and both died at 76"
matches = re.findall(regex_pattern, txt)
print(matches)  # ['8', '1', '9', '4', '2', '1', '4', '2', '0', '1', '8', '7', '6'] - this is not what we want
```

**Output:**
```text
['8', '1', '9', '4', '2', '1', '4', '2', '0', '1', '8', '7', '6']
```

### One or more times `+`

```python
# Example 1:

regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = "Hawking born on 8 January 1942 and died on 14 March 2018 Einstein's birth anniversary (Pi-Day) and both died at 76"
matches = re.findall(regex_pattern, txt)
print(matches)  # ['8', '1942', '14', '2018', '76'] - this is better!
```

**Output:**
```text
['8', '1942', '14', '2018', '76']
```

### Period `.`

```python
# Example 1:

regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and Banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']
```

**Output:**
```text
['an', 'an', 'an', 'a ', 'ar']
```

```python
# Example 2: [] with +

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and Banana are fruits']
```

**Output:**
```text
['and Banana are fruits']
```

### Zero or more times `*`

```python
# Example 1:

regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and Banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and Banana are fruits']
```

**Output:**
```text
['and Banana are fruits']
```

### Zero or one time `?`

Zero or one time. The pattern may not occur or it may occur once.

```python
# Example 1:

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

**Output:**
```text
['e-mail', 'email', 'Email', 'E-mail']
```

### Quantifier `{}`

We can specify the length of the substring we are looking for in a text, using a curly brackets **`{}`**. Let us imagine, we are interested in a substring with a length of 4 characters:

```python
# Example 1:

txt = "Hawking born on 8 January 1942 and died on 14 March 2018 Einstein's birth anniversary (Pi-Day) and both died at 76"
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['1942', '2018']
```

**Output:**
```text
['1942', '2018']
```

```python
# Example 2:

txt = "Hawking born on 8 January 1942 and died on 14 March 2018 Einstein's birth anniversary (Pi-Day) and both died at 76"
regex_pattern = r'\d{1,4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['8', '1942', '76', '14', '2018', '76']
```

**Output:**
```text
['8', '1942', '14', '2018', '76']
```

### Cart `^`

```python
# Example 1: Starts with

txt = "Hawking born on 8 January 1942 and died on 14 March 2018 Einstein's birth anniversary (Pi-Day) and both died at 76"
regex_pattern = r'^Hawking'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Hawking']
```

**Output:**
```text
['Hawking']
```

```python
# Example 2: Negation

txt = "Hawking born on 8 January 1942 and died on 14 March 2018 Einstein's birth anniversary (Pi-Day) and both died at 76"
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['8', '1942', '14', '2018', "'", '(', '-', ')', '76']
```

**Output:**
```text
['8', '1942', '14', '2018', "'", '(', '-', ')', '76']
```

## 💻 Exercises ➞ <span class='label label-default'>RegEx</span>

### Exercises ➞ <span class='label label-default'>Level 1</span>

 1. What is the most frequent word in the following paragraph?
    - ```py
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
    ```

   - ```sy
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
    ```

2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

    - ```py
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) # 12
    ```

### Exercises ➞ <span class='label label-default'>Level 2</span>

1. Write a pattern which identifies if a string is a valid python variable

    - ```py
    is_valid_variable('first_name')  # True
    is_valid_variable('first-name')  # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname')   # True
    ```


### Exercises ➞ <span class='label label-default'>Level 3</span>

1. Clean the following text. After cleaning, count three most frequent words in the string.

    - ```py
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

    print(clean_text(sentence));
    I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
    ```

---
