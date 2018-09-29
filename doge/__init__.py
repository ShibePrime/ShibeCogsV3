from .doge import doge


async def setup(bot):
    cog = doge(bot)
    bot.add_cog(cog)