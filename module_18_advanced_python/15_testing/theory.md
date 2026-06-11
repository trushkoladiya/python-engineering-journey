# Testing (Introduction to Professional Practice)

## Why Test Your Code?

Testing ensures your code works correctly **now** and **continues to work** after changes. Without tests, every change is risky.

## unittest — Python's Built-in Testing Framework

```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
```

## Common Assert Methods

| Method | Checks |
|--------|--------|
| `assertEqual(a, b)` | a == b |
| `assertNotEqual(a, b)` | a != b |
| `assertTrue(x)` | x is True |
| `assertFalse(x)` | x is False |
| `assertIsNone(x)` | x is None |
| `assertIn(a, b)` | a in b |
| `assertRaises(Error)` | Error is raised |

## Test Structure: Arrange, Act, Assert

```python
def test_discount(self):
    # Arrange — set up data
    price = 100
    discount = 0.2

    # Act — call the function
    result = apply_discount(price, discount)

    # Assert — check the result
    self.assertEqual(result, 80)
```

## setUp and tearDown

```python
class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Runs BEFORE each test
        self.db = create_test_database()

    def tearDown(self):
        # Runs AFTER each test
        self.db.close()

    def test_insert(self):
        self.db.insert({"name": "Trush"})
        self.assertEqual(self.db.count(), 1)
```

## Key Points

- Write tests for every function that has logic
- Use `assertEqual`, `assertTrue`, `assertRaises` for assertions
- Follow **Arrange → Act → Assert** pattern
- Use `setUp()` and `tearDown()` for shared setup/cleanup
- Run tests with `python -m unittest` from the terminal
