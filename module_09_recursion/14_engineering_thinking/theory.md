# Engineering-Level Thinking

Designing recursive solutions is a skill. Here's a systematic approach.

## Problem Breakdown Strategy

When you see a problem, ask:
1. **What's the smallest version?** → That's your base case
2. **If I had the answer for a smaller input, how do I build the full answer?** → That's your recursive case
3. **What gets smaller each call?** → That's your progress toward base case

## Identifying Recursive Structure

Look for these patterns in problems:
- **"Find all..."** → likely backtracking
- **"Nested..."** → likely tree recursion
- **"Divide into parts..."** → likely divide and conquer
- **"Build up from smaller..."** → likely linear recursion

## The Recursive Template

```python
def solve(problem):
    # 1. Base case — simplest version
    if problem is trivial:
        return trivial answer

    # 2. Break down
    smaller = make_smaller(problem)

    # 3. Recursive solve
    sub_answer = solve(smaller)

    # 4. Combine
    return combine(problem, sub_answer)
```

## Key Points

- Start with the base case — what's the simplest input?
- Trust the recursion — assume the recursive call works correctly
- Focus on ONE level — don't try to trace the whole thing
- Test with small inputs before scaling up
