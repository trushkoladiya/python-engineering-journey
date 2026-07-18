# Duck Typing & Dynamic Typing

Python doesn't care **what type** an object is — it cares **what the object can do**. This is called **duck typing**.

## "If it walks like a duck..."

> "If it walks like a duck and quacks like a duck, then it's a duck."

In Python, you don't check the type — you check if the object has the **methods you need**:

```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

def make_it_quack(thing):
    print(thing.quack())   # works with ANY object that has quack()

make_it_quack(Duck())     # "Quack!"
make_it_quack(Person())   # "I'm quacking like a duck!"
```

No inheritance needed — just compatible **behavior**.

## Duck Typing vs Type Checking

| Approach | Philosophy | Code |
|----------|-----------|------|
| Type checking | "Are you a Duck?" | `isinstance(obj, Duck)` |
| Duck typing | "Can you quack?" | Just call `obj.quack()` |

## Python Uses Duck Typing Everywhere

```python
# len() works with anything that has __len__
len([1, 2, 3])      # list
len("hello")         # string
len({"a": 1})        # dict

# for loop works with anything that has __iter__
for x in [1, 2, 3]: pass    # list
for x in "hello": pass       # string
for x in {1, 2}: pass        # set
```

## EAFP vs LBYL

| Style | Meaning | Approach |
|-------|---------|----------|
| **EAFP** | Easier to Ask Forgiveness than Permission | Try it, catch errors |
| **LBYL** | Look Before You Leap | Check first, then do it |

```python
# EAFP (Pythonic)
try:
    result = obj.quack()
except AttributeError:
    print("Can't quack")

# LBYL (less Pythonic)
if hasattr(obj, "quack"):
    result = obj.quack()
```

Python prefers **EAFP**.

## Key Points

- Duck typing = behavior over type
- If an object has the right methods, it works — no inheritance needed
- Python built-ins use duck typing (`len()`, `for`, `in`, etc.)
- Prefer EAFP (try/except) over LBYL (hasattr checks)
- Duck typing makes code flexible and composable
