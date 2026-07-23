# ============================================
# MODULE 14 - SUBTOPIC 8: Importing from Packages
# ============================================

# Two import styles: absolute and relative.
# This demo creates real packages to show both.

import os
import sys
import tempfile
import shutil

# =============================
# 1. SETUP: CREATE A PACKAGE
# =============================

print("=== Setting Up Demo Package ===")
print()

base_dir = tempfile.mkdtemp()

# Create package: myproject/
project_dir = os.path.join(base_dir, "myproject")
os.makedirs(project_dir)

# Create sub-packages
utils_dir = os.path.join(project_dir, "utils")
models_dir = os.path.join(project_dir, "models")
os.makedirs(utils_dir)
os.makedirs(models_dir)

# __init__.py files
for d in [project_dir, utils_dir, models_dir]:
    with open(os.path.join(d, "__init__.py"), "w") as f:
        f.write("")

# myproject/utils/helpers.py
with open(os.path.join(utils_dir, "helpers.py"), "w") as f:
    f.write('''
def format_name(first, last):
    return f"{first.title()} {last.title()}"

def format_phone(number):
    return f"({number[:3]}) {number[3:6]}-{number[6:]}"
''')

# myproject/utils/validators.py
with open(os.path.join(utils_dir, "validators.py"), "w") as f:
    f.write('''
def is_valid_email(email):
    return "@" in email and "." in email

def is_valid_age(age):
    return 0 <= age <= 150
''')

# myproject/models/user.py
with open(os.path.join(models_dir, "user.py"), "w") as f:
    f.write('''
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"User({self.name}, {self.email})"
''')

# myproject/models/product.py
with open(os.path.join(models_dir, "product.py"), "w") as f:
    f.write('''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product({self.name}, ${self.price:.2f})"
''')

# Show structure
print("  Package structure:")
print("    myproject/")
print("    ├── __init__.py")
print("    ├── utils/")
print("    │   ├── __init__.py")
print("    │   ├── helpers.py")
print("    │   └── validators.py")
print("    └── models/")
print("        ├── __init__.py")
print("        ├── user.py")
print("        └── product.py")
print()

# Add to path
sys.path.insert(0, base_dir)

# =============================
# 2. ABSOLUTE IMPORTS
# =============================

print("=== Absolute Imports ===")
print()

# Full path from project root
import myproject.utils.helpers
result = myproject.utils.helpers.format_name("john", "doe")
print(f"  import myproject.utils.helpers")
print(f"  format_name('john', 'doe') = '{result}'")
print()

# Import specific module
from myproject.utils import validators
print(f"  from myproject.utils import validators")
print(f"  is_valid_email('test@mail.com') = {validators.is_valid_email('test@mail.com')}")
print(f"  is_valid_email('invalid') = {validators.is_valid_email('invalid')}")
print()

# Import specific class
from myproject.models.user import User
u = User("Trush", "trush@example.com")
print(f"  from myproject.models.user import User")
print(f"  User('Trush', 'trush@example.com') = {u}")
print()

# Import specific function
from myproject.utils.helpers import format_phone
print(f"  from myproject.utils.helpers import format_phone")
print(f"  format_phone('5551234567') = '{format_phone('5551234567')}'")
print()

# =============================
# 3. RELATIVE IMPORTS (CONCEPT)
# =============================

print("=== Relative Imports (Concept) ===")
print()

# Relative imports use dots:
#   from . import module        ← same package
#   from .module import name    ← name from same package
#   from .. import module       ← parent package
#   from ..sub import module    ← sibling package

# Example: Inside myproject/utils/helpers.py, you could write:
#   from . import validators          ← same folder (utils/)
#   from .validators import is_valid  ← specific function
#   from ..models import user         ← sibling package (models/)

print("  Relative imports use dots:")
print("    .   = current package")
print("    ..  = parent package")
print("    ... = grandparent package")
print()
print("  Example (inside myproject/utils/helpers.py):")
print("    from . import validators        ← same package")
print("    from ..models import user       ← sibling package")
print()

# =============================
# 4. RELATIVE IMPORTS (LIVE DEMO)
# =============================

print("=== Relative Imports (Live Demo) ===")
print()

# Update helpers.py to use relative imports
with open(os.path.join(utils_dir, "helpers.py"), "w") as f:
    f.write('''
# Using relative import: import from same package
from . import validators

def format_name(first, last):
    return f"{first.title()} {last.title()}"

def format_phone(number):
    return f"({number[:3]}) {number[3:6]}-{number[6:]}"

def create_validated_name(first, last, age):
    """Uses validators from same package via relative import."""
    if validators.is_valid_age(age):
        return f"{format_name(first, last)} (age: {age})"
    return f"Invalid age: {age}"
''')

# Reload to pick up changes
import importlib
import myproject.utils.helpers
importlib.reload(myproject.utils.helpers)

from myproject.utils.helpers import create_validated_name
print(f"  create_validated_name('trush', 'smith', 21):")
print(f"    = '{create_validated_name('trush', 'smith', 21)}'")
print(f"  create_validated_name('trush', 'smith', 200):")
print(f"    = '{create_validated_name('trush', 'smith', 200)}'")
print()

# =============================
# 5. ABSOLUTE vs RELATIVE
# =============================

print("=== Absolute vs Relative ===")
print()

print("  Absolute imports:")
print("    ✅ Clear — full path visible")
print("    ✅ Always work")
print("    ✅ PEP 8 recommended")
print()
print("  Relative imports:")
print("    ✅ Shorter for sibling modules")
print("    ❌ Only work inside packages")
print("    ❌ Can be confusing in deep nesting")
print()

# =============================
# 6. MULTIPLE IMPORT STYLES
# =============================

print("=== Multiple Styles Side-by-Side ===")
print()

# All of these access the same User class:
from myproject.models.user import User as User1      # absolute, specific
from myproject.models import user as user_module      # absolute, module
import myproject.models.user                          # absolute, full

u1 = User1("Method1", "a@b.com")
u2 = user_module.User("Method2", "c@d.com")
u3 = myproject.models.user.User("Method3", "e@f.com")

print(f"  from myproject.models.user import User → {u1}")
print(f"  from myproject.models import user      → {u2}")
print(f"  import myproject.models.user           → {u3}")
print()

# Cleanup
sys.path.remove(base_dir)
shutil.rmtree(base_dir)

# ============================================
# TRY IT YOURSELF:
# 1. Create a package with two sub-packages
# 2. Import modules using absolute imports
# 3. Add relative imports between sibling modules
# ============================================
