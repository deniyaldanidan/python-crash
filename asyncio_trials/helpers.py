import asyncio


async def task_fn(n):
    print(f"Start of task_fn{n}")
    await asyncio.sleep(3)
    print(f"End of task_fn{n}")
    return f"task_fn with {n} ended"
