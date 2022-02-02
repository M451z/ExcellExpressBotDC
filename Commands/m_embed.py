import nextcord
from nextcord.ext import commands
import datetime

class Embed(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(name="Embed", help="Sends an embed.")
    @commands.has_role("Staff")
    async def embed(self,ctx):
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        await ctx.send('1) Waiting for a title')
        title = await self.Bot.wait_for('message', check=check)
    
        await ctx.send('2) Waiting for a description')
        desc = await self.Bot.wait_for('message', check=check)

        embed = nextcord.Embed(title=title.content, description=desc.content, color=nextcord.Colour.blurple(), timestamp=datetime.datetime.now())
        embed.set_footer(text=f"Sent by {ctx.message.author}",icon_url="https://i.imgur.com/IQWI5ID.png")
        await ctx.send(embed=embed)        

def setup(Bot):
    Bot.add_cog(Embed(Bot))