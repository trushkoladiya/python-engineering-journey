# String Slicing

Slicing lets you extract a **portion** (substring) of a string by specifying a range of indices.

## Basic Slicing: `start:end`

```python
word = "Python"
print(word[0:3])   # Pyt — characters at index 0, 1, 2
print(word[2:5])   # tho — characters at index 2, 3, 4
```

- `start` is **included**
- `end` is **excluded** (stops one before)

## Omitting Start or End

```python
word = "Python"
print(word[:3])    # Pyt — from beginning to index 2
print(word[3:])    # hon — from index 3 to the end
print(word[:])     # Python — full copy of the string
```

## Step Slicing: `start:end:step`

The third number controls the **step** (how many characters to skip):

```python
word = "Python"
print(word[0:6:2])   # Pto — every 2nd character
print(word[::2])     # Pto — same thing (start and end omitted)
print(word[1:6:2])   # yhn — every 2nd character starting from index 1
```

## Reversing a String

Use a step of `-1`:

```python
word = "Python"
print(word[::-1])   # nohtyP — reversed!
```

## Negative Indices in Slicing

```python
word = "Python"
print(word[-4:-1])   # tho — from index -4 to -2
print(word[-3:])     # hon — last 3 characters
```

## Out-of-Range Slicing

Unlike indexing, slicing does **not** cause errors for out-of-range values:

```python
word = "Hi"
print(word[0:100])   # Hi — Python just gives what it can
print(word[5:10])    # (empty string) — nothing in that range
```

## Key Points

- `string[start:end]` — end is **excluded**
- Omitting `start` means "from the beginning"
- Omitting `end` means "to the end"
- `string[::step]` — skip characters by step
- `string[::-1]` — reverses the string
- Out-of-range slicing is safe (no error)
