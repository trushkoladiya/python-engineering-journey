# Environment & Path Handling

When you import a module, Python searches specific locations. Understanding `sys.path` helps you control where Python looks.

## `sys.path` — The Search Path

`sys.path` is a list of directories Python searches when you `import`:

```python
import sys
for path in sys.path:
    print(path)
```

## Search Order

Python searches in this order:
1. **Current directory** (or script's directory)
2. **PYTHONPATH** environment variable directories
3. **Standard library** directories
4. **Site-packages** (installed third-party packages)

## Adding to the Path

```python
import sys

# Add a directory temporarily
sys.path.append("/path/to/my/modules")
sys.path.insert(0, "/path/to/priority/modules")  # search first
```

## Module Search Mechanism

When you write `import mymodule`, Python:
1. Checks `sys.modules` (cache) first
2. Searches each directory in `sys.path`
3. Looks for `mymodule.py` or `mymodule/` (package)
4. If found → loads and caches it
5. If not found → raises `ImportError`

## Key Points

- `sys.path` controls where Python looks for modules
- The current directory is usually first in the path
- You can add directories with `sys.path.append()`
- `ImportError` means Python couldn't find the module
- Understanding the path helps debug import issues
