from .pollen import pollen


async def setup(bot):
    cog = pollen(bot)
    bot.add_cog(cog)