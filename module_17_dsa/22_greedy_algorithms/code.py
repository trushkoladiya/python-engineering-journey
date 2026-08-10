# ============================================
# MODULE 17 - SUBTOPIC 22: Greedy Algorithms (Intro)
# ============================================

# Greedy: make the locally optimal choice at each step.
# Fast and simple, but doesn't always give the global optimum.

# =============================
# 1. COIN CHANGE (GREEDY)
# =============================

print("=== Coin Change — Greedy ===")
print()

def greedy_coins(denominations, amount):
    """Make change using fewest coins (greedy approach)."""
    # Sort denominations largest first
    denominations = sorted(denominations, reverse=True)
    coins_used = []

    remaining = amount
    for coin in denominations:
        while remaining >= coin:
            coins_used.append(coin)
            remaining -= coin

    if remaining > 0:
        return None    # can't make exact change
    return coins_used

# Standard US coins — greedy works perfectly
us_coins = [25, 10, 5, 1]
for amount in [67, 30, 99, 41]:
    result = greedy_coins(us_coins, amount)
    print(f"  {amount}¢ → {result} ({len(result)} coins)")
print()

# =============================
# 2. WHEN GREEDY FAILS
# =============================

print("=== When Greedy Fails ===")
print()

# Non-standard coins — greedy gives wrong answer!
weird_coins = [1, 3, 4]
amount = 6

greedy_result = greedy_coins(weird_coins, amount)
print(f"  Coins: {weird_coins}, Amount: {amount}")
print(f"  Greedy: {greedy_result} ({len(greedy_result)} coins)")
print(f"  Optimal: [3, 3] (2 coins)")
print("  → Greedy picked 4, then needed 1+1. Optimal uses 3+3!")
print()

# =============================
# 3. ACTIVITY SELECTION
# =============================

print("=== Activity Selection (Classic Greedy) ===")
print()

def select_activities(activities):
    """
    Select maximum non-overlapping activities.
    Greedy: always pick the activity that ends earliest.
    """
    # Sort by end time
    sorted_acts = sorted(activities, key=lambda x: x[1])

    selected = [sorted_acts[0]]
    last_end = sorted_acts[0][1]

    for start, end, name in sorted_acts[1:]:
        if start >= last_end:
            selected.append((start, end, name))
            last_end = end

    return selected

activities = [
    (1, 4, "Meeting A"),
    (3, 5, "Meeting B"),
    (0, 6, "Meeting C"),
    (5, 7, "Meeting D"),
    (3, 9, "Meeting E"),
    (5, 9, "Meeting F"),
    (6, 10, "Meeting G"),
    (8, 11, "Meeting H"),
    (8, 12, "Meeting I"),
    (2, 14, "Meeting J"),
    (12, 16, "Meeting K"),
]

selected = select_activities(activities)
print("  All activities:")
for start, end, name in sorted(activities):
    marker = " ✓" if (start, end, name) in selected else ""
    bar = "░" * start + "█" * (end - start) + "░" * (16 - end)
    print(f"    {name:12} [{start:2}-{end:2}] {bar}{marker}")
print()
print(f"  Selected {len(selected)} non-overlapping activities:")
for start, end, name in selected:
    print(f"    {name} [{start}-{end}]")
print()

# =============================
# 4. FRACTIONAL KNAPSACK
# =============================

print("=== Fractional Knapsack (Greedy) ===")
print()

def fractional_knapsack(items, capacity):
    """
    Maximize value with fractional items allowed.
    Greedy: take items with highest value/weight ratio first.
    """
    # Sort by value-to-weight ratio (descending)
    sorted_items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    taken = []

    for weight, value, name in sorted_items:
        if capacity >= weight:
            # Take whole item
            capacity -= weight
            total_value += value
            taken.append((name, weight, value, 1.0))
        elif capacity > 0:
            # Take fraction
            fraction = capacity / weight
            total_value += value * fraction
            taken.append((name, capacity, value * fraction, fraction))
            capacity = 0

    return total_value, taken

items = [
    (10, 60, "Gold"),
    (20, 100, "Silver"),
    (30, 120, "Bronze"),
]

capacity = 50
max_value, taken = fractional_knapsack(items, capacity)

print(f"  Items: {[(n, f'w={w}, v={v}') for w, v, n in items]}")
print(f"  Capacity: {capacity}")
print(f"  Taken:")
for name, weight, value, fraction in taken:
    print(f"    {name}: {fraction:.0%} (weight={weight:.0f}, value={value:.0f})")
print(f"  Total value: {max_value:.0f}")
print()

# =============================
# 5. JUMP GAME
# =============================

print("=== Jump Game ===")
print()

def can_jump(nums):
    """
    Can you reach the last index?
    nums[i] = max jump length from position i.
    Greedy: track the farthest position reachable.
    """
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
    return True

test_cases = [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([1, 1, 1, 1, 1], True),
    ([0], True),
]

for nums, expected in test_cases:
    result = can_jump(nums)
    status = "✓" if result == expected else "✗"
    print(f"  {status} {nums} → {'can' if result else 'cannot'} reach end")
print()

# =============================
# 6. ASSIGN COOKIES
# =============================

print("=== Assign Cookies ===")
print()

def assign_cookies(children, cookies):
    """
    Each child has a greed factor. Each cookie has a size.
    A child is satisfied if cookie size >= greed factor.
    Maximize satisfied children.
    """
    children = sorted(children)
    cookies = sorted(cookies)

    child_idx = 0
    cookie_idx = 0
    satisfied = 0

    while child_idx < len(children) and cookie_idx < len(cookies):
        if cookies[cookie_idx] >= children[child_idx]:
            satisfied += 1
            child_idx += 1
        cookie_idx += 1

    return satisfied

children_greed = [1, 2, 3, 4, 5]
cookie_sizes = [1, 1, 3, 5, 7]

result = assign_cookies(children_greed, cookie_sizes)
print(f"  Children's greed: {children_greed}")
print(f"  Cookie sizes: {cookie_sizes}")
print(f"  Satisfied children: {result}")
print()

# =============================
# 7. GREEDY SUMMARY
# =============================

print("=== When to Use Greedy ===")
print()

problems = [
    ("Activity Selection", "✓ Greedy", "Pick earliest finish"),
    ("Fractional Knapsack", "✓ Greedy", "Pick best value/weight"),
    ("0/1 Knapsack", "✗ Need DP", "Can't take fractions"),
    ("Coin Change (std)", "✓ Greedy", "Pick largest coin"),
    ("Coin Change (any)", "✗ Need DP", "Greedy may miss optimal"),
    ("Jump Game", "✓ Greedy", "Track farthest reach"),
]

for problem, approach, reason in problems:
    print(f"  {problem:22} → {approach:10} | {reason}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Implement a scheduling algorithm: given tasks
#    with deadlines and profits, maximize profit
# 2. Find minimum number of platforms needed at
#    a train station (given arrival/departure times)
# 3. Implement Huffman coding (character encoding
#    using a greedy approach)
# ============================================
