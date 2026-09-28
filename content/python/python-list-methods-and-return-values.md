# Python List Methods — Complete Parameter, Return & Mutation Guide

Python lists have **11 commonly used built-in methods**. Here they are in short:

|  # | List Method | What it does                            |
| -: | ----------- | --------------------------------------- |
|  1 | `append()`  | Adds **one element** at the end         |
|  2 | `extend()`  | Adds **multiple elements**              |
|  3 | `insert()`  | Adds an element at a **specific index** |
|  4 | `remove()`  | Removes an element by **value**         |
|  5 | `pop()`     | Removes an element by **index**         |
|  6 | `clear()`   | Removes **all elements**                |
|  7 | `index()`   | Finds the **index of a value**          |
|  8 | `count()`   | Counts how many times a value occurs    |
|  9 | `sort()`    | Sorts the list                          |
| 10 | `reverse()` | Reverses the list                       |
| 11 | `copy()`    | Creates a copy of the list              |

---

### 🧠 Easy grouping

**Adding:**
* `append()`
* `extend()`
* `insert()`

**Removing:**
* `remove()`
* `pop()`
* `clear()`

**Searching/Counting:**
* `index()`
* `count()`

**Ordering:**
* `sort()`
* `reverse()`

**Copying:**
* `copy()`

---

### ⚠️ Important

`find()`, `search()`, and `delete()` are **not built-in list methods**.

Also, `del` is a **Python keyword**, not a list method.

**Total built-in list methods = 11.**

---

## 🐍 Python List Methods — Complete Parameter + Return Notes

Assume:

```python
numbers = [10, 20, 30, 40, 50]
```

|  # | Method / Syntax                    | Parameter            | What it does                    | Returns             |
| -: | ---------------------------------- | -------------------- | ------------------------------- | ------------------- |
|  1 | `append(x)`                        | `x`                  | Adds `x` at the end             | `None`              |
|  2 | `clear()`                          | None                 | Removes all elements            | `None`              |
|  3 | `copy()`                           | None                 | Creates a shallow copy          | **New list**        |
|  4 | `count(x)`                         | `x`                  | Counts occurrences of `x`       | **Integer**         |
|  5 | `extend(iterable)`                 | `iterable`           | Adds all elements from iterable | `None`              |
|  6 | `index(x)`                         | `x`                  | Finds first index of `x`        | **Integer**         |
|  7 | `index(x, start)`                  | `x`, `start`         | Searches from `start`           | **Integer**         |
|  8 | `index(x, start, stop)`            | `x`, `start`, `stop` | Searches from `start` to `stop` | **Integer**         |
|  9 | `insert(index, x)`                 | `index`, `x`         | Inserts `x` at `index`          | `None`              |
| 10 | `pop()`                            | None                 | Removes last element            | **Removed element** |
| 11 | `pop(index)`                       | `index`              | Removes element at `index`      | **Removed element** |
| 12 | `remove(x)`                        | `x`                  | Removes first occurrence of `x` | `None`              |
| 13 | `reverse()`                        | None                 | Reverses the list               | `None`              |
| 14 | `sort()`                           | None                 | Sorts in ascending order        | `None`              |
| 15 | `sort(reverse=True)`               | `reverse`            | Sorts in descending order       | `None`              |
| 16 | `sort(key=function)`               | `key`                | Sorts using a custom rule       | `None`              |
| 17 | `sort(key=function, reverse=True)` | `key`, `reverse`     | Custom sort + descending        | `None`              |

---

### 🔥 Important return values

| Method      | Returns         |
| ----------- | --------------- |
| `append()`  | `None`          |
| `clear()`   | `None`          |
| `copy()`    | New list        |
| `count()`   | Number (`int`)  |
| `extend()`  | `None`          |
| `index()`   | Index (`int`)   |
| `insert()`  | `None`          |
| `pop()`     | Removed element |
| `remove()`  | `None`          |
| `reverse()` | `None`          |
| `sort()`    | `None`          |

---

### 🧠 Very important concept

Don't confuse **what the method does** with **what it returns**.

For example:

```python
numbers = [10, 20, 30]

result = numbers.append(40)

print(numbers)
print(result)
```

Output:

```text
[10, 20, 30, 40]
None
```

`append()` **changes the list**, but it returns `None`.

Compare that with `pop()`:

```python
numbers = [10, 20, 30]

result = numbers.pop()

print(numbers)
print(result)
```

Output:

```text
[10, 20]
30
```

`pop()` **changes the list AND returns the removed element**.

---

### ⭐ Easy rule to remember

**Returns something useful:**

```text
copy()  → new list
count() → number
index() → index
pop()   → removed element
```

**Returns `None`:**

```text
append()
clear()
extend()
insert()
remove()
reverse()
sort()
```

---

### 🚨 Common Exception Behavior

* **`index()`**: Raises **`ValueError`** if the value isn't found in the list.
* **`pop()`**: Raises **`IndexError`** if the index is invalid or if the list is empty.
