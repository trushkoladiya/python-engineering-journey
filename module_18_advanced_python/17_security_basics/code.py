# ============================================
# MODULE 18 - SUBTOPIC 17: Security Basics
# ============================================

# Safe coding practices to avoid common vulnerabilities.

import os
import json
import hashlib
import secrets
import html
import re

# =============================
# 1. INPUT VALIDATION
# =============================

print("=== Input Validation ===")
print()

def validate_username(username):
    """Validate a username — only alphanumeric and underscores."""
    if not isinstance(username, str):
        return False, "Username must be a string"
    if len(username) < 3 or len(username) > 20:
        return False, "Username must be 3-20 characters"
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain letters, numbers, underscores"
    return True, "Valid"

test_usernames = [
    "trush_123",          # Valid
    "ab",                 # Too short
    "a" * 25,             # Too long
    "user<script>",       # Contains special chars
    "normal_user",        # Valid
    "",                   # Empty
]

for uname in test_usernames:
    valid, msg = validate_username(uname)
    status = "✓" if valid else "✗"
    display = uname[:20] + "..." if len(uname) > 20 else uname
    print(f"  {status} '{display}' → {msg}")
print()

# =============================
# 2. TYPE VALIDATION
# =============================

print("=== Type Validation ===")
print()

def validate_age(value):
    """Validate age is a reasonable integer."""
    if not isinstance(value, int):
        raise TypeError(f"Age must be int, got {type(value).__name__}")
    if not 0 <= value <= 150:
        raise ValueError(f"Age must be 0-150, got {value}")
    return value

test_ages = [25, -5, 200, "thirty", 0, 150, 3.14]

for age in test_ages:
    try:
        result = validate_age(age)
        print(f"  ✓ {age!r:10s} → valid ({result})")
    except (TypeError, ValueError) as e:
        print(f"  ✗ {age!r:10s} → {e}")
print()

# =============================
# 3. DANGERS OF eval() AND exec()
# =============================

print("=== Dangers of eval() and exec() ===")
print()

# NEVER DO THIS with user input:
# eval(user_input)     # User could execute ANY Python code
# exec(user_input)     # Same danger

# Safe alternative: restrict eval
def safe_math_eval(expression):
    """Evaluate only simple math expressions."""
    # Only allow digits, operators, and spaces
    allowed = set("0123456789+-*/.() ")
    if not all(c in allowed for c in expression):
        raise ValueError(f"Invalid characters in expression")
    
    # Additional check — no double underscores (blocks __import__, etc.)
    if "__" in expression:
        raise ValueError("Dangerous pattern detected")
    
    return eval(expression, {"__builtins__": {}})

safe_expressions = ["2 + 3", "10 * (5 + 2)", "100 / 4"]
dangerous_expressions = [
    "__import__('os').system('echo hacked')",
    "open('/etc/passwd').read()",
]

print("  Safe expressions:")
for expr in safe_expressions:
    try:
        result = safe_math_eval(expr)
        print(f"    '{expr}' = {result}")
    except ValueError as e:
        print(f"    '{expr}' → BLOCKED: {e}")

print()
print("  Dangerous expressions (blocked):")
for expr in dangerous_expressions:
    try:
        result = safe_math_eval(expr)
        print(f"    '{expr}' = {result}")
    except ValueError as e:
        print(f"    '{expr[:40]}...' → BLOCKED: {e}")
print()

# =============================
# 4. PATH TRAVERSAL PREVENTION
# =============================

print("=== Path Traversal Prevention ===")
print()

BASE_DIR = "/data/uploads"

def safe_file_path(base_dir, filename):
    """Ensure file path stays within base directory."""
    # Resolve to absolute path
    requested = os.path.realpath(os.path.join(base_dir, filename))
    base = os.path.realpath(base_dir)
    
    # Check that resolved path starts with base directory
    if not requested.startswith(base + os.sep) and requested != base:
        raise ValueError(f"Path traversal attempt: {filename}")
    
    return requested

test_paths = [
    "document.txt",              # Safe
    "subdir/file.txt",           # Safe
    "../../etc/passwd",          # ATTACK!
    "../../../root/.ssh/id_rsa", # ATTACK!
    "normal_file.pdf",           # Safe
]

for path in test_paths:
    try:
        safe = safe_file_path(BASE_DIR, path)
        print(f"  ✓ '{path}' → {safe}")
    except ValueError as e:
        print(f"  ✗ '{path}' → BLOCKED: {e}")
print()

# =============================
# 5. HTML ESCAPING (XSS Prevention)
# =============================

print("=== HTML Escaping ===")
print()

