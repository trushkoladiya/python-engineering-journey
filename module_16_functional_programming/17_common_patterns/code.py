# ============================================
# MODULE 16 - SUBTOPIC 17: Common Patterns (Engineering Thinking)
# ============================================

# Real-world functional patterns for data processing.
# These are patterns you'll use every day as a developer.

from functools import reduce, partial
from collections import defaultdict

# =============================
# 1. DATA TRANSFORMATION PIPELINE
# =============================

print("=== Data Transformation Pipeline ===")
print()

# Raw CSV-like data
raw_data = [
    "Trush,85,Engineering",
    "Rahul,92,Marketing",
    "Eve,78,Engineering",
    "Charlie,95,Design",
    "Diana,88,Marketing",
    "Frank,71,Engineering",
]

# Step 1: Parse raw strings into dicts
def parse_record(line):
    name, score, dept = line.split(",")
    return {"name": name, "score": int(score), "dept": dept}

# Step 2: Add grade
def add_grade(record):
    score = record["score"]
    grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "F"))
    return {**record, "grade": grade}

# Step 3: Format for display
def format_record(record):
    return f"  {record['name']:10} | {record['dept']:12} | {record['score']:3} | {record['grade']}"

# Build the pipeline
records = list(map(parse_record, raw_data))
graded = list(map(add_grade, records))
formatted = list(map(format_record, graded))

print("  Name       | Department   | Score | Grade")
print("  " + "-" * 45)
for line in formatted:
    print(line)
print()

# =============================
# 2. GROUP BY PATTERN
# =============================

print("=== Group By Pattern ===")
print()

def group_by(items, key_func):
    """Group items by a key function."""
    groups = defaultdict(list)
    for item in items:
        groups[key_func(item)].append(item)
    return dict(groups)

# Group students by department
by_dept = group_by(graded, lambda r: r["dept"])

for dept, members in sorted(by_dept.items()):
    names = [m["name"] for m in members]
    avg = sum(m["score"] for m in members) / len(members)
    print(f"  {dept}: {', '.join(names)} (avg: {avg:.1f})")
print()

# Group by grade
by_grade = group_by(graded, lambda r: r["grade"])
for grade, members in sorted(by_grade.items()):
    names = [m["name"] for m in members]
    print(f"  Grade {grade}: {', '.join(names)}")
print()

# =============================
# 3. MAP-FILTER-REDUCE PATTERN
# =============================

print("=== Map-Filter-Reduce Pattern ===")
print()

products = [
    {"name": "Laptop", "price": 999, "qty": 2, "category": "Electronics"},
    {"name": "Book", "price": 15, "qty": 10, "category": "Education"},
    {"name": "Phone", "price": 699, "qty": 5, "category": "Electronics"},
    {"name": "Pen", "price": 2, "qty": 100, "category": "Office"},
    {"name": "Tablet", "price": 449, "qty": 3, "category": "Electronics"},
    {"name": "Notebook", "price": 5, "qty": 50, "category": "Office"},
]

# Total revenue from electronics priced above $500
electronics_revenue = reduce(
    lambda total, p: total + p["price"] * p["qty"],
    filter(lambda p: p["category"] == "Electronics" and p["price"] > 500, products),
    0
)
print(f"  Electronics (>$500) revenue: ${electronics_revenue:,}")

# Average price per category
categories = group_by(products, lambda p: p["category"])
for cat, items in sorted(categories.items()):
    avg_price = sum(p["price"] for p in items) / len(items)
    total_qty = sum(p["qty"] for p in items)
    print(f"  {cat}: avg ${avg_price:.2f}, total qty {total_qty}")
print()

# =============================
# 4. FILTERING AND AGGREGATION SYSTEM
# =============================

print("=== Filtering and Aggregation System ===")
print()

def make_report(data, filters=None, aggregations=None):
    """Generic reporting function."""
    # Apply all filters
    filtered = data
    if filters:
        for f in filters:
            filtered = list(filter(f, filtered))

    # Apply all aggregations
    results = {}
    if aggregations:
        for name, agg_func in aggregations.items():
            results[name] = agg_func(filtered)

    return filtered, results

sales = [
    {"product": "Widget A", "amount": 150, "region": "North"},
    {"product": "Widget B", "amount": 300, "region": "South"},
    {"product": "Widget A", "amount": 200, "region": "South"},
    {"product": "Widget C", "amount": 50, "region": "North"},
    {"product": "Widget B", "amount": 400, "region": "North"},
    {"product": "Widget A", "amount": 100, "region": "South"},
]

# Generate report with filters and aggregations
filtered, stats = make_report(
    sales,
    filters=[
        lambda s: s["region"] == "North",
        lambda s: s["amount"] > 100,
    ],
    aggregations={
        "count": len,
        "total_amount": lambda items: sum(i["amount"] for i in items),
        "avg_amount": lambda items: sum(i["amount"] for i in items) / len(items) if items else 0,
        "products": lambda items: list(set(i["product"] for i in items)),
    },
)

print("  Report: North region, amount > $100")
print(f"  Records: {stats['count']}")
print(f"  Total: ${stats['total_amount']}")
print(f"  Average: ${stats['avg_amount']:.2f}")
print(f"  Products: {stats['products']}")
print()

# =============================
# 5. DATA CLEANING PIPELINE
# =============================

print("=== Data Cleaning Pipeline ===")
print()

raw_emails = [
    "  Trush@Example.COM  ",
    "",
    "   RAHUL@test.com",
    "invalid-email",
    "eve@Company.Org  ",
    None,
    "  charlie@email.COM",
    "   ",
]

def remove_none(items):
    return [x for x in items if x is not None]

def strip_whitespace(items):
    return [x.strip() for x in items]

