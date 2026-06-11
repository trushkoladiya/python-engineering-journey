# ============================================
# MODULE 14 - SUBTOPIC 7: Packages Basics
# ============================================

# A package is a folder containing modules.
# This example creates real packages to demonstrate.

import os
import sys
import tempfile

# =============================
# 1. WHAT IS A PACKAGE?
# =============================

print("=== What is a Package? ===")
print()

print("  Module  = a single .py file")
print("  Package = a folder containing .py files")
print("  The folder needs an __init__.py file to be a package")
print()

# =============================
# 2. CREATING A PACKAGE (LIVE DEMO)
# =============================

print("=== Creating a Real Package ===")
print()

# Create a temporary directory for our package
base_dir = tempfile.mkdtemp()
pkg_dir = os.path.join(base_dir, "animals")
os.makedirs(pkg_dir)

# Create __init__.py (makes it a package)
with open(os.path.join(pkg_dir, "__init__.py"), "w") as f:
    f.write('"""Animals package."""\n')

# Create module: dogs.py
with open(os.path.join(pkg_dir, "dogs.py"), "w") as f:
    f.write('''
def bark():
    return "Woof! Woof!"

def fetch(item):
    return f"Dog fetched the {item}!"

BREEDS = ["Labrador", "Poodle", "Bulldog", "Beagle"]
''')

# Create module: cats.py
with open(os.path.join(pkg_dir, "cats.py"), "w") as f:
    f.write('''
def meow():
    return "Meow!"

def purr():
    return "Purrrrr..."

BREEDS = ["Persian", "Siamese", "Maine Coon", "Bengal"]
''')

# Show the structure
print("  Package structure:")
print(f"    {pkg_dir}/")
print(f"      __init__.py")
print(f"      dogs.py")
print(f"      cats.py")
print()

# Add to path and import
sys.path.insert(0, base_dir)

# =============================
# 3. IMPORTING FROM A PACKAGE
# =============================

print("=== Importing from a Package ===")
print()

# Way 1: import package.module
import animals.dogs

print(f"  animals.dogs.bark() = '{animals.dogs.bark()}'")
print(f"  animals.dogs.fetch('ball') = '{animals.dogs.fetch('ball')}'")
print(f"  animals.dogs.BREEDS = {animals.dogs.BREEDS}")
print()

# Way 2: from package import module
from animals import cats

print(f"  cats.meow() = '{cats.meow()}'")
print(f"  cats.purr() = '{cats.purr()}'")
print(f"  cats.BREEDS = {cats.BREEDS}")
print()

# Way 3: from package.module import name
from animals.dogs import bark, BREEDS

print(f"  bark() = '{bark()}'")
print(f"  BREEDS = {BREEDS}")
print()

# =============================
# 4. NESTED PACKAGES (SUB-PACKAGES)
# =============================

print("=== Nested Packages ===")
print()

# Create a sub-package
exotic_dir = os.path.join(pkg_dir, "exotic")
os.makedirs(exotic_dir)

with open(os.path.join(exotic_dir, "__init__.py"), "w") as f:
    f.write('"""Exotic animals sub-package."""\n')

with open(os.path.join(exotic_dir, "reptiles.py"), "w") as f:
    f.write('''
def hiss():
    return "Ssssss!"

TYPES = ["Snake", "Lizard", "Turtle", "Gecko"]
''')

print("  Nested structure:")
print(f"    animals/")
print(f"      __init__.py")
print(f"      dogs.py")
print(f"      cats.py")
print(f"      exotic/")
print(f"        __init__.py")
print(f"        reptiles.py")
print()

# Import from nested package
from animals.exotic import reptiles

print(f"  reptiles.hiss() = '{reptiles.hiss()}'")
print(f"  reptiles.TYPES = {reptiles.TYPES}")
print()

# =============================
# 5. PACKAGE vs MODULE
# =============================

print("=== Package vs Module ===")
print()

import animals
import animals.dogs

print(f"  type(animals) = {type(animals)}")
print(f"  type(animals.dogs) = {type(animals.dogs)}")
print(f"  animals.__path__ exists? {'Yes — it is a PACKAGE' if hasattr(animals, '__path__') else 'No'}")
print(f"  animals.dogs.__path__ exists? {'Yes' if hasattr(animals.dogs, '__path__') else 'No — it is a MODULE'}")
print()

# Key difference:
# Packages have __path__ (they're directories)
# Modules don't (they're single files)

# =============================
# 6. REAL-WORLD EXAMPLE
# =============================

print("=== Real-World Package Layout ===")
print()

print("  A web application might look like:")
print()
print("    webapp/")
print("    ├── __init__.py")
print("    ├── models/")
print("    │   ├── __init__.py")
print("    │   ├── user.py")
print("    │   └── product.py")
print("    ├── views/")
print("    │   ├── __init__.py")
print("    │   ├── auth.py")
print("    │   └── shop.py")
print("    └── utils/")
print("        ├── __init__.py")
print("        ├── validators.py")
print("        └── formatters.py")
print()
print("  Usage:")
print("    from webapp.models.user import User")
print("    from webapp.views.auth import login")
print("    from webapp.utils.validators import is_valid_email")
print()

# Cleanup
sys.path.remove(base_dir)

import shutil
shutil.rmtree(base_dir)

# ============================================
# TRY IT YOURSELF:
# 1. Create a 'tools/' folder with __init__.py and two modules
# 2. Import functions from your package
# 3. Create a sub-package inside your package
# ============================================
