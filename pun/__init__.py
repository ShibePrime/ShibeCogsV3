from .pun import pun


async def setup(bot):
    cog = pun(bot)
    bot.add_cog(cog)