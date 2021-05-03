import discord
from discord.ext import commands

client=commands.Bot(command_prefix= '$')

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command(name='hi')
async def welcome(ctx):
    response = "Hi there. Sending a warm welcome from the weather bot:) "
    await ctx.send(response)

API_KEY="6e3313543740951245a1a23b5a7d2491"

@client.command(name='we')
async def weather_getter(ctx, zip_code:str, country_code:str)
    url="https://api.openweathermap.org/data/2.5/weather?zip=" +str(zip_code)+
    ","+ str(country_code)+ "&appid=" + API_KEY +"&units="
    response=requests.get(url)
    current=response.json()['main']['temp']
    done="Current Temp in the "+str(zip_code) +" zip code is " +current
    await ctx.send(done)



client.run('ODM4ODA2MDgwOTY0Mzk1MDI4.YJAdCQ.sVRy9lZQLNFgI5MLmJcxWUQ8Scg')