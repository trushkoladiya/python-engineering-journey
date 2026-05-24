# Basic Debugging

## What is Debugging?

Debugging means **finding and fixing errors** in your code. Errors are normal — every programmer deals with them.

## 1. Syntax Errors

A **syntax error** means Python can't understand your code. You broke a grammar rule.

```python
print("hello"    # ❌ SyntaxError: missing closing )
print "hello"    # ❌ SyntaxError: missing parentheses
```

### Common syntax errors:
- Missing `:`, `)`, `"`, or `]`
- Misspelled keywords
- Wrong indentation

## 2. Runtime Errors

Code is written correctly, but **something goes wrong when it runs**.

```python
print(10 / 0)        # ❌ ZeroDivisionError
print(int("hello"))  # ❌ ValueError
```

The code looks fine, but the operation itself is impossible.

## 3. Reading Error Messages

Python error messages tell you **what** went wrong and **where**.

```
Traceback (most recent call last):
  File "code.py", line 3, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero
```

### How to read it:
1. **Last line** = the error type and message
2. **`line 3`** = which line the error is on
3. **`File "code.py"`** = which file

### Tips:
- Always read the **last line** first
- Look at the **line number**
- Fix one error at a time — sometimes one fix removes others

## Key Points

- Syntax errors = broken grammar (Python can't read it)
- Runtime errors = code runs but fails
- Always read error messages from the **bottom up**
- Errors are normal — they help you learn
