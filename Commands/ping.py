import nextcord
from nextcord.ext import commands

class Ping(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def ping(self,ctx):
        ping = round(self.Bot.latency * 1000)
        if ping > 70:
            ping= f"<:no:923454493998350366> {ping}ms"
        else:
            ping= f"<:yes:923454526348996608> {ping}ms"
        embed = nextcord.Embed(title="Pong!", description=f"**{ping}**", colour=nextcord.Color.blurple())
        await ctx.reply(embed=embed)

def setup(Bot):
    Bot.add_cog(Ping(Bot))