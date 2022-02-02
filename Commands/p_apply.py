import nextcord
from nextcord.ext import commands

class Apply(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(name="apply", help="Sends an embed about applying.")
    async def apply(self,ctx):
        embed = nextcord.Embed(title="**Want to join us?**", description="📝 Start filling out the form, by clicking [here](https://docs.google.com/forms/d/e/1FAIpQLSd2vIhcSJTmVT7JjzPYmZbPFU2Cy5NvchwuqzyGYNGB8lN6Vg/viewform).\n🢂 [**Steps**](https://discord.com/channels/903712744358948884/903714400660226108/905173969320181861)\n\n<:truckersmp:936264070171086928> - [TruckersMP Page](https://truckersmp.com/vtc/49974)\n<:vtlog:936268850784264193> - [VTLOG Page](https://11915.vtlog.net/)",colour = nextcord.Color.og_blurple())
        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(Bot):
    Bot.add_cog(Apply(Bot))