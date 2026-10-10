# Python Functions, Scopes, Modules & Packages

Complete guide to user-defined functions, arguments (*args, **kwargs, defaults), LEGB scopes (global, local, nonlocal), recursion, lambda/anonymous functions, built-in modules (math, random), and packages.

---

# 04_Python_Functions

## Introduction 👋

Functions are an essential part of the Python programming language. A **function is a block of code defined with a name**. We use functions whenever we need to perform the same task multiple times without writing the same code again. It can take arguments and returns the value.

Python has a DRY principle like other programming languages. DRY stands for Don’t Repeat Yourself. Consider a scenario where we need to do some action/task many times. We can define that action only once using a function and call that function whenever required to do the same activity.

Function improves efficiency and reduces errors because of the reusability of a code. Once we create a function, we can call it anywhere and anytime. The benefit of using a function is reusability and modularity.

---

## Table of contents 📋

| **No.** | **Name** | 
| ------- | -------- | 
| 01 | **[Python_Functions](https://github.com/milaan9/04_Python_Functions/blob/main/001_Python_Functions.ipynb)** |
|    | 1.1 **[Python_Docstrings](https://github.com/milaan9/04_Python_Functions/blob/main/Python_Docstrings.ipynb)** |
|    | 1.2 **[Python_Built-In_Functions](https://github.com/milaan9/04_Python_Functions/tree/main/002_Python_Functions_Built_in)** |
|    | 1.3 **[Python_User-Defined_Functions](https://github.com/milaan9/04_Python_Functions/blob/main/Python_User_defined_Functions.ipynb)** |
| 02 | **[Python_Function_Global_Local_Nonlocal](https://github.com/milaan9/04_Python_Functions/blob/main/002_Python_Function_Global_Local_Nonlocal.ipynb)** |
| 03 | **[Python_Function_global_Keywords](https://github.com/milaan9/04_Python_Functions/blob/main/003_Python_Function_global_Keywords.ipynb)** |
| 04 | **[Python_Function_Arguments](https://github.com/milaan9/04_Python_Functions/blob/main/004_Python_Function_Arguments.ipynb)** |
| 05 | **[Python_Function_Recursion](https://github.com/milaan9/04_Python_Functions/blob/main/005_Python_Function_Recursion.ipynb)** |
| 06 | **[Python_Function_Anonymous](https://github.com/milaan9/04_Python_Functions/blob/main/006_Python_Function_Anonymous.ipynb)** |
| 07 | **[Python_Function_Module](https://github.com/milaan9/04_Python_Functions/blob/main/007_Python_Function_Module.ipynb)** |
| 08 | **[Python_Function_random_Module](https://github.com/milaan9/04_Python_Functions/blob/main/008_Python_Function_random_Module.ipynb)** |
| 09 | **[Python_Function_math_Module.ipynb](https://github.com/milaan9/04_Python_Functions/blob/main/009_Python_Function_math_Module.ipynb.ipynb)** |
| 10 | **[Python_Function_Package](https://github.com/milaan9/04_Python_Functions/blob/main/010_Python_Function_Package.ipynb)** |


These are online **read-only** versions. However you can **`Run ▶`**  all the codes **online** by clicking here ➞ 

---

## Frequently asked questions ❔

### How can I thank you for writing and sharing this tutorial? 🌷

You can <img src="https://img.shields.io/static/v1?label=%E2%AD%90 Star &message=if%20useful&style=style=flat&color=blue" alt="Star Badge"/> and <img src="https://img.shields.io/static/v1?label=%E2%B5%96 Fork &message=if%20useful&style=style=flat&color=blue" alt="Fork Badge"/> Starring and Forking is free for you, but it tells me and other people that it was helpful and you like this tutorial.

Go [**`here`**](https://github.com/milaan9/04_Python_Functions) if you aren't here already and click ➞ **`✰ Star`** and **`ⵖ Fork`** button in the top right corner. You'll be asked to create a GitHub account if you don't already have one.

---

### How can I read this tutorial without an Internet connection? <img alt="GIF" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/hmm.gif" width="20" />

1. Go [**`here`**](https://github.com/milaan9/04_Python_Functions) and click the big green ➞ **`Code`** button in the top right of the page, then click ➞ [**`Download ZIP`**](https://github.com/milaan9/04_Python_Functions/archive/refs/heads/main.zip).

    ![Download ZIP](img/dnld_rep.png)

2. Extract the ZIP and open it. Unfortunately I don't have any more specific instructions because how exactly this is done depends on which operating system you run.
    
3. Launch ipython notebook from the folder which contains the notebooks. Open each one of them
  
    **`Kernel > Restart & Clear Output`**
    
This will clear all the outputs and now you can understand each statement and learn interactively.

If you have git and you know how to use it, you can also clone the repository instead of downloading a zip and extracting it. An advantage with doing it this way is that you don't need to download the whole tutorial again to get the latest version of it, all you need to do is to pull with git and run ipython notebook again.

---

## Authors ✍️

I'm Dr. Milaan Parmar and I have written this tutorial. If you think you can add/correct/edit and enhance this tutorial you are most welcome🙏

See [github's contributors page](https://github.com/milaan9/04_Python_Functions/graphs/contributors) for details.

If you have trouble with this tutorial please tell me about it by [Create an issue on GitHub](https://github.com/milaan9/04_Python_Functions/issues/new). and I'll make this tutorial better. This is probably the best choice if you had trouble following the tutorial, and something in it should be explained better. You will be asked to create a GitHub account if you don't already have one.

If you like this tutorial, please [give it a ⭐ star](https://github.com/milaan9/04_Python_Functions).

---

## Licence 📜

You may use this tutorial freely at your own risk. See [LICENSE](./LICENSE).

---

## 📘 Python Abs()
*Source: `4. Python Functions/1. Python abs().ipynb`*

# Python `abs()`

The **`abs()`** method returns the absolute value of the given number. If the number is a complex number, **`abs()`** returns its magnitude.

**Syntax**:

```python
abs(num)
```

## `abs()` Parameters

**`abs()`** method takes a single argument:

* **num** - a number whose absolute value is to be returned. The number can be:
    * integer
    * floating number
    * complex number

## Return value from `abs()`

**`abs()`** method returns the absolute value of the given number.

* For integers - integer absolute value is returned
* For floating numbers - floating absolute value is returned
* For complex numbers - magnitude of the number is returned

```python
# Example 1: Get absolute value of a number

# random integer
integer = -20
print('Absolute value of -20 is:', abs(integer))

#random floating number
floating = -30.33
print('Absolute value of -30.33 is:', abs(floating))
```

**Output:**
```text
Absolute value of -20 is: 20
Absolute value of -30.33 is: 30.33
```

```python
# Example 2: Get magnitude of a complex number

# random complex number
complex = (3 - 4j)
print('Magnitude of 3 - 4j is:', abs(complex))
```

**Output:**
```text
Magnitude of 3 - 4j is: 5.0
```

---

## 📘 Python Functions
*Source: `4. Python Functions/1. Python Functions.ipynb`*

# Python Functions

In this class, you'll learn about functions, what a function is, the syntax, components, and types of functions. Also, you'll learn to create a function in Python.

# What is a function in Python?

In Python, a **function is a block of organized, reusable (DRY- Don’t Repeat Yourself) code with a name** that is used to perform a single, specific task. It can take arguments and returns the value.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

Furthermore, it improves efficiency and reduces errors because of the reusability of a code.

## Types of Functions

Python support two types of functions

1. **Built-in** function
2. **User-defined** function

1.**Built-in function**

The functions which are come along with Python itself are called a built-in function or predefined function. Some of them are:
**`range()`**, **`print()`**, **`input()`**, **`type()`**, **`id()`**, **`eval()`** etc.

**Example:** Python **`range()`** function generates the immutable sequence of numbers starting from the given start integer to the stop integer.

```python
>>> for i in range(1, 10):
>>>     print(i, end=' ')

1 2 3 4 5 6 7 8 9
```

2. **User-defined function**

Functions which are created by programmer explicitly according to the requirement are called a user-defined function.

**Syntax:**

```python
def function_name(parameter1, parameter2):
    """docstring"""
    # function body    
    # write some action
return value
```

<div>

</div>

## Defining a Function

1. **`def`** is a keyword that marks the start of the function header.

2. **`function_name`** to uniquely identify the function. Function naming follows the same **rules of writing identifiers in Python**.

2. **`parameter`** is the value passed to the function. They are optional.

3. **`:`** (colon) to mark the end of the function header.

4. **`function body`** is a block of code that performs some task and all the statements in **`function body`** must have the same **indentation** level (usually 4 spaces). 

5. **"""docstring"""** documentation string is used to describe what the function does.

6. **`return`** is a keyword to return a value from the function.. A return statement with no arguments is the same as return **`None`**.

>**Note:** While defining a function, we use two keywords, **`def`** (mandatory) and **`return`** (optional).

**Example:**

```python
>>> def add(num1,num2):           # Function name: 'add', Parameters: 'num1', 'num2'
>>>     print("Number 1: ", num1) #  Function body
>>>     print("Number 2: ", num2) #  Function body
>>>     addition = num1 + num2    #  Function body
>>>     return addition           # return value


>>> res = add(2, 4)   # Function call
>>> print("Result: ", res)
```

## Defining a function without any parameters

Function can be declared without parameters.

```python
# Example 1: 
    
def greet():
    print("Welcome to Python for Data Science")

# call function using its name
greet()
```

**Output:**
```text
Welcome to Python for Data Science
```

```python
# Example 2: 

def add_two_numbers ():
    num_one = 3
    num_two = 6
    total = num_one + num_two
    print(total)
add_two_numbers() # calling a function
```

**Output:**
```text
9
```

```python
# Example 3: 

def generate_full_name ():
    first_name = 'Milaan'
    last_name = 'Parmar'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function
```

**Output:**
```text
Milaan Parmar
```

## Defining a function without parameters and `return` value

Function can also return values, if a function does not have a **`return`** statement, the value of the function is None. Let us rewrite the above functions using **`return`**. From now on, we get a value from a function when we call the function and print it.

```python
# Example 1: 

def add_two_numbers ():
    num_one = 3
    num_two = 6
    total = num_one + num_two
    return total
print(add_two_numbers())
```

**Output:**
```text
9
```

```python
# Example 2: 

def generate_full_name ():
    first_name = 'Milaan'
    last_name = 'Parmar'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
```

**Output:**
```text
Milaan Parmar
```

## Defining a function with parameters

In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as a parameter.

### Single Parameter: 

If our function takes a parameter we should call our function with an argument

```python
# Example 1: Gereeting

def greet(name):
    """
    This function greets to the person passed in as a parameter
    """
    print("Hello, " + name + ". Good morning!")   # No output!
```

```python
# Example 2: 

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100)) # 5050
```

**Output:**
```text
55
None
5050
None
```

### Two Parameter: 

A function may or may not have a parameter or parameters. A function may also have two or more parameters. If our function takes parameters we should call it with arguments.

```python
# Example 1: 

def course(name, course_name):
    print("Hello", name, "Welcome to Python for Data Science")
    print("Your course name is", course_name)

course('Arthur', 'Python')   # call function
```

**Output:**
```text
Hello Arthur Welcome to Python for Data Science
Your course name is Python
```

## Defining a function with parameters and `return` value

```python
# Example 1: 

def greetings (name):  # single parameter
    message = name + ', welcome to Python for Data Science'
    return message

print(greetings('Milaan'))
```

**Output:**
```text
Milaan, welcome to Python for Data Science
```

```python
# Example 2: 

def add_ten(num):  # single parameter
    ten = 10
    return num + ten
print(add_ten(90))
```

**Output:**
```text
100
```

```python
# Example 3: 

def square_number(x):  # single parameter
    return x * x
print(square_number(3))
```

**Output:**
```text
9
```

```python
# Example 4: 

def area_of_circle (r):  # single parameter
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))
```

**Output:**
```text
314.0
```

```python
# Example 5: 

def calculator(a, b):  # two parameter
    add = a + b   
    return add    # return the addition

result = calculator(30, 6)   # call function & take return value in variable
print("Addition :", result)   # Output Addition : 36
```

**Output:**
```text
Addition : 36
```

```python
# Example 6: 

def generate_full_name (first_name, last_name):  # two parameter
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Milaan','Parmar'))
```

**Output:**
```text
Full Name:  Milaan Parmar
```

```python
# Example 7: 

def sum_two_numbers (num_one, num_two):  # two parameter
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))
```

**Output:**
```text
Sum of two numbers:  10
```

```python
# Example 8: 

def calculate_age (current_year, birth_year):  # two parameter
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819))
```

**Output:**
```text
Age:  202
```

```python
# Example 9: 

def weight_of_object (mass, gravity):  # two parameter
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

**Output:**
```text
Weight of an object in Newtons:  981.0 N
```

## Function `return` Statement

In Python, to return value from the function, a **`return`** statement is used. It returns the value of the expression following the returns keyword.

**Syntax:**

```python
def fun():
    statement-1
    statement-2
    statement-3
    .          
    .          
    return [expression]
```

The **`return`** value is nothing but a outcome of function.

* The **`return`** statement ends the function execution.
* For a function, it is not mandatory to return a value.
* If a **`return`** statement is used without any expression, then the **`None`** is returned.
* The **`return`** statement should be inside of the function block.

### Return Single Value

```python
print(greet("Cory"))
```

**Output:**
```text
Hello, Cory. Good morning!
None
```

Here, **`None`** is the returned value since **`greet()`** directly prints the name and no **`return`** statement is used.

## Passing Arguments with Key and Value

If we pass the arguments with key and value, the order of the arguments does not matter.

```python
# Example 1: 

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Milaan', lastname = 'Parmar'))
```

**Output:**
```text
Milaan Parmar
None
```

```python
# Example 2:

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
```

**Output:**
```text
5
None
```

If we do not **`return`** a value with a function, then our function is returning **`None`** by default. To return a value with a function we use the keyword **`return`** followed by the variable we are returning. We can return any kind of data types from a function.

```python
# Example 1:  with return statement

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print(print_fullname(firstname = 'Milaan', lastname = 'Parmar'))
```

**Output:**
```text
Milaan Parmar
```

```python
# Example 2:  with return statement

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
```

**Output:**
```text
5
```

```python
# Example 3:

def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(2))
print(absolute_value(-4))
```

**Output:**
```text
2
4
```

```python
# Example 4:

def sum(a,b):  # Function 1
    print("Adding the two values")
    print("Printing within Function")
    print(a+b)
    return a+b

def msg():  # Function 2
    print("Hello")
    return

total=sum(10,20)
print('total : ',total)
msg()
print("Rest of code")
```

**Output:**
```text
Adding the two values
Printing within Function
30
total :  30
Hello
Rest of code
```

```python
# Example 5:

def is_even(list1):
    even_num = []
    for n in list1:
        if n % 2 == 0:
            even_num.append(n)
    # return a list
    return even_num

# Pass list to the function
even_num = is_even([2, 3, 46, 63, 72, 83, 90, 19])
print("Even numbers are:", even_num)
```

**Output:**
```text
Even numbers are: [2, 46, 72, 90]
```

### Return Multiple Values

You can also return multiple values from a function. Use the return statement by separating each expression by a comma.

```python
# Example 1:

def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    multiply = num1 * num2
    division = num1 / num2
    # return four values
    return add, sub, multiply, division

a, b, c, d = arithmetic(10, 2)  # read four return values in four variables

print("Addition: ", a)
print("Subtraction: ", b)
print("Multiplication: ", c)
print("Division: ", d)
```

**Output:**
```text
Addition:  12
Subtraction:  8
Multiplication:  20
Division:  5.0
```

### Return Boolean Values

```python
# Example 1:

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

**Output:**
```text
even
True
False
```

### Return a List

```python
# Example 1:

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

**Output:**
```text
[0, 2, 4, 6, 8, 10]
```

## How to call a function in python?

Once we have defined a function, we can call it from another function, program or even the Python prompt. To call a function we simply type the function name with appropriate parameters.

<div>

</div>

```python
greet('Alan')
```

**Output:**
```text
Hello, Alan. Good morning!
```

>**Note:** Try running the above code in the Python program with the function definition to see the output.

```python
# Example 1: 

def wish(name):
    """
    This function wishes to the person passed in as a parameter
    """
    print("Happy birthday, " + name + ". Hope you have a wonderful day!")

wish('Bill')
```

**Output:**
```text
Happy birthday, Bill. Hope you have a wonderful day!
```

```python
# Example 2: 

def greetings (name = 'Clark'):
    message = name + ', welcome to Python for Data Science'
    return message
print(greetings())
print(greetings('Milaan'))
```

**Output:**
```text
Clark, welcome to Python for Data Science
Milaan, welcome to Python for Data Science
```

```python
# Example 3: 

def generate_full_name (first_name = 'Milaan', last_name = 'Parmar'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print(generate_full_name('Ethan','Hunt'))
```

**Output:**
```text
Milaan Parmar
Ethan Hunt
```

```python
# Example 4: 

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))
```

**Output:**
```text
Age:  200
```

```python
# Example 5: 

def swap(x, y):
    """
    This function swaps the value of two variables
    """
    temp = x;  # value of x will go inside temp
    x = y;     # value of y will go inside x
    y = temp;  # value of temp will go inside y
    print("value of x is:", x)
    print("value of y is:", y)
    return     # "return" is optional

x = 6
y = 9
swap(x, y)     #call function
```

**Output:**
```text
value of x is: 9
value of y is: 6
```

```python
# Example 6: 

def even_odd(n):    
    if n % 2 == 0:   # check number is even or odd
        print(n, 'is a Even number')
    else:
        print(n, 'is a Odd Number')

even_odd(9)   # calling function by its name
```

**Output:**
```text
9 is a Odd Number
```

```python
# Example 7: 

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
```

**Output:**
```text
Weight of an object in Newtons:  981.0 N
Weight of an object in Newtons:  162.0 N
```

## Docstrings

The first string after the function header is called the **docstring** and is short for documentation string. It is a descriptive text (like a comment) written by a programmer to let others know what block of code does.

Although **optional**, documentation is a good programming practice. Unless you can remember what you had for dinner last week, always document your code.

It is being declared using triple single quotes **`''' '''`** or triple-double quote **`""" """`** so that docstring can extend up to multiple lines.

We can access docstring using doc attribute **`__doc__`** for any object like list, tuple, dict, and user-defined function, etc.

In the above example, we have a docstring immediately below the function header.

```python
print(greet.__doc__)
```

**Output:**
```text
This function greets to the person passed in as a parameter
```

To learn more about docstrings in Python, visit **Python Docstrings**.

## Function `pass` Statement

In Python, the **`pass`** is the keyword, which won’t do anything. Sometimes there is a situation where we need to define a syntactically empty block. We can define that block using the **`pass`** keyword.

When the interpreter finds a **`pass`** statement in the program, it returns no operation.

```python
# Example 1:

def addition(num1, num2):
    # Implementation of addition function in comming release
    # Pass statement 
    pass

addition(10, 2)
```

## 💻 Exercises ➞ <span class='label label-default'>Functions</span>

### Exercises ➞ <span class='label label-default'>Level 1</span>

1. Area of a circle is calculated as follows: **area = π x r x r** and **perimeter = 2 x π x r**. Write a function that calculates **`area_of_circle`** and **`perimeter_of_circle`**.
2. Write a function called **`add_all_nums`** which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
3. Temperature in **°C** can be converted to **°F** using this formula: **°F = (°C x 9/5) + 32**. Write a function which converts **°C to °F**, **`convert_celsius_2_fahrenheit`**.
4. Write a function called **`check_season`**, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
5. Write a function called **`calculate_slope`** which return the slope of a linear equation
6. Quadratic equation is calculated as follows: **ax² + bx + c = 0**. Write a function which calculates solution set of a quadratic equation, **`solve_quadratic_eqn`**.
7. Declare a function named **`print_list`**. It takes a list as a parameter and it prints out each element of the list.
8. Declare a function named **`reverse_list`**. It takes an array as a parameter and it returns the reverse of the array (use loops).

    - ```py
print(reverse_list([1, 2, 3, 4, 5]))
#[5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
#["C", "B", "A"]
    ```

9. Declare a function named **`capitalize_list_items`**. It takes a list as a parameter and it returns a capitalized list of items
10. Declare a function named **`add_item`**. It takes a list and an item parameters. It returns a list with the item added at the end.

    - ```py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Fungi'))  #['Potato', 'Tomato', 'Mango', 'Milk', 'Fungi']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]
    ```

11. Declare a function named **`remove_item`**. It takes a list and an item parameters. It returns a list with the item removed from it.

    - ```py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
    ```

12. Declare a function named **`sum_of_numbers`**. It takes a number parameter and it adds all the numbers in that range.

    - ```py
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
     ```

13. Declare a function named **`sum_of_odds`**. It takes a number parameter and it adds all the odd numbers in that range.
14. Declare a function named **`sum_of_even`**. It takes a number parameter and it adds all the even numbers in that - range.

### Exercises ➞ <span class='label label-default'>Level 2</span>

1.  Declare a function named **`evens_and_odds`**. It takes a positive integer as parameter and it counts number of evens and odds in the number.

    - ```py
    print(evens_and_odds(100))
    #The number of odds are 50.
    #The number of evens are 51.
    ```

2. Call your function **`factorial`**, it takes a whole number as a parameter and it return a factorial of the number
3. Call your function **`is_empty`**, it takes a parameter and it checks if it is empty or not
4. Write different functions which take lists. They should **`calculate_mean`**, **`calculate_median`**, **`calculate_mode`**, **`calculate_range`**, **`calculate_variance`**, **`calculate_std`** (standard deviation).

### Exercises ➞ <span class='label label-default'>Level 3</span>

1. Write a function called **`is_prime`**, which checks if a number is prime.
2. Write a functions which checks if all items are unique in the list.
3. Write a function which checks if all the items of the list are of the same data type.
4. Write a function which check if provided variable is a valid python variable
5. Go to the data folder and access the **countries_data.py** file.

- Create a function called the **`most_spoken_languages`** in the world. It should return 10 or 20 most spoken languages in the world in descending order
- Create a function called the **`most_populated_countries`**. It should return 10 or 20 most populated countries in descending order.

---

## 📘 Python Any()
*Source: `4. Python Functions/2. Python any().ipynb`*

# Python `any()`

The **`any()`** function returns **`True`** if any element of an iterable is True. If not, **`any()`** returns **`False`**.

**Syntax**:

```python
any(iterable)
```

## Parameters for the `any()` function

The **`any()`** function takes an iterable (list, string, dictionary etc.) in Python.

## Value Returned by the `any()` function

The **`any()`** function returns a boolean value:

* **`True`** if at least one element of an iterable is true
* **`False`** if all elements are false or if an iterable is empty

| Condition | Return Value |
|:----| :--- |
| **All values are true** | **True** |
| **All values are false** | **False** |
| **One value is true (others are false)** | **True** |
| **One value is false (others are true)** | **True** |
| **Empty Iterable** | **False** |

```python
# Example 1: Using any() on Python Lists

# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(any(l))

# False since both are False
l = [0, False]
print(any(l))

# True since 5 is true
l = [0, False, 5]
print(any(l))

# False since iterable is empty
l = []
print(any(l))
```

**Output:**
```text
True
False
True
False
```

The **`any()`** method works in a similar way for **tuples** and **sets** like lists.

```python
# Example 2: Using any() on Python Strings

# Atleast one (in fact all) elements are True
s = "This is good"
print(any(s))

# 0 is False because it is a non-iterable number
# '0' is True because now it is not a number, it is a string character
s = '000'
print(any(s))

# False since empty iterable
s = ''
print(any(s))
```

**Output:**
```text
True
True
False
```

```python
# Example 3: Using any() with Python Dictionaries

# In the case of dictionaries, if all keys (not values) are false or the dictionary is empty, 
# `any()` returns `False`. If at least one key is true, `any()` returns `True`.

# 0 is False
d = {0: 'False'}
print(any(d))

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))

# iterable is empty
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))
```

**Output:**
```text
False
True
False
False
True
```

---

## 📘 Python Function Global Local Nonlocal
*Source: `4. Python Functions/2. Python Function Global Local Nonlocal.ipynb`*

# Python Global, Local and Nonlocal variables

In this class, you’ll learn about Python Global variables, Local variables, Nonlocal variables and where to use them.

When we define a function with variables, then those variables scope is limited to that function. In Python, the scope of a variable is the portion of a program where the variable is declared. Parameters and variables defined inside a function are not visible from outside the function. Hence, it is called the variable’s local scope.

>**Note:** The inner function does have access to the outer function’s local scope.

When we are executing a function, the life of the variables is up to running time. Once we return from the function, those variables get destroyed. So function does no need to remember the value of a variable from its previous call.

## Global Variables

In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.

For example:

```python
# Example 1: Create a Global Variable

global_var = 999

def fun1():
    print("Value in 1st function:", global_var)

def fun2():
    print("Value in 2nd function:", global_var)

fun1()
fun2()
```

**Output:**
```text
Value in 1st function: 999
Value in 2nd function: 999
```

```python
# Example 2: 

x = "global"

def fun():
    print("x inside:", x)

fun()
print("x outside:", x)
```

**Output:**
```text
x inside: global
x outside: global
```

In the above code, we created **`x`** as a global variable and defined a **`fun()`** to print the global variable **`x`**. Finally, we call the **`fun()`** which will print the value of **`x`**.

What if you want to change the value of **`x`** inside a function?

```python
# Example 3: 

x = "global"

def fun():
    x = x * 2
    print(x)

fun()
```

**Explanation:**

The output shows an error because Python treats **`x`** as a local variable and **`x`** is also not defined inside **`fun()`**.

To make this work, we use the **`global`** keyword. Visit **Python Global Keyword** to learn more.

```python
# Example 4: 

global_lang = 'DataScience'

def var_scope_test():
    local_lang = 'Python'
    print(local_lang)

var_scope_test()  # Output 'Python'

# outside of function
print(global_lang)   # Output 'DataScience'

print(local_lang)   # NameError: name 'local_lang' is not defined
```

**Output:**
```text
Python
DataScience
```

```python
# Example 5: 

a=90   # 'a' is a variable defined outside of function, i.e., Global variable

def print_data():
    a=6  # 'a' is a variable defined inside of function, i.e., local variable
    b=30
    print("(a,b):(",a,",",b,")")

print_data() #(a,b):( 5 , 10 )
print("Global a :",a)  #Global x : 50
print("Local b : ",b)  #b is local veriable - throw NameError
```

**Output:**
```text
(a,b):( 6 , 30 )
Global a : 90
```

## Local Variables

A variable declared inside the function's body or in the local scope is known as a local variable.

If we try to access the local variable from the outside of the function, we will get the error as **`NameError`**.

```python
# Example 1: Accessing local variable outside the scope

def fun():
    y = "local"
    
fun()
print(y)
```

The output shows an error because we are trying to access a local variable **`y`** in a global scope whereas the local variable only works inside **`fun()`** or local scope.

```python
# Example 2: Create a Local Variable

# Normally, we declare a variable inside the function to create a local variable.

def fun():
    y = "local"
    print(y)

fun()
```

**Output:**
```text
local
```

Let's take a look at the cell **In [2]: # Example 3:** where **`x`** was a global variable and we wanted to modify **`x`** inside **`fun()`**.

```python
# Exercise 3: 

def fun1():
    loc_var = 999   # local variable
    print("Value is :", loc_var)

def fun2():
    print("Value is :", loc_var)

fun1()
fun2()
```

**Output:**
```text
Value is : 999
```

## Global and local variables

Here, we will show how to use global variables and local variables in the same code.

```python
# Example 1: Using Global and Local variables in the same code

x = "global"

def fun():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

fun()
```

**Output:**
```text
globalglobal
local
```

**Explanation**:

In the above code, we declare **`x`** as a global and **`y`** as a local variable in the **`fun()`**. Then, we use multiplication operator **`*`** to modify the global variable **`x`** and we print both **`x`** and **`y`**.

After calling the **`fun()`**, the value of **`x`** becomes **`global global`** because we used the **`x * 2`** to print two times **`global`**. After that, we print the value of local variable **`y`** i.e **`local`**.

```python
# Example 2: Global variable and Local variable with same name

x = 9

def fun():
    x = 19
    print("local x:", x)


fun()
print("global x:", x)
```

**Output:**
```text
local x: 19
global x: 9
```

**Explanation**:

In the above code, we used the same name **`x`** for both global variable and local variable. We get a different result when we print the same variable because the variable is declared in both scopes, i.e. the local scope inside **`fun()`** and global scope outside **`fun()`**.

When we print the variable inside **`fun()`** it outputs **`local x: 19`**. This is called the local scope of the variable.

Similarly, when we print the variable outside the **`fun()`**, it outputs **`global x: 9`**. This is called the global scope of the variable.

```python
# Exercise 3: 

def my_func():  # for this Function I am not writing any argument in parenthesis '()'
    x = 10
    print("Value inside the body of function:",x)

x = 20                             # first, this line to execute
my_func()                          # second, the body of function will execute
print("Value outside of function:",x) # finally, this line will execute
```

**Output:**
```text
Value inside the body of function: 10
Value outside of function: 20
```

**Explanation:**

Here, we can see that the value of **`x`** is 20 initially. Even though the function **`my_func()`** changed the value of **`x`** to 10, it did not affect the value outside the function.

This is because the variable **`x`** inside the function is different (local to the function) from the one outside. Although they have the same names, they are two different variables with different scopes.

On the other hand, variables outside of the function are visible from inside. They have a global scope.

We can read these values from inside the function but cannot change (write) them. In order to modify the value of variables outside the function, they must be declared as global variables using the keyword global.

## Nonlocal Variables

Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.

Let's see an example of how a global variable is created in Python.

We use **`nonlocal`** keywords to create nonlocal variables.

```python
# Example 1: Create a nonlocal variable

x1 = "global"  # Global variable

def outer_fun():  # main function
    x1 = "local"  # 'x' is local variable for main function and it is nested variable for nested function
    print("variable type for Outer function:", x1)
    
    def inner_fun():  # nested fucntion
        nonlocal x1   # using local variable 'x' in nested function as nonloval variable
        x1 = "nonlocal"  # changing the value of my 'x'
        print("variable type for Inner function:", x1)  # print 'nonlocal'

    inner_fun()   #print("outer:", x1)  # print 'nonlocal'
    
outer_fun()
print("Variable type of x1:", x1)
```

**Output:**
```text
variable type for Outer function: local
variable type for Inner function: nonlocal
Variable type of x1: global
```

In the above code, there is a nested **`inner()`** function. We use nonlocal keywords to create a **`nonlocal`** variable. The **`inner()`** function is defined in the scope of another function **`outer()`**.

> **Note**: If we change the value of a nonlocal variable, the changes appear in the local variable.

```python
# Exercise 2: 

def outer_fun():
    x = 999

    def inner_fun():
        # local variable now acts as global variable
        nonlocal x
        x = 900
        print("value of x inside inner function is:", x)

    inner_fun()
    print("value of x inside outer function is:", x)

outer_fun()
```

**Output:**
```text
value of x inside inner function is: 900
value of x inside outer function is: 900
```

---

## 📘 Python All()
*Source: `4. Python Functions/3. Python all().ipynb`*

# Python `all()`

The **`all()`** method returns **`True`** when all elements in the given iterable are true. If not, it returns **`False`**.

**Syntax**:

```python
all(iterable)
```

## `all()` Parameters

**`any()`** method takes a single parameter:

* **iterable** - any iterable (**list**, **tuple**, **dictionary**, etc.) which contains the elements

## Return Value from `all()`

**`all()`** method returns:

* **`True`** If all elements in an iterable are true
* **`False`** If any element in an iterable is false

**Truth table for **`all()`****:

| When | Return Value |
|:----| :--- |
| **All values are true** | **True** |
| **All values are false** | **False** |
| **One value is true (others are false)** | **False** |
| **One value is false (others are true)** | **False** |
| **Empty Iterable** | **True** |

```python
# Example 1: How all() works for lists?

# all values true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))
```

**Output:**
```text
True
False
False
False
True
```

The **`all()`** method works in a similar way for tuples and sets like lists.

```python
# Example 2: How all() works for strings?

s = "This is good"
print(all(s))

# 0 is False
# '0' is True
s = '000'
print(all(s))

s = ''
print(all(s))
```

**Output:**
```text
True
True
True
```

```python
# Example 3: Using all() with Python Dictionaries

# In the case of dictionaries, if all keys (not values) are false or the dictionary is empty, 
# `all()` returns `True`. Else, it returns false for all other cases.

s = {0: 'False', 1: 'False'}
print(all(s))

s = {1: 'True', 2: 'True'}
print(all(s))

s = {1: 'True', False: 0}
print(all(s))

s = {}
print(all(s))

# 0 is False
# '0' is True
s = {'0': 'True'}
print(all(s))
```

**Output:**
```text
False
True
False
True
True
```

---

## 📘 Python Function Global Keywords
*Source: `4. Python Functions/3. Python Function global Keywords.ipynb`*

# Python `global` Keyword

In this class, you’ll learn about the **`global`** keyword, global variable and when to use **`global`** keyword.

Before reading this article, make sure you have got some basics of **Python Global, Local and Nonlocal Variables**.

# What is `global` keyword?

In Python, **`global`** keyword allows you to modify the variable outside of the current scope. It is used to create a global variable and make changes to the variable in a local context.

## Rules of `global` Keyword

The basic rules for **`global`** keyword in Python are:

1. When we create a variable inside a function, it is local by default.
2. When we define a variable outside of a function, it is global by default. You don't have to use **`global`** keyword.
3. We use **`global`** keyword to read and write a global variable inside a function.
4. Use of **`global`** keyword outside a function has no effect.

## Use of `global` Keyword

```python
# Example 1: Accessing global Variable From Inside a Function

a = 1 # global variable

def add():
    print(a)

add()
```

**Output:**
```text
1
```

However, we may have some scenarios where we need to modify the global variable from inside a function.

```python
# Example 2: Modifying Global Variable From Inside the Function

a = 1 # global variable
    
def add():
    a = a + 3 # increment a by 3 (modifying my global variable)
    print(a)

add()
```

This is because we can only access the global variable but cannot modify it from inside the function.

The solution for this is to use the **`global`** keyword.

```python
# Example 2: Changing Global Variable From Inside a Function using global

a = 0 # global variable

def add():
    global a  # using global variable inside my function
    a = a + 3 # increment by 3
    print("Inside add():", a)

add()
print("In main:", a)
```

**Output:**
```text
Inside add(): 3
In main: 3
```

**Explanation:**

In the above program, we define **`a`** as a global keyword inside the **`add()`** function.

Then, we increment the variable **`a`** by 1, i.e **`a = a + 3`**. After that, we call the **`add()`** function. Finally, we print the global variable **`a`**.

As we can see, change also occurred on the global variable outside the function, **`a = 3`**.

Let’s see another example where we don’t use **`global`** keyword to access the global variable in the function.

```python
# Exercise 3: without `global` keyword.

global_var = 9   # Global variable

def fun1():
    print("Value in 1st function:", global_var)

def fun2():
    # Modify global variable
    # function will treat it as a local variable
    global_var = 999
    print("Value in 2nd function:", global_var)

def fun3():
    print("Value in 3rd function:", global_var)

fun1()
fun2()
fun3()
```

**Output:**
```text
Value in 1st function: 9
Value in 2nd function: 999
Value in 3rd function: 9
```

**Explanation:**

As you can see, **`fun2()`** treated **`global_var`** as a new variable (local variable). To solve such issues or access/modify global variables inside a function, we use the **`global`** keyword.

```python
# Exercise 3: use the `global` keyword.


x = 9   # Global variable

# defining 1st function
def fun1():
    print("Value in 1st function:", x)

# defining 2nd function
def fun2():
    # Modify global variable using global keyword
    global x
    x = 999
    print("Value in 2nd function:", x)

# defining 3rd function
def fun3():
    print("Value in 3rd function:", x)

fun1()
fun2()
fun3()
```

**Output:**
```text
Value in 1st function: 9
Value in 2nd function: 999
Value in 3rd function: 999
```

## Global Variables Across Python Modules

In Python, we create a single module **config.py** to hold global variables and share information across Python modules within the same program.

Here is how we can share global variables across the python modules.

### Example : Share a global Variable Across Python Modules

Create a **config.py** file, to store global variables

```python
>>> a = 0
>>> b = "empty"
```

Create a **update.py** file, to change global variables

```python
>>> import config  # import config.py here

>>> config.a = 10  # change the value of 'a' from 0 to 10
>>> config.b = "alphabet"  # change the value of 'b' from "empty" to "alphabet"
```

Create a **main1.py** file, to test changes in value

```python
>>> import config  # import config.py here
>>> import update  # import update.py here

>>> print(config.a)  # print the updated value of 'a'
>>> print(config.b)  # print the updated value of 'b'
```

When we run the **main.py** file, the output will be

`
10
alphabet
`

In the above, we have created three files: **config.py**, **update.py**, and **main.py**.

The module **config.py** stores global variables of **`a`** and **`b`**. In the **update.py** file, we import the **config.py** module and modify the values of **`a`** and **`b`**. Similarly, in the **main.py** file, we import both **config.py** and **update.py** module. Finally, we print and test the values of global variables whether they are changed or not.

## Global in Nested Functions

Here is how you can use a global variable in nested function.

```python
# Example 1: Using a Global Variable in Nested Function

def fun():  # main function
    x = 30

    def day():  # nested fucntion
        global x
        x = 66
    
    print("Before calling bar function:", x)  # check indentation
    print("Calling bar function now")
    day()
    print("After calling bar function:", x)

fun()
print("x in main function:", x)
```

**Output:**
```text
Before calling bar function: 30
Calling bar function now
After calling bar function: 30
x in main function: 66
```

**Explanation:**

In the above program, we declared a global variable inside the nested function **`day()`**. Inside **`fun()`** function, **`x`** has no effect of the global keyword.

Before and after calling **`day()`**, the variable **`x`** takes the value of local variable i.e **`x = 30`**. Outside of the **`fun()`** function, the variable **`x`** will take value defined in the **`day()`** function i.e **`x = 66`**. This is because we have used global keyword in **`x`** to create global variable inside the **`day()`** function (local scope).

If we make any changes inside the **`day()`** function, the changes appear outside the local scope, i.e. **`fun()`**.

---

## 📘 Python Ascii()
*Source: `4. Python Functions/4. Python ascii().ipynb`*

# Python `ascii()`

The **`ascii()`** method returns a string containing a printable representation of an object. It escapes the non-ASCII characters in the string using **`\x`**, **`\u`** or **`\U`** escapes.

**Syntax**:

```python
ascii(object)
```

## `ascii()` Parameters

**`ascii()`** method takes an object (like: **strings**, **list** etc).

## Return Value from `ascii()`

It returns a string containing a printable representation of an object.

For example, **`ö`** is changed to **`\xf6n`**, **`√`** is changed to **`\u221a`**

The non-ASCII characters in the string are escaped using **`\x`**, **`\u`** or **`\U`**.

```python
# Example 1: How ascii() method works?

normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')
```

**Output:**
```text
'Python is interesting'
'Pyth\xf6n is interesting'
Pythön is interesting
```

```python
# Example 2: randomList

randomList = ['Python', 'Pythön', 5]
print(ascii(randomList))
```

**Output:**
```text
['Python', 'Pyth\xf6n', 5]
```

---

## 📘 Python Function Arguments
*Source: `4. Python Functions/4. Python Function Arguments.ipynb`*

# Function Argument and Parameter

The argument is a value, a variable, or an object that we pass to a function or method call. 

There can be two types of data passed in the function.

* The First type of data is the data passed in the function call. This data is called **arguments**.

* The second type of data is the data received in the function definition. This data is called **parameters**.

    - Arguments can be literals, variables and expressions. 
    - Parameters must be variable to hold incoming values.

Alternatively, arguments can be called as **actual parameters** or **actual arguments** and parameters can be called as **formal parameters** or **formal arguments**.

# Python Function Arguments

In Python, you can define a function that takes variable number of arguments. In this article, you will learn to define such functions using default, keyword and arbitrary arguments.

In Python, there are 2 types of arguments allowed.
<b>
1. Positional Arguments (Basic)
2. Variable Function Arguments
</b>

## Positional Arguments (Basic)

In the **User-defined function** topic, we learned about defining a function and calling it. Otherwise, the function call will result in an error. For example:

```python
# Example 1:

def greet(name, msg):
    """This function greets to the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Arthur", "Good morning!")
```

**Output:**
```text
Hello Arthur, Good morning!
```

**Explanation:**

Here, the function **`greet()`** has two parameters.

Since we have called this function with two arguments, it runs smoothly and we do not get any error.

If we call it with a different number of arguments, the interpreter will show an error message. Below is a call to this function with one and no arguments along with their respective error messages.

```python
greet("Arthur")    # only one argument
```

```python
greet()    # no arguments
```

```python
# Example 2:

def add(a, b):
    print(a - b)

add(90, 30)  # Output 60
add(60, 30)  # Output -30
```

**Output:**
```text
60
30
```

```python
# Example 2: If you try to use pass more parameters you will get an error.

def add(a, b):
    print(a - b)
add(109, 633, 9)
```

>**Note:** In the **Positional argument** number and position of arguments must be matched. If we change the order, then the result may change. Also, If we change the number of arguments, then we will get an error.

```python
# Example 3:

def evenodd(x):     # x is parameters or formal parameters or formal arguments.
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

# Driver code
evenodd(6)   # here 2 is argument or actual perameter
evenodd(9)   # here 3 is argument or actual perameter
```

**Output:**
```text
even
odd
```

```python
# Example 4:

def cube(x):
    "This x a passed num value into this function, return cube of x"
    y=x*x*x;
    return y

# Now you can call cube function
z=cube(2)  #required to pass argument
print(z)
```

**Output:**
```text
8
```

## Variable Function Arguments

Up until now, functions had a fixed number of arguments. In Python, there are other ways to define a function that can take variable number of arguments.

Three different forms of this type are described below:
<b>
1. Default Arguments
2. Keyword Arguments
3. Arbitrary/Variable-length Arguments
</b>

### Python Default Arguments

Default arguments are arguments that take the default value during the function call. If we do not pass any argument to the function, then the default argument will take place. We can assign default values using the **`=`** assignment operator. For example:

```python
# Example 1:

def greet(name, msg="Good morning!"):  # two arguments: `name` is fixed arg and 'msg' is variable arg

    print("Hello", name + ', ' + msg)


greet("Alan")
greet("Bruce", "How do you do?")
greet("Carson","Good night!")
```

**Output:**
```text
Hello Alan, Good morning!
Hello Bruce, How do you do?
Hello Carson, Good night!
```

**Explanation:**

In this function, the parameter **`name`** does not have a default value and is required (mandatory) during a call.

On the other hand, the parameter **`msg`** has a default value of **`"Good morning!"`**. So, it is optional during a call. If a value is provided, it will overwrite the default value.

Any number of arguments in a function can have a default value. But once we have a default argument, all the arguments to its right must also have default values.

This means to say, non-default arguments cannot follow default arguments. For example, if we had defined the function header above as:

```python
>>> def greet(msg = "Good morning!", name):
```

We would get an error as:
```python
SyntaxError: non-default argument follows default argument
```

```python
# Example 2: function with default argument

def message(name="Everyone"):
    print("Hello", name)

# calling function with argument
message("David")

# calling function without argument
message()
```

**Output:**
```text
Hello David
Hello Everyone
```

**Explanation:** 

When we call a function with an argument, it will be considered that value.

Like in the above example, we passed **`name="David"`** we pass to the function, then the function will consider that value. If we do not pass any argument, it will be considered **`"name=Everyone"`** as a default value.

```python
# Example 3: it prints default age if it is not passed

def emp_data(name, emp_id, age, company="Baidu.com"):  # total 4 arguments (3 is fixed and 1 is variable)
    print("Details of: ",name)
    print("Empoyee Id : ",emp_id)
    print("Age : ",age)
    print("Company : ",company)

#call emp_data fun
emp_data("Bill",101,21,"Samsung.com")
print("-----------------------")
emp_data("Cory",102,22)
```

**Output:**
```text
Details of:  Bill
Empoyee Id :  101
Age :  21
Company :  Samsung.com
-----------------------
Details of:  Cory
Empoyee Id :  102
Age :  22
Company :  Baidu.com
```

### Python Keyword Arguments

Keyword arguments are related to the function calls. A keyword argument is an argument value, passed to function preceded by the variable name and an equals sign.

This allows you to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters.

```python
# Example 1:

greet("Eric", "How do you do?")

# 2 keyword arguments
greet(name = "Eric",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Eric") 

# 1 positional, 1 keyword argument
greet("Eric", msg = "How do you do?")
```

**Output:**
```text
Hello Eric, How do you do?
Hello Eric, How do you do?
Hello Eric, How do you do?
Hello Eric, How do you do?
```

As we can see, we can mix positional arguments with keyword arguments during a function call. But we must keep in mind that keyword arguments must follow positional arguments.

Having a positional argument after keyword arguments will result in errors. For example, the function call as follows:

```python
greet("Eric","How do you do?")
```

**Output:**
```text
Hello Eric, How do you do?
```

```python
greet(name="Eric","How do you do?")  # Will result in an error
```

```python
# Example 2:

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print(print_fullname(firstname = 'Milaan', lastname = 'Parmar'))
```

**Output:**
```text
Milaan Parmar
```

```python
# Example 3:

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
```

**Output:**
```text
5
```

```python
# Example 4:

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))
```

**Output:**
```text
Age:  200
```

```python
# Example 5:

def remainder(dividend,divisor):
    x=dividend%divisor
    return x

#rem = remainder(10,3)
rem = remainder(divisor = 3, dividend = 10) # keyword argument
print("remainder of 10/3 : ",rem)
```

**Output:**
```text
remainder of 10/3 :  1
```

```python
# Example 6:

def message(name, surname):
    print("Hello", name, surname)

message(name="Frank", surname="Harper")
message(surname="Clayton", name="Gretta")
```

**Output:**
```text
Hello Frank Harper
Hello Gretta Clayton
```

In keyword arguments order of argument is not matter, but the number of arguments must match. Otherwise, we will get an error.

While using keyword and positional argument simultaneously, we need to pass 1st arguments as positional arguments and then keyword arguments. Otherwise, we will get **`SyntaxError`**. See the following example.

```python
# Example 7:

def message(first_nm, last_nm):
    print("Hello..!", first_nm, last_nm)

# correct use
message("Frank", "Harper")
message("Frank", last_nm="Harper")

message(first_nm="Frank", "Harper")  # SyntaxError: positional argument follows keyword argument
```

### Python Arbitrary/Variable-length Arguments

Sometimes, we do not know in advance the number of arguments that will be passed into a function. Python allows us to handle this kind of situation through function calls with an arbitrary number of arguments.

We can pass any number of arguments to this function. Internally all these values are represented in the form of a **tuple**.

In the function definition, we use an asterisk **`*`** before the parameter name to denote this kind of argument. For example:

```python
# Example 1: 

def greet(*names):
    """This function greets all the person in the names tuple."""
    # names is a tuple with arguments
    for name in names:
        print("Hello", name)

greet("Gary", "Hank", "Ivan", "John")
```

**Output:**
```text
Hello Gary
Hello Hank
Hello Ivan
Hello John
```

Here, we have called the function with multiple arguments. These arguments get wrapped up into a tuple before being passed into the function. Inside the function, we use a **`for`** loop to retrieve all the arguments back.

```python
# Example 2: 

def addition(*numbers):
    total = 0
    for no in numbers:
        total = total + no
    print("Sum is:", total)

addition()                 # 0 arguments
addition(10, 5, 3, 6, 9)   # 5 arguments
addition(96, 77, 3.6)      # 3 arguments
```

**Output:**
```text
Sum is: 0
Sum is: 33
Sum is: 176.6
```

```python
# Example 3: 

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

**Output:**
```text
10
```

Default and Arbitrary Number of Parameters in Functions

```python
# Example 1: 

def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print ("Output is: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return

    # Now you can call printinfo function
printinfo( 10 ) # We have given only one value for the argument
printinfo( 70, 40, 20 )
printinfo( 30, 60, 90, 120 )
```

**Output:**
```text
Output is: 
10
Output is: 
70
40
20
Output is: 
30
60
90
120
```

```python
# Example 2: 

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Milaan','Arthur','Clark','Ethan'))
```

**Output:**
```text
Team-1
Milaan
Arthur
Clark
Ethan
None
```

## Function as a Parameter of Another Function

```python
# Example 1: You can pass functions around as parameters

def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

**Output:**
```text
9
```

---

## 📘 Python Bin()
*Source: `4. Python Functions/5. Python bin().ipynb`*

# Python `bin()`

The **`bin()`** method converts and returns the binary equivalent string of a given integer. If the parameter isn't an integer, it has to implement **`__index__()`** method to return an integer.

**Syntax**:

```python
bin(num)
```

## `bin()` Parameters

**`bin()`** method takes a single parameter:

* **num** - an integer number whose binary equivalent is to be calculated.
If not an integer, should implement **`__index__()`** method to return an integer.

## Return Value from `bin()`

**`bin()`** method returns the binary string equivalent to the given integer.

If not specified an integer, it raises a **`TypeError`** exception highlighting the type cannot be interpreted as an integer.

```python
# Example 1: Convert integer to binary using bin()
number = 5
print('The binary equivalent of 5 is:', bin(number))
```

**Output:**
```text
The binary equivalent of 5 is: 0b101
```

The prefix **`0b`** represents that the result is a binary string.

```python
# Example 2: Convert an object to binary implementing __index__() method

class Quantity:
    apple = 1
    orange = 2
    grapes = 2
    
    def __index__(self):
        return self.apple + self.orange + self.grapes
        
print('The binary equivalent of quantity is:', bin(Quantity()))
```

**Output:**
```text
The binary equivalent of quantity is: 0b101
```

**Explanation**:

Here, we've sent an object of class **`Quantity`** to the **`bin()`** method.

**`bin()`** method doesn't raise an error even if the object Quantity is not an integer.

This is because we have implemented the **`__index__()`** method which returns an integer (sum of fruit quantities). This integer is then supplied to the **`bin()`** method.

---

## 📘 Python Function Recursion
*Source: `4. Python Functions/5. Python Function Recursion.ipynb`*

# Python Recursion

In this class, you will learn to create a recursive function (a function that calls itself again and again).

# What is recursion?

Recursion is the process of defining something in terms of itself.

A physical world example would be to **place two parallel mirrors facing each other**. Any object in between them would be reflected recursively.

## Python Recursive Function

In Python, we know that a **function** can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

The following image shows the working of a recursive function called **`recurse`**.

<div>

</div>

Following is an example of a recursive function to find the factorial of an integer.

Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 6 (denoted as 6!) is 

```python
1*2*3*4*5*6 = 720.
```

```python
# Example 1:

def factorial(n):
    """This is a recursive function to find the factorial of an integer"""

    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))  # 3 * 2 * 1 = 6


num = 3
print("The factorial of", num, "is", factorial(num))
```

**Output:**
```text
The factorial of 3 is 6
```

In the above example, **`factorial()`** is a recursive function as it calls itself.

When we call this function with a positive integer, it will recursively call itself by decreasing the number.

Each function multiplies the number with the factorial of the number below it until it is equal to one. This recursive call can be explained in the following steps.

```python
factorial(3)          # 1st call with 3
3 * factorial(2)      # 2nd call with 2
3 * 2 * factorial(1)  # 3rd call with 1
3 * 2 * 1             # return from 3rd call as number=1
3 * 2                 # return from 2nd call
6                     # return from 1st call
```

Let's look at an image that shows a step-by-step process of what is going on:

<div>

</div>

Our recursion ends when the number reduces to 1. This is called the base condition.

Every recursive function must have a base condition that stops the recursion or else the function calls itself infinitely.

The Python interpreter limits the depths of recursion to help avoid infinite recursions, resulting in stack overflows.

By default, the maximum depth of recursion is **`1000`**. If the limit is crossed, it results in **`RecursionError`**. Let's look at one such condition.

```python
def recursor():
    recursor()
recursor()
```

## Advantages of Recursion

1. Recursive functions make the code look clean and elegant.
2. A complex task can be broken down into simpler sub-problems using recursion.
3. Sequence generation is easier with recursion than using some nested iteration.

## Disadvantages of Recursion

1. Sometimes the logic behind recursion is hard to follow through.
2. Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
3. Recursive functions are hard to debug.

---

## 📘 Python Bool()
*Source: `4. Python Functions/6. Python bool().ipynb`*

# Python `bool()`

The **`bool()`** method converts a value to Boolean (**`True`** or **`False`**) using the standard truth testing procedure.

**Syntax**:

```python
bool([value])
```

## `bool()` Parameters

It's not mandatory to pass a value to **`bool()`**. If you do not pass a value, **`bool()`** returns **`False`**.

In general use, **`bool()`** takes a single parameter value.

## Return Value from `bool()`

**`bool()`** returns:

* **`False`** if the **`value`** is omitted or false
* **`True`** if the **`value`** is true

## The following values are considered false in Python:

* **`None`**
* **`False`**
* Zero of any numeric type. For example, **`0`**, **`0.0`**, **`0j`**
* Empty sequence. For example, **`()`**, **`[]`**, **`''`**.
* Empty mapping. For example, **`{}`**
* objects of Classes which has **`__bool__()`** or **`__len()__`** method which returns **`0`** or **`False`**

All other values except these values are considered true.

```python
# Example 1: How bool() works?

test = []
print(test,'is',bool(test))

test = [0]
print(test,'is',bool(test))

test = 0.0
print(test,'is',bool(test))

test = None
print(test,'is',bool(test))

test = True
print(test,'is',bool(test))

test = 'Easy string'
print(test,'is',bool(test))
```

**Output:**
```text
[] is False
[0] is True
0.0 is False
None is False
True is True
Easy string is True
```

---

## 📘 Python Function Anonymous
*Source: `4. Python Functions/6. Python Function Anonymous.ipynb`*

# Python Anonymous/**`lambda`** Function

In this class, you'll learn about the anonymous function, also known as **`lambda`** functions. You'll learn what they are, their syntax and how to use them (with examples).

## What are **`lambda`** functions in Python?

In Python, an anonymous function is a **function** that is defined without a name.

While normal functions are defined using the **`def`** keyword in Python, anonymous functions are defined using the **`lambda`** keyword.

In opposite to a normal function, a Python **`lambda`** function is a single expression. But, in a lambda body, we can expand with expressions over multiple lines using parentheses **`()`** or a multiline string **`""" """`**.

For example: **`lambda n:n+n`**

The reason behind the using anonymous function is for instant use, that is, one-time usage and the code is very concise so that there is more readability in the code.

Hence, anonymous functions are also called **`lambda`** functions.

* Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.

* An anonymous function cannot be a direct call to print because **lambda** requires an expression. 

* **`lambda`** functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace. 

* Although it appears that lambdas are a one-line version of a function, they are not equivalent to inline statements in C or C++, whose purpose is to stack allocation by passing function, during invocation for performance reasons.

**Syntax:** 

```python
lambda argument_list: expression
```

Let’s see an example to print even numbers without a **`lambda`** function and with a **`lambda`** function. See the difference in line of code as well as readability of code.

```python
# Example 1: Program for even numbers without lambda function

def even_numbers(nums):
    even_list = []
    for n in nums:
        if n % 2 == 0:
            even_list.append(n)
    return even_list

num_list = [10, 9, 16, 78, 2, 3, 7, 1]
ans = even_numbers(num_list)
print("Even numbers are:", ans)
```

**Output:**
```text
Even numbers are: [10, 16, 78, 2]
```

```python
# Example 1: Program for even number with a lambda function

l = [10, 9, 16, 78, 2, 3, 7, 1]
even_nos = list(filter(lambda x: x % 2 == 0, l))
print("Even numbers are: ", even_nos)
```

**Output:**
```text
Even numbers are:  [10, 16, 78, 2]
```

```python
# Example 2: Program to show the use of lambda functions

double = lambda x: x * 2

print(double(6))
```

**Output:**
```text
12
```

**Explanation:**

In the above program, lambda **`x: x * 2`** is the lambda function. Here **`x`** is the argument and **`x * 2`** is the expression that gets evaluated and returned.

This function has no name. It returns a function object which is assigned to the identifier **`double`**. We can now call it as a normal function. The statement

```python
>>> double = lambda x: x * 2
```

is nearly the same as:

```python
>>> def double(x):
>>>     return x * 2
```

```python
# Example 3: Normal Function definition is here

def square(x):
    return x*x

# anonymous function
sqr = lambda x: x*x

#Calling square function
print("Square of number is",square(10)) #call normal function
print("Square of number is",sqr(2)) #call anonymous function
```

**Output:**
```text
Square of number is 100
Square of number is 4
```

## Use of **`lambda`** Function in python

We use **`lambda`** function when we require a nameless function for a short period of time.

In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as **arguments**). **`lambda`** function are used along with built-in functions like **`filter()`**, **`map()`**, **`reduce()`** etc.

### `lambda` function use with `filter()`

The **`filter()`** function in Python takes in a function and a list as arguments.

The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to **`True`**.

Here is an example use of **`filter()`** function to filter out only even numbers from a list.

```python
# Example 1: Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]  # total 8 elements

new_list = list(filter(lambda x: (x%2 == 0), my_list)) # returns the output in form of a list

print("Even numbers are: ", new_list)
```

**Output:**
```text
Even numbers are:  [4, 6, 8, 12]
```

```python
# Example 2: 

l = [-10, 5, 12, -78, 6, -1, -7, 9]
positive_nos = list(filter(lambda x: x > 0, l))
print("Positive numbers are: ", positive_nos)
```

**Output:**
```text
Positive numbers are:  [5, 12, 6, 9]
```

### `lambda` function with `map()`

The **`map()`** function in Python takes in a function and a list.

The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.

Here is an example use of **`map()`** function to double all the items in a list.

```python
# Example 1: Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]  # total 8 elements
new_list = list(map(lambda x: x * 2, my_list)) # returns the output in form of a list
print("Double values are: ", new_list)
```

**Output:**
```text
Double values are:  [2, 10, 8, 12, 16, 22, 6, 24]
```

```python
# Example 2:

list1 = [2, 3, 4, 8, 9]
list2 = list(map(lambda x: x*x*x, list1))
print("Cube values are:", list2)
```

**Output:**
```text
Cube values are: [8, 27, 64, 512, 729]
```

### `lambda` function with `reduce()`

The **`reduce()`** function is used to minimize sequence elements into a single value by applying the specified condition.

The **`reduce()`** function is present in the **`functools`** module; hence, we need to import it using the import statement before using it.

```python
# Example 1:

from functools import reduce
list1 = [20, 13, 4, 8, 9]
add = reduce(lambda x, y: x+y, list1)
print("Addition of all list elements is : ", add)
```

**Output:**
```text
Addition of all list elements is :  54
```

---

## 📘 Python Bytearray()
*Source: `4. Python Functions/7. Python bytearray().ipynb`*

# Python `bytearray()`

The **`bytearray()`** method returns a bytearray object which is an array of the given bytes.

**Syntax**:

```python
bytearray([source[, encoding[, errors]]])
```

**`bytearray()`** method returns a bytearray object which is mutable (can be modified) sequence of integers in the range **`0 <= x < 256`**.

If you want the immutable version, use **bytes()** method.

## `bytearray()` Parameters

**`bytearray()`** method takes three optional parameters:

* **source (Optional)** - source to initialize the array of bytes.
* **encoding (Optional)** - if the source is a string, the encoding of the string.
* **errors (Optional)** - if the source is a string, the action to take when the encoding conversion fails (Read more: **String encoding**)

The **source** parameter can be used to initialize the byte array in the following ways:

**Different source parameters**:

| Type | Description |
|:----| :--- |
| **String** | **Converts the string to bytes using `str.encode()` Must also provide encoding and optionally errors** |
| **Integer** | **Creates an array of provided size, all initialized to null** |
| **Object** | **A read-only buffer of the object will be used to initialize the byte array** |
| **Iterable** | **Creates an array of size equal to the iterable count and initialized to the iterable elements Must be iterable of integers between `0 <= x < 256`** |
| **No source (arguments)** | **Creates an array of size `0`**. |

## Return Value from `bytearray()`

**`bytearray()`** method returns an array of bytes of the given size and initialization values.

```python
# Example 1: Array of bytes from a string

string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)
```

**Output:**
```text
bytearray(b'Python is interesting.')
```

```python
# Example 2: Array of bytes of given integer size

size = 5

arr = bytearray(size)
print(arr)
```

**Output:**
```text
bytearray(b'\x00\x00\x00\x00\x00')
```

```python
# Example 3: Array of bytes from an iterable list
rList = [1, 2, 3, 4, 5]

arr = bytearray(rList)
print(arr)
```

**Output:**
```text
bytearray(b'\x01\x02\x03\x04\x05')
```

---

## 📘 Python Function Module
*Source: `4. Python Functions/7. Python Function Module.ipynb`*

# Python Modules

In this class, you will learn to create and import custom modules in Python. Also, you will find different techniques to import and use custom and built-in modules in Python.

## What are modules in Python?

Module containing a set of codes or a set of functions which can be included to an application. Modules refer to the Python file, which contains Python code like Python statements, classes, functions, variables, etc. A file with Python code is defined with extension**`.py`**

For example: In **`main.py`**, where the **`main`** is the module name.

In Python, large code is divided into small modules. The benefit of modules is, it provides a way to share reusable functions.

## Advantage

* **Reusability**: Module can be used in some other python code. Hence it provides the facility of code reusability.
* **Categorization**: Similar type of attributes can be placed in one module.

## Creating a module in Python

A file containing Python code, for example: **`example.py`**, is called a module, and its module name would be **`example`**.

We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.

We can define our most used functions in a module and import it, instead of copying their definitions into different programs.

The module contains Python code like classes, functions, methods, but it also has variables. A variable can list, tuple, dict, etc.

Let us create a module. Type the following and save it as **`example.py`**.

```python
# Python Module example

>>> def add(a, b):
>>>     """This program adds two numbers and return the result"""
>>>     result = a + b
>>>     return result
```

Here, we have defined a **function** **`add()`** inside a module named **`example`**. The function takes in two numbers and returns their sum.

## How to import modules in Python?

We can import the definitions inside a module to another module or the interactive interpreter in Python.

We use the **`import`** keyword to do this. To import our previously defined module example, we type the following in the Python prompt.

```python
>>> import example
```
This does not import the names of the functions defined in **`example`** directly in the current symbol table. It only imports the module name **`example`** there.

Using the module name we can access the function using the dot **`.`** operator. For example:

**# Example 1:**

```python
import example
example.add(3,6.6)
```

**Output:**
```text
9.6
```

Python has tons of standard modules. You can check out the full list of **[Python standard modules](https://docs.python.org/3/py-modindex.html)** and their use cases. These files are in the Lib directory inside the location where you installed Python.

Standard modules can be imported the same way as we import our user-defined modules.

There are various ways to import modules. They are listed below:

**# Example 2:**

The Python code for a module named a name normally resides in a file **main.py**. But first create a function in **test.py**. Here is an example of a simple module,

**test.py** - 

```python
>>> def fun():
>>>     print("something here inside fun()")
```
**main.py** −

```python
>>> import test
>>> from test import fun
>>> fun()
```

Output of above example: Run **main.py**

`something here inside fun()`

----------------------------------------------------------------
For **test.ipynb** or **test1.ipynb** and **main.ipynb**

Open anaconda prompt and type **`pip install import-ipynb`**

see:
Downloading import-ipynb-0.1.3.tar.gz (4.0 kB)

**test.py** or **test1.ipynb** - 

```python
>>> def fun():
>>>     print("something here inside fun()")
```
**main.ipynb** −

```python
>>> import import_ipynb

>>> import test1
>>> from test1 import fun
>>> fun()
```

Output of above example: Run **main.ipynb**

`something here inside fun()`

**# Example 3:**

**fibo.py** - 

```python
# Fibonacci numbers module
>>> def fib(n): # return Fibonacci series up to n
>>>     result = []
>>>     a, b = 0, 1
>>>     while b < n:
>>>         result.append(b)
>>>         a, b = b, a + b
>>>     return result
```
**main.py** −

```python
>>> import fibo
>>> from fibo import fib
>>> print(fib(100))
```

Output of above example: Run **main.py**

`[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]`

----------------------------------------------------------------
For **test.ipynb** or **test1.ipynb** and **main.ipynb**

Open anaconda prompt and type **`pip install import-ipynb`**

see:
Downloading import-ipynb-0.1.3.tar.gz (4.0 kB)

**fibo1.ipynb** or **fibo.py** - 

```python
# Fibonacci numbers module
>>> def fib(n): # return Fibonacci series up to n
>>>     result = []
>>>     a, b = 0, 1
>>>     while b < n:
>>>         result.append(b)
>>>         a, b = b, a + b
>>>     return result
```
**main.ipynb** −

```python
>>> import import_ipynb

>>> import fibo1
>>> from fibo1 import fib
>>> print(fib(100))
```

Output of above example: Run **main.ipynb**

`[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]`

**# Example 4:**

**equal.py** - 

```python
#function definition
>>> def equal(a, b):
>>>     if(a == b):
>>>         return True
```
**main.py** −

```python
>>> from equal import *
>>> a, b = 10, 10
>>> print(equal(a, b))
```

Output of above example: Run **main.py**

`True`

----------------------------------------------------------------
For **equal.ipynb** or **equal1.ipynb** and **main.ipynb**

Open anaconda prompt and type **`pip install import-ipynb`**

see:
Downloading import-ipynb-0.1.3.tar.gz (4.0 kB)

**equal.ipynb** or **equal1.ipynb** - 

```python
#function definition
>>> def equal(a, b):
>>>     if(a == b):
>>>         return True
```
**main.ipynb** −

```python
>>> import import_ipynb

>>> from equal1 import *
>>> a, b = 10, 10
>>> print(equal(a, b))
```

Output of above example: Run **main.ipynb**

`True`

In Python, each and every built-in module has a large number of predefined functions to perform specific tasks. For instance, Python has a built-in module named **`operator`**, inside which the function called **`eq()`** is defined. This function returns the boolean value of **`True`** if the given two input values are equal. Else, returns **`False`**.

So now, we can make use of this operator module in our **`main()`** program to check if two numbers are equal. This means we would no longer need that **`equal.py`** module.

```python
# Example 5: 

#main function
from operator import *
a, b = 10, 10
print(eq(a, b))
```

**Output:**
```text
True
```

### Python `import` statement

We can import a module using the **`import`** statement and access the definitions inside it using the dot operator **`.`** as described above. Here is an example.

```python
# Example 1: 

# import statement example to import standard module math
import math
print("The value of pi is", math.pi)
```

**Output:**
```text
The value of pi is 3.141592653589793
```

```python
# Example 2:

import math

# use math module functions
print(math.sqrt(6))    # Output 2.449489742783178
```

**Output:**
```text
2.449489742783178
```

### `import` multiple modules

If we want to use more than one module, then we can import multiple modules. This is the simplest form of **`import`** a keyword that we already use in the above example.

```python
# Example 1: Import two modules

import math, random

print(math.factorial(6))
print(random.randint(10, 30))
```

**Output:**
```text
720
28
```

### Python `from-import` statement

To import particular classes or functions, we can use the **`from-import`** statement. It is an alternate way to **`import`**. By using this form, we can import individual attributes and methods directly into the program.We can import specific names from a module without importing the module as a whole.

```python
# Example 1: import only factorial function from math module
from math import factorial

print(factorial(6))
```

**Output:**
```text
720
```

```python
# Example 2: 

from math import pi, e
e
```

**Output:**
```text
2.718281828459045
```

```python
# Example 3: 

# import only pi from math module
from math import pi
print("The value of pi is", pi)
```

**Output:**
```text
The value of pi is 3.141592653589793
```

Here, we imported only the **`pi`** attribute from the **`math`** module.

In such cases, we don't use the dot operator. We can also import multiple attributes as follows:

```python
# Example 4: 

from math import pi, e
pi
```

**Output:**
```text
3.141592653589793
```

### `import` with renaming

We can import a module by renaming it as follows:

```python
# Example 1: 

# import module by renaming it
import math as m
print("The value of pi is", m.pi)
```

**Output:**
```text
The value of pi is 3.141592653589793
```

We have renamed the **`math`** module as **`m`**. This can save us typing time in some cases.

>**Note:** that the name **`math`** is not recognized in our scope. Hence, **`math.pi`** is invalid, and **`m.pi`** is the correct implementation.

```python
# Example 2:  Import a module by renaming it

import random as rand

print(rand.randrange(10, 20, 2))
```

**Output:**
```text
12
```

```python
# Example 3:  import a method by renaming it

# rename randint as random_number
from random import randint as random_number

# Gives any random number from range(10, 50)
print(random_number(30, 60))
```

**Output:**
```text
49
```

### `import` all names

We can **`import`** all functions and attributes of a specific module, then instead of writing all function names and attribute names, we can import all using an **asterisk** **`*`**.

```python
# Example 1: 

# import all names from the standard module math

from math import *
print("The value of pi is", pi)
```

**Output:**
```text
The value of pi is 3.141592653589793
```

Here, we have imported all the definitions from the **`math`** module. This includes all names visible in our scope except those beginning with an underscore(private definitions).

Importing everything with the asterisk **`*`** symbol is not a good programming practice. This can lead to duplicate definitions for an identifier. It also hampers the readability of our code.

```python
# Example 2: 

from math import *
print(pow(6,3))
print(factorial(6))

print(pi*3)
print(sqrt(100))
```

**Output:**
```text
216.0
720
9.42477796076938
10.0
```

## Python Module Search Path

While importing a module, Python looks at several places. Interpreter first looks for a built-in module. Then(if built-in module not found), Python looks into a list of directories defined in **`sys.path`**. The search is in this order.

1. The current directory.
2. **`PYTHONPATH`** (an environment variable with a list of directories).
3. The installation-dependent default directory.

```python
import sys
sys.path
```

**Output:**
```text
['C:\\Users\\Dell\\Downloads\\04_Python_Functions-main',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\python37.zip',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\DLLs',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\lib',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3',
 '',
 'C:\\Users\\Dell\\AppData\\Roaming\\Python\\Python37\\site-packages',
 'C:\\Users\\Dell\\AppData\\Roaming\\Python\\Python37\\site-packages\\win32',
 'C:\\Users\\Dell\\AppData\\Roaming\\Python\\Python37\\site-packages\\win32\\lib',
 'C:\\Users\\Dell\\AppData\\Roaming\\Python\\Python37\\site-packages\\Pythonwin',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\win32',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\win32\\lib',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\Pythonwin',
 'C:\\Users\\Dell\\AppDat
... [Output truncated for brevity]
```

We can add and modify this list to add our own path.

## Reloading a module

The Python interpreter imports a module only once during a session. This makes things more efficient. Foe example:

**# Example 1:**

Suppose we have the following code in a module named **`my_module`**.

```python
# This module shows the effect of
#  multiple imports and reload

print("This code got executed")
```

```python
import my_module
```

**Output:**
```text
This code got executed
```

We can see that our code got executed only once. This goes to say that our module was imported only once.

Now if our module changed during the course of the program, we would have to reload it.One way to do this is to restart the interpreter. But this does not help much.

Python provides a more efficient way of doing this. We can use the **`reload()`** function inside the **`imp`** module to reload a module. We can do it in the following ways:

```python
import imp
import my_module
```

```python
import my_module
imp.reload(my_module)
```

**Output:**
```text
This code got executed
<module 'my_module' from 'C:\\Users\\Deepak\\01_Learn_Python4Data\\04_Python_Functions\\my_module.py'>
```

**# Example 2:**

First, create a Python module with the name **`greet_module.pynb`**
and write the below code in that file.

```python
>>> print("Welcome to Dr Parmar's Python4DataScience class")
```

Now, create a Python file with the name, **main.py** and write the below code in it and import the module test_module.py. See the following code.

```python
>>> import import_ipynb
>>> import time
>>> from importlib import reload

>>> # load 1st time
>>> import test_module
>>> time.sleep(25)
>>> # reload 
>>> reload(test_module)
>>> time.sleep(25) 

>>> # reload again  
>>> reload(test_module)
>>> print("This is test file..")
```

Output of above example: Run **main.py** 

```python
Welcome to Dr Parmar's Python4DataScience class
Welcome to Dr Parmar's Python4DataScience class
Welcome to Dr Parmar's Python4DataScience class
This is test file..
```

## The `dir()` built-in function

We can use the **`dir()`** function to find out names that are defined inside a module. When we use this function with any object (an object can be sequence like list, tuple, set, dict or can be class, function, module, etc. ), it returns properties, attributes, and method.

For example, we have defined a function **`add()`** in the module example that we had in the beginning.

We can use dir in example module in the following way:

```python
# Example 1:

dir(example)
```

**Output:**
```text
['__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'add']
```

Here, we can see a sorted list of names (along with **`add`**). All other names that begin with an underscore are default Python attributes associated with the module (not user-defined).

For example, the **`__name__`** attribute contains the name of the module.

```python
# Example 2:

import example
example.__name__
```

**Output:**
```text
'example'
```

All the names defined in our current namespace can be found out using the **`dir()`** function without any arguments.

```python
# Example 3:

a = 1
b = "hello"
import math
dir()
['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']
```

**Output:**
```text
['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']
```

```python
# Example 4:

import math

print(dir(math))
```

**Output:**
```text
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
```

## Python Modules List

Using Python built-in function **`help()`**, we can obtain the list of built-in modules available in Python. On executing the line help ('modules') in Python IDE, you can see all the Python built-in modules. Some of the frequently used ones are discussed below.

| Module | Description |
|:----| :--- |
| **`Operator`** |   This module provides a set of pre-defined functions corresponding to operators in Python.  | 
| **`decimal`** |   This module is used to print the complete decimal value when one number is divided by another number.  | 
| **random** |   random module is used to generate random numbers. Some of the pre-defined functions of this module are **`randint()`**, **`choice()`**, **`uniform`**, etc.  | 
| **`string`** |   string module provides a set of functions that are used to perform certain operations on characters. This module has pre-defined functions like capwords, ascii_letters, etc.  | 
| **math** |   math module is used to perform mathematical operations. This module provides some pre-defined mathematical functions like sqrt, factorial, etc.  |

## Python Built-In Modules Examples

There are many **built-in** modules in Python. Some of the common built-in modules: **`os`**, **[sys](https://docs.python.org/3/library/sys.html)**, **`operator`**, **`string`**, **`decimal`**, **random** , **math**, **`statistics`**, **`datetime`**, **`time`**, **`collections`**, **`threading`**, **`mailbox`**, **`tkinter`**, **`json`**, **`re`**, etc.

### Example Using `os` Module

Using python **`os`** module it is possible to automatically perform many operating system tasks. The **`os`** module in Python provides functions for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory.

```python
# Example 1:

# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

### Example Using `sys` Module

The **[sys](https://docs.python.org/3/library/sys.html)** module provides functions and variables used to manipulate different parts of the Python runtime environment.

**`sys.argv`** function returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.

```python
import sys
sys.path
```

**Output:**
```text
['C:\\Users\\Dell\\Downloads\\04_Python_Functions-main',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\python37.zip',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\DLLs',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\lib',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3',
 '',
 'C:\\Users\\Dell\\AppData\\Roaming\\Python\\Python37\\site-packages',
 'C:\\Users\\Dell\\AppData\\Roaming\\Python\\Python37\\site-packages\\win32',
 'C:\\Users\\Dell\\AppData\\Roaming\\Python\\Python37\\site-packages\\win32\\lib',
 'C:\\Users\\Dell\\AppData\\Roaming\\Python\\Python37\\site-packages\\Pythonwin',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\win32',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\win32\\lib',
 'C:\\Users\\Dell\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\Pythonwin',
 'C:\\Users\\Dell\\AppDat
... [Output truncated for brevity]
```

**First**, create a Python module with the name **`script.py`** and write the below code in that file.

```py
>>> import sys
>>> # print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
>>> print('Welcome {}. Enjoy  {} for Data Science ^_^'.format(sys.argv[1], sys.argv[2]))
```
**Second**, open **`Anaconda Prompt (Anaconda3)`**

**Third**, type system path after **`cd`**

```sy
cd D:\\Final Training\\Python with Code\\4. Python Functions\\04_Python_Functions
```

**Forth**, type

```sy
python script.py Alpha Python
```

**Output:**

```sy
Welcome Alpha. Enjoy  Python for Data Science ^_^
```

<div>

</div>

Some useful **`sys`** commands to type in:

```py
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version
```

### Example Using `operator` Module

```python
# Example 1:

from operator import *
a, b = 10, 20
#prints the product of the values 'a' and 'b'
print(mul(a, b))
#prints True if the value of 'a' is greater than 'b'. Else, False
print(gt(a, b))
#prints the remainder value, when the value of 'a' is divided by 'b'
print(mod(a, b))
#concatenates and prints the given two strings
print(concat("Hello ", "World"))
```

**Output:**
```text
200
False
10
Hello World
```

### Example Using `string` Module

A **string** module is a useful module for many purposes. The example below shows some use of the string module.

```python
# Example 1:

from string import *
print(capwords("hello world")) #capitalizes the first letter of each words
print(ascii_letters) #prints all lowercase and uppercase letters
```

**Output:**
```text
Hello World
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```

```python
# Example 2:

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

**Output:**
```text
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Example Using `decimal` Module

```python
# Example 1:

from decimal import *
a, b = 10, 3
c = a / b
print(c)
print(Decimal(c)) #prints the complete decimal value of c
```

**Output:**
```text
3.3333333333333335
3.333333333333333481363069950020872056484222412109375
```

### Example Using `random` Module

The **random** module is used to generate the random numbers. It provides the following two built in functions:

#### Comparision operators in Python

| Function | Description |
|:----| :--- |
| **`random()`** |   It returns a random number between 0.0 and 1.0 where 1.0 is exclusive.  | 
| **`randint(x,y)`** |   It returns a random number between x and y where both the numbers are inclusive.  |

```python
# Example 1:

from random import *
print(randint(10, 20)) #prints a random number between the given range

list1 = [30, 23, 45, 16, 89, 56]
print(choice(list1)) #prints a random element from the given iterator

print(uniform(10, 20)) #prints a random float number between two given values
```

**Output:**
```text
10
16
13.03505598723366
```

```python
# Example 2:

import random

print(random.random())
print(random.randint(2,8))
```

**Output:**
```text
0.2946014910624595
8
```

```python
# Example 3:

from random import randint   # import randint function

print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999

# call randint function to get random number
print(randint(10, 30))  # it returns a random integer number between [10, 30] inclusive
```

### Example Using `math` Module

Using **math** module, you can use different built in mathematical functions.

#### math module Functions:

| Function | Description |
|:----| :--- |
| **`ceil(n)`** |   It returns the next integer number of the given number.  | 
| **`sqrt(n)`** |   It returns the Square root of the given number.  | 
| **`exp(n)`** |   It returns the natural logarithm e raised to the given number.  | 
| **`floor(n)`** |   It returns the previous integer number of the given number.  | 
| **`log(n,baseto)`** |   It returns the previous integer number of the given number.  | 
| **`pow(baseto, exp)`** |   It returns baseto raised to the exp power.  | 
| **`sin(n)`** |   It returns sine of the given radian.  | 
| **`cos(n)`** |   It returns cosine of the given radian.  | 
| **`tan(n)`** |   It returns tangent of the given radian.  |

```python
# Example 1:

from math import *
print(sqrt(16)) # prints the square root of the value 16 in the form of a floating-point value
print(factorial(5)) # prints the factorial of the value 5
```

**Output:**
```text
4.0
120
```

```python
# Example 2:

import math

a=4.6
print(math.ceil(a))       # 5, rounding to the highest
print(math.floor(a))      # 4, rounding to the lowest
b=9
print(math.sqrt(b))       # 3.0, square root
print(math.exp(3.0))      # 20.085536923187668
print(math.log(2.0))      # 0.6931471805599453
print(math.pow(2.0,3.0))  # 8.0, exponential function
print(math.sin(0))        # 0.0
print(math.cos(0))        # 1.0
print (math.tan(45))      # 1.6197751905438615
print(math.log10(100))    # 2.0, logarithm with 10 as base
```

**Output:**
```text
5
4
3.0
20.085536923187668
0.6931471805599453
8.0
0.0
1.0
1.6197751905438615
2.0
```

#### Constants  -  

The math module provides two constants for mathematical Operations:

* **`math.pi`** : Returns constant Pi = 3.14159...
* **`math.e`** : Returns constant e= 2.71828...

```python
# Example 3:

import math 

print("math.pi : ",math.pi)  # 3.141592653589793, pi constant
print("math.e : ",math.e)    # 2.718281828459045, e  constant
```

**Output:**
```text
math.pi :  3.141592653589793
math.e :  2.718281828459045
```

### Example Using `statistics` Module

The statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which are defined in this module: **`mean`**, **`median`**, **`mode`**, **`stdev`** etc.

```python
# Example 1:

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

**Output:**
```text
21.09090909090909
22
20
6.106628291529549
```

### Wrap up

Since Python provides a lot of built-in modules, it is advisable to use built-in modules rather than user-created modules to perform basic operations.

## 💻 Exercises ➞ <span class='label label-default'>Module</span>

### Exercises ➞ <span class='label label-default'>Level 1</span>

1. Writ a function which generates a six digit/character **`random_user_id`**.
    - ```py
     print(random_user_id());
     '1ee33d'
    ```
2. Modify the previous task. Declare a function named **`user_id_gen_by_user`**. It doesn’t take any parameters but it takes two inputs using **`input()`**. One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
   
    - ```py
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
    ``` 
 
    - ```py
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
    ```

3. Write a function named **`rgb_color_gen`**. It will generate rgb colors (3 values ranging from 0 to 255 each).
   
    - ```py
print(rgb_color_gen()) 
#rgb(125,244,255) - the output should be in this form
    ```
 
### Exercises ➞ <span class='label label-default'>Level 2</span>

1. Write a function **`list_of_hexa_colors`** which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after **`#`**. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
2. Write a function **`list_of_rgb_colors`** which returns any number of RGB colors in an array.
3. Write a function **`generate_colors`** which can generate any number of hexa or rgb colors.

    - ```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
    ```
   
### Exercises ➞ <span class='label label-default'>Level 3</span>

1. Call your function **`shuffle_list`**, it takes a list as a parameter and it returns a shuffled list
2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

---

## 📘 Python Callable()
*Source: `4. Python Functions/8. Python callable().ipynb`*

# Python `callable()`

The **`callable()`** method returns **`True`** if the object passed appears callable. If not, it returns **`False`**.

**Syntax**:

```python
callable(object)
```

## `callable()` Parameters

**`callable()`** method takes a single argument **`object`**.

## Return Value from `callable()`

**`callable()`** method returns:

* **`True`** - if the object appears callable
* **`False`** - if the object is not callable.

It important to remember that, even if **`callable()`** is **`True`**, call to the object may still fail.

However, if **`callable()`** returns **`False`**, call to the object will certainly fail.

```python
# Example 1: How callable() works?

x = 5
print(callable(x))

def testFunction():
    print("Test")

y = testFunction
print(callable(y))
```

**Output:**
```text
False
True
```

Here, the object **`x`** is not callable. And, the object **`y`** appears to be callable (but may not be callable).

```python
# Example 2: Callable Object 

class Foo:
    def __call__(self):
        print('Print Something')

print(callable(Foo))
```

**Output:**
```text
True
```

The instance of **`Foo`** class appears to be callable (and is callable in this case).

```python
class Foo:
    def __call__(self):
        print('Print Something')

InstanceOfFoo = Foo()

# Prints 'Print Something'
InstanceOfFoo()
```

**Output:**
```text
Print Something
```

```python
# Example 3: Object Appears to be Callable but isn't callable.

class Foo:
    def printLine(self):
        print('Print Something')

print(callable(Foo))
```

**Output:**
```text
True
```

The instance of **`Foo`** class appears to be callable but it's not callable. The following code will raise an error.

```python
class Foo:
    def printLine(self):
        print('Print Something')

print(callable(Foo))

InstanceOfFoo = Foo()
# Raises an Error
# 'Foo' object is not callable
InstanceOfFoo()
```

**Output:**
```text
True
```

---

## 📘 Python Function Random Module
*Source: `4. Python Functions/8. Python Function random Module.ipynb`*

# Python Random Module

You can generate random numbers in Python by using random module.

Python offers **`random`** module that can generate random numbers.

These are pseudo-random number as the sequence of number generated depends on the seed.

If the seeding value is same, the sequence will be the same. For example, if you use 2 as the seeding value, you will always see the following sequence.

```python
import random
random.seed(2)

print(random.random())
print(random.random())
print(random.random())
```

**Output:**
```text
0.9560342718892494
0.9478274870593494
0.05655136772680869
```

**Not so random eh?** Since this generator is completely deterministic, it must not be used for encryption purpose.

Here is the list of all the functions defined in random module with a brief explanation of what they do.

**List of Functions in Python Random Module**

| Function | Description |
|:----| :--- |
| **`seed(a=None, version=2)`** | Initialize the random number generator | 
| **`getstate()`** | Returns an object capturing the current internal state of the generator | 
| **`setstate(state)`** | Restores the internal state of the generator | 
| **`getrandbits(k)`** | Returns a Python integer with k random bits | 
| **`randrange(start, stop[, step])`** | Returns a random integer from the range | 
| **`randint(a, b)`** | Returns a random integer between a and b inclusive | 
| **`choice(seq)`** | Return a random element from the non-empty sequence | 
| **`shuffle(seq)`** | Shuffle the sequence | 
| **`sample(population, k)`** | Return a k length list of unique elements chosen from the population sequence | 
| **`random()`** | Return the next random floating point number in the range [0.0, 1.0] | 
| **`uniform(a, b)`** | Return a random floating point number between a and b inclusive | 
| **`triangular(low, high, mode)`** | Return a random floating point number between low and high, with the specified mode between those bounds | 
| **`betavariate(alpha, beta)`** | Beta distribution | 
| **`expovariate(lambd)`** | Exponential distribution | 
| **`gammavariate(alpha, beta)`** | Gamma distribution | 
| **`gauss(mu, sigma)`** | Gaussian distribution | 
| **`lognormvariate(mu, sigma)`** | Log normal distribution | 
| **`normalvariate(mu, sigma)`** | Normal distribution | 
| **`vonmisesvariate(mu, kappa)`** | Vonmises distribution | 
| **`paretovariate(alpha)`** | Pareto distribution | 
| **`weibullvariate(alpha, beta)`** | Weibull distribution |

Visit this page to learn more on **[how you can generate pseudo-random numbers in Python](https://docs.python.org/3/library/random.html)**.

---

## 📘 Python Bytes()
*Source: `4. Python Functions/9. Python bytes().ipynb`*

# Python `bytes()`

The **`bytes()`** method returns a immutable bytes object initialized with the given size and data.

**Syntax**:

```python
bytes([source[, encoding[, errors]]])
```

**`bytes()`** method returns a bytes object which is an immutable (cannot be modified) sequence of integers in the range **`0 <=x < 256`**.

If you want to use the mutable version, use **bytearray()** method.

## `bytes()` Parameters

**`bytes()`** method takes three optional parameters:

* **source (Optional)** - source to initialize the array of bytes.
* **encoding (Optional)** - if the source is a string, the encoding of the string.
* **errors (Optional)** - if the source is a string, the action to take when the encoding conversion fails.

The **source** parameter can be used to initialize the byte array in the following ways:

**Different source parameters**:

| Type | Description |
|:----| :--- |
| **String** | **Converts the string to bytes using `str.encode()` Must also provide encoding and optionally errors** |
| **Integer** | **Creates an array of provided size, all initialized to null** |
| **Object** | **A read-only buffer of the object will be used to initialize the byte array** |
| **Iterable** | **Creates an array of size equal to the iterable count and initialized to the iterable elements Must be iterable of integers between `0 <= x < 256`** |
| **No source (arguments)** | **Creates an array of size `0`**. |

## Return Value from `bytes()`

**`bytes()`** method returns a bytes object of the given size and initialization values.

```python
# Example 1: Convert string to bytes
string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)
```

**Output:**
```text
b'Python is interesting.'
```

```python
# Example 2: Create a byte of given integer size
size = 5

arr = bytes(size)
print(arr)
```

**Output:**
```text
b'\x00\x00\x00\x00\x00'
```

```python
# Example 3: Convert iterable list to bytes
rList = [1, 2, 3, 4, 5]

arr = bytes(rList)
print(arr)
```

**Output:**
```text
b'\x01\x02\x03\x04\x05'
```

---

## 📘 Python Function Math Module.Ipynb
*Source: `4. Python Functions/9. Python Function math Module.ipynb.ipynb`*

# Python Mathematical Functions

Learn about all the mathematical functions available in Python and how you can use them in your program.

## What is `math` module in Python?

The **`math`** **module** is a standard module in Python and is always available. To use mathematical functions under this module, you have to import the module using **`import math`**.

It gives access to the underlying C library functions. For example:

```python
# Square root calculation

import math
math.sqrt(4)
```

**Output:**
```text
2.0
```

This module does not support complex datatypes. The **[cmath module](https://docs.python.org/3.0/library/cmath.html)** is the **`complex`** counterpart.

## Functions in Python Math Module

Here is the list of all the functions and attributes defined in **`math`** module with a brief explanation of what they do.

**List of Functions in Python Math Module**

| Function | Description |
|:----| :--- |
| **`ceil(x)`** | Returns the smallest integer greater than or equal to x. | 
| **`copysign(x, y)`** | Returns x with the sign of y | 
| **`fabs(x)`** | Returns the absolute value of x | 
| **`factorial(x)`** | Returns the factorial of x | 
| **`floor(x)`** | Returns the largest integer less than or equal to x | 
| **`fmod(x, y)`** | Returns the remainder when x is divided by y | 
| **`frexp(x)`** | Returns the mantissa and exponent of x as the pair (m, e) | 
| **`fsum(iterable)`** | Returns an accurate floating point sum of values in the iterable | 
| **`isfinite(x)`** | Returns True if x is neither an infinity nor a NaN (Not a Number) | 
| **`isinf(x)`** | Returns True if x is a positive or negative infinity | 
| **`isnan(x)`** | Returns True if x is a NaN | 
| **`ldexp(x, i)`** | Returns x * (2**i) | 
| **`modf(x)`** | Returns the fractional and integer parts of x | 
| **`trunc(x)`** | Returns the truncated integer value of x | 
| **`exp(x)`** | Returns e**x | 
| **`expm1(x)`** | Returns e**x - 1 | 
| **`log(x[, b])`** | Returns the logarithm of **`x`** to the base **`b`** (defaults to e) | 
| **`log1p(x)`** | Returns the natural logarithm of 1+x | 
| **`log2(x)`** | Returns the base-2 logarithm of x | 
| **`log10(x)`** | Returns the base-10 logarithm of x | 
| **`pow(x, y)`** | Returns x raised to the power y | 
| **`sqrt(x)`** | Returns the square root of x | 
| **`acos(x)`** | Returns the arc cosine of x | 
| **`asin(x)`** | Returns the arc sine of x | 
| **`atan(x)`** | Returns the arc tangent of x | 
| **`atan2(y, x)`** | Returns atan(y / x) | 
| **`cos(x)`** | Returns the cosine of x | 
| **`hypot(x, y)`** | Returns the Euclidean norm, sqrt(x*x + y*y) | 
| **`sin(x)`** | Returns the sine of x | 
| **`tan(x)`** | Returns the tangent of x | 
| **`degrees(x)`** | Converts angle x from radians to degrees | 
| **`radians(x)`** | Converts angle x from degrees to radians | 
| **`acosh(x)`** | Returns the inverse hyperbolic cosine of x | 
| **`asinh(x)`** | Returns the inverse hyperbolic sine of x | 
| **`atanh(x)`** | Returns the inverse hyperbolic tangent of x | 
| **`cosh(x)`** | Returns the hyperbolic cosine of x | 
| **`sinh(x)`** | Returns the hyperbolic cosine of x | 
| **`tanh(x)`** | Returns the hyperbolic tangent of x | 
| **`erf(x)`** | Returns the error function at x | 
| **`erfc(x)`** | Returns the complementary error function at x | 
| **`gamma(x)`** | Returns the Gamma function at x | 
| **`lgamma(x)`** | Returns the natural logarithm of the absolute value of the Gamma function at x | 
| **`pi`** | Mathematical constant, the ratio of circumference of a circle to it's diameter (3.14159...) | 
| **`e`** | mathematical constant e (2.71828...) |

Visit this page to learn about all the **[mathematical functions defined in Python 3](https://docs.python.org/3/library/math.html)**.

---

## 📘 Python Chr()
*Source: `4. Python Functions/10. Python chr().ipynb`*

# Python `chr()`

The **`chr()`** method returns a character (a string) from an integer (represents unicode code point of the character).

**Syntax**:

```python
chr(i)
```

## `chr()` Parameters

**`chr()`** method takes a single parameter, an integer **`i`**.

The valid range of the integer is from 0 through 1,114,111.

## Return Value from `chr()`

**`chr()`** returns:

* a character (a string) whose Unicode code point is the integer **`i`**

If the integer **`i`** is outside the range, **`ValueError`** will be raised.

```python
# Example 1: How chr() works?

print(chr(97))
print(chr(65))
print(chr(1200))
```

**Output:**
```text
a
A
Ұ
```

```python
# Example 2: Integer passed to chr() is out of the range
print(chr(-1))
```

**Explanation**:

When you run the program, **`ValueError`** is raised.

It's because the argument passed to **`chr()`** method is out of the range.

The reverse operation of **`chr()`** function can be performed by **`ord()`** function.

---

## 📘 Python Function Package
*Source: `4. Python Functions/10. Python Function Package.ipynb`*

# Python Package

In this class, you'll learn to divide your code base into clean, efficient modules using Python packages. Also, you'll learn to import and use your own or third party packagesin your Python program.

## What are packages?

We don't usually store all of our files on our computer in the same location. We use a well-organized hierarchy of directories for easier access.

Similar files are kept in the same directory, for example, we may keep all the songs in the "**music**" directory. Analogous to this, Python has packages for directories and **modules** for files.

As our application program grows larger in size with a lot of modules, we place similar modules in one package and different modules in different packages. This makes a project (program) easy to manage and conceptually clear.

Similarly, as a directory can contain subdirectories and files, a Python package can have sub-packages and modules.

A directory must contain a file named **`__init__.py`** in order for Python to consider it as a package. This file can be left empty but we generally place the initialization code for that package in this file.

Here is an example. Suppose we are developing a game. One possible organization of packages and modules could be as shown in the figure below.

|  | 
|:--:| 
| **Package Module Structure in Python Programming** |

## Importing module from a package

We can import modules from packages using the dot **`.`** operator.

For example, if we want to import the **`start`** module in the above example, it can be done as follows:

```python
>>>import Game.Level.start
```

Now, if this module contains a **function** named **`select_difficulty()`**, we must use the full name to reference it.

```python
>>>Game.Level.start.select_difficulty(2)
```

If this construct seems lengthy, we can import the module without the package prefix as follows:

```python
>>>from Game.Level import start
```

We can now call the function simply as follows:

```python
>>>start.select_difficulty(2)
```

Another way of importing just the required function (or class or variable) from a module within a package would be as follows:

```python
>>>from Game.Level.start import select_difficulty
```

Now we can directly call this function.

```python
>>>select_difficulty(2)
```

Although easier, this method is not recommended. Using the full **namespace** avoids confusion and prevents two same identifier names from colliding.

While importing packages, Python looks in the list of directories defined in **`sys.path`**, similar as for **module search path**.

---

## 📘 Python Compile()
*Source: `4. Python Functions/11. Python compile().ipynb`*

# Python `compile()`

The **`compile()`** method returns a Python code object from the source (normal string, a byte string, or an AST object).

**Syntax**:

```python
compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
```

**`compile()`** method is used if the Python code is in string form or is an AST object, and you want to change it to a code object.

The code object returned by **`compile()`** method can later be called using methods like: **exec()** and **eval()** which will execute dynamically generated Python code.

## `compile()` Parameters

* **`source`** - a normal string, a byte string, or an AST object
* **`filename`** - file from which the code was read. If it wasn't read from a file, you can give a name yourself
* **`mode`** - Either **`eval`** or **`exec`** or **`single`**.
    * **`eval`** - accepts only a single expression.
    * **`exec`** - It can take a code block that has Python statements, class and functions, and so on.
    * **`single`** - if it consists of a single interactive statement
* **`flags`** (optional) and **`dont_inherit`** (optional) - controls which future statements affect the * compilation of the source. Default Value: 0
* **`optimize`** (optional) - optimization level of the compiler. Default value -1.

## Return Value from `compile()`

**`compile()`** method returns a Python code object.

```python
# Example 1: How compile() works?

codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')

exec(codeObejct)
```

**Output:**
```text
sum = 11
```

**Explanation**:

Here, **`source`** is in normal string form. The **`filename`** is sumstring. And, the **`exec`** mode later allows the use of **`exec()`** method.

**`compile()`** method converts the string to Python code object. The code object is then executed using **`exec()`** method.

---

## 📘 Python Classmethod()
*Source: `4. Python Functions/12. Python classmethod().ipynb`*

# Python `classmethod()`

The **`classmethod()`** method returns a class method for the given function.

**Syntax**:

```python
classmethod(function)
```

**`classmethod()`** is considered un-Pythonic so in newer Python versions, you can use the **`@classmethod`** decorator for classmethod definition.

**Syntax**:

```python
@classmethod
def func(cls, args...)
```

## `classmethod()` Parameters

**`classmethod()`** method takes a single parameter:

* **function** - Function that needs to be converted into a class method

## Return Value from `classmethod()`

**`classmethod()`** method returns a class method for the given function.

## What is a class method?

A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like **staticmethod()**.

The difference between a static method and a class method is:

* Static method knows nothing about the class and just deals with the parameters
* Class method works with the class since its parameter is always the class itself.
The class method can be called both by the class and its object.

```python
Class.classmethod()
Or even
Class().classmethod()
```

But no matter what, the class method is always attached to a class with the first argument as the class itself **`cls`**.

```python
def classMethod(cls, args...)
```

```python
# Example 1: Create class method using classmethod()

class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method
Person.printAge = classmethod(Person.printAge)

Person.printAge()
```

**Output:**
```text
The age is: 25
```

**Explanation**:

Here, we have a class **`Person`**, with a member variable **`age`** assigned to 25.

We also have a function **`printAge`** that takes a single parameter **`cls`** and not **`self`** we usually take.

**`cls`** accepts the class **`Person`** as a parameter rather than Person's object/instance.

Now, we pass the method **`Person.printAge`** as an argument to the function **`classmethod`**. This converts the method to a class method so that it accepts the first parameter as a class (i.e. Person).

In the final line, we call **`printAge`** without creating a Person object like we do for static methods. This prints the class variable **`age`**.

## When do you use class method?

### 1. **Factory methods**

Factory methods are those methods that return a class object (like constructor) for different use cases.

It is similar to function overloading in C++. Since, Python doesn't have anything as such, class methods and static methods are used.

```python
# Example 2: Create factory method using class method

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()
```

**Output:**
```text
Adam's age is: 19
John's age is: 36
```

**Explanation**:

Here, we have two class instance creator, a constructor and a **`fromBirthYear`** method.

The constructor takes normal parameters **`name`** and **`age`**. While, **`fromBirthYear`** takes **`class`**, **`name`** and **`birthYear`**, calculates the current age by subtracting it with the current year and returns the class instance.

The fromBirthYear method takes Person class (not Person object) as the first parameter **`cls`** and returns the constructor by calling **`cls(name, date.today().year - birthYear)`**, which is equivalent to **`Person(name, date.today().year - birthYear)`**

Before the method, we see **`@classmethod`**. This is called a **decorator** for converting **`fromBirthYear`** to a class method as **`classmethod()`**.

### 2. Correct instance creation in inheritance

Whenever you derive a class from implementing a factory method as a class method, it ensures correct instance creation of the derived class.

You can create a static method for the above example but the object it creates, will always be hardcoded as Base class.

But, when you use a class method, it creates the correct instance of the derived class.

```python
# Example 3: How the class method works for the inheritance?

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))
```

**Output:**
```text
True
False
```

**Explanation**:

Here, using a static method to create a class instance wants us to hardcode the instance type during creation.

This clearly causes a problem when inheriting **`Person`** to **`Man`**.

**`fromFathersAge`** method doesn't return a **`Man`** object but its base class **`Person`**'s object.

This violates OOP paradigm. Using a class method as **`fromBirthYear`** can ensure the OOP-ness of the code since it takes the first parameter as the class itself and calls its factory method.

---

## 📘 Python Complex()
*Source: `4. Python Functions/13. Python complex().ipynb`*

# Python `complex()`

The **`complex()`** method returns a complex number when real and imaginary parts are provided, or it converts a string to a complex number.

**Syntax**:

```python
complex([real[, imag]])
```

## `complex()` Parameters

In general, **`complex()`** method takes two parameters:

* **real** - real part. If **`real`** is omitted, it defaults to 0.
* **imag** - imaginary part. If **`imag`** is omitted, it defaults to 0.

If the first parameter passed to this method is a string, it will be interpreted as a complex number. In this case, the second parameter shouldn't be passed.

## Return Value from `complex()`

As suggested by the name, **`complex()`** method returns a complex number.

If the string passed to this method is not a valid complex number, **`ValueError`** exception is raised.

> **Note**: The string passed to **`complex()`** should be in the form **`real+imagj`** or **`real+imagJ`**

```python
# Example 1: How to create a complex number in Python?

z = complex(2, -3)
print(z)

z = complex(1)
print(z)

z = complex()
print(z)

z = complex('5-9j')
print(z)
```

**Output:**
```text
(2-3j)
(1+0j)
0j
(5-9j)
```

```python
# Example 2: Create complex Number Without Using complex()

# It's possible to create a complex number without using `complex()` method. 
# For that, you have to put 'j' or 'J' after a number.

a = 2+3j
print('a =',a)
print('Type of a is',type(a))

b = -2j
print('b =',b)
print('Type of b is',type(a))

c = 0j
print('c =',c)
print('Type of c is',type(c))
```

**Output:**
```text
a = (2+3j)
Type of a is <class 'complex'>
b = (-0-2j)
Type of b is <class 'complex'>
c = 0j
Type of c is <class 'complex'>
```

---

## 📘 Python Delattr()
*Source: `4. Python Functions/14. Python delattr().ipynb`*

# Python `delattr()`

The **`delattr()`** deletes an attribute from the object (if the object allows it).

**Syntax**:

```python
delattr(object, name)
```

## `delattr()` Parameters

**`delattr()`** takes two parameters:

* **object** - the object from which **`name`** attribute is to be removed
* **name** - a string which must be the name of the attribute to be removed from the **`object`**

## Return Value from `delattr()`

**`delattr()`** doesn't return any value (returns **`None`**). It only removes an attribute (if the object allows it).

```python
# Example 1: How delattr() works?

class Coordinate:
    x = 10
    y = -5
    z = 0

point1 = Coordinate() 

print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)

delattr(Coordinate, 'z')

print('--After deleting z attribute--')
print('x = ',point1.x)
print('y = ',point1.y)

# Raises Error
print('z = ',point1.z)
```

**Output:**
```text
x =  10
y =  -5
z =  0
--After deleting z attribute--
x =  10
y =  -5
```

**Explanation**:

Here, attribute **`z`** is removed from the **`Coordinate`** class using **`delattr(Coordinate, 'z')`**.

```python
# Example 2: Deleting Attribute Using del Operator

# You can also delete attribute of an object using del operator.

class Coordinate:
    x = 10
    y = -5
    z = 0

point1 = Coordinate() 

print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)

# Deleting attribute z
del Coordinate.z

print('--After deleting z attribute--')
print('x = ',point1.x)
print('y = ',point1.y)

# Raises Attribute Error
print('z = ',point1.z)
```

**Output:**
```text
x =  10
y =  -5
z =  0
--After deleting z attribute--
x =  10
y =  -5
```

The output of the program will be the same as above.

---

## 📘 Python Dict()
*Source: `4. Python Functions/15. Python dict().ipynb`*

# Python `dict()`

The **`dict()`** constructor creates a dictionary in Python.

Different forms of **`dict()`** constructors are:

```python
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
```

> **Note**: <b>`**kwarg`</b> let you take an arbitrary number of keyword arguments.

A keyword argument is an argument preceded by an identifier (eg. **`name=`**). Hence, the keyword argument of the form **`kwarg=value`** is passed to **`dict()`** constructor to create dictionaries.

**`dict()`** doesn't return any value (returns **`None`**).

```python
# Example 1: Create Dictionary Using keyword arguments only

numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))

empty = dict()
print('empty =', empty)
print(type(empty))
```

**Output:**
```text
numbers = {'x': 5, 'y': 0}
<class 'dict'>
empty = {}
<class 'dict'>
```

```python
# Example 2: Create Dictionary Using Iterable

# keyword argument is not passed
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)

# keyword argument is also passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)

# zip() creates an iterable in Python 3
numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers3 =',numbers3)
```

**Output:**
```text
numbers1 = {'x': 5, 'y': -5}
numbers2 = {'x': 5, 'y': -5, 'z': 8}
numbers3 = {'x': 1, 'y': 2, 'z': 3}
```

```python
# Example 3: Create Dictionary Using Mapping

numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =',numbers1)

# you don't need to use dict() in above code
numbers2 = {'x': 4, 'y': 5}
print('numbers2 =',numbers2)

# keyword argument is also passed
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)
```

**Output:**
```text
numbers1 = {'x': 4, 'y': 5}
numbers2 = {'x': 4, 'y': 5}
numbers3 = {'x': 4, 'y': 5, 'z': 8}
```

---

## 📘 Python Dir()
*Source: `4. Python Functions/16. Python dir().ipynb`*

# Python `dir()`

The **`dir()`** method tries to return a list of valid attributes of the object.

**Syntax**:

```python
dir([object])
```

## `dir()` Parameters

**`dir()`** takes maximum of one object.

* **object** (optional) - **`dir()`** attempts to return all attributes of this object.

## Return Value from `dir()`

**`dir()`** tries to return a list of valid attributes of the object.

* If the object has **`__dir__()`** method, the method will be called and must return the list of attributes.
* If the object doesn't have **`__dir__()`** method, this method tries to find information from the **`__dict__`** attribute (if defined), and from type object. In this case, the list returned from **`dir()`** may not be complete.

If an object is not passed to **`dir()`** method, it returns the list of names in the current local scope.

```python
# Example 1: How dir() works?

number = [1, 2, 3]
print(dir(number))

print('\nReturn Value from empty dir()')
print(dir())
```

**Output:**
```text
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Return Value from empty dir()
['In', 'NamespaceMagics', 'Out', '_', '_Jupyter', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_getshapeof', '_getsizeof', '_i', '_i1', '_ih', '_ii', '_iii', '_nms', '_oh', 'exit', 'get_ipython', 'getsizeof', 'json', 'np', 'number', 'quit', 'var_dic_list']
```

```python
# Example 2: dir() on User-defined Object

class Person:
    def __dir__(self):
        return ['age', 'name', 'salary']
    

teacher = Person()
print(dir(teacher))
```

**Output:**
```text
['age', 'name', 'salary']
```

---

## 📘 Python Divmod()
*Source: `4. Python Functions/17. Python divmod().ipynb`*

# Python `divmod()`

The **`divmod()`** method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.

**Syntax**:

```python
divmod(x, y)
```

## `divmod()` Parameters

**`divmod()`** takes two parameters:

* **x** - a non-complex number (numerator)
* **y** - a non-complex number (denominator)

## Return Value from `divmod()`

**`divmod()`** returns

* **`(q, r)`** - a pair of numbers (a **[tuple](https://github.com/milaan9/02_Python_Datatypes/blob/main/004_Python_Tuple.ipynb)**) consisting of quotient **`q`** and remainder **`r`**

If **`x`** and **`y`** are integers, the return value from **`divmod()`** is same as **`(a // b, x % y)`**.

If either **`x`** or **`y`** is a float, the result is **`(q, x%y)`**. Here, **`q`** is the whole part of the quotient.

```python
# Example 1: How divmod() works in Python?

print('divmod(8, 3) = ', divmod(8, 3))
print('divmod(3, 8) = ', divmod(3, 8))
print('divmod(5, 5) = ', divmod(5, 5))

# divmod() with Floats
print('divmod(8.0, 3) = ', divmod(8.0, 3))
print('divmod(3, 8.0) = ', divmod(3, 8.0))
print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5))
print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))
```

**Output:**
```text
divmod(8, 3) =  (2, 2)
divmod(3, 8) =  (0, 3)
divmod(5, 5) =  (1, 0)
divmod(8.0, 3) =  (2.0, 2.0)
divmod(3, 8.0) =  (0.0, 3.0)
divmod(7.5, 2.5) =  (3.0, 0.0)
divmod(2.6, 0.5) =  (5.0, 0.10000000000000009)
```

---

## 📘 Python Enumerate()
*Source: `4. Python Functions/18. Python enumerate().ipynb`*

# Python `enumerate()`

The **`enumerate()`** method adds counter to an iterable and returns it (the enumerate object).

**Syntax**:

```python
enumerate(iterable, start=0)
```

## `enumerate()` Parameters

**`enumerate()`** takes two parameters:

* **iterable** - a sequence, an iterator, or objects that supports iteration
* **start** (optional) - **`enumerate()`** starts counting from this number. If **`start`** is omitted, **`0`** is taken as **`start`**.

## Return Value from `enumerate()`

**`enumerate()`** method adds counter to an iterable and returns it. The returned object is a enumerate object.

You can convert enumerate objects to list and tuple using **list()** and **tuple()** method respectively.

```python
# Example 1: How enumerate() works in Python?

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
```

```python
# Example 2: Looping Over an Enumerate object

grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
    print(item)

print('\n')
for count, item in enumerate(grocery):
    print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
    print(count, item)
```

**Output:**
```text
(0, 'bread')
(1, 'milk')
(2, 'butter')


0 bread
1 milk
2 butter


100 bread
101 milk
102 butter
```

---

## 📘 Python Staticmethod()
*Source: `4. Python Functions/19. Python staticmethod().ipynb`*

# Python `staticmethod()`

The **`staticmethod()`** built-in function returns a static method for a given function.

**Syntax**:

```python
staticmethod(function)
```

Using **`staticmethod()`** is considered a un-Pythonic way of creating a static function.

Hence, in newer versions of Python, you can use the **`@staticmethod`** decorator.

The syntax of **`@staticmethod`** is:

**Syntax**:

```python
@staticmethod
def func(args, ...)
```

## `staticmethod()` Parameters

The **`staticmethod()`** method takes a single parameter:

* **function** - function that needs to be converted to a static method

## Return Value from `staticmethod()`

The **`staticmethod()`** returns a static method for a function passed as the parameter.

## What is a static method?

Static methods, much like **class methods**, are methods that are bound to a class rather than its object.

They do not require a class instance creation. So, they are not dependent on the state of the object.

The difference between a static method and a class method is:

* Static method knows nothing about the class and just deals with the parameters.
* Class method works with the class since its parameter is always the class itself.

They can be called both by the class and its object.

```python
Class.staticmethodFunc()
or even
Class().staticmethodFunc()
```

```python
# Example 1: Create a static method using staticmethod()

class Mathematics:

    def addNumbers(x, y):
        return x + y

# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))
```

**Output:**
```text
The sum is: 15
```

## When do you use static methods?

### 1. Grouping utility function to a class

Static methods have a limited use case because, like class methods or any other methods within a class, they cannot access the properties of the class itself.

However, when you need a utility function that doesn't access any properties of a class but makes sense that it belongs to the class, we use static functions.

```python
# Example 2: Create a utility function as a static method

class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if(date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")
```

**Output:**
```text
Equal
```

Here, we have a **`Dates`** class that only works with dates with dashes. However, in our previous database, all dates were present in slashes.

In order to convert the slash-dates to dash-dates, we have created a utility function **`toDashDate`** within **`Dates`**.

It is a static method because it doesn't need to access any properties of Dates itself and only requires the parameters.

We can also create **`toDashDate`** outside the class, but since it works only for dates, it's logical to keep it inside the **`Dates`** class.

### 2. Having a single implementation

Static methods are used when we don't want subclasses of a class change/override a specific implementation of a method.

```python
# Example 3: How inheritance works with static method?

class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)

date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

if(date.getDate() == dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")
```

**Output:**
```text
Equal
```

**Explanation**:

Here, we wouldn't want the subclass **`DatesWithSlashes`** to override the static utility method **`toDashDate`** because it only has a single use, i.e. change date to dash-dates.

We could easily use the static method to our advantage by overriding **`getDate()`** method in the subclass so that it works well with the **`DatesWithSlashes`** class.

---

## 📘 Python Filter()
*Source: `4. Python Functions/20. Python filter().ipynb`*

# Python `filter()`

The **`filter()`** constructs an iterator from elements of an iterable for which a function returns true.

In simple words, **`filter()`** method filters the given iterable with the help of a function that tests each element in the iterable to be true or not.

**Syntax**:

```python
filter(function, iterable)
```

## `filter()` Parameters

The **`filter()`** method takes two parameters:

* **function** - function that tests if elements of an iterable return true or false
    * If None, the function defaults to Identity function - which returns false if any elements are false

* **iterable** - iterable which is to be filtered, could be **sets**, **lists**, **tuples**, or containers of any iterators

## Return Value from `filter()`

**`filter()`** method returns an iterator that passed the function check for each element in the iterable.

**`filter()`** method is equivalent to:

```python
# when function is defined
(element for element in iterable if function(element))

# when function is None
(element for element in iterable if element)
```

```python
# Example 1: How filter() works for iterable list?

# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, letters)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)
```

**Output:**
```text
The filtered vowels are:
a
e
i
o
```

**Explanation**:

Here, we have a list of letters and need to filter out only the vowels in it.

We could use a for loop to loop through each element in **`letters`** list and store it in another list, but in Python, this process is easier and faster using **`filter()`** method.

We have a function **`filterVowels`** that checks if a letter is a vowel or not. This function is passed onto **`filter()`** method with the list of letters.

**`filter()`** method then passes each letter to the **`filterVowels`** method to check if it returns true or not. In the end, it creates an iterator of the ones that return true (vowels).

Since the iterator doesn't store the values itself, we loop through it and print out vowels one by one.

```python
# Example 2: How filter() method works without the filter function?

# random list
randomList = [1, 'a', 0, False, True, '0']

filteredList = filter(None, randomList)

print('The filtered elements are:')
for element in filteredList:
    print(element)
```

**Output:**
```text
The filtered elements are:
1
a
True
0
```

**Explanation**:

Here, we have a random list of numbers, string, and boolean in **`randomList`**.

We pass **`randomList`** to the **`filter()`** method with first parameter (filter function) as **`None`**.

With filter function as None, the function defaults to Identity function, and each element in **`randomList`** is checked if it's true or not.

When we loop through the final **`filteredList`**, we get the elements which are true: **`1, a, True and '0'`** ('0' as a string is also true).

---

## 📘 Python Eval()
*Source: `4. Python Functions/21. Python eval().ipynb`*

# Python `eval()`

The **`eval()`** method parses the expression passed to this method and runs python expression (code) within the program.

In simple terms, the **`eval()`** function runs the python code (which is passed as an argument) within the program.

**Syntax**:

```python
eval(expression, globals=None, locals=None)
```

## `eval()` Parameters

The **`filter()`** function takes three parameters:

* **expression** - the string parsed and evaluated as a Python expression
* **globals** (optional) - a dictionary
* **locals** (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.

The use of **`globals`** and **`locals`** will be discussed later in this article.

## Return Value from `eval()`

The **`eval()`** method returns the result evaluated from the **`expression`**.

```python
# Example 1: How eval() works in Python

x = 1
print(eval('x + 1'))
```

**Output:**
```text
2
```

**Explanation**:

Here, the **`eval()`** function evaluates the expression **`x + 1`** and **`print`** is used to display this value.

```python
# Example 2: Practical Example to Demonstrate Use of eval()

# Perimeter of Square
def calculatePerimeter(l):
    return 4*l

# Area of Square
def calculateArea(l):
    return l*l


expression = input("Type a function: ")

for l in range(1, 5):
    if (expression == 'calculatePerimeter(l)'):
        print("If length is ", l, ", Perimeter = ", eval(expression))
    elif (expression == 'calculateArea(l)'):
        print("If length is ", l, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break
        
'''
Output:
Type a function: calculateArea(l)
If length is  1 , Area =  1
If length is  2 , Area =  4
If length is  3 , Area =  9
If length is  4 , Area =  16
'''
```

**Output:**
```text
Type a function: calculateArea(l)
If length is  1 , Area =  1
If length is  2 , Area =  4
If length is  3 , Area =  9
If length is  4 , Area =  16
'\nOutput:\nType a function: calculateArea(l)\nIf length is  1 , Area =  1\nIf length is  2 , Area =  4\nIf length is  3 , Area =  9\nIf length is  4 , Area =  16\n'
```

## Warnings when using `eval()`

Consider a situation where you are using a Unix system (macOS, Linux etc) and you have imported the os module. The **`os`** module provides a portable way to use operating system functionalities like reading or writing to a file.

If you allow users to input a value using **`eval(input())`**, the user may issue commands to change file or even delete all the files using the command: **`os.system('rm -rf *')`**.

If you are using **`eval(input())`** in your code, it is a good idea to check which variables and methods the user can use. You can see which variables and methods are available using **dir() method**.

```python
from math import *
print(eval('dir()'))
```

**Output:**
```text
['In', 'NamespaceMagics', 'Out', '_', '_2', '_Jupyter', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_getshapeof', '_getsizeof', '_i', '_i1', '_i2', '_i3', '_ih', '_ii', '_iii', '_nms', '_oh', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'calculateArea', 'calculatePerimeter', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exit', 'exp', 'expm1', 'expression', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'get_ipython', 'getsizeof', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'json', 'l', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'np', 'perm', 'pi', 'pow', 'prod', 'quit', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'var_dic_list', 'x']
```

## Restricting the Use of Available Methods and Variables in `eval()`

More often than not, all the available methods and variables used in the **`expression`** (first parameter to **`eval()`**) may not be needed, or even may have a security hole. You may need to restrict the use of these methods and variables for **`eval()`**. You can do so by passing optional **`globals`** and **`locals`** parameters (dictionaries) to the **`eval()`** function.

### 1. When both globals and locals parameters omitted

If both parameters are omitted (as in our earlier examples), the **`expression`** is executed in the current scope. You can check the available variables and methods using following code:

```python
print(eval('dir()'))
```

**Output:**
```text
['In', 'NamespaceMagics', 'Out', '_', '_2', '_Jupyter', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_getshapeof', '_getsizeof', '_i', '_i1', '_i2', '_i3', '_i4', '_ih', '_ii', '_iii', '_nms', '_oh', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'calculateArea', 'calculatePerimeter', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exit', 'exp', 'expm1', 'expression', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'get_ipython', 'getsizeof', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'json', 'l', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'np', 'perm', 'pi', 'pow', 'prod', 'quit', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'var_dic_list', 'x']
```

### 2. Passing globals parameter; locals parameter is omitted

The **`globals`** and **`locals`** parameters (dictionaries) are used for global and local variables respectively. If the **`locals`** dictionary is omitted, it defaults to **`globals`** dictionary. Meaning, **`globals`** will be used for both global and local variables.

> **Note**: You can check the current global and local dictionary in Python using **globals()** and **locals()** built-in methods respectively.

```python
# Example 3: Passing empty dictionary as globals parameter
    
from math import *
print(eval('dir()', {}))

# The code will raise an exception
print(eval('sqrt(25)', {}))
```

**Output:**
```text
['__builtins__']
```

**Explanation**:

If you pass an empty dictionary as **`globals`**, only the **`__builtins__`** are available to **`expression`** (first parameter to the **`eval()`**).

Even though we have imported the **`math`** module in the above program, **`expression`** can't access any functions provided by the **math module**.

```python
# Example 4: Making Certain Methods available

from math import *
print(eval('dir()', {'sqrt': sqrt, 'pow': pow}))
```

**Output:**
```text
['__builtins__', 'pow', 'sqrt']
```

**Explanation**:

Here, the expression can only use the **`sqrt()`** and the **`pow()`** methods along with **`__builtins__`**.

It is also possible to change the name of the method available for the **`expression`** as to your wish:

```python
from math import *
names = {'square_root': sqrt, 'power': pow}
print(eval('dir()', names))

# Using square_root in Expression
print(eval('square_root(9)', names))
```

**Output:**
```text
['__builtins__', 'power', 'square_root']
3.0
```

**Explanation**:

In the above program, **`square_root()`** calculates the square root using **`sqrt()`**. However, trying to use **`sqrt()`** directly will raise an error.

```python
# Example 5: Restricting the Use of built-ins
# You can restrict the use of __builtins__ in the expression as follows:

eval(expression, {'__builtins__': None})
```

### 3. Passing both globals and locals dictionary

You can make needed functions and variables available for use by passing the **`locals`** dictionary. For example:

```python
from math import *

a = 169
print(eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt}))
```

**Output:**
```text
13.0
```

**Explanation**:

In this program, **`expression`** can have **`sqrt()`** method and variable **`a`** only. All other methods and variables are unavailable.

Restricting the use of **`eval()`** by passing **`globals`** and **`locals`** dictionaries will make your code secure particularly when you are using input provided by the user to the **`eval()`** method.

> **Note**: Sometimes, **`eval()`** is not secure even with limited names. When an object and its methods are made accessible, almost anything can be done. The only secure way is by validating the user input.

---

## 📘 Python Float()
*Source: `4. Python Functions/22. Python float().ipynb`*

# Python `float()`

The **`float()`** method returns a floating point number from a number or a string.

**Syntax**:

```python
float([x])
```

## `float()` Parameters

The **`float()`** method takes a single parameter:

* **`x` (Optional)** - number or string that needs to be converted to floating point number
If it's a string, the string should contain decimal points

**Different parameters with **`float()`****:

| Parameter Type | Usage |
|:----| :--- |
| **Float number** | **Use as a floating number** |
| **Integer** | **Use as an integer** |
| **String** | **Must contain decimal numbers. Leading and trailing whitespaces are removed. Optional use of "`+`", "`-`" signs. Could contain `NaN`, `Infinity`, `inf` (lowercase or uppercase).** |

## Return Value from `float()`

**`float()`** method returns:

* Equivalent floating point number if an argument is passed
* 0.0 if no arguments passed
* **`OverflowError`** exception if the argument is outside the range of Python float

```python
# Example 1: How float() works in Python?

# for integers
print(float(10))

# for floats
print(float(11.22))

# for string floats
print(float("-13.33"))

# for string floats with whitespaces
print(float("     -24.45\n"))

# string float error
print(float("abc"))
```

**Output:**
```text
10.0
11.22
-13.33
-24.45
```

```python
# Example 2: float() for infinity and Nan(Not a number)?

# for NaN
print(float("nan"))
print(float("NaN"))

# for inf/infinity
print(float("inf"))
print(float("InF"))
print(float("InFiNiTy"))
print(float("infinity"))
```

**Output:**
```text
nan
nan
inf
inf
inf
inf
```

---

## 📘 Python Format()
*Source: `4. Python Functions/23. Python format().ipynb`*

# Python `format()`

The built-in **`format()`** method returns a formatted representation of the given value controlled by the format specifier.

The **`format()`** function is similar to the **String format** method. Internally, both methods call **`__format__()`** method of an object.

While the built-in **`format()`** function is a low level implementation for formatting an object using **`__format__()`** internally, string **`format()`** is a higher level implementation able to perform complex formatting operations on multiple object strings as well.

**Syntax**:

```python
format(value[, format_spec])
```

## `format()` Parameters

The **`format()`** function takes two parameters:

* **value** - value that needs to be formatted
* **format_spec** - The specification on how the value should be formatted.

The format specifier could be in the format:

**`[[fill]align][sign][#][0][width][,][.precision][type]`**

**where, the options are**

| Parameter Type | **`::=`** | Usage |
|:----| :--- | :--- |
| **fill** | **`::=`** | **any character** |
| **align** | **`::=`** | **"`<`" or "`>`" or "`=`" or "`^`"** |
| **sign** | **`::=`** | **"`+`" or "`-`" or "` `"** |
| **width** | **`::=`** | **integer** |
| **precision** | **`::=`** | **integer** |
| **type** | **`::=`** | **"`b`" or "`c`" or "`d`" or "`e`" or "`E`" or "`f`" or "`F`" or "`g`" or "`G`" or "`n`" or "`o`" or "`s`" or "`x`" or "`X`" or "`%`"** |

Visit these links to learn more about **format types** and **alignment**.

## Return Value from `format()`

The **`format()`** function returns a formatted representation of a given value specified by the format specifier.

```python
# Example 1: Number formatting with format()
# d, f and b are type

# integer
print(format(123, "d"))

# float arguments
print(format(123.4567898, "f"))

# binary format
print(format(12, "b"))
```

**Output:**
```text
123
123.456790
1100
```

```python
# Example 2: Number formatting with fill, align, sign, width, precision and type
# integer 

print(format(1234, "*>+7,d"))

# float number
print(format(123.4567, "^-09.3f"))
```

**Output:**
```text
*+1,234
0123.4570
```

**Explanation**:

Here, when formatting the integer **`1234`**, we've specified the formatting specifier **`*>+7,d`**. Let's understand each option:

* **`*`** - It is the fill character that fills up the empty spaces after formatting
* **`>`** - It is the right alignment option that aligns the output string to the right
* **`+`** - It is the sign option that forces the number to be signed (having a sign on its left)
* **`7`** - It is the width option that forces the number to take a minimum width of 7, other spaces will be filled by fill character
* **`,`** - It is the thousands operator that places a comma between all thousands.
* **`d`** - It is the type option that specifies the number is an integer.

When formatting the floating point number **`123.4567`**, we've specified the format specifier **`^-09.3f`**. These are:

* **`^`** - It is the center alignment option that aligns the output string to the center of the remaining space
* **`-`** - It is the sign option that forces only negative numbers to show the sign
* **`0`** - It is the character that is placed in place of the empty spaces.
* **`9`** - It is the width option that sets the minimum width of the number to 9 (including decimal point, thousands comma and sign)
* **`.3`** - It is the precision operator that sets the precision of the given floating number to 3 places
* **`f`** - It is the type option that specifies the number is a float.

```python
# Example 3: Using format() by overriding __format__()
# custom __format__() method

class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

print(format(Person(), "age"))
```

**Output:**
```text
23
```

**Explanation**:

Here, we have overridden the **`__format__()`** method of the class **`Person`**.

It now accepts a **`format`** parameter and returns 23 if it is equal to **`'age'`**. If no format is specified, **`None`** is returned.

The **`format()`** function internally runs **`Person().__format__("age")`** to return 23.

---

## 📘 Python Frozenset()
*Source: `4. Python Functions/24. Python frozenset().ipynb`*

# Python `frozenset()`

The **`frozenset()`** function returns an immutable frozenset object initialized with elements from the given iterable.
Frozen set is just an immutable version of a **Python set** object. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.

Due to this, frozen sets can be used as keys in **Dictionary** or as elements of another set. But like sets, it is not ordered (the elements can be set at any index).

**Syntax**:

```python
frozenset([iterable])
```

## `frozenset()` Parameters

The **`format()`** function takes a single parameter:

* **iterable (Optional)** - the iterable which contains elements to initialize the frozenset with.
    * Iterable can be set, dictionary, **tuple**, etc.

## Return Value from `frozenset()`

The **`frozenset()`** function returns an immutable **`frozenset`** initialized with elements from the given iterable.

If no parameters are passed, it returns an empty **`frozenset`**.

```python
# Example 1: Working of Python frozenset()

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())

# frozensets are immutable
fSet.add('v')
```

**Output:**
```text
The frozen set is: frozenset({'e', 'o', 'u', 'a', 'i'})
The empty frozen set is: frozenset()
```

```python
# Example 2: frozenset() for Dictionary

# When you use a dictionary as an iterable for a frozen set, 
# it only takes keys of the dictionary to create the set.

# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)
```

**Output:**
```text
The frozen set is: frozenset({'name', 'age', 'sex'})
```

## Frozenset operations

Like normal sets, frozenset can also perform different operations like **`copy()`**, **`union()`**, **`intersection()`**, **`difference()`**, and **`symmetric_difference()`**.

```python
# Example 1: Frozensets

# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()               # Output: frozenset({1, 2, 3, 4})
print(C)

# union
print(A.union(B))          # Output: frozenset({1, 2, 3, 4, 5, 6})

# intersection
print(A.intersection(B))   # Output: frozenset({3, 4})

# difference
print(A.difference(B))     # Output: frozenset({1, 2})

# symmetric_difference
print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})
```

**Output:**
```text
frozenset({1, 2, 3, 4})
frozenset({1, 2, 3, 4, 5, 6})
frozenset({3, 4})
frozenset({1, 2})
frozenset({1, 2, 5, 6})
```

Similarly, other set methods like **`isdisjoint()`**, **`issubset()`**, and **`issuperset()`** are also available.

```python
# Example 2: Frozensets

# initialize A, B and C
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

# isdisjoint() method
print(A.isdisjoint(C))  # Output: True

# issubset() method
print(C.issubset(B))    # Output: True

# issuperset() method
print(B.issuperset(C))  # Output: True
```

**Output:**
```text
True
True
True
```

---

## 📘 Python Getattr()
*Source: `4. Python Functions/25. Python getattr().ipynb`*

# Python `getattr()`

The **`getattr()`** method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.

**Syntax**:

```python
getattr(object, name[, default])
```
The above syntax is equivalent to:

```python
object.name
```

## `getattr()` Parameters

The **`getattr()`** method takes multiple parameters:

* **object** - object whose named attribute's value is to be returned
* **name** - string that contains the attribute's name
* **default (Optional)** - value that is returned when the named attribute is not found

## Return Value from `getattr()`

**`getattr()`** method returns:

* value of the named attribute of the given object
* **`default`**, if no named attribute is found
* **`AttributeError`** exception, if named attribute is not found and **`default`** is not defined

```python
# Example 1: How getattr() works in Python?

class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)
```

**Output:**
```text
The age is: 23
The age is: 23
```

```python
# Example 2: getattr() when named attribute is not found

class Person:
    age = 23
    name = "Adam"

person = Person()

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))

# when no default value is provided
print('The sex is:', getattr(person, 'sex'))
```

**Output:**
```text
The sex is: Male
```

**Explanation**:

The named attribute **`sex`** is not present in the class **`Person`**. So, when calling **`getattr()`** method with a default value **`Male`**, it returns Male.

But, if we don't provide any default value, when the named attribute sex is not found, it raises an **`AttributeError`** saying the object has no sex attribute.

---

## 📘 Python Globals()
*Source: `4. Python Functions/26. Python globals().ipynb`*

# Python `globals()`

The **`globals()`** method returns the dictionary of the current global symbol table.
A symbol table is a data structure maintained by a compiler which contains all necessary information about the program.

These include variable names, methods, classes, etc.

There are mainly two kinds of symbol table.

1. Local symbol table
2. Global symbol table

**Local** symbol table stores all information related to the local scope of the program, and is accessed in Python using **locals()** method.

The local scope could be within a function, within a class, etc.

Likewise, a **Global** symbol table stores all information related to the global scope of the program, and is accessed in Python using **`globals()`** method.

The global scope contains all functions, variables that are not associated with any class or function.

## Syntax of `globals()`

The globals table dictionary is the dictionary of the current module (inside a function, this is a module where it is defined, not the module where it is called).

**Syntax**:

```python
globals()
```

## `globals()` Parameters

The **`globals()`** method doesn't take any parameters.

## Return Value from `globals()`

**`globals()`** method returns the dictionary of the current global symbol table.

```python
# Example 1: How globals() method works in Python?

globals()
```

**Output:**
```text
{'__name__': '__main__',
 '__doc__': 'Automatically created module for IPython interactive environment',
 '__package__': None,
 '__loader__': None,
 '__spec__': None,
 '__builtin__': <module 'builtins' (built-in)>,
 '__builtins__': <module 'builtins' (built-in)>,
 '_ih': ['',
  '# Example 1: How globals() method works in Python?\n\nglobals()'],
 '_oh': {},
 '_dh': ['C:\\Users\\Deepak\\01_Learn_Python4Data\\04_Python_Functions\\002_Python_Functions_Built_in'],
 'In': ['', '# Example 1: How globals() method works in Python?\n\nglobals()'],
 'Out': {},
 'get_ipython': <function IPython.core.getipython.get_ipython()>,
 'exit': <IPython.core.autocall.ZMQExitAutocall at 0x1689fe80700>,
 'quit': <IPython.core.autocall.ZMQExitAutocall at 0x1689fe80700>,
 '_': '',
 '__': '',
 '___': '',
 'json': <module 'json' from 'C:\\ProgramData\\Anaconda3\\lib\\json\\__init__.py'>,
 'getsizeof': <function sys.getsizeof>,
 'NamespaceMagics': IPython.core.magics.namespace.NamespaceMagics,
 '_nms': <IPython.co
... [Output truncated for brevity]
```

The output shows all global variables and other symbols for the current program.

```python
# Example 2: Modify global variable using global()

age = 23

globals()['age'] = 25
print('The age is:', age)
```

**Output:**
```text
The age is: 25
```

**Explanation**:

Here, since the global symbol table also stores all global variables, i.e. in this case, **`age`**, the value of **`age`** can be changed using **`globals()`** function.

The dictionary returned is accessed using the key of the variable **`age`** and modified to 25.

This is reflected in the global symbol table again.

---

## 📘 Python Exec()
*Source: `4. Python Functions/27. Python exec().ipynb`*

# Python `exec()`

The **`exec()`** method executes the dynamically created program, which is either a string or a code object.

**Syntax**:

```python
exec(object, globals, locals)
```

## `exec()` Parameters

**`exec()`** takes three parameters:

* **object** - Either a string or a code object
* **globals (optional)** - a dictionary
* **locals (optional)**- a mapping object. Dictionary is the standard and commonly used mapping type in Python.

The use of **`globals`** and **`locals`** will be discussed later in the article.

## Return Value from `exec()`

**`exec()`** doesn't return any value, it returns **`None`**.

```python
# Example 1: How exec() works?

program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
```

**Output:**
```text
Sum = 15
```

**Explanation**:

Here, the string object program is passed to **`exec()`** which executes the program. **`globals`** and **`locals`** are omitted in this case.

```python
# Example 2: Allow user to provide input

program = input('Enter a program:')
exec(program)

'''
Output:

Enter a program: [print(item) for item in [1, 2, 3]]
1
2
3
'''
```

**Output:**
```text
Enter a program:program
'\nOutput:\n\nEnter a program: [print(item) for item in [1, 2, 3]]\n1\n2\n3\n'
```

**Explanation**:

If you want to take Python code from the user which allows multiline code (using **`'\n'`**), you can use **`compile()`** method before using **`exec()`**.

Learn more about **compile() method in Python**.

## Be careful while using `exec()`

Consider a situation, you are using a Unix system (macOS, Linux etc) and you have imported **`os`** module. The os module provides a portable way to use operating system functionalities like read or write a file.

If you allow users to input a value using **`exec(input())`**, the user may issue commands to change file or even delete all the files using the command **`os.system('rm -rf *')`**.

If you are using **`exec(input())`** in your code, it's a good idea to check which variables and methods the user can use. You can see which variables and methods are available using **dir() method**.

```python
from math import *
exec('print(dir())')
```

**Output:**
```text
['In', 'NamespaceMagics', 'Out', '_', '_2', '_Jupyter', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_getshapeof', '_getsizeof', '_i', '_i1', '_i2', '_i3', '_ih', '_ii', '_iii', '_nms', '_oh', 'a', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'b', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exit', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'get_ipython', 'getsizeof', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'json', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'np', 'perm', 'pi', 'pow', 'prod', 'program', 'quit', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'var_dic_list']
```

## Restricting the Use of Available Methods and Variables in `exec()`

More often than not, all the available methods and variables used in **`exec()`** may not be needed, or even may have a security hole. You can restrict the use of these variables and methods by passing optional **`globals`** and **`locals`** parameters (dictionaries) to **`exec()`** method.

### 1. Both globals and locals parameters are omitted

If both parameters are omitted (as in our earlier examples), the code expected to be executed by **`exec()`** is executed in the current scope. You can check the available variables and methods using the following code:

```python
exec('print(dir())')
```

**Output:**
```text
['In', 'NamespaceMagics', 'Out', '_', '_2', '_Jupyter', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_getshapeof', '_getsizeof', '_i', '_i1', '_i2', '_i3', '_i4', '_ih', '_ii', '_iii', '_nms', '_oh', 'a', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'b', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exit', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'get_ipython', 'getsizeof', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'json', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'np', 'perm', 'pi', 'pow', 'prod', 'program', 'quit', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'var_dic_list']
```

### 2. Passing globals parameter; locals parameter is omitted

The **`globals`** and **`locals`** parameters (dictionaries) are used for global and local variables respectively. If **`locals`** dictionary is omitted, it defaults to **`globals`** dictionary. Meaning, **`globals`** will be used for both global and local variables.

> **Note**: You can check the current global and local dictionary in Python using **globals()** and **locals()** built-in methods respectively.

### 3. Passing empty dictionary as globals parameter

```python
from math import *
exec('print(dir())', {})

# This code will raise an exception
# exec('print(sqrt(9))', {})
```

**Output:**
```text
['__builtins__']
```

If you pass an empty dictionary as **`globals`**, only the **`__builtins__`** are available to the **`object`** (first parameter to the **`exec()`**). Even though we have imported math module in the above program, trying to access any of the functions provided by the **math module** will raise an exception.

#### Making Certain Methods available

```python
from math import *
exec('print(dir())', {'sqrt': sqrt, 'pow': pow})

# object can have sqrt() module
exec('print(sqrt(9))', {'sqrt': sqrt, 'pow': pow})
```

**Output:**
```text
['__builtins__', 'pow', 'sqrt']
3.0
```

Here, the code that is executed by **`exec()`** can also have **`sqrt()`** and **`pow()`** methods along with **`__builtins__`**.

It's possible to change the name of the method according to your wish.

```python
from math import *
exec('print(dir())', {'squareRoot': sqrt, 'pow': pow})

# object can have squareRoot() module
exec('print(squareRoot(9))', {'squareRoot': sqrt, 'pow': pow})
```

**Output:**
```text
['__builtins__', 'pow', 'squareRoot']
3.0
```

In the above program, **`squareRoot()`** calculates the square root (similar functionality like **`sqrt()`**). However, trying to use **`sqrt()`** will raise an exception.

#### Restricting the Use of built-ins

You can restrict the use of **`__builtins__`** by giving value **`None`** to the **`'__builtins__'`** in the **`globals`** dictionary.

```python
exec(object, {'__builtins__': None}) 
```

### 4. Passing both globals and locals dictionary

You can make needed functions and variables available for use by passing **`locals`** dictionary. For example:

```python
from math import *

globalsParameter = {'__builtins__' : None}
localsParameter = {'print': print, 'dir': dir}
exec('print(dir())', globalsParameter, localsParameter)
```

**Output:**
```text
['dir', 'print']
```

Here, only two built-in methods **print()** and **dir()** can be executed by **`exec()`** method.

It's important to note that, **`exec()`** executes the code and doesn't return any value (returns **`None`**). Hence, you cannot use return and **yield** statements outside of the function definitions.

---

## 📘 Python Hasattr()
*Source: `4. Python Functions/28. Python hasattr().ipynb`*

# Python `hasattr()`

The **`hasattr()`** method returns true if an object has the given named attribute and false if it does not.

**Syntax**:

```python
hasattr(object, name)
```

**`hasattr()`** is called by **getattr()** to check to see if **`AttributeError`** is to be raised or not.

## `hasattr()` Parameters

**`hasattr()`** method takes two parameters:

* **object** - object whose named attribute is to be checked
* **name** - name of the attribute to be searched

## Return Value from `hasattr()`

**`hasattr()`** method returns:

* **True**, if object has the given named attribute
* **False**, if object has no given named attribute

```python
# Example: How hasattr() works in Python?

class Person:
    age = 23
    name = 'Adam'

person = Person()

print('Person has age?:', hasattr(person, 'age'))
print('Person has salary?:', hasattr(person, 'salary'))
```

**Output:**
```text
Person has age?: True
Person has salary?: False
```

---

## 📘 Python Help()
*Source: `4. Python Functions/29. Python help().ipynb`*

# Python `help()`

The **`help()`** method calls the built-in Python help system.

**Syntax**:

```python
help(object)
```

## `help()` Parameters

The **`help()`** method takes a maximum of one parameter.

* **object (optional)** - you want to generate the help of the given **`object`**

## Return Value from `help()`

The **`help()`** method is used for interactive use. It's recommended to try it in your interpreter when you need help to write Python program and use **Python modules**.

> **Note**: object is passed to **`help()`** (not a string)

Try these on Python shell or Jupyter cell

```python
help(list)
```

**Output:**
```text
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self))
... [Output truncated for brevity]
```

```python
help(dict)
```

**Output:**
```text
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Built-in subclasses:
 |      StgDict
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |  
... [Output truncated for brevity]
```

```python
help(print)
```

**Output:**
```text
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

```python
help([1, 2, 3])
```

**Output:**
```text
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate sign
... [Output truncated for brevity]
```

If **`string`** is passed as an argument, name of a module, function, class, method, keyword, or documentation topic, and a help page is printed.

> **Note:** string is passed as an argument to **`help()`**

```python
help('random thing')
```

**Output:**
```text
No Python documentation found for 'random thing'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.
```

```python
help('print')
```

**Output:**
```text
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

```python
help('def')
```

**Output:**
```text
Function definitions
********************

A function definition defines a user-defined function object (see
section The standard type hierarchy):

   funcdef                   ::= [decorators] "def" funcname "(" [parameter_list] ")"
               ["->" expression] ":" suite
   decorators                ::= decorator+
   decorator                 ::= "@" dotted_name ["(" [argument_list [","]] ")"] NEWLINE
   dotted_name               ::= identifier ("." identifier)*
   parameter_list            ::= defparameter ("," defparameter)* "," "/" ["," [parameter_list_no_posonly]]
                        | parameter_list_no_posonly
   parameter_list_no_posonly ::= defparameter ("," defparameter)* ["," [parameter_list_starargs]]
                                 | parameter_list_starargs
   parameter_list_starargs   ::= "*" [parameter] ("," defparameter)* ["," ["**" parameter [","]]]
                               | "**" parameter [","]
   parameter                 ::= identifier [":" expression
... [Output truncated for brevity]
```

```python
from math import * 
help('math.pow')
```

**Output:**
```text
Help on built-in function pow in math:

math.pow = pow(x, y, /)
    Return x**y (x to the power of y).
```

> **Note:** no argument is passed to **`help()`**

If no argument is passed, Python's help utility (interactive help system) starts on the console.

```python
help()
```
Then, you can enter the name of the topic to get help on writing Python programs and using Python modules. For example:

```python
help> True
help> 'print'
help > print`
```

To quit the help utility and return to the interpreter, you need to type quit and press enter.

```python
help > quit
```

```python
help()
```

**Output:**
```text
Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
```

---

## 📘 Python Hex()
*Source: `4. Python Functions/30. Python hex().ipynb`*

# Python `hex()`

The **`hex()`** function converts an integer number to the corresponding hexadecimal string.

**Syntax**:

```python
hex(x)
```

## `hex()` Parameters

**`hex()`** function takes a single argument.

* **x** - integer number (int object or it has to define **`__index__()`** method that returns an integer)

## Return Value from `hex()`

**`hex()`** function converts an integer to the corresponding hexadecimal number in string form and returns it.

The returned hexadecimal string starts with the prefix **`0x`** indicating it's in hexadecimal form.

```python
# Example 1: How hex() works?

number = 435
print(number, 'in hex =', hex(number))

number = 0
print(number, 'in hex =', hex(number))

number = -34
print(number, 'in hex =', hex(number))

returnType = type(hex(number))
print('Return type from hex() is', returnType)
```

**Output:**
```text
435 in hex = 0x1b3
0 in hex = 0x0
-34 in hex = -0x22
Return type from hex() is <class 'str'>
```

If you need to find a hexadecimal representation of a float, you need to use **`float.hex()`** method.

```python
# Example 2: Hexadecimal representation of a float

number = 2.5
print(number, 'in hex =', float.hex(number))

number = 0.0
print(number, 'in hex =', float.hex(number))

number = 10.5
print(number, 'in hex =', float.hex(number))
```

**Output:**
```text
2.5 in hex = 0x1.4000000000000p+1
0.0 in hex = 0x0.0p+0
10.5 in hex = 0x1.5000000000000p+3
```

---

## 📘 Python Hash()
*Source: `4. Python Functions/31. Python hash().ipynb`*

# Python `hash()`

The **`hash()`** method returns the hash value of an object if it has one.

Hash values are just integers that are used to compare dictionary keys during a dictionary lookup quickly.

Internally, **`hash()`** method calls **`__hash__()`** method of an object which is set by default for any object. We'll look at this later..

**Syntax**:

```python
hash(object)
```

## `hash()` Parameters

**`hash()`** method takes a single parameter:

* **object** - the object whose hash value is to be returned (integer, string, float)

## Return Value from `hash()`

**`hash()`** method returns the hash value of an object if it has one.

If an object has custom **`__hash__()`** method, it truncates the return value to the size of **`Py_ssize_t`**.

```python
# Example 1: How hash() works in Python?
# hash for integer unchanged
print('Hash for 181 is:', hash(181))

# hash for decimal
print('Hash for 181.23 is:',hash(181.23))

# hash for string
print('Hash for Python is:', hash('Python'))
```

**Output:**
```text
Hash for 181 is: 181
Hash for 181.23 is: 530343892119126197
Hash for Python is: 5047677840638240195
```

```python
# Example 2: hash() for immutable tuple object?
# hash() method only works for immutable objects as tuple.

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

print('The hash is:', hash(vowels))
```

**Output:**
```text
The hash is: -8193489769393279200
```

## How hash() works for custom objects?

As stated above, hash() method internally calls **`__hash__()`** method. So, any objects can override **`__hash__()`** for custom hash values.

But for correct hash implementation, **`__hash__()`** should always return an integer. And, both **`__eq__()`** and **`__hash__()`** methods have to be implemented.

Below are the cases for correct **`__hash__()`** override.

**Cases for custom hash implementation for objects**

| **`__eq__()`** | **`__hash__()`** | **Description** |
|:----| :--- |:--- |
| **Defined (by default)** | **Defined (by default)** | **If left as is, all objects compare unequal (except themselves)** |
| **(If mutable) Defined** | **Should not be defined** | **Implementation of hashable collection requires key's hash value be immutable** |
| **Not defined** | **Should not be defined** | **If `__eq__()` isn't defined, `__hash__()` should not be defined.** |
| **Defined** | **Not defined** | **Class instances will not be usable as hashable collection. `__hash__()` implicity set to `None`. Raises `TypeError` exception if tried to retrieve the hash.** |
| **Defined** | **Retain from Parent** | **`__hash__ = <ParentClass>.__hash__`** |
| **Defined** | **Doesn't want to hash** | **`__hash__ = None`. Raises TypeError exception if tried to retrieve the hash.** |

```python
# Example 3: hash() for Custom Objects by overriding __hash__()

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))

person = Person(23, 'Adam')
print(hash(person))
```

**Output:**
```text
The hash is:
-9002918617615370443
```

> **Note:** You don't have to implement **`__eq__()`** method for the hash as it is created by default for all objects.

---

## 📘 Python Input()
*Source: `4. Python Functions/32. Python input().ipynb`*

# Python `input()`

The **`input()`** method reads a line from input, converts into a string and returns it.

**Syntax**:

```python
input([prompt])
```

## `input()` Parameters

The **`input()`** method takes a single optional argument:

* **prompt (Optional)** - a string that is written to standard output (usually screen) without trailing newline

## Return Value from `input()`

The **`input()`** method reads a line from the input (usually from the user), converts the line into a string by removing the trailing newline, and returns it.

If **EOF** is read, it raises an **`EOFError`** exception.

```python
# Example 1: How input() works in Python?
# get input from user

inputString = input()

print('The inputted string is:', inputString)
```

**Output:**
```text
Hello
The inputted string is: Hello
```

```python
# Example 2: Get input from user with a prompt
# get input from user

inputString = input('Enter a string:')

print('The inputted string is:', inputString)
```

**Output:**
```text
Enter a string:Perfect
The inputted string is: Perfect
```

---

## 📘 Python Id()
*Source: `4. Python Functions/33. Python id().ipynb`*

# Python `id()`

The **`id()`** function returns identity (unique integer) of an object.

**Syntax**:

```python
id(object)
```

## `id()` Parameters

**`id()`** function takes a single parameter **`object`**.

## Return Value from `id()`

**`id()`** unction returns the identity of the object. This is an integer that is unique for the given object and remains constant during its lifetime.

```python
# Example 1: How id() works?
class Foo:
    b = 5

dummyFoo = Foo()
print('id of dummyFoo =',id(dummyFoo))
```

**Output:**
```text
id of dummyFoo = 1830087123344
```

```python
# More Examples on id()

print('id of 5 =',id(5))

a = 5
print('id of a =',id(a))

b = a
print('id of b =',id(b))

c = 5.0
print('id of c =',id(c))
```

**Output:**
```text
id of 5 = 140731973642160
id of a = 140731973642160
id of b = 140731973642160
id of c = 1830086141680
```

It's important to note that everything in Python is an object, even numbers, and Classes.

Hence, integer **`5`** has a unique id. The id of the integer **`5`** remains constant during the lifetime. Similar is the case for float **`5.5`** and other objects.

---

## 📘 Python Isinstance()
*Source: `4. Python Functions/34. Python isinstance().ipynb`*

# Python `isinstance()`

The **`isinstance()`** function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).

**Syntax**:

```python
isinstance(object, classinfo)
```

## `isinstance()` Parameters

**`isinstance()`** takes two parameters:

* **object** - **`object`** to be checked
* **classinfo** - class, type, or tuple of classes and types

## Return Value from `isinstance()`

**`isinstance()`** returns:

* **`True`** if the **`object`** is an instance or subclass of a class or any element of the tuple
* **`False`** otherwise

If **`classinfo`** is not a type or tuple of types, a **`TypeError`** exception is raised.

```python
# Example 1: How isinstance() works?

class Foo:
    a = 5

fooInstance = Foo()

print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))
```

**Output:**
```text
True
False
True
```

```python
# Example 2: Working of isinstance() with Native Types

numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers,'instance of list?', result)

result = isinstance(numbers, dict)
print(numbers,'instance of dict?', result)

result = isinstance(numbers, (dict, list))
print(numbers,'instance of dict or list?', result)

number = 5

result = isinstance(number, list)
print(number,'instance of list?', result)

result = isinstance(number, int)
print(number,'instance of int?', result)
```

**Output:**
```text
[1, 2, 3] instance of list? True
[1, 2, 3] instance of dict? False
[1, 2, 3] instance of dict or list? True
5 instance of list? False
5 instance of int? True
```

---

## 📘 Python Int()
*Source: `4. Python Functions/35. Python int().ipynb`*

# Python `int()`

The **`int()`** method returns an integer object from any number or string.

**Syntax**:

```python
int(x=0, base=10)
```

## `int()` Parameters

**`int()`** method takes two arguments:

* **x** - Number or string to be converted to integer object.
    * The default argument is **`zero`**.
* **base** - Base of the number in x.
    * Can be 0 (code literal) or 2-36.

## Return Value from `int()`

**`int()`** method returns:

* an integer object from the given number or string treats default base as 10
* (No parameters) returns 0
* (If base given) treats the string in the given base (0, 2, 8, 10, 16)

```python
# Example 1: How int() works in Python?

# integer
print("int(123) is:", int(123))

# float
print("int(123.23) is:", int(123.23))

# string
print("int('123') is:", int('123'))
```

**Output:**
```text
int(123) is: 123
int(123.23) is: 123
int('123') is: 123
```

```python
# Example 2: How int() works for decimal, octal and hexadecimal?

# binary 0b or 0B
print("For 1010, int is:", int('1010', 2))
print("For 0b1010, int is:", int('0b1010', 2))

# octal 0o or 0O
print("For 12, int is:", int('12', 8))
print("For 0o12, int is:", int('0o12', 8))

# hexadecimal
print("For A, int is:", int('A', 16))
print("For 0xA, int is:", int('0xA', 16))
```

**Output:**
```text
For 1010, int is: 10
For 0b1010, int is: 10
For 12, int is: 10
For 0o12, int is: 10
For A, int is: 10
For 0xA, int is: 10
```

```python
# Example 3: int() for custom objects

# Internally, int() method calls an object's __int__() method.
# So, even if an object isn't a number, you can convert the object into an integer object.
# You can do this by overriding __index__() and __int__() methods of the class to return a number.
# These two methods should return the same value as older versions of Python uses __int__(), 
# while newer uses __index__() method.

class Person:
    age = 23

    def __index__(self):
        return self.age
    
    def __int__(self):
        return self.age

person = Person()
print('int(person) is:', int(person))
```

**Output:**
```text
int(person) is: 23
```

---

## 📘 Python Issubclass()
*Source: `4. Python Functions/36. Python issubclass().ipynb`*

# Python `issubclass()`

The **`issubclass()`** function checks if the class argument (first argument) is a subclass of classinfo class (second argument).

**Syntax**:

```python
issubclass(class, classinfo)
```

## `issubclass()` Parameters

**`issubclass()`** takes two parameters:

* **class** - class to be checked
* **classinfo** - class, type, or tuple of classes and types

## Return Value from `issubclass()`

**`issubclass()`** returns:

* **`True`** if **`class`** is subclass of a class, or any element of the tuple
* **`False`**  otherwise

```python
# Example 1: How issubclass() works?

class Polygon:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)

class Triangle(Polygon):
    def __init__(self):

        Polygon.__init__('triangle')
    
print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))
```

**Output:**
```text
True
False
True
True
```

It's important to note that class is considered a subclass of itself.

---

## 📘 Python Iter()
*Source: `4. Python Functions/37. Python iter().ipynb`*

# Python `iter()`

The Python **`iter()`** function returns an iterator for the given object.

The **`iter()`** function creates an object which can be iterated one element at a time.

These objects are useful when coupled with loops like **for loop**, **while loop**.

**Syntax**:

```python
iter(object, sentinel)
```

## `iter()` Parameters

The **`iter()`** function takes two parameters:

* **object** - object whose iterator has to be created (can be **sets**, **tuples**, etc.)
* **sentinel (optional)** - special value that is used to represent the end of a sequence

## Return Value from `iter()`

* The **`iter()`**  function returns an iterator object for the given object.

* If the user-defined object doesn't implement **`__iter__()`**, and **`__next__()** or **`__getitem()__`**, the **`TypeError`** exception is raised.

* If the sentinel parameter is also provided, **`iter()`** returns an iterator until the sentinel character isn't found.

```python
# Example 1: Working of Python iter()

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)

print(next(vowels_iter))    # 'a'
print(next(vowels_iter))    # 'e'
print(next(vowels_iter))    # 'i'
print(next(vowels_iter))    # 'o'
print(next(vowels_iter))    # 'u'
```

**Output:**
```text
a
e
i
o
u
```

```python
# Example 2: iter() for custom objects

class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

print_num = PrintNumber(3)

print_num_iter = iter(print_num)
print(next(print_num_iter))  # 1
print(next(print_num_iter))  # 2
print(next(print_num_iter))  # 3

# raises StopIteration
print(next(print_num_iter))
```

**Output:**
```text
1
2
3
```

```python
# Example 3: iter() with sentinel parameter

class DoubleIt:

    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start

    __call__ = __next__
    
my_iter = iter(DoubleIt(), 16)

for x in my_iter:
    print(x)
```

**Output:**
```text
2
4
8
```

Here, we have implemented a custom iterable object without a **`StopIteration`** condition.

However, we can use the **`iter()`** method with the **`sentinel`** parameter to stop the iteration. If the value returned from **`__next__()`** is equal to **`sentinel`**, **`StopIteration`** will be raised, otherwise, the value will be returned.

> Recommended Reading: **Python Iterators**

---

## 📘 Python List() Function
*Source: `4. Python Functions/38. Python list() Function.ipynb`*

# Python `list()`

The **`list()`** constructor returns a list in Python.

**Syntax**:

```python
list([iterable])
```

## `list()` Parameters

The **`list()`** constructor takes a single argument:

* **iterable (optional)** - an object that could be a sequence (**string**, **tuples**) or collection (**set**, **dictionary**) or any iterator object

## Return Value from `list()`

The **`list()`**  constructor returns a list.

* If no parameters are passed, it returns an empty list
* If iterable is passed as a parameter, it creates a list consisting of iterable's items.

```python
# Example 1: Create lists from string, tuple, and list

# empty list
print(list())

# vowel string
vowel_string = 'aeiou'
print(list(vowel_string))

# vowel tuple
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))

# vowel list
vowel_list = ['a', 'e', 'i', 'o', 'u']
print(list(vowel_list))
```

**Output:**
```text
[]
['a', 'e', 'i', 'o', 'u']
['a', 'e', 'i', 'o', 'u']
['a', 'e', 'i', 'o', 'u']
```

```python
# Example 2: Create lists from set and dictionary

# vowel set
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(list(vowel_set))

# vowel dictionary
vowel_dictionary = {'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5}
print(list(vowel_dictionary))
```

**Output:**
```text
['a', 'e', 'o', 'i', 'u']
['a', 'e', 'i', 'o', 'u']
```

> **Note:** In the case of dictionaries, the keys of the dictionary will be the items of the list. Also, the order of the elements will be random.

```python
# Example 3: Create a list from an iterator object

# objects of this class are iterators
class PowTwo:
    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        self.num = 0
        return self
        
    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result

pow_two = PowTwo(5)
pow_two_iter = iter(pow_two)

print(list(pow_two_iter))
```

**Output:**
```text
[1, 2, 4, 8, 16]
```

---

## 📘 Python Locals()
*Source: `4. Python Functions/39. Python locals().ipynb`*

# Python `locals()`

The **`locals()`** method updates and returns a dictionary of the current local symbol table.

A symbol table is a data structure maintained by a compiler which contains all necessary information about the program.

These include variable names, methods, classes, etc.

There are mainly two kinds of symbol table.

1. Global symbol table
2. Local symbol table

A **Global** symbol table stores all information related to the global scope of the program, and is accessed in Python using **globals()** method.

The global scope contains all functions, variables which are not associated with any class or function.

Likewise, **Local** symbol table stores all information related to the local scope of the program, and is accessed in Python using **`locals()`** method.

The local scope could be within a function, within a class, etc.

> Recommended Reading: **Namespace and scope of in Python**

**Syntax**:

```python
locals()
```

## `locals()` Parameters

**`locals()`** method doesn't take any parameters.

## Return Value from `locals()`

**`locals()`**  method updates and returns the dictionary associated with the current local symbol table.

```python
# Example 1: How locals() works in Python?

locals()
```

**Output:**
```text
{'__name__': '__main__',
 '__doc__': 'Automatically created module for IPython interactive environment',
 '__package__': None,
 '__loader__': None,
 '__spec__': None,
 '__builtin__': <module 'builtins' (built-in)>,
 '__builtins__': <module 'builtins' (built-in)>,
 '_ih': ['', '# Example 1: How locals() works in Python?\n\nlocals()'],
 '_oh': {},
 '_dh': ['C:\\Users\\Deepak\\01_Learn_Python4Data\\04_Python_Functions\\002_Python_Functions_Built_in'],
 'In': ['', '# Example 1: How locals() works in Python?\n\nlocals()'],
 'Out': {},
 'get_ipython': <function IPython.core.getipython.get_ipython()>,
 'exit': <IPython.core.autocall.ZMQExitAutocall at 0x225ebef0700>,
 'quit': <IPython.core.autocall.ZMQExitAutocall at 0x225ebef0700>,
 '_': '',
 '__': '',
 '___': '',
 'json': <module 'json' from 'C:\\ProgramData\\Anaconda3\\lib\\json\\__init__.py'>,
 'getsizeof': <function sys.getsizeof>,
 'NamespaceMagics': IPython.core.magics.namespace.NamespaceMagics,
 '_nms': <IPython.core.magics.namespace.
... [Output truncated for brevity]
```

> **Note:** **`globals()`** and **`locals()`** symbol table for the global environment is the same.

```python
# Example 2: How locals() works inside a local scope?

def localsNotPresent():
    return locals()

def localsPresent():
    present = True
    return locals()

print('localsNotPresent:', localsNotPresent())
print('localsPresent:', localsPresent())
```

**Output:**
```text
localsNotPresent: {}
localsPresent: {'present': True}
```

```python
# Example 3: Updating locals() dictionary values

def localsPresent():
    present = True
    print(present)
    locals()['present'] = False;
    print(present)

localsPresent()
```

**Output:**
```text
True
True
```

Unlike, **`globals()`** dictionary which reflects the change to the actual global table, **`locals()`** dictionary may not change the information inside the locals table.

---

## 📘 Python Len()
*Source: `4. Python Functions/40. Python len().ipynb`*

# Python `len()`

The **`len()`** function returns the number of items (length) in an object.

**Syntax**:

```python
len(s)
```

## `len()` Parameters

* **s** - a sequence (string, bytes, tuple, list, or range) or a collection (dictionary, set or frozen set)

## Return Value from `len()`

**`len()`**  function returns the number of items of an object.

Failing to pass an argument or passing an invalid argument will raise a **`TypeError`** exception.

```python
# Example 1: How len() works with tuples, lists and range?

testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))
```

**Output:**
```text
[] length is 0
[1, 2, 3] length is 3
(1, 2, 3) length is 3
Length of range(1, 10) is 9
```

```python
# Example 2: How len() works with strings and bytes?

testString = ''
print('Length of', testString, 'is', len(testString))

testString = 'Python'
print('Length of', testString, 'is', len(testString))

# byte object
testByte = b'Python'
print('Length of', testByte, 'is', len(testByte))

testList = [1, 2, 3]

# converting to bytes object
testByte = bytes(testList)
print('Length of', testByte, 'is', len(testByte))
```

**Output:**
```text
Length of  is 0
Length of Python is 6
Length of b'Python' is 6
Length of b'\x01\x02\x03' is 3
```

```python
# Example 3: How len() works with dictionaries and sets?

testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))

# Empty Set
testSet = set()
print(testSet, 'length is', len(testSet))

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))

testDict = {}
print(testDict, 'length is', len(testDict))

testSet = {1, 2}
# frozenSet
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))
```

**Output:**
```text
{1, 2, 3} length is 3
set() length is 0
{1: 'one', 2: 'two'} length is 2
{} length is 0
frozenset({1, 2}) length is 2
```

Internally, **`len()`** calls object's **`__len__`** method. You can think of **`len()`** as:

```python
def len(s):
    return s.__len__()
```

So, you can assign custom length to the object (if necessary)

```python
# Example 4: How len() works for custom objects?

class Session:
    def __init__(self, number = 0):
        self.number = number
    
    def __len__(self):
        return self.number


# default length is 0
s1 = Session()
print(len(s1))

# giving custom length
s2 = Session(6)
print(len(s2))
```

**Output:**
```text
0
6
```

---

## 📘 Python Max()
*Source: `4. Python Functions/41. Python max().ipynb`*

# Python `max()`

The Python **`max()`** funfunction returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.

**The **`max()`** function has two forms:**

```python
// to find the largest item in an iterable
max(iterable, *iterables, key, default)

// to find the largest item between two or more objects
max(arg1, arg2, *args, key)
```

## 1. `max()` with iterable arguments

To find the largest item in an iterable, we use this syntax:

```python
max(iterable, *iterables, key, default)
```

## `max()` Parameters

* **iterable** - an iterable such as list, tuple, set, dictionary, etc.
* **\*iterables** (optional) - any number of iterables; can be more than one
* **key (optional)** - key function where the iterables are passed and comparison is performed based on its return value
* **default (optional)** - default value if the given iterable is empty

```python
# Example 1: Get the largest item in a list

number = [3, 2, 8, 5, 10, 6]
largest_number = max(number);

print("The largest number is:", largest_number)
```

**Output:**
```text
The largest number is: 10
```

If the items in an iterable are strings, the largest item (ordered alphabetically) is returned.

```python
# Example 2: the largest string in a list

languages = ["Python", "C Programming", "Java", "JavaScript"]
largest_string = max(languages);

print("The largest string is:", largest_string)
```

**Output:**
```text
The largest string is: Python
```

In the case of dictionaries, **`max()`** returns the largest key. Let's use the **`key`** parameter so that we can find the dictionary's key having the largest value.

```python
# Example 3: max() in dictionaries

square = {2: 4, -3: 9, -1: 1, -2: 4}

# the largest key
key1 = max(square)
print("The largest key:", key1)    # 2

# the key whose value is the largest
key2 = max(square, key = lambda k: square[k])

print("The key with the largest value:", key2)    # -3

# getting the largest value
print("The largest value:", square[key2])    # 9
```

**Output:**
```text
The largest key: 2
The key with the largest value: -3
The largest value: 9
```

In the second **`max()`** function, we have passed a **lambda function** to the **`key`** parameter.

```python
key = lambda k: square[k]
```

The function returns the values of dictionaries. Based on the values (rather than the dictionary's keys), the key having the maximum value is returned.

>Few Notes:
* If we pass an empty iterator, a **`ValueError`** exception is raised. To avoid this, we can pass the **`default`** parameter.
* If we pass more than one iterators, the largest item from the given iterators is returned.

## 2. `max()` without iterable

To find the largest object between two or more parameters, we can use this syntax:

```python
max(arg1, arg2, *args, key)
```

## `max()` Parameters

* **arg1** - an object; can be numbers, strings, etc.
* **arg2** - an object; can be numbers, strings, etc.
* **\*args (optional)** - any number of objects
* **key (optional)** - key function where each argument is passed, and comparison is performed based on its return value

Basically, the **`max()`** function finds the largest item between two or more objects.

```python
# Example 4: Find the maximum among the given numbers

result = max(4, -5, 23, 5)
print("The maximum number is:", result)
```

**Output:**
```text
The maximum number is: 23
```

If you need to find the smallest item, you can use the **Python min()** function.

---

## 📘 Python Min()
*Source: `4. Python Functions/42. Python min().ipynb`*

# Python `min()`

The Python **`min()`** function returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters.

**The `min()` function has two forms:**

```python
// to find the smallest item in an iterable
min(iterable, *iterables, key, default)

// to find the smallest item between two or more objects
min(arg1, arg2, *args, key)
```

## 1. `min()` with iterable arguments

To find the largest item in an iterable, we use this syntax:

```python
min(iterable, *iterables, key, default)
```

## `min()` Parameters

* **iterable** - an iterable such as list, tuple, set, dictionary, etc.
* **\*iterables** (optional) - any number of iterables; can be more than one
* **key (optional)** - key function where the iterables are passed and comparison is performed based on its return value
* **default (optional)** - default value if the given iterable is empty

```python
# Example 1: Get the smallest item in a list

number = [3, 2, 8, 5, 10, 6]
largest_number = min(number);

print("The smallest number is:", largest_number)
```

**Output:**
```text
The smallest number is: 2
```

If the items in an iterable are strings, the smallest  item (ordered alphabetically) is returned.

```python
# Example 2: the smallest string in a list

languages = ["Python", "C Programming", "Java", "JavaScript"]
largest_string = min(languages);

print("The smallest string is:", largest_string)
```

**Output:**
```text
The smallest string is: C Programming
```

In the case of dictionaries, **`min()`** returns the largest key. Let's use the **`key`** parameter so that we can find the dictionary's key having the largest value.

```python
# Example 3: min() in dictionaries

square = {2: 4, -3: 9, -1: 1, -2: 4}

# the largest key
key1 = min(square)
print("The largest key:", key1)    # 2

# the key whose value is the largest
key2 = min(square, key = lambda k: square[k])

print("The key with the smallest value:", key2)    # -3

# getting the largest value
print("The largest value:", square[key2])    # 9
```

**Output:**
```text
The largest key: -3
The key with the smallest value: -1
The largest value: 1
```

In the second **`min()`** function, we have passed a **lambda function** to the **`key`** parameter.

```python
key = lambda k: square[k]
```

The function returns the values of dictionaries. Based on the values (rather than the dictionary's keys), the key having the maximum value is returned.

>Few Notes:
* If we pass an empty iterator, a **`ValueError`** exception is raised. To avoid this, we can pass the **`default`** parameter.
* If we pass more than one iterators, the smallest item from the given iterators is returned.

## 2. `min()` without iterable

To find the smallest object between two or more parameters, we can use this syntax:

```python
min(arg1, arg2, *args, key)
```

## `min()` Parameters

* **arg1** - an object; can be numbers, strings, etc.
* **arg2** - an object; can be numbers, strings, etc.
* **\*args (optional)** - any number of objects
* **key (optional)** - key function where each argument is passed, and comparison is performed based on its return value

Basically, the **`min()`** function finds the smallest item between two or more objects.

```python
# Example 4: Find the minimum among the given numbers

result = min(4, -5, 23, 5)
print("The minimum number is:", result)
```

**Output:**
```text
The minimum number is: -5
```

If you need to find the smallest item, you can use the **Python max()** function.

---

## 📘 Python Map()
*Source: `4. Python Functions/43. Python map().ipynb`*

# Python `map()`

The **`map()`** function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.

**Syntax**:

```python
map(function, iterable, ...)
```

## `map()` Parameters

* **function** - **`map()`** passes each item of the iterable to this function.
* **iterable** - iterable which is to be mapped

You can pass more than one iterable to the **`map()`** function.

## Return Value from `map()`

The **`map()`** function applies a given to function to each item of an iterable and returns a list of the results.

The returned value from **`map()`** (map object) can then be passed to functions like **list()** (to create a list), **set()** (to create a set) and so on.

```python
# Example 1: Working of map()

def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)  

# converting map object to set or list or tuple
numbersSquare = set(result)
#numbersSquare = list(result)
#numbersSquare = tuple(result)
print(numbersSquare)
```

In the above example, each item of the tuple is squared.

Since **`map()`** expects a function to be passed in, lambda functions are commonly used while working with **`map()`** functions.

A **lambda function** is a short function without a name. Visit this page to learn more about **Python lambda Function**.

```python
# Example 2: How to use lambda function with map()?

numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set or list or tuple
numbersSquare = set(result)
#numbersSquare = list(result)
#numbersSquare = tuple(result)
print(numbersSquare)
```

There is no difference in functionalities of this example and **Example 1**.

```python
# Example 3: Passing Multiple Iterators to map() Using Lambda

# In this example, corresponding items of two lists are added.

num1 = [4, 5, 6]
num2 = [5, 6, 7]

# Format: result = map(functionName, arguments)
result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))
```

**Output:**
```text
[9, 11, 13]
```

---

## 📘 Python Memoryview()
*Source: `4. Python Functions/44. Python memoryview().ipynb`*

# Python `memoryview()`

The **`memoryview()`** function returns a memory view object of the given argument.

Before we get into what memory views are, we need to first understand about Python's buffer protocol.

## Python Buffer Protocol

The buffer protocol provides a way to access the internal data of an object. This internal data is a memory array or a buffer.

The buffer protocol allows one object to expose its internal data (buffers) and the other to access those buffers without intermediate copying.

This protocol is only accessible to us at the C-API level and not using our normal codebase.

So, in order to expose the same protocol to the normal Python codebase, memory views are present.

## What is a memory view?

A memory view is a safe way to expose the buffer protocol in Python.

It allows you to access the internal buffers of an object by creating a memory view object.

## Why buffer protocol and memory views are important?

We need to remember that whenever we perform some action on an object (call a function of an object, slice an array), Python needs to create a **copy of the object**.

If we have large data to work with (eg. binary data of an image), we would unnecessarily create copies of huge chunks of data, which serves almost no use.

Using the buffer protocol, we can give another object access to use/modify the large data without copying it. This makes the program use less memory and increases the execution speed.

**Syntax**:

```python
memoryview(obj)
```

## `memoryview()` Parameters

The **`memoryview()`** function takes a single parameter:

* **obj** - object whose internal data is to be exposed. **`obj`** must support the buffer protocol (**bytes**, **bytearray**)

## Return Value from `memoryview()`

The **`memoryview()`** function returns a memory view object.

```python
# Example 1: How memoryview() works in Python?

# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')

mv = memoryview(random_byte_array)

# access memory view's zeroth index
print(mv[0])

# create byte from memory view
print(bytes(mv[0:2]))

# create list from memory view
print(list(mv[0:3]))
```

**Output:**
```text
65
b'AB'
[65, 66, 67]
```

**Explanation:**

Here, we created a memory view object **`mv`** from the byte array **`random_byte_array`**.

Then, we accessed the **`mv`**'s 0th index, **`'A'`**, and printed it (which gives the ASCII value - 65).

Again, we accessed the **`mv`**'s indices from 0 and 1, **`'AB'`** , and converted them into bytes.

Finally, we accessed all indices of **`mv`** and converted it to a list. Since internally **`bytearray`** stores ASCII value for the alphabets, the output is a list of ASCII values of **`A`**, **`B`**, and **`C`**.

```python
# Example 2: Modify internal data using memory view

# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')
print('Before updation:', random_byte_array)

mv = memoryview(random_byte_array)

# update 1st index of mv to Z
mv[1] = 90
print('After updation:', random_byte_array)
```

**Output:**
```text
Before updation: bytearray(b'ABC')
After updation: bytearray(b'AZC')
```

**Explanation:**

Here, we updated the memory view's 1st index to 90, the ASCII value of **`Z`**.

Since, the memory view object mv references the same buffer/memory, updating the index in **`mv`** also updates **`random_byte_array`**.

---

## 📘 Python Next()
*Source: `4. Python Functions/45. Python next().ipynb`*

# Python `next()`

The **`next()`** function returns the next item from the iterator.

**Syntax**:

```python
next(iterator, default)
```

## `next()` Parameters

The **`next()`** function takes a single parameter:

* **iterator** - **`next()`** retrieves next item from the **`iterator`**
* **default (optional)** - this value is returned if the iterator is exhausted (there is no next item)

## Return Value from `next()`

* The **`next()`** function returns the next item from the iterator.
* If the iterator is exhausted, it returns the **`default`** value passed as an argument.
* If the **`default`** parameter is omitted and the **`iterator`** is exhausted, it raises **`StopIteration`** exception.

```python
# Example 1: Get the next item

random = [5, 9, 'cat']

# converting the list to an iterator
random_iterator = iter(random)
print(random_iterator)

# Output: 5
print(next(random_iterator))

# Output: 9
print(next(random_iterator))

# Output: 'cat'
print(next(random_iterator))

# This will raise Error
# iterator is exhausted
print(next(random_iterator))
```

A list is an **iterable** and you can get its **iterator** from it by using the **`iter()`** function in Python.

We got an error from the last statement in the above program because we tried to get the next item when no next item was available (iterator is exhausted).

In such cases, you can give a **`default`** value as the second parameter.

```python
# Example 2: Passing default value to next()

random = [5, 9]

# converting the list to an iterator
random_iterator = iter(random)

# Output: 5
print(next(random_iterator, '-1'))

# Output: 9
print(next(random_iterator, '-1'))

# random_iterator is exhausted
# Output: '-1'
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
```

**Output:**
```text
5
9
-1
-1
-1
```

> **Note:** Internally, **`next()`** calls the **`__next__()`** method.

---

## 📘 Python Object()
*Source: `4. Python Functions/46. Python object().ipynb`*

# Python `object()`

The **`object()`** function returns a featureless object which is a base for all classes.

**Syntax**:

```python
o = object()
```

## `object()` Parameters

The **`object()`** function doesn't accept any parameters.

## Return Value from `object()`

The **`object()`** function function returns a featureless object.

```python
# Example: How object() works?

test = object()

print(type(test))
print(dir(test))
```

Here, an object **`test`** is created.

In the program, we have used **type()** to get the type of the object.

Similarly, we have used **dir()** to get all the attributes. These attributes (properties and methods) are common to instances of all Python classes.

---

## 📘 Python Oct()
*Source: `4. Python Functions/47. Python oct().ipynb`*

# Python `oct()`

The **`oct()`** function takes an integer number and returns its octal representation.

**Syntax**:

```python
oct(x)
```

## `oct()` Parameters

The **`oct()`** function takes a single parameter x.

This parameter could be:

* an integer number (binary, decimal or hexadecimal)
* if not an integer, it should implement **`__index__()`** to return an integer

## Return Value from `oct()`

The **`oct()`** function returns an octal string from the given integer number.

```python
# Example 1: How oct() works in Python?

# decimal to octal
print('oct(10) is:', oct(10))

# binary to octal
print('oct(0b101) is:', oct(0b101))

# hexadecimal to octal
print('oct(0XA) is:', oct(0XA))
```

**Output:**
```text
oct(10) is: 0o12
oct(0b101) is: 0o5
oct(0XA) is: 0o12
```

```python
# Example 2: oct() for custom objects

class Person:
    age = 23

    def __index__(self):
        return self.age

    def __int__(self):
        return self.age

person = Person()
print('The oct is:', oct(person))
```

**Output:**
```text
The oct is: 0o27
```

Here, the Person class implements **`__int__()`** and **`__index__()`**. That's why we can use **`oct()`** on the objects of Person.

> **Note:** For compatibility, it's recommended to implement **`__int__()`** and **`__index__()`** with the same output.

---

## 📘 Python Ord()
*Source: `4. Python Functions/48. Python ord().ipynb`*

# Python `ord()`

The **`ord()`** function returns an integer representing the Unicode character.

**Syntax**:

```python
ord(ch)
```

## `ord()` Parameters

The **`ord()`** function takes a single parameter:

* **ch** - a Unicode character

## Return Value from `ord()`

The **`ord()`** function returns an integer representing the Unicode character.

```python
# Example: How ord() works in Python?

print(ord('5'))    # 53
print(ord('A'))    # 65
print(ord('$'))    # 36
```

**Output:**
```text
53
65
36
```

By the way, the **`ord()`** function is the inverse of the **Python chr() function**.

---

## 📘 Python Open()
*Source: `4. Python Functions/49. Python open().ipynb`*

# Python `open()`

The **`open()`** function opens the file (if possible) and returns the corresponding file object.

**Syntax**:

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

## `open()` Parameters

* **file** - path-like object (representing a file system path)
* **mode (optional)** - mode while opening a file. If not provided, it defaults to **`'r'`** (open for reading in text mode). Available file modes are:

| Mode | Description |
|:----| :--- |
| **`'r'`** | **Open a file for reading. (default)** |
| **`'w'`** | **Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.** |
| **`'x'`** | **Open a file for exclusive creation. If the file already exists, the operation fails.** |
| **`'a'`** | **Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.** |
| **`'t'`** | **Open in text mode. (default)** |
| **`'b'`** | **Open in binary mode.** |
| **`'+'`** | **Open a file for updating (reading and writing)** |

* **buffering** (optional) - used for setting buffering policy
* **encoding** (optional) - the encoding format
* **errors** (optional) - string specifying how to handle encoding/decoding errors
* **newline** (optional) - how newlines mode works (available values: **`None`**, **`' '`**, **`'\n'`**, **`'r'`**, and **`'\r\n'`**
* **closefd** (optional) - must be **`True`** (default); if given otherwise, an exception will be raised
* **opener** (optional) - a custom opener; must return an open file descriptor

## Return Value from `open()`

The **`open()`** function returns a file object which can used to read, write and modify the file.

If the file is not found, it raises the **`FileNotFoundError`** exception.

```python
# Example 1: How to open a file in Python?

# opens test.text file of the current directory
f = open("test.txt")

# To get the current directory
#import os
#os.getcwd()

# specifying the full path
f = open("C:/Python99/README.txt")
```

Since the mode is omitted, the file is opened in **`'r'`** mode; opens for reading.

```python
# Example 2: Providing mode to open()

# opens the file in reading mode
#f = open("path_to_file", mode='r')
f = open("C:/Python99/README.txt", mode='r')

# opens the file in writing mode 
#f = open("path_to_file", mode = 'w')
f = open("C:/Python99/README.txt", mode='w')

# opens for writing to the end 
#f = open("path_to_file", mode = 'a')
f = open("C:/Python99/README.txt", mode='a')
```

Python's default encoding is ASCII. You can easily change it by passing the **`encoding`** parameter.

```python
#f = open("path_to_file", mode = 'r', encoding='utf-8')
f = open("C:/Python99/README.txt", mode = 'r', encoding='utf-8')
```

---

## 📘 Python Pow()
*Source: `4. Python Functions/50. Python pow().ipynb`*

# Python `pow()`

The **`pow()`** function returns the power of a number.

**Syntax**:

```python
pow(x, y, z)
```

## `pow()` Parameters

The pow() function takes three parameters:

* **x** - a number, the base
* **y** - a number, the exponent
* **z (optional)** - a number, used for modulus

Hence,

* **`pow(x, y)`** is equal to **$x^y$**
* **`pow(x, y, z)`** is equal to **$x^y$`% z`**

```python
# Example 1: Python pow()

# positive x, positive y (x**y)
print(pow(2, 2))    # 4

# negative x, positive y
print(pow(-2, 2))    # 4  

# positive x, negative y
print(pow(2, -2))    # 0.25

# negative x, negative y
print(pow(-2, -2))    # 0.25
```

**Output:**
```text
4
4
0.25
0.25
```

```python
# Example 2: pow() with three arguments (x**y) % z

x = 7
y = 2
z = 5

print(pow(x, y, z))    # 4
```

**Output:**
```text
4
```

Here, 7 powered by 2 equals 49. Then, 49 modulus 5 equals 4.

---

## 📘 Python Print()
*Source: `4. Python Functions/51. Python print().ipynb`*

# Python `print()`

The **`print()`** function prints the given object to the standard output device (screen) or to the text stream file.

**Syntax**:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

## `print()` Parameters

* **objects** - object to the printed. **\*** indicates that there may be more than one object
* **sep** - objects are separated by sep. **Default value:** **`' '`**
* **end** - **`end`** is printed at last
* **file** - must be an object with write(string) method. If omitted it, **`sys.stdout`** will be used which prints objects on the screen.
* **flush** - If **`True`**, the stream is forcibly flushed. **Default value:** **`False`**

>**Note:** **`sep`**, **`end`**, **`file`**, and **`flush`** are keyword arguments. If you want to use **`sep`** argument, you have to use:

```python
print(*objects, sep = 'separator')
```
not

```python
print(*objects, 'separator')
```

## Return Value from `print()`

The **`print()`** function doesn't return any value; returns **`None`**.

```python
# Example 1: How print() works in Python?

print("Python is fun.")

a = 5
# Two objects are passed
print("a =", a)

b = a
# Three objects are passed
print('a =', a, '= b')
```

**Output:**
```text
Python is fun.
a = 5
a = 5 = b
```

In the above program, only **`objects`** parameter is passed to **`print()`** function (in all three print statements).

Hence,

* **`' '`** separator is used. Notice, the space between two objects in the output.
* **`end`** parameter **`'\n'`** (newline character) is used. Notice, each print statement displays the output in the new line.
* **`file`** is **`sys.stdout`**. The output is printed on the screen.
* **`flush`** is **`False`**. The stream is not forcibly flushed.

```python
# Example 2: print() with separator and end parameters

a = 5
print("a =", a, sep='00000', end='\n\n\n')
print("a =", a, sep='0', end='')
```

**Output:**
```text
a =000005


a =05
```

We passed the **`sep`** and **`end`** parameters in the above program.

```python
# Example 3: print() with file parameter

# In Python, you can print objects to the file by specifying the file parameter.

sourceFile = open('python.txt', 'w')
print('Pretty cool, huh!', file = sourceFile)
sourceFile.close()
```

This program tries to open the **python.txt** in writing mode. If this file doesn't exist, **python.txt** file is created and opened in writing mode.

Here, we have passed **`sourceFile`** file object to the **`file`** parameter. The string object 'Pretty cool, huh!' is printed to **python.txt** file (check it in your system).

Finally, the file is closed using **`close()`** method.

---

## 📘 Python Property()
*Source: `4. Python Functions/52. Python property().ipynb`*

# Python `property()`

The **`property()`** construct returns the property attribute.

**Syntax**:

```python
property(fget=None, fset=None, fdel=None, doc=None)
```

## `property()` Parameters

The **`property()`** takes four optional parameters:

* **fget (optional)** - Function for getting the attribute value. Defaults to **`None`**.
* **fset (optional)** - Function for setting the attribute value. Defaults to **`None`**.
* **fdel (optional)** - Function for deleting the attribute value. Defaults to **`None`**.
* **doc (optional)** - A string that contains the documentation (docstring) for the attribute. Defaults to **`None`**.

## Return Value from `property()`

**`property()`** returns the property attribute from the given getter, setter, and deleter.

* If no arguments are given, **`property()`** returns a base property attribute that doesn't contain any getter, setter or deleter.
* If **doc** isn't provided, **`property()`** takes the docstring of the getter function.

```python
# Example 1: Create attribute with getter, setter, and deleter

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name
    # and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')

p = Person('Adam')
print(p.name)
p.name = 'John'
del p.name
```

**Output:**
```text
Getting name
Adam
Setting name to John
Deleting name
```

Here, **`_name`** is used as the private variable for storing the name of Person.

We also set:

* a getter method **`get_name()`** to get the name of the person,
* a setter method **`set_name()`** to set the name of the person,
* a deleter method **`del_name()`** to delete the name of the person.

Now, we set a new property attribute **`name`** by calling the **`property()`** method.

As shown in the program, referencing **`p.name`** internally calls **`get_name()`** as getter, **`set_name()`** as setter and **`del_name()`** as deleter through the printed output present inside the methods.

```python
# Example 2: Using @property decorator

# Instead of using property(), you can use the Python decorator @property to assign
# the getter, setter, and deleter.

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

p = Person('Adam')
print('The name is:', p.name)
p.name = 'John'
del p.name
```

**Output:**
```text
Getting name
The name is: Adam
Setting name to John
Deleting name
```

Here, instead of using **`property()`**, we've used the **`@property`** **decorator**.

First, we specify that **`name()`** method is also an attribute of **`Person`**. This is done by using **`@property`** before the getter method as shown in the program.

Next, we use the attribute name to specify the setter and the deleter.

This is done by using **`@name.setter`** for the setter method and **`@name.deleter`** for the deleter method.

Notice, we've used the same method **`name()`** with different definitions for defining the getter, setter, and deleter.

Now, whenever we use **`p.name`**, it internally calls the appropriate getter, setter, and deleter as shown by the printed output present inside the method.

---

## 📘 Python Range()
*Source: `4. Python Functions/53. Python range().ipynb`*

# Python `range()`

The **`range()`** type **generates an immutable sequence of numbers** between the given start integer to the stop integer.

**`range()`** constructor has two forms of definition:

```python
range(stop)
range(start, stop[, step])
```

## `range()` Parameters

**`range()`** takes mainly three arguments. Out of the three 2 arguments are optional. i.e., start and step are the optional arguments having the same use in both definitions:

* **start** - integer starting from which the sequence of integers is to be returned, i.e., lower limit. By default, it starts with 0 if not specified.

* **stop** - integer before which the sequence of integers is to be returned. i.e., upper lmit where it generate numbers up to this number. The **`range()`** doesn’t include this number in the result, i.e., the range of integers ends at **`stop - 1`**.

* **step (Optional)** - integer value which determines the increment between each integer in the sequence, i.e., difference between each number in the result. The default value of the step is 1 if not specified.

## Return Value from `range()`

**`range()`** returns an immutable sequence object of numbers depending upon the definitions used:

* **`range(stop)`**

Returns a sequence of numbers starting from **`0`** to **`stop - 1`**
Returns an empty sequence if **`stop`** is **`negative`** or **`0`**.

* **`range(start, stop[, step])`**
The return value is calculated by the following formula with the given constraints:

```python
r[n] = start + step*n (for both positive and negative step)
where, n >=0 and r[n] < stop (for positive step)
where, n >= 0 and r[n] > stop (for negative step)
```

* (If no **`step`**) Step defaults to 1. Returns a sequence of numbers starting from **`start`** and ending at **`stop - 1`**.
* (if **`step`** is zero) Raises a **`ValueError`** exception
* (if **`step`** is non-zero) Checks if the **value constraint** is met and returns a sequence according to the formula
If it doesn't meet the value constraint, **Empty** sequence is returned.

```python
# Example 1: How range works in Python?

# empty range
print(list(range(0)))

# using range(stop)
print(list(range(5)))

# using range(stop)
print(list(range(10)))

# using range(start, stop)
print(list(range(1, 10)))
```

**Output:**
```text
[]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

<div>

</div>

>**Note:** We've converted the range to a **[Python list](https://github.com/milaan9/02_Python_Datatypes/blob/main/003_Python_List.ipynb)**, as **`range()`** returns a generator-like object that only prints the output on demand.

However, the range object returned by the range constructor can also be accessed by its index. It supports both positive and negative indices.

You can access the range object by index as:

```python
rangeObject[index]
```

```python
# Example 2: Create a list of even number between the given numbers using range()

start = 2
stop = 14
step = 2

print(list(range(start, stop, step)))
```

**Output:**
```text
[2, 4, 6, 8, 10, 12]
```

```python
# Example 3: How range() works with negative step?

start = 2
stop = -14
step = -2

print(list(range(start, stop, step)))

# value constraint not met
print(list(range(start, 14, step)))
```

**Output:**
```text
[2, 0, -2, -4, -6, -8, -10, -12]
[]
```

## Python `range()` using `for` loop

Using **`for`** loop, we can iterate over a sequence of numbers produced by the **`range( )`** function. Let’s understand how to use a **`range( )`** function of Python 3 with the help of a simple example.

```python
# Example 4: Using only one argument
# Print first 5 numbers using range function

print("Python range() example")
print("Get numbers from range 0 to 5")
for i in range(5):
    print(i, end=', ')
```

**Output:**
```text
Python range() example
Get numbers from range 0 to 5
0, 1, 2, 3, 4,
```

<div>

</div>

>**Note**: We got integers from 0 to 4 because **`range( )`** function doesn’t include the last (stop) number in the result, i.e., Only a stop argument is passed to **`range( )`**. So by default, it takes **`start = 0`** and **`step = 1`**.

```python
# Example 5: using two arguments (i.e., start and stop)

# Print integers within given start and stop number using range()
for i in range(5, 10):
    print(i, end=', ')
```

**Output:**
```text
5, 6, 7, 8, 9,
```

>**Note:** By default, it took step value as 1.

```python
# Example 6: using all three arguments

# using start, stop, and step arguments in range()
print("Printing All even numbers between 2 and 10 using range()")
for i in range(2, 10, 2):
    print(i, end=', ')
```

**Output:**
```text
Printing All even numbers between 2 and 10 using range()
2, 4, 6, 8,
```

>**Note:** All three arguments are specified i.e., **`start = 2`**, **`stop = 10`**, **`step = 2`**.  The step value is 2 so the difference between each number is 2.

### Practice Problem 1:

Generate a range of numbers from 9 to 100 divisible by 3 in Python using **`range()`** function.

### Points to remember about `range()` function arguments

* **`range()`** only works with the integers. All arguments must be integers. You can not use float number or any other type in a start, stop and step argument of a **`range()`**.

* All three arguments can be positive or negative.

* The step value must not be zero. If a step is zero Python raises a ValueError exception.

### for `i` in range – `for` loop with `range()`

As you know for loop executes a block of code or statement repeatedly for the fixed number of times. Using for loop we can iterate over a sequence of numbers produced by the **`range()`** function. Let’s see how to use for loop and **`range()`** function to print the odd numbers between 1 and 10. Using this example, we can understand how i is getting its value when we use **`range()`** and for loop together.

```python
# Example 7:

for i in range(1, 10, 2):
    print("Current value of i is:", i)
```

**Output:**
```text
Current value of i is: 1
Current value of i is: 3
Current value of i is: 5
Current value of i is: 7
Current value of i is: 9
```

**In `for i in range()` i is the iterator variable**. To understand what does for i in **`range()`** mean in Python, first, we need to understand the working of **`range()`** function.  The **`range()`** function uses the generator to produce numbers within a range, i.e., it doesn’t produce all numbers at once. It generates the next value only when for loop iteration asked for it. In each loop iteration, Python generates the next value and assign it to the iterator variable i.

**Explanation:**

Program execution

* As you can see in the output, the variable i is not getting the value 1, 3, 5, 7, 9 at the same time.
* In the first iteration of for loop value of i is the value of start.  i.e., The first value of i is the starting number of a range. Here the range starts at 1.
* Next, In every subsequent iteration of for loop, the value of i incremented sequentially. The value of i is determined by the formula i = i + step. i.e., in the second iteration, i become 3, and so on.

As you know, In every iteration of for loop, **`range()`** generates the next number and assigns it to the iterator variable i. i.e., We get numbers on demand (**`range()`** produces number one by one as the loop moves to the next iteration). Because of this behavior **`range()`** is faster and saves memory.

### Practice Problem 3:

Print the following number pattern using Python **`range()`** and for loop.

```python
1 
2 2 
3 3 3
```

`for num in range(3):
    for i in range(num):
        print(num, end=" ")
    print()  # new line after each row to show pattern correctly`

### Inclusive range

In this section, we will learn how to generate an inclusive range. The **`range(n)`** is of exclusive nature that is why it doesn’t include the last number in the output.  i.e., The given endpoint is never part of the generated result. 

For example, **`range(0, 5) = [0, 1, 2, 3, 4]`**. The result contains numbers from **`0`** to up to **`5`** but not 5 and the total count is 5. The **`range(start, stop)`** not include stop number in the output because the index (i) always starts with 0 in Python.

If you want to include the last number in the output i.e., If you want an inclusive range then set stop argument value as stop+step.

```python
# Example 8: Inclusive range() example.

# Printing inclusive range
start = 1
stop  = 5 
step  = 1
stop +=step #now stop is 6

for i in range(start, stop, step):
    print(i, end=', ')
```

**Output:**
```text
1, 2, 3, 4, 5,
```

```python
# Example 9: Printing inclusive range
start = 2
stop  = 10 
step  = 2
stop +=step #now stop is 12

for i in range(start, stop, step):
    print(i, end=', ')
```

**Output:**
```text
2, 4, 6, 8, 10,
```

### Decrementing with **`range()`** using a negative step

We can use negative values in all the arguments of **`range()`** function i.e., start, stop, and step.

```python
# Example 10:

start = -2
stop = -10
step = -2
print("Negative number range")
for number in range(start, stop, step):
    print(number, end=', ')
```

**Output:**
```text
Negative number range
-2, -4, -6, -8,
```

### Decrementing with the range from Negative to Positive number

Here in this example, we will learn how to use a step argument to display a range of numbers from negative to positive. Range of negative numbers.

```python
# Example 11:

# printing range from negative to positive
for num in range(-2, 5, 1):
    print(num, end=", ")
```

**Output:**
```text
-2, -1, 0, 1, 2, 3, 4,
```

### Python range from Positive to Negative number

Here in this example, we can learn how to use step argument effectively to display numbers from positive to negative.

```python
# Example 12:

# printing range from positive to negtive
print (" printing range from Positive to Negative")
for num in range(2,-5,-1):
    print(num, end=", ")
```

**Output:**
```text
printing range from Positive to Negative
2, 1, 0, -1, -2, -3, -4,
```

### Reverse range

If you want to print the sequence of numbers within range by descending order or reverse order in Python then its possible, there are two ways to do this.

**The first is to use a negative or down step value**. i.e., set the step argument of a **`range()`** to **`-1`**. For example, if you want to display a number sequence like **`[5, 4, 3, 2, 1, 0]`** i.e., we want reverse iteration or backward iteration of for loop with **`range()`** function.

Let’s see how to **loop backward using indices** in Python to display a range of numbers from 5 to 0.

```python
# Example 13:

print ("Displaying a range of numbers by reverse order")
for i in range(5, -1, -1):
    print (i, end=', ')
```

**Output:**
```text
Displaying a range of numbers by reverse order
5, 4, 3, 2, 1, 0,
```

### Use the reversed function to reverse range in Python

Alternatively, using The **`reversed()`** function, we can reverse any sequence. If we use the **`reversed()`** function with **`range()`**, that will return a range_iterator that accesses the given range of numbers in the reverse order. The below example will let you know how to make a reverse for loop in Python.

```python
# Example 14:

print("Printing reverse range using reversed()")
for i in reversed(range(0, 5)):
    print(i)
```

**Output:**
```text
Printing reverse range using reversed()
4
3
2
1
0
```

```python
# Example 15: Check the output type if  we use range() with reversed()

print("Checking the type")
print(type(range(0, 5)))
print(type(reversed(range(0,5))))
```

**Output:**
```text
Checking the type
<class 'range'>
<class 'range_iterator'>
```

### Concatenating the result of two range() function

Let say you want to add **`range(5) + range(10,15)`**. (Note: this code is a pseudo-code.)  And you want the concatenated range like **`[0, 1, 2, 3, 4, 10, 11, 12, 13, 14]`**.

We can concatenate the output of two range functions using the itertools’s **`chain()`** function.

Program: Concatenating two range function results.

```python
# Example 16:

from itertools import chain

print ("Concatinated two range() function")
concatenated_range = chain(range(10), range(50, 75))
for num in concatenated_range:
    print(num,end=", ")
```

**Output:**
```text
Concatinated two range() function
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
```

---

## 📘 Python Repr()
*Source: `4. Python Functions/54. Python repr().ipynb`*

# Python `repr()`

The **`repr()`** function returns a printable representation of the given object.

**Syntax**:

```python
repr(obj)
```

## `repr()` Parameters

The **`repr()`** function takes a single parameter:

* **obj** - the object whose printable representation has to be returned

## Return Value from `property()`

The **`repr()`** function returns a printable representational string of the given object.

```python
# Example 1: How repr() works in Python?

var = 'foo'

print(repr(var))
```

**Output:**
```text
'foo'
```

Here, we assign a value **`'foo'`** to **`var`**. Then, the **`repr()`** function returns **`"'foo'"`**, **`'foo'`** inside double-quotes.

When the result from **`repr()`** is passed to **`eval()`**, we will get the original object (for many types).

```python
# Example 2: Implement __repr__() for custom objects

# Internally, repr()function calls __repr__() of the given object.

# You can easily implement/override __repr__() so that repr() works differently.

class Person:
    name = 'Adam'

    def __repr__(self):
        return repr('Hello ' + self.name )

print(repr(Person()))
```

**Output:**
```text
'Hello Adam'
```

---

## 📘 Python Reversed()
*Source: `4. Python Functions/55. Python reversed().ipynb`*

# Python `reversed()`

The **`reversed()`** function returns the reversed iterator of the given sequence.

**Syntax**:

```python
reversed(seq)
```

## `reversed()` Parameters

The **`reversed()`** function takes a single parameter:

* **seq** - the sequence to be reversed

A sequence is an object that supports sequence protocols: **`__len__()`** and **`__getitem__()`** methods. For example, **tuple**, **string**, **list**, **range()**, etc.

We can also use **`reversed()`** in any object that implements **`__reverse__()`**.

## Return Value from `reversed()`

The **`reversed()`** function returns an iterator that accesses the given sequence in the reverse order.

```python
# Example 1: Using reveresed() in string, tuple, list, and range

# for string
seq_string = 'Python'
print(list(reversed(seq_string)))

# for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))

# for range
seq_range = range(5, 9)
print(list(reversed(seq_range)))

# for list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))
```

**Output:**
```text
['n', 'o', 'h', 't', 'y', 'P']
['n', 'o', 'h', 't', 'y', 'P']
[8, 7, 6, 5]
[5, 3, 4, 2, 1]
```

In our example, we have converted the iterators returned by **`reversed()`** to list using the **`list()`** function.

```python
# Example 2: reversed() in custom objects

class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)

v = Vowels()
print(list(reversed(v)))
```

**Output:**
```text
['u', 'o', 'i', 'e', 'a']
```

---

## 📘 Python Round()
*Source: `4. Python Functions/56. Python round().ipynb`*

# Python `round()`

The **`round()`** function returns a floating-point number rounded to the specified number of decimals.

**Syntax**:

```python
round(number, ndigits)
```

## `round()` Parameters

The **`round()`** function takes two parameters:

* **number** - the number to be rounded
* **ndigits (optional)** - number up to which the given number is rounded; defaults to 0

## Return Value from `round()`

* If **`ndigits`** is not provided, **`round()`** returns the nearest integer to the given number.
* If **`ndigits`** is given, **`round()`** returns the number rounded off to the **`ndigits`** digits.

```python
# Example 1: How round() works in Python?

# for integers
print(round(10))

# for floating point
print(round(10.7))

# even choice
print(round(5.5))
```

**Output:**
```text
10
11
6
```

```python
# Example 2: Round a number to the given number of decimal places

print(round(2.665, 2))
print(round(2.675, 2))
```

**Output:**
```text
2.67
2.67
```

>**Note:** The behavior of **`round()`** for floats can be surprising. Notice **`round(2.675, 2) `** gives **`2.67`** instead of the expected **`2.68`**. This is not a bug: it's a result of the fact that most decimal fractions can't be represented exactly as a float.
When the decimal **`2.675`** is converted to a binary floating-point number, it's again replaced with a binary approximation, whose exact value is:
```python
2.67499999999999982236431605997495353221893310546875
```
Due to this, it is rounded down to 2.67.

If you're in a situation where this precision is needed, consider using the **`decimal`** module, which is designed for floating-point arithmetic:

```python
# Example 3:

from decimal import Decimal

# normal float
num = 2.675
print(round(num, 2))

# using decimal.Decimal (passed float as string for precision)
num = Decimal('2.675')
print(round(num, 2))
```

**Output:**
```text
2.67
2.68
```

---

## 📘 Python Set()
*Source: `4. Python Functions/57. Python set().ipynb`*

# Python `set()`

The **`set()`** builtin creates a set in Python.

**Syntax**:

```python
set(iterable)
```

## `set()` Parameters

**`set()`** takes a single optional parameter:

* **iterable (optional)** - a sequence (**string**, **tuple**, etc.) or collection (**set**, **dictionary**, etc.) or an iterator object to be converted into a set.

## Return Value from `set()`

**`set()`** returns:

* an empty set if no parameters are passed
* a set constructed from the given **iterable** parameter

```python
# Example 1: Create sets from string, tuple, list, and range

# empty set
print(set())

# from string
print(set('Python'))

# from tuple
print(set(('a', 'e', 'i', 'o', 'u')))

# from list
print(set(['a', 'e', 'i', 'o', 'u']))

# from range
print(set(range(5)))
```

**Output:**
```text
set()
{'P', 't', 'o', 'y', 'h', 'n'}
{'e', 'u', 'o', 'a', 'i'}
{'e', 'u', 'o', 'a', 'i'}
{0, 1, 2, 3, 4}
```

>**Note:** We cannot create empty sets using **`{ }`** syntax as it creates an empty dictionary. To create an empty set, we use **`set()`**.

```python
# Example 2: Create sets from another set, dictionary and frozen set

# from set
print(set({'a', 'e', 'i', 'o', 'u'}))

# from dictionary
print(set({'a':1, 'e': 2, 'i':3, 'o':4, 'u':5}))

# from frozen set
frozen_set = frozenset(('a', 'e', 'i', 'o', 'u'))
print(set(frozen_set))
```

**Output:**
```text
{'e', 'i', 'u', 'o', 'a'}
{'e', 'i', 'u', 'o', 'a'}
{'e', 'i', 'u', 'o', 'a'}
```

```python
# Example 3: Create set() for a custom iterable object

class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

# print_num is an iterable
print_num = PrintNumber(5)

# creating a set
print(set(print_num))
```

**Output:**
```text
{1, 2, 3, 4, 5}
```

---

## 📘 Python Setattr()
*Source: `4. Python Functions/58. Python setattr().ipynb`*

# Python `setattr()`

The **`setattr()`** function sets the value of the attribute of an object.

**Syntax**:

```python
setattr(object, name, value)
```

If you want to get the attribute of an object, use **getattr()**.

## `setattr()` Parameters

The **`setattr()`** function takes three parameters:

* **object** - object whose attribute has to be set
* **name** - attribute name
* **value** - value given to the attribute

## Return Value from `setattr()`

The **`setattr()`** method doesn't return anything; returns **`None`**.

```python
# Example 1: How setattr() works in Python?

class Person:
    name = 'Adam'
    
p = Person()
print('Before modification:', p.name)

# setting name to 'John'
setattr(p, 'name', 'John')

print('After modification:', p.name)
```

**Output:**
```text
Before modification: Adam
After modification: John
```

```python
# Example 2: When the attribute is not found in setattr()

# If the attribute is not found, setattr() creates a new attribute an assigns value to it. 
# However, this is only possible if the object implements the __dict__() method.

# You can check all the attributes of an object by using the dir() function.

class Person:
    name = 'Adam'
    
p = Person()

# setting attribute name to John
setattr(p, 'name', 'John')
print('Name is:', p.name)

# setting an attribute not present in Person
setattr(p, 'age', 23)
print('Age is:', p.age)
```

**Output:**
```text
Name is: John
Age is: 23
```

In above example, You can check all the attributes of an object by using the **dir() function**.

---

## 📘 Python Slice()
*Source: `4. Python Functions/59. Python slice().ipynb`*

# Python `slice()`

The **`slice()`** function returns a slice object that can use used to slice strings, lists, tuple etc.

The slice object is used to slice a given sequence (**string**, **bytes**, **tuple**, **list** or **range**) or any object which supports sequence protocol (implements **`__getitem__()`** and **`__len__()`** method).

**Syntax**:

```python
slice(start, stop, step)
```

## `slice()` Parameters

**`slice()`** can take three parameters:

* **start (optional)** - Starting integer where the slicing of the object starts. Default to **`None`** if not provided.
* **stop** - Integer until which the slicing takes place. The slicing stops at index **stop -1 (last element)**.
* **step (optional)** - Integer value which determines the increment between each index for slicing. Defaults to **`None`** if not provided.

```python
# Example 1: Create a slice object for slicing

# contains indices (0, 1, 2)
result1 = slice(3)
print(result1)

# contains indices (1, 3)
result2 = slice(1, 5, 2)
print(slice(1, 5, 2))
```

**Output:**
```text
slice(None, 3, None)
slice(1, 5, 2)
```

Here, **`result1`** and **`result2`** are slice objects.

Now we know about slice objects, let's see how we can get substring, sub-list, sub-tuple, etc. from slice objects.

```python
# Example 2: Get substring using slice object

# Program to get a substring from the given string 

py_string = 'Python'

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3) 
print(py_string[slice_object])  # Pyt

# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6, 2)
print(py_string[slice_object])   # yhn
```

**Output:**
```text
Pyt
yhn
```

```python
# Example 3: Get substring using negative index

py_string = 'Python'

# start = -1, stop = -4, step = -1
# contains indices -1, -2 and -3
slice_object = slice(-1, -4, -1)

print(py_string[slice_object])   # noh
```

**Output:**
```text
noh
```

```python
# Example 4: Get sublist and sub-tuple

py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices 0, 1 and 2
slice_object = slice(3)
print(py_list[slice_object]) # ['P', 'y', 't']

# contains indices 1 and 3
slice_object = slice(1, 5, 2)
print(py_tuple[slice_object]) # ('y', 'h')
```

**Output:**
```text
['P', 'y', 't']
('y', 'h')
```

```python
# Example 5: Get sublist and sub-tuple using negative index

py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices -1, -2 and -3
slice_object = slice(-1, -4, -1) 
print(py_list[slice_object])  # ['n', 'o', 'h']

# contains indices -1 and -3
slice_object = slice(-1, -5, -2)
print(py_tuple[slice_object]) # ('n', 'h')
```

**Output:**
```text
['n', 'o', 'h']
('n', 'h')
```

```python
# Example 6: Using Indexing Syntax for Slicing

# The slice object can be substituted with the indexing syntax in Python.

#You can alternately use the following syntax for slicing:

#obj[start:stop:step]
#For example,

py_string = 'Python'

# contains indices 0, 1 and 2
print(py_string[0:3])  # Pyt

# contains indices 1 and 3
print(py_string[1:5:2]) # yh
```

**Output:**
```text
Pyt
yh
```

---

## 📘 Python Sorted()
*Source: `4. Python Functions/60. Python sorted().ipynb`*

# Python `sorted()`

The **`sorted()`** function returns a sorted list from the items in an iterable.

The **`sorted()`** function sorts the elements of a given iterable in a specific order (either **ascending** or **descending**) and returns the sorted iterable as a list.

**Syntax**:

```python
sorted(iterable, key=None, reverse=False)
```

## `sorted()` Parameters

**`sorted()`** can take a maximum of three parameters:

* **iterable** - A sequence (**string**, **tuple**, **list**) or collection (**set**, **dictionary**, **frozen set**) or any other iterator.
* **reverse (Optional)** - If **`True`**, the sorted list is reversed (or sorted in descending order). Defaults to **`False`** if not provided.
* **key (Optional)** - A function that serves as a key for the sort comparison. Defaults to **`None`**.

```python
# Example 1: Sort string, list, and tuple

# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list))

# string
py_string = 'Python'
print(sorted(py_string))

# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))
```

**Output:**
```text
['a', 'e', 'i', 'o', 'u']
['P', 'h', 'n', 'o', 't', 'y']
['a', 'e', 'i', 'o', 'u']
```

Notice that in all cases that a sorted list is returned.

>**Note:** A list also has the **sort()** method which performs the same way as **`sorted()`**. The only difference is that the **`sort()`** method doesn't return any value and changes the original list.

```python
# Example 2: Sort in descending order

# The sorted() function accepts a reverse parameter as an optional argument.

#Setting reverse = True sorts the iterable in the descending order.

# set
py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))

# dictionary
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(py_dict, reverse=True))

# frozen set
frozen_set = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(frozen_set, reverse=True))
```

**Output:**
```text
['u', 'o', 'i', 'e', 'a']
['u', 'o', 'i', 'e', 'a']
['u', 'o', 'i', 'e', 'a']
```

### key Parameter in Python `sorted()` function

If you want your own implementation for sorting, **`sorted()`** also accepts a **`key`** function as an optional parameter.

Based on the returned value of the key function, you can sort the given iterable.

```python
sorted(iterable, key=len)
```

Here, **`len()`** is Python's in-built function to count the length of an object.

The list is sorted based on the length of the element, from the lowest count to highest.

```python
# Example 3: Sort the list using sorted() having a key function

# take the second element for sort
def take_second(elem):
    return elem[1]


# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sorted_list = sorted(random, key=take_second)

# print list
print('Sorted list:', sorted_list)
```

**Output:**
```text
Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]
```

```python
# Example 4: Sorting with multiple keys

# Let us suppose that we have the following list:

# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100, Age)

participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]
```

We want to sort the list in such a way that the student with the highest marks is in the beginning. In case the students have equal marks, they must be sorted so that the younger participant comes first.

We can achieve this type of sorting with multiple keys by returning tuple instead of a number.

Two tuples can be compared by comparing their elements starting from first. If there is a tie (elements are equal), the second element is compared, and so on.

```python
(1,3) > (1, 4)
```

**Output:**
```text
False
```

```python
(1, 4) < (2,2)
```

**Output:**
```text
True
```

```python
(1, 4, 1) < (2, 1)
```

**Output:**
```text
True
```

```python
# Let's use this logic to build our sorting logic.

# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]


def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)


sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)
```

**Output:**
```text
[('Jimmy', 90, 22), ('Terence', 75, 12), ('David', 75, 20), ('Alison', 50, 18), ('John', 45, 12)]
```

Since the sorting logic function is small and fits in one line, **`lambda`** function is used inside **`key`** rather than passing a separate function name.

The above program can be written using the **`lambda`** function in the following way:

```python
# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))
print(sorted_list)
```

**Output:**
```text
[('Jimmy', 90, 22), ('Terence', 75, 12), ('David', 75, 20), ('Alison', 50, 18), ('John', 45, 12)]
```

---

## 📘 Python Str()
*Source: `4. Python Functions/61. Python str().ipynb`*

# Python `str()`

The **`str()`** function returns the string version of the given object.

**Syntax**:

```python
str(object, encoding='utf-8', errors='strict')
```

## `str()` Parameters

**`str()`** method takes three parameters:

* **object** - The **`object`** whose string representation is to be returned. If not provided, returns the empty string
* **encoding** - Encoding of the given object. Defaults of **UTF-8** when not provided.
* **errors** - Response when decoding fails. Defaults to **`'strict'`**.

There are six types of **`errors`**:

* **strict** - default response which raises a **`UnicodeDecodeError`** exception on failure
* **ignore** - ignores the unencodable Unicode from the result
* **replace** - replaces the unencodable Unicode to a question mark
* **xmlcharrefreplace** - inserts XML character reference instead of unencodable Unicode
* **backslashreplace** - inserts a **`\uNNNN`** espace sequence instead of unencodable Unicode
* **namereplace** - inserts a **`\N{...}`** escape sequence instead of unencodable Unicode

## Return value from `str()`

The **`str()`** method returns a string, which is considered an informal or nicely printable representation of the given object.

```python
# Example 1: Convert to String

# If encoding and errors parameter isn't provided, str() internally calls the __str__() method 
# of an object.

# If it cannot find the __str__() method, it instead calls repr(obj).

result = str(10)
print(result)
```

**Output:**
```text
10
```

If it cannot find the **`__str__()`** method, it instead calls **repr(obj)**.

>**Note:** The result variable will contain a string.

Also try these commands on the Python console.

```python
str('Adam')
```

**Output:**
```text
'Adam'
```

```python
str(b'Python!')
```

**Output:**
```text
"b'Python!'"
```

## `str()` with bytes

If **`encoding`** and **`errors`** parameter is provided, the first parameter, **object**, should be a **bytes-like-object** (**bytes** or **bytearray**).

If the object is **bytes or bytearray**, **`str()`** internally calls **`bytes.decode(encoding, errors)`**.

Otherwise, it gets the bytes object in the buffer before calling the **`decode()`** method.

```python
# Example 2: 

# bytes
b = bytes('pythön', encoding='utf-8')

print(str(b, encoding='ascii', errors='ignore'))
```

**Output:**
```text
pythn
```

Here, the character **`'ö'`** cannot be decoded by ASCII. Hence, it should give an error. However, we have set the **`errors ='ignore'`**. Hence, Python ignores the character which cannot be decoded by **`str()`**.

---

## 📘 Python Sum()
*Source: `4. Python Functions/62. Python sum().ipynb`*

# Python `sum()`

The **`sum()`** function adds the items of an iterable and returns the sum.

**Syntax**:

```python
sum(iterable, start)
```

The **`sum()`** function adds **`start`** and items of the given **`iterable`** from left to right.

## `sum()` Parameters

* **iterable** - iterable (list, tuple, dict, etc). The items of the iterable should be numbers.
* **start (optional)** - this value is added to the sum of items of the iterable. The default value of **`start`** is 0 (if omitted)

## Return value from `sum()`

**`sum()`** returns the sum of **`start`** and items of the given **`iterable`**.

```python
# Example: Working of Python sum()

numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbers_sum = sum(numbers)
print(numbers_sum)

# start = 10
numbers_sum = sum(numbers, 10)
print(numbers_sum)
```

**Output:**
```text
4.5
14.5
```

If you need to add floating-point numbers with exact precision, then you should use **`math.fsum(iterable)`** instead.

If you need to concatenate items of the given iterable (items must be strings), then you can use the **`join()`** method.

```python
'string'.join(sequence)
```

---

## 📘 Python Tuple() Function
*Source: `4. Python Functions/63. Python tuple() Function.ipynb`*

# Python `tuple()`

The **`tuple()`** builtin can be used to create tuples in Python.

In Python, a tuple is an immutable sequence type. One of the ways of creating tuple is by using the **`tuple()`** construct.

**Syntax**:

```python
tuple(iterable)
```

## `tuple()` Parameters

* **iterable (optional)** - an iterable (list, range, etc.) or an iterator object

If the **`iterable`** is not passed to **`tuple()`**, the function returns an empty tuple.

```python
# Example 1: Create tuples using tuple()

t1 = tuple()
print('t1 =', t1)

# creating a tuple from a list
t2 = tuple([1, 4, 6])
print('t2 =', t2)

# creating a tuple from a string
t1 = tuple('Python')
print('t1 =',t1)

# creating a tuple from a dictionary
t1 = tuple({1: 'one', 2: 'two'})
print('t1 =',t1)
```

**Output:**
```text
t1 = ()
t2 = (1, 4, 6)
t1 = ('P', 'y', 't', 'h', 'o', 'n')
t1 = (1, 2)
```

---

## 📘 Python Type()
*Source: `4. Python Functions/64. Python type().ipynb`*

# Python `type()`

The **`type()`** function either returns the type of the object or returns a new type object based on the arguments passed.

**Syntax**:

```python
type(object)
type(name, bases, dict)
```

## `type()` With a Single Object Parameter

If a single **`object`** is passed to **`type()`**, the function returns its type.

```python
# Example 1: Get Type of an Object

numbers_list = [1, 2]
print(type(numbers_list))

numbers_dict = {1: 'one', 2: 'two'}
print(type(numbers_dict))

class Foo:
    a = 0

foo = Foo()
print(type(foo))
```

If you need to check the type of an object, it is better to use the **Python isinstance() function** instead. It's because the **`isinstance()` function** also checks if the given object is an instance of the subclass.

## `type()` With name, bases and dict Parameters

If three parameters are passed to **`type()`**, it returns a new type object.

The three parameters are:

| Parameter | Description |
|:----| :--- |
| **name** | **a class name; becomes the `__name__` attribute** |
| **name** | **a tuple that itemizes the base class; becomes the `__bases__` attribute** |
| **name** | **a dictionary which is the namespace containing definitions for the class body; becomes the `__dict__` attribute** |

```python
# Example 2: Create a type object

o1 = type('X', (object,), dict(a='Foo', b=12))

print(type(o1))
print(vars(o1))

class test:
    a = 'Foo'
    b = 12
  
o2 = type('Y', (test,), dict(a='Foo', b=12))
print(type(o2))
print(vars(o2))
```

In the program, we have used the **Python vars() function** which returns the **`__dict__`** attribute. **`__dict__`** is used to store object's writable attributes.

You can easily change these attributes if necessary. For example, if you need to change the **`__name__`** attribute of **`o1`** to **`'Z'`**, use:

```python
o1.__name = 'Z'
```

---

## 📘 Python Vars()
*Source: `4. Python Functions/65. Python vars().ipynb`*

# Python `vars()`

The **`vars()`** function returns the **`__dict__`** attribute of the given object.

**Syntax**:

```python
vars(object)
```

## `vars()` Parameter

**`vars()`** takes a maximum of one parameter.

* **object** - can be module, class, instance, or any object having the **`__dict__`** attribute.

## Return Value from `vars()`

* **`vars()`** returns the **`__dict__`** attribute of the given object.
* If the object passed to **`vars()`** doesn't have the **`__dict__`** attribute, it raises a TypeError exception.
* If no argument is passed to **`vars()`**, this function acts like **locals() function**.

>**Note:** **`__dict__`** is a dictionary or a mapping object. It stores object's (writable) attributes.

```python
# Example: Working of Python vars()

class Foo:
    def __init__(self, a = 5, b = 10):
        self.a = a
        self.b = b
object = Foo()
print(vars(object))
```

**Output:**
```text
{'a': 5, 'b': 10}
```

Also, run these statements on Python shell:

```python
vars(list)
```

**Output:**
```text
mappingproxy({'__repr__': <slot wrapper '__repr__' of 'list' objects>,
              '__hash__': None,
              '__getattribute__': <slot wrapper '__getattribute__' of 'list' objects>,
              '__lt__': <slot wrapper '__lt__' of 'list' objects>,
              '__le__': <slot wrapper '__le__' of 'list' objects>,
              '__eq__': <slot wrapper '__eq__' of 'list' objects>,
              '__ne__': <slot wrapper '__ne__' of 'list' objects>,
              '__gt__': <slot wrapper '__gt__' of 'list' objects>,
              '__ge__': <slot wrapper '__ge__' of 'list' objects>,
              '__iter__': <slot wrapper '__iter__' of 'list' objects>,
              '__init__': <slot wrapper '__init__' of 'list' objects>,
              '__len__': <slot wrapper '__len__' of 'list' objects>,
              '__getitem__': <method '__getitem__' of 'list' objects>,
              '__setitem__': <slot wrapper '__setitem__' of 'list' objects>,
              '__delitem__': <slot wrapper '__del
... [Output truncated for brevity]
```

```python
vars(str)
```

**Output:**
```text
mappingproxy({'__repr__': <slot wrapper '__repr__' of 'str' objects>,
              '__hash__': <slot wrapper '__hash__' of 'str' objects>,
              '__str__': <slot wrapper '__str__' of 'str' objects>,
              '__getattribute__': <slot wrapper '__getattribute__' of 'str' objects>,
              '__lt__': <slot wrapper '__lt__' of 'str' objects>,
              '__le__': <slot wrapper '__le__' of 'str' objects>,
              '__eq__': <slot wrapper '__eq__' of 'str' objects>,
              '__ne__': <slot wrapper '__ne__' of 'str' objects>,
              '__gt__': <slot wrapper '__gt__' of 'str' objects>,
              '__ge__': <slot wrapper '__ge__' of 'str' objects>,
              '__iter__': <slot wrapper '__iter__' of 'str' objects>,
              '__mod__': <slot wrapper '__mod__' of 'str' objects>,
              '__rmod__': <slot wrapper '__rmod__' of 'str' objects>,
              '__len__': <slot wrapper '__len__' of 'str' objects>,
              '__getitem__': <slot
... [Output truncated for brevity]
```

```python
vars(dict)
```

**Output:**
```text
mappingproxy({'__repr__': <slot wrapper '__repr__' of 'dict' objects>,
              '__hash__': None,
              '__getattribute__': <slot wrapper '__getattribute__' of 'dict' objects>,
              '__lt__': <slot wrapper '__lt__' of 'dict' objects>,
              '__le__': <slot wrapper '__le__' of 'dict' objects>,
              '__eq__': <slot wrapper '__eq__' of 'dict' objects>,
              '__ne__': <slot wrapper '__ne__' of 'dict' objects>,
              '__gt__': <slot wrapper '__gt__' of 'dict' objects>,
              '__ge__': <slot wrapper '__ge__' of 'dict' objects>,
              '__iter__': <slot wrapper '__iter__' of 'dict' objects>,
              '__init__': <slot wrapper '__init__' of 'dict' objects>,
              '__len__': <slot wrapper '__len__' of 'dict' objects>,
              '__getitem__': <method '__getitem__' of 'dict' objects>,
              '__setitem__': <slot wrapper '__setitem__' of 'dict' objects>,
              '__delitem__': <slot wrapper '__del
... [Output truncated for brevity]
```

---

## 📘 Python Zip()
*Source: `4. Python Functions/66. Python zip().ipynb`*

# Python `zip()`

The **`zip()`** function takes iterables (can be zero or more), aggregates them in a tuple, and return it.

**Syntax**:

```python
zip(*iterables)
```

## `zip()` Parameter

| Parameter | Description |
|:----| :--- |
| **`iterables`** | **can be built-in iterables (like: list, string, dict), or user-defined iterables** |

## Return Value from `zip()`

The **`zip()`** function returns an iterator of tuples based on the iterable objects.

* If we do not pass any parameter, **`zip()`** returns an empty iterator
* If a single iterable is passed, **`zip()`** returns an iterator of tuples with each tuple having only one element.
* If multiple iterables are passed, **`zip()`** returns an iterator of tuples with each tuple having elements from all the iterables.

Suppose, two iterables are passed to **`zip()`**; one iterable containing three and other containing five elements. Then, the returned iterator will contain three tuples. It's because iterator stops when the shortest iterable is exhausted.

```python
# Example 1: Python zip()

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting itertor to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting itertor to set
result_set = set(result)
print(result_set)
```

**Output:**
```text
[]
{(2, 'two'), (3, 'three'), (1, 'one')}
```

```python
# Example 2: Different number of iterable elements

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)
```

**Output:**
```text
{(3, 'THREE'), (2, 'TWO'), (1, 'ONE')}
{(2, 'two', 'TWO'), (1, 'one', 'ONE')}
```

The **`*`** operator can be used in conjunction with **`zip()`** to unzip the list.

```python
zip(*zippedList)
```

```python
# Example 3: Unzipping the Value Using zip()

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v =  zip(*result_list)
print('c =', c)
print('v =', v)
```

**Output:**
```text
[('x', 3), ('y', 4), ('z', 5)]
c = ('x', 'y', 'z')
v = (3, 4, 5)
```

---

## 📘 Python Super()
*Source: `4. Python Functions/68. Python super().ipynb`*

# Python `super()`

The **`super()`** builtin returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.

In Python, **`super()`** has two major use cases:

* Allows us to avoid using the base class name explicitly
* Working with Multiple Inheritance

```python
# Example 1: super() with Single Inheritance

# In the case of single inheritance, it allows us to refer base class by super().

class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')
    
d1 = Dog()
```

**Output:**
```text
Dog has four legs.
Dog is a warm-blooded animal.
```

Here, we called the **`__init__()`** method of the **`Mammal`** class (from the **`Dog`** class) using code

```python
super().__init__('Dog')
```

instead of

```python
Mammal.__init__(self, 'Dog')
```

Since we do not need to specify the name of the base class when we call its members, we can easily change the base class name (if we need to).

```python
# changing base class to CanidaeFamily
class Dog(CanidaeFamily):
    def __init__(self):
        print('Dog has four legs.')

    # no need to change this
    super().__init__('Dog')
```

The **`super()`** builtin returns a proxy object, a substitute object that can call methods of the base class via delegation. This is called indirection (ability to reference base object with **`super()`**)

Since the indirection is computed at the runtime, we can use different base classes at different times (if we need to).

```python
# Example 2: super() with Multiple Inheritance

class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.');

class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')
```

**Output:**
```text
Dog has 4 legs.
Dog can't swim.
Dog can't fly.
Dog is a warm-blooded animal.
Dog is an animal.

Bat can't swim.
Bat is a warm-blooded animal.
Bat is an animal.
```

## Method Resolution Order (MRO)

**Method Resolution Order (MRO)** is the order in which methods should be inherited in the presence of multiple inheritance. You can view the MRO by using the **`__mro__`** attribute.

```python
>>> Dog.__mro__
(<class 'Dog'>, 
<class 'NonMarineMammal'>, 
<class 'NonWingedMammal'>, 
<class 'Mammal'>, 
<class 'Animal'>, 
<class 'object'>)
```

Here is how MRO works:

* A method in the derived calls is always called before the method of the base class. In our example, **`Dog`** class is called before **`NonMarineMammal`** or **`NoneWingedMammal`**. These two classes are called before **`Mammal`**, which is called before **`Animal`**, and **`Animal`** class is called before the **`object`**.

* If there are multiple parents like **`Dog(NonMarineMammal, NonWingedMammal)`**, methods of **`NonMarineMammal`** is invoked first because it appears first.

---

## 📘 Equal1
*Source: `4. Python Functions/equal1.ipynb`*

```python
# Python Module example

#function definition
def equal(a, b):
    if(a == b):
        return True
```

---

## 📘 Fibo1
*Source: `4. Python Functions/fibo1.ipynb`*

```python
# Fibonacci numbers module
def fib(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
```

---

## 📘 Greet1
*Source: `4. Python Functions/greet1.ipynb`*

```python
print("Welcome to Xalt Analytics")
```

**Output:**
```text
Welcome to Xalt Analytics
```

---

## 📘 Main1
*Source: `4. Python Functions/main1.ipynb`*

```python
import config
import update

print(config.a)
print(config.b)
```

**Output:**
```text
10
alphabet
```

---

## 📘 Main
*Source: `4. Python Functions/main.ipynb`*

```python
import import_ipynb

import test1           # importing module test1.ipynb
from test1 import fun  # importing function "fun" here
fun()
```

**Output:**
```text
importing Jupyter notebook from test1.ipynb
something here inside fun()
```

```python
import test  # importing module test.py
from test import fun  # importing function "fun" here
fun()

#x = test.fun()
#print("x=",x)
```

**Output:**
```text
something here inside fun()
```

```python
import fibo  # importing module fibo.py
from fibo import fib
print(fib(100))
```

**Output:**
```text
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

```python
import import_ipynb

import fibo1  # importing module fibo1.ipynb
from fibo1 import fib
print(fib(100))
```

**Output:**
```text
importing Jupyter notebook from fibo1.ipynb
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

```python
from equal import *  # '*' means import all the functions in the file equal.py
a, b = 10, 10
print(equal(a, b))
```

**Output:**
```text
True
```

```python
import import_ipynb

from equal1 import *  # '*' means import all the functions in the file equal.ipynb
a, b = 10, 10
print(equal(a, b))
```

**Output:**
```text
importing Jupyter notebook from equal1.ipynb
True
```

In Python, each and every built-in module has a large number of predefined functions to perform specific tasks. For instance, Python has a built-in module named **`operator`**, inside which the function called **`eq()`** is defined. This function returns the boolean value of **`True`** if the given two input values are equal. Else, returns **`False`**.

So now, we can make use of this operator module in our **`main()`** program to check if two numbers are equal. This means we would no longer need that **`equal.py`** module.

```python
#main function
from operator import *
a, b = 10, 10
print(eq(a, b))
```

**Output:**
```text
True
```

```python
import time
from importlib import reload

# load 1st time
import greet   # importing module greet.py
time.sleep(15)
# reload 
reload(greet)
time.sleep(15) 

 # reload again  
reload(greet)
print("This is test file..")
```

**Output:**
```text
Welcome to Dr Parmar's Python4DataScience class
Welcome to Dr Parmar's Python4DataScience class
Welcome to Dr Parmar's Python4DataScience class
This is test file..
```

```python
import import_ipynb
import time
from importlib import reload

# load 1st time
import greet   # importing module greet.ipynb
time.sleep(15)
# reload 
reload(greet)
time.sleep(15) 

 # reload again  
reload(greet)
print("This is test file..")
```

**Output:**
```text
Welcome to Dr Parmar's Python4DataScience class
Welcome to Dr Parmar's Python4DataScience class
This is test file..
```

---

## 📘 Python Docstrings
*Source: `4. Python Functions/Python Docstrings.ipynb`*

# Python Docstrings

In this class, we will learn about Python docstrings. More specifically, we will learn how and why docstrings are used with the help of examples.

Python docstrings are the string literals that appear right after the definition of a function, method, class, or module. For example:

```python
# Example 1: Docstrings

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
```

Here, the string literal:
```python
 '''Takes in a number n, returns the square of n'''
```

inside the triple quotation marks is the **docstring** of the function **`square()`** as it appears right after its definition.

>**Note:** We can also use triple **`'''`** quotations to create docstrings.

## Python Comments vs Docstrings

### Python Comments

Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

In Python, we use the hash symbol **`#`** to write a single-line comment. For example,

```python
# Example 1: Program to print "Hello World"

print("Hello World")
```

**Output:**
```text
Hello World
```

### Python Comments Using Strings

If we do not assign strings to any variable, they act as comments. For example,

```python
# Example 1:

"I am a single-line comment"

'''
I am a
multi-line comment!
'''

print("Hello World")
```

**Output:**
```text
Hello World
```

>**Note:** We use triple quotation marks for multi-line strings.

### Python docstrings

As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 

**1. They are used to document our code**.

We can access these docstrings using the **`__doc__`** attribute.

## Python `__doc__` attribute

Whenever string literals are present just after the definition of a function, module, class or a method, they are associated with the object as their **`__doc__`** attribute. We can later use this attribute to retrieve this docstring.

```python
# Example 1: Printing docstring

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)
```

**Output:**
```text
Takes in a number n, returns the square of n
```

Here, the documentation of our **`square()`** function can be accessed using the **`__doc__`** attribute.

Now, let's look at docstrings for the built-in function **`print()`**:

```python
# Example 2: Docstrings for the built-in `print()` function

print(print.__doc__)
```

**Output:**
```text
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
```

Here, we can see that the documentation of the **`print()`** function is present as the **`__doc__`** attribute of this function.

## Single-line docstrings in Python

Single line docstrings are the documents that fit in one line.

**Standard conventions to write single-line docstrings:**

* Even though they are single-lined, we still use the triple quotes around these docstrings as they can be expanded easily later.
* The closing quotes are on the same line as the opening quotes.
* There's no blank line either before or after the docstring.
* They should not be descriptive, rather they must follow "Do this, return that" structure ending with a period.

Let's take an example.

```python
# Example 1: Write single-line docstrings for a function
    
def multiplier(a, b):
    """Takes in two numbers, returns their product."""
    return a*b
```

```python
# Example 2:

def factorial(x):
    """This function returns the factorial of a given number."""
    return x

# access doc string
print(factorial.__doc__)
```

**Output:**
```text
This function returns the factorial of a given number.
```

```python
# Example 3:

# pass function name to help() function
print(help(factorial))
```

**Output:**
```text
Help on function factorial in module __main__:

factorial(x)
    This function returns the factorial of a given number.

None
```

## Multi-line Docstrings in Python

Multi-line docstrings consist of a summary line just like a one-line docstring, followed by a blank line, followed by a more elaborate description.

The PEP 257 document provides the standard conventions to write multi-line docstrings for various objects.

Some have been listed below:

### 1. Docstrings for Python Modules

* The docstrings for Python Modules should list all the available classes, functions, objects and exceptions that are imported when the module is imported.
* They should also have a one-line summary for each item.

They are written at the beginning of the Python file.

Let's look at the docstrings for the builtin module in Python called pickle.

```python
# Example 1: Docstrings of Python module

import pickle
print(pickle.__doc__)
```

**Output:**
```text
Create portable serialized representations of Python objects.

See module copyreg for a mechanism for registering custom picklers.
See module pickletools source for extensive comments.

Classes:

    Pickler
    Unpickler

Functions:

    dump(object, file)
    dumps(object) -> string
    load(file) -> object
    loads(string) -> object

Misc variables:

    __version__
    format_version
    compatible_formats
```

Here, we can see that the docstring written at the beginning of the **pickle.py** module file can be accessed as its docstring.

### 2. Docstrings for Python Functions

* The docstring for a function or method should summarize its behavior and document its arguments and return values.
* It should also list all the exceptions that can be raised and other optional arguments.

```python
# Example 1: Docstrings for Python functions

def add_binary(a, b):
    '''
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    '''
    binary_sum = bin(a+b)[2:]
    return binary_sum


print(add_binary.__doc__)
```

**Output:**
```text
Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
```

As you can see, we have included a short description of what the function does, the parameter it takes in and the value it returns. The string literal is embedded to the function **`add_binary`** as its **`__doc__`** attribute.

```python
# Example 2:

def any_fun(parameter1):
    """             
   Description of function
                 
   Arguments:   
   parameter1(int):Description of parameter1
                 
   Returns:      
   int value     
    """ 

print(any_fun.__doc__)
```

**Output:**
```text
Description of function
                 
   Arguments:   
   parameter1(int):Description of parameter1
                 
   Returns:      
   int value
```

### 3. Docstrings for Python Classes

The docstrings for classes should summarize its behavior and list the public methods and instance variables.
The subclasses, constructors, and methods should each have their own docstrings.

```python
# Example 1: Docstrings for Python class

# Suppose we have a Person.py file with the following code:

class Person:
    """
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, name, surname, age):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            name : str
                first name of the person
            surname : str
                family name of the person
            age : int
                age of the person
        """

        self.name = name
        self.surname = surname
        self.age = age

    def info(self, additional=""):
        """
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """

        print(f'My name is {self.name} {self.surname}. I am {self.age} years old.' + additional)
```

Here, we can use the following code to access only the docstrings of the **`Person`** class:

```python
print(Person.__doc__)
```

**Output:**
```text
A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
```

## Using the `help()` Function for Docstrings

We can also use the **`help()`** function to read the docstrings associated with various objects.

```python
# Example 1: Read Docstrings with the `help()` function

# We can use the help() function on the class Person in Example as:

help(Person)
```

**Output:**
```text
Help on class Person in module __main__:

class Person(builtins.object)
 |  Person(name, surname, age)
 |  
 |  A class to represent a person.
 |  
 |  ...
 |  
 |  Attributes
 |  ----------
 |  name : str
 |      first name of the person
 |  surname : str
 |      family name of the person
 |  age : int
 |      age of the person
 |  
 |  Methods
 |  -------
 |  info(additional=""):
 |      Prints the person's name and age.
 |  
 |  Methods defined here:
 |  
 |  __init__(self, name, surname, age)
 |      Constructs all the necessary attributes for the person object.
 |      
 |      Parameters
 |      ----------
 |          name : str
 |              first name of the person
 |          surname : str
 |              family name of the person
 |          age : int
 |              age of the person
 |  
 |  info(self, additional='')
 |      Prints the person's name and age.
 |      
 |      If the argument 'additional' is passed, then it is appended after the main info.
 |      
 |      
... [Output truncated for brevity]
```

Here, we can see that the **`help()`** function retrieves the docstrings of the **`Person`** class along with the methods associated with that class.

### 4. Docstrings for Python Scripts

* The docstrings for Python script should document the script's functions and command-line syntax as a usable message.
* It should serve as a quick reference to all the functions and arguments.

### 5. Docstrings for Python Packages

The docstrings for a Python package is written in the package's **`__init__.py`** file.

* It should contain all the available modules and sub-packages exported by the package.

## Docstring Formats

We can write docstring in many formats like the reStructured text (reST) format, Google format or the NumPy documentation format. To learn more, visit **[Popular Docstring Formats](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)**

We can also generate documentation from docstrings using tools like Sphinx. To learn more, visit **[Official Sphinx Documentation](https://www.sphinx-doc.org/en/master/)**

---

## 📘 Python User Defined Functions
*Source: `4. Python Functions/Python User defined Functions.ipynb`*

# Python User-defined Functions

In this class, you will find the advantages of using user-defined functions and best practices to follow.

## What are user-defined functions in Python?

Functions that we define ourselves to do certain specific task are referred as user-defined functions. The way in which we define and call **functions in Python** are already discussed.

Functions that readily come with Python are called built-in functions. If we use functions written by others in the form of library, it can be termed as library functions.

All the other functions that we write on our own fall under user-defined functions. So, our user-defined function could be a library function to someone else.

## Advantages of user-defined functions

1. User-defined functions help to decompose a large program into small segments which makes program easy to understand, maintain and debug.
2. If repeated code occurs in a program. Function can be used to include those codes and execute when needed by calling that function.
3. Programmars working on large project can divide the workload by making different functions.

```python
# Example 1: illustrate the use of user-defined functions

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

def my_addition(num1,num2):
    sum = float(num1) + float(num2)
    return sum

#num1 = 9.3
#num2 = 6.9

print("The sum is", my_addition(num1, num2))
```

**Output:**
```text
Enter first number: 9.3
Enter second number: 6.9
The sum is 16.200000000000003
```

**Explanation:**

Here, we have defined the function **`my_addition()`** which adds two numbers and returns the result.

This is our user-defined function. We could have multiplied the two numbers inside our function (it's all up to us). But this operation would not be consistent with the name of the function. It would create ambiguity.

It is always a good idea to name functions according to the task they perform.

In the above example, **print** is a **built-in function in Python**.

---

## 📘 Test
*Source: `4. Python Functions/test.ipynb`*

```python
def fun():
    print("something here inside fun()")
```

---
