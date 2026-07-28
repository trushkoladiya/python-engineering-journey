# Advanced Generator Features

Generators have three advanced methods: `send()`, `close()`, and `throw()`. These allow two-way communication with a running generator.

## `send()` — Sending Values INTO a Generator

The `send()` method lets you send a value back into the generator. The value becomes the result of the `yield` expression:

```python
def echo():
    while True:
        received = yield     # yield can RECEIVE a value
        print(f"Got: {received}")

gen = echo()
next(gen)             # start the generator (must call next first!)
gen.send("hello")     # Got: hello
gen.send("world")     # Got: world
```

## `close()` — Stopping a Generator

Terminates the generator. Raises `GeneratorExit` inside it:

```python
def counter():
    n = 0
    while True:
        yield n
        n += 1

gen = counter()
print(next(gen))   # 0
print(next(gen))   # 1
gen.close()        # generator is now done
```

## `throw()` — Throwing Exceptions

Raises an exception at the point where the generator is paused:

```python
gen = counter()
next(gen)
gen.throw(ValueError, "Something went wrong")
```

## Key Points

- `send(value)` — sends a value into the generator via `yield`
- `close()` — terminates the generator
- `throw(exception)` — raises an exception inside the generator
- Always call `next()` once before `send()` to start the generator
- These are advanced features — most generators only use `yield` and `next()`
