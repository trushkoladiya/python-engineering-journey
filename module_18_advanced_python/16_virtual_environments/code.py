# ============================================
# MODULE 18 - SUBTOPIC 16: Virtual Environments & Dependencies
# ============================================

# This file demonstrates the CONCEPTS of virtual environments
# and dependency management. The actual venv commands are run
# in the terminal, but we can explore the tools programmatically.

import sys
import os
import subprocess
import venv
import sysconfig

# =============================
# 1. CURRENT PYTHON ENVIRONMENT
# =============================

print("=== Current Python Environment ===")
print()

print(f"  Python executable: {sys.executable}")
print(f"  Python version: {sys.version}")
print(f"  Platform: {sys.platform}")
print(f"  Prefix: {sys.prefix}")
print(f"  Exec prefix: {sys.exec_prefix}")
print()

# =============================
# 2. CHECK IF IN A VIRTUAL ENVIRONMENT
# =============================

print("=== Virtual Environment Check ===")
print()

in_venv = sys.prefix != sys.base_prefix

print(f"  sys.prefix: {sys.prefix}")
print(f"  sys.base_prefix: {sys.base_prefix}")
print(f"  In virtual environment: {in_venv}")
print()

# When in a venv, sys.prefix points to the venv directory
# When NOT in a venv, sys.prefix == sys.base_prefix

# =============================
# 3. WHERE PACKAGES ARE INSTALLED
# =============================

print("=== Package Installation Paths ===")
print()

paths = sysconfig.get_paths()
print(f"  Site packages: {paths.get('purelib', 'N/A')}")
print(f"  Scripts: {paths.get('scripts', 'N/A')}")
print(f"  Headers: {paths.get('include', 'N/A')}")
print()

# =============================
# 4. LISTING INSTALLED PACKAGES
# =============================

print("=== Installed Packages (via importlib) ===")
print()

try:
    from importlib.metadata import distributions

    packages = sorted(
        [(d.metadata['Name'], d.metadata['Version'])
         for d in distributions()],
        key=lambda x: x[0].lower()
    )

    # Show first 15 packages
    for name, version in packages[:15]:
        print(f"  {name:30s} {version}")

    if len(packages) > 15:
        print(f"  ... and {len(packages) - 15} more packages")
    print(f"\n  Total packages: {len(packages)}")
except ImportError:
    print("  (importlib.metadata not available)")
print()

# =============================
# 5. CREATING A VENV PROGRAMMATICALLY
# =============================

print("=== Creating a venv Programmatically ===")
print()

script_dir = os.path.dirname(os.path.abspath(__file__))
test_venv_dir = os.path.join(script_dir, "_test_venv")

# Create a minimal venv (for demonstration)
print(f"  Creating test venv at: {os.path.basename(test_venv_dir)}")
builder = venv.EnvBuilder(
    system_site_packages=False,
    with_pip=False,  # Skip pip for speed
    clear=True
)
builder.create(test_venv_dir)

# Show the venv structure
print(f"  Venv created! Contents:")
for item in sorted(os.listdir(test_venv_dir)):
    item_path = os.path.join(test_venv_dir, item)
    item_type = "dir" if os.path.isdir(item_path) else "file"
    print(f"    {item} ({item_type})")
print()

# Show the pyvenv.cfg
cfg_file = os.path.join(test_venv_dir, "pyvenv.cfg")
if os.path.exists(cfg_file):
    print("  pyvenv.cfg contents:")
    with open(cfg_file) as f:
        for line in f:
            print(f"    {line.strip()}")
print()

# Clean up test venv
import shutil
shutil.rmtree(test_venv_dir)
print(f"  Cleaned up test venv")
print()

# =============================
# 6. REQUIREMENTS.TXT FORMAT
# =============================

print("=== requirements.txt Format ===")
print()

requirements_example = """# Exact version
requests==2.31.0

# Minimum version
numpy>=1.24.0

# Compatible release (2.0.x but not 3.0)
flask~=2.0.0

# Version range
pandas>=1.5.0,<3.0.0

# Any version
beautifulsoup4

# From a git repository
# git+https://github.com/user/repo.git@main
"""

print("  Example requirements.txt:")
for line in requirements_example.strip().split('\n'):
    print(f"    {line}")
print()

# =============================
# 7. PARSING REQUIREMENTS
# =============================

print("=== Parsing Requirements ===")
print()

def parse_requirements(text):
    """Parse a requirements.txt format string."""
    requirements = []
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        requirements.append(line)
    return requirements

sample_req = """
requests==2.31.0
flask>=3.0.0
numpy~=1.24.0
pytest>=7.0
black==23.7.0
"""

parsed = parse_requirements(sample_req)
print("  Parsed requirements:")
for req in parsed:
    print(f"    {req}")
print()

# =============================
# 8. UNDERSTANDING sys.path
# =============================

print("=== sys.path — Where Python Finds Packages ===")
print()

for i, path in enumerate(sys.path[:8]):
    print(f"  [{i}] {path}")
if len(sys.path) > 8:
    print(f"  ... and {len(sys.path) - 8} more paths")
print()

# When you activate a venv, the venv's site-packages
# is added to sys.path, and the global site-packages is removed

# =============================
# 9. VENV WORKFLOW SUMMARY
# =============================

print("=== Virtual Environment Workflow ===")
print()

workflow = [
    ("1. Create project directory", "mkdir my_project && cd my_project"),
    ("2. Create virtual environment", "python3 -m venv venv"),
    ("3. Activate it", "source venv/bin/activate"),
    ("4. Install packages", "pip install requests flask"),
    ("5. Save dependencies", "pip freeze > requirements.txt"),
    ("6. Add venv/ to .gitignore", "echo 'venv/' >> .gitignore"),
    ("7. Work on your project", "python main.py"),
    ("8. Deactivate when done", "deactivate"),
]

for step, command in workflow:
    print(f"  {step}")
    print(f"    $ {command}")
    print()

# =============================
# 10. BEST PRACTICES
# =============================

print("=== Best Practices ===")
print()

practices = [
    "Always use a virtual environment for each project",
    "Never install project packages globally",
    "Keep requirements.txt updated with pip freeze",
    "Add venv/ to .gitignore (don't commit it)",
    "Use descriptive venv names if you have multiple",
    "Pin exact versions for production (==)",
    "Use minimum versions for libraries (>=)",
    "Document Python version requirements in README",
]

for i, practice in enumerate(practices, 1):
    print(f"  {i}. {practice}")
print()

# ============================================
# TRY IT YOURSELF (in terminal):
# 1. Create a virtual environment:
#      python3 -m venv my_env
# 2. Activate it:
#      source my_env/bin/activate
# 3. Install a package:
#      pip install requests
# 4. Check installed packages:
#      pip list
# 5. Save requirements:
#      pip freeze > requirements.txt
# 6. Deactivate:
#      deactivate
# ============================================
