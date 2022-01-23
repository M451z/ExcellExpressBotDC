import nextcord
from nextcord.ext import commands
import asyncio
import json

class Manage_Gallery(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addimage(self,ctx,*,message):
        '''Add images to Excell Gallery'''
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
    Bot.add_cog(Manage_Gallery(Bot))
