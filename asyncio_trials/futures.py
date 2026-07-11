import time
import asyncio


async def future_result_setter(future, n):
    print("future_result_setter has started")
    await asyncio.sleep(3)
    future.set_result(n**2)

    await asyncio.sleep(3)
    print("future_result_setter is done")


async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    asyncio.create_task(future_result_setter(future, 5))

    result = await future

    print(f"Produced future value: {result}")


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"total time: {round(end-start, 2)} seconds")
