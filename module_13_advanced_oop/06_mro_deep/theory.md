# MRO (Method Resolution Order) — Deep Dive

You saw MRO basics in Module 12. Now let's understand **how** Python decides which method to call in complex inheritance hierarchies.

## What is MRO?

When you call a method on an object, Python searches through classes in a specific order. This order is the **Method Resolution Order (MRO)**.

## The C3 Linearization Algorithm

Python uses **C3 linearization** to determine MRO. The rules are:

1. The child class comes **first**
2. Parents are checked in the **order listed**
3. A class only appears once
4. A parent is not checked before all its children

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

# D → B → C → A → object
print(D.__mro__)
```

## The Diamond Problem

When two parents share a common grandparent:

```
      A
     / \
    B   C
     \ /
      D
```

Without C3, `A` could be called **before** `C`, breaking the order. C3 ensures each class appears only once and in the right position.

## Viewing MRO

```python
# Two ways:
print(D.__mro__)         # tuple of classes
print(D.mro())           # list of classes
```

## `super()` Follows MRO

`super()` doesn't just call the parent — it calls the **next class in MRO**:

```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")
        super().method()   # calls next in MRO, not necessarily A

class C(A):
    def method(self):
        print("C")
        super().method()

class D(B, C):
    def method(self):
        print("D")
        super().method()

D().method()  # D → B → C → A (follows MRO!)
```

## Key Points

- MRO = the order Python searches for methods
- Uses **C3 linearization** — consistent and predictable
- Check with `ClassName.__mro__` or `ClassName.mro()`
- `super()` follows MRO, not just the direct parent
- Solves the **diamond problem** by visiting each class exactly once
