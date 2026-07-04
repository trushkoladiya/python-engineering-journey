# ============================================
# MODULE 9 - SUBTOPIC 12: Advanced Recursive Patterns
# ============================================

# =============================
# 1. DIVIDE AND CONQUER — MERGE SORT
# =============================

# --- Example 1: Merge sort ---
def merge_sort(items):
    """Split → Sort halves → Merge."""
    if len(items) <= 1:
        return items
    
    # DIVIDE
    mid = len(items) // 2
    left = merge_sort(items[:mid])     # Sort left half
    right = merge_sort(items[mid:])    # Sort right half
    
    # CONQUER (merge)
    return merge(left, right)

def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

data = [38, 27, 43, 3, 9, 82, 10]
print(f"Merge sort:")
print(f"  Input:  {data}")
print(f"  Sorted: {merge_sort(data)}")

# --- Example 2: Tracing merge sort ---
def merge_sort_trace(items, depth=0):
    indent = "  " * depth
    print(f"{indent}sort({items})")
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort_trace(items[:mid], depth + 1)
    right = merge_sort_trace(items[mid:], depth + 1)
    result = merge(left, right)
    print(f"{indent}→ merged: {result}")
    return result

print(f"\nMerge sort traced:")
merge_sort_trace([4, 2, 7, 1])

# =============================
# 2. DIVIDE AND CONQUER — QUICK SELECT
# =============================

# --- Example 3: Find k-th smallest element ---
def quick_select(items, k):
    """Find the k-th smallest element (0-indexed)."""
    if len(items) == 1:
        return items[0]
    
    pivot = items[len(items) // 2]
    smaller = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    larger = [x for x in items if x > pivot]
    
    if k < len(smaller):
        return quick_select(smaller, k)
    elif k < len(smaller) + len(equal):
        return pivot
    else:
        return quick_select(larger, k - len(smaller) - len(equal))

data = [7, 3, 9, 1, 5, 8, 2]
print(f"\nQuick select from {data}:")
for k in range(len(data)):
    print(f"  {k}th smallest: {quick_select(data, k)}")

# =============================
# 3. TREE-LIKE DATA PROCESSING
# =============================

# --- Example 4: Processing a nested dictionary (like a tree) ---
def process_tree(node, depth=0):
    """Process a tree represented as nested dicts."""
    indent = "  " * depth
    if isinstance(node, dict):
        for key, value in node.items():
            print(f"{indent}{key}:")
            process_tree(value, depth + 1)
    elif isinstance(node, list):
        for item in node:
            process_tree(item, depth + 1)
    else:
        print(f"{indent}→ {node}")

org_chart = {
    "CEO": {
        "CTO": {
            "Dev Lead": ["Trush", "Rahul"],
            "QA Lead": ["Charlie"],
        },
        "CFO": {
            "Accountant": ["Diana"],
        },
    }
}

print(f"\nOrg chart (tree traversal):")
process_tree(org_chart)

# --- Example 5: Count all leaf values in a nested structure ---
def count_leaves(node):
    if isinstance(node, dict):
        return sum(count_leaves(v) for v in node.values())
    elif isinstance(node, list):
        return sum(count_leaves(item) for item in node)
    return 1

print(f"\nTotal employees: {count_leaves(org_chart)}")

# =============================
# 4. DIVIDE AND CONQUER — MAX SUBARRAY SUM
# =============================

# --- Example 6: Maximum crossing subarray ---
def max_crossing_sum(arr, low, mid, high):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, low - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)
    
    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, high + 1):
        total += arr[i]
        right_sum = max(right_sum, total)
    
    return left_sum + right_sum

def max_subarray(arr, low=0, high=None):
    """Find maximum subarray sum using divide and conquer."""
    if high is None: high = len(arr) - 1
    if low == high: return arr[low]
    
    mid = (low + high) // 2
    left_max = max_subarray(arr, low, mid)
    right_max = max_subarray(arr, mid + 1, high)
    cross_max = max_crossing_sum(arr, low, mid, high)
    
    return max(left_max, right_max, cross_max)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"\nMax subarray sum of {arr}:")
print(f"  Result: {max_subarray(arr)}")   # 6 (subarray [4, -1, 2, 1])

# =============================
# 5. RECURSIVE SEARCH IN TREE
# =============================

# --- Example 7: Find a value in a nested structure ---
def find_in_tree(node, target):
    """Search for a value in any nested structure."""
    if node == target:
        return True
    if isinstance(node, dict):
        return any(find_in_tree(v, target) for v in node.values())
    if isinstance(node, list):
        return any(find_in_tree(item, target) for item in node)
    return False

data = {"a": [1, 2, {"b": [3, 4, {"c": 5}]}]}
print(f"\nSearch in nested structure:")
print(f"  Find 5: {find_in_tree(data, 5)}")
print(f"  Find 9: {find_in_tree(data, 9)}")
print(f"  Find 3: {find_in_tree(data, 3)}")

# ============================================
# TRY IT YOURSELF:
# 1. Implement a recursive binary search tree
# 2. Write a function to sum all numbers in a deeply nested structure
# 3. Implement quick sort using divide and conquer
# ============================================
