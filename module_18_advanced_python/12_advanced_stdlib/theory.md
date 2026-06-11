# Advanced Standard Library Usage

## The Standard Library Is Your Superpower

Python's standard library contains powerful modules that solve common problems efficiently. Mastering them means writing less code that runs faster.

## collections — Specialized Containers

### Counter
```python
from collections import Counter
words = ["apple", "banana", "apple", "cherry", "apple"]
count = Counter(words)
print(count)               # Counter({'apple': 3, 'banana': 1, 'cherry': 1})
print(count.most_common(2))  # [('apple', 3), ('banana', 1)]
```

### defaultdict
```python
from collections import defaultdict
groups = defaultdict(list)
groups["fruits"].append("apple")
groups["vegs"].append("carrot")
# No KeyError — automatically creates empty list
```

### deque
```python
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)   # O(1) — faster than list.insert(0, x)
dq.pop()            # O(1)
```

## itertools — Efficient Iteration

```python
from itertools import chain, product, combinations

# Chain multiple iterables
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# All pairs
list(product("AB", "12"))  # [('A','1'), ('A','2'), ('B','1'), ('B','2')]

# Combinations
list(combinations([1, 2, 3], 2))  # [(1,2), (1,3), (2,3)]
```

## functools — Function Tools

```python
from functools import reduce, partial

# Reduce a sequence to a single value
total = reduce(lambda a, b: a + b, [1, 2, 3, 4])  # 10

# Create a partial function
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
print(square(5))  # 25
```

## Key Points

- `collections` provides Counter, defaultdict, deque, namedtuple, OrderedDict
- `itertools` provides memory-efficient iteration tools
- `functools` provides reduce, partial, lru_cache, wraps
- Learn these modules well — they replace hundreds of lines of custom code
