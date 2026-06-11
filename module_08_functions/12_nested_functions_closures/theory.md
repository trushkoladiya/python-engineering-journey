# Nested Functions & Closures

You can define functions **inside** other functions. These are called **nested** or **inner** functions.

## Inner Functions

```python
def outer():
    def inner():
        print("I'm inside!")
    inner()   # Call inner from outer

outer()       # Prints: I'm inside!
# inner()    # ❌ Error — inner is not accessible outside
```

Inner functions are **only accessible** inside the outer function.

## Closures

A **closure** is when an inner function **remembers** variables from the outer function, even after the outer function has finished:

```python
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"   # Uses 'greeting' from outer
    return greeter

hello = make_greeter("Hello")
print(hello("Trush"))   # Hello, Trush!
```

The inner function `greeter` "closes over" the variable `greeting`.

## Persistent State

Closures can remember state between calls:

```python
def make_counter():
    count = [0]   # Use list to allow modification
    def counter():
        count[0] += 1
        return count[0]
    return counter

my_counter = make_counter()
print(my_counter())   # 1
print(my_counter())   # 2
print(my_counter())   # 3
```

## Key Points

- Functions can be defined inside other functions
- Inner functions can access variables from the outer function
- A **closure** is an inner function that remembers outer variables
- Closures are useful for creating function factories and maintaining state
