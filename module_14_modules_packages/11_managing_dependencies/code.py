# ============================================
# MODULE 14 - SUBTOPIC 11: Managing Dependencies
# ============================================

# Beyond the standard library, Python has a huge ecosystem
# of third-party packages. This is an introduction.

import sys
import os

# =============================
# 1. pip — PYTHON'S PACKAGE MANAGER
# =============================

print("=== pip — Package Manager ===")
print()

# pip is the tool for installing external packages
# It comes with Python (Python 3.4+)

print("  Common pip commands (run in terminal, not Python):")
print()
print("    pip install requests       ← install a package")
print("    pip install requests==2.28 ← install specific version")
print("    pip install --upgrade pip  ← upgrade a package")
print("    pip uninstall requests     ← remove a package")
print("    pip list                   ← show installed packages")
print("    pip show requests          ← show package details")
print("    pip freeze                 ← list with versions")
print()

# =============================
# 2. CHECKING INSTALLED PACKAGES
# =============================

print("=== Currently Installed Packages ===")
print()

# We can check what's installed from within Python
import pkg_resources

installed = [(d.project_name, d.version) for d in pkg_resources.working_set]
installed.sort(key=lambda x: x[0].lower())

print(f"  Total packages installed: {len(installed)}")
print(f"  First 10:")
for name, version in installed[:10]:
    print(f"    {name} == {version}")
print()

# =============================
# 3. CHECKING IF A PACKAGE IS AVAILABLE
# =============================

print("=== Checking Package Availability ===")
print()

packages_to_check = [
    "json",       # standard library
    "os",         # standard library
    "requests",   # popular third-party
    "numpy",      # popular third-party
    "flask",      # web framework
    "math",       # standard library
]

for pkg_name in packages_to_check:
    try:
        __import__(pkg_name)
        print(f"  {pkg_name:12s} → ✅ Available")
    except ImportError:
        print(f"  {pkg_name:12s} → ❌ Not installed")
print()

# =============================
# 4. requirements.txt
# =============================

print("=== requirements.txt ===")
print()

# requirements.txt lists all packages a project needs

example_requirements = """# requirements.txt example
# Format: package_name==version

# Web framework
# flask==2.3.0

# HTTP requests
# requests>=2.28.0

# Data processing
# pandas>=1.5.0
# numpy>=1.23.0

# Testing
# pytest>=7.0.0
"""

print("  Example requirements.txt:")
for line in example_requirements.strip().split("\n"):
    print(f"    {line}")
print()

print("  Install all at once:")
print("    pip install -r requirements.txt")
print()

# =============================
# 5. VERSION SPECIFIERS
# =============================

print("=== Version Specifiers ===")
print()

print("  Exact version:    package==1.2.3")
print("  Minimum version:  package>=1.2.0")
print("  Compatible:       package~=1.2.0  (>=1.2.0, <1.3.0)")
print("  Range:            package>=1.0,<2.0")
print("  Any version:      package")
print()

# =============================
# 6. POPULAR THIRD-PARTY PACKAGES
# =============================

print("=== Popular Third-Party Packages ===")
print()

popular_packages = [
    ("requests",     "HTTP requests — talk to web APIs"),
    ("numpy",        "Numerical computing — fast math on arrays"),
    ("pandas",       "Data analysis — work with tables/CSV"),
    ("flask",        "Web framework — build web apps"),
    ("django",       "Web framework — full-featured"),
    ("pytest",       "Testing — write and run tests"),
    ("pillow",       "Image processing — edit images"),
    ("matplotlib",   "Plotting — create charts and graphs"),
    ("sqlalchemy",   "Database — ORM for SQL databases"),
    ("beautifulsoup4", "Web scraping — parse HTML"),
]

for name, description in popular_packages:
    print(f"  {name:18s} → {description}")
print()

# =============================
# 7. SAFE IMPORTING PATTERN
# =============================

print("=== Safe Import Pattern ===")
print()

# When a package might not be installed, use try/except

try:
    import requests
    print("  requests is installed — can make HTTP calls!")
    HAS_REQUESTS = True
except ImportError:
    print("  requests not installed — install with: pip install requests")
    HAS_REQUESTS = False

print(f"  HAS_REQUESTS = {HAS_REQUESTS}")
print()

# This pattern is common in libraries that have optional dependencies

# =============================
# 8. PYTHON VERSION INFO
# =============================

print("=== Your Python Environment ===")
print()

print(f"  Python version: {sys.version}")
print(f"  Python executable: {sys.executable}")
print(f"  Platform: {sys.platform}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Run 'pip list' in your terminal to see installed packages
# 2. Run 'pip show pip' to see pip's own info
# 3. Create a requirements.txt for a small project
# 4. Try 'pip install requests' and then 'import requests'
# ============================================
