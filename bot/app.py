# This is the main file of Taur. Our Discord bot written in discord.py
# if you need more information about Taur, you can check the GitHub repository
# https://github.com/PabloCorCon/Taur

import discord
from discord.ext import commands
import colorama
import platform
import json

colorama.init(autoreset=True)

TOKEN = 'NzQ1NTM1NDg2Nzg0ODMxNTA5.XzzMBw.cXYIAvAIX6zskgRwkOzeU_FwYfQ'

bot = commands.Bot(command_prefix='t/')

@bot.event
async def on_ready():

    """
    This function will start once the bot is ready, using the client.event decorator
    and the on_ready() function.
    """
    print(colorama.Fore.LIGHTYELLOW_EX + '· · · · · · · · · TAUR · · · · · · · · ·')
    print('\nBy Pablo Corbalán.')
    print('   Twitter: @pablocorbcon')
    print('   GitHub: @PabloCorbCon')

    # bot log in information
    print('\nLogged in as {}, id: {} | Servers: {} | Users: {}'.format(bot.user.name,
                                                                     bot.user.id,
                                                                     len(bot.guilds),
                                                                     len(set(bot.get_all_members()))) + ' users')

    # bot python information
    print('\nPython version: {} | Discord.py version: {}'.format(platform.python_version(),
                                                               discord.__version__))

    #liks
    invite = 'https://discord.com/oauth2/authorize?client_id=745535486784831509&scope=bot&permissions=268690782'
    print('\nUse this link to invite {}:'.format(bot.user.name))
    print(invite)

    github_repo = 'github.com/PabloCorbCon/Taur'
    print('\nGitHub repository: {}'.format(github_repo))


@bot.command()
async def info(ctx):

    """
    This function will display information about the bot using the
    t/info ccommand, to display an embed message.
    """
    # description of the message
    d = '''
Taur is a Discord bot written with the discord.py library that implements a large number of commands,
although it is still in the early stages of development.
Every week we add at least three new commands to Taur, which are previously tested.

Maybe you need the command **t/commands**, to display the bot commands.
    '''

    # create the discord embed message
    info_embed = discord.Embed(title="Information",
        description=d,
        color=0x0a8f3f)

    # create the embed message
    info_embed=discord.Embed(title="Taur | Information",
        description=open('doc/description.txt').read(),
        color=0x087d1b)
    info_embed.set_author(name="Taur",
        url="https://github.com/PabloCorbCon/Taur")
    info_embed.set_image(url='https://github.com/PabloCorbCon/Taur/blob/master/branding/logo.png?raw=true')
    info_embed.set_footer(text="By Pablo Corbalán | Twitter: @pablocorbcon - GitHub: @PabloCorbCon")

    print('\nTaur has responded to a command (t/info) in {}'.format(ctx))
    
    await ctx.send(embed=info_embed)

bot.run(TOKEN)