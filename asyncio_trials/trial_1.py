import asyncio
from helpers import task_fn


async def main():
    print("Start of main")
    # * main will wait for task1 to finish before moving to next-line
    task1 = await task_fn(1)
    task2 = await task_fn(2)
    print(f"received task1: {task1}")
    print(f"received task2: {task2}")
    print("End of main")


asyncio.run(main())
