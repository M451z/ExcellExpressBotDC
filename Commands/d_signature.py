import nextcord
from nextcord.ext import commands
import requests
from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageChops
import urllib.request
from datetime import datetime

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

    @commands.command(name="signature", help="Shows the driver information.")
    async def signature(self,ctx,steamID=None):
        drivers = ["76561198292480805", "76561198374248155", "76561198967414285", "76561198880376950", "76561199040156215", "76561198349129563"]
        rookieDrivers = ["76561198967414285", "76561198880376950"]
        if steamID is None:
            await ctx.reply("Provide a steam ID!")
        elif not steamID in drivers:
            await ctx.reply("Only **Excell Express Drivers** have signatures!")
        else:
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
            
            if steamID in rookieDrivers:
                rank = "Rookie Driver"
            else:
                rank = "Trainee Driver"

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

            
            


def setup(Bot):
    Bot.add_cog(Signature(Bot))