from .spellnum import spellnum


async def setup(bot):
    cog = spellnum(bot)
    await cog.refresh_levels()
    bot.add_cog(cog)