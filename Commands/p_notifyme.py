import nextcord
from nextcord.ext import commands

class Notifyme(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(name="notifyme", help="Be notified about everything!")
    async def notifyme(self,ctx):
        user = ctx.message.author
        NotificationsRole = nextcord.utils.get(ctx.guild.roles, name="Notifications")
        reaction = "<a:done:936254064897982464>"
        if NotificationsRole in user.roles:
            await user.remove_roles(NotificationsRole)
            await ctx.message.add_reaction(reaction)
        else:
            await user.add_roles(NotificationsRole)
            await ctx.message.add_reaction(reaction)

def setup(Bot):
    Bot.add_cog(Notifyme(Bot))