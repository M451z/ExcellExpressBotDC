import nextcord
from nextcord.ext import commands
import datetime

class Logs(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        logCh = self.Bot.get_channel(920817546503008316)
        embed = nextcord.Embed(title="**Message Deleted**",colour=nextcord.Color.red(),timestamp=datetime.datetime.now())
        embed.add_field(name="Content",value=message.content,inline=False)
        embed.add_field(name="In", value=f"<#{message.channel.id}>")
        embed.add_field(name="By", value=f"<@{message.author.id}>")
        await logCh.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        logCh = self.Bot.get_channel(920817546503008316)
        embed = nextcord.Embed(title="**Message Edited**", colour=nextcord.Color.orange(), timestamp=datetime.datetime.now())
        embed.add_field(name="Before", value=message_before.content)
        embed.add_field(name="After", value=message_after.content,inline=False)
        embed.add_field(name="In", value=f"<#{message_before.channel.id}>")
        embed.add_field(name="By", value=f"<@{message_before.author.id}>")
        if message_before.content != message_after.content and message_before.author.id != 921103358444568606:
            await logCh.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logCh = self.Bot.get_channel(920817546503008316)
        embed = nextcord.Embed(title=f"**{member} has left the server!**", colour=nextcord.Color.red())
        await logCh.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Logs(Bot))