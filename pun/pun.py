import json
import discord
from aiohttp import ClientSession
from discord.ext import commands
from redbot.core import Config
from redbot.core.utils import chat_formatting

url = 'https://pun.andrewmacheret.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}


class pun:
    """Random Puns"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pun", pass_context=True)
    async def pun(self, ctx):
        await self.get_pun()
        """Prints Random Puns"""

    async def get_pun(self, ctx):
        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                onepun = await response.json()
                twopun = onepun["pun"]
                pun = "**" + twopun + "**"
                em = discord.Embed(title='', description=pun, colour=0x6FA8DC, )
                await ctx.send(embed=em)
