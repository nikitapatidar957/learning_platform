"""
Python & Data Engineering Topics and Lessons Seed Data
Incorporating concepts from:
- python_interview/README.md
- python_interview/cross_question_answer.md
- python_interview/notes_copy1.md
- python_interview/jupyter/pandas/pandas_notes.md
- python_interview/github.md
"""

PYTHON_TOPICS = [
    {
        "subjectSlug": "python",
        "title": "Python Basics & Core Fundamentals",
        "slug": "python-basics-programming",
        "description": "Syntax, keywords, identifiers, statement indentation, variables, constants, literals, data types, type conversion, I/O, and operators.",
        "order": 1,
        "isPublished": True,
    },
    {
        "subjectSlug": "python",
        "title": "Python Architecture & Memory Internals",
        "slug": "python-execution-memory",
        "description": "Deep dive into CPython execution, bytecode, JIT, reference counting, cyclic garbage collection, and shallow vs deep copy.",
        "order": 2,
        "isPublished": True,
    },
    {
        "subjectSlug": "python",
        "title": "Flow Control, Loops & Conditionals",
        "slug": "python-flow-control",
        "description": "Conditional branching (if, elif, else, nested if), loops (for, while, range), and loop control statements (break, continue, pass).",
        "order": 3,
        "isPublished": True,
    },
    {
        "subjectSlug": "python",
        "title": "Functions, Scopes & Advanced Patterns",
        "slug": "functions-scopes-advanced",
        "description": "LEGB scope resolution, *args/**kwargs, mutable default arguments traps, decorators, and memory-saving generators.",
        "order": 4,
        "isPublished": True,
    },
    {
        "subjectSlug": "python",
        "title": "Object-Oriented Programming (OOP) in Python",
        "slug": "python-oop-mastery",
        "description": "The 4 pillars of OOP, Method Resolution Order (MRO), class vs static methods, dunder/magic methods, and context managers.",
        "order": 5,
        "isPublished": True,
    },
    {
        "subjectSlug": "python",
        "title": "File I/O, Exceptions & Regular Expressions",
        "slug": "python-files-regex",
        "description": "Reading and writing files, os directory management, robust exception handling (try-except-else-finally), and regex patterns.",
        "order": 6,
        "isPublished": True,
    },
    {
        "subjectSlug": "python",
        "title": "NumPy & High-Performance Array Computing",
        "slug": "python-numpy-numerical",
        "description": "Multidimensional ndarrays, vectorization, indexing, slicing, broadcasting, reshaping, and statistical operations in NumPy.",
        "order": 7,
        "isPublished": True,
    },
    {
        "subjectSlug": "python",
        "title": "Pandas & Tabular Data Manipulation",
        "slug": "pandas-data-manipulation",
        "description": "Series vs DataFrame, loc vs iloc indexing, handling missing values, filtering, groupby aggregations, merges, and pivot tables.",
        "order": 8,
        "isPublished": True,
    },
    {
        "subjectSlug": "python",
        "title": "Data Visualization with Matplotlib & Seaborn",
        "slug": "python-data-visualization",
        "description": "Creating publication-quality charts: line plots, scatter plots, bar charts, histograms, heatmaps, box plots, and pair plots.",
        "order": 9,
        "isPublished": True,
    },
    {
        "subjectSlug": "python",
        "title": "DateTime, Timestamps & Time Profiling",
        "slug": "python-datetime-time",
        "description": "Working with dates, times, timedeltas, formatting with strftime(), parsing with strptime(), timestamps, and time.sleep().",
        "order": 10,
        "isPublished": True,
    },
    {
        "subjectSlug": "python",
        "title": "Concurrency & The Global Interpreter Lock (GIL)",
        "slug": "python-concurrency-gil",
        "description": "Understanding the GIL, CPU-bound vs I/O-bound bottlenecks, threading vs multiprocessing vs asyncio.",
        "order": 11,
        "isPublished": True,
    },
    {
        "subjectSlug": "python",
        "title": "Git & Collaborative Version Control",
        "slug": "git-version-control",
        "description": "Distributed VCS, the 4 Git areas, DAG commit graphs, blobs/trees, branching, fast-forward vs 3-way merges, and rebasing.",
        "order": 12,
        "isPublished": True,
    },
]


