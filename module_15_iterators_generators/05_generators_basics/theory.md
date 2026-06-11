# Generators Basics

A **generator** is a simpler way to create iterators. Instead of writing a class with `__iter__` and `__next__`, you write a function with `yield`.

## The `yield` Keyword

`yield` is like `return`, but the function **pauses** instead of ending:

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i     # produce a value and PAUSE
        i += 1

for num in count_up(3):
    print(num)   # 1, 2, 3
```

## Generator vs Normal Function

| Feature | Normal Function | Generator Function |
|---------|----------------|-------------------|
| Keyword | `return` | `yield` |
| Returns | A single value | An iterator |
| Execution | Runs to completion | Pauses at each `yield` |
| Memory | All results at once | One result at a time |

## What Makes a Function a Generator?

Any function with `yield` in its body is a generator function:

```python
def my_generator():
    yield 1
    yield 2
    yield 3

# Calling it returns a generator OBJECT (not the values!)
gen = my_generator()   # does NOT execute the function body
next(gen)              # NOW it runs until first yield → 1
next(gen)              # continues until next yield → 2
```

## Lazy Evaluation

Generators produce values **on demand** — they don't compute everything upfront:

```python
def big_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Doesn't create a billion numbers in memory!
for num in big_range(1_000_000_000):
    if num > 5:
        break
    print(num)
```

## Key Points

- Use `yield` instead of `return` to create a generator
- Generators are a simple way to create iterators
- Values are produced one at a time (lazy evaluation)
- The function pauses at `yield` and resumes on `next()`
- Much less code than writing a full iterator class
