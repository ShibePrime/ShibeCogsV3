from .spellnum import spellnum


async def setup(bot):
    cog = spellnum(bot)
    bot.add_cog(cog)