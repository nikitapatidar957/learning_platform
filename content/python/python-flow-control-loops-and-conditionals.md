# Python Flow Control: Conditionals, Loops & Control Statements

Detailed explanations and code implementations of if, if-else, if-elif-else, nested if structures, for loops, while loops, and loop control statements (break, continue, pass).

---

# 03_Python_Flow_Control

## Introduction 👋

The control flow statements are an essential part of the Python programming language.

A control flow statement is a block of programming that analyses variables and chooses a direction in which to go based on given parameters. In simple sentence, a control structure is just a decision that the computer makes. So, it is the basic decision-making process in programming and flow of control determines how a computer program will respond when given certain conditions and parameters. It determines the  order in which the program’s code executes.

They are **decision making statements** that allow the program to take the decision as which statement should be executed next.

Decision Making statements are used when we want a set of instructions should be executed in one situation and different instructions should be executed in another situation .Decision making can be implemented in python using:

&#8594; **`if`** statements

&#8594; **`else`** statements

&#8594; **`elif`** statements

&#8594; **`for`** loops

&#8594; **`while`** loops

&#8594; **`break`** statement

&#8594; **`control`** statement

&#8594; **`pass`** statement

---

## Table of contents 📋

| **No.** | **Name** | 
| ------- | -------- | 
| 00 | **[Python_Flow_Control_statement](https://github.com/milaan9/03_Python_Flow_Control/blob/main/000_Python_Flow_Control_statement%20.ipynb)** |
| 01 | **[Python_if_statement](https://github.com/milaan9/03_Python_Flow_Control/blob/main/001_Python_if_statement.ipynb)** |
| 02 | **[Python_if_else_statement](https://github.com/milaan9/03_Python_Flow_Control/blob/main/002_Python_if_else_statement.ipynb)** |
| 03 | **[Python_if_elif_else_statement](https://github.com/milaan9/03_Python_Flow_Control/blob/main/003_Python_if_elif_else_statement%20.ipynb)** |
| 04 | **[Python_Nested_if_statement](https://github.com/milaan9/03_Python_Flow_Control/blob/main/004_Python_Nested_if_statement.ipynb)** |
| 05 | **[Python_for_Loop](https://github.com/milaan9/03_Python_Flow_Control/blob/main/005_Python_for_Loop.ipynb)** |
| 06 | **[Python_while_Loop](https://github.com/milaan9/03_Python_Flow_Control/blob/main/006_Python_while_Loop.ipynb)** |
| 07 | **[Python_break_continue_pass_statements](https://github.com/milaan9/03_Python_Flow_Control/blob/main/007_Python_break_continue_pass_statements.ipynb)** |

These are online **read-only** versions. However you can **`Run ▶`** the code **online** by clicking here ➞ 

---

## Frequently asked questions ❔

### How can I thank you for writing and sharing this tutorial? 🌷

You can <img src="https://img.shields.io/static/v1?label=%E2%AD%90 Star &message=if%20useful&style=style=flat&color=blue" alt="Star Badge"/> and <img src="https://img.shields.io/static/v1?label=%E2%B5%96 Fork &message=if%20useful&style=style=flat&color=blue" alt="Fork Badge"/> Starring and Forking is free for you, but it tells me and other people that it was helpful and you like this tutorial.

Go [**`here`**](https://github.com/milaan9/03_Python_Flow_Control) if you aren't here already and click ➞ **`✰ Star`** and **`ⵖ Fork`** button in the top right corner. You'll be asked to create a GitHub account if you don't already have one.

---

### How can I read this tutorial without an Internet connection? <img alt="GIF" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/hmm.gif" width="20" />

1. Go [**`here`**](https://github.com/milaan9/03_Python_Flow_Control) and click the big green ➞ **`Code`** button in the top right of the page, then click ➞ [**`Download ZIP`**](https://github.com/milaan9/03_Python_Flow_Control/archive/refs/heads/main.zip).

    ![Download ZIP](img/dnld_rep.png)

2. Extract the ZIP and open it. Unfortunately I don't have any more specific instructions because how exactly this is done depends on which operating system you run.
    
3. Launch ipython notebook from the folder which contains the notebooks. Open each one of them
  
    **`Kernel > Restart & Clear Output`**
    
This will clear all the outputs and now you can understand each statement and learn interactively.

If you have git and you know how to use it, you can also clone the repository instead of downloading a zip and extracting it. An advantage with doing it this way is that you don't need to download the whole tutorial again to get the latest version of it, all you need to do is to pull with git and run ipython notebook again.

---

## Authors ✍️

I'm Dr. Milaan Parmar and I have written this tutorial. If you think you can add/correct/edit and enhance this tutorial you are most welcome🙏

See [github's contributors page](https://github.com/milaan9/03_Python_Flow_Control/graphs/contributors) for details.

If you have trouble with this tutorial please tell me about it by [Create an issue on GitHub](https://github.com/milaan9/03_Python_Flow_Control/issues/new). and I'll make this tutorial better. This is probably the best choice if you had trouble following the tutorial, and something in it should be explained better. You will be asked to create a GitHub account if you don't already have one.

If you like this tutorial, please [give it a ⭐ star](https://github.com/milaan9/03_Python_Flow_Control).

---

## Licence 📜

You may use this tutorial freely at your own risk. See [LICENSE](./LICENSE).

---

## 📘 Python Flow Control Statement
*Source: `3. Python Flow Control/0. Python Flow Control statement.ipynb`*

# Python Flow-Control (Decision-Making) Statements

In Python programming, decision-making statements are those that **help in deciding the flow of the program**. 

For example, at times, you might want to execute a block of code only if a particular condition is satisfied. Well, in this case, decision-making statement will be of great help. Let us consider an example to understand this better.

Decision making is required when we want to execute a code only if a certain condition is satisfied.

The key thing to note about Python's control flow statements and program structure is that it uses **`_indentation_`** to mark blocks. Hence the amount of white space (space or tab characters) at the start of a line is very important. This generally helps to make code more readable but can catch out new users of python.

* Suppose you are given a number and are asked to check if it is an even number or not. How would you do it?

> The first thought that would pop up your mind is this - **"If the number is divisible by 2, then it is an even number, else it is an odd number"**. That's absolutely the right logic. But when this has to be coded, you will need the help of decision-making statements. To understand this, let's now look at how they function.

## Control Flow Statements

The flow control statements are divided into **three** categories:

1. **Conditional statements**
2. **Iterative statements**
3. **Transfer/Control statements**

<div>

</div>

## Conditional statements

In Python, condition statements act depending on whether a given condition is true or false. You can execute different blocks of codes depending on the outcome of a condition. Condition statements always evaluate to either **`True`** or **`False`**.

There are **four** types of conditional statements:

1. **if**
2. **if-else**
3. **if-elif-else**
4. **nested-if**

## Iterative statements

In Python, iterative statements allow us to execute a block of code repeatedly as long as the condition is **`True`**. We also call it a loop statements.

Python provides us the following **two** loop statement to perform some actions repeatedly

1. **for loop**
2. **while loop**

## Transfer statements

In Python, transfer statements are used to alter the program’s way of execution in a certain manner. For this purpose, we use **three** types of transfer statements.

1. **break statement**
2. **continue statement**
3. **pass statements**

---

## 📘 Python If Statement
*Source: `3. Python Flow Control/1. Python if statement.ipynb`*

# Python `if` statement

In control statements, The **`if`** statement is the simplest form. It takes a condition and evaluates to either **`True`** or **`False`**.

If the condition is **`True`**, then the **`True`** block of code will be executed, and if the condition is **`False`**, then the block of code is skipped, and The controller moves to the next line.

### Syntax:

```python
if(condition):
    statement 1
    statement 2
    statement n
```

* An **`if`** statement should be preceded by the keyword **`if`** and ended with a colon **`:`**. The condition of an if statement can be written with or without round brackets **`()`**.

* In Python, the body of the **`if`** statement is indicated by the indentation. The body starts with an indentation and the first unindented line marks the end.

* Python interprets non-zero values as **`True`**. **`None`** and **`0`** are interpreted as **`False`**.

<div>

</div>

**Example: of `if` statement:**

```python
>>> grade = 70
>>> if grade >= 65:
>>>     print("Passing grade")

Passing grade
```

With this code, we have the variable grade and are giving it the integer value of 70. We are then using the **`if`** statement to evaluate whether or not the variable grade is **greater than or equal `>=`** to 65. If it does meet this **condition**, we are telling the program to print out the string Passing grade. 

Again, if we change the grade to 50 or < 65 number, we will receive no output.

```python
# Example 1:
grade = 70
if grade >= 65:
    print("Passing grade")
```

**Output:**
```text
Passing grade
```

```python
# Example 2: If the number is positive, we print an appropriate message

num = 3
if (num > 0):  # if condition is TRUE: enter the body of if
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:  # if condition is FALSE: do not enter the body of if
    print(num, "is a negative number.")
print("This is also always printed.")
```

**Output:**
```text
3 is a positive number.
This is always printed.
This is also always printed.
```

**Explanation**:

In the above example, **`num > 0`** is the test expression.

The body of **`if`** is executed only if this evaluates to **`True`**.

When the variable **`num`** is equal to 3, test expression is true and statements inside the body of **`if`** are executed.

If the variable **`num`** is equal to -1, test expression is false and statements inside the body of **`if`** are skipped.

The **print()** statement falls outside of the **`if`** block (unindented). Hence, it is executed regardless of the test expression.

```python
# Example 3: Calculate the square of a number if it greater than 6

number = 9
if number > 6:
    # Calculate square
    print(number * number)
print('Next lines of code')
```

**Output:**
```text
81
Next lines of code
```

```python
# Example 4: Check if num1 is less than num2

num1, num2 = 6, 9
if(num1 < num2):
    print("num1 is less than num2")
```

**Output:**
```text
num1 is less than num2
```

```python
x = 12
if x > 10:
    print("Hello")
```

**Output:**
```text
Hello
```

```python
if 5 != 3 * 6:
    print ("Hooray!")
```

**Output:**
```text
Hooray!
```

```python
if 5 == 15/3:
    print ("Horray!")
```

**Output:**
```text
Horray!
```

### Shortcut for `if` statement (Short-hand `if` or one-line `if`)

If you have only one statement to execute, then you can put it on the same line as the `if` statement. Let's try doing this for the above example.

```python
num1, num2 = 5, 6
if(num1 < num2): print("num1 is less than num2")
```

**Output:**
```text
num1 is less than num2
```

### The Difference....

Now, try to execute the below-given code and observe the difference.

```python
#program to check if num1 is less than num 2
num1, num2 = 6, 5
if (num1 < num2):
    print("num1 is less than num2")
```

**Explanation:**

**Did your Python IDE print anything?** No, it will not.

In the above-given code, the value 6 is greater than 5, this means the condition is False. We have instructed the interpreter to print only when the condition is True and hence it in this case, nothing gets printed. However, **you can also instruct the interpreter what to do when the condition is False and this can be done using else statement**.

```python
if 5 == 18/3:
    print ("Hooray!")
```

---

## 📘 Python If Else Statement
*Source: `3. Python Flow Control/2. Python if else statement.ipynb`*

# Python `if-else` statement

It is likely that we will want the program to do something even when an **if statement** **evaluates to false**. In our grade example of previous tutorial, we will want output whether the grade is passing or failing.

```python
x = 1

if x > 3:
    print ("Case 1")
if x <= 3:
    print ("Case 2")
```

**Output:**
```text
Case 2
```

The **`if-else`** statement checks the condition and executes the **`if`** block of code when the condition is **`True`**, and **`if`** the condition is **`False`**, it will execute the **`else`** block of code.

### Syntax :

```python
if condition:
    statement 1
else:
    statement 2
```

1. The **`if..else`** statement evaluates **`condition`** and will execute the body of **`if`** only when the test condition is **`True`**.

2. If the condition is **`False`**, the body of **`else`** is executed. Indentation is used to separate the blocks.

<div>

</div>

To do this, we will add an else statement to the grade condition above that is constructed like this:

```python
>>> grade = 60   
>>> if grade >= 65:
>>>     print("Passing grade")
>>> else:
>>>     print("Failing grade")

Failing grade
```

Since the grade variable above has the value of 60, the if statement evaluates as false, so the program will not print out Passing grade. The else statement that follows tells the program to do **something anyway**.

If we then rewrite the program to give the grade a value of 65 or higher, we will instead receive the output Passing grade.

```python
# Example 1:

grade = 60
    
if grade >= 65:
    print("Passing grade")
else:
    print("Failing grade")
```

**Output:**
```text
Failing grade
```

```python
# Example 2: Program checks if the number is positive or negative and displays an appropriate message

num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")
```

**Output:**
```text
Positive or Zero
```

**Explanation**

In the above example, when **`num`** is equal to 3, the test expression is true and the body of **`if`** is executed and the **`body`** of else is skipped.

If **`num`** is equal to -5, the test expression is false and the body of **`else`** is executed and the body of **`if`** is skipped.

If **`num`** is equal to 0, the test expression is true and body of **`if`** is executed and **`body`** of else is skipped.

```python
# Example 3: program to check if a num1 is less than num2

num1, num2 = 6, 5
if (num1 < num2):
    print("num1 is less than num2")
else:
    print("num2 is less than num1")
```

**Output:**
```text
num2 is less than num1
```

```python
# Example 4:

def password_check(password):
    if password == "Python@99>":
        print("Correct password")
    else:
        print("Incorrect Password")

password_check("Python@99>")
# Output Correct password

password_check("Python99")
# Output Incorrect Password
```

**Output:**
```text
Correct password
Incorrect Password
```

### Shortcut of `if else` (Short Hand if ... else or One line `if else`)

If you have **only one statement each for if and else, then they can be put in the same line**. This can be done as shown below

```python
hungry = True
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)
```

**Output:**
```text
Feed the bear now!
```

```python
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed
```

**Output:**
```text
A is positive
```

```python
num1, num2 = 6, 5
print("num1 is less than num2") if (num1 < num2) else print("num2 is less than num1")
```

**Output:**
```text
num2 is less than num1
```

```python
number = 96
if number > 0: print("positive") 
else: print("negative")
```

**Output:**
```text
positive
```

```python
x = 12
if 10 < x < 11:
    print("hello")
else:
    print("world")
```

**Output:**
```text
world
```

```python
'''
x = 1

if x > 3:
    print ("Case 1")
if x <= 3:
    print ("Case 2")
'''

x = 1

if x > 3:
    print ("Case 1")
else:
    print ("Case 2")
```

**Output:**
```text
Case 2
```

```python
x = 2

if x > 4:
    print ("Correct")
else:
    print("Incorrect")
```

**Output:**
```text
Incorrect
```

### The difference....

Now, let us try to execute the same above discussed code with different input values.

```python
#program to check if num1 is less than num2

num1, num2 = 5, 5
if (num1 < num2):
    print("num1 is less than num2")
else:
    print("num2 is less than num1")

'''
Output: num2 is lesser than num1
'''
```

**Output:**
```text
num2 is less than num1
'\nOutput: num2 is lesser than num1\n'
```

**Explanation:**

* **Why was the output wrong?**

Since both the input values are equal, the condition **`num1<num2`** is **`False`**. So immediately the control shifts to else block and the print statement inside it gets executed. However, this is not logically correct as both the input values are equal (5 = 5).


*  **How to rectify this?**

Your program should logically include every possible test case and only then your program will produce accurate results. So this mean **you need to add another conditional statement to check if num1 is equal to num 2**. Let us now see how this can be done.

## 💻 Exercises  ➞ <span class='label label-default'>List</span>

1.  Get user input using **`input(“Enter your age: ”)`**. If user is 18 or older, give feedback: **`You are old enough to drive`**. If below 18 give feedback to **`wait for the missing amount of years`**. 

Output:

```py
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
```

2.  Compare the values of my_age and your_age using **`if-else`**. Who is older (me or you)? Use **`input(“Enter your age: ”)`** to get the age as input. You can use a nested condition to print **`'year'`** for 1 year difference in age, **`'years'`** for bigger differences, and a custom text if **`my_age = your_age`**. 

Output:

```py
    Enter your age: 30
    You are 5 years older than me.
```

---

## 📘 Python If Elif Else Statement
*Source: `3. Python Flow Control/3. Python if elif else statement.ipynb`*

# Python `if-elif-else` statement

So far, we have presented a Boolean option for conditional statements, with each **if statement** evaluating to either **`True`** or **`False`**. In Python, the **`if-elif-else`** condition statement has an **`elif`** keyword used to chain multiple conditions one after another.

### Syntax:

```python
if condition-1:  
     statement 1 
elif condition-2:
     stetement 2 
elif condition-3:
     stetement 3 
     ...         
else:            
     statement  
```

1. The **`elif`** is short for else if. It allows us to check for multiple expressions.

2. If the condition for **`if`** is **`False`**, it checks the condition of the next **`elif`** block and so on.

3. If all the conditions are **`False`**, the body of **`else`** is executed.

4. Only one block among the several **`if-elif-else`** blocks is executed according to the condition.

5. The **`if`** block can have only one **`else`** block. But it can have multiple **`elif`** blocks.

<div>

</div>

```python
# Example 1:

'''In this program, we check if the number is positive or negative or zero and 
display an appropriate message'''

num = 0

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
```

**Output:**
```text
Zero
```

**Explanation:**

When variable **`num`** is positive, **`Positive number`** is printed.

If **`num`** is equal to 0, **`Zero`** is printed.

If **`num`** is negative, **`Negative number`** is printed.

```python
# Example 2:

num1, num2 = 5, 5
if(num1 > num2):
    print("num1 is greater than num2")
elif(num1 == num2):
    print("num1 is equal to num2")
else:
    print("num1 is less than num2")
```

**Output:**
```text
num1 is equal to num2
```

```python
# Example 3:

x = 10
y = 12
if x > y:
    print("x>y")
elif x < y:
    print("x<y")
else:
    print("x=y")
```

**Output:**
```text
x<y
```

```python
# Example 4:

grade = 96

if grade >= 90:
    print("A grade")
elif grade >=80:
    print("B grade")
elif grade >=70:
    print("C grade")
elif grade >= 65:
    print("D grade")
else:
    print("Failing grade")
```

**Output:**
```text
A grade
```

```python
# Example 5:

def user_check(choice):
    if choice == 1:
        print("Admin")
    elif choice == 2:
        print("Editor")
    elif choice == 3:
        print("Guest")
    else:
        print("Wrong entry")

user_check(1)  # Admin
user_check(2)  # Editor
user_check(3)  # Guest
user_check(4)  # Wrong entry
```

**Output:**
```text
Admin
Editor
Guest
Wrong entry
```

## if-elif-else statements with logical operators

We can avoid writing nested condition by using logical operator **`and`**.

### if-elif-else statements `and` Logical Operator

**Syntax:**

```py
if condition and condition:
    code
```

```python
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

**Output:**
```text
A is zero
```

### if-elif-else statements `or` Logical Operator

**Syntax:**

```py
if condition or condition:
    code
```

```python
user = 'Arthur'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

**Output:**
```text
Access denied!
```

## 💻 Exercises ➞ <span class='label label-default'>List</span>

### Exercises ➞ <span class='label label-default'>Level 1</span>

1.  Get two numbers from the user using input prompt. If **`num_1`** is greater than **`num_2`** return **`num_1`** is greater than **`num_2`**, if **`num_1`** is less **`num_2`** return **`num_1`** is smaller than **`num_2`**, else **`num_1`** is equal to **`num_2`**. Output:

```sh
Enter number one: 9
Enter number two: 6
9 is greater than 6
```

### Exercises ➞ <span class='label label-default'>Level 2</span>

1. Write a code which gives grade to students according to theirs scores:
   
```py
 80-100, A
 70-89, B
 60-69, C
 50-59, D
 0-49, F
```

2. Check if the season is Autumn, Winter, Spring or Summer. 
    - If the user input is:
        - September, October or November, the season is Autumn.
        - December, January or February, the season is Winter.
        - March, April or May, the season is Spring
        - June, July or August, the season is Summer


3.  The following list contains some fruits:
       - If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print **`('That fruit already exist in the list')`** 
    
```py
 fruits = ['banana', 'orange', 'mango', 'pear']
```    


### Exercises ➞ <span class='label label-default'>Level 3</span>

   1. Here we have a person dictionary. Feel free to modify it!
   
```py
    person={
    'first_name': 'Milaan',
    'last_name': 'Parmar',
    'age': 96,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['Python', 'Matlab', 'R', 'C', 'C++'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
```

     * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
     * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
     * If a person skills has only Python and Matlab, print('He knows machine learning'), if the person skills has Python, and R print('He knows statistics'), if the person skills has C, and C++, Print('He knows software development'), else print('unknown title') - for more accurate results more conditions can be nested!
     * If the person is married and if he lives in Finland, print the information in the following format:

```py
    Milaan Parmar lives in Finland. He is married.
```

---

## 📘 Python Nested If Statement
*Source: `3. Python Flow Control/4. Python Nested if statement.ipynb`*

# Python Nested `if` statement

We can have a nested-**if-else** or nested-**if-elif-else)** statement inside another **`if-else`** statement. This is called **nesting** in computer programming. The nested if statements is useful when we want to make a series of decisions.

Any number of these statements can be nested inside one another. Indentation is the only way to figure out the level of nesting. They can get confusing, so they must be avoided unless necessary.

We can use nested if statements for situations where we want to check for a **secondary condition** if the first condition executes as **`True`**.

### Syntax:

#### Example 1:
```python
if conditon_outer:
    if condition_inner:
        statement of nested if
    else:
        statement of nested if else:
    statement ot outer if
else:
    Outer else 
statement outside if block
```

#### Example 2:
```python
if expression1:
    statement(s)
    if expression2:
        statement(s)
    elif expression3:
        statement(s)
    elif expression4:
        statement(s)
    else:
        statement(s)
else:
    statement(s)
```

```python
# Example 1:

a=10
if a>=20:  # Condition FALSE
    print ("Condition is True")
else:  # Code will go to ELSE body
    if a>=15:  # Condition FALSE
        print ("Checking second value")
    else:  # Code will go to ELSE body
        print ("All Conditions are false")
```

**Output:**
```text
All Conditions are false
```

```python
# Example 2:

x = 10
y = 12
if x > y:
    print( "x>y")
elif x < y:
    print( "x<y")
    if x==10:
        print ("x=10")
    else:
        print ("invalid")
else:
    print ("x=y")
```

**Output:**
```text
x<y
x=10
```

```python
# Example 3:

num1 = 0
if (num1 != 0):  # For zero condition is FALSE
    if(num1 > 0):  
        print("num1 is a positive number")
    else:  
        print("num1 is a negative number")
else:  # For zero condition is TRUE
    print("num1 is neither positive nor negative")
```

**Output:**
```text
num1 is neither positive nor negative
```

```python
# Example 4:

'''In this program, we input a number check if the number is 
positive or negative or zero and display an appropriate message. 
This time we use nested if statement'''

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
```

**Output:**
```text
Enter a number: 9
Positive number
```

```python
# Example 5:

def number_arithmetic(num1, num2):
    if num1 >= num2:
        if num1 == num2:
            print(f'{num1} and {num2} are equal')
        else:
            print(f'{num1} is greater than {num2}')
    else:
        print(f'{num1} is smaller than {num2}')

number_arithmetic(96, 66)
# Output 96 is greater than 66
number_arithmetic(96, 96)
# Output 56 and 56 are equal
```

**Output:**
```text
96 is greater than 66
96 and 96 are equal
```

---

## 📘 Python For Loop
*Source: `3. Python Flow Control/5. Python for Loop.ipynb`*

# Loops in Python

Loops in Python programming function similar to loops in C, C++, Java or other languages. Python loops are used to repeatedly execute a block of statements until a given condition returns to be **`False`**. In Python, we have **two types of looping statements**, namely:
<div>

</div>

# Python `for` Loop

In this class, you'll learn to iterate over a sequence of elements using the different variations of **`for`** loop. We use a **`for`** loop when we want to repeat a code block for a **fixed number of times**.

## What is `for` loop in Python? 

The for loop in Python is used to iterate over a sequence (**string**, **list**, **dictionary**, **set**, or **tuple**). Iterating over a sequence is called traversal.

## Why use `for` loop?

Let’s see the use **`for`** loop in Python.

* **Definite Iteration:** When we know how many times we wanted to run a loop, then we use count-controlled loops such as **`for`** loops. It is also known as definite iteration. For example, Calculate the percentage of 50 students. here we know we need to iterate a loop 50 times (1 iteration for each student).
* **Reduces the code’s complexity:** Loop repeats a specific block of code a fixed number of times. It reduces the repetition of lines of code, thus reducing the complexity of the code. Using **`for`** loops and while loops we can automate and repeat tasks in an efficient manner.
* **Loop through sequences:** used for iterating over lists, strings, tuples, dictionaries, etc., and perform various operations on it, based on the conditions specified by the user.

### Syntax :

```python  
for element in sequence:
    body of for loop 
```

1. First, **`element`** is the variable that takes the value of the item inside the sequence on each iteration.

2. Second, all the **`statements`** in the body of the for loop are executed with the same value. The body of for loop is separated from the rest of the code using indentation.

3. Finally, loop continues until we reach the last item in the **`sequence`**. The body of for loop is separated from the rest of the code using indentation.

<div>

</div>

```python
# Example 1: For loop 

words = ['one', 'two', 'three', 'four', 'five']

for i in words:
    print(i)
```

**Output:**
```text
one
two
three
four
five
```

```python
# Example 2: Calculate the average of list of numbers

numbers = [10, 20, 30, 40, 50]

# definite iteration
# run loop 5 times because list contains 5 items
sum = 0
for i in numbers:
    sum = sum + i
list_size = len(numbers)
average = sum / list_size
print(average)
```

**Output:**
```text
30.0
```

## `for` loop with `range()` function

The **range()** function returns a sequence of numbers starting from 0 (by default) if the initial limit is not specified and it increments by 1 (by default) until a final limit is reached.

The **`range()`** function is used with a loop to specify the range (how many times) the code block will be executed. Let us see with an example.

We can generate a sequence of numbers using **`range()`** function. **`range(5)`** will generate numbers from 0 to 4 (5 numbers). 

<div>

</div>

The **`range()`** function is "lazy" in a sense because it doesn't generate every number that it "contains" when we create it. However, it is not an iterator since it supports **len()** and **`__getitem__`** operations.

This **`range()`** function does not store all the values in memory; it would be inefficient. So it remembers the start, stop, step size and generates the next number on the go.

We can also define the start, stop and step size as **`range(start, stop,step_size)`**. **`step_size`** defaults to 1 if not provided.

```python
# Example 1: How range works in Python?

# empty range
print(list(range(0)))

# using range(stop)
print(list(range(10)))

# using range(start, stop)
print(list(range(1, 10)))
```

**Output:**
```text
[]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
# Example 2:

for num in range(10):
    print(num)
```

**Output:**
```text
0
1
2
3
4
5
6
7
8
9
```

```python
# Example 3:

for i in range(1, 11):
    print(i)
```

**Output:**
```text
1
2
3
4
5
6
7
8
9
10
```

```python
# Example 4:

for i in range (2, 12, 2):  # beginning 2 with distance of 2 and stop before 12
    print (i)
```

**Output:**
```text
2
4
6
8
10
```

```python
# Example 5:

num=2

for a in range (1,6):  # range (1,6) means numbers from 1 to 5, i.e., (1,2,3,4,5)
    print (num * a)
```

**Output:**
```text
2
4
6
8
10
```

```python
# Example 6: Find Sum of 10 Numbers

sum=0
for n in range(1,11):  # range (1,11) means numbers from 1 to 5, i.e., (1,2,3,4,5,6,7,8,9,10)
    sum+=n  
    print (sum)
    
'''
0+1 = 1
1+2 = 3
3+3 = 6
6+4 = 10
10+5 =15
21
28
36
45
45+10 = 55
'''
```

**Output:**
```text
1
3
6
10
15
21
28
36
45
55
'\n0+1 = 1\n1+2 = 3\n3+3 = 6\n6+4 = 10\n10+5 =15\n21\n28\n36\n45\n45+10 = 55\n'
```

```python
# Example 7: printing a series of numbers using for and range

print("Case 1:")
for i in range(5):  # Print numbers from 0 to 4
    print (i)

print("Case 2:")  
for i in range(5, 10):  # Print numbers from 5 to 9
    print (i)

print("Case 3:")
for i in range(5, 10, 2):  # Print numbers from 5 with distace 2 and stop before 10
    print (i)
```

**Output:**
```text
Case 1:
0
1
2
3
4
Case 2:
5
6
7
8
9
Case 3:
5
7
9
```

## `for` loop with `if-else`

A **`for`** loop can have an optional **if-else** block. The **`if-else`** checks the condition and if the condition is **`True`** it executes the block of code present inside the **`if`** block and if the condition is **`False`**, it will execute the block of code present inside the **`else`** block.

```python
# Example 1: Print all even and odd numbers

for i in range(1, 11):
    if i % 2 == 0:
        print('Even Number:', i)
    else:
        print('Odd Number:', i)
```

**Output:**
```text
Odd Number: 1
Even Number: 2
Odd Number: 3
Even Number: 4
Odd Number: 5
Even Number: 6
Odd Number: 7
Even Number: 8
Odd Number: 9
Even Number: 10
```

## `for` loop with `else`

A **`for`** loop can have an optional **`else`** block as well. The **`else`** part is executed if the items in the sequence used in for loop exhausts.

**`else`** block will be skipped/ignored when:

* **`for`** loop terminate abruptly
* the **break statement** is used to break the **`for`** loop.

```python
# Example 1:

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")
```

**Output:**
```text
0
1
5
No items left.
```

**Explanation:**

Here, the for loop prints items of the list until the loop exhausts. When the for loop exhausts, it executes the block of code in the **`else`** and prints **`No items left`**.

```python
# Example 2:

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
```

**Output:**
```text
0
1
2
3
4
5
6
7
8
9
10
The loop stops at 10
```

```python
# Example 3: Else block in for loop

for i in range(1, 6):
    print(i)
else:
    print("Done")
```

**Output:**
```text
1
2
3
4
5
Done
```

This **`for-else`** statement can be used with the **`break`** keyword to run the **`else`** block only when the **`break`** keyword was not executed. Let's take an example:

```python
# Example 4:

student_name = 'Arthur'

marks = {'Alan': 99, 'Bill': 55, 'Cory': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')
```

**Output:**
```text
No entry with that name found.
```

```python
# Example 5:

count = 0
for i in range(1, 6):
    count = count + 1
    if count > 2:
        break
    else:
        print(i)
else:
    print("Done")
```

**Output:**
```text
1
2
```

## Using Control Statement in `for` loops in Python

**Control statements** in Python like **`break`**, **`continue`**, etc can be used to control the execution flow of **`for`** loop in Python. Let us now understand how this can be done.

It is used when you want to exit a loop or skip a part of the loop based on the given condition. It also knows as **transfer statements**.

### a) `break` in `for` loop

Using the **`break`** statement, we can exit from the **`for`** loop before it has looped through all the elements in the sequence as shown below. As soon as it breaks out of the **`for`** loop, the control shifts to the immediate next line of code. For example,

```python
# Example 1:

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

**Output:**
```text
0
1
2
3
```

**Explanation:**

In the above example, the loop stops when it reaches 3.

```python
# Example 2:

color = ['Green', 'Pink', 'Blue']
for i in color:
    if(i == 'Pink'):
        break
print (i)
```

**Output:**
```text
Pink
```

**Explanation:**

Here, in the second iteration, the **`if`** condition becomes **`True`**. Hence the loop beaks out of the for loop and the immediate next line of code i.e **`print (i)`** is executed and as a result, pink is outputted.

```python
# Example 3:

numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]
for i in numbers:
    if i > 15:
        # break the loop
        break
    else:
        print(i)
```

**Output:**
```text
1
4
7
8
15
```

```python
# Example 4:

for i in range(5):
    for j in range(5):
        if j == i:
            break
        print(i, j)
```

**Output:**
```text
1 0
2 0
2 1
3 0
3 1
3 2
4 0
4 1
4 2
4 3
```

**Explanation:**

We have two loops. The outer **`for`** loop iterates the first four numbers using the **range()** function, and the inner **`for`** loop also iterates the first four numbers. If the outer number and a current number of the inner loop are the same, then break the inner (nested) loop.

### b) `continue` in `for` loop

The **`continue`** statement is used to stop/skip the block of code in the loop for the current iteration only and continue with the next iteration. For example,

```python
# Example 1:

color = ['Green', 'Pink', 'Blue']
for i in color:
    if(i == 'Pink'):
        continue
print (i)
```

**Output:**
```text
Blue
```

**Explanation:**

Here, in the second iteration, the condition becomes **`True`**. Hence the interpreter skips the **`print (i)`** statement and immediately executes the next iteration.

```python
# Example 2:

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
```

**Output:**
```text
0
Next number should be  1
1
Next number should be  2
2
Next number should be  3
3
4
Next number should be  5
5
loop's end
outside the loop
```

**Explanation:**

In the example above, if the number equals 3, the step **after** the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left.

```python
# Example 3:

first = [3, 6, 9]
second = [3, 6, 9]
for i in first:
    for j in second:
        if i == j:
            continue
        print(i, '*', j, '= ', i * j)
```

**Output:**
```text
3 * 6 =  18
3 * 9 =  27
6 * 3 =  18
6 * 9 =  54
9 * 3 =  27
9 * 6 =  54
```

**Explanation:**

We have two loops. The outer for loop iterates the first list, and the inner loop also iterates the second list of numbers. If the outer number and the inner loop’s current number are the same, then move to the next iteration of an inner loop.

As you can see in the output, no same numbers multiplying to each other.

```python
# Example 4:

name = "mariya mennen"
count = 0
for char in name:
    if char != 'm':
        continue
    else:
        count = count + 1

print('Total number of m is:', count)
```

**Output:**
```text
Total number of m is: 2
```

### c) `pass` in `for` loop

The **`pass`** statement is a null statement, i.e., nothing happens when the statement is executed. Primarily it is used in empty functions or classes. When the interpreter finds a pass statement in the program, it returns no operation.

```python
# Example 1:

for number in range(6):
    pass
```

```python
# Example 2:

num = [1, 4, 5, 3, 7, 8]
for i in num:
    # calculate multiplication in future if required
    pass
```

## Reverse for loop

Till now, we have learned about forward looping in **`for`** loop with various examples. Now we will learn about the backward iteration of a loop.

Sometimes we require to do reverse looping, which is quite useful. For example, to reverse a list.

There are three ways to iterating the **`for`** loop backward:

* Reverse **`for`** loop using **range()** function
* Reverse **`for`** loop using the **reversed()** function

### Backward Iteration using the `reversed()` function

We can use the built-in function **reversed()** with **`for`** loop to change the order of elements, and this is the simplest way to perform a reverse looping.

```python
# Example 1: Reversed numbers using `reversed()` function

list1 = [10, 20, 30, 40]
for num in reversed(list1):
    print(num)
```

**Output:**
```text
40
30
20
10
```

### Reverse for loop using `range()`

We can use the built-in **range()** function with the **`for`** loop to reverse the elements order. The **`range()`** generates the integer numbers between the given start integer to the stop integer.

```python
# Example 1:

print("Reverse numbers using for loop")
num = 5
# start = 5
# stop = -1
# step = -1
for num in (range(num, -1, -1)):
    print(num)
```

**Output:**
```text
Reverse numbers using for loop
5
4
3
2
1
0
```

There are many helper functions that make **`for`** loops even more powerful and easy to use. For example **enumerate()**, **zip()**, **sorted()**, **reversed()**

```python
# Example 2:

print("reversed: \t",end="")
for ch in reversed("abc"):
    print(ch,end=";")

print("\nenuemerated:\t",end="")
for i,ch in enumerate("abc"):
    print(i,"=",ch,end="; ")
    
print("\nzip'ed: ")
for a,x in zip("abc","xyz"):
    print(a,":",x)
```

**Output:**
```text
reversed: 	c;b;a;
enuemerated:	0 = a; 1 = b; 2 = c; 
zip'ed: 
a : x
b : y
c : z
```

## Nested `for` loops

**Nested `for` loop** is a **`for`** loop inside another **`for`** a loop. 

A nested loop has one loop inside of another. In Python, you can use any loop inside any other loop. For instance, a **`for`** loop inside a **while loop**, a **`while`** inside **`for`** in and so on. It is mainly used with two-dimensional arrays.

In nested loops, the inner loop finishes all of its iteration for each iteration of the outer loop. i.e., For each iteration of the outer loop inner loop restart and completes all its iterations, then the next iteration of the outer loop begins.

**Syntax:**

```python
# outer for loop
for element in sequence 
   # inner for loop
    for element in sequence:
        body of inner for loop
    body of outer for loop
other statements
```

### `for` loop inside `for` loop

#### Example: Nested `for` loop 

In this example, we are using a **`for`** loop inside a **`for`** loop. In this example, we are printing a multiplication table of the first ten numbers.

<div>

</div>

1. The outer **`for`** loop uses the **range()** function to iterate over the first ten numbers
2. The inner **`for`** loop will execute ten times for each outer number
3. In the body of the inner loop, we will print the multiplication of the outer number and current number
4. The inner loop is nothing but a body of an outer loop.

```python
# Example 1: printing a multiplication table of the first ten numbers

# outer loop
for i in range(1, 11):
    # nested loop   
    for j in range(1, 11):   # to iterate from 1 to 10        
        print(i * j, end=' ')    # print multiplication
    print()
```

**Output:**
```text
1 2 3 4 5 6 7 8 9 10 
2 4 6 8 10 12 14 16 18 20 
3 6 9 12 15 18 21 24 27 30 
4 8 12 16 20 24 28 32 36 40 
5 10 15 20 25 30 35 40 45 50 
6 12 18 24 30 36 42 48 54 60 
7 14 21 28 35 42 49 56 63 70 
8 16 24 32 40 48 56 64 72 80 
9 18 27 36 45 54 63 72 81 90 
10 20 30 40 50 60 70 80 90 100
```

**Explanation:**

* In this program, the outer **`for`** loop is iterate numbers from 1 to 10. The **`range()`** return 10 numbers. So total number of iteration of the outer loop is 10.
* In the first iteration of the nested loop, the number is 1. In the next, it 2. and so on till 10.
* Next, the inner loop will also execute ten times because we rea printing multiplication table up to ten. For each iteration of the outer loop, the inner loop will execute ten times.
* In each iteration of an inner loop, we calculated the multiplication of two numbers.

```python
# Example 1:

person = {
    'first_name':'Milaan',
    'last_name':'Parmar',
    'age':96,
    'country':'Finland',
    'is_marred':True,
    'skills':['Python', 'Matlab', 'R', 'C', 'C++'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

**Output:**
```text
Python
Matlab
R
C
C++
```

```python
# Example 2: Write a code to add all the prime numbers between 17 to 53 using while loop
# 17, 19, 23, 29, 31, 37, 41, 43, 47, 53

sum=0
for i in range(17,54):    
    for j in range(2,i):        
        if i%j ==0:            
            break    
    else:        
        sum=sum+i
        print(i)
print(sum)
```

**Output:**
```text
17
19
23
29
31
37
41
43
47
53
340
```

```python
# Example 3: iterating through nested for loops

color = ['Red', 'Pink']
element = ['flower', 'watch']
for i in color:
    for j in element:
        print(i, j)
```

**Output:**
```text
Red flower
Red watch
Pink flower
Pink watch
```

```python
# Example 4: A use case of a nested for loop in `list_of_lists` case would be

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total=0
for list1 in list_of_lists:
    for i in list1:
        total = total+i
print(total)
```

**Output:**
```text
45
```

```python
# Example 5:

numbers = [[1, 2, 3], [4, 5, 6]]

cnt = 0
for i in numbers:
    for j in i:
        print('iteration', cnt, end=': ')
        print(j)
        cnt = cnt + 1
```

**Output:**
```text
iteration 0: 1
iteration 1: 2
iteration 2: 3
iteration 3: 4
iteration 4: 5
iteration 5: 6
```

#### Example: Nested `for` loop to print pattern

```python
*
* *
* * *
* * * *
* * * * *
```

```python
>>>rows = 5
   # outer loop
>>>for i in range(1, rows + 1):
       # inner loop
>>>    for j in range(1, i + 1):
>>>        print("*", end=" ")
>>>    print('')
```

<div>

</div>

**Explanation:**

* In this program, the outer loop is the number of rows print. 
* The number of rows is five, so the outer loop will execute five times
* Next, the inner loop is the total number of columns in each row.
* For each iteration of the outer loop, the columns count gets incremented by 1
* In the first iteration of the outer loop, the column count is 1, in the next it 2. and so on.
* The inner loop iteration is equal to the count of columns.
* In each iteration of an inner loop, we print star

```python
# Example 1: Method 1

rows = 5
for i in range(1, rows + 1):    # outer loop    
    for j in range(1, i + 1):   # inner loop
        print("*", end=" ")
    print('')
```

**Output:**
```text
* 
* * 
* * * 
* * * * 
* * * * *
```

```python
# Example 1: Method 2 - Print Floyd Triangle with user input
		

ran = input("How many rows? ")

rang = int(ran)
k = 1
for i in range(1, rang+1):
    for j in range(1, i+1):
        print("*", end=" ")
        k = k + 1
    print()
```

**Output:**
```text
How many rows? 5
* 
* * 
* * * 
* * * * 
* * * * *
```

```python
# Example 2: Method 1

for i in range(1,6):       # numbers from 0,1,2,3,4,5
    for j in range(1, i+1):  
        print(i, end=" ")  # print number    
    print(" ")             # line after each row to display pattern correctly
```

**Output:**
```text
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
```

```python
# Example 2: Method 2

rows = 6 
for num in range(rows):     # from 0,1,2,3,4,5
    for i in range(num):
        print(num,end=" ")  # print the number
    print(" ")              # line after each row to print
```

**Output:**
```text
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
```

```python
# Example 3: Method 3

n=5  # giving number of rows i want
x = 0
for i in range(0 , n):         # from 0 to 4
    x += 1                     # equivalent to x=x+1
    for j in range(0, i + 1):  # 0,1,2,3,4,5
        print(x , end=" ") 
    print(" ")
```

**Output:**
```text
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
```

```python
# Example 4: Method 1

rows = 5
for row in range(1, rows+1):       # from 1
    for column in range(1, row+1): # from 1,2,3,4,5
        print(column, end=" ")
    print(" ")
```

**Output:**
```text
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5
```

```python
# Example 4: Method 2

for i in range (1, 6):  # rows from 1 to 5
    for j in range(i):  # column range(i)
        print (j + 1, end = ' ')
    print ()
```

**Output:**
```text
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```

```python
# Example 5: Method 1

for i in range (1,6):
    for j in range (i,0,-1):
        print(j, end=" ")
    print(" ")
    
"""
i = 1 2 3 4 5 

# loop 1
for i = 1, range (1,0,-1): j=1
i = 1, print: 1 

# loop 2
for  i =2, range (2,0,-1): j = 2,1
i = 2, print: 2,1
"""
```

**Output:**
```text
1  
2 1  
3 2 1  
4 3 2 1  
5 4 3 2 1  
'\ni = 1 2 3 4 5 \n\n# loop 1\nfor i = 1, range (1,0,-1): j=1\ni = 1, print: 1 \n\n# loop 2\nfor  i =2, range (2,0,-1): j = 2,1\ni = 2, print: 2,1\n'
```

```python
# Example 5: Method 2

for i in range(0,5):
    for j in range(i+1,0,-1):
        print(j, end=" ")
    print()
```

**Output:**
```text
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
```

```python
# Example 6: Example 1 reverse pyramid 


for i in range (1,6):            # rows from 1 to 5
    for j in range (5,i-1,-1):   # column range(5,0,-1) = 54321
        print ("*", end=" "),
    print (" ")
```

**Output:**
```text
* * * * *  
* * * *  
* * *  
* *  
*
```

```python
# Example 7: Example 2 reverse pyramid Method 1

rows = 5
#        range(1,10,2)  # from 1,3,5,7,9
for i in range(rows,0,-1):  # from 3,2,1
    num = i
    for j in range(0,i):
        print(num, end=" ")
    print(" ")
```

**Output:**
```text
5 5 5 5 5  
4 4 4 4  
3 3 3  
2 2  
1
```

```python
# Example 7: Example 2 reverse pyramid Method 2

for i in range(5,0,-1):  # range from 5 4 3 2 1
    for j in range(0,i): # range(0,5)=0 1 2 3 4
        print(i, end=" ")
    print(" ")
    
"""
i = 5 4 3 2 1 

# loop 1
for i = 5, range (0,5): j=5 4 3 2 1
i = 5, print: 5 5 5 5 5

# loop 2
for i = 4, range (0,4): j=4 3 2 1
i = 4, print: 4 4 4 4 
"""
```

**Output:**
```text
5 5 5 5 5  
4 4 4 4  
3 3 3  
2 2  
1  
'\ni = 5 4 3 2 1 \n\n# loop 1\nfor i = 5, range (0,5): j=5 4 3 2 1\ni = 5, print: 5 5 5 5 5\n\n# loop 2\nfor i = 4, range (0,4): j=4 3 2 1\ni = 4, print: 4 4 4 4 \n'
```

```python
# Example 8: Method 1

for i in range(5,0,-1):  # rows range = 5 4 3 2 1 
    for j in range(1,i+1): # column range 
        print(j, end =" ")
    print()
```

**Output:**
```text
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1
```

```python
# Example 8: Method 2

for i in range(1,6):
    for j in range(6-i):
        print(j+1, end=" ")
    print(" ")
    
"""
i = 1 2 3 4 5 

# loop 1
for i = 1, range (5): j=0 1 2 3 4
i = 1, print: 1 2 3 4 5

# loop 2
for i = 2, range (4): j=0 1 2 3
i = 2, print: 1 2 3 4

# loop 3
for i = 3, range (3): j=0 1 2
i = 3, print: 1 2 3

# loop 4
for i = 4, range (2): j=0 1
i = 4, print: 1 2

# loop 5
for i = 5, range (1): j=0 
i = 5, print: 1 
"""
```

**Output:**
```text
1 2 3 4 5  
1 2 3 4  
1 2 3  
1 2  
1  
'\ni = 1 2 3 4 5 \n\n# loop 1\nfor i = 1, range (5): j=0 1 2 3 4\ni = 1, print: 1 2 3 4 5\n\n# loop 2\nfor i = 2, range (4): j=0 1 2 3\ni = 2, print: 1 2 3 4\n\n# loop 3\nfor i = 3, range (3): j=0 1 2\ni = 3, print: 1 2 3\n\n# loop 4\nfor i = 4, range (2): j=0 1\ni = 4, print: 1 2\n\n# loop 5\nfor i = 5, range (1): j=0 \ni = 5, print: 1 \n'
```

```python
# Example 9: Print following rectangle of stars of 6 rows and 3 columns
```

### `while` loop inside `for` loop

The **[while loop](https://github.com/milaan9/03_Python_Flow_Control/blob/main/006_Python_while_Loop.ipynb)** is an entry-controlled loop, and a **`for`** loop is a count-controlled loop. We can also use a **`while`** loop under the for loop statement. For example,

```python
# Example 1: Print Multiplication table of a first 5 numbers using `for` loop and `while` loop

# outer loop
for i in range(1, 6):
    print('Multiplication table of:', i)
    count = 1
    # inner loop to print multiplication table of current number
    while count < 11:
        print(i * count, end=' ')
        count = count + 1
    print('\n')
```

**Output:**
```text
Multiplication table of: 1
1 2 3 4 5 6 7 8 9 10 

Multiplication table of: 2
2 4 6 8 10 12 14 16 18 20 

Multiplication table of: 3
3 6 9 12 15 18 21 24 27 30 

Multiplication table of: 4
4 8 12 16 20 24 28 32 36 40 

Multiplication table of: 5
5 10 15 20 25 30 35 40 45 50
```

**Explanation:** 

* In this program, we iterate the first five numbers one by one using the outer loop and range function
* Next, in each iteration of the outer loop, we will use the inner while loop to print the multiplication table of the current number

```python
# Example 2:

names = ['Amy', 'Bella', 'Cathy']

for name in names:  # outer loop    
    count = 0       # inner while loop
    while count < 5:
        print(name, end=' ')
        # increment counter
        count = count + 1
    print()
```

**Output:**
```text
Amy Amy Amy Amy Amy 
Bella Bella Bella Bella Bella 
Cathy Cathy Cathy Cathy Cathy
```

## `for ` loop in one line

We can also formulate the **`for`** loop statement in one line to reduce the number of lines of code. For example:

```python
# Example 1: regular `for` loop code

first = [3, 6, 9]
second = [30, 60, 90]
final = []
for i in first:
    for j in second:
        final.append(i+j)
print(final)
```

**Output:**
```text
[33, 63, 93, 36, 66, 96, 39, 69, 99]
```

```python
# Example 1: single line `for` loop code

first = [3, 6, 9]
second = [30, 60, 90]
final = [i+j for i in first for j in second]
print(final)
```

**Output:**
```text
[33, 63, 93, 36, 66, 96, 39, 69, 99]
```

```python
# Example 2: Print the even numbers by adding 1 to the odd numbers in the list

odd = [1, 5, 7, 9]
even = [i + 1 for i in odd if i % 2 == 1]
print(even)
```

**Output:**
```text
[2, 6, 8, 10]
```

```python
# Example 3:

final = [[x, y] for x in [30, 60, 90] for y in [60, 30, 90] if x != y]
print(final)
```

**Output:**
```text
[[30, 60], [30, 90], [60, 30], [60, 90], [90, 60], [90, 30]]
```

## Accessing the index in for loop

The **enumerate()** function is useful when we wanted to access both value and its index number or any sequence such as list or string. For example, a list is an ordered data structure that stores each item with its index number. Using the item’s index number, we can access or modify its value.

Using enumerate function with a loop, we can access the list’s items with their index number. The **`enumerate()`** adds a counter to iteration and returns it in the form of an enumerable object.

There three ways to access the index in **`for`** loop let’s see each one by one

```python
# Example 1: Print elements of the list with its index number using the `enumerate()` function

#In this program, the for loop iterates through the list and displays the 
#elements along with its index number.

numbers = [4, 2, 5, 7, 8]
for i, v in enumerate(numbers):
    print('Numbers[', i, '] =', v)
```

**Output:**
```text
Numbers[ 0 ] = 4
Numbers[ 1 ] = 2
Numbers[ 2 ] = 5
Numbers[ 3 ] = 7
Numbers[ 4 ] = 8
```

```python
# Example 2: Printing the elements of the list with its index number using the `range()` function

numbers = [1, 2, 4, 6, 8]
size = len(numbers)
for i in range(size):
    print('Index:', i, " ", 'Value:', numbers[i])
```

**Output:**
```text
Index: 0   Value: 1
Index: 1   Value: 2
Index: 2   Value: 4
Index: 3   Value: 6
Index: 4   Value: 8
```

## Iterate String using `for` loop

By looping through the **string** using **`for`** loop, we can do lots of string operations. Let’s see how to perform various string operations using a **`for`** loop.

```python
# Example 1: For loop with string

# Method 1:
language = 'Python'
for letter in language:
    print(letter)

# Method 2: using range() function

for i in range(len(language)):
    print(language[i])
```

**Output:**
```text
P
y
t
h
o
n
P
y
t
h
o
n
```

```python
# Example 2: Printing the elements of a string using for loop

for i in 'Hello World':
    print(i)
```

**Output:**
```text
H
e
l
l
o
 
W
o
r
l
d
```

```python
# Example 3: Access all characters of a string

name = "Alan"
for i in name:
    print(i, end=' ')
```

**Output:**
```text
A l a n
```

```python
# Example 4: Iterate string in reverse order

name = "Alan"
for i in name[::-1]:
    print(i, end=' ')
```

**Output:**
```text
n a l A
```

```python
# Example 5: Iterate over a particular set of characters in string

name = "Alan Watson"
for char in name[2:7:1]:
    print(char, end=' ')
```

**Output:**
```text
a n   W a
```

```python
# Example 6: Iterate over words in a sentence using the `split()` function.

dialogue = "Remember, Red, hope is a good thing, maybe the best of things, and no good thing ever dies"
# split on whitespace
for word in dialogue.split():
    print(word)
```

**Output:**
```text
Remember,
Red,
hope
is
a
good
thing,
maybe
the
best
of
things,
and
no
good
thing
ever
dies
```

```python
# Example 7:

for ch in 'abc':
    print(ch)
total = 0
for i in range(5):  # from 0 to 4
    total += i  # total = 0+1+2+3+4 = 10
for i,j in [(1,2),(3,1)]:  # [(1),(3)]
    total += i**j  # total = 1+3 = 4
print("total =",total)
```

**Output:**
```text
a
b
c
total = 14
```

## Iterate List using `for` loop

**Python list** is an ordered collection of items of different data types. It means Lists are ordered by index numbers starting from 0 to the total items-1. List items are enclosed in square **`[]`** brackets.

Below are the few examples of Python list.

```python
>>> numers = [1,2,4,6,7]
>>> players = ["Messi", "Ronaldo", "Neymar"]
```
Using a loop, we can perform various operations on the list. There are ways to iterate through elements in it. Here are some examples to help you understand better.

```python
# Example 1: Iterate over a list Method 1

numbers = [1, 2, 3, 6, 9]
for num in numbers:
    print(num)
```

**Output:**
```text
1
2
3
6
9
```

```python
# Example 2: Iterate over a list Method 2 (list comprehension)

numbers = [1, 2, 3, 6, 9]
[print(i) for i in numbers]
```

**Output:**
```text
1
2
3
6
9
[None, None, None, None, None]
```

```python
# Example 3: Iterate over a list using a for loop and range.

numbers = [1, 2, 3, 6, 9]
size = len(numbers)
for i in range(size):
    print(numbers[i])
```

**Output:**
```text
1
2
3
6
9
```

```python
# Example 4: printing the elements of a list using for loop

even_numbers = [2, 4, 6, 8, 10]  # list with 5 elements
for i in even_numbers:
    print(even_numbers)
```

**Output:**
```text
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]
```

```python
# Example 5: printing the elements of a list using for loop

list = [60, "HelloWorld", 90.96]
for i in list:
    print(i)
```

**Output:**
```text
60
HelloWorld
90.96
```

```python
# Example 6: Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 6, 11]  # list with 9 elements

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)
```

**Output:**
```text
The sum is 50
```

```python
# Example 7: Calculate the square of each number using for loop.

numbers = [1, 2, 3, 4, 5]
# iterate over each element in list num
for i in numbers:
    # ** exponent operator
    square = i ** 2
    print("Square of:", i, "is:", square)
```

**Output:**
```text
Square of: 1 is: 1
Square of: 2 is: 4
Square of: 3 is: 9
Square of: 4 is: 16
Square of: 5 is: 25
```

**Explanation:** **`i`** iterates over the 0,1,2,3,4. Every time it takes each value and executes the algorithm inside the loop. It is also possible to iterate over a nested list illustrated below.

```python
# Example 8: Calculate the average of list of numbers

numbers = [10, 20, 30, 40, 50]

# definite iteration
# run loop 5 times because list contains 5 items
sum = 0
for i in numbers:
    sum = sum + i
list_size = len(numbers)
average = sum / list_size
print(average)
```

**Output:**
```text
30.0
```

```python
# Example 9: Printing a list using range function

color = ['Green', 'Pink', 'Blue']  # list with total 3 elements
print(len(color))  # print length of color
for i in range(len(color)):
    print(color[i])
```

**Output:**
```text
3
Green
Pink
Blue
```

```python
# Example 10: Printing a list using range function

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # list with 3 elements
for list1 in list_of_lists:
        print(list1)
```

**Output:**
```text
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```

## Iterate Tuple using `for` loop

**Python list** Only the difference is that list is enclosed between square bracket **`[]`**, tuple between parentheses **`()`** and we cannot change the elements of a tuple once it is assigned, i.e., **immutable** whereas we can change the elements of a list i.e., **mutable**.

Below are the few examples of Python list.

```python
>>> numers = (1,2,4,6,7)
>>> players = ("Messi", "Ronaldo", "Neymar")
```
Using a loop, we can perform various operations on the tuple. There are ways to iterate through elements in it. Here are some examples to help you understand better.

```python
# Example 1: For loop with tuple

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

**Output:**
```text
0
1
2
3
4
5
```

## Iterate Dictionary using `for` loop

**Python dictionary** is used to store the items in the format of **key-value** pair. It doesn’t allow duplicate items. It is enclosed with **`{}`**. Here are some of the examples of dictionaries.

```python
>>> dict1 = {1: "Apple", 2: "Ball", 3: "Cat"}
>>> dict2 = {"Antibiotics": "Penicillin", "Inventor": "Fleming", "Year": 1928}
```

There are ways to iterate through **key-value** pairs. Here are some examples to help you understand better.

```python
# Example 1: Access only the keys of the dictionary.

dict1 = {"Antibiotics": "Penicillin", "Inventor": "Fleming", "Year": 1928}
for key in dict1:
    print(key)
```

**Output:**
```text
Antibiotics
Inventor
Year
```

```python
# Example 2: Iterate keys and values of the dictionary

dict1 = {"Vaccine": "Polio", "Inventor": "Salk", "Year": 1953}
for key in dict1:
    print(key, "->", dict1[key])
```

**Output:**
```text
Vaccine -> Polio
Inventor -> Salk
Year -> 1953
```

```python
# Example 3: Iterate only the values the dictionary

dict1 = {"Vaccine": "Smallpox ", "Inventor": "Jenner", "Year": 1796}
for value in dict1.values():
    print(value)
```

**Output:**
```text
Smallpox 
Jenner
1796
```

```python
# Example 4: For loop with dictionary
#Looping through a dictionary gives you the key of the dictionary.

person = {
    'first_name':'Milaan',
    'last_name':'Parmar',
    'age':96,
    'country':'Finland',
    'is_marred':True,
    'skills':['Python', 'Matlab', 'R', 'C', 'C++'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
```

**Output:**
```text
first_name
last_name
age
country
is_marred
skills
address
first_name Milaan
last_name Parmar
age 96
country Finland
is_marred True
skills ['Python', 'Matlab', 'R', 'C', 'C++']
address {'street': 'Space street', 'zipcode': '02210'}
```

## Iterate Set using `for` loop

**Python sets** is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

However, a set itself is **mutable**. We can add or remove items from it.

```python
>>> my_set = {1, 2, 3}
>>> my_vaccine = {"Penicillin", "Fleming", "1928"}
```

Sets can also be used to perform mathematical set operations like **union**, **intersection**, **symmetric difference**, etc.

```python
# Example 6: For loop with set

mix_fruits = {'Banana', 'Apple', 'Mango', 'Orange', 'GUava', 'Kiwi', 'Grape'}
for fruits in mix_fruits:
    print(fruits)
```

**Output:**
```text
GUava
Banana
Grape
Kiwi
Orange
Apple
Mango
```

## 💻 Exercises ➞ <span class='label label-default'>List</span>

### Exercises ➞ <span class='label label-default'>Level 1</span>

1. Iterate 0 to 10 using **`for`** loop, do the same using **`while`** loop.
2. Iterate 10 to 0 using **`for`** loop, do the same using **`while`** loop.
3. Write a loop that makes seven calls to **`print()`**, so we get on the output the following triangle:

```py
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
```

4. Use nested loops to create the following:

```py
      #
     ###
    #####
   #######
  #########
 ###########
#############
```

5. Print the following pattern using loops

```py
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
```

6. Iterate through the list, ['Python', 'Numpy','Pandas','Scikit', 'Pytorch'] using a **`for`** loop and print out the items.
7. Use **`for`** loop to iterate from 0 to 100 and print only even numbers
8. Use **`for`** loop to iterate from 0 to 100 and print only odd numbers
   
### Exercises ➞ <span class='label label-default'>Level 2</span>
    
1.  Use **`for`** loop to iterate from 0 to 100 and print the sum of all numbers.

```py
   The sum of all numbers is 5050.
```

1. Use **`for`** loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

```py
    The sum of all evens is 2550. And the sum of all odds is 2500.
```

### Exercises ➞ <span class='label label-default'>Level 3</span>

1. Go to the data folder and use the **countries.py** file. Loop through the countries and extract all the countries containing the word **`land`**.
1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
2. Go to the data folder and use the **countries_data.py** file. 
   1. What are the total number of languages in the data
   2. Find the ten most spoken languages from the data
   3. Find the 10 most populated countries in the world

---

## 📘 Python While Loop
*Source: `3. Python Flow Control/6. Python while Loop.ipynb`*

# Loops in Python

Loops in Python programming function similar to loops in C, C++, Java or other languages. Python loops are used to repeatedly execute a block of statements until a given condition returns to be **`False`**. In Python, we have **two types of looping statements**, namely:
<div>

</div>

# Python `while` Loop

Loops are used in programming to repeat a specific block of code. In this article, you will learn to create a **`while`** loop in Python. We use a **`while`** loop when we want to repeat a code block.

## What is `while` loop in Python?

The **`while`** loop in Python is used to iterate over a block of code as long as the  expression/condition is **`True`**. When the condition becomes **`False`**, execution comes out of the loop immediately, and the first statement after the **`while`** loop is executed.

We generally use this loop when we don't know the number of times to iterate beforehand.

Python interprets any non-zero value as **`True`**. **`None`** and **`0`** are interpreted as **`False`**.

## Why and When to use `while` loop in Python

Now, the question might arise: when do we use a **`while`** loop, and why do we use it.

* **Automate and repeat tasks:** As we know, **`while`** loops execute blocks of code over and over again until the condition is met it allows us to automate and repeat tasks in an efficient manner.
* **Indefinite Iteration:**The **`while`** loop will run as often as necessary to complete a particular task. When the user doesn’t know the number of iterations before execution, **`while`** loop is used instead of a **for loop** loop
* **Reduce complexity:** **`while`** loop is easy to write. using the loop, we don’t need to write the statements again and again. Instead, we can write statements we wanted to execute again and again inside the body of the loop thus, reducing the complexity of the code
* **Infinite loop:** If the code inside the **`while`** loop doesn’t modify the variables being tested in the loop condition, the loop will run forever.

### Syntax: 

```python
while condition:
    body of while loop
```
1. In the **`while`** loop, expression/condition is checked first.
2. The body of the loop is entered only if the expression/condition evaluates to **`True`**.
3. After one iteration, the expression/condition is checked again. This process continues until the test_expression evaluates to **`False`**.

<div>

</div>

>**Note:** An infinite loop occurs when a program keeps executing within one loop, never leaving it. To exit out of infinite loops on the command line, press **CTRL + C**.

```python
# Example 1: Print numbers less than 5

count = 1
# run loop till count is less than 5
while count < 5:
    print(count)
    count = count + 1
```

**Output:**
```text
1
2
3
4
```

```python
# Example 2:

num = 10
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i + 1
print("Sum of first 10 number is:", sum)
```

**Output:**
```text
Sum of first 10 number is: 55
```

```python
# Example 3:

a=10        # 'a' is my variable

while a>0:  # Enter the body of while loop because condition is TRUE
    print (("Value of a is"),a)
    a=a-2
print ("Loop is Completed")
```

**Output:**
```text
Value of a is 10
Value of a is 8
Value of a is 6
Value of a is 4
Value of a is 2
Loop is Completed
```

```python
# Example 4:

n=153
sum=0

while n>0:
    r=n%10   # r is the remainder of the division
    sum+=r   # sum+=r is equal to sum = sum+r
    n=n/10
print (sum)
```

**Output:**
```text
9.999999999999998
```

```python
# Example 5: How many times a given number can be divided by 3 before it is less than or equal to 10.

count = 0
number = 180
while number > 10:
    # divide number by 3
    number = number / 3
    # increase count
    count = count + 1
print('Total iteration required', count)
```

**Output:**
```text
Total iteration required 3
```

```python
# Example 6: Program to add natural numbers up to sum = 1+2+3+...+n

# To take input from the user, 
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter, i.e., the value of i will change from 1 to 2 in next iteration...

# print the sum
print("The sum is", sum)
```

**Output:**
```text
The sum is 55
```

**Explanation:**

In the above program, the test expression will be **`True`** as long as our counter variable **`i`** is less than or equal to **`n`** (10 in our program).

We need to increase the value of the counter variable in the body of the loop. This is very important (and mostly forgotten). Failing to do so will result in an infinite loop (never-ending loop).

Finally, the result is displayed.

```python
# Example 7: simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print() # line ending
```

**Output:**
```text
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
```

## `while` loop with `if-else`

A **`while`** loop can have an optional **if-else** block. We use **`if-else`** statement in the loop when conditional iteration is needed. i.e., If the condition is **`True`**, then the statements inside the if block will execute othwerwise, the else block will execute.

```python
# Example 1: Print even and odd numbers between 1 to the entered number.

n = int(input('Please Enter Number '))
while n > 0:
    # check even and odd
    if n % 2 == 0:
        print(n, 'is a even number')
    else:
        print(n, 'is a odd number')
    # decrease number by 1 in each iteration
    n = n - 1
```

**Output:**
```text
Please Enter Number 9
9 is a odd number
8 is a even number
7 is a odd number
6 is a even number
5 is a odd number
4 is a even number
3 is a odd number
2 is a even number
1 is a odd number
```

```python
# Example 2: printing the square of odd numbers less than n. 

n =10
i = 1
while i < n:
    #if (i % 2 == 0): (for even numbers)
    if (i % 2 != 0):
        print(i ** 2)
        i = i + 1
    else:
        print(i)
        i = i + 1
```

**Output:**
```text
1
2
9
4
25
6
49
8
81
```

```python
# Example 3: Add all even numbers from 1 to 10 using while loop
# 2+4+6+8+10

# n = int(input("Please enter the maximum value: "))
n = 10

sum = 0
i = 1

while i <= n:
    if(i%2==0):
        sum = sum + i
#        sum += i
    i = i+1
    
# print the sum
print("The sum is", sum)
```

**Output:**
```text
The sum is 30
```

```python
# Example 4: Write a code to add all the prime numbers between 17 to 53 using while loop
# 17, 19, 23, 29, 31, 37, 41, 43, 47, 53

'''Method 1'''

sum=0
for i in range(17,54):
    k=2
    if i>=2:
        while i % k!=0:
            k+=1
        if i==k:
            sum += i
            print(i)
print("The total sum is",sum)
```

**Output:**
```text
17
19
23
29
31
37
41
43
47
53
The total sum is 340
```

## `while` loop with `else`

A **`while`** loop can have an optional **`else`** block as well. The **`else`** part is executed if the condition in the **`while`** loop evaluates to **`False`**.

The **`else`** will be skipped/ignored when:

* **`while`** loop terminates abruptly
* The **break statement** is used to break the **`while`** loop

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

**Output:**
```text
0
1
2
3
4
5
```

**Explanation:**

The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed.

```python
# Example 1: Use while loop to print numbers from 1 to 6

i = 1
while i <= 6:
    print(i)
    i = i + 1
else:
    print("Done. 'while loop' executed normally")
```

**Output:**
```text
1
2
3
4
5
6
Done. 'while loop' executed normally
```

```python
# Example 2: Else block with break statement in a while loop.

i = 1
while i <= 6:
    print(i)
    if i == 3:
        break
    i = i + 1
else:
    print("Done. `while loop` executed normally")
```

**Output:**
```text
1
2
3
```

```python
# Example 3:
'''Example to illustrate the use of else statement with the while loop'''

counter = 0  # counter is my variable

while counter < 3:
    print("Inside while loop")
    counter = counter + 1  # increment the counter
else:
    print("Inside else")
```

**Output:**
```text
Inside while loop
Inside while loop
Inside while loop
Inside else
```

**Explanation:**

Here, we use a **`counter`** variable to print the string **`Inside loop`** three times.

On the fourth iteration, the condition in **`while`** becomes **`False`**. Hence, the **`else`** part is executed.

```python
# Example 4: we want a user to enter any number between 100 and 600

number = int(input('Enter any number between 100 and 600 '))
# number greater than 100 and less than 600
while number < 100 or number > 600:
    print('Incorrect number, Please enter correct number:')
    number = int(input('Enter a Number between 100 and 600 '))
else:
    print("Given Number is correct", number)
```

**Output:**
```text
Enter any number between 100 and 600 555
Given Number is correct 555
```

## Using Control Statement in `while` loops in Python

**Control statements** in Python like **`break`**, **`continue`**, etc can be used to control the execution flow of **`while`** loop in Python. Let us now understand how this can be done.

It is used when you want to exit a loop or skip a part of the loop based on the given condition. It also knows as **transfer statements**.

### a) `break` in `while` loop

Using the **`break`** statement, we can exit from the **`while`** loop even if the condition is **`True`**. 

If the **`break`** statement is used inside a nested loop (loop inside another loop), it will terminate the innermost loop. For example,

```python
# Example 1:

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

**Output:**
```text
0
1
2
```

**Explanation**: 

Here, the **`while`** loop runs until the value of the variable **`i`** is less than 5. But because of the **`break`** statement, the loop gets terminated when the value of the variable **`i`** is 3 and it prints 0, 1, 2

```python
# Example 2:

list = [60, "HelloWorld", 90.45, 50, 67.23, "Python"]  # total 6 elements
i = 0
while(i < 6):
    print(list[i])
    i = i + 1
    if(i == 3):
        break
```

**Output:**
```text
60
HelloWorld
90.45
```

**Explanation**: 

Here, the **`while`** loop runs until the value of the variable **`i`** is less than 6. But because of the **`break`** statement, the loop gets terminated when the value of the variable **`i`** is 3.

```python
# Example 3: Display each character from a string and if `a` character is number then stop the loop.

name = 'Alan99White'
size = len(name)
i = 0
# iterate loop till the last character
while i < size:
    # break loop if current character is number
    if name[i].isdecimal():
        break;
    # print current character
    print(name[i], end=' ')
    i = i + 1
```

**Output:**
```text
A l a n
```

### b) `continue` in while loop

The **`continue`** statement is used to stop/skip the block of code in the loop for the current iteration only and continue with the next iteration. 

For example, let's say you want to print all the odd numbers less than a particular value. Here is how you can do it using **`continue`** keyword in Python.

```python
# Example 1:

count = 0
while count < 5:
    if count == 3:
        continue        
    else:
        print(count)
        count = count + 1
```

**Output:**
```text
0
1
2
```

**Explanation:**

The above **`while`** loop only prints 0, 1, 2 and 4 (skips 3).

```python
# Example 2: printing odd numbers less than `n`

n=10
i = 1
while (i < n):
    if (i % 2 == 0):
        i = i + 1
        continue  # continue means skip the current loop
    else:
        print (i)
        i = i + 1
```

**Output:**
```text
1
3
5
7
9
```

**Explanation:**

Here, the **`continue`** statement gets executed when the value of the variable is an even number. This simply means, whenever it is an even number, we simply skip all other statements and execute the next iteration.

```python
# Example 3: Write a while loop to display only alphabets from a string.

name = 'Alan99White'

size = len(name)
i = -1
# iterate loop till the last character
while i < size - 1:
    i = i + 1
    # skip while loop body if current character is not alphabet
    if not name[i].isalpha():
        continue
    # print current character
    print(name[i], end=' ')
```

**Output:**
```text
A l a n W h i t e
```

### c) `pass` in `while` loop

The **`pass`** statement is a null statement, i.e., nothing happens when the statement is executed. Primarily it is used in empty functions or classes. When the interpreter finds a pass statement in the program, it returns no operation.

```python
# Example 1:

n = 4
while n > 0:
    n = n - 1
    pass
```

## Reverse `while` loop

A reverse loop means an iterating loop in the backward direction. A simple example includes:

* Display numbers from 10 to 1.
* Reverse a string or list

```python
# Example 1: Reverse a while loop to display numbers from 10 to 1

# reverse while loop
i = 10
while i >= 0:
    print(i, end=' ')
    i = i - 1
```

**Output:**
```text
10 9 8 7 6 5 4 3 2 1 0
```

## Nested `while` loops

**Nested while loop** is a **`while`** loop inside another **`while`** a loop. 

In the nested **`while`** loop, the number of iterations will be equal to the number of iterations in the outer loop multiplied by the iterations in the inner loop. In each iteration of the outer loop inner loop execute all its iteration.

**Syntax:**

```python
while expression:
    while expression:
        statement(s)
    statement(s)
```

### `while` loop inside `while` loop

#### Example: Nested `while` loop

```python
# Example: print the first 10 numbers on each line 5 times

i = 1
while i <= 3:
    j = 1
    while j <= 10:
        print(j, end='')
        j = j + 1
    i = i + 1
    print()
```

**Output:**
```text
12345678910
12345678910
12345678910
```

#### Example: Nested `while` loop to print the pattern

```python
*
* *
* * *
* * * *
* * * * *
```

```python
# Example 1: Method 1

i = 1
# outer while loop
# 5 rows in pattern
while i < 6:
    j = 0
    # nested while loop
    while j < i:
        print('*', end=' ')
        j = j + 1
    # end of nested while loop
    # new line after each row
    print('')
    i = i + 1
```

**Output:**
```text
* 
* * 
* * * 
* * * * 
* * * * *
```

### `for` loop inside `while` loop

We can also use **for loop** inside a **`while`** loop as a nested loop. For example,

```python
# Example 1: Method 2

i = 1
# outer while loop
while i < 6:
    # nested for loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')
    i = i + 1
```

**Output:**
```text
* 
* * 
* * * 
* * * * 
* * * * *
```

```python
# Example 2: Write a code to add all the prime numbers between 17 to 53 using while loop
# 17, 19, 23, 29, 31, 37, 41, 43, 47, 53

'''Method 1'''

n=17
sum=0
while n<=53:
    for i in range(2,n):
        if(n % i)== 0: 
            break
        else:
            i=i+1
    else:
        sum=sum+n
        print(n)
    n=n+1
print("The total sum is",sum)
```

**Output:**
```text
17
19
23
29
31
37
41
43
47
53
The total sum is 340
```

```python
# Example 3:

print('Show Perfect number fom 1 to 100')
n = 2

while n <= 100:            # outer while loop
    x_sum = 0    
    for i in range(1, n):  # inner for loop
        if n % i == 0:
            x_sum += i
    if x_sum == n:
        print('Perfect number:', n)
    n += 1
```

**Output:**
```text
Show Perfect number fom 1 to 100
Perfect number: 6
Perfect number: 28
```

## Iterate String using `while` loop

By looping through the **string** using **`while`** loop, we can do lots of string operations. For example,

```python
# Example 1: while loop to iterate string letter by letter

name = "Alan"
i = 0
res = len(name) - 1
while i <= res:
    print(name[i])
    i = i + 1
```

**Output:**
```text
A
l
a
n
```

## Iterate List using `while` loop

**Python list**  is an ordered collection of items of different data types. It means Lists are ordered by index numbers starting from 0 to the total items-1. List items are enclosed in square **`[]`** brackets.

Below are the few examples of Python list.

```python
>>> numers = [1,2,4,6,7]
>>> players = ["Messi", "Ronaldo", "Neymar"]
```
Using a loop, we can perform various operations on the list. There are ways to iterate through elements in it. Here are some examples to help you understand better.

```python
# Example 1: Use while loop to iterate over a list.

numbers = [1, 2, 3, 6, 9]
size = len(numbers)
i = 0
while i < size:
    print(numbers[i])
    i = i + 1
```

**Output:**
```text
1
2
3
6
9
```

```python
# Example 2: printing the first two elements of a list

list = [60, "HelloWorld", 90.96]  # list with three elements
i = 0
while(i < 2):
    print (list[i]) #printing the element in the index i
    i = i + 1
```

**Output:**
```text
60
HelloWorld
```

>**Note**: When working with the **`while`** loop, it is important to declare the indexing variable **`i`** beforehand and to increment the indexing variable accordingly. Else it will result in an infinite loop.

## Iterate Numbers using `while` loop

Now, consider a program where you want to print out the squares of all the **numbers** less a particular number. Let's see how this works with a while statement.

```python
# Example 1: printing the square of numbers less than `n`

i = 1
while (i <= 10):
    print (i ** 2) #printing the element in the index i
    i = i + 1
```

**Output:**
```text
1
4
9
16
25
36
49
64
81
100
```

```python
# Example 2: Find the cube of number from 1 to 9.

i = 1
while(i<10):
    print(i*i*i)
#   print(i**3)
    i=i+1
```

**Output:**
```text
1
8
27
64
125
216
343
512
729
```

```python
# Example 3:

i = 1
while i < 3:
    print(i ** 2)
    i = i+1
print('Loop over')
```

**Output:**
```text
1
4
Loop over
```

## While loop in Python FAQs


1. A while loop in python is used for what type of iteration?
> A while loop is ideal for iteration when the number of iterations is not known. Also, it is ideal to use a while loop when you have a condition that needs to be satisfied.


2. Why does infinite while loop occur in Python?
> A loop becomes an infinite loop if the while condition never becomes FALSE. Such a loop that never terminates is called an infinite loop.


3. Is there a do...while loop in Python?
>No. There is no do while loop in Python.


4. How do you break a while loop in Python?
>Usually, the control shifts out of the while loop when the while condition is no False. Or you can use various control statements like break, continue, etc to break out of the while loop or break of the particular iteration of the while loop.


5. How to write an empty while function in Python?
>You can write an empty while function in Python using the pass statements. Here is how you can write it.

```python
#empty while statement in python
>>> i = 0
>>> while (i < 10) :
>>>     pass
```

---

## 📘 Python Break Continue Pass Statements
*Source: `3. Python Flow Control/7. Python break continue pass statements.ipynb`*

# Control Statements in Python

As you may know, loops in Python are used to iterate repeatedly over a block of code. But at times, you might want to **shift the control once a particular condition is satisfied**. This is where control statements in Python come into the picture.

Control statements in python are **used to control the flow of execution of the program based on the specified conditions**. Python supports **3 types of control statements**:

|      | Statement | Description |
|:----|:----| :--- |
|1| **`break`** | Terminate the current loop. Use the **`break`** statement to come out of the loop instantly. |
|2| **`continue`** | Skip the current iteration of a loop and move to the next iteration |
|3| **`pass`** | Do nothing. Ignore the condition in which it occurred and proceed to run the program as usual |

Loops iterate over a block of code until the test expression is **`False`**, but sometimes we wish to terminate the current iteration or even the whole loop without checking test expression.

The **`break`** and **`continue`** statements are part of a control flow statements that helps you to understand the basics of Python.

<div>

</div>

# 1. Python `break` statement

In Python, the **`break`** statement provides you with the opportunity to **exit out** of a loop when an external condition is **triggered**, and the program control transfer to the next statement following the loop.

If the **`break`** statement is inside a nested loop (loop inside another loop), the **`break`** statement will terminate the innermost loop.

You’ll put the **`break`** statement within the block of code under your loop statement, usually after a conditional **if statement**. This statement can only be used in **for loop** and **while loop**.

<div>

</div>

The working of **`break`** statement in **`for`** loop and **`while`**  loop is shown below.

<div>

</div>

```python
# Example 1:

numbers = [10, 30, 120, 330]
for i in numbers:
    if i > 100:
        break
    print('current number', i)
```

**Output:**
```text
current number 10
current number 30
```

```python
# Example 2: Let’s look at an example that uses the break statement in a `for` loop

number = 0
for number in range(10):
    number = number + 1
    if number == 5:
        break    # break here
    print('Number is ' + str(number))
print('Out of loop')
```

**Output:**
```text
Number is 1
Number is 2
Number is 3
Number is 4
Out of loop
```

**Explanation:**

1. In this small program, the variable number is initialized at **`0`**. Then a **`for`** statement constructs the loop as long as the variable number is **less than 10**.

2. Within the **`for`** loop, the number increases incrementally by **`1`** with each pass because of the line **number = number + 1**.

3. Then, there is an **`if`** statement that presents the condition that if the variable number is **equivalent** to the integer **`5`**, then the loop will break.

4. Within the loop is also a **print()** statement that will execute with each iteration of the **`for`** loop until the loop breaks, since it is after the **`break`** statement.

5. To see when we are out of the loop, we have included a final **`print()`** statement outside of the **`for`** loop.

This shows that once the integer number is evaluated as equivalent to **`5`**, the loop breaks, as the program is told to do so with the **`break`** statement.

## Nested `break` loops

### 1. `break` Statement in Nested Loop

To terminate the nested loop, use a **`break`** statement inside the inner loop. For example:

```python
# Example 1:

for i in range(100):
    print(i,end="...")
    if i>=10:
        break
print("completed.")
```

**Output:**
```text
0...1...2...3...4...5...6...7...8...9...10...completed.
```

```python
# Example 2: Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)
print("The end")
```

**Output:**
```text
s
t
r
The end
```

**Explanation:**

In this program, we iterate through the "**`string`**" sequence. We check if the letter is **`i`**, upon which we break from the loop. Hence, we see in our output that all the letters up till **`i`** gets printed. After that, the loop terminates.

Print the letters in "HELLOWORLD" one by one untill the letter R is reached using break statement in Python.

```python
# Example 3: 

for letter in "HELLOWORLD":   # letter is a variable which could have been with any name. each iteration the letter is advanced in the string "FACEPREP" and stored in variable letter.
    if letter == "R":        #check for condition
        break               # if condition true, then break out of the loop and print the final print statement.
    print(letter)       # if condition false, then print that letter.
print('untill letter R printed')    #once the for loop is terminated, print this. 

# Note: observe the indentations carefully
```

**Output:**
```text
H
E
L
L
O
W
O
untill letter R printed
```

```python
# Example 4: program to check if letter 'A' is present in the input

a = input ("Enter a word: ")
for i in a:
    if (i == 'A'):
        print ("A is found")
        break 
else:
    print ("A not found")
    
# Note: Python is case-sensitive language.
```

**Output:**
```text
Enter a word: Happy
A not found
```

```python
# Example 5: bested `while` loop with `break`

name = 'Alan99 White'

size = len(name)
i = 0
# iterate loop till the last character
while i < size:
    # break loop if current character is space
    if name[i].isspace():
        break
    # print current character
    print(name[i], end=' ')
    i = i + 1
```

**Output:**
```text
A l a n 9 9
```

```python
# Example 6:

for i in range(1, 11):
    print('Multiplication table of', i)
    for j in range(1, 11):
        # condition to break inner loop
        if i > 5 and j > 5:
            break
        print(i * j, end=' ')
    print('')
```

**Output:**
```text
Multiplication table of 1
1 2 3 4 5 6 7 8 9 10 
Multiplication table of 2
2 4 6 8 10 12 14 16 18 20 
Multiplication table of 3
3 6 9 12 15 18 21 24 27 30 
Multiplication table of 4
4 8 12 16 20 24 28 32 36 40 
Multiplication table of 5
5 10 15 20 25 30 35 40 45 50 
Multiplication table of 6
6 12 18 24 30 
Multiplication table of 7
7 14 21 28 35 
Multiplication table of 8
8 16 24 32 40 
Multiplication table of 9
9 18 27 36 45 
Multiplication table of 10
10 20 30 40 50
```

**Explanation:**

We have two loops, the outer loop, and the inner loop. The outer for loop iterates the first 10 numbers using the **range()** function, and the internal loop prints the multiplication table of each number.

But if the current number of both the outer loop and the inner loop is greater than 5 then terminate the inner loop using the **`break`** statement.

### 2. `break` Statement in Outer Loop

To terminate the outside loop, use a **`break`** statement inside the outer loop. For example:

```python
# Example 1: Break nested loop

for i in range(1, 11):
    # condition to break outer loop
    if i > 5:
        break
    print('Multiplication table of', i)
    for j in range(1, 11):
        print(i * j, end=' ')
    print('')
```

**Output:**
```text
Multiplication table of 1
1 2 3 4 5 6 7 8 9 10 
Multiplication table of 2
2 4 6 8 10 12 14 16 18 20 
Multiplication table of 3
3 6 9 12 15 18 21 24 27 30 
Multiplication table of 4
4 8 12 16 20 24 28 32 36 40 
Multiplication table of 5
5 10 15 20 25 30 35 40 45 50
```

**Explanation:**

We have two loops, the outer loop, and the inner loop. The outer loop iterates the first 10 numbers, and the internal loop prints the multiplication table of each number.

But if the current number of the outer loop is greater than 5 then terminate the outer loop using the **`break`** statement.

```python
# Example 2:

numbers = [3, 6, 12, 9]
for i in numbers:
    print('Current Number is:', i)
    # skip below statement if number is greater than 10
    if i > 10:
        continue
    square = i * i
    print('Square of a current number is:', square)
```

**Output:**
```text
Current Number is: 3
Square of a current number is: 9
Current Number is: 6
Square of a current number is: 36
Current Number is: 12
Current Number is: 9
Square of a current number is: 81
```

```python
# Example 3: Python Continue Statement Example:

a=0

while a<=5:
    a=a+1
    if a%2==0: 
        continue
    print (a)
print ("End of Loop")
```

**Output:**
```text
1
3
5
End of Loop
```

**Explanation:**

You can use the **`continue`** statement to avoid deeply nested conditional code, or to optimize a loop by eliminating frequently occurring cases that you would like to reject.

The **`continue`** statement causes a program to skip certain factors that come up within a loop, but then continue through the rest of the loop.

```python
# Example 4: Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
```

**Output:**
```text
s
t
r
n
g
The end
```

**Explanation**:

This program is same as the above example except the **`break`** statement has been replaced with **`continue`**.

We continue with the loop, if the string is **`i`**, not executing the rest of the block. Hence, we see in our output that all the letters except **`i`** gets printed.

```python
# Example 5:

for i in range(10):
    if i>4:
        print("Ignored",i)
        continue
    # this statement is not reach if i > 4
    print("Processed",i)
```

**Output:**
```text
Processed 0
Processed 1
Processed 2
Processed 3
Processed 4
Ignored 5
Ignored 6
Ignored 7
Ignored 8
Ignored 9
```

Write a program to skip all "O"s in a given string "HELLOWORLD"

```python
# Example 6:

for letters in "HelloWorld":  # for every letter in FACEPREP
    if letters == "O":      # if letter is E, then skip printing the letter and go to the next iteration with the next alphabet
        continue            # Remember that loop is not terminated like break statement.
    print(letters)
print("The End")
```

**Output:**
```text
H
e
l
l
o
W
o
r
l
d
The End
```

# 2. Python `continue` statement

In Python, the **`continue`** statement is a **jump statement** which is used to skip execution of current iteration. After **skipping**, loop **`continue`** with next iteration. We can use **`continue`** statement **only** with **for loop** as well as **while loop** in Python. It is typically **only** used within an **if statement** (otherwise the remainder of the loop would never be executed).

<div>

</div>

The working of **`continue`** statement in **`for`** loop and **`while`** loop is shown below.

<div>

</div>

## `continue` statement in `while` loop

We can also use the **`continue`** statement inside a **`while`** loop. For example:

Write a **while loop** to display each character from a string and if a character is a space, then don’t display it and move to the next character.

Use the if condition with the **`continue`** statement to jump to the next iteration. If the current character is space, then the condition evaluates to true, then the **`continue`** statement will execute, and the loop will move to the next iteration by skipping the remeaning body.

```python
# Example 1: use the `continue` statement inside a `while` loop

name = 'Art hu r'

size = len(name)
i = -1
# iterate loop till the last character
while i < size - 1:
    i = i + 1
    # skip loop body if current character is space
    if name[i].isspace():
        continue
    # print current character
    print(name[i], end=' ')
```

**Output:**
```text
A r t h u r
```

## `continue` statement with `else` statements

Sometimes we want to know if a loop exited 'normally' or via a **`break`** statement. This can be achieved with an **`else:`** statement in a loop which only executes if there was no **`break`** statement.

```python
# Example 1: program to check if letter 'A' is present in the input

a = input ("Enter a word: ")
for i in a:
    if(i != 'A'):        
        continue        
    else:
        print("A is found")
        break
    print("A is not found")
    
# Enter a word: Honey is sweet
```

**Output:**
```text
Enter a word: Honey is sweet
```

```python
# Example 1 :without using continue

a = input ("Enter a word: ")
for i in a:
    if (i == 'A'):
        print("A is found")
        break
else:
    print ("A is not found")
    
# Enter a word: Honey is sweet
```

**Output:**
```text
Enter a word: Honey is sweet
A is not found
```

```python
# Example 2:

count = 0
while count < 10:
    count += 1
    if count % 2 == 0: # even number
        count += 2
        continue
    elif 5 < count < 9:
        break # abnormal exit if we get here!
    print("count =",count)
else: # while-else
    print("Normal exit with",count)
```

**Output:**
```text
count = 1
count = 5
count = 9
Normal exit with 12
```

## Nested `continue` loops

### 1. `continue` Statement in Nested Loop

To skip the current iteration of the nested loop, use the **`continue`** statement inside the body of the inner loop. For example:

```python
# Example 1: `continue` statement in nested loop

for i in range(1, 11):
    print('Multiplication table of', i)
    for j in range(1, 11):
        # condition to skip current iteration
        if j == 5:
            continue
        print(i * j, end=' ')
    print('')
```

**Output:**
```text
Multiplication table of 1
1 2 3 4 6 7 8 9 10 
Multiplication table of 2
2 4 6 8 12 14 16 18 20 
Multiplication table of 3
3 6 9 12 18 21 24 27 30 
Multiplication table of 4
4 8 12 16 24 28 32 36 40 
Multiplication table of 5
5 10 15 20 30 35 40 45 50 
Multiplication table of 6
6 12 18 24 36 42 48 54 60 
Multiplication table of 7
7 14 21 28 42 49 56 63 70 
Multiplication table of 8
8 16 24 32 48 56 64 72 80 
Multiplication table of 9
9 18 27 36 54 63 72 81 90 
Multiplication table of 10
10 20 30 40 60 70 80 90 100
```

**Explanation:**

We have the outer loop and the inner loop. The outer loop iterates the first 10 numbers, and the internal loop prints the multiplication table of each number.

But if the current number of the inner loop is equal to 5, then skip the current iteration and move to the next iteration of the inner loop using the **`continue`** statement.

### 2. `continue` Statement in Outer Loop

To skip the current iteration of an outside loop, use the **`continue`** statement inside the outer loop. For example:

```python
# Example 1: `continue` statement in outer loop

for i in range(1, 11):
    # condition to skip iteration
    # Don't print multiplication table of even numbers
    if i % 2 == 0:
        continue
    print('Multiplication table of', i)
    for j in range(1, 11):
        print(i * j, end=' ')
    print('')
```

**Output:**
```text
Multiplication table of 1
1 2 3 4 5 6 7 8 9 10 
Multiplication table of 3
3 6 9 12 15 18 21 24 27 30 
Multiplication table of 5
5 10 15 20 25 30 35 40 45 50 
Multiplication table of 7
7 14 21 28 35 42 49 56 63 70 
Multiplication table of 9
9 18 27 36 45 54 63 72 81 90
```

**Explanation:**

The outer loop iterates the first 10 numbers, and the internal loop prints the multiplication table of each number.

But if the current number of the outer loop is even, then skip the current iteration of the outer loop and move to the next iteration.

>**Note:** If we skip the current iteration of an outer loop, the inner loop will not be executed for that iteration because the inner loop is part of the body of an outer loop.

## Catching exceptions with `continue` statement

Sometimes it is desirable to deal with errors without stopping the whole program. This can be achieved using a **try** statement. Appart from dealing with with system errors, it also alows aborting from somewhere deep down in nested execution. It is possible to attach multiple error handlers depending on the type of the exception

```python
try:
    code
except <Exception Type> as <variable name>:
    # deal with error of this type
except:
    # deal with any error
finally:
    # execute irrespective of whether an exception occured or not
```

```python
try:
    count=0
    while True:
        while True:
            while True:
                print("Looping")
                count = count + 1
                if count > 3:
                    raise Exception("abort") # exit every loop or function
                if count > 4:
                    raise StopIteration("I'm bored") # built in exception type
except StopIteration as e:
    print("Stopped iteration:",e)
except Exception as e: # this is where we go when an exception is raised
    print("Caught exception:",e)
finally:
    print("All done")
```

**Output:**
```text
Looping
Looping
Looping
Looping
Caught exception: abort
All done
```

This can also be useful to handle unexpected system errors more gracefully:

```python
try:
    for i in [2,1.5,0.0,3]:
        inverse = 1.0/i
except Exception as e: # no matter what exception
    print("Cannot calculate inverse because:", e)
```

**Output:**
```text
Cannot calculate inverse because: float division by zero
```

# 3. Python `pass` statement

In Python, **`pass`** keyword is used to execute **nothing**; it means, when we don't want to execute code, the pass can be used to execute empty. It is same as the name refers to. It just makes the control to pass by without executing any code. If we want to bypass any code pass statement can be used.

It is used as a placeholder for future implementation of functions, loops, etc.

Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. They cannot have an empty body. The interpreter would give an error. So, we use the **`pass`** statement to construct a body that does nothing.

### Example:

```python
'''pass is just a placeholder for
functionality to be added later.'''
>>> sequence = {'p', 'a', 's', 's'}
>>> for val in sequence:
>>>     pass
```

We can do the same thing in an empty **function** or **class** as well.

```python
>>> def function(args):
>>>     pass
```
or
```python
>>> class Example:
>>>    pass
```

```python
# Example 1:

months = ['January', 'June', 'March', 'April']
for mon in months:
    pass
print(months)
```

**Output:**
```text
['January', 'June', 'March', 'April']
```

```python
# Example 2: Python Pass Statement

number = 0

for number in range(10):
    number = number + 1
    if number == 5:
        pass   # pass here
    print('Number is ' + str(number))
print('Out of loop')
```

**Output:**
```text
Number is 1
Number is 2
Number is 3
Number is 4
Number is 5
Number is 6
Number is 7
Number is 8
Number is 9
Number is 10
Out of loop
```

**Explanation**:

By using the **`pass`** statement in this program, we notice that the program runs exactly as it would if there were no conditional statement in the program. The **`pass`** statement tells the program to **disregard that condition** and **continue to run** the program as usual.

## Control Statements in Python FAQs

1. How many control statements are present in Python?
> In Python, there are 3 types of control statements. Namely, break, continue and pass statements.

2. How to break from a loop in Python?
>The keyword break is used to break or terminate from the current loop. The control shifts to the next statement outside the loop.

3. What is the difference between break and continue statements in Python?
>Break statement exits out of the loop, but the continue statement shifts the control to the next iteration and doesn’t exit out of the loop.

4. Can we use continue in if statement in Python?
>Yes. Continue statements can be used within an if statement.

5. What is the use of pass keyword in Python?
>Pass keyword helps in avoiding errors that result due to an empty loop.

---
