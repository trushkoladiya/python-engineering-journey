# What is a Module?

A **module** is simply a Python file (`.py`) that contains code — variables, functions, classes — that you can reuse in other files.

## Why Modules?

Without modules, you'd put **all** your code in one file. As projects grow, that becomes unreadable and unmaintainable.

Modules let you:
- **Organize** code into logical files
- **Reuse** code across different programs
- **Share** code with others

## Every `.py` File is a Module

If you create a file called `helpers.py`, that file is a module named `helpers`.

```python
# helpers.py
greeting = "Hello from helpers!"

def add(a, b):
    return a + b

class Calculator:
    def __init__(self):
        self.history = []
```

Any other Python file can now **import** and use this code.

## You've Already Used Modules

When you wrote:
```python
import math
```

You were importing Python's built-in `math` module — a `.py` file (or C extension) that comes with Python.

## Module = Reusability

The key idea: **write once, use everywhere**.

```python
# utils.py
def square(n):
    return n ** 2

def cube(n):
    return n ** 3
```

```python
# main.py
import utils
print(utils.square(5))   # 25
print(utils.cube(3))     # 27
```

## Key Points

- A module is a `.py` file containing Python code
- Modules promote code reuse and organization
- Python has many built-in modules (you'll explore them soon)
- You can create your own modules easily
