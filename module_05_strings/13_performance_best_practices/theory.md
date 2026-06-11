# Performance & Best Practices (Intro)

When working with strings, some approaches are faster and cleaner than others.

## `join()` vs `+` for Concatenation

When building a string in a loop, using `+` creates a **new string every time**:

```python
# ❌ Slower — creates many intermediate strings
result = ""
for i in range(5):
    result = result + str(i)
# Creates: "", "0", "01", "012", "0123", "01234"
```

Using `join()` is **much faster** for many strings:

```python
# ✅ Faster — builds the string all at once
parts = []
for i in range(5):
    parts = parts + [str(i)]
result = "".join(parts)
```

> For small strings (under ~10 pieces), `+` is fine. For larger operations, prefer `join()`.

## Avoiding Unnecessary Copies

Since strings are immutable, every "modification" creates a new copy. Be aware of this:

```python
# ❌ Creates 3 intermediate strings
text = "Hello"
text = text + " "
text = text + "World"
text = text + "!"

# ✅ Better — single concatenation
text = "Hello" + " " + "World" + "!"
```

## Use f-strings Over Concatenation

```python
name = "Trush"
age = 21

# ❌ Harder to read
message = "Name: " + name + ", Age: " + str(age)

# ✅ Much cleaner
message = f"Name: {name}, Age: {age}"
```

## Key Points

- Use `join()` for combining many strings (especially in loops)
- Use `+` for simple, small concatenations
- Use f-strings instead of `+` for mixing text and variables
- Remember: every string operation creates a **new** string
