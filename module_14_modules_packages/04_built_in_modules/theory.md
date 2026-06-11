# Built-in Modules

Python comes with a rich **standard library** — a collection of modules available without installing anything extra.

## `math` — Mathematical Functions

```python
import math

math.pi          # 3.14159...
math.sqrt(16)    # 4.0
math.ceil(3.1)   # 4
math.floor(3.9)  # 3
math.factorial(5)  # 120
math.gcd(12, 8)  # 4
```

## `random` — Random Number Generation

```python
import random

random.randint(1, 10)       # random int between 1 and 10
random.choice(["a", "b"])   # pick random item
random.shuffle(my_list)     # shuffle in place
random.random()             # float between 0.0 and 1.0
```

## `sys` — System Information

```python
import sys

sys.version          # Python version string
sys.platform         # 'linux', 'win32', 'darwin'
sys.path             # where Python looks for modules
sys.argv             # command line arguments
```

## `os` — Operating System Interface

```python
import os

os.name              # 'posix' or 'nt'
os.getcwd()          # current working directory
os.listdir(".")      # list files in directory
os.path.exists("file.txt")  # check if file exists
```

## `datetime` — Dates and Times

```python
import datetime

datetime.datetime.now()     # current date and time
datetime.date.today()       # today's date
```

## `collections` — Specialized Data Structures

```python
from collections import Counter, defaultdict

Counter(["a", "b", "a"])     # Counter({'a': 2, 'b': 1})
defaultdict(list)            # dict with default values
```

## Key Points

- Python's standard library is huge and powerful
- No installation needed — these modules come with Python
- `math`, `random`, `sys`, `os`, `datetime` are the most commonly used
- Use `dir(module)` to explore what a module offers
