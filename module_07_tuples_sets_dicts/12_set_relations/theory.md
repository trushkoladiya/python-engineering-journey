# Set Relations

Python provides methods to check **relationships** between sets.

## Subset — `issubset()`

Set A is a **subset** of B if **every** element of A is also in B:

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))    # True  — all of a is in b
print(b.issubset(a))    # False — b has elements not in a
```

You can also use `<=`:

```python
print(a <= b)   # True
```

## Superset — `issuperset()`

Set B is a **superset** of A if B contains **all** elements of A:

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(b.issuperset(a))   # True  — b contains all of a
print(a.issuperset(b))   # False
```

You can also use `>=`:

```python
print(b >= a)   # True
```

## Disjoint — `isdisjoint()`

Two sets are **disjoint** if they have **no** common elements:

```python
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))   # True — no overlap

c = {3, 4, 5}
print(a.isdisjoint(c))   # False — 3 is in both
```

## Key Points

- `issubset()` / `<=` — is A contained within B?
- `issuperset()` / `>=` — does B contain all of A?
- `isdisjoint()` — do A and B share zero elements?
- Every set is a subset and superset of **itself**
