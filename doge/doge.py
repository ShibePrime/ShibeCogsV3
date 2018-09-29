# noinspection PyUnresolvedReferences
import discord
import random
from discord.ext import commands
from redbot.core import Config
from redbot.core.utils import chat_formatting

__author__ = "shibe "


class doge:
    """ShibeBot's Commands"""

    def __init__(self, bot):
        self.bot = bot
        self.base = 'data/doge/'

    # --Start Much E-sports Image embeds , Images go in /data/images/

    # --END Image embeds

    @commands.command(pass_context=True, no_pm=True, aliases=["suhdude"])
    async def suh(self, ctx):
        """suh dude"""
        await self.bot.delete_message(ctx.message)
        await self.bot.say(":v: SUH DUDE :v: ")

    @commands.command(pass_context=True, no_pm=True)
    async def greg(self, ctx):
        """ShibeBot , ATTACK!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.say("ShibeBot growls and attacks Greg's face")

    @commands.command(name="piefact", aliases=["piefacts"])
    async def piefact(self):
        """100 Percent PieFacts"""
        lines = open('{}/piefacts/piefacts.txt'.format(self.base)).read().splitlines()
        piefact = random.choice(lines)
        await self.bot.say(piefact)

    @commands.command()
    async def pecker(self):
        """How-to be safe"""
        lines = open('{}/pecker/pecker.txt'.format(self.base)).read().splitlines()
        pecker = random.choice(lines)
        await self.bot.say(pecker)
