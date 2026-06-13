# String Iteration

Since strings are sequences of characters, you can **loop** through them just like any other sequence.

## Looping Through Characters

Use a `for` loop to go through each character:

```python
word = "Hello"
for char in word:
    print(char)
# Output: H, e, l, l, o (each on a new line)
```

## Index-Based Iteration

Use `range(len(...))` to get both the index and the character:

```python
word = "Hello"
for i in range(len(word)):
    print("Index", i, "→", word[i])
```

## Using `while` Loop

You can also iterate with a `while` loop:

```python
word = "Hello"
i = 0
while i < len(word):
    print(word[i])
    i += 1
```

## Practical Example: Counting Characters

```python
text = "banana"
count = 0
for char in text:
    if char == "a":
        count += 1
print("Letter 'a' appears", count, "times")   # 3
```

## Key Points

- `for char in string` iterates through each character
- `for i in range(len(string))` gives you index-based access
- You can use `while` loops for iteration too
- Combine iteration with conditions to search or count
