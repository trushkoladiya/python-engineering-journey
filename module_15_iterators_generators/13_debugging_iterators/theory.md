# Debugging Iterators & Generators

Iterators and generators have unique behaviors that can cause confusing bugs. Knowing these pitfalls helps you debug faster.

## 1. Exhausted Iterators

The most common issue — trying to use an iterator after it's been consumed:

```python
gen = (x**2 for x in range(3))
print(list(gen))   # [0, 1, 4]
print(list(gen))   # [] — empty! Already exhausted.
```

**Fix:** Create a new generator, or convert to a list if you need multiple passes.

## 2. Accidental Exhaustion

Checking length or printing exhausts the generator:

```python
gen = (x for x in range(5))
print(f"Items: {list(gen)}")   # [0, 1, 2, 3, 4]

for item in gen:      # nothing happens — gen is empty!
    print(item)
```

## 3. Generator vs Generator Function

```python
def my_gen():
    yield 1
    yield 2

# This is the FUNCTION — calling it creates a generator
result = my_gen     # wrong! This is the function itself
result = my_gen()   # correct! This is the generator object
```

## 4. Modifying Data While Iterating

```python
# DON'T modify a list while iterating over it
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    if item % 2 == 0:
        my_list.remove(item)   # BUG! Skips items
```

**Fix:** Iterate over a copy, or use a generator to filter.

## Key Points

- Generators exhaust after one pass — this is the #1 bug
- Don't print/convert a generator you plan to iterate later
- Remember: `my_gen` is the function, `my_gen()` is the generator
- Never modify a collection while iterating over it
