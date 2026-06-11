# Code Organization Patterns

Good code organization makes projects easier to understand, maintain, and extend.

## Separating Logic into Modules

Instead of one giant file, split code by responsibility:

```
# BAD: everything in one file
main.py  (500+ lines of mixed code)

# GOOD: separated by purpose
models.py       ← data classes
validators.py   ← input validation
formatters.py   ← output formatting
database.py     ← data storage
main.py         ← ties everything together
```

## Grouping Related Code

Group modules that work together into packages:

```
project/
├── auth/               ← authentication
│   ├── __init__.py
│   ├── login.py
│   └── permissions.py
├── data/               ← data handling
│   ├── __init__.py
│   ├── readers.py
│   └── writers.py
├── utils/              ← shared utilities
│   ├── __init__.py
│   ├── validators.py
│   └── formatters.py
└── main.py
```

## Common Patterns

1. **One class per file** — for large classes
2. **Related functions in one module** — for utility functions
3. **Constants in a separate file** — `constants.py` or `config.py`
4. **Entry point in `main.py`** — uses `if __name__ == "__main__":`

## Key Points

- Split code by **responsibility** (what it does)
- Group related modules into **packages** (folders)
- Keep modules focused — each does ONE thing well
- Use `main.py` as the entry point that ties everything together