# User input in HTML without escaping = XSS vulnerability
user_inputs = [
    "Hello World",
    "<script>alert('hacked')</script>",
    "Name: <b>Bold</b>",
    'Image: <img src="x" onerror="alert(1)">',
]

for text in user_inputs:
    escaped = html.escape(text)
    print(f"  Input:   {text}")
    print(f"  Escaped: {escaped}")
    print()

# =============================
# 6. PASSWORD HASHING
# =============================

print("=== Password Hashing ===")
print()

# NEVER store passwords in plain text!
# Use a hash function with salt

def hash_password(password, salt=None):
    """Hash a password with a random salt."""
    if salt is None:
        salt = secrets.token_hex(16)
    salted = salt + password
    hashed = hashlib.sha256(salted.encode()).hexdigest()
    return salt, hashed

def verify_password(password, salt, stored_hash):
    """Verify a password against its hash."""
    _, computed_hash = hash_password(password, salt)
    return secrets.compare_digest(computed_hash, stored_hash)

# Hash a password
password = "my_secret_password"
salt, password_hash = hash_password(password)

print(f"  Password: {'*' * len(password)}")
print(f"  Salt: {salt}")
print(f"  Hash: {password_hash}")
print()

# Verify correct password
correct = verify_password("my_secret_password", salt, password_hash)
print(f"  Correct password: {correct}")

# Verify wrong password
wrong = verify_password("wrong_password", salt, password_hash)
print(f"  Wrong password: {wrong}")
print()

# =============================
# 7. SECRETS MODULE — SECURE RANDOM
# =============================

print("=== Secure Random with secrets ===")
print()

# DON'T use random module for security! Use secrets.

# Generate secure tokens
token = secrets.token_hex(16)
print(f"  Hex token: {token}")

url_token = secrets.token_urlsafe(16)
print(f"  URL-safe token: {url_token}")

# Generate secure random number
secure_num = secrets.randbelow(1000)
print(f"  Random number (0-999): {secure_num}")

# Generate a secure password
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
password = ''.join(secrets.choice(alphabet) for _ in range(16))
print(f"  Generated password: {password}")
print()

# =============================
# 8. SAFE FILE OPERATIONS
# =============================

print("=== Safe File Operations ===")
print()

def safe_read_file(filepath, allowed_extensions=None):
    """Read a file with safety checks."""
    # Check extension
    if allowed_extensions:
        ext = os.path.splitext(filepath)[1].lower()
        if ext not in allowed_extensions:
            raise ValueError(f"File type '{ext}' not allowed")
    
    # Check file exists
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Check file size (prevent reading huge files)
    max_size = 10 * 1024 * 1024  # 10 MB
    size = os.path.getsize(filepath)
    if size > max_size:
        raise ValueError(f"File too large: {size} bytes (max {max_size})")
    
    with open(filepath, 'r') as f:
        return f.read()

print("  Safe file reading with:")
print("    ✓ Extension whitelist")
print("    ✓ File existence check")
print("    ✓ File size limit")
print()

# =============================
# 9. ENVIRONMENT VARIABLES FOR SECRETS
# =============================

print("=== Environment Variables for Secrets ===")
print()

# NEVER hardcode secrets in your code!
# Use environment variables instead.

# Bad:
# API_KEY = "sk-1234567890abcdef"  # NEVER DO THIS!

# Good:
api_key = os.environ.get("API_KEY", "not-set")
db_password = os.environ.get("DB_PASSWORD", "not-set")

print(f"  API_KEY: {'set' if api_key != 'not-set' else 'not-set'}")
print(f"  DB_PASSWORD: {'set' if db_password != 'not-set' else 'not-set'}")
print()
print("  To set: export API_KEY='your-key-here'")
print()

# =============================
# 10. SECURITY CHECKLIST
# =============================

print("=== Security Checklist ===")
print()

checklist = [
    "Validate ALL user input (type, range, format)",
    "Never use eval()/exec() with untrusted data",
    "Never unpickle untrusted data — use JSON",
    "Escape HTML output to prevent XSS",
    "Hash passwords — never store plain text",
    "Use secrets module for cryptographic randomness",
    "Check file paths to prevent directory traversal",
    "Store secrets in environment variables, not code",
    "Limit file sizes when reading user uploads",
    "Use HTTPS for network communication",
]

for i, item in enumerate(checklist, 1):
    print(f"  {i:2d}. {item}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a function that validates an email address
# 2. Create a secure password generator with
#    configurable length and character types
# 3. Build a simple "user registration" system that
#    hashes passwords and validates usernames
# ============================================
