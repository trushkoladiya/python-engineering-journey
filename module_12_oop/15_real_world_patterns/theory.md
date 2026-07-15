# Real-World Patterns (Engineering Thinking)

This subtopic brings everything together. You'll see how OOP is used to **model real-world systems** with clean, practical code.

## Modeling Real-World Entities

Every real-world concept can be modeled as a class:

- A **User** has a name, email, and can log in
- A **Product** has a name, price, and quantity
- An **Order** has items, a total, and a status

The key is deciding:
- What **data** does this entity hold? → attributes
- What **actions** can it perform? → methods
- How does it **relate** to other entities? → relationships

## Data Models Using Classes

Instead of scattered dictionaries, use classes to enforce structure:

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self):
        return self.stock > 0

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False
```

## Object Interaction Design

Objects work **together** — one object calls methods on another:

```python
class Cart:
    def __init__(self):
        self.items = []

    def add(self, product, qty):
        product.sell(qty)          # Cart interacts with Product
        self.items.append((product, qty))
```

## Think in Objects

When designing a system, ask:
1. **What are the nouns?** → classes (User, Product, Order)
2. **What are the verbs?** → methods (login, purchase, ship)
3. **What are the relationships?** → composition, aggregation
4. **What data does each noun hold?** → attributes

## Key Points

- Model real-world things as classes with data + behavior
- Objects interact by calling each other's methods
- Use composition to build complex systems from simple parts
- Think: nouns → classes, verbs → methods, has-a → composition
- Start simple, add complexity only when needed
