# `__init__.py` — Package Initialization

The `__init__.py` file is what makes a directory a Python package. It runs automatically when the package is imported.

## Purpose

1. **Marks a directory as a package** — Python won't treat it as a package without this file
2. **Runs initialization code** — executed when the package is first imported
3. **Controls what gets exported** — defines what `from package import *` includes

## Empty `__init__.py`

The simplest case — just marks the folder as a package:

```python
# mypackage/__init__.py
# (empty file)
```

## `__init__.py` with Imports

You can make the package easier to use by importing key items:

```python
# shapes/__init__.py
from .circle import Circle
from .rectangle import Rectangle

# Now users can do:
# from shapes import Circle, Rectangle
# Instead of:
# from shapes.circle import Circle
```

## `__all__` — Controlling Wildcard Imports

The `__all__` list controls what `from package import *` exports:

```python
# mypackage/__init__.py
__all__ = ["Circle", "Rectangle"]

# Now 'from mypackage import *' only imports these two
```

## Key Points

- `__init__.py` makes a directory a Python package
- It runs when the package is first imported
- Use it to provide convenient top-level imports
- Use `__all__` to control wildcard import behavior
- It can be empty — that's perfectly fine
