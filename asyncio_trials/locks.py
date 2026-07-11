import asyncio

shared_resource = 0

# * Lock will locks access to CRITICAL_SHARED_RESOURCE to ONE_AT_A_TIME
lock = asyncio.Lock()


async def modify_shared_resouce():
    global shared_resource
    async with lock:
        print(f"before mod: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(1)
        print(f"after mod: {shared_resource}")


async def main():
    await asyncio.gather(*(modify_shared_resouce() for _ in range(6)))


asyncio.run(main())
