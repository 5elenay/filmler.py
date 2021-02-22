import aiohttp
__api__ = "https://api.filmler.fun/api/"

class FilmlerPy(object):
    class api:
        async def Al(uri):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{__api__}{uri.replace(' ', '+')}") as res:
                    return await res.json()

class Wrapper(object):
    class random:
        async def Film():
            return await FilmlerPy().api.Al("rastgele/film")

        async def Dizi():
            return await FilmlerPy().api.Al("rastgele/dizi")

        async def Soz():
            return await FilmlerPy().api.Al("soz/rastgele")

    class soz:
        async def Tur(deger: str = "film"])):
            return await FilmlerPy().api.Al(f"soz/tur/{deger}")

        async def Ad(deger: str = "matrix"):
            return await FilmlerPy().api.Al(f"soz/ad/{deger}")

    async def Ara(self, deger: str):
        return await FilmlerPy().api.Al(f"ara/{deger}")

    async def Trend(self):
        result = await FilmlerPy().api.Al("trend")
        return result["trend"].split(",")
