import nextcord
from nextcord.ext import commands
import requests

class Leaderboard(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def leaderboard(self,ctx):
        url = "https://api.vtlog.net/v3/companies/11543/leaderboards/profit"
        req = requests.get(url=url)
        json = req.json()
        u1 = json["response"][0]
        u1Name = u1["username"]
        u1profit = u1["profit"]
        u1Id = u1["steam_id"]
        u2 = json["response"][1]
        u2Name = u2["username"]
        u2profit = u2["profit"]
        u2Id = u2["steam_id"]
        u3 = json["response"][2]
        u3Name = u3["username"]
        u3profit = u3["profit"]
        u3Id = u3["steam_id"]
        u4 = json["response"][3]
        u4Name = u4["username"]
        u4profit = u4["profit"]
        u4Id = u4["steam_id"]
        u5 = json["response"][4]
        u5Name = u5["username"]
        u5profit = u5["profit"]
        u5Id = u5["steam_id"]
        embed = nextcord.Embed(title="Leaderboard",description=f"`1.` 🥇 **[{u1Name}](https://steamcommunity.com/profiles/{u1Id})** - €{u1profit}\n`2.` 🥈 **[{u2Name}](https://steamcommunity.com/profiles/{u2Id})** - €{u2profit}\n`3.` 🥉 **[{u3Name}](https://steamcommunity.com/profiles/{u3Id})** - €{u3profit}\n\n`4.` **[{u4Name}](https://steamcommunity.com/profiles/{u4Id})** - €{u4profit}\n`5.` **[{u5Name}](https://steamcommunity.com/profiles/{u5Id})** - €{u5profit}",colour=nextcord.Color.blurple())
        embed.set_author(name="Excell Express",icon_url=ctx.guild.icon,url="https://11543.vtlog.net/")
        embed.set_footer(text="Earn money by completing jobs to take place on leaderboard!")
        await ctx.send(embed=embed)


def setup(Bot):
    Bot.add_cog(Leaderboard(Bot))