# Deep Copy vs Shallow Copy in Python

## 1. Normal Assignment (`=`)

```python id="0i8tn0"
a = [1, 2, 3]

b = a
```

Here:

* `a` and `b` point to SAME list
* No copy happens

Memory:

```text id="1e1nhq"
a ----\
       ---> [1, 2, 3]
b ----/
```

---

## If we change `b`

```python id="e6uxnq"
b[0] = 100

print(a)
```

Output:

```python id="5lmh07"
[100, 2, 3]
```

Because both variables point to SAME object.

---

# 2. Shallow Copy

A shallow copy creates:

✅ New outer list
❌ Inner nested objects are shared

---

# Example 1: Simple List

```python id="17whrx"
a = [1, 2, 3]

b = a.copy()

b[0] = 100

print(a)
print(b)
```

Output:

```python id="pk1bo2"
[1, 2, 3]
[100, 2, 3]
```

---

# Why original did NOT change?

Because:

```python id="3r3hbo"
a.copy()
```

creates a NEW outer list.

Memory:

```text id="lsd4n4"
a ---> [1, 2, 3]

b ---> [1, 2, 3]
```

Different objects.

---

# Important Point

This works safely because integers are immutable.

---

# Example 2: Nested List (List Inside List)

```python id="mxy7e9"
a = [[1, 2], [3, 4]]

b = a.copy()
```

Now memory looks like:

```text id="9b9v8g"
a ---> [ X , Y ]
b ---> [ X , Y ]

X ---> [1, 2]
Y ---> [3, 4]
```

---

# VERY IMPORTANT

Outer list is copied.

But inner lists are NOT copied.

Both lists share SAME inner objects.

---

# Changing Inner Object

```python id="tvjlwm"
b[0][0] = 100

print(a)
print(b)
```

Output:

```python id="0v5mhy"
[[100, 2], [3, 4]]
[[100, 2], [3, 4]]
```

---

# Why did original change?

Because:

```python id="6ngg1p"
a[0]
```

and

```python id="j5l1vn"
b[0]
```

both point to SAME inner list.

Memory:

```text id="7go7wd"
a[0] ----\
           ---> [100, 2]
b[0] ----/
```

So modifying inner list affects both.

---

# Changing Outer Structure

## append()

```python id="s6hzh6"
a = [[1], [2]]

b = a.copy()

b.append([3])

print(a)
print(b)
```

Output:

```python id="90eq7s"
[[1], [2]]
[[1], [2], [3]]
```

---

# Why original did NOT change?

Because append changes only outer list `b`.

It does NOT modify shared inner objects.

---

# sort()

```python id="yzvws3"
a = [[3], [1], [2]]

b = a.copy()

b.sort()

print(a)
print(b)
```

Output:

```python id="z0ht3m"
[[3], [1], [2]]
[[1], [2], [3]]
```

---

# Why original did NOT change?

Because sorting changes order inside `b` only.

Inner objects remain same.

---

# Shallow Copy Summary

| Operation     | Original Changes? |
| ------------- | ----------------- |
| `b.append()`  | ❌ No              |
| `b.sort()`    | ❌ No              |
| `b[0] = [9]`  | ❌ No              |
| `b[0][0] = 9` | ✅ Yes             |

---

# Why Shallow Copy Fails

Shallow copy fails when nested mutable objects exist.

Examples:

* list inside list
* dict inside list
* set inside list
* custom mutable objects

Because nested objects are shared.

---

# 3. Deep Copy

Deep copy creates:

✅ New outer list
✅ New inner objects
✅ Completely independent copy

---

# Syntax

```python id="94h31y"
import copy

b = copy.deepcopy(a)
```

---

# Example

```python id="ys2t6j"
import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

b[0][0] = 100

print(a)
print(b)
```

Output:

```python id="ymv6x4"
[[1, 2], [3, 4]]
[[100, 2], [3, 4]]
```

---

# Why original did NOT change?

Because deep copy copies EVERYTHING recursively.

Memory:

```text id="4rt0jx"
a ---> [ X , Y ]
X ---> [1, 2]

b ---> [ P , Q ]
P ---> [100, 2]
```

Different inner objects.

---

# Deep Copy vs Shallow Copy

| Feature                        | Shallow Copy | Deep Copy |
| ------------------------------ | ------------ | --------- |
| Outer list copied              | ✅            | ✅         |
| Inner objects copied           | ❌            | ✅         |
| Nested changes affect original | ✅            | ❌         |
| Faster                         | ✅            | ❌         |
| More memory efficient          | ✅            | ❌         |

