import time
import asyncio
from helpers import task_fn


async def main():
    start = time.perf_counter()
    print("Start of main")
    task1 = asyncio.create_task(task_fn(1))
    task2 = asyncio.create_task(task_fn(2))
    task3 = asyncio.create_task(task_fn(3))
    # * Moment it waits on One task it moves to next one
    result1 = await task1
    result2 = await task2
    result3 = await task3

    # * Task 4 will wait for top-3 tasks to finish
    task4 = asyncio.create_task(task_fn(4))
    result4 = await task4

    print(f"received task1: {result1}")
    print(f"received task2: {result2}")
    print(f"received task2: {result3}")
    print(f"received task2: {result4}")
    print("End of main")
    end = time.perf_counter()
    print(f"total time: {round(end-start, 2)} seconds")


asyncio.run(main())
