import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')
val: discord.Member


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$What should I play?'):
        await message.channel.send('Doomsday.')

    if message.content.startswith('$MBT'):
        await message.channel.send('...is unplayable.')

    #if message.content.startswith({bot.user}):
     #   await message.channel.sent('Why are you talking to a computer???')

@bot.command(pass_context=True)
async def test(ctx, ):
    await channel.send('This is a test to see if  I respond to a "command"')

@bot.command(pass_context=True)
async def ch(ctx, member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {user.mention} ')


bot.run(TOKEN)
