import asyncio
from wrapper import Wrapper

async def main():
    random = Wrapper().Random()
    print(await random.Dizi())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())