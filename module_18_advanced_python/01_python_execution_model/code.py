# ============================================
# MODULE 18 - SUBTOPIC 1: Python Execution Model
# ============================================

# Python runs your code in 3 steps:
# 1. Read source code (.py)
# 2. Compile to bytecode (.pyc)
# 3. Execute bytecode in the PVM

import dis
import sys

# =============================
# 1. CHECKING YOUR PYTHON VERSION
# =============================

print("=== Python Execution Info ===")
print()

print(f"  Python version: {sys.version}")
print(f"  Implementation: {sys.implementation.name}")
print(f"  Platform: {sys.platform}")
print()

# =============================
# 2. SEEING BYTECODE WITH dis
# =============================

print("=== Bytecode: Simple Assignment ===")
print()

def simple_add(a, b):
    result = a + b
    return result

# dis.dis() shows the bytecode instructions
print("  Bytecode for simple_add(a, b):")
dis.dis(simple_add)
print()

# Each line shows:
# - Line number in source
# - Instruction offset
# - Operation name (LOAD_FAST, BINARY_ADD, etc.)
# - Arguments

# =============================
# 3. BYTECODE FOR DIFFERENT OPERATIONS
# =============================

print("=== Bytecode: If Statement ===")
print()

def check_positive(n):
    if n > 0:
        return "positive"
    return "not positive"

print("  Bytecode for check_positive(n):")
dis.dis(check_positive)
print()

# Notice: Python uses COMPARE_OP and jump instructions
# The PVM reads these one by one

# =============================
# 4. BYTECODE FOR A LOOP
# =============================

print("=== Bytecode: Loop ===")
print()

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("  Bytecode for sum_list(numbers):")
dis.dis(sum_list)
print()

# Loops in bytecode use GET_ITER, FOR_ITER, JUMP instructions
# The PVM handles iteration at the bytecode level

# =============================
# 5. COMPILE() FUNCTION
# =============================

print("=== Using compile() ===")
print()

# Python's compile() creates a code object from source
source_code = "x = 10 + 20"
code_object = compile(source_code, "<string>", "exec")

print(f"  Source: {source_code}")
print(f"  Code object: {code_object}")
print(f"  Code type: {type(code_object)}")
print()

# You can execute the code object
namespace = {}
exec(code_object, namespace)
print(f"  After exec: x = {namespace['x']}")
print()

# =============================
# 6. INSPECTING CODE OBJECTS
# =============================

print("=== Code Object Details ===")
print()

def multiply(a, b):
    return a * b

code = multiply.__code__

print(f"  Function: multiply")
print(f"  Argument count: {code.co_argcount}")
print(f"  Variable names: {code.co_varnames}")
print(f"  Constants: {code.co_consts}")
print(f"  Filename: {code.co_filename}")
print(f"  First line number: {code.co_firstlineno}")
print()

# Every function carries a __code__ object
# The PVM uses this object to execute the function

# =============================
# 7. __pycache__ AND .pyc FILES
# =============================

print("=== Understanding __pycache__ ===")
print()

import os

# When you import a module, Python creates __pycache__/
# with .pyc files containing compiled bytecode

# Check if __pycache__ exists in common locations
script_dir = os.path.dirname(os.path.abspath(__file__))
cache_dir = os.path.join(script_dir, "__pycache__")

print(f"  Script directory: {script_dir}")
print(f"  __pycache__ exists: {os.path.exists(cache_dir)}")

if os.path.exists(cache_dir):
    cached_files = os.listdir(cache_dir)
    for f in cached_files[:5]:  # Show first 5
        print(f"    {f}")
print()

# Key facts about .pyc files:
# - Created automatically when you import a module
# - Stored in __pycache__/ with Python version in filename
# - Example: module.cpython-312.pyc
# - Python checks if .py is newer than .pyc before re-compiling

# =============================
# 8. EVAL vs EXEC
# =============================

print("=== eval() vs exec() ===")
print()

# eval() — evaluates an EXPRESSION, returns a value
result = eval("3 * 7 + 2")
print(f"  eval('3 * 7 + 2') = {result}")

# exec() — executes a STATEMENT, returns None
exec_ns = {}
exec("greeting = 'Hello from exec'", exec_ns)
print(f"  exec result: greeting = {exec_ns['greeting']}")
print()

# Both go through: source → compile → execute
# eval is for expressions (returns value)
# exec is for statements (no return value)

# =============================
# 9. THE EXECUTION FLOW VISUALIZED
# =============================

print("=== Execution Flow ===")
print()

print("  Step 1: You write  →  my_script.py")
print("  Step 2: Python     →  Compiles to bytecode")
print("  Step 3: PVM        →  Reads bytecode instructions")
print("  Step 4: PVM        →  Executes each instruction")
print("  Step 5: Output     →  Results appear on screen")
print()

# This is why Python is called "interpreted":
# - The PVM interprets bytecode line by line
# - No separate compilation step needed
# - But internally, compilation DOES happen (to bytecode)

# =============================
# 10. PRACTICAL: COMPARING BYTECODE
# =============================

print("=== Comparing Bytecode: Two Ways to Do the Same Thing ===")
print()

# Method 1: Using + operator
def concat_plus(a, b):
    return a + b

# Method 2: Using f-string
def concat_fstring(a, b):
    return f"{a}{b}"

print("  concat_plus bytecode:")
dis.dis(concat_plus)
print()

print("  concat_fstring bytecode:")
dis.dis(concat_fstring)
print()

# Both do string concatenation, but generate different bytecode
# The PVM executes different instructions for each

# ============================================
# TRY IT YOURSELF:
# 1. Use dis.dis() on a function with a while loop
# 2. Compare bytecode for list comprehension vs for loop
# 3. Inspect the __code__ object of your own function
# ============================================
