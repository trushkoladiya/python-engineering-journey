# Python Syntax Basics

## 1. Indentation

Python uses **spaces** (not braces `{}`) to group code. This is called indentation.

- Standard is **4 spaces** per level
- Incorrect indentation causes errors
- You'll use indentation more in later modules (control flow, functions, etc.)

For now, just know: **start your code at the beginning of the line** (no extra spaces).

```python
# ✅ Correct
print("hello")

# ❌ Wrong - unexpected indent
    print("hello")
```

## 2. Statements vs Expressions

### Statement
A statement **does something**. It's an instruction.

```python
print("hello")    # this is a statement (it does something)
x = 5             # this is a statement (it assigns a value)
```

### Expression
An expression **produces a value**.

```python
2 + 3       # this is an expression (it produces 5)
10 * 2      # this is an expression (it produces 20)
```

> A statement can contain an expression, but not the other way around.

## 3. Comments

Comments are notes for humans. Python ignores them.

```python
# This is a comment
print("hello")  # This is also a comment
```

- Start with `#`
- Everything after `#` on that line is ignored
- Use comments to explain your code

## Key Points

- Indentation matters in Python
- Statements do things, expressions produce values
- Use `#` for comments
- Keep code at the left edge (for now)
