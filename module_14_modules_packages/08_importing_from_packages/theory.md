# Importing from Packages

When importing from packages, Python supports two styles: **absolute imports** and **relative imports**.

## Absolute Imports

Use the full path from the project root:

```python
from myproject.utils.helpers import format_name
from myproject.models.user import User
import myproject.database
```

**Advantages:**
- Clear and explicit
- Easy to see where code comes from
- Recommended by PEP 8

## Relative Imports

Use dots to refer to the current or parent package:

```python
# Inside myproject/utils/helpers.py

from . import validators          # same package (utils/)
from .validators import is_valid  # specific item from same package
from .. import models             # parent package (myproject/)
from ..models import user         # module in parent's sub-package
```

| Syntax | Meaning |
|--------|---------|
| `.` | Current package |
| `..` | Parent package |
| `...` | Grandparent package |

## When to Use Which?

| Style | When to Use |
|-------|------------|
| Absolute | Default choice — always works |
| Relative | Inside large packages, for sibling modules |

> **Note:** Relative imports only work inside packages, not in scripts run directly.

## Key Points

- Absolute imports use the full dotted path — always preferred
- Relative imports use dots (`.`, `..`) for nearby modules
- Relative imports only work inside packages
- PEP 8 recommends absolute imports for clarity
