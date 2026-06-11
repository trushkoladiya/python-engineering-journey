# ============================================
# MODULE 18 - SUBTOPIC 12: Advanced Standard Library Usage
# ============================================

# Deep dive into collections, itertools, and functools —
# the most powerful modules in Python's standard library.

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap
from itertools import (chain, product, combinations, permutations,
                       accumulate, groupby, islice, cycle, repeat, starmap)
from functools import reduce, partial, wraps, total_ordering
import operator

# =============================
# 1. COLLECTIONS: Counter (Deep Use)
# =============================

print("=== Counter — Deep Usage ===")
print()

# Count word frequencies
text = "the quick brown fox jumps over the lazy dog the fox"
word_count = Counter(text.split())
print(f"  Word counts: {word_count}")
print(f"  Most common 3: {word_count.most_common(3)}")

# Arithmetic with counters
inventory_a = Counter(apples=5, bananas=3, oranges=2)
inventory_b = Counter(apples=2, bananas=5, grapes=4)

print(f"  Combined: {inventory_a + inventory_b}")
print(f"  Difference: {inventory_a - inventory_b}")
print(f"  Intersection: {inventory_a & inventory_b}")  # Min of each
print(f"  Union: {inventory_a | inventory_b}")          # Max of each

# Count characters
char_count = Counter("mississippi")
print(f"  'mississippi' chars: {char_count}")
print(f"  Total elements: {sum(char_count.values())}")
print()

# =============================
# 2. COLLECTIONS: defaultdict
# =============================

print("=== defaultdict ===")
print()

# Group items by category
items = [
    ("fruit", "apple"), ("veggie", "carrot"), ("fruit", "banana"),
    ("meat", "chicken"), ("veggie", "peas"), ("fruit", "cherry"),
    ("meat", "beef"), ("veggie", "corn"),
]

groups = defaultdict(list)
for category, item in items:
    groups[category].append(item)

for category, items_list in groups.items():
    print(f"  {category}: {items_list}")
print()

# defaultdict with int (for counting)
word_freq = defaultdict(int)
for word in "hello world hello python hello world".split():
    word_freq[word] += 1
print(f"  Word frequency: {dict(word_freq)}")

# defaultdict with set (for unique items)
tags = defaultdict(set)
tags["python"].add("programming")
tags["python"].add("scripting")
tags["python"].add("programming")  # Duplicate — ignored
print(f"  Tags: {dict(tags)}")
print()

# =============================
# 3. COLLECTIONS: deque
# =============================

print("=== deque — Double-Ended Queue ===")
print()

# deque is O(1) for append/pop on BOTH ends (list is O(n) for left)
dq = deque([1, 2, 3, 4, 5])
print(f"  Initial: {dq}")

dq.appendleft(0)
print(f"  appendleft(0): {dq}")

dq.append(6)
print(f"  append(6): {dq}")

dq.popleft()
print(f"  popleft(): {dq}")

dq.rotate(2)  # Rotate right by 2
print(f"  rotate(2): {dq}")

dq.rotate(-2)  # Rotate left by 2
print(f"  rotate(-2): {dq}")

# Fixed-size deque — automatically drops old items
recent = deque(maxlen=3)
for i in range(5):
    recent.append(i)
    print(f"    Added {i}: {list(recent)}")
print()

# =============================
# 4. COLLECTIONS: namedtuple
# =============================

print("=== namedtuple ===")
print()

Point = namedtuple('Point', ['x', 'y'])
Color = namedtuple('Color', 'red green blue')

p = Point(3, 4)
print(f"  Point: {p}")
print(f"  x={p.x}, y={p.y}")
print(f"  As tuple: {tuple(p)}")
print(f"  As dict: {p._asdict()}")

# Create a new point with one field changed
p2 = p._replace(x=10)
print(f"  Replaced x: {p2}")

c = Color(255, 128, 0)
print(f"  Color: {c}")
print()

# =============================
# 5. COLLECTIONS: ChainMap
# =============================

print("=== ChainMap ===")
print()

# Search through multiple dicts in order
defaults = {"color": "blue", "size": "medium", "font": "Arial"}
user_prefs = {"color": "red", "font": "Helvetica"}
cli_args = {"color": "green"}

config = ChainMap(cli_args, user_prefs, defaults)
print(f"  color: {config['color']}")   # green (from cli_args)
print(f"  font: {config['font']}")     # Helvetica (from user_prefs)
print(f"  size: {config['size']}")     # medium (from defaults)
print()

# =============================
# 6. ITERTOOLS: chain, product, combinations
# =============================

print("=== itertools: Combinatorics ===")
print()

