# Dunder Methods & The Python Data Model

**Dunder methods** are special methods in Python whose names start and end with **double underscores**.

**Dunder = Double Underscore**

For example:

```python
__init__
__len__
__str__
__getitem__
__setitem__
```

They allow you to define **how your custom object behaves when you use normal Python operations**.

---

### Simple example

```python
class MyList:

    def __init__(self):
        self.size = 5

    def __len__(self):
        return self.size
```

Now:

```python
arr = MyList()

len(arr)
```

Python automatically calls:

```python
arr.__len__()
```

So the result is:

```text
5
```

---

### Common dunder methods

| Operation      | Dunder method    |
| -------------- | ---------------- |
| Create object  | `__init__()`     |
| `len(arr)`     | `__len__()`      |
| `print(arr)`   | `__str__()`      |
| `arr[0]`       | `__getitem__()`  |
| `arr[0] = 10`  | `__setitem__()`  |
| `arr1 + arr2`  | `__add__()`      |
| `arr1 == arr2` | `__eq__()`       |
| `x in arr`     | `__contains__()` |

---

### Why do we use them?

Without dunder methods:

```python
arr.get_item(0)
```

With `__getitem__`:

```python
arr[0]
```

Without `__len__`:

```python
arr.get_length()
```

With `__len__`:

```python
len(arr)
```

So the main idea is:

> **Dunder methods are Python's way of letting your own classes participate in Python's built-in syntax and operations.**

For the `MyList` you're building, learning `__init__`, `__len__`, `__getitem__`, `__setitem__`, `__iter__`, and `__contains__` will be especially useful.

---

## Predefined Dunder Methods vs Custom Names

`__any_method__` is **not a special Python method just because it has double underscores**.

There are two concepts here:

### 1. Python's predefined dunder methods

Methods such as:

```python
__init__
__len__
__str__
__getitem__
__setitem__
__add__
```

have **special meaning to Python**.

They let your custom class interact with Python's built-in syntax/functions.

For example:

```python
class MyList:

    def __init__(self):
        self.size = 10

    def __len__(self):
        return self.size
```

Now:

```python
arr = MyList()

len(arr)
```

Python effectively uses:

```python
arr.__len__()
```

---

### 2. `__any_method__` that you create yourself

Suppose you write:

```python
class MyList:

    def __my_method__(self):
        print("Hello")
```

Python doesn't automatically give `__my_method__` any special behavior.

You can call it:

```python
arr = MyList()

arr.__my_method__()
```

But there's no built-in Python operation that automatically calls it.

So this:

```python
def __my_method__(self):
```

is essentially just a strangely named method.

---

### Why are dunder methods useful?

They allow you to **define how your object behaves with Python syntax**.

For example:

```python
class MyList:

    def __init__(self):
        self.data = [10, 20, 30]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        return str(self.data)
```

Now your custom object can behave naturally:

```python
arr = MyList()

len(arr)
```

calls:

```python
arr.__len__()
```

And:

```python
arr[1]
```

calls:

```python
arr.__getitem__(1)
```

And:

```python
print(arr)
```

calls:

```python
arr.__str__()
```

So you can think of dunder methods as **hooks that Python calls automatically when you use certain operations**.

---

### A useful mental model

```text
Python operation       →  Dunder method

MyList()               →  __init__()
len(arr)               →  __len__()
arr[2]                 →  __getitem__(2)
arr[2] = 50            →  __setitem__(2, 50)
print(arr)             →  __str__()
arr + other            →  __add__(other)
arr == other           →  __eq__(other)
```

> **Important:** Don't create arbitrary names like `__my_method__` expecting Python to treat them specially. Python's special methods are the ones defined by the language/data model.
