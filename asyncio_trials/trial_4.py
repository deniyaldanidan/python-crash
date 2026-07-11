import time
import asyncio
from helpers import task_fn


async def main():
    start = time.perf_counter()
    print("Start of main")

    tasks = []
    # * TaskGroup will fail if anyone of the tasks failed
    async with asyncio.TaskGroup() as tskgrp:
        for i in range(1, 4):
            task = tskgrp.create_task(task_fn(i))
            tasks.append(task)

    print("TaskGroups are done")

    # * Task 4 will wait for top tasks to finish
    task4 = asyncio.create_task(task_fn(4))
    result4 = await task4

    for i, tsk in enumerate(tasks):
        print(f"received task{i}: {tsk.result()}")

    print(f"received task2: {result4}")
    print("End of main")
    end = time.perf_counter()
    print(f"total time: {round(end-start, 2)} seconds")


asyncio.run(main())
