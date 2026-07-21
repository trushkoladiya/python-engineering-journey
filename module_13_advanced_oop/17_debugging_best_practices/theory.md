# Debugging & Best Practices

Knowing when **NOT** to use advanced OOP is just as important as knowing how to use it.

## When NOT to Use Advanced OOP

### Don't Use Metaclasses When...
- A decorator or `__init_subclass__` can do the same thing
- You're the only person reading the code and it's simple

### Don't Use Abstract Classes When...
- You only have one implementation
- A simple base class with `NotImplementedError` suffices

### Don't Use Operator Overloading When...
- The operator doesn't make intuitive sense for your class
- It would confuse other developers

### Don't Use `__slots__` When...
- You don't have thousands of instances
- You need dynamic attributes

## Readability vs Cleverness

```python
# Too clever — nobody understands this
class Meta(type):
    def __new__(mcs, name, bases, ns):
        ns = {k: staticmethod(v) if callable(v) else v for k, v in ns.items()}
        return super().__new__(mcs, name, bases, ns)

# Simple and clear — everyone understands this
class MyClass:
    @staticmethod
    def method():
        pass
```

## The Rules

1. **Start simple** — add complexity only when needed
2. **Readability first** — clever code costs more to maintain
3. **One pattern at a time** — don't combine 5 patterns in one class
4. **YAGNI** — You Aren't Gonna Need It (don't add features "just in case")
5. **Test your classes** — if it's hard to test, it's probably too complex

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Deep inheritance (5+ levels) | Use composition |
| God class (does everything) | Split into focused classes |
| Overusing design patterns | Use only when solving a real problem |
| Mutating shared class attributes | Use instance attributes |
| Forgetting `super()` in `__init__` | Always call `super().__init__()` |

## Key Points

- Simple > clever
- Don't use advanced features just because you can
- Ask: "Would a junior developer understand this?"
- Measure before optimizing (don't use `__slots__` without proof)
- Design for readability and maintainability
