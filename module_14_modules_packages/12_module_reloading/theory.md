# Module Reloading & Caching

Python caches modules after the first import. Understanding this behavior helps you debug import-related issues.

## Module Caching

When you import a module, Python:
1. Checks if it's already in `sys.modules` (the cache)
2. If yes — returns the cached version (does NOT re-execute the file)
3. If no — loads, executes, and caches the module

```python
import sys

# All cached modules
print(len(sys.modules))  # hundreds of modules!

# Check if a specific module is cached
"math" in sys.modules  # True (if imported before)
```

## Why Caching Matters

```python
import mymodule   # executes mymodule.py
import mymodule   # does NOTHING — uses cache

# Even if you change mymodule.py between imports,
# the second import uses the OLD cached version!
```

## Reloading Modules with `importlib`

To force Python to re-read and re-execute a module:

```python
import importlib
import mymodule

# ... make changes to mymodule.py ...

importlib.reload(mymodule)  # re-reads and re-executes
```

> **Note:** `reload()` only works on modules that were already imported.

## Key Points

- Python caches modules in `sys.modules` after first import
- Repeated `import` statements use the cache — no re-execution
- Use `importlib.reload()` to force re-loading
- Caching is efficient — modules load only once
- Be careful with reload — it can cause inconsistencies
