from .logger import doge


async def setup(bot):
    cog = doge(bot)
    await cog.refresh_levels()
    bot.add_cog(cog)