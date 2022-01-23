import nextcord
from nextcord.ext import commands

class Team(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def team(self,ctx):
        embed = nextcord.Embed(colour=nextcord.Color.blurple())
        embed.set_author(name="Excell Express Team",icon_url=ctx.guild.icon)
        embed.add_field(name="Management",value="<@724389652957495386>, <@413308019364069376>")
        embed.add_field(name="Staff",value="<@453613270725558292>",inline=False)
        embed.add_field(name="Driver",value="<@677124887684317196>, <@135073442146942976>, <@611830505738076170>",inline=False)
        await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Team(Bot))