# chain — flatten multiple iterables
flattened = list(chain([1, 2], [3, 4], [5, 6]))
print(f"  chain: {flattened}")

# product — cartesian product
pairs = list(product("AB", [1, 2, 3]))
print(f"  product: {pairs}")

# combinations — unordered selections
combos = list(combinations([1, 2, 3, 4], 2))
print(f"  combinations(4, 2): {combos}")

# permutations — ordered arrangements
perms = list(permutations([1, 2, 3], 2))
print(f"  permutations(3, 2): {perms}")
print()

# =============================
# 7. ITERTOOLS: accumulate, groupby
# =============================

print("=== itertools: accumulate & groupby ===")
print()

# accumulate — running totals
numbers = [1, 2, 3, 4, 5]
running_sum = list(accumulate(numbers))
print(f"  Running sum of {numbers}: {running_sum}")

running_product = list(accumulate(numbers, operator.mul))
print(f"  Running product: {running_product}")

running_max = list(accumulate([3, 1, 4, 1, 5, 9, 2, 6], max))
print(f"  Running max: {running_max}")
print()

# groupby — group consecutive items
data = sorted([
    ("A", 1), ("B", 2), ("A", 3), ("B", 4), ("C", 5)
])
print(f"  Sorted data: {data}")
for key, group in groupby(data, key=lambda x: x[0]):
    items = list(group)
    print(f"    Group '{key}': {items}")
print()

# =============================
# 8. ITERTOOLS: islice, cycle, repeat
# =============================

print("=== itertools: Infinite Iterators ===")
print()

# islice — slice any iterator
from itertools import count
first_10_evens = list(islice(count(0, 2), 10))
print(f"  First 10 evens: {first_10_evens}")

# cycle — repeat endlessly, take a slice
colors = list(islice(cycle(["red", "green", "blue"]), 8))
print(f"  Cycling colors: {colors}")

# repeat
fives = list(repeat(5, times=6))
print(f"  Repeat 5 six times: {fives}")

# starmap — map with unpacked arguments
pairs = [(2, 3), (4, 5), (6, 7)]
products = list(starmap(operator.mul, pairs))
print(f"  starmap mul: {pairs} → {products}")
print()

# =============================
# 9. FUNCTOOLS: reduce, partial, total_ordering
# =============================

print("=== functools: Advanced Usage ===")
print()

# reduce — fold a sequence into one value
numbers = [1, 2, 3, 4, 5]
total = reduce(operator.add, numbers)
product = reduce(operator.mul, numbers)
print(f"  reduce(add, {numbers}) = {total}")
print(f"  reduce(mul, {numbers}) = {product}")

# Find max using reduce
largest = reduce(lambda a, b: a if a > b else b, [34, 12, 89, 45])
print(f"  reduce(max) = {largest}")
print()

# partial — create specialized functions
def greet(greeting, name):
    return f"{greeting}, {name}!"

hello = partial(greet, "Hello")
hi = partial(greet, "Hi")
print(f"  hello('Trush') = {hello('Trush')}")
print(f"  hi('Rahul') = {hi('Rahul')}")
print()

# total_ordering — define all comparison operators from __eq__ and one other
@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

    def __repr__(self):
        return f"Student({self.name}, {self.grade})"

students = [Student("Trush", 90), Student("Rahul", 85), Student("Charlie", 92)]
print(f"  Students sorted: {sorted(students)}")
print(f"  Trush > Rahul? {students[0] > students[1]}")
print()

# =============================
# 10. PRACTICAL: COMBINING STDLIB TOOLS
# =============================

print("=== Practical: Text Analysis ===")
print()

text = """Python is a great language for learning programming.
Python makes it easy to write clean code.
Learning Python is fun and rewarding.
Clean code is important for any programmer."""

# Word frequency with Counter
words = text.lower().split()
word_freq = Counter(words)
print(f"  Top 5 words: {word_freq.most_common(5)}")

# Group words by first letter using defaultdict
by_letter = defaultdict(list)
for word in set(words):
    by_letter[word[0]].append(word)
for letter in sorted(by_letter)[:5]:
    print(f"    '{letter}': {sorted(by_letter[letter])}")

# Running character count with accumulate
line_lengths = [len(line) for line in text.split('\n')]
cumulative = list(accumulate(line_lengths))
print(f"  Line lengths: {line_lengths}")
print(f"  Cumulative: {cumulative}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use Counter to find the 5 most common characters
#    in a paragraph of text
# 2. Use deque(maxlen=N) to implement a "recent history"
#    feature that remembers the last 10 actions
# 3. Use itertools.combinations to find all pairs of
#    numbers from a list that sum to a target
# ============================================
