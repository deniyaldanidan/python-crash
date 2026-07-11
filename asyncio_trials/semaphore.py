import time
import asyncio

# * USE SEMAPHORE when you want to restrict how many asynchronous process wants to run at a same time. Let's say you're targeting a web server for scraping 50 web-pages at a same time, If you did the server will block your IP. So limit it to 2 at a time using SEMAPHORE


async def access_semaphore(semaphore, n):
    async with semaphore:
        print(f"Running task {n}")
        await asyncio.sleep(2)
        print(f"Task {n} completed")


async def main():
    semaphore = asyncio.Semaphore(3)  # Allow MAX 3 to run concurrently
    await asyncio.gather(*(access_semaphore(semaphore, i) for i in range(1, 12)))


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(
        f"Total time taken: {round(end-start, 2)} seconds"
    )  # Total will be ceil(11 / 3) = 4 * 2 = 8 seconds
