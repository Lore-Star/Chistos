import discord
from discord.ext import commands
from config import token


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='c!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def pe(ctx, count_heh = 5):
    await ctx.send("pe" * count_heh)

bot.run(token)