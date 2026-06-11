# Standard Library Navigation

Python's standard library contains hundreds of modules. Knowing how to discover and explore them is a key skill.

## Discovering Available Modules

```python
# See all available modules (huge list!)
help("modules")

# Check if a specific module exists
import importlib
spec = importlib.util.find_spec("json")
print(spec is not None)  # True — json exists
```

## Exploring a Module

```python
import json

# See all names in the module
dir(json)

# Get help on a specific function
help(json.dumps)
```

## `dir()` — List Module Contents

```python
import os

# All public names (filter out private ones)
public = [name for name in dir(os) if not name.startswith("_")]
```

## `help()` — Read Documentation

```python
import math
help(math.sqrt)
# Shows: sqrt(x) — Return the square root of x.
```

## Useful Standard Library Modules

| Module | Purpose |
|--------|---------|
| `json` | Read/write JSON data |
| `csv` | Read/write CSV files |
| `re` | Regular expressions |
| `pathlib` | Modern file path handling |
| `collections` | Specialized data structures |
| `functools` | Higher-order functions |
| `itertools` | Iterator building blocks |
| `time` | Time functions |
| `copy` | Shallow and deep copy |
| `pprint` | Pretty printing |

## Key Points

- Use `dir(module)` to see what's available
- Use `help(module.name)` to read documentation
- Python's standard library is vast — explore it!
- The official docs (docs.python.org) are the best reference
