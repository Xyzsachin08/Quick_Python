import asyncio

async def task():
    await asyncio.sleep(1)
    print("done")

async def main():
    await task()

asyncio.run(main())