def remove_empty(items):
    return [x for x in items if x]

def lowercase_all(items):
    return [x.lower() for x in items]

def validate_email(items):
    return [x for x in items if "@" in x and "." in x.split("@")[-1]]

# Apply pipeline
pipeline_steps = [
    ("Remove None", remove_none),
    ("Strip whitespace", strip_whitespace),
    ("Remove empty", remove_empty),
    ("Lowercase", lowercase_all),
    ("Validate format", validate_email),
]

data = raw_emails
print(f"  Raw: {raw_emails}")
for step_name, step_func in pipeline_steps:
    data = step_func(data)
    print(f"  After {step_name}: {data}")
print()

# =============================
# 6. FUNCTION TOOLKIT PATTERN
# =============================

print("=== Function Toolkit Pattern ===")
print()

# Build reusable functional tools
def pluck(key):
    """Return a function that extracts a key from a dict."""
    return lambda d: d[key]

def where(**conditions):
    """Return a predicate that checks multiple conditions."""
    def check(item):
        return all(item.get(k) == v for k, v in conditions.items())
    return check

def sum_by(key):
    """Return a function that sums a specific key."""
    return lambda items: sum(item[key] for item in items)

# Use the toolkit
orders = [
    {"product": "A", "amount": 100, "status": "shipped"},
    {"product": "B", "amount": 200, "status": "pending"},
    {"product": "C", "amount": 150, "status": "shipped"},
    {"product": "D", "amount": 300, "status": "pending"},
]

# Get names of shipped orders
shipped = list(filter(where(status="shipped"), orders))
shipped_products = list(map(pluck("product"), shipped))
shipped_total = sum_by("amount")(shipped)

print(f"  Shipped products: {shipped_products}")
print(f"  Shipped total: ${shipped_total}")
print()

pending_total = sum_by("amount")(list(filter(where(status="pending"), orders)))
print(f"  Pending total: ${pending_total}")
print()

# =============================
# 7. CHAIN OF RESPONSIBILITY
# =============================

print("=== Chain of Processors ===")
print()

def make_processor(*steps):
    """Create a processor from a chain of functions."""
    def process(data):
        result = data
        for step in steps:
            result = step(result)
        return result
    return process

# Text processing chain
normalize_text = make_processor(
    str.strip,
    str.lower,
    lambda s: " ".join(s.split()),     # normalize spaces
    lambda s: s.replace("  ", " "),    # double spaces
    str.title,
)

messy_texts = [
    "   hello    WORLD   ",
    "  PYTHON   is   GREAT  ",
    "functional   PROGRAMMING  ",
]

for text in messy_texts:
    print(f"  '{text}' → '{normalize_text(text)}'")
print()

# =============================
# 8. FREQUENCY ANALYSIS PATTERN
# =============================

print("=== Frequency Analysis ===")
print()

def frequency(items, key_func=None):
    """Count frequency of items (or key applied to items)."""
    counts = defaultdict(int)
    for item in items:
        key = key_func(item) if key_func else item
        counts[key] += 1
    return dict(sorted(counts.items(), key=lambda x: -x[1]))

text = "the quick brown fox jumps over the lazy dog the fox the dog"
word_freq = frequency(text.split())

print(f"  Text: '{text}'")
print("  Word frequencies:")
for word, count in word_freq.items():
    bar = "█" * count
    print(f"    {word:6} {count} {bar}")
print()

# Character frequency (excluding spaces)
char_freq = frequency(text.replace(" ", ""))
print("  Top 5 characters:")
for char, count in list(char_freq.items())[:5]:
    print(f"    '{char}': {count}")
print()

# =============================
# 9. PUTTING IT ALL TOGETHER
# =============================

print("=== Full Example: Sales Dashboard ===")
print()

sales_data = [
    {"date": "2024-01", "product": "Widget", "amount": 1200, "region": "North"},
    {"date": "2024-01", "product": "Gadget", "amount": 800, "region": "South"},
    {"date": "2024-02", "product": "Widget", "amount": 1500, "region": "North"},
    {"date": "2024-02", "product": "Gadget", "amount": 900, "region": "South"},
    {"date": "2024-02", "product": "Widget", "amount": 600, "region": "South"},
    {"date": "2024-03", "product": "Gadget", "amount": 1100, "region": "North"},
    {"date": "2024-03", "product": "Widget", "amount": 1800, "region": "North"},
    {"date": "2024-03", "product": "Gadget", "amount": 700, "region": "South"},
]

# Monthly totals (group + aggregate)
by_month = group_by(sales_data, pluck("date"))
print("  Monthly Revenue:")
for month, sales in sorted(by_month.items()):
    total = sum_by("amount")(sales)
    print(f"    {month}: ${total:,}")
print()

# Product comparison
by_product = group_by(sales_data, pluck("product"))
print("  Product Totals:")
for product, sales in sorted(by_product.items()):
    total = sum_by("amount")(sales)
    avg = total / len(sales)
    print(f"    {product}: ${total:,} total, ${avg:,.0f} avg")
print()

# Regional breakdown
by_region = group_by(sales_data, pluck("region"))
print("  Regional Breakdown:")
for region, sales in sorted(by_region.items()):
    total = sum_by("amount")(sales)
    products = list(set(map(pluck("product"), sales)))
    print(f"    {region}: ${total:,} ({', '.join(products)})")
print()

# Top sale
top_sale = max(sales_data, key=pluck("amount"))
print(f"  Top sale: {top_sale['product']} in {top_sale['region']}"
      f" ({top_sale['date']}) — ${top_sale['amount']:,}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Build a data pipeline for processing log entries:
#    parse → filter errors → group by hour → count
# 2. Create a report generator using group_by and sum_by
# 3. Build a frequency analyzer for any type of data
# ============================================
