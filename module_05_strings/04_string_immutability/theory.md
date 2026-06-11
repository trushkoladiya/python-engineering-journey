# String Immutability

Strings in Python are **immutable** — once created, they **cannot be changed**. You can only create new strings.

## What Does Immutable Mean?

You **cannot** modify a character in a string:

```python
word = "Hello"
# word[0] = "J"   # ❌ TypeError: 'str' object does not support item assignment
```

This is different from some other data types you'll learn later.

## Creating New Strings from Old Ones

Instead of changing a string, you create a **new** string:

```python
word = "Hello"
new_word = "J" + word[1:]
print(new_word)   # Jello
```

The original string `"Hello"` stays unchanged. `new_word` is a completely new string.

## More Examples

```python
name = "Trush"
# To "change" Trush to Trask:
name = name[:2] + "a" + name[3:4] + "k"
print(name)   # Trask
```

Note: We **reassigned** the variable `name` to a new string. The old string `"Trush"` is gone from the variable, but we didn't modify it — we replaced it.

## Reassigning vs Modifying

```python
text = "Hello"
text = "World"    # ✅ This is reassignment — creating a new string
# text[0] = "W"   # ❌ This would be modification — NOT allowed
```

Reassigning a variable to a new string is **always** fine. Trying to change individual characters is **not**.

## Key Points

- Strings are **immutable** — you cannot change individual characters
- To "modify" a string, create a **new** string using slicing and concatenation
- Reassigning a variable to a new string is not the same as modifying
- This is an important concept that applies to other Python types too
