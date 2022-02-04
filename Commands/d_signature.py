#fixed ranking calculation
#improved usage (made easy to use) -signature []/[steam_id]/[discord_id]/[discord_mention]/[disord_name]/[discord_server_nickname]
import nextcord
from nextcord.ext import commands
import requests
from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageChops
import urllib.request
from datetime import datetime
import time
def crop_to_circle(im):
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, im.split()[-1])
    im.putalpha(mask)

class Signature(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot
        self.before = time.monotonic()

    def discord_id(self):
        #fetch from vtlog
        r=requests.get('https://api.vtlog.net/v3/companies/11915/members').json()['response']
        d={}
        
        for i in r['members']:
            if i['discord_id']!='0':
                #d[i['discord_id']]=i['steam_id']
                d[i['steam_id']]=[i['discord_id'],i['username']]
        return d
    
    @commands.command(name="signature", help="Shows the driver information.")
    async def signature(self,ctx,steamID=None): #either author with nothing/ steamid/ discord @451 {ping} is passes
        async with ctx.typing():
            d_ids=Signature(self.Bot).discord_id()
            found=False
            #-signature [my nick name in discord] (find by name or nickname)
            if steamID and found==False:
                for i in d_ids.keys():
                    user=ctx.message.guild.get_member(int(d_ids[i][0])) or None
                    if steamID in d_ids[i][1]:
                        print('found via name or nickname/server_display_name',steamID)
                        if steamID in d_ids[i][1]:print('found via vtlog name')
                        steamID=i
                        found=True
                        break
                    if (user!=None) and ((steamID in str(user)) or (steamID in user.display_name)):
                        steamID=i
                        found=True
                        break
                        
            
            if steamID and found==False: # if -signature {@451 [pinged]} or {876543[discord or steam id is passed]}
                id_=''
                for i in steamID:
                    if i.isdigit(): id_+=i
                for i in d_ids.keys():
                    
                    if id_ == i:
                        steamID=i
                        found=True
                        break
                    elif id_ == d_ids[i][0]:
                        steamID=i
                        found=True
                        break
            
            #-signature #if author is a driver
            if steamID==None and found==False:
                for i in d_ids.keys():
                    if d_ids[i][0]==str(ctx.message.author.id):
                        steamID=i
                        found=True
                        break

            #user found
            if found==True:
                url = f"https://api.vtlog.net/v3/users/{steamID}"
                req = requests.get(url=url)
                json = req.json()
                avatar = json["response"]["avatar"]
                url2 = f"https://api.vtlog.net/v3/users/{steamID}/stats/lifetime"
                req2 = requests.get(url=url2)
                jjson = req2.json()
                job1 = jjson["response"]["eut2"]["singleplayer"]["jobs"]
                job2 = jjson["response"]["eut2"]["truckersmp"]["jobs"]
                job3 = jjson["response"]["ats"]["singleplayer"]["jobs"]
                job4 = jjson["response"]["ats"]["truckersmp"]["jobs"]
                dist1 = jjson["response"]["eut2"]["singleplayer"]["distance"]
                dist2 = jjson["response"]["eut2"]["truckersmp"]["distance"]
                dist3 = jjson["response"]["ats"]["singleplayer"]["distance"]
                dist4 = jjson["response"]["ats"]["truckersmp"]["distance"]
                inc1 = jjson["response"]["eut2"]["singleplayer"]["income"]
                inc2 = jjson["response"]["eut2"]["truckersmp"]["income"]
                inc3 = jjson["response"]["ats"]["singleplayer"]["income"]
                inc4 = jjson["response"]["ats"]["truckersmp"]["income"]
                username = json["response"]["username"]
                ts = json["response"]["created"]
                timestamp = int(f"{ts}")
                created = datetime.utcfromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M:%S')
                totaljobs = job1 + job2 + job3 + job4
                totaldistance = dist1 + dist2 + dist3 + dist4
                totalincome = inc1 + inc2 + inc3 + inc4
                
                if totalincome<10000:
                    rank='Trainee Driver'
                elif totalincome<100000:
                    rank='Advanced Driver'
                elif totalincome<1000000:
                    rank='Experienced Driver'
                elif totalincome<10000000:
                    rank='Veteran Driver'
                else:
                    rank='Legendary Driver'

                av = urllib.request.urlretrieve(f"{avatar}", "avatar.png")

                background = Image.open(".\Images\card.png")
                draw = ImageDraw.Draw(background)
                font = ImageFont.truetype("arial.ttf", 25)
                draw.text((575, 110),f"{username}",(0,0,0),font=font)
                draw.text((620, 166),f"{totaljobs}",(0,0,0),font=font)
                draw.text((642, 195),f"{totaldistance}",(0,0,0),font=font)
                draw.text((670, 224),f"{totalincome}",(0,0,0),font=font)
                draw.text((555, 253),f"{rank}",(0,0,0),font=font)
                draw.text((610, 282),f"{steamID}",(0,0,0),font=font)
                draw.text((590, 310),f"{created}",(0,0,0),font=font)

                avatar = Image.open("avatar.png")
                ra = avatar.resize([270,270])
                crop_to_circle(ra)

                background.paste(ra, (45, 90), ra)

                background.save("result.png")

                await ctx.send(file=nextcord.File('result.png'))
                await ctx.send(embed=nextcord.Embed(title=f'render took {round((time.monotonic() - self.before)/10)}s',colour=nextcord.Color.blurple()),delete_after=4)
            else:
                print('nope')
                await ctx.reply(embed=nextcord.Embed(title="Only **Excell Express Drivers** have signatures!",colour=nextcord.Color.blurple()),delete_after=None)    
                await ctx.send(embed=nextcord.Embed(title='Are you a driver! Still not recognized ?',description='->Make sure you link your discord account with <:vtlog:936268850784264193> - [VTLOG](https://11915.vtlog.net/) website',colour=nextcord.Color.blurple()),delete_after=20)
                
def setup(Bot):
    Bot.add_cog(Signature(Bot))
