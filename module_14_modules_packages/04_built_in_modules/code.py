# ============================================
# MODULE 14 - SUBTOPIC 4: Built-in Modules
# ============================================

# Python includes many useful modules out of the box.
# No installation needed — just import and use.

# =============================
# 1. math MODULE
# =============================

print("=== math Module ===")
print()

import math

print(f"  pi = {math.pi}")
print(f"  e = {math.e}")
print(f"  sqrt(144) = {math.sqrt(144)}")
print(f"  ceil(3.1) = {math.ceil(3.1)}")
print(f"  floor(3.9) = {math.floor(3.9)}")
print(f"  factorial(6) = {math.factorial(6)}")
print(f"  gcd(24, 36) = {math.gcd(24, 36)}")
print(f"  log(100, 10) = {math.log(100, 10)}")
print(f"  pow(2, 10) = {math.pow(2, 10)}")
print()

# =============================
# 2. random MODULE
# =============================

print("=== random Module ===")
print()

import random

print(f"  randint(1, 100) = {random.randint(1, 100)}")
print(f"  random() = {random.random():.4f}")
print(f"  uniform(1.0, 10.0) = {random.uniform(1.0, 10.0):.4f}")

fruits = ["apple", "banana", "cherry", "mango"]
print(f"  choice({fruits}) = {random.choice(fruits)}")
print(f"  sample({fruits}, 2) = {random.sample(fruits, 2)}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"  shuffle([1,2,3,4,5]) = {numbers}")
print()

# =============================
# 3. sys MODULE
# =============================

print("=== sys Module ===")
print()

import sys

print(f"  Python version: {sys.version}")
print(f"  Platform: {sys.platform}")
print(f"  Max integer size: {sys.maxsize}")
print(f"  Recursion limit: {sys.getrecursionlimit()}")
print(f"  Command line args: {sys.argv}")
print(f"  Number of module search paths: {len(sys.path)}")
print()

# =============================
# 4. os MODULE
# =============================

print("=== os Module ===")
print()

import os

print(f"  OS name: {os.name}")
print(f"  Current directory: {os.getcwd()}")
print(f"  Path separator: '{os.sep}'")
print(f"  Line separator repr: {repr(os.linesep)}")

# List first 5 files in current directory
files = os.listdir(".")
print(f"  Files in '.': {files[:5]}{'...' if len(files) > 5 else ''}")
print()

# os.path — file path utilities
print("  os.path utilities:")
test_path = "/home/user/documents/report.txt"
print(f"    basename('{test_path}') = {os.path.basename(test_path)}")
print(f"    dirname('{test_path}') = {os.path.dirname(test_path)}")
print(f"    splitext('report.txt') = {os.path.splitext('report.txt')}")
print()

# =============================
# 5. datetime MODULE
# =============================

print("=== datetime Module ===")
print()

import datetime

now = datetime.datetime.now()
today = datetime.date.today()

print(f"  Now: {now}")
print(f"  Today: {today}")
print(f"  Year: {today.year}")
print(f"  Month: {today.month}")
print(f"  Day: {today.day}")
print(f"  Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print()

# =============================
# 6. string MODULE
# =============================

print("=== string Module ===")
print()

import string

print(f"  ascii_lowercase: {string.ascii_lowercase}")
print(f"  ascii_uppercase: {string.ascii_uppercase}")
print(f"  digits: {string.digits}")
print(f"  punctuation: {string.punctuation}")
print()

# Practical: generate a random password
password_chars = string.ascii_letters + string.digits + "!@#$"
password = "".join(random.choice(password_chars) for _ in range(12))
print(f"  Random password: {password}")
print()

# =============================
# 7. collections MODULE
# =============================

print("=== collections Module ===")
print()

from collections import Counter, defaultdict

# Counter — count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = Counter(words)
print(f"  Counter({words[:3]}...) = {word_counts}")
print(f"  Most common: {word_counts.most_common(2)}")
print()

# defaultdict — dict with default values
scores = defaultdict(list)
scores["Trush"].append(95)
scores["Trush"].append(87)
scores["Rahul"].append(92)
print(f"  defaultdict scores: {dict(scores)}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use math to calculate the hypotenuse of a 3-4-5 triangle
# 2. Use random to simulate rolling two dice 5 times
# 3. Use datetime to print the day of the week
# 4. Use collections.Counter on a string to count letters
# ============================================
