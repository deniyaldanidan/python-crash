import asyncio


async def waiter(event):
    print("WAITER: Waiting for event to be set")
    await event.wait()
    # * Below will only run after the event is set
    print("WAITER: Event is SET")


async def setter(event):
    print("SETTER: Setting Event")
    await asyncio.sleep(2)
    event.set()
    print("SETTER: Event has been set")


async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))


if __name__ == "__main__":
    asyncio.run(main())
