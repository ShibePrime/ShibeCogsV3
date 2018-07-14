from .logger import pun


async def setup(bot):
    cog = pun(bot)
    await cog.refresh_levels()
    bot.add_cog(cog)