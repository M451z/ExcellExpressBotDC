import nextcord
from nextcord.ext import commands
import asyncio

class Gallery(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def gallery(self,ctx):
        urls = ["https://cdn.discordapp.com/attachments/903715176082202724/922553994583355492/ets2_20211220_211338_00.png","https://cdn.discordapp.com/attachments/921763147143053332/922572585986822235/ats_20211219_181530_00.png","https://cdn.discordapp.com/attachments/921763147143053332/922572620535320626/ats_20211219_183529_00.png","https://cdn.discordapp.com/attachments/921763147143053332/922572691603615744/ets2_20211219_141137_00.png","https://cdn.discordapp.com/attachments/921763147143053332/922572799720161280/ets2_20211214_155059_00.png"]
        embed1 = nextcord.Embed(colour=nextcord.Color.blurple())
        embed1.set_image(url=urls[0])
        embed1.set_author(name="Excell Express Photo Gallery",icon_url=ctx.guild.icon)
        embed2 = nextcord.Embed(colour=nextcord.Color.blurple())
        embed2.set_image(url=urls[1])
        embed2.set_author(name="Excell Express Photo Gallery",icon_url=ctx.guild.icon)
        embed3 = nextcord.Embed(colour=nextcord.Color.blurple())
        embed3.set_image(url=urls[2])
        embed3.set_author(name="Excell Express Photo Gallery",icon_url=ctx.guild.icon)
        embed4 = nextcord.Embed(colour=nextcord.Color.blurple())
        embed4.set_image(url=urls[3])
        embed4.set_author(name="Excell Express Photo Gallery",icon_url=ctx.guild.icon)
        embed5 = nextcord.Embed(colour=nextcord.Color.blurple())
        embed5.set_image(url=urls[4])
        embed5.set_author(name="Excell Express Photo Gallery",icon_url=ctx.guild.icon)
        contents = [embed1, embed2, embed3,embed4, embed5]
        pages = 5
        cur_page = 1
        message = await ctx.send(embed=embed1)
        # getting the message object for editing and reacting

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
            # This makes sure nobody except the command sender can interact with the "menu"

        while True:
            try:
                reaction, user = await self.Bot.wait_for("reaction_add", timeout=60, check=check)
                # waiting for a reaction to be added - times out after x seconds, 60 in this
                # example

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(content=f"Page {cur_page}/{pages}\n",embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(content=f"Page {cur_page}/{pages}\n",embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)
                    # removes reactions if the user tries to go forward on the last page or
                    # backwards on the first page
            except asyncio.TimeoutError:
                pass

def setup(Bot):
    Bot.add_cog(Gallery(Bot))