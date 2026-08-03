# ============================================
# MODULE 16 - SUBTOPIC 15: Functional vs Imperative Style
# ============================================

# Python supports both styles.
# Knowing WHEN to use each is key.

from functools import reduce

# =============================
# 1. TRANSFORMING A LIST
# =============================

print("=== Transforming a List ===")
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# IMPERATIVE: loop and accumulate
result_imp = []
for x in numbers:
    if x % 2 == 0:
        result_imp.append(x ** 2)

# FUNCTIONAL: list comprehension
result_func = [x ** 2 for x in numbers if x % 2 == 0]

# FUNCTIONAL: map + filter
result_mapf = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

print(f"  Imperative:    {result_imp}")
print(f"  Comprehension: {result_func}")
print(f"  map+filter:    {result_mapf}")
print()

# =============================
# 2. SUMMING VALUES
# =============================

print("=== Summing Values ===")
print()

prices = [9.99, 24.50, 3.75, 149.00, 12.99]

# IMPERATIVE
total_imp = 0
for price in prices:
    total_imp += price

# FUNCTIONAL
total_func = sum(prices)

# FUNCTIONAL: reduce
total_reduce = reduce(lambda a, b: a + b, prices)

print(f"  Imperative: ${total_imp:.2f}")
print(f"  sum():      ${total_func:.2f}")
print(f"  reduce():   ${total_reduce:.2f}")
print()

# =============================
# 3. FINDING ITEMS
# =============================

print("=== Finding Items ===")
print()

words = ["python", "java", "javascript", "go", "rust", "typescript"]

# IMPERATIVE: find first word longer than 6
found_imp = None
for word in words:
    if len(word) > 6:
        found_imp = word
        break

# FUNCTIONAL: next with generator
found_func = next((w for w in words if len(w) > 6), None)

print(f"  Imperative: {found_imp}")
print(f"  Functional: {found_func}")
print()

# =============================
# 4. GROUPING DATA
# =============================

print("=== Grouping Data ===")
print()

students = [
    ("Trush", "A"), ("Rahul", "B"), ("Eve", "A"),
    ("Charlie", "C"), ("Diana", "B"), ("Frank", "A"),
]

# IMPERATIVE
groups_imp = {}
for name, grade in students:
    if grade not in groups_imp:
        groups_imp[grade] = []
    groups_imp[grade].append(name)

# FUNCTIONAL (still uses loop, but builds cleanly)
from collections import defaultdict
groups_func = defaultdict(list)
for name, grade in students:
    groups_func[grade].append(name)

print(f"  Imperative groups: {dict(groups_imp)}")
print(f"  Functional groups: {dict(groups_func)}")
print()

# =============================
# 5. STRING PROCESSING
# =============================

print("=== String Processing ===")
print()

raw_names = ["  TRUSH  ", "rahul", "  Eve ", "CHARLIE", "  diana  "]

# IMPERATIVE
cleaned_imp = []
for name in raw_names:
    cleaned_imp.append(name.strip().title())

# FUNCTIONAL: comprehension
cleaned_comp = [name.strip().title() for name in raw_names]

# FUNCTIONAL: map
cleaned_map = list(map(lambda n: n.strip().title(), raw_names))

print(f"  Raw: {raw_names}")
print(f"  Imperative:    {cleaned_imp}")
print(f"  Comprehension: {cleaned_comp}")
print(f"  map():         {cleaned_map}")
print()

# =============================
# 6. NESTED DATA PROCESSING
# =============================

print("=== Nested Data Processing ===")
print()

orders = [
    {"customer": "Trush", "items": [{"price": 10}, {"price": 20}]},
    {"customer": "Rahul", "items": [{"price": 30}]},
    {"customer": "Eve", "items": [{"price": 5}, {"price": 15}, {"price": 25}]},
]

# IMPERATIVE: calculate total per customer
print("  Imperative:")
for order in orders:
    total = 0
    for item in order["items"]:
        total += item["price"]
    print(f"    {order['customer']}: ${total}")
print()

# FUNCTIONAL: same thing
print("  Functional:")
totals = [
    (order["customer"], sum(item["price"] for item in order["items"]))
    for order in orders
]
for customer, total in totals:
    print(f"    {customer}: ${total}")
print()

# =============================
# 7. WHEN FUNCTIONAL IS BETTER
# =============================

print("=== When Functional Shines ===")
print()

data = range(1, 11)

# Chained transformations are clean
result = (
    sorted(
        map(lambda x: x ** 2,
            filter(lambda x: x % 2 == 0, data)),
        reverse=True
    )
)
print(f"  Chained: {result}")

# Even cleaner as comprehension
result2 = sorted([x ** 2 for x in data if x % 2 == 0], reverse=True)
print(f"  Comprehension: {result2}")
print()

# =============================
# 8. WHEN IMPERATIVE IS BETTER
# =============================

print("=== When Imperative Shines ===")
print()

# Complex logic with multiple branches and state
def process_transactions(transactions):
    """Complex logic that's clearer as imperative code."""
    results = []
    balance = 0

    for t in transactions:
        if t["type"] == "deposit":
            balance += t["amount"]
            status = "OK"
        elif t["type"] == "withdraw":
            if balance >= t["amount"]:
                balance -= t["amount"]
                status = "OK"
            else:
                status = "INSUFFICIENT FUNDS"
        else:
            status = "UNKNOWN TYPE"

        results.append({
            "type": t["type"],
            "amount": t["amount"],
            "status": status,
            "balance": balance,
        })

    return results

transactions = [
    {"type": "deposit", "amount": 100},
    {"type": "withdraw", "amount": 30},
    {"type": "withdraw", "amount": 200},
    {"type": "deposit", "amount": 50},
]

results = process_transactions(transactions)
for r in results:
    print(f"  {r['type']:8} ${r['amount']:3} → {r['status']:20} Balance: ${r['balance']}")
print()
print("  (This complex state logic is clearer as imperative code)")
print()

# =============================
# 9. MIXING BOTH STYLES
# =============================

print("=== Best of Both Worlds ===")
print()

# Use functional for data transformation
raw_scores = [85, 92, 78, 95, 88, 67, 91, 73, 99, 82]

# Functional parts
passing_scores = [s for s in raw_scores if s >= 70]   # filter
curved_scores = [min(s + 5, 100) for s in passing_scores]  # map
average = sum(curved_scores) / len(curved_scores)  # reduce

# Imperative part for formatting
print("  Score Report:")
print(f"  Total students: {len(raw_scores)}")
print(f"  Passing: {len(passing_scores)}")
print(f"  Average (curved): {average:.1f}")
print(f"  Highest: {max(curved_scores)}")
print(f"  Lowest: {min(curved_scores)}")
print()

# =============================
# 10. READABILITY COMPARISON
# =============================

print("=== Readability Comparison ===")
print()

# Too much functional — hard to read
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bad = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, map(lambda x: x + 1, filter(lambda x: x > 3, data)))))
print(f"  Over-functional: {bad}")

# Same thing, readable
good = [
    (x + 1) ** 2
    for x in data
    if x > 3
    if (x + 1) % 2 == 0
]
print(f"  Readable:        {good}")
print()
print("  Rule: If it's hard to read, it's wrong style!")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Rewrite an imperative loop as a list comprehension
# 2. Identify code where imperative is genuinely clearer
# 3. Mix both styles to process a complex dataset
# ============================================
