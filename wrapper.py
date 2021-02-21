import random
import aiohttp

__api__ = "https://api.filmler.fun/api/"
class Wrapper(object):
    class Random(object):
        async def Film(self):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{__api__}rastgele/film") as res:
                    return await res.json()

        async def Dizi(self):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{__api__}rastgele/dizi") as res:
                    return await res.json()

    class Soz(object):
        async def Tur(self, deger: str = random.choice(["film", "anime", "tv"])):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{__api__}soz/tur/{deger}") as res:
                    return await res.json()

        async def Ad(self, deger: str = "matrix"):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{__api__}soz/ad/{deger}") as res:
                    return await res.json()

        async def Random(self):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{__api__}soz/rastgele") as res:
                    return await res.json()

    async def Ara(self, deger: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{__api__}ara/{deger.replace(' ', '+')}") as res:
                return await res.json()

    async def Trend(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{__api__}trend") as res:
                result = await res.json()
                return result["trend"].split(",")