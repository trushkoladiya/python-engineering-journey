# ============================================
# MODULE 14 - SUBTOPIC 15: Best Practices
# ============================================

# Clean, professional patterns for modules and packages.

# =============================
# 1. IMPORT ORDERING (PEP 8)
# =============================

print("=== Import Ordering (PEP 8) ===")
print()

# PEP 8 specifies this order:
#
# 1. Standard library imports
# 2. Third-party imports (blank line)
# 3. Local imports (blank line)
#
# Example:
#
#   import os
#   import sys
#   import json
#
#   import requests
#   import numpy as np
#
#   from myproject.utils import helpers
#   from myproject.models import User

print("  PEP 8 import order:")
print("    1. Standard library  (os, sys, json)")
print("    2. Third-party       (requests, numpy)")
print("    3. Local             (myproject.utils)")
print("    Separate each group with a blank line")
print()

# =============================
# 2. AVOID WILDCARD IMPORTS
# =============================

print("=== Avoid Wildcard Imports ===")
print()

# BAD: from math import *
# This brings in ALL names — you can't tell what came from where

# GOOD: explicit imports
from math import sqrt, pi, ceil

print(f"  sqrt(16) = {sqrt(16)}")
print(f"  pi = {pi:.6f}")
print(f"  ceil(3.2) = {ceil(3.2)}")
print()

print("  ❌ from math import *    ← hides where names come from")
print("  ✅ from math import sqrt ← clear and explicit")
print("  ✅ import math           ← clearest (uses math.sqrt)")
print()

# =============================
# 3. ONE IMPORT PER LINE
# =============================

print("=== One Import Per Line ===")
print()

# BAD
# import os, sys, json

# GOOD
import os
import sys
import json

print("  ❌ import os, sys, json   ← hard to read, bad diffs")
print("  ✅ import os              ← one per line")
print("     import sys")
print("     import json")
print()

# Exception: multiple names from SAME module is fine
# from math import sqrt, ceil, floor   ← OK

# =============================
# 4. NAMING CONVENTIONS
# =============================

print("=== Module Naming Conventions ===")
print()

print("  File names:")
print("    ✅ my_module.py        ← lowercase, underscores")
print("    ✅ string_helpers.py   ← descriptive")
print("    ✅ validators.py       ← clear purpose")
print("    ❌ MyModule.py         ← no CamelCase for modules")
print("    ❌ string-helpers.py   ← no hyphens (can't import)")
print()

print("  DANGER — never use standard library names:")
print("    ❌ random.py    ← shadows Python's random")
print("    ❌ math.py      ← shadows Python's math")
print("    ❌ os.py        ← shadows Python's os")
print("    ❌ test.py      ← shadows Python's test module")
print()

# =============================
# 5. ALWAYS USE __main__ GUARD
# =============================

print("=== Always Use __main__ Guard ===")
print()

# Every module that has executable code should use this

def calculate_stats(numbers):
    """Calculate basic statistics."""
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return {
        "total": total,
        "count": count,
        "average": round(average, 2),
        "min": min(numbers) if numbers else None,
        "max": max(numbers) if numbers else None,
    }

if __name__ == "__main__":
    # Demo/test code — only runs when executed directly
    data = [23, 45, 12, 67, 34, 89, 56]
    stats = calculate_stats(data)
    print(f"  Data: {data}")
    print(f"  Stats: {stats}")
    print()

# =============================
# 6. DOCSTRINGS FOR MODULES
# =============================

print("=== Module Docstrings ===")
print()

# Every module should have a docstring at the top:
#
#   """
#   User authentication module.
#   
#   Handles login, logout, and session management.
#   """

print("  Every module should start with a docstring:")
print('    """')
print("    Module description.")
print()
print("    Details about what it provides.")
print('    """')
print()

# Check a real module's docstring
print(f"  os module docstring (first line):")
if os.__doc__:
    print(f"    {os.__doc__.split(chr(10))[0]}")
print()

# =============================
# 7. CIRCULAR IMPORT WARNING
# =============================

print("=== Avoiding Circular Imports ===")
print()

# Circular import: A imports B, and B imports A
# This causes errors!

# BAD:
#   # module_a.py
#   from module_b import func_b
#   
#   # module_b.py
#   from module_a import func_a    ← CIRCULAR!

print("  Circular imports happen when:")
print("    module_a imports from module_b")
print("    module_b imports from module_a")
print()
print("  Solutions:")
print("    1. Restructure — move shared code to module_c")
print("    2. Import inside functions (lazy import)")
print("    3. Use import at module level, not from...import")
print()

# Example of lazy import (solution #2):
def process_data(data):
    # Import inside the function — avoids circular import
    import json
    return json.dumps(data)

result = process_data({"key": "value"})
print(f"  Lazy import example: {result}")
print()

# =============================
# 8. COMPLETE BEST PRACTICES CHECKLIST
# =============================

print("=== Best Practices Checklist ===")
print()

checklist = [
    ("Imports at top of file", True),
    ("Group: stdlib → third-party → local", True),
    ("One import per line", True),
    ("No wildcard imports", True),
    ("Lowercase module names", True),
    ("No standard library name conflicts", True),
    ("__main__ guard for scripts", True),
    ("Module docstrings", True),
    ("No circular imports", True),
    ("Small, focused modules", True),
    ("__all__ for public API", True),
    ("Clean, readable structure", True),
]

for item, good in checklist:
    emoji = "✅" if good else "❌"
    print(f"  {emoji} {item}")
print()

# =============================
# 9. PUTTING IT ALL TOGETHER
# =============================

print("=== Example: Well-Structured Module ===")
print()

print('  """')
print("  user_auth.py — User authentication module.")
print()
print("  Provides login, logout, and token management.")
print('  """')
print()
print("  # Standard library")
print("  import hashlib")
print("  import secrets")
print("  from datetime import datetime, timedelta")
print()
print("  # Constants")
print('  TOKEN_EXPIRY_HOURS = 24')
print("  MAX_LOGIN_ATTEMPTS = 5")
print()
print("  # Public API")
print("  __all__ = ['login', 'logout', 'verify_token']")
print()
print("  def login(username, password):")
print('      """Authenticate a user."""')
print("      ...")
print()
print("  def logout(token):")
print('      """Invalidate a session."""')
print("      ...")
print()
print("  def _hash_password(password):")
print('      """Internal helper — not part of public API."""')
print("      ...")
print()
print("  if __name__ == '__main__':")
print("      # Quick test")
print("      print('Auth module loaded successfully')")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Review your old code — fix any import ordering issues
# 2. Add docstrings to your modules
# 3. Check for any standard library naming conflicts
# 4. Add __main__ guards to all your modules
# ============================================
