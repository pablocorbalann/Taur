# TAUR
# By Pablo Corbalán
# Twitter: @pablocorbcon
# GitHub: @PabloCorbCon


# This is the main file of Taur. Our Discord bot written in discord.py
# if you need more information about Taur, you can check the GitHub repository
# https://github.com/PabloCorCon/Taur

import discord
from discord.ext import commands
import colorama
import platform

import load
import decorators

colorama.init(autoreset=True)

#colors
yellow = colorama.Fore.LIGHTYELLOW_EX
violet = colorama.Fore.LIGHTMAGENTA_EX

# set the token (const token)
TOKEN = 

# create the bot using the discord.Bot() class
bot = commands.Bot(command_prefix='t/')

@bot.event
async def on_ready():

    """
    This function will start once the bot is ready, using the client.event decorator
    and the on_ready() function. 
    It will display information about the bot itself, the server and the programmer
    """
    print(yellow + '· · · · · · · · · TAUR · · · · · · · · ·')
    print(yellow + '\nBy Pablo Corbalán.')
    print(yellow + '   Twitter: @pablocorbcon')
    print(yellow + '   GitHub: @PabloCorbCon')

    # bot log in information
    print(yellow + '\nLogged in as {}, id: {} | Servers: {} | Users: {}'.format(bot.user.name,
                                                                     bot.user.id,
                                                                     len(bot.guilds),
                                                                     len(set(bot.get_all_members()))) + ' users')

    # bot python information
    print(yellow + '\nPython version: {} | Discord.py version: {}'.format(platform.python_version(),
                                                               discord.__version__))

    #liks
    invite = 'https://discord.com/oauth2/authorize?client_id=745535486784831509&scope=bot&permissions=268690782'
    print(yellow + '\nUse this link to invite {}:'.format(bot.user.name))
    print(invite)

    github_repo = 'github.com/PabloCorbCon/Taur'
    print(yellow + '\nGitHub repository: {}'.format(github_repo))


@bot.command()
async def info(ctx):

    """
    This function will display information about the bot using the
    t/info ccommand, to display an embed message.
    """
    # create the embed message
    info_embed=discord.Embed(title="Taur | Information",
        description=open('doc/description.txt').read(),
        color=0x087d1b)
    info_embed.set_author(name="Taur",
        url="https://github.com/PabloCorbCon/Taur")
    info_embed.set_image(url='https://github.com/PabloCorbCon/Taur/blob/master/branding/logo.png?raw=true')
    info_embed.set_footer(text="By Pablo Corbalán | Twitter: @pablocorbcon - GitHub: @PabloCorbCon")

    print(violet + '\nTaur has responded to a command (t/info) in {}'.format(ctx))
    await ctx.send(embed=info_embed)




@bot.command()
async def command(ctx):

    """
    This function will display information about the bot using the
    t/command ccommand, to display an embed message and it uses other functions
    as load_help_commadns() located in commands.py to load all the data.
    """
    # create the embed message
    commands_embed=discord.Embed(title="Taur | Commands",
        description='**All the commands start with the prefix "t/**".\n' + load.load_help_commands('dic/commands.json', True) + "\n\n",
        color=0x087d1b)
    commands_embed.set_author(name="Taur",
        url="https://github.com/PabloCorbCon/Taur")
    commands_embed.set_footer(text="By Pablo Corbalán | Twitter: @pablocorbcon - GitHub: @PabloCorbCon")

    print(violet + '\nTaur has responded to a command (t/commands) in {}'.format(ctx))
    await ctx.send(embed=commands_embed)




@bot.command()
async def invite(ctx):

    """
    This function will provide a link to invite Taur
    to your own discord server. This link is not provided using
    an embed message
    """

    #create the bot link
    bot_invite_link = 'https://discord.com/oauth2/authorize?client_id=745535486784831509&scope=bot&permissions=268690782'

    print(violet + '\nTaur has responded to a command (t/command) in {}'.format(ctx))
    await ctx.send("You can invite Taur using this link:\n\n{}".format(bot_invite_link))




@bot.command()
async def ping(ctx):

    """
    This function pings the user using the bot.latency attribute.
    This command is called using the "t/ping" string
    """
    await ctx.send('Pong! {}'.format(round(bot.latency, 1)))
    print(violet + '\nTaur has responded to a command (t/ping) in {}'.format(ctx))




#kick command using discord.py
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason='Not defined reason.'):

    """
    This command (t/kick) will kick a member from the discord server
    usign the .kick() method. It recibes two parameters:

        p:user => the user to kick
        reason => the reason to kick the user (d:None)
    """

    await user.kick(reason=reason)
    # create an embed message and inform the server
    message = await ctx.send('Taur has kicked **{0}**.\n\nReason:\n{1}'.format(user, reason))
    print(violet + '\nTaur has responded to a command (t/kick) in {}'.format(ctx))
    add_reactions(message, (':thumbsup:'))

bot.run(TOKEN)