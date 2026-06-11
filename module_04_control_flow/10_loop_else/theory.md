# Loop with Else

In Python, loops can have an `else` block. The `else` runs **only when the loop completes normally** (without hitting `break`).

## `for-else`

```python
for i in range(5):
    print(i)
else:
    print("Loop finished normally")
```

The `else` block runs because the loop completed without `break`.

## When `else` Does NOT Run

If the loop exits via `break`, the `else` block is **skipped**:

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print")    # skipped because of break
```

Output: `0, 1, 2` — the `else` is skipped.

## `while-else`

Same behavior — `else` runs if the loop ends normally:

```python
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop finished normally")
```

## Practical Use: Search Pattern

The most useful case for loop-else is **searching**:

```python
target = 7
for num in range(1, 10):
    if num == target:
        print("Found:", target)
        break
else:
    print("Not found!")
```

- If `target` is found → `break` runs → `else` is skipped
- If `target` is not found → loop finishes → `else` runs

## Key Points

- `else` after a loop runs only when the loop ends **without `break`**
- If `break` is triggered, `else` is skipped
- Works with both `for` and `while` loops
- Most useful for search/find patterns
- If the loop never runs (condition is False from start), `else` still runs
