# Loop Control Statements

Loop control statements change the normal flow of a loop. Python provides three: `break`, `continue`, and `pass`.

## `break` — Immediately Exit the Loop

`break` stops the loop entirely and jumps to the code after it:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0, 1, 2, 3, 4 (stops at 5, doesn't print 5)
```

## `continue` — Skip to Next Iteration

`continue` skips the rest of the current iteration and goes to the next one:

```python
for i in range(6):
    if i == 3:
        continue
    print(i)
# Output: 0, 1, 2, 4, 5 (skips 3)
```

## `pass` — Do Nothing (Placeholder)

`pass` is a no-op. It does nothing but prevents an empty block error:

```python
for i in range(5):
    pass    # placeholder — will add code later
```

Without `pass`, an empty block causes a `SyntaxError`.

## `break` with `while`

```python
count = 0
while True:
    if count >= 3:
        break
    print(count)
    count += 1
# Output: 0, 1, 2
```

This is a common pattern: `while True` + `break` when a condition is met.

## Key Points

- `break` → exit the loop immediately
- `continue` → skip current iteration, go to next
- `pass` → do nothing (placeholder for future code)
- `break` only exits the **innermost** loop
- Use `break` with `while True` for condition-at-end loops
