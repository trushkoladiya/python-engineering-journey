# Module Usage Patterns

Once you import a module, there are several patterns for accessing and using its contents effectively.

## Dot Notation

When you use `import module_name`, access everything with a dot:

```python
import math

math.pi         # variable
math.sqrt(16)   # function
```

The dot tells Python: "Look inside the `math` namespace for this name."

## Aliasing with `as`

You can give a module (or imported name) a shorter alias:

```python
import math as m

print(m.pi)       # same as math.pi
print(m.sqrt(9))  # same as math.sqrt(9)
```

Common conventions:
```python
import numpy as np          # everyone uses np
import pandas as pd         # everyone uses pd
import matplotlib.pyplot as plt  # everyone uses plt
```

## Aliasing Specific Imports

You can also alias individual names:

```python
from math import factorial as fact

print(fact(5))  # 120
```

This is useful when:
- The original name is long
- There's a name clash with your own code

## Selective Imports

Import only what you need — keeps your namespace clean:

```python
from random import randint, choice

# Only randint and choice are available
# Other random functions are NOT imported
```

## Key Points

- Dot notation (`module.name`) is the clearest approach
- Use `as` to create short, convenient aliases
- Follow community conventions for common aliases
- Selective imports keep your namespace clean
