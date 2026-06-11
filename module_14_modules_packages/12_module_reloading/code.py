# ============================================
# MODULE 14 - SUBTOPIC 12: Module Reloading & Caching
# ============================================

# Python caches modules after first import.
# importlib.reload() forces re-loading.

import sys
import os
import tempfile
import importlib

# =============================
# 1. MODULE CACHING — sys.modules
# =============================

print("=== Module Caching (sys.modules) ===")
print()

# sys.modules is a dictionary of ALL loaded modules
print(f"  Total cached modules: {len(sys.modules)}")
print()

# Check specific modules
check_modules = ["math", "os", "sys", "json", "random"]
for mod_name in check_modules:
    is_cached = mod_name in sys.modules
    print(f"  '{mod_name}' cached? {is_cached}")
print()

# =============================
# 2. IMPORT USES THE CACHE
# =============================

print("=== Import Uses Cache ===")
print()

import math
id_first = id(math)

import math   # second import
id_second = id(math)

print(f"  First import  → id(math) = {id_first}")
print(f"  Second import → id(math) = {id_second}")
print(f"  Same object? {id_first == id_second}")
print("  → Python reuses the cached module!")
print()

# =============================
# 3. PROVING THE CACHE
# =============================

print("=== Proving Module is NOT Re-executed ===")
print()

# Create a module that prints when loaded
base_dir = tempfile.mkdtemp()
module_path = os.path.join(base_dir, "counter_mod.py")

with open(module_path, "w") as f:
    f.write('''
import_count = 0
import_count += 1
print(f"    [counter_mod.py] Module executed! count = {import_count}")
''')

sys.path.insert(0, base_dir)

print("  First import:")
import counter_mod
print(f"  counter_mod.import_count = {counter_mod.import_count}")

print("  Second import:")
import counter_mod   # no output — cached!
print(f"  counter_mod.import_count = {counter_mod.import_count}")
print("  → Module code did NOT run again!")
print()

# =============================
# 4. importlib.reload()
# =============================

print("=== importlib.reload() ===")
print()

# Modify the module file
with open(module_path, "w") as f:
    f.write('''
version = "2.0"
message = "Module has been UPDATED!"
print(f"    [counter_mod.py] Reloaded! version = {version}")
''')

print("  Before reload:")
print(f"    counter_mod has 'version'? {hasattr(counter_mod, 'version')}")

print("  After reload:")
importlib.reload(counter_mod)
print(f"    counter_mod.version = '{counter_mod.version}'")
print(f"    counter_mod.message = '{counter_mod.message}'")
print()

# =============================
# 5. RELOAD WITH CHANGING DATA
# =============================

print("=== Reload with Changing Data ===")
print()

# Simulate a config file that changes
config_path = os.path.join(base_dir, "config_mod.py")

# Version 1
with open(config_path, "w") as f:
    f.write('''
DEBUG = True
DATABASE = "sqlite"
PORT = 8080
''')

import config_mod
print(f"  Config v1: DEBUG={config_mod.DEBUG}, DB={config_mod.DATABASE}, PORT={config_mod.PORT}")

# Version 2 — settings changed
with open(config_path, "w") as f:
    f.write('''
DEBUG = False
DATABASE = "postgresql"
PORT = 5432
''')

# Without reload — still shows old values
import config_mod
print(f"  After re-import (cached): DEBUG={config_mod.DEBUG}, DB={config_mod.DATABASE}")

# With reload — shows new values
importlib.reload(config_mod)
print(f"  After reload (fresh):     DEBUG={config_mod.DEBUG}, DB={config_mod.DATABASE}, PORT={config_mod.PORT}")
print()

# =============================
# 6. CACHE INSPECTION
# =============================

print("=== Inspecting the Module Cache ===")
print()

# Find our custom modules in sys.modules
custom_modules = [
    name for name in sys.modules
    if name in ["counter_mod", "config_mod", "math", "os", "json"]
]

for mod_name in custom_modules:
    mod = sys.modules[mod_name]
    has_file = hasattr(mod, "__file__") and mod.__file__ is not None
    print(f"  {mod_name:15s} → file: {mod.__file__ if has_file else '(built-in)'}")
print()

# =============================
# 7. REMOVING FROM CACHE
# =============================

print("=== Removing a Module from Cache ===")
print()

print(f"  'counter_mod' in sys.modules? {('counter_mod' in sys.modules)}")

# Remove from cache
if "counter_mod" in sys.modules:
    del sys.modules["counter_mod"]
    print("  Removed 'counter_mod' from cache")

print(f"  'counter_mod' in sys.modules? {('counter_mod' in sys.modules)}")
print()

# =============================
# 8. WARNINGS ABOUT RELOAD
# =============================

print("=== Reload Caveats ===")
print()

print("  ⚠️ reload() caveats:")
print("    1. Only works on already-imported modules")
print("    2. Objects created from OLD module stay old")
print("    3. 'from module import name' references are NOT updated")
print("    4. Can cause inconsistent state")
print()
print("  Best practice:")
print("    - Use reload only during development/debugging")
print("    - In production, restart the program instead")
print()

# Cleanup
sys.path.remove(base_dir)
for mod_name in ["counter_mod", "config_mod"]:
    if mod_name in sys.modules:
        del sys.modules[mod_name]

import shutil
shutil.rmtree(base_dir)

# ============================================
# TRY IT YOURSELF:
# 1. Import math, check 'math' in sys.modules
# 2. Count how many modules are cached (len(sys.modules))
# 3. Create a module, import it, change it, reload it
# ============================================
