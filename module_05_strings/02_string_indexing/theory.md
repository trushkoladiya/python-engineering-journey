# String Indexing

Every character in a string has a **position number** called an **index**. You can use it to access individual characters.

## Positive Indexing

Counting starts from `0` (not 1):

```python
word = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5

print(word[0])   # P  (first character)
print(word[1])   # y  (second character)
print(word[5])   # n  (last character)
```

## Negative Indexing

You can count **backwards** from the end using negative numbers:

```python
word = "Python"
#       P   y   t   h   o   n
#      -6  -5  -4  -3  -2  -1

print(word[-1])   # n  (last character)
print(word[-2])   # o  (second from last)
print(word[-6])   # P  (first character)
```

## Getting the Last Character

Two ways to get the last character:

```python
word = "Python"
print(word[len(word) - 1])   # n — using len()
print(word[-1])              # n — using negative index (easier!)
```

## IndexError

If you use an index that is **too large**, Python gives an error:

```python
word = "Hi"
# word[5]  → IndexError: string index out of range
```

Always check that the index is within range (0 to `len(string) - 1`).

## Key Points

- Indexing starts at `0`, not `1`
- Negative indexing starts at `-1` (last character)
- `word[0]` is the first character, `word[-1]` is the last
- Going beyond the string length causes an `IndexError`
