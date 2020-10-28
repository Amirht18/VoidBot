import discord
import os
from dotenv import load_dotenv
# from MrDestructoid import keep_alive
from discord.ext import commands

load_dotenv()
client = discord.Client()
# env = os.environ
bot = commands.Bot(command_prefix="!")
TOKEN=os.getenv("DISCORD_TOKEN")
GUILD=os.getenv('DISCORD_GUILD')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(guild)
    print("bot btw haHAA")
    # print(bot.name,guild.id)
    print(bot.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content == 'ping':
            await message.channel.send('ping')

        elif message.content == 'forsenLookingAtYou':
            await message.channel.send('forsenOkay')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')

@bot.command(help='no,i don\'t think so')
async def ping(ctx):
    await ctx.send('forsenSmug')

# keep_alive()
# client.run(TOKEN)
bot.run(TOKEN)

