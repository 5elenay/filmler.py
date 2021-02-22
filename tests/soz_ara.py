import asyncio
from wrapper import Wrapper

async def main():
    wrapper = Wrapper()
    print(await wrapper.soz.Ad("matrix"))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
