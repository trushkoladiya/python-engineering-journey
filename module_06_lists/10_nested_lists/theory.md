# Nested Lists (Deep)

Nested lists are lists inside lists. They let you represent grids, tables, and multi-dimensional data.

## Accessing Nested Elements

Use **two indices** — first for the outer list, then for the inner:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])       # [1, 2, 3] — first row
print(matrix[0][1])    # 2 — first row, second element
print(matrix[2][2])    # 9 — third row, third element
```

## Modifying Nested Structures

```python
matrix = [[1, 2], [3, 4]]
matrix[0][1] = 99
print(matrix)   # [[1, 99], [3, 4]]
```

## Multi-Dimensional Lists (Matrix)

A 2D list can represent a grid or table:

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access row by row
for row in grid:
    print(row)
```

## Iterating Over Nested Lists

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

## Key Points

- Use `list[row][col]` for 2D access
- Nested lists can be modified in place
- Use nested `for` loops to iterate all elements
- Useful for grids, tables, and matrix data
