import nextcord
from nextcord.ext import commands
import datetime

class BanUnbanKick(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(name="ban",help="Bans the user.")
    @commands.has_role("Staff")
    async def ban(self, ctx, member: nextcord.Member=None, *, reason=None):
        if member is None:
            await ctx.reply("Who am i going to ban?")
        embed = nextcord.Embed(title=f"{member} has been banned!",colour=nextcord.Colour.red())
        await ctx.channel.send(embed=embed)
        await member.send(f"You have been banned from **Excell Express**.\nReason: {reason}\nModerator: {ctx.message.author}")
        await member.ban(reason=reason)
        await ctx.message.delete()
        logEmbed = nextcord.Embed(title="User Banned",colour=nextcord.Colour.red(),timestamp = datetime.datetime.now())
        logEmbed.add_field(name="User",value=f"{member.mention}({member.id})")
        logEmbed.add_field(name="Moderator",value=f"{ctx.message.author.mention}({ctx.message.author.id})")
        logEmbed.add_field(name="Reason",value=reason,inline=False)
        logchannel = self.Bot.get_channel(920817546503008316)
        await logchannel.send(embed=logEmbed)

    @commands.command(name="unban", help = "Unbans the user.")
    @commands.has_role("Staff")
    async def unban(self,ctx, *, member_id: int = None):
        if member_id is None:
            await ctx.reply("Who am i going to unban?")
        await ctx.guild.unban(nextcord.Object(id=member_id))
        embed = nextcord.Embed(title=f"<@{member_id}> has been unbanned!",colour=nextcord.Colour.blue())
        await ctx.send(embed=embed)
        logEmbed = nextcord.Embed(title="User Unbanned",colour=nextcord.Colour.blue(),timestamp = datetime.datetime.now())
        logEmbed.add_field(name="User",value=f"<@{member_id}>({member_id})")
        logEmbed.add_field(name="Moderator",value=f"{ctx.message.author.mention}({ctx.message.author.id})")
        logchannel = self.Bot.get_channel(920817546503008316)
        await logchannel.send(embed=logEmbed)
        await ctx.message.delete()
    
    @commands.command(name="kick", help="Kicks the user.")
    @commands.has_role("Staff")
    async def kick(self,ctx, member:nextcord.Member=None, *, reason=None):
        await member.send(f"You have been kicked from **Excell Express**.\nReason: {reason}\nModerator: {ctx.message.author}")
        embed = nextcord.Embed(title=f"{member} has been kicked!",colour=nextcord.Color.orange())
        await member.kick()
        await ctx.send(embed=embed)
        await ctx.message.delete()
        logEmbed = nextcord.Embed(title="User Kicked",colour=nextcord.Colour.orange(),timestamp = datetime.datetime.now())
        logEmbed.add_field(name="User",value=f"{member}({member.id})")
        logEmbed.add_field(name="Moderator",value=f"{ctx.message.author.mention}({ctx.message.author.id})")
        logEmbed.add_field(name="Reason",value=reason,inline=False)
        logchannel = self.Bot.get_channel(920817546503008316)
        await logchannel.send(embed = logEmbed)

def setup(Bot):
    Bot.add_cog(BanUnbanKick(Bot))