# Packages Basics

A **package** is a folder that contains Python modules. It's the next level of code organization.

## Module vs Package

| Concept | What it is |
|---------|-----------|
| Module | A single `.py` file |
| Package | A folder containing modules |

## Basic Package Structure

```
mypackage/
├── __init__.py     ← makes it a package
├── module_a.py
├── module_b.py
└── module_c.py
```

The `__init__.py` file tells Python: "This folder is a package."

## Using a Package

```python
# Import a module from the package
import mypackage.module_a

# Or import specific items
from mypackage.module_b import some_function
```

## Nested Packages (Sub-packages)

Packages can contain other packages:

```
myproject/
├── __init__.py
├── utils/
│   ├── __init__.py
│   ├── math_helpers.py
│   └── string_helpers.py
└── models/
    ├── __init__.py
    └── user.py
```

```python
from myproject.utils.math_helpers import add
from myproject.models.user import User
```

## Why Use Packages?

- **Organization:** Group related modules together
- **Scalability:** Easy to add new modules
- **Namespacing:** Avoid name clashes between modules
- **Distribution:** Share your code as installable packages

## Key Points

- A package is a folder with an `__init__.py` file
- Packages contain modules (and sub-packages)
- Use dot notation to import from packages
- Packages help organize large projects
