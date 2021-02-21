import asyncio
from wrapper import Wrapper

async def main():
    soz = Wrapper().Soz()
    print(await soz.Tur()) # film/anime/tv

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())