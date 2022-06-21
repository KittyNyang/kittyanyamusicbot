import time
import discord
from discord.ext import commands
from musicbot import LOGGER, BOT_NAME_TAG_VER, color_code

class Ping (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot

    @commands.command (name = 'ping', aliases = ['핑'])
    async def ping(self, ctx):
        latancy = self.bot.latency
        before = time.monotonic()
        embed=discord.Embed(title="**키티서버(샤드) 핑**", description=f':ping_pong: 퐁냥! 웹소켓 핑 {round(latancy * 1000)}ms\n:ping_pong: 퐁냥! 측정중...', color=color_code)
        embed.set_footer(text=BOT_NAME_TAG_VER)
        message = await ctx.send(embed=embed)
        ping = (time.monotonic() - before) * 1000
        embed=discord.Embed(title="**키티서버(샤드) 핑테스트**", description=f':ping_pong: 퐁냥! 웹소켓 핑 상태: {round(latancy * 1000)}ms\n:ping_pong: 퐁냥! 메시지 핑 상태: {int(ping)}ms', color=color_code)
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await message.edit(embed=embed)

def setup (bot) :
    bot.add_cog (Ping (bot))
    LOGGER.info('Ping loaded!')
