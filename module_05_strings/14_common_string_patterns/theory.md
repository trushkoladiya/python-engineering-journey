# Common String Patterns

This subtopic covers frequently used string patterns that combine everything from Module 5.

## Palindrome Check

A palindrome reads the same forwards and backwards:

```python
word = "racecar"
if word == word[::-1]:
    print("Palindrome!")
else:
    print("Not a palindrome")
```

## Character Frequency Counting

Count how many times each character appears:

```python
text = "hello"
for char in text:
    count = text.count(char)
    print(f"'{char}' appears {count} times")
```

## Substring Search

Find all positions of a substring:

```python
text = "abcabcabc"
sub = "abc"
pos = text.find(sub)
while pos != -1:
    print(f"Found at index {pos}")
    pos = text.find(sub, pos + 1)
```

## Basic Parsing

Extract information from structured text:

```python
line = "Name: Trush, Age: 21"
parts = line.split(", ")
for part in parts:
    key_value = part.split(": ")
    print(f"{key_value[0]} → {key_value[1]}")
```

## Key Points

- Palindrome: compare string with its reverse (`[::-1]`)
- Frequency: use `count()` or loop through characters
- Substring search: use `find()` in a loop
- Parsing: use `split()` to break structured text into pieces
