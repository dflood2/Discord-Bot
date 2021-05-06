#!/usr/bin/env python3

import discord
import requests
import os
import time
from discord.ext import commands
from decouple import config

TOKEN = config('DISCORD_TOKEN')
client=commands.Bot(command_prefix= '$')

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command(name='hi', help="This command sends a welcome message\n\n Ex. $hi")
async def welcome(ctx):
    response = "Hi there. Sending a warm welcome from the weather bot:) "
    await ctx.send(response)

API_KEY="6e3313543740951245a1a23b5a7d2491"

@client.command(name='weather', help="This command provides the current temperature from an inputted zip code and country code\n\nTwo inputs required: zip code and country code\n\nEx. $weather 22903 us")
async def weather_getter(ctx, zip_code:str, country_code:str):
    url="https://api.openweathermap.org/data/2.5/weather?zip=" +str(zip_code)+","+ str(country_code)+ "&appid=" + API_KEY +"&units=imperial"
    response = requests.get(url)
    current = response.json()['main']['temp']
    done = "The current Temp in the " + str(zip_code) + " zip code is " + str(current) + " degrees Fahrenheit"
    await ctx.send(done)

@client.command(name='go_outside', help="This command tells you whether or not it is warm enough to go outside right now\n\nTwo inputs required: zip code and country code\n\nEx. $go_outside 22903 us")
async def outside(ctx, zip_code:str, country_code:str):
    url="https://api.openweathermap.org/data/2.5/weather?zip=" +str(zip_code)+","+ str(country_code)+ "&appid=" + API_KEY +"&units=imperial"
    response = requests.get(url)
    current = response.json()['main']['temp']
    if (current < 60):
        done= "The weather in the "+str(zip_code)+ " zip code is colder than 60 degrees fahrenheit...you should stay inside today!"
    else:
        done = "The weather in the " + str(zip_code) + " zip code is warmer than 60 degrees fahrenheit...you should go outside today!"
    await ctx.send(done)

@client.command(name='sunset', help="This command tells you what time the sunset is today\n\nTwo inputs required: zip code and country code\n\nEx. $sunset 22903 us")
async def sunset_getter(ctx, zip_code:str, country_code:str):
    url="https://api.openweathermap.org/data/2.5/weather?zip=" +str(zip_code)+","+ str(country_code)+ "&appid=" + API_KEY +"&units=imperial"
    response = requests.get(url)
    sunset = response.json()['sys']['sunset']
    readable = time.ctime(sunset)
    done="The sun will set at approximately..."+ str(readable)
    await ctx.send(done)

@client.command(name='docs', help="provides a summary of my commands")
async def summary_func(ctx):
    done= "Hi, I am the weather bot! I have 6 commands\n\n1. weather (2 parameters)\n2. go_outside (2 parameters)\n3. sunset (2 parameters)\n4. hi (no parameters)\n5. docs (no parameters)\n6. help (1 parameter)\n\nTo use any of these commands type a $ in front of the command (no space) and input any parameters needed with spaces in between each parameter\n\nUse the $help + space + command to receive more detailed instructions on how to use each command\n\nExample: type $help sunset to learn more about that command!\n\nFeel free to check our git hub repo if you have any further questions about me: https://github.com/dflood2/Discord-Bot\n\nEnjoy!"
    await ctx.send(done)

client.run(TOKEN)
