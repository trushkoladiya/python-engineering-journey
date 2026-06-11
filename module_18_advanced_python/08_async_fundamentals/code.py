# ============================================
# MODULE 18 - SUBTOPIC 8: Async Fundamentals
# ============================================

# Async programming runs I/O tasks concurrently on a single thread.
# Uses async/await syntax and the asyncio event loop.

import asyncio
import time

# =============================
# 1. BASIC COROUTINE
# =============================

async def say_hello(name):
    """A simple coroutine."""
    print(f"  Hello, {name}!")

# Run a single coroutine
print("=== Basic Coroutine ===")
print()
asyncio.run(say_hello("World"))
print()

# =============================
# 2. AWAIT — NON-BLOCKING WAIT
# =============================

async def delayed_greeting(name, delay):
    """Wait without blocking other tasks."""
    print(f"  {name}: starting (will wait {delay}s)")
    await asyncio.sleep(delay)  # Non-blocking sleep
    print(f"  {name}: done!")
    return f"{name} complete"

async def demo_await():
    print("=== await Demo ===")
    print()
    result = await delayed_greeting("Task", 0.5)
    print(f"  Result: {result}")
    print()

asyncio.run(demo_await())

# =============================
# 3. CONCURRENT WITH gather()
# =============================

async def demo_gather():
    print("=== Concurrent with gather() ===")
    print()

    start = time.time()

    # These run CONCURRENTLY (not one after another)
    results = await asyncio.gather(
        delayed_greeting("Task-A", 0.3),
        delayed_greeting("Task-B", 0.2),
        delayed_greeting("Task-C", 0.4),
    )

    elapsed = time.time() - start
    print(f"  All results: {results}")
    print(f"  Total time: {elapsed:.3f}s (not 0.9s!)")
    print()

asyncio.run(demo_gather())

# =============================
# 4. SEQUENTIAL vs CONCURRENT
# =============================

async def fetch_data(name, seconds):
    """Simulate fetching data from a server."""
    await asyncio.sleep(seconds)
    return f"{name}: {seconds}s of data"

async def demo_sequential_vs_concurrent():
    print("=== Sequential vs Concurrent ===")
    print()

    # Sequential — one at a time
    start = time.time()
    r1 = await fetch_data("DB", 0.3)
    r2 = await fetch_data("API", 0.2)
    r3 = await fetch_data("Cache", 0.1)
    seq_time = time.time() - start
    print(f"  Sequential: {seq_time:.3f}s")
    print(f"    Results: [{r1}, {r2}, {r3}]")
    print()

    # Concurrent — all at once
    start = time.time()
    results = await asyncio.gather(
        fetch_data("DB", 0.3),
        fetch_data("API", 0.2),
        fetch_data("Cache", 0.1),
    )
    conc_time = time.time() - start
    print(f"  Concurrent: {conc_time:.3f}s")
    print(f"    Results: {results}")
    print(f"  Speedup: {seq_time / conc_time:.1f}x")
    print()

asyncio.run(demo_sequential_vs_concurrent())

# =============================
# 5. create_task() — SCHEDULE TASKS
# =============================

async def demo_create_task():
    print("=== create_task() ===")
    print()

    async def background_work(name, delay):
        await asyncio.sleep(delay)
        return f"{name} result"

    # Create tasks — they start running immediately
    task1 = asyncio.create_task(background_work("Download", 0.3))
    task2 = asyncio.create_task(background_work("Process", 0.2))

    print("  Tasks created and running...")

    # Do other work while tasks run
    print("  Doing other work...")
    await asyncio.sleep(0.1)
    print("  Other work done.")

    # Now collect results
    result1 = await task1
    result2 = await task2
    print(f"  Task results: {result1}, {result2}")
    print()

asyncio.run(demo_create_task())

# =============================
# 6. ASYNC FOR AND ASYNC GENERATORS
# =============================

async def demo_async_generator():
    print("=== Async Generator ===")
    print()

    async def countdown(n):
        """An async generator that yields with delays."""
        for i in range(n, 0, -1):
            await asyncio.sleep(0.1)
            yield i

    async for number in countdown(5):
        print(f"  {number}...")
    print("  Liftoff!")
    print()

asyncio.run(demo_async_generator())

# =============================
# 7. HANDLING EXCEPTIONS IN ASYNC
# =============================

async def demo_async_exceptions():
    print("=== Async Exception Handling ===")
    print()

    async def might_fail(name, should_fail):
        await asyncio.sleep(0.1)
        if should_fail:
            raise ValueError(f"{name} failed!")
        return f"{name} succeeded"

    # Using try/except with await
    try:
        result = await might_fail("Task-1", should_fail=True)
    except ValueError as e:
        print(f"  Caught: {e}")

    # gather with return_exceptions=True
    results = await asyncio.gather(
        might_fail("Task-A", False),
        might_fail("Task-B", True),
        might_fail("Task-C", False),
        return_exceptions=True  # Don't crash, return exceptions
    )

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"  Task {i}: ERROR — {result}")
        else:
            print(f"  Task {i}: {result}")
    print()

asyncio.run(demo_async_exceptions())

# =============================
# 8. TIMEOUTS WITH wait_for()
# =============================

async def demo_timeout():
    print("=== Timeouts ===")
    print()

    async def slow_task():
        await asyncio.sleep(5)
        return "finally done"

    try:
        result = await asyncio.wait_for(slow_task(), timeout=0.5)
        print(f"  Result: {result}")
    except asyncio.TimeoutError:
        print("  Task timed out after 0.5s!")
    print()

asyncio.run(demo_timeout())

# =============================
# 9. PRACTICAL: SIMULATED WEB SCRAPER
# =============================

async def demo_web_scraper():
    print("=== Practical: Simulated Web Scraper ===")
    print()

    async def fetch_page(url, delay):
        """Simulate fetching a web page."""
        print(f"  Fetching {url}...")
        await asyncio.sleep(delay)
        content_length = len(url) * 100  # Fake content
        print(f"  ✓ Got {url} ({content_length} bytes)")
        return {"url": url, "size": content_length}

    urls = [
        ("example.com/page1", 0.3),
        ("example.com/page2", 0.2),
        ("example.com/page3", 0.4),
        ("example.com/page4", 0.1),
        ("example.com/page5", 0.3),
    ]

    start = time.time()
    results = await asyncio.gather(
        *[fetch_page(url, delay) for url, delay in urls]
    )
    elapsed = time.time() - start

    total_bytes = sum(r["size"] for r in results)
    print(f"\n  Fetched {len(results)} pages, {total_bytes} bytes total")
    print(f"  Time: {elapsed:.3f}s (sequential would be ~{sum(d for _, d in urls):.1f}s)")
    print()

asyncio.run(demo_web_scraper())

# =============================
# 10. ASYNC CONTEXT MANAGER
# =============================

async def demo_async_context():
    print("=== Async Context Manager ===")
    print()

    class AsyncResource:
        async def __aenter__(self):
            print("  Opening resource...")
            await asyncio.sleep(0.1)
            print("  Resource ready")
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print("  Closing resource...")
            await asyncio.sleep(0.1)
            print("  Resource closed")

        async def do_work(self):
            await asyncio.sleep(0.1)
            return "work complete"

    async with AsyncResource() as resource:
        result = await resource.do_work()
        print(f"  Result: {result}")
    print()

asyncio.run(demo_async_context())

# ============================================
# TRY IT YOURSELF:
# 1. Create 10 async tasks that each sleep for
#    a random time, run them concurrently
# 2. Implement a timeout for a slow coroutine
# 3. Build an async pipeline: fetch → process → save
# ============================================
