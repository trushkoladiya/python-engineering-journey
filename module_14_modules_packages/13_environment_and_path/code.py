# ============================================
# MODULE 14 - SUBTOPIC 13: Environment & Path Handling
# ============================================

# sys.path controls where Python looks for modules.
# Understanding it helps you debug import errors.

import sys
import os
import tempfile

# =============================
# 1. sys.path — THE SEARCH PATH
# =============================

print("=== sys.path — Module Search Path ===")
print()

print(f"  Python searches {len(sys.path)} directories for modules:")
print()

for i, path in enumerate(sys.path):
    # Shorten long paths for readability
    display = path if len(path) < 60 else "..." + path[-57:]
    print(f"  [{i:2d}] {display}")
print()

# =============================
# 2. SEARCH ORDER
# =============================

print("=== Search Order ===")
print()

print("  When you write 'import mymodule', Python searches:")
print()
print("  1. sys.modules (cache — already imported?)")
print("  2. Current directory / script directory")
print("  3. PYTHONPATH environment variable directories")
print("  4. Standard library directories")
print("  5. site-packages (pip-installed packages)")
print()

# =============================
# 3. FIRST ENTRY: CURRENT DIRECTORY
# =============================

print("=== Current Directory in Path ===")
print()

# The first entry is usually '' (empty string = current directory)
# or the script's directory
print(f"  sys.path[0] = '{sys.path[0]}'")
print(f"  Current working directory: {os.getcwd()}")
print()

# This is WHY you can import modules from the same folder!

# =============================
# 4. ADDING TO sys.path
# =============================

print("=== Adding to sys.path ===")
print()

# Create a module in a separate directory
custom_dir = tempfile.mkdtemp()
module_path = os.path.join(custom_dir, "secret_tools.py")

with open(module_path, "w") as f:
    f.write('''
def secret_function():
    return "You found the secret module!"

SECRET_VALUE = 42
''')

# Try importing BEFORE adding to path
print("  Before adding to path:")
try:
    import secret_tools
    print("    ✅ Found!")
except ImportError:
    print("    ❌ ImportError: module not found")
print()

# Add the directory to path
sys.path.insert(0, custom_dir)
print(f"  Added '{custom_dir}' to sys.path")
print()

# Try importing AFTER adding to path
print("  After adding to path:")
import secret_tools
print(f"    ✅ secret_tools.secret_function() = '{secret_tools.secret_function()}'")
print(f"    ✅ secret_tools.SECRET_VALUE = {secret_tools.SECRET_VALUE}")
print()

# Cleanup
sys.path.remove(custom_dir)
del sys.modules["secret_tools"]

# =============================
# 5. WHERE BUILT-IN MODULES LIVE
# =============================

print("=== Where Modules Live ===")
print()

# Check the location of some modules
modules_to_locate = ["math", "os", "json", "random", "sys"]

for mod_name in modules_to_locate:
    mod = sys.modules.get(mod_name)
    if mod is None:
        __import__(mod_name)
        mod = sys.modules[mod_name]

    if hasattr(mod, "__file__") and mod.__file__:
        # Show just the filename
        print(f"  {mod_name:8s} → {mod.__file__}")
    else:
        print(f"  {mod_name:8s} → (built-in, no file)")
print()

# =============================
# 6. PYTHONPATH ENVIRONMENT VARIABLE
# =============================

print("=== PYTHONPATH Environment Variable ===")
print()

pythonpath = os.environ.get("PYTHONPATH", "")
if pythonpath:
    print(f"  PYTHONPATH = '{pythonpath}'")
    for p in pythonpath.split(os.pathsep):
        print(f"    → {p}")
else:
    print("  PYTHONPATH is not set (that's normal)")
print()

print("  To set PYTHONPATH (in terminal):")
print("    export PYTHONPATH=/my/modules:/more/modules")
print("  These directories are added to sys.path automatically")
print()

# =============================
# 7. DEBUGGING ImportError
# =============================

print("=== Debugging ImportError ===")
print()

print("  When you get 'ModuleNotFoundError', check:")
print()
print("  1. Is the module installed?")
print("     → pip install module_name")
print()
print("  2. Is the file in the right directory?")
print("     → Check sys.path to see where Python looks")
print()
print("  3. Is there a naming conflict?")
print("     → Don't name your files 'math.py', 'random.py', etc.!")
print()
print("  4. Is __init__.py present (for packages)?")
print("     → Required to make a folder a package")
print()

# --- Example: Name conflict danger ---
print("  ⚠️ NAME CONFLICT EXAMPLE:")
print("    If you create 'random.py' in your project,")
print("    'import random' will import YOUR file, not Python's!")
print("    → NEVER name your files after standard library modules!")
print()

# =============================
# 8. site-packages LOCATION
# =============================

print("=== site-packages (pip packages) ===")
print()

import site

# Where pip installs packages
site_packages = site.getsitepackages()
print("  pip installs packages to:")
for sp in site_packages:
    print(f"    {sp}")
print()

# User-specific packages
user_site = site.getusersitepackages()
print(f"  User packages: {user_site}")
print()

# Cleanup
import shutil
shutil.rmtree(custom_dir)

# ============================================
# TRY IT YOURSELF:
# 1. Print all entries in sys.path
# 2. Find where the 'json' module file is located
# 3. Create a module in a different folder and add its path
# 4. Check if PYTHONPATH is set in your environment
# ============================================
