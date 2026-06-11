# Importing Modules

Python provides several ways to import code from modules. Each has its own use case.

## 1. `import module_name`

Imports the entire module. Access contents with dot notation.

```python
import math

print(math.pi)        # 3.14159...
print(math.sqrt(16))  # 4.0
```

## 2. `from module_name import name`

Imports specific items directly into your namespace.

```python
from math import pi, sqrt

print(pi)        # 3.14159... (no math. prefix needed)
print(sqrt(16))  # 4.0
```

## 3. `from module_name import *`

Imports **everything** from the module into your namespace.

```python
from math import *

print(pi)       # works
print(sqrt(9))  # works
print(ceil(3.2))  # works
```

> ⚠️ **Warning:** This is generally bad practice because:
> - You don't know what names are imported
> - It can overwrite your own variables
> - It makes code harder to read

## When to Use Which?

| Syntax | When to Use |
|--------|------------|
| `import math` | When using many things from the module |
| `from math import sqrt` | When using only a few specific things |
| `from math import *` | Almost never — avoid in real code |

## Key Points

- `import module` — safe, clear, uses dot notation
- `from module import name` — convenient for a few items
- `from module import *` — risky, avoid in production code
- Always prefer clarity over convenience
