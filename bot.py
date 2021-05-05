

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

@client.command(name='hi')
async def welcome(ctx):
    response = "Hi there. Sending a warm welcome from the weather bot:) "
    await ctx.send(response)

API_KEY="6e3313543740951245a1a23b5a7d2491"

@client.command(name='weather')
async def weather_getter(ctx, zip_code:str, country_code:str):
    url="https://api.openweathermap.org/data/2.5/weather?zip=" +str(zip_code)+","+ str(country_code)+ "&appid=" + API_KEY +"&units=imperial"
    response = requests.get(url)
    current = response.json()['main']['temp']
    done = "The current Temp in the " + str(zip_code) + " zip code is " + str(current) + " degrees Fahrenheit"
    await ctx.send(done)

@client.command(name='go_outside')
async def weather_getter(ctx, zip_code:str, country_code:str):
    url="https://api.openweathermap.org/data/2.5/weather?zip=" +str(zip_code)+","+ str(country_code)+ "&appid=" + API_KEY +"&units=imperial"
    response = requests.get(url)
    current = response.json()['main']['temp']
    if (current < 60):
        done= "The weather in the "+str(zip_code)+ " zip code is colder than 60 degrees fahrenheit...you should stay inside today!"
    else:
        done = "The weather in the " + str(zip_code) + " zip code is warmer than 60 degrees fahrenheit...you should go outside today!"
    await ctx.send(done)

@client.command(name='sunset')
async def weather_getter(ctx, zip_code:str, country_code:str):
    url="https://api.openweathermap.org/data/2.5/weather?zip=" +str(zip_code)+","+ str(country_code)+ "&appid=" + API_KEY +"&units=imperial"
    response = requests.get(url)
    sunset = response.json()['sys']['sunset']
    readable = time.ctime(sunset)
    done="The sun will set at approximately..."+ str(readable)
    await ctx.send(done)

client.run(TOKEN)
