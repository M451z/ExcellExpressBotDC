import nextcord
from nextcord.ext import commands
import json
import os
import random

intents = nextcord.Intents.all()
Bot = commands.Bot(command_prefix="-",intents=intents)

with open("config.json", "r") as f:
    config = json.load(f)

token = config["token"]

@Bot.event
async def on_ready():
    print("I'm Online!")
    await Bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="Excell Express | 6 Drivers"))

@Bot.event
async def on_member_join(member):
    channel = Bot.get_channel(904006198834110504)
    randomMSGs = [f"{member} just slid into the server.", f"{member} joined the party.", f"Everyone welcome {member}!", f"A wild {member} appeared.", f"{member} just showed up!", f"Good to see you, {member}", f"{member} hopped into the server.", f"Glad you're here, {member}.", f"{member} just landed.", f"Welcome {member}. Say hi!", f"Welcome, {member}. We hope you've brought pizza."]
    wMSG = random.choice(randomMSGs)
    PublicRole = nextcord.utils.get(member.guild.roles, name="Public")
    await member.add_roles(PublicRole)
    embed = nextcord.Embed(title=f"<a:blobWave:936374831472054382> {wMSG}",colour=nextcord.Colour.green())
    await channel.send(embed=embed)

for file in os.listdir("./Commands"):
    if file.endswith(".py"):
        Bot.load_extension(f'Commands.{file[:-3]}')

Bot.run(token)