PYTHON_LESSONS = [
    # -------------------------------------------------------------------------
    # Topic 1: Python Architecture & Memory Internals
    # -------------------------------------------------------------------------
    {
        "topicSlug": "python-execution-memory",
        "subjectSlug": "python",
        "title": "Python Execution Model & JIT Compilation",
        "slug": "python-execution-architecture",
        "description": "Discover how Python runs: source code to bytecode (.pyc), the Python Virtual Machine (PVM), CPython vs PyPy, and JIT.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "How Does Python Actually Run Your Code?",
                    "content": (
                        "Many developers think Python is purely interpreted line-by-line. In reality, Python is a two-step compiled-and-interpreted language:\n\n"
                        "1. Compilation to Bytecode:\n"
                        "   When you run `script.py`, CPython first compiles your human-readable source code into intermediate, platform-independent instructions called Bytecode (`.pyc` files stored in `__pycache__`).\n\n"
                        "2. Execution via Python Virtual Machine (PVM):\n"
                        "   The PVM is a giant evaluation loop written in C (`ceval.c`). It reads each bytecode instruction one by one and executes the corresponding machine instructions on the CPU."
                    )
                },
                {
                    "type": "code",
                    "title": "Inspecting Real Python Bytecode with the dis Module",
                    "language": "python",
                    "code": (
                        "import dis\n\n"
                        "def add_tax(price):\n"
                        "    return price * 1.18\n\n"
                        "# Disassemble into human-readable bytecode instructions\n"
                        "dis.dis(add_tax)\n"
                        "# Output:\n"
                        "# LOAD_FAST   0 (price)\n"
                        "# LOAD_CONST  1 (1.18)\n"
                        "# BINARY_OP   5 (*)\n"
                        "# RETURN_VALUE"
                    )
                },
                {
                    "type": "explanation",
                    "title": "What is JIT (Just-In-Time) Compilation & PyPy?",
                    "content": (
                        "• Standard CPython: Interprets bytecode in every loop iteration. If a loop runs 10,000,000 times, the PVM decodes and interprets the exact same bytecode 10,000,000 times!\n\n"
                        "• JIT Compilation (e.g., PyPy, Numba):\n"
                        "  Monitors running code to identify 'hot code' (functions or loops executed repeatedly). "
                        "  The JIT compiler translates that hot bytecode directly into native machine code (x86/ARM assembly) and saves it in RAM. "
                        "  Subsequent iterations run at raw C-speed without interpreter overhead (often 5x to 10x faster)!"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Compiled vs Interpreted: The Translation Model",
                    "content": (
                        "• Compiled: Converts the entire program into machine code (0s and 1s) before running it (e.g., C, C++). Compilation happens before running.\n\n"
                        "• Interpreted: Program is executed through an interpreter/runtime rather than producing a standalone machine-code executable first (e.g., Python, JS).\n\n"
                        "🧠 Real-Life Analogy: Hindi Book vs Live Translator\n"
                        "- Compiled: Translating the whole book into English first, then giving it to your friend to read.\n"
                        "- Interpreted: Having a translator sit beside your friend, translating sentence by sentence as they read.\n\n"
                        "⚠️ Python Reality: Python compiles source code to Bytecode (.pyc) first, then the Python Virtual Machine executes it. "
                        "Best interview definition: 'A compiled language converts the program into machine code before execution, while an interpreted language executes the program through an interpreter or runtime.'"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Extensible vs Embeddable in Python",
                    "content": (
                        "• Extensible (Python → calls C/C++):\n"
                        "  Add functionality written in C/C++ to a Python program using ctypes, Cython, or Python's C API. "
                        "  Used in NumPy, Pandas, PyTorch, and TensorFlow for high-performance CPU calculations.\n\n"
                        "• Embeddable (Put Python inside another application):\n"
                        "  Main application is C++ (e.g., a high-performance game engine), but executes Python inside it using PyRun_SimpleString() for scripting, automation, or game logic.\n\n"
                        "🧠 Mental Model (Python is a House):\n"
                        "- Extensible: Add something to the Python house (Python + C/C++ functionality).\n"
                        "- Embeddable: Put Python inside another house (C++ application + Python inside it).\n\n"
                        "⭐ Interview Shortcut: Extensible = Other language → Python | Embeddable = Python → Other language."
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "Why doesn't standard CPython use JIT? CPython prioritizes predictable startup times, simple C-extension compatibility (NumPy, PyTorch), and cross-platform simplicity."
                }
            ]
        }
    },
    {
        "topicSlug": "python-execution-memory",
        "subjectSlug": "python",
        "title": "Memory Management & Garbage Collection",
        "slug": "memory-management-gc",
        "description": "Understand stack vs heap memory in Python, reference counting, cyclic generational garbage collection, and object identity.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Stack vs Heap Memory in Python",
                    "content": (
                        "• Stack Memory: Stores function call frames, primitive references, and variable names. Fast, LIFO (Last In First Out), automatically allocated and freed when functions return.\n\n"
                        "• Heap Memory: Stores the actual objects themselves (all integers, strings, lists, dictionaries, custom class instances). Everything in Python is an object living on the private heap managed by the Python memory manager."
                    )
                },
                {
                    "type": "explanation",
                    "title": "How Garbage Collection Works: 2-Pillar System",
                    "content": (
                        "Python uses a dual-engine memory cleanup system:\n\n"
                        "1. Primary: Reference Counting\n"
                        "   Every object header in CPython (`PyObject`) contains an internal counter called `ob_refcnt`. "
                        "   • When a variable references the object: ref count increases.\n"
                        "   • When a variable goes out of scope or is reassigned: ref count decreases.\n"
                        "   • As soon as `refcnt == 0`: Memory is IMMEDIATELY freed. Fast and deterministic!\n\n"
                        "2. Secondary: Generational Cyclic Garbage Collector (`gc` module)\n"
                        "   What if Object A references Object B, and Object B references Object A (circular reference)? "
                        "   Even if no other variable in your program can access them, their ref count never drops to 0! "
                        "   Python's cyclic GC periodically scans generations (Generation 0, 1, 2) to detect isolated circular dependency graphs and destroys them."
                    )
                },
                {
                    "type": "code",
                    "title": "Inspecting Reference Counts and Object Identity",
                    "language": "python",
                    "code": (
                        "import sys\n\n"
                        "x = [1, 2, 3]\n"
                        "print('Initial refs:', sys.getrefcount(x) - 1)  # getrefcount adds 1 temporary ref\n\n"
                        "y = x  # y points to the exact same list in heap memory\n"
                        "print('After alias:', sys.getrefcount(x) - 1)  # count = 2\n\n"
                        "# Object Identity: id() and the 'is' keyword\n"
                        "print(id(x) == id(y))  # True: both have identical memory addresses\n"
                        "print(x is y)          # True: identical object in RAM\n"
                        "print(x == y)          # True: identical contents"
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Interview Trap: 'is' checks memory address equality (`id(a) == id(b)`). '==' checks value equality (`a.__eq__(b)`). Always use '==' for value comparisons unless checking against singletons like `None` (`x is None`)."
                }
            ]
        }
    },
    {
        "topicSlug": "python-execution-memory",
        "subjectSlug": "python",
        "title": "Mutability, Shallow Copy & Deep Copy",
        "slug": "mutability-shallow-deep-copy",
        "description": "Master mutable vs immutable objects in memory, normal assignment vs shallow copy vs deep copy, and tricky nested gotchas.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 3,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Mutable vs Immutable Objects",
                    "content": (
                        "• Immutable (Cannot be modified after creation):\n"
                        "  `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`, `bool`.\n"
                        "  If you change a string or add to a tuple, Python does NOT modify the object in place—it creates a brand new object at a new memory address!\n\n"
                        "• Mutable (Can be modified in place in memory):\n"
                        "  `list`, `dict`, `set`, `bytearray`.\n"
                        "  Modifying an element alters the original object in place without changing its memory address `id()`."
                    )
                },
                {
                    "type": "explanation",
                    "title": "The 3 Types of Copying in Python",
                    "content": (
                        "1. Normal Assignment (`b = a`):\n"
                        "   Does NOT copy any data! It merely creates a second variable name (alias) pointing to the EXACT same memory address in RAM. Modifying `b` modifies `a`!\n\n"
                        "2. Shallow Copy (`b = copy.copy(a)` or `b = a.copy()` or `b = a[:]`):\n"
                        "   Creates a brand new outer container object, but populates it with REFERENCES to the original child items. "
                        "   If the list contains nested lists or objects, modifying a nested object will alter both `a` and `b`!\n\n"
                        "3. Deep Copy (`b = copy.deepcopy(a)`):\n"
                        "   Recursively creates a completely independent clone of the outer container AND all nested sub-objects. "
                        "   Changes to `b` can NEVER affect `a`."
                    )
                },
                {
                    "type": "code",
                    "title": "The Classic Interview Cross-Examination Code",
                    "language": "python",
                    "code": (
                        "import copy\n\n"
                        "original = [1, [2, 3], 4]\n\n"
                        "# Shallow Copy\n"
                        "shallow = copy.copy(original)\n"
                        "shallow[0] = 99        # Modifies outer list -> ONLY shallow changes\n"
                        "shallow[1][0] = 999    # Modifies nested list -> BOTH original & shallow change!\n\n"
                        "print('Original after shallow mutation:', original)\n"
                        "# Output: [1, [999, 3], 4]  <-- nested list was modified in both!\n\n"
                        "# Deep Copy\n"
                        "deep = copy.deepcopy(original)\n"
                        "deep[1][0] = 777       # Completely independent memory tree\n"
                        "print('Original after deep mutation:', original)\n"
                        "# Output: [1, [999, 3], 4]  <-- original is completely untouched!"
                    )
                },
                {
                    "type": "callout",
                    "variant": "warning",
                    "content": "Interview Edge Case: Small integers between -5 and 256 are pre-cached singletons in CPython. `a = 100` and `b = 100` will have `a is b == True`, but for larger numbers `a = 1000` and `b = 1000`, `a is b` may evaluate to `False` in interactive shells!"
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 2: Functions, Scopes & Advanced Patterns
    # -------------------------------------------------------------------------
    {
        "topicSlug": "functions-scopes-advanced",
        "subjectSlug": "python",
        "title": "Scopes, Closures & Function Arguments",
        "slug": "scopes-closures-arguments",
        "description": "Understand LEGB scope resolution, *args/**kwargs, closures, and the infamous mutable default argument trap.",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The LEGB Scope Resolution Rule",
                    "content": (
                        "When Python encounters a variable name, it searches for it in this exact order:\n\n"
                        "1. Local (L): Inside the current function or lambda.\n"
                        "2. Enclosing (E): Inside any enclosing outer/nested functions (closures).\n"
                        "3. Global (G): Top-level of the current module/file.\n"
                        "4. Built-in (B): Python pre-loaded names (`len`, `range`, `print`, `ValueError`).\n\n"
                        "If the name is not found in any of the 4 scopes, Python raises `NameError`."
                    )
                },
                {
                    "type": "code",
                    "title": "The Mutable Default Argument Trap (Most Asked Interview Bug)",
                    "language": "python",
                    "code": (
                        "# THE BUG:\n"
                        "def append_to(element, target_list=[]):  # target_list is evaluated ONCE at function definition time!\n"
                        "    target_list.append(element)\n"
                        "    return target_list\n\n"
                        "print(append_to(1))  # [1]\n"
                        "print(append_to(2))  # [1, 2] <-- BUG! Default list is reused across calls!\n\n"
                        "# THE FIX (Use None sentinel pattern):\n"
                        "def append_to_safe(element, target_list=None):\n"
                        "    if target_list is None:\n"
                        "        target_list = []  # Fresh list allocated on each invocation\n"
                        "    target_list.append(element)\n"
                        "    return target_list\n\n"
                        "print(append_to_safe(1))  # [1]\n"
                        "print(append_to_safe(2))  # [2] <-- Clean and correct!"
                    )
                },
                {
                    "type": "explanation",
                    "title": "*args and **kwargs Demystified",
                    "content": (
                        "• `*args`: Collects positional arguments passed into a tuple. Allows a function to accept any number of positional inputs.\n"
                        "• `**kwargs`: Collects keyword arguments passed into a dictionary. Allows a function to accept arbitrary named keyword parameters.\n"
                        "• Order in function signature: `def func(pos, *args, kw_only=1, **kwargs):`"
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "What is a Closure? A nested function that retains access to variables from its enclosing lexical scope even after the outer function has completed execution."
                }
            ]
        }
    },
    {
        "topicSlug": "functions-scopes-advanced",
        "subjectSlug": "python",
        "title": "Python Decorators Deep Dive",
        "slug": "python-decorators-mastery",
        "description": "Understand higher-order functions, writing custom decorators from scratch, preserving metadata with @functools.wraps, and decorator factories.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "What is a Decorator?",
                    "content": (
                        "In Python, functions are first-class citizens: they can be passed as arguments, returned from other functions, and assigned to variables. "
                        "A decorator is simply a higher-order function that takes another function as an argument, extends or modifies its behavior, "
                        "and returns an updated wrapper function—all without altering the original function's source code!\n\n"
                        "Syntax Sugar: `@my_decorator` placed above a function definition is shorthand for:\n"
                        "`my_function = my_decorator(my_function)`."
                    )
                },
                {
                    "type": "code",
                    "title": "Building a Timing & Logging Decorator with functools.wraps",
                    "language": "python",
                    "code": (
                        "import time\n"
                        "from functools import wraps\n\n"
                        "def timer_decorator(func):\n"
                        "    # @wraps preserves original func's __name__, __doc__, and signature\n"
                        "    @wraps(func)\n"
                        "    def wrapper(*args, **kwargs):\n"
                        "        start_time = time.perf_counter()\n"
                        "        result = func(*args, **kwargs)  # Call original function\n"
                        "        elapsed = time.perf_counter() - start_time\n"
                        "        print(f'Function {func.__name__!r} executed in {elapsed:.6f} seconds')\n"
                        "        return result\n"
                        "    return wrapper\n\n"
                        "@timer_decorator\n"
                        "def calculate_squares(n):\n"
                        "    \"\"\"Compute sum of squares up to n.\"\"\"\n"
                        "    return sum(i * i for i in range(n))\n\n"
                        "calculate_squares(1_000_000)\n"
                        "print('Preserved docstring:', calculate_squares.__doc__)"
                    )
                },
                {
                    "type": "callout",
                    "variant": "warning",
                    "content": "Why is @wraps necessary? Without `@wraps(func)`, `calculate_squares.__name__` would print `'wrapper'` and its docstring would be lost, breaking debugging tools and documentation generators!"
                }
            ]
        }
    },
    {
        "topicSlug": "functions-scopes-advanced",
        "subjectSlug": "python",
        "title": "Iterators, Generators & The yield Keyword",
        "slug": "iterators-generators-yield",
        "description": "Understand the iteration protocol, generator functions, memory efficiency, and handling infinite streams with yield.",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate",
        "order": 3,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Iteration Protocol in Python",
                    "content": (
                        "• Iterable: Any object that can return an iterator (has an `__iter__()` method, e.g., list, tuple, dict, str).\n"
                        "• Iterator: An object with a `__next__()` method that yields one value at a time and raises `StopIteration` when depleted."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Generators & The yield Keyword",
                    "content": (
                        "A generator is a function that contains the `yield` statement instead of `return`.\n\n"
                        "How it works:\n"
                        "When a generator function is called, it does NOT execute the code immediately. It returns a generator object. "
                        "When `next(gen)` is called, execution proceeds until it hits `yield value`. It sends the value back, "
                        "freezes its execution state (local variables and instruction pointer remain intact in memory), and pauses! "
                        "On the next call, it resumes right where it left off.\n\n"
                        "Massive RAM Advantage: A list of 10,000,000 integers takes ~400 MB of RAM. A generator producing those same 10,000,000 integers takes only ~120 bytes of RAM because it computes values on the fly!"
                    )
                },
                {
                    "type": "code",
                    "title": "Generator vs List Comprehension Memory Benchmark",
                    "language": "python",
                    "code": (
                        "import sys\n\n"
                        "# 1. List Comprehension: Allocates all 1,000,000 items in RAM immediately\n"
                        "list_data = [x * 2 for x in range(1_000_000)]\n"
                        "print(f'List Memory:      {sys.getsizeof(list_data):,} bytes (~8.4 MB)')\n\n"
                        "# 2. Generator Expression: Evaluates on the fly (lazy evaluation)\n"
                        "gen_data = (x * 2 for x in range(1_000_000))\n"
                        "print(f'Generator Memory: {sys.getsizeof(gen_data):,} bytes (tiny!)')\n\n"
                        "# Fetching items one by one\n"
                        "print('First item:', next(gen_data))  # 0\n"
                        "print('Next item:', next(gen_data))   # 2"
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 3: Object-Oriented Programming (OOP) in Python
    # -------------------------------------------------------------------------
    {
        "topicSlug": "python-oop-mastery",
        "subjectSlug": "python",
        "title": "Classes, Methods & The 4 Pillars of OOP",
        "slug": "oop-four-pillars",
        "description": "Master Encapsulation (name mangling), Inheritance, Method Resolution Order (MRO), Polymorphism, and Abstraction (abc module).",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The 4 Pillars of Object-Oriented Programming in Python",
                    "content": (
                        "1. Encapsulation: Bundling data and methods into a single unit, and restricting direct external access.\n"
                        "   • Public: `self.name` (accessible anywhere)\n"
                        "   • Protected: `self._balance` (convention indicating internal use)\n"
                        "   • Private: `self.__password` (triggers Name Mangling to `_ClassName__password` to prevent accidental overrides)\n\n"
                        "2. Inheritance: Deriving a child class from a parent class to reuse code and establish hierarchies.\n\n"
                        "3. Polymorphism: Different classes can implement the same method interface. In Python, this is enabled by Duck Typing (\"If it walks like a duck and quacks like a duck, it's a duck!\").\n\n"
                        "4. Abstraction: Hiding internal implementation complexities and exposing only essential interfaces using Python's `abc` (Abstract Base Classes) module."
                    )
                },
                {
                    "type": "code",
                    "title": "Implementing the 4 Pillars in Clean Python",
                    "language": "python",
                    "code": (
                        "from abc import ABC, abstractmethod\n\n"
                        "# 4. Abstraction: Contract definition\n"
                        "class PaymentGateway(ABC):\n"
                        "    @abstractmethod\n"
                        "    def process_payment(self, amount: float) -> bool:\n"
                        "        pass\n\n"
                        "# 2. Inheritance & 3. Polymorphism\n"
                        "class StripeGateway(PaymentGateway):\n"
                        "    def __init__(self, api_key: str):\n"
                        "        # 1. Encapsulation: Private attribute\n"
                        "        self.__api_key = api_key\n\n"
                        "    def process_payment(self, amount: float) -> bool:\n"
                        "        print(f'Charging ${amount:.2f} via Stripe using key: {self.__api_key[:4]}***')\n"
                        "        return True\n\n"
                        "class PayPalGateway(PaymentGateway):\n"
                        "    def process_payment(self, amount: float) -> bool:\n"
                        "        print(f'Charging ${amount:.2f} via PayPal Express')\n"
                        "        return True\n\n"
                        "# Polymorphic checkout runner\n"
                        "def checkout(gateway: PaymentGateway, total: float):\n"
                        "    gateway.process_payment(total)\n\n"
                        "checkout(StripeGateway('sk_live_987654321'), 99.00)\n"
                        "checkout(PayPalGateway(), 45.50)"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Multiple Inheritance & Method Resolution Order (MRO)",
                    "content": (
                        "When a class inherits from multiple parents (`class Child(ParentA, ParentB)`), which version of a method gets called? "
                        "Python uses the C3 Linearization Algorithm to determine the MRO order. "
                        "You can inspect this order with `Child.mro()` or `Child.__mro__`."
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Always use `super().__init__()` instead of calling `ParentClass.__init__(self)` directly. `super()` respects the cooperative MRO chain in multiple inheritance!"
                }
            ]
        }
    },
    {
        "topicSlug": "python-oop-mastery",
        "subjectSlug": "python",
        "title": "Method Types & Magic Dunder Methods",
        "slug": "methods-and-dunder-internals",
        "description": "Understand instance vs class (@classmethod) vs static (@staticmethod) methods, and implement essential dunders (__str__, __repr__, context managers).",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Instance Methods vs @classmethod vs @staticmethod",
                    "content": (
                        "• Instance Method: Takes `self` as the first argument. Can access and modify instance state (`self.name`) and class state (`self.__class__`).\n\n"
                        "• Class Method (`@classmethod`): Takes `cls` as the first argument. Can modify class-level state that applies to all instances. Commonly used as Factory Methods to instantiate objects from alternate data formats (e.g., `User.from_json()`).\n\n"
                        "• Static Method (`@staticmethod`): Takes neither `self` nor `cls`. Behaves like a plain function that belongs to the class's namespace for logical grouping. Does not modify class or instance state."
                    )
                },
                {
                    "type": "code",
                    "title": "Factory Classmethods and Essential Dunder Methods",
                    "language": "python",
                    "code": (
                        "class Vector2D:\n"
                        "    def __init__(self, x: float, y: float):\n"
                        "        self.x = x\n"
                        "        self.y = y\n\n"
                        "    # Alternate Factory constructor\n"
                        "    @classmethod\n"
                        "    def from_string(cls, coord_str: str):\n"
                        "        x_str, y_str = coord_str.split(',')\n"
                        "        return cls(float(x_str.strip()), float(y_str.strip()))\n\n"
                        "    # __repr__: Unambiguous representation for developers\n"
                        "    def __repr__(self):\n"
                        "        return f'Vector2D(x={self.x}, y={self.y})'\n\n"
                        "    # __str__: Human-friendly representation\n"
                        "    def __str__(self):\n"
                        "        return f'({self.x}, {self.y})'\n\n"
                        "    # Operator overloading: Enables v1 + v2\n"
                        "    def __add__(self, other):\n"
                        "        return Vector2D(self.x + other.x, self.y + other.y)\n\n"
                        "v1 = Vector2D(3, 4)\n"
                        "v2 = Vector2D.from_string('10, 20')\n"
                        "v3 = v1 + v2\n"
                        "print('Result vector:', repr(v3))  # Vector2D(x=13.0, y=24.0)"
                    )
                },
                {
                    "type": "explanation",
                    "title": "What are Dunder Methods? (Double Underscore)",
                    "content": (
                        "Dunder methods are special methods in Python whose names start and end with double underscores (Dunder = Double Underscore).\n\n"
                        "They allow you to define how your custom object behaves when you use normal Python operations:\n"
                        "• MyList() → calls __init__()\n"
                        "• len(arr) → calls arr.__len__()\n"
                        "• arr[0] → calls arr.__getitem__(0)\n"
                        "• arr[0] = 10 → calls arr.__setitem__(0, 10)\n"
                        "• print(arr) → calls arr.__str__()\n"
                        "• arr1 + arr2 → calls arr1.__add__(arr2)\n"
                        "• arr1 == arr2 → calls arr1.__eq__(arr2)\n"
                        "• x in arr → calls arr.__contains__(x)\n\n"
                        "⚠️ Predefined vs Custom Names:\n"
                        "Creating a method like `__my_method__` does NOT give it special behavior. Only Python's predefined dunder methods are hooks called automatically by Python syntax."
                    )
                },
                {
                    "type": "code",
                    "title": "Building Custom Container Class with Dunders (MyList)",
                    "language": "python",
                    "code": (
                        "class MyList:\n"
                        "    def __init__(self):\n"
                        "        self.data = [10, 20, 30]\n\n"
                        "    def __len__(self):\n"
                        "        return len(self.data)\n\n"
                        "    def __getitem__(self, index):\n"
                        "        return self.data[index]\n\n"
                        "    def __setitem__(self, index, value):\n"
                        "        self.data[index] = value\n\n"
                        "    def __str__(self):\n"
                        "        return str(self.data)\n\n"
                        "arr = MyList()\n"
                        "print(len(arr))   # Automatically calls arr.__len__() -> 3\n"
                        "print(arr[1])     # Automatically calls arr.__getitem__(1) -> 20\n"
                        "arr[1] = 99       # Automatically calls arr.__setitem__(1, 99)\n"
                        "print(arr)        # Automatically calls arr.__str__() -> [10, 99, 30]"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Building a Context Manager with __enter__ and __exit__",
                    "content": (
                        "The `with` statement guarantees resource cleanup (e.g., closing database connections, unlocking mutexes) even if exceptions occur. "
                        "You can build your own context manager by implementing `__enter__()` and `__exit__()`."
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "python-oop-mastery",
        "subjectSlug": "python",
        "title": "The 11 Built-in List Methods & Return Values Guide",
        "slug": "python-list-methods-and-mutations",
        "description": "Master the 11 built-in list methods, parameters, in-place mutation vs return values (None vs useful values), and exceptions.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 3,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The 11 Built-in List Methods & Their Groupings",
                    "content": (
                        "Python lists have exactly 11 built-in methods (Note: find(), search(), and delete() do NOT exist on lists; `del` is a keyword):\n\n"
                        "1. Adding: `append(x)` (adds 1 item at end), `extend(iterable)` (adds multiple items), `insert(index, x)` (adds at specific index)\n"
                        "2. Removing: `remove(x)` (removes first occurrence of value), `pop([index])` (removes by index and returns it), `clear()` (removes all)\n"
                        "3. Searching/Counting: `index(x, [start, [stop]])` (finds index), `count(x)` (counts occurrences)\n"
                        "4. Ordering: `sort([key=func, reverse=bool])` (sorts in-place), `reverse()` (reverses in-place)\n"
                        "5. Copying: `copy()` (creates a shallow copy)"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Crucial Interview Concept: What a Method Does vs What It Returns",
                    "content": (
                        "A very common bug and interview question is checking the return value of in-place list methods:\n\n"
                        "• Returns None (Modifies list in-place):\n"
                        "  `append()`, `clear()`, `extend()`, `insert()`, `remove()`, `reverse()`, `sort()`\n"
                        "  Example: `result = numbers.append(40)` -> `result` is `None`!\n\n"
                        "• Returns a Useful Value:\n"
                        "  `pop([index])` -> Returns the removed element!\n"
                        "  `index(x)` -> Returns integer index!\n"
                        "  `count(x)` -> Returns integer occurrence count!\n"
                        "  `copy()` -> Returns a new shallow-copied list!\n\n"
                        "🚨 Exception Behavior:\n"
                        "- `index()` raises ValueError if the target is not in the list.\n"
                        "- `pop()` raises IndexError if the index is out of bounds or the list is empty."
                    )
                },
                {
                    "type": "code",
                    "title": "List Mutation and Return Values in Action",
                    "language": "python",
                    "code": (
                        "numbers = [10, 20, 30]\n\n"
                        "# append() modifies in-place and returns None\n"
                        "res_append = numbers.append(40)\n"
                        "print('After append:', numbers)       # [10, 20, 30, 40]\n"
                        "print('res_append:', res_append)       # None\n\n"
                        "# pop() modifies in-place AND returns the removed element\n"
                        "res_pop = numbers.pop()\n"
                        "print('After pop:', numbers)          # [10, 20, 30]\n"
                        "print('res_pop:', res_pop)             # 40 (the removed element)\n\n"
                        "# index() returns an int or raises ValueError\n"
                        "print('Index of 20:', numbers.index(20)) # 1"
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 4: Concurrency & The GIL
    # -------------------------------------------------------------------------
    {
        "topicSlug": "python-concurrency-gil",
        "subjectSlug": "python",
        "title": "The Global Interpreter Lock (GIL) & Concurrency",
        "slug": "gil-threading-multiprocessing",
        "description": "Understand what the GIL is, why it exists, and how to select between threading, multiprocessing, and asyncio for maximum throughput.",
        "estimatedTime": "30 mins",
        "difficulty": "Advanced",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "What is the Global Interpreter Lock (GIL)?",
                    "content": (
                        "The GIL is a mutex (mutual exclusion lock) used by CPython to prevent multiple native OS threads from executing Python bytecodes simultaneously. "
                        "Even on an 8-core CPU, a multi-threaded Python program running CPU-heavy calculations will only run on 1 single core!\n\n"
                        "Why does Python have a GIL? Because CPython's memory management relies heavily on reference counting. "
                        "Without a global lock, race conditions would corrupt reference counters, leading to memory leaks and catastrophic crashes."
                    )
                },
                {
                    "type": "explanation",
                    "title": "CPU-Bound vs I/O-Bound: Choosing the Right Tool",
                    "content": (
                        "1. I/O-Bound Tasks (Web scraping, database queries, file writing, API requests):\n"
                        "   • The thread spends 99% of its time waiting for the network card or disk.\n"
                        "   • Solution: `threading` module or `asyncio`. When a thread waits for I/O, CPython RELEASES the GIL so other threads can run!\n\n"
                        "2. CPU-Bound Tasks (Image processing, machine learning training, cryptography, heavy math):\n"
                        "   • The threads actively consume 100% CPU. Multiple threads will fight for the GIL and run SLOWER than a single thread!\n"
                        "   • Solution: `multiprocessing` module or `concurrent.futures.ProcessPoolExecutor`. Spawns independent OS processes, each with its own separate Python interpreter and GIL, achieving true multi-core hardware parallelism."
                    )
                },
                {
                    "type": "code",
                    "title": "Multiprocessing for CPU-Bound Parallelism",
                    "language": "python",
                    "code": (
                        "import multiprocessing\n"
                        "import time\n\n"
                        "def cpu_heavy_task(n):\n"
                        "    return sum(i * i for i in range(n))\n\n"
                        "if __name__ == '__main__':\n"
                        "    numbers = [20_000_000, 20_000_000, 20_000_000, 20_000_000]\n"
                        "    \n"
                        "    start = time.perf_counter()\n"
                        "    # Pool will utilize all available CPU cores in parallel\n"
                        "    with multiprocessing.Pool() as pool:\n"
                        "        results = pool.map(cpu_heavy_task, numbers)\n"
                        "    \n"
                        "    print(f'Finished in {time.perf_counter() - start:.2f} seconds across cores!')"
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "Asyncio Advantage: Asyncio uses cooperative multitasking on a single thread. It can easily handle 50,000+ concurrent network connections with minimal RAM, where threading would exhaust OS resources."
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 5: Pandas & Tabular Data Manipulation
    # -------------------------------------------------------------------------
    {
        "topicSlug": "pandas-data-manipulation",
        "subjectSlug": "python",
        "title": "Pandas Data Structures & File I/O",
        "slug": "pandas-structures-io",
        "description": "Understand Series vs DataFrames, loading CSV/JSON datasets, inspecting shapes, types, and summary statistics.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "What is Pandas?",
                    "content": (
                        "Pandas is the industry-standard data manipulation library in Python. Built on top of NumPy, it provides fast, flexible, "
                        "and expressive data structures designed to work with structured, tabular data.\n\n"
                        "• Series: A 1-dimensional labeled array capable of holding any data type (like a single column in Excel).\n"
                        "• DataFrame: A 2-dimensional tabular structure with labeled rows and columns (like a complete SQL table or spreadsheet)."
                    )
                },
                {
                    "type": "code",
                    "title": "Creating DataFrames and Inspecting Data",
                    "language": "python",
                    "code": (
                        "import pandas as pd\n\n"
                        "data = {\n"
                        "    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],\n"
                        "    'Department': ['Engineering', 'Product', 'Engineering', 'Marketing'],\n"
                        "    'Salary': [95000, 88000, 115000, 62000],\n"
                        "    'Experience': [5, 4, 8, 2]\n"
                        "}\n\n"
                        "df = pd.DataFrame(data)\n\n"
                        "# Essential inspection methods\n"
                        "print('Shape (rows, cols):', df.shape)  # (4, 4)\n"
                        "print('\\nData Types:\\n', df.dtypes)\n"
                        "print('\\nSummary Stats:\\n', df.describe())\n"
                        "print('\\nFirst 2 rows:\\n', df.head(2))"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "pandas-data-manipulation",
        "subjectSlug": "python",
        "title": "Indexing, Cleaning & Filtering in Pandas",
        "slug": "pandas-indexing-cleaning",
        "description": "Master .loc vs .iloc selection, handling missing null data (dropna/fillna), and multi-condition boolean filtering.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "loc vs iloc: The Critical Distinction",
                    "content": (
                        "• `.loc[row_label, col_label]`: Label-based indexing. You specify the name of the row index and the column name.\n"
                        "  Example: `df.loc[0, 'Salary']`\n\n"
                        "• `.iloc[row_idx, col_idx]`: Integer position-based indexing (0 to n-1). You specify the numerical position.\n"
                        "  Example: `df.iloc[0, 2]`"
                    )
                },
                {
                    "type": "code",
                    "title": "Cleaning Missing Values and Boolean Filtering",
                    "language": "python",
                    "code": (
                        "import pandas as pd\n"
                        "import numpy as np\n\n"
                        "df = pd.DataFrame({\n"
                        "    'Emp': ['A', 'B', 'C', 'D'],\n"
                        "    'Score': [85, np.nan, 92, np.nan],\n"
                        "    'Dept': ['IT', 'HR', 'IT', 'Sales']\n"
                        "})\n\n"
                        "# 1. Detecting missing values\n"
                        "print('Missing counts:\\n', df.isna().sum())\n\n"
                        "# 2. Filling missing values with column mean\n"
                        "df['Score_Imputed'] = df['Score'].fillna(df['Score'].mean())\n\n"
                        "# 3. Boolean Filtering (Multi-condition with & / | and parentheses)\n"
                        "high_it = df[(df['Dept'] == 'IT') & (df['Score_Imputed'] > 80)]\n"
                        "print('\\nHigh IT employees:\\n', high_it)"
                    )
                },
                {
                    "type": "callout",
                    "variant": "warning",
                    "content": "Pandas Syntax Gotcha: In Python, `and` and `or` evaluate truthiness of entire objects. In Pandas, you MUST use bitwise operators `&` and `|`, and wrap each condition in parentheses: `(df['A'] > 5) & (df['B'] < 10)`."
                }
            ]
        }
    },
    {
        "topicSlug": "pandas-data-manipulation",
        "subjectSlug": "python",
        "title": "Grouping, Merging & Reshaping Data",
        "slug": "pandas-groupby-merges",
        "description": "Master Split-Apply-Combine with groupby(), merging/joining DataFrames, and generating pivot tables.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 3,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "GroupBy: The Split-Apply-Combine Pattern",
                    "content": (
                        "1. Split: Partition the dataset into groups based on key columns.\n"
                        "2. Apply: Compute aggregation functions (mean, sum, count, min, max) on each group.\n"
                        "3. Combine: Stitch the summary results into a clean new DataFrame."
                    )
                },
                {
                    "type": "code",
                    "title": "GroupBy Aggregations and pd.merge",
                    "language": "python",
                    "code": (
                        "import pandas as pd\n\n"
                        "employees = pd.DataFrame({\n"
                        "    'dept_id': [1, 2, 1, 3],\n"
                        "    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],\n"
                        "    'salary': [90000, 80000, 110000, 70000]\n"
                        "})\n\n"
                        "departments = pd.DataFrame({\n"
                        "    'dept_id': [1, 2, 4],\n"
                        "    'dept_name': ['Engineering', 'Marketing', 'Finance']\n"
                        "})\n\n"
                        "# 1. GroupBy department and compute stats\n"
                        "dept_summary = employees.groupby('dept_id')['salary'].agg(['mean', 'max', 'count'])\n"
                        "print('Dept Salary Stats:\\n', dept_summary)\n\n"
                        "# 2. Inner Merge (SQL Join equivalent)\n"
                        "merged_df = pd.merge(employees, departments, on='dept_id', how='inner')\n"
                        "print('\\nInner Join Result:\\n', merged_df)"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "pandas-data-manipulation",
        "subjectSlug": "python",
        "title": "Day 15: Working with CSV Files in Pandas (16 Parameters)",
        "slug": "day15-pandas-working-with-csv-files",
        "description": "Master all 16 parameters of pd.read_csv(): sep, usecols, dtypes, parse_dates, chunksize, converters, and memory optimization.",
        "estimatedTime": "35 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 4,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Mastering the 16 Parameters of pd.read_csv",
                    "content": (
                        "Pandas provides extensive controls for reading CSV and tabular data files:\n\n"
                        "1. `sep`: Set delimiter (e.g. `sep='\\t'` for TSV files).\n"
                        "2. `index_col`: Set primary key as index (`index_col='enrollee_id'`).\n"
                        "3. `header`: Choose header row index (`header=1`).\n"
                        "4. `usecols`: Select specific columns to drastically save memory (`usecols=['id', 'gender', 'target']`).\n"
                        "5. `squeeze`: Convert single column into a Series.\n"
                        "6. `nrows` & `skiprows`: Inspect samples or skip metadata headers.\n"
                        "7. `encoding`: Specify text encoding (`encoding='latin-1'`).\n"
                        "8. `on_bad_lines`: Skip corrupted lines (`on_bad_lines='skip'`).\n"
                        "9. `dtype`: Explicitly downcast column types (`dtype={'target': int}`).\n"
                        "10. `parse_dates`: Convert date strings into `datetime64[ns]`.\n"
                        "11. `converters`: Apply transformation functions on-the-fly (`converters={'team1': rename_func}`).\n"
                        "12. `na_values`: Define custom missing value tokens (`na_values=['Male', '?', 'N/A']`).\n"
                        "13. `chunksize`: Stream multi-GB files in manageable iterations (`chunksize=5000`)."
                    )
                },
                {
                    "type": "code",
                    "title": "Memory-Efficient Chunk Reading and Custom Converters",
                    "language": "python",
                    "code": (
                        "import pandas as pd\n\n"
                        "# 1. Read dates and custom converters\n"
                        "def standardize_team(name):\n"
                        "    return 'RCB' if name == 'Royal Challengers Bangalore' else name\n\n"
                        "df = pd.read_csv('IPL Matches 2008-2020.csv', parse_dates=['date'], converters={'team1': standardize_team})\n\n"
                        "# 2. Stream huge dataset in memory-friendly chunks\n"
                        "chunk_iterator = pd.read_csv('aug_train.csv', chunksize=5000, usecols=['enrollee_id', 'city', 'target'])\n"
                        "for chunk in chunk_iterator:\n"
                        "    print('Processing chunk with shape:', chunk.shape)"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "pandas-data-manipulation",
        "subjectSlug": "python",
        "title": "Day 16: Working with JSON & SQL in Pandas",
        "slug": "day16-pandas-working-with-json-and-sql",
        "description": "Read local and API JSON payloads with pd.read_json(), connect to relational databases, and query tables with pd.read_sql_query().",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 5,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "JSON and SQL Ingestion Pipelines",
                    "content": (
                        "Pandas natively bridges semi-structured JSON and relational SQL databases:\n\n"
                        "• **JSON Ingestion**: Use `pd.read_json()` on local files or directly against web endpoints.\n"
                        "• **SQL Database Queries**: Connect to MySQL/Postgres/SQLite and execute SQL queries directly into DataFrames with `pd.read_sql_query()`.\n"
                        "• **Writing Back to SQL**: Persist cleaned DataFrames back to database tables using `df.to_sql('table_name', conn, if_exists='replace')`."
                    )
                },
                {
                    "type": "code",
                    "title": "Querying SQL and Fetching API JSON",
                    "language": "python",
                    "code": (
                        "import pandas as pd\n"
                        "import mysql.connector\n\n"
                        "# 1. Read JSON from public API endpoint\n"
                        "rates_df = pd.read_json('https://api.exchangerate-api.com/v4/latest/INR')\n"
                        "print(rates_df.head())\n\n"
                        "# 2. Connect to MySQL and query records\n"
                        "conn = mysql.connector.connect(host='localhost', user='root', password='', database='world')\n"
                        "sql_df = pd.read_sql_query('SELECT CountryCode, Language, Percentage FROM countrylanguage WHERE Percentage > 50', conn)\n"
                        "print(sql_df.head())"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "pandas-data-manipulation",
        "subjectSlug": "python",
        "title": "Day 17: Ingesting REST APIs into Pandas DataFrames",
        "slug": "day17-pandas-api-to-dataframe",
        "description": "Fetch remote REST API payloads, unpack JSON responses into DataFrames, implement pagination loops, and export to CSV.",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate",
        "order": 6,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "API Ingestion & Multi-Page Pagination",
                    "content": (
                        "When data is hosted behind REST APIs, ingestion requires 3 steps:\n\n"
                        "1. **Request**: Call the endpoint using Python's `requests.get()` with API keys and headers.\n"
                        "2. **Parse**: Extract JSON records (`response.json()['results']`) and convert to `pd.DataFrame`.\n"
                        "3. **Pagination**: Iterate through pages, append records to a list, and combine using `pd.concat()`."
                    )
                },
                {
                    "type": "code",
                    "title": "Multi-Page REST API Ingestion Script",
                    "language": "python",
                    "code": (
                        "import requests\n"
                        "import pandas as pd\n\n"
                        "all_movies = []\n"
                        "for page in range(1, 10):\n"
                        "    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key=SAMPLE_KEY&language=en-US&page={page}'\n"
                        "    res = requests.get(url)\n"
                        "    if res.status_code == 200:\n"
                        "        data = res.json().get('results', [])\n"
                        "        all_movies.extend(data)\n\n"
                        "df = pd.DataFrame(all_movies)[['id', 'title', 'release_date', 'vote_average', 'vote_count']]\n"
                        "df.to_csv('movies_dataset.csv', index=False)\n"
                        "print('Total movies harvested:', df.shape)"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "pandas-data-manipulation",
        "subjectSlug": "python",
        "title": "Day 18: Web Scraping to Pandas DataFrames with BeautifulSoup",
        "slug": "day18-pandas-dataframe-using-web-scraping",
        "description": "Overcome HTTP 403 Forbidden with User-Agents, parse HTML with BeautifulSoup, extract card containers, and build DataFrames.",
        "estimatedTime": "40 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 7,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "HTML Web Scraping & Container Pattern",
                    "content": (
                        "Web scraping transforms raw unstructured website markup into structured pandas tables:\n\n"
                        "• **User-Agent Spoofing**: Pass browser headers to bypass HTTP 403 Forbidden bot blocks.\n"
                        "• **Container Pattern**: Always loop through parent container divs (`soup.find_all('div', class_='card')`) rather than parallel lists, ensuring missing fields do not desynchronize rows.\n"
                        "• **Error Handling**: Use `try...except` to assign `np.nan` for missing metadata tags."
                    )
                },
                {
                    "type": "code",
                    "title": "Multi-Page Web Scraping to DataFrame",
                    "language": "python",
                    "code": (
                        "import requests\n"
                        "from bs4 import BeautifulSoup\n"
                        "import pandas as pd\n"
                        "import numpy as np\n\n"
                        "headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0.0.0'}\n"
                        "records = []\n\n"
                        "webpage = requests.get('https://www.ambitionbox.com/list-of-companies?page=1', headers=headers).text\n"
                        "soup = BeautifulSoup(webpage, 'lxml')\n"
                        "cards = soup.find_all('div', class_='company-content-wrapper')\n\n"
                        "for card in cards:\n"
                        "    name = card.find('h2').text.strip() if card.find('h2') else np.nan\n"
                        "    rating = card.find('p', class_='rating').text.strip() if card.find('p', class_='rating') else np.nan\n"
                        "    records.append({'company': name, 'rating': rating})\n\n"
                        "df = pd.DataFrame(records)\n"
                        "print(df.head())"
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 6: Git & Collaborative Version Control
    # -------------------------------------------------------------------------
    {
        "topicSlug": "git-version-control",
        "subjectSlug": "python",
        "title": "Git Internals & Core Architecture",
        "slug": "git-internals-workflow",
        "description": "Understand distributed version control, the 4 Git areas, SHA-1 content addressing, DAG commit trees, and blobs.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "How Git Revolutionized Version Control",
                    "content": (
                        "Created by Linus Torvalds in 2005 for Linux kernel development, Git is a Distributed Version Control System (DVCS). "
                        "Unlike centralized systems (like SVN) where every commit requires an online connection to a central server, "
                        "every Git clone contains the FULL project history locally on your disk. You can branch, commit, and diff completely offline."
                    )
                },
                {
                    "type": "explanation",
                    "title": "The 4 Areas of Git",
                    "content": (
                        "1. Working Directory: The actual files on your filesystem that you edit.\n"
                        "2. Staging Area (Index): The prep zone where changes are selected (`git add`) for the next snapshot.\n"
                        "3. Local Repository (`.git`): Permanent compressed snapshots stored as a DAG of commit objects on your local machine (`git commit`).\n"
                        "4. Remote Repository: The shared remote hub on GitHub / GitLab (`git push`)."
                    )
                },
                {
                    "type": "explanation",
                    "title": "The Internal Object Model: Blobs, Trees, and Commits",
                    "content": (
                        "Git is fundamentally a content-addressable key-value database stored in `.git/objects`:\n\n"
                        "• Blob: Stores raw file content (identified by the SHA-1 hash of its contents).\n"
                        "• Tree: A directory listing containing filenames, permissions, and pointers to blobs or sub-trees.\n"
                        "• Commit: Contains the root tree hash, author, committer, timestamp, commit message, and parent commit hash(es)."
                    )
                },
                {
                    "type": "code",
                    "title": "Core Git Daily Commands",
                    "language": "bash",
                    "code": (
                        "# Check repository state\n"
                        "git status\n\n"
                        "# Stage files\n"
                        "git add app/main.py\n\n"
                        "# Commit snapshot with message\n"
                        "git commit -m \"feat: implement user authentication endpoint\"\n\n"
                        "# View visual commit graph\n"
                        "git log --oneline --graph --all"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "git-version-control",
        "subjectSlug": "python",
        "title": "Branching, Merging & Conflict Resolution",
        "slug": "git-branching-merging",
        "description": "Master pointer-based branching, fast-forward vs 3-way merges, resolving merge conflicts, and rebase vs merge tradeoffs.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Why Git Branching is Lightning Fast",
                    "content": (
                        "In older version control systems, creating a branch meant copying the entire codebase on disk (slow and heavy). "
                        "In Git, a branch is literally a tiny 41-byte text file inside `.git/refs/heads/` that stores a single 40-character SHA commit hash! "
                        "Creating a branch costs 1 file write and takes 2 milliseconds."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Fast-Forward vs 3-Way Merge",
                    "content": (
                        "• Fast-Forward Merge: If `main` has not had any new commits since your feature branch split off, Git simply moves the `main` pointer forward to point to your latest commit. No merge commit is created.\n\n"
                        "• 3-Way Merge (Recursive): If `main` has new commits while you were working, Git finds the Common Ancestor commit, combines changes from both branches, and creates a new 'Merge Commit' with two parents."
                    )
                },
                {
                    "type": "explanation",
                    "title": "How to Resolve Merge Conflicts",
                    "content": (
                        "A merge conflict occurs when two branches modify the EXACT SAME line in a file, and Git doesn't know which version you want to keep.\n\n"
                        "Git marks the file with conflict markers:\n"
                        "```\n"
                        "<<<<<<< HEAD\n"
                        "PORT = 8000  # from current branch\n"
                        "=======\n"
                        "PORT = 9000  # from incoming branch\n"
                        ">>>>>>> feature-branch\n"
                        "```\n"
                        "To resolve: Edit the file, remove the conflict markers, keep the desired code, then run `git add filename` and `git commit`!"
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Rebase vs Merge: `git merge` preserves full history and exact timestamps with merge commits. `git rebase` rewrites commits on top of the target branch for a clean, linear commit history."
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic: Python Basics & Core Fundamentals
    # -------------------------------------------------------------------------
    {
        "topicSlug": "python-basics-programming",
        "subjectSlug": "python",
        "title": "Python Syntax, Variables, Literals & Operators",
        "slug": "python-syntax-variables-operators",
        "description": "Core Python syntax, dynamic typing, keywords, naming identifiers, statement indentation, numeric/string literals, and arithmetic, logical & bitwise operators.",
        "estimatedTime": "30 mins",
        "difficulty": "Beginner",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Python Syntax, Indentation & Identifiers",
                    "content": (
                        "• Python is dynamically and strongly typed: variables are references bound to objects in memory; types are checked at runtime.\n"
                        "• Indentation defines block scope (typically 4 spaces) rather than curly braces `{}`.\n"
                        "• Identifiers: Can contain letters, digits, and underscores, but cannot start with a digit. Case-sensitive (`total` vs `Total`).\n"
                        "• Keywords: Reserved words (e.g., `def`, `class`, `if`, `is`, `in`, `lambda`, `yield`, `pass`, `del`) that cannot be used as identifiers."
                    )
                },
                {
                    "type": "code",
                    "title": "Variables, Multiple Assignment & Arithmetic Operators",
                    "language": "python",
                    "code": (
                        "# Multiple variable assignment\n"
                        "a, b, c = 10, 20.5, 'Python'\n\n"
                        "# Arithmetic operators\n"
                        "print('Floor Division:', 17 // 3)  # 5\n"
                        "print('Modulo:', 17 % 3)          # 2\n"
                        "print('Exponentiation:', 2 ** 5)   # 32\n\n"
                        "# Identity vs Equality\n"
                        "x = [1, 2, 3]\n"
                        "y = [1, 2, 3]\n"
                        "print('Equality (==):', x == y)    # True (same values)\n"
                        "print('Identity (is):', x is y)    # False (different memory addresses!)"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "python-basics-programming",
        "subjectSlug": "python",
        "title": "Type Conversion, Input/Output & Namespaces",
        "slug": "python-type-conversion-io",
        "description": "Implicit vs explicit type conversion, formatted string interpolation (f-strings), console I/O, and namespace symbol tables.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Type Conversion: Implicit vs Explicit Casting",
                    "content": (
                        "• Implicit Type Conversion: Python automatically promotes smaller types to avoid data loss (e.g., adding `int` + `float` results in `float`).\n\n"
                        "• Explicit Type Conversion (Type Casting): Developer explicitly converts values using built-in constructors (`int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`)."
                    )
                },
                {
                    "type": "code",
                    "title": "Type Casting and Formatted f-Strings",
                    "language": "python",
                    "code": (
                        "# Explicit casting\n"
                        "num_str = '42'\n"
                        "num_int = int(num_str)\n\n"
                        "# Modern f-string formatting with specifiers\n"
                        "pi = 3.14159265\n"
                        "print(f'Value of Pi: {pi:.2f}')       # 3.14\n"
                        "print(f'Hexadecimal: {255:#x}')        # 0xff\n"
                        "print(f'Binary: {42:#b}')             # 0b101010"
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic: Flow Control, Loops & Conditionals
    # -------------------------------------------------------------------------
    {
        "topicSlug": "python-flow-control",
        "subjectSlug": "python",
        "title": "Conditionals: if, elif, else & Nested Logic",
        "slug": "python-conditional-statements",
        "description": "Master boolean expressions, truthy/falsy evaluation, chained if-elif-else branches, and nested decision trees.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Truthy vs Falsy in Python",
                    "content": (
                        "In Python, all objects evaluate to a boolean context:\n"
                        "• Falsy values: `False`, `None`, `0`, `0.0`, `''` (empty string), `[]` (empty list), `()` (empty tuple), `{}` (empty dict), `set()`.\n"
                        "• Truthy values: Any non-zero number, non-empty collection, or custom object whose `__bool__()` or `__len__()` returns non-zero."
                    )
                },
                {
                    "type": "code",
                    "title": "Clean Conditional Branching and Ternary Operator",
                    "language": "python",
                    "code": (
                        "score = 88\n\n"
                        "if score >= 90:\n"
                        "    grade = 'A'\n"
                        "elif score >= 80:\n"
                        "    grade = 'B'\n"
                        "elif score >= 70:\n"
                        "    grade = 'C'\n"
                        "else:\n"
                        "    grade = 'F'\n\n"
                        "# Python Ternary Expression (One-line conditional)\n"
                        "status = 'Passed' if score >= 70 else 'Failed'\n"
                        "print(f'Grade: {grade}, Status: {status}')"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "python-flow-control",
        "subjectSlug": "python",
        "title": "Loops: for, while, range, break, continue & pass",
        "slug": "python-loops-control-flow",
        "description": "Definite iteration with for loops, indefinite iteration with while loops, range() generation, early exit, skipping, and loop-else clauses.",
        "estimatedTime": "30 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Loop Control Statements & The loop-else Clause",
                    "content": (
                        "• `break`: Immediately terminates the innermost loop.\n"
                        "• `continue`: Skips the remainder of the current iteration and jumps to the next loop cycle.\n"
                        "• `pass`: Null statement used as a syntactic placeholder.\n"
                        "• Loop `else` clause: Executes ONLY if the loop completed normally without encountering a `break` statement!"
                    )
                },
                {
                    "type": "code",
                    "title": "Prime Number Search using for-else and break",
                    "language": "python",
                    "code": (
                        "def is_prime(n):\n"
                        "    if n < 2:\n"
                        "        return False\n"
                        "    for i in range(2, int(n ** 0.5) + 1):\n"
                        "        if n % i == 0:\n"
                        "            break  # Found divisor, not prime!\n"
                        "    else:\n"
                        "        return True  # Executed only if no break occurred!\n"
                        "    return False\n\n"
                        "print('Is 29 prime?', is_prime(29))  # True\n"
                        "print('Is 35 prime?', is_prime(35))  # False"
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic: File I/O, Exceptions & Regular Expressions
    # -------------------------------------------------------------------------
    {
        "topicSlug": "python-files-regex",
        "subjectSlug": "python",
        "title": "File I/O: Reading, Writing & Context Managers",
        "slug": "python-file-io-operations",
        "description": "Open modes (r, w, a, x, b, +), buffered I/O, cursor seeking (tell, seek), encoding parameters, and the with statement.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "File Modes & Resource Safety",
                    "content": (
                        "• `'r'`: Read (default, throws FileNotFoundError if absent).\n"
                        "• `'w'`: Write (truncates/overwrites existing file).\n"
                        "• `'a'`: Append (writes to end of file without truncating).\n"
                        "• `'b'`: Binary mode (for images, audio, compiled binaries).\n\n"
                        "Always use `with open(...) as f:` to guarantee proper OS file descriptor closure even in the event of unhandled exceptions."
                    )
                },
                {
                    "type": "code",
                    "title": "Safe File Writing, Reading & Line Iteration",
                    "language": "python",
                    "code": (
                        "# Writing text to file\n"
                        "with open('sample.txt', 'w', encoding='utf-8') as f:\n"
                        "    f.write('Python Data Engineering\\n')\n"
                        "    f.writelines(['Line 1\\n', 'Line 2\\n', 'Line 3\\n'])\n\n"
                        "# Memory-efficient line-by-line streaming\n"
                        "with open('sample.txt', 'r', encoding='utf-8') as f:\n"
                        "    for line_num, line in enumerate(f, start=1):\n"
                        "        print(f'{line_num}: {line.strip()}')"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "python-files-regex",
        "subjectSlug": "python",
        "title": "Exception Handling & Regular Expressions",
        "slug": "python-exceptions-and-regex",
        "description": "Structured exception handling (try-except-else-finally), raising custom exceptions, and pattern matching with the re module.",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Full try-except-else-finally Lifecycle",
                    "content": (
                        "• `try`: Block containing code that might raise an exception.\n"
                        "• `except SpecificError as e`: Handles specific exception type.\n"
                        "• `else`: Runs ONLY if NO exception was raised in the `try` block.\n"
                        "• `finally`: Runs ALWAYS, regardless of exceptions (ideal for resource cleanup)."
                    )
                },
                {
                    "type": "code",
                    "title": "Exception Handling and Regular Expression Pattern Matching",
                    "language": "python",
                    "code": (
                        "import re\n\n"
                        "# Robust exception handling\n"
                        "try:\n"
                        "    val = int('42')\n"
                        "except ValueError as err:\n"
                        "    print('Conversion error:', err)\n"
                        "else:\n"
                        "    print('Conversion success:', val)\n"
                        "finally:\n"
                        "    print('Execution complete.')\n\n"
                        "# Regular Expressions with re module\n"
                        "text = 'Contact support@nexuslearn.io or info@learni.com for questions.'\n"
                        "email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'\n"
                        "emails = re.findall(email_pattern, text)\n"
                        "print('Extracted emails:', emails)  # ['support@nexuslearn.io', 'info@learni.com']"
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic: NumPy & High-Performance Array Computing
    # -------------------------------------------------------------------------
    {
        "topicSlug": "python-numpy-numerical",
        "subjectSlug": "python",
        "title": "NumPy ndarrays, Indexing, Slicing & Broadcasting",
        "slug": "numpy-arrays-vectorization",
        "description": "Contiguous C-memory layouts in ndarray, multidimensional slicing, vectorization benefits over loops, and broadcasting rules.",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Why NumPy is 50x-100x Faster than Python Lists",
                    "content": (
                        "• Python Lists: Store arrays of pointers to Python objects scattered across heap memory. Iterating causes CPU cache misses and pointer indirection overhead.\n\n"
                        "• NumPy ndarrays: Store homogeneous data types (e.g., `int64`, `float32`) contiguously in raw C-memory blocks with SIMD (Single Instruction Multiple Data) vectorization."
                    )
                },
                {
                    "type": "code",
                    "title": "Creating ndarrays, Slicing & Broadcasting",
                    "language": "python",
                    "code": (
                        "import numpy as np\n\n"
                        "# Array creation\n"
                        "arr = np.arange(1, 10).reshape((3, 3))\n"
                        "print('2D Array:\\n', arr)\n\n"
                        "# Slicing rows and columns: arr[row_slice, col_slice]\n"
                        "print('Top-right 2x2 submatrix:\\n', arr[:2, 1:])\n\n"
                        "# Broadcasting: 3x3 matrix + 1D array of 3 elements\n"
                        "bias = np.array([10, 20, 30])\n"
                        "print('Broadcasting addition:\\n', arr + bias)"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "python-numpy-numerical",
        "subjectSlug": "python",
        "title": "NumPy Reshaping, Stacking & Statistical Operations",
        "slug": "numpy-array-manipulation-stats",
        "description": "Reshaping arrays, vertical and horizontal stacking, axis-based aggregations (mean, std, sum, argmax), and boolean masking.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Array Manipulation & Axis Semantics",
                    "content": (
                        "• `axis=0`: Operates along the rows (downwards, across columns).\n"
                        "• `axis=1`: Operates along the columns (horizontally, across rows).\n"
                        "• `reshape(-1, n)`: Automatically calculates the unknown dimension."
                    )
                },
                {
                    "type": "code",
                    "title": "Axis-based Statistics and Boolean Masking",
                    "language": "python",
                    "code": (
                        "import numpy as np\n\n"
                        "data = np.array([\n"
                        "    [10, 25, 30],\n"
                        "    [40, 55, 60],\n"
                        "    [70, 85, 90]\n"
                        "])\n\n"
                        "print('Column Means (axis=0):', data.mean(axis=0))\n"
                        "print('Row Sums (axis=1):', data.sum(axis=1))\n"
                        "print('Max index per row:', data.argmax(axis=1))\n\n"
                        "# Boolean Indexing (Filtering without loops)\n"
                        "greater_than_50 = data[data > 50]\n"
                        "print('Elements > 50:', greater_than_50)"
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic: Data Visualization with Matplotlib & Seaborn
    # -------------------------------------------------------------------------
    {
        "topicSlug": "python-data-visualization",
        "subjectSlug": "python",
        "title": "Data Visualization: Matplotlib Charts & Seaborn Distributions",
        "slug": "matplotlib-seaborn-visualizations",
        "description": "Construct publication-ready figures: line charts, scatter plots, histograms, heatmaps, box plots, and multi-panel subplots.",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Matplotlib Object-Oriented API vs Seaborn",
                    "content": (
                        "• Matplotlib (Object-Oriented): Explicitly instantiate `fig, ax = plt.subplots()`. Provides granular control over axes, ticks, spines, labels, and figure dimensions.\n\n"
                        "• Seaborn: High-level statistical visualization library built on top of Matplotlib that integrates seamlessly with Pandas DataFrames and color palettes."
                    )
                },
                {
                    "type": "code",
                    "title": "Plotting Subplots and Correlation Heatmaps",
                    "language": "python",
                    "code": (
                        "import matplotlib.pyplot as plt\n"
                        "import seaborn as sns\n"
                        "import pandas as pd\n"
                        "import numpy as np\n\n"
                        "# Matplotlib subplots\n"
                        "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))\n"
                        "x = np.linspace(0, 10, 100)\n"
                        "ax1.plot(x, np.sin(x), color='indigo', label='sin(x)')\n"
                        "ax1.set_title('Sine Wave')\n"
                        "ax1.legend()\n\n"
                        "# Seaborn correlation heatmap\n"
                        "df = pd.DataFrame(np.random.rand(5, 5), columns=list('ABCDE'))\n"
                        "sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax2)\n"
                        "ax2.set_title('Feature Correlation Matrix')\n"
                        "plt.tight_layout()"
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic: DateTime, Timestamps & Time Profiling
    # -------------------------------------------------------------------------
    {
        "topicSlug": "python-datetime-time",
        "subjectSlug": "python",
        "title": "datetime & time Modules: strftime, strptime & Profiling",
        "slug": "datetime-time-module-mastery",
        "description": "Manipulate dates, times, timedeltas, format timestamps with strftime, parse ISO strings with strptime, and benchmark with time.perf_counter().",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "strftime vs strptime: The Essential Mnemonic",
                    "content": (
                        "• `strftime()` (String Format Time): datetime object → formatted string (`f` = format for display).\n"
                        "• `strptime()` (String Parse Time): string input → datetime object (`p` = parse into object).\n\n"
                        "Common Directives:\n"
                        "• `%Y`: 4-digit year (e.g., 2026)\n"
                        "• `%m`: 2-digit month (01-12)\n"
                        "• `%d`: 2-digit day of the month (01-31)\n"
                        "• `%H`: Hour in 24-hour format (00-23)\n"
                        "• `%M`: Minute (00-59)\n"
                        "• `%S`: Second (00-59)"
                    )
                },
                {
                    "type": "code",
                    "title": "Parsing, Formatting and Measuring Code Execution",
                    "language": "python",
                    "code": (
                        "from datetime import datetime, timedelta\n"
                        "import time\n\n"
                        "# Parsing string to datetime\n"
                        "date_str = '2026-09-28 14:30:00'\n"
                        "dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')\n\n"
                        "# Date arithmetic with timedelta\n"
                        "future_dt = dt + timedelta(days=7, hours=3)\n"
                        "print('Future Date:', future_dt.strftime('%A, %B %d, %Y'))\n\n"
                        "# High-precision performance benchmarking\n"
                        "start = time.perf_counter()\n"
                        "total = sum(i ** 2 for i in range(100_000))\n"
                        "duration = time.perf_counter() - start\n"
                        "print(f'Execution duration: {duration:.4f} seconds')"
                    )
                }
            ]
        }
    },
]