---

# Methods for Shallow Copy

```python id="x0zdv7"
b = a.copy()

b = a[:]

b = list(a)

import copy
b = copy.copy(a)
```

---

# Method for Deep Copy

```python id="6iswqz"
import copy

b = copy.deepcopy(a)
```

---

# Easy Rule to Remember

## Shallow Copy

```text id="pqj1jd"
Copies only first layer
```

---

## Deep Copy

```text id="j6jlwm"
Copies everything recursively
```

---

# Interview One-Line Definition

## Shallow Copy

Creates a new outer object but shares nested mutable objects.

---

## Deep Copy

Creates completely independent copies of all nested objects recursively.

Both create a **shallow copy** of the list.

```python id="6wh34v"
l2 = list(l1)
```

and

```python id="6c70tl"
l2 = l1[:]
```

usually behave the same for normal lists.

---

# Example

```python id="n2s8pw"
l1 = [1, 2, 3]

l2 = list(l1)
l3 = l1[:]

l2[0] = 100
l3[1] = 200

print(l1)
print(l2)
print(l3)
```

Output:

```python id="z7uyd2"
[1, 2, 3]
[100, 2, 3]
[1, 200, 3]
```

Original does not change.

---

# Both are shallow copies

Nested objects are still shared.

Example:

```python id="n92vwq"
l1 = [[1], [2]]

l2 = list(l1)
l3 = l1[:]

l2[0][0] = 100

print(l1)
print(l2)
print(l3)
```

Output:

```python id="k58g7z"
[[100], [2]]
[[100], [2]]
[[100], [2]]
```

Because inner lists are shared.

---

# Difference Between Them

# 1. Syntax Style

## `list(l1)`

Uses constructor.

```python id="v7gqha"
l2 = list(l1)
```

Works with ANY iterable.

Example:

```python id="5ghd6k"
t = (1, 2, 3)

l2 = list(t)
```

Tuple converted to list.

---

## `l1[:]`

Uses slicing.

```python id="ph78rp"
l2 = l1[:]
```

Works mainly with sequence types supporting slicing.

---

# 2. Performance

Usually:

```text id="0djlwm"
l1[:]   → slightly faster
list()  → slightly more general
```

But difference is tiny.

---

# 3. Readability

| Method     | Meaning                     |
| ---------- | --------------------------- |
| `l1[:]`    | copy by slicing             |
| `list(l1)` | make new list from iterable |

Many people prefer:

```python id="q63zyu"
l2 = l1.copy()
```

because it is clearer.

---

# Important Interview Point

All three are shallow copies:

```python id="tqll4m"
l2 = l1.copy()

l2 = l1[:]

l2 = list(l1)
```

None performs deep copy.

---

# Best Practice

## For shallow copy

```python id="1jlwm5"
l2 = l1.copy()
```

Most readable.

---

## For deep copy

```python id="8ijjlwm"
import copy

l2 = copy.deepcopy(l1)
```
`ceil()` gives the greater integer.

The opposite function for the smaller integer is:

# `floor()`

---

# Import

```python id="jlwmkk"
from math import ceil, floor
```

---

# Example

```python id="jlwmll"
print(ceil(4.2))
print(floor(4.2))
```

Output:

```python id="jlwmmm"
5
4
```

---

# Meaning

| Function   | Meaning    |
| ---------- | ---------- |
| `ceil(x)`  | Round UP   |
| `floor(x)` | Round DOWN |

---

# Examples

| Value | `ceil()` | `floor()` |
| ----- | -------- | --------- |
| `4.1` | `5`      | `4`       |
| `4.9` | `5`      | `4`       |
| `4.0` | `4`      | `4`       |

---

# Negative Numbers (Important)

```python id="’winina"
print(ceil(-4.2))
print(floor(-4.2))
```

Output:

```python id="6t1jlwm"
-4
-5
```

---

# Why?

## `ceil()`

Smallest integer ≥ number

```text id="jlwmoo"
ceil(-4.2) = -4
```

because:

```text id="jlwmpp"
-4 is greater than -4.2
```

---

## `floor()`

Largest integer ≤ number

```text id="jlwmqq"
floor(-4.2) = -5
```

because:

```text id="jlwmrr"
-5 is smaller than -4.2
```

---

# Visual Number Line

```text id="jlwmss"
-5 ---- -4.2 ---- -4
```

* floor → left side
* ceil → right side

---

# Easy Memory Trick

## Ceiling

```text id="jlwmtt"
goes UP to ceiling
```

## Floor

```text id="jlwmuu"
goes DOWN to floor
```

