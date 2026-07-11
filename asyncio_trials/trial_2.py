import asyncio
from helpers import task_fn


async def main():
    print("Start of main")
    # ? Gather is not good with error handling, If one of the tasks failed others just keep moving not gonna stop
    # Below executes both at the sametime
    results = await asyncio.gather(task_fn(1), task_fn(2))
    print(f"received task1: {results[0]}")
    print(f"received task2: {results[1]}")
    print("End of main")


asyncio.run(main())
