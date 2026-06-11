# Best Practices

Writing **clean error handling** code is what separates beginners from engineers.

## Rule 1: Never Use Bare `except`

```python
# BAD — catches EVERYTHING, hides bugs
try:
    do_something()
except:
    pass

# GOOD — catches only what you expect
try:
    do_something()
except ValueError:
    print("Invalid value")
```

## Rule 2: Don't Catch Too Broadly

```python
# BAD — Exception catches too many things
try:
    number = int(text)
except Exception:
    pass

# GOOD — catch only the specific error
try:
    number = int(text)
except ValueError:
    print("Not a number")
```

## Rule 3: Don't Silence Errors

```python
# BAD — error disappears silently
except ValueError:
    pass

# GOOD — at least log it
except ValueError as e:
    print(f"Warning: {e}")
```

## Rule 4: Handle Only Expected Errors

Only catch exceptions that you **know how to handle**:

```python
# I know what to do about a missing file
except FileNotFoundError:
    return default_config()

# I don't know what to do about this — let it propagate!
# except Exception:
#     ???
```

## Rule 5: Use `with` for Resource Safety

```python
# GOOD — automatically closes file even on error
with open("data.txt", "r") as f:
    content = f.read()
```

The `with` statement handles cleanup automatically — better than manual `try/finally`.

## Rule 6: Keep try Blocks Small

```python
# BAD — too much code in try
try:
    data = read_file()
    processed = transform(data)
    result = calculate(processed)
    save(result)
except ValueError:
    print("Error!")   # Which step failed?

# GOOD — focused try block
data = read_file()
try:
    number = int(data)
except ValueError:
    print("Data is not a number")
```

## Key Points

- Catch **specific** exceptions, not broad ones
- Never **silence** errors with `pass`
- Keep `try` blocks **small and focused**
- Use `with` for **automatic resource cleanup**
- Only catch what you **know how to handle**
