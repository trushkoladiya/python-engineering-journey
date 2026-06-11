# Creating Custom Modules

You can create your own modules by simply writing a `.py` file and importing it from another file.

## Step 1: Create a Module File

Create a file called `mymath.py`:

```python
# mymath.py

PI = 3.14159

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def square(n):
    return n ** 2
```

## Step 2: Import and Use It

In another file (same directory):

```python
# main.py
import mymath

print(mymath.PI)          # 3.14159
print(mymath.add(3, 4))   # 7
print(mymath.square(5))   # 25
```

Or import specific items:

```python
from mymath import add, square

print(add(10, 20))   # 30
print(square(6))     # 36
```

## Organizing Functions into Files

A common pattern is grouping related functions:

```
project/
├── validators.py    ← validation functions
├── formatters.py    ← formatting functions
├── calculators.py   ← math functions
└── main.py          ← uses all of them
```

## Key Points

- Any `.py` file is a module — just import its name (without `.py`)
- The module must be in the same directory (or on Python's path)
- Group related functions together in one module
- Use clear, descriptive module names
