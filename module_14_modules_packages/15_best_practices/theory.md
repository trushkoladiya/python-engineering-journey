# Best Practices for Modules & Packages

Follow these guidelines to write clean, maintainable, and professional Python code.

## Import Best Practices

### 1. Avoid Wildcard Imports
```python
# BAD
from math import *

# GOOD
from math import sqrt, pi
import math
```

### 2. Group and Order Imports
```python
# Standard library imports
import os
import sys
import json

# Third-party imports
import requests
import numpy as np

# Local imports
from myproject.utils import helpers
from myproject.models import User
```

### 3. One Import Per Line
```python
# BAD
import os, sys, json

# GOOD
import os
import sys
import json
```

### 4. Import at the Top of the File
```python
# Imports go at the TOP, after docstring and comments
import os
import sys

# Then your code
def my_function():
    ...
```

## Module Naming

- Use **lowercase** names: `my_module.py` ✅ not `MyModule.py` ❌
- Use **underscores** for multi-word: `string_helpers.py` ✅
- **Never** name files after standard library modules (`random.py` ❌)

## Modular Design

- Each module should have a **single responsibility**
- Keep modules **focused and small**
- Use `__init__.py` to provide **clean public APIs**
- Document with docstrings

## Key Points

- Avoid `from module import *` — it pollutes the namespace
- Group imports: stdlib → third-party → local
- Name modules with lowercase and underscores
- Keep modules focused — one responsibility per module
- Always use `if __name__ == "__main__":` for script code
