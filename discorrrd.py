import discord
import random
from discord.ext import commands
from config import token


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='c!', intents=intents)

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return f'{ctx.author} **se papeo a** {argument}'

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def papear(ctx, *, reason: Slapper):
    await ctx.send(reason)

@bot.command()
async def pe(ctx, count_heh = 5):
    await ctx.send("pe" * count_heh)

bot.run(token)