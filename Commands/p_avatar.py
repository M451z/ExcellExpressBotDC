import nextcord
from nextcord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(name="avatar", help="Shows the avatar.")
    async def avatar(self, ctx, *,  member : nextcord.Member=None):
        if member is None:
            member = ctx.message.author
        avatar = member.avatar
        embed = nextcord.Embed(colour=nextcord.Color.blurple())
        embed.set_author(name=f"Avatar for {member}",icon_url=avatar)
        embed.set_image(url=avatar)
        embed.set_footer(text=f"Requested by {ctx.message.author}",icon_url=ctx.message.author.avatar)
        await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Avatar(Bot))