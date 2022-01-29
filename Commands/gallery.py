import nextcord
from nextcord.ext import commands
import asyncio
import json
#dynamic gallery
#now you no need to add each embed for every new image
#its all would be done on its own plus images can be added via a discord command find on another pull request at "addimage.py"
class Gallery(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def gallery(self,ctx):
        with open('gallery.json') as g:
            urls=json.load(g)['links']

        #save below commented dict to root of this repo as gallery.json
        '''

{"links": ["https://cdn.discordapp.com/attachments/903715176082202724/922553994583355492/ets2_20211220_211338_00.png", "https://cdn.discordapp.com/attachments/921763147143053332/922572585986822235/ats_20211219_181530_00.png", "https://cdn.discordapp.com/attachments/921763147143053332/922572620535320626/ats_20211219_183529_00.png", "https://cdn.discordapp.com/attachments/921763147143053332/922572691603615744/ets2_20211219_141137_00.png", "https://cdn.discordapp.com/attachments/921763147143053332/922572799720161280/ets2_20211214_155059_00.png", "https://cdn.discordapp.com/attachments/903715176082202724/934742406207787008/270880_20220123172246_1.png", "https://cdn.discordapp.com/attachments/903715176082202724/934657283361734676/ats_20220122_225347_00.png", "https://cdn.discordapp.com/attachments/904347958173122571/934769920556826664/uwu.png"]}
'''
        embed1 = nextcord.Embed(colour=nextcord.Color.random())
        embed1.set_image(url=urls[0])
        embed1.set_author(name="Excell Express Photo Gallery",icon_url=ctx.guild.icon)
        
        #no need to make 100 variables 
        async def emm(cur_page,message):
            embed=nextcord.Embed(colour=nextcord.Color.burple())
            embed.set_image(url=urls[cur_page-1])
            embed.set_author(name="Excell Express Photo Gallery",icon_url=ctx.guild.icon)
            await message.edit(content=f"Page {cur_page}/{pages}\n",embed=embed)
            await message.remove_reaction(reaction, user)

        #all dynamic
        pages = len(urls)
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

                if str(reaction.emoji) == "▶️" and cur_page != pages and cur_page<pages:
                    cur_page += 1
                    await emm(cur_page,message)
                    
                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await emm(cur_page,message) 
                    
                else:
                    await message.remove_reaction(reaction, user)
                    # removes reactions if the user tries to go forward on the last page or
                    # backwards on the first page
            except asyncio.TimeoutError:
                pass

def setup(Bot):
    Bot.add_cog(Gallery(Bot))
