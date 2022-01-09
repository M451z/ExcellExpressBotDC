import nextcord
from nextcord import activity
from nextcord.ext import commands
import json
import os

Bot = commands.Bot(command_prefix=">")

with open("config.json", "r") as f:
    config = json.load(f)

token = config["token"]

@Bot.event
async def on_ready():
    print("I'm Online!")
    await Bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="Excell Express"))

for file in os.listdir("./Commands"):
    if file.endswith(".py"):
        Bot.load_extension(f'Commands.{file[:-3]}')

Bot.run(token)