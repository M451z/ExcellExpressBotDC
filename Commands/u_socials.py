import nextcord
from nextcord.ext import commands

class Socials(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(name="socials", help="Shows an embed contents social accounts of Excell Express.")
    @commands.has_role("Upper Management")
    async def socials(self,ctx):
        embed = nextcord.Embed(title="📨 __Socials__",description="<:discord:936264436111527946> - [Discord](https://discord.gg/AeCzzHsXuf)\n<:steam:936264424363270147> - [Steam](https://steamcommunity.com/groups/EEVTC)\n<:instagram:936264069990719488>  - [Instagram](https://www.instagram.com/eevtc69/)\n<:twitter:936264069814558760> - [Twitter](https://twitter.com/ExcellExpressEE)\n<:truckersmp:936264070171086928> - [TruckersMP](https://truckersmp.com/vtc/49974)\n<:vtlog:936268850784264193> - [VTLOG](https://11915.vtlog.net/)\n<:Gmail:938204511518998559> - [Gmail](https://textsaver.flap.tv/lists/4l1n)",colour = nextcord.Color.blurple())
        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(Bot):
    Bot.add_cog(Socials(Bot))