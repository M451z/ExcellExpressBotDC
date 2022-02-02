import nextcord
from nextcord.ext import commands
import asyncio
import json

class Gallery(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(name="gallery", help="A gallery that contents the photos taken by Excell Express drivers.")
    async def gallery(self,ctx):
        with open('gallery.json') as g:
            urls=json.load(g)['links']
        
        embed1 = nextcord.Embed(colour=nextcord.Color.blurple())
        embed1.set_image(url=urls[0])
        embed1.set_author(name="Excell Express Photo Gallery",icon_url=ctx.guild.icon)
        
        async def emm(cur_page,message):
            embed=nextcord.Embed(colour=nextcord.Color.blurple())
            embed.set_image(url=urls[cur_page-1])
            embed.set_author(name="Excell Express Photo Gallery",icon_url=ctx.guild.icon)
            await message.edit(content=f"Page {cur_page}/{pages}\n",embed=embed)
            await message.remove_reaction(reaction, user)

        pages = len(urls)
        cur_page = 1
        message = await ctx.send(embed=embed1)

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await self.Bot.wait_for("reaction_add", timeout=60, check=check)

                if str(reaction.emoji) == "▶️" and cur_page != pages and cur_page<pages:
                    cur_page += 1
                    await emm(cur_page,message)
                    
                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await emm(cur_page,message) 
                    
                else:
                    await message.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                pass


    @commands.command(name="addimage", help="Adds image in photo gallery.")
    @commands.has_role("Staff")
    async def addimage(self,ctx,*,message):
        with open('gallery.json','r') as g:
            urls=json.load(g)
        print('adding',message)
        print(urls)
        links=urls['links']
        links.append(message)
        print(links)

        gl={'links':links}
        with open('gallery.json','w') as g:
            json.dump(gl,g)
        print('added',message)
        await ctx.reply(f'{message} has been added to gallery')

def setup(Bot):
    Bot.add_cog(Gallery(Bot))