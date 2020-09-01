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
import csv
import random 

import load
import decorators

colorama.init(autoreset=True)

#colors
yellow = colorama.Fore.LIGHTYELLOW_EX
violet = colorama.Fore.LIGHTMAGENTA_EX

# set the token (const token)
TOKEN = 'NzQ1NTM1NDg2Nzg0ODMxNTA5.XzzMBw.U5enxWUI7QXUp1p_iCiURbe7Hy0'

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



@bot.event
async def on_message(message):

    """
    This discord event will read all the new messages in the discord
    server, so if the user wants to use a command but the command does not need
    permisions or parameters; it will be implemented in this event
    """

    # check if the bot is the author of the message
    if message.author == bot.user:
        return

    with open('dic/bad_words.txt') as f:
        bad_words = [line.rstrip() for line in f]
        # moderation of the message
        message_content = message.content.lower()
        for word in message_content.split():
            # check for mod
               if word in bad_words and message.author != bot.user:
                # delete the message 
                await message.delete()
                print(colorama.Fore.LIGHTMAGENTA_EX + 'Taur has deleted the following message:\n {}\nBecause of the word {}\n(from {})'.format(message.content, word, message.author.name))
                # include the message
                await message.channel.send('Be carefull {}, your message includes the word "{}". Please avoid that word.'.format(message.author.name, word))
                # create the embed message to send to the user (private)
                d = '''
Taur found the word {} in your message. 
This word is included in our [list of prohibited words.]() so Taur has deleted your message
Be careful and avoid these words as you could be banned from the server.

Message:
```{}```
                '''.format(word, message.content)
                bad_word_embed=discord.Embed(title="Taur | Moderation",
                    description=d,
                    color=discord.Color.red())
                bad_word_embed.set_author(name="Taur",
                    url="https://github.com/PabloCorbCon/Taur")
                bad_word_embed.set_footer(text="By Pablo Corbalán | Twitter: @pablocorbcon - GitHub: @PabloCorbCon")
                await message.author.send(embed=bad_word_embed)
                print(decorators.responded_to(message.author.name))


    if message.content.startswith('t/info'):
        # send information about the bot
        info_embed=discord.Embed(title="Taur | Information",
            description=open('doc/description.txt').read(),
            color=0x087d1b)
        info_embed.set_author(name="Taur",
            url="https://github.com/PabloCorbCon/Taur")
        info_embed.set_image(url='https://github.com/PabloCorbCon/Taur/blob/master/branding/logo.png?raw=true')
        info_embed.set_footer(text="By Pablo Corbalán | Twitter: @pablocorbcon - GitHub: @PabloCorbCon")

        print(decorators.responded_to('t/info'))
        await message.channel.send(embed=info_embed)


    elif message.content.startswith('t/commands'):
        # create the embed message
        commands_embed=discord.Embed(title="Taur | Commands",
            description='**All the commands start with the prefix "t/**".\n' + load.load_help_commands('dic/commands.json', True) + "\n\n",
            color=0x087d1b)
        commands_embed.set_author(name="Taur",
            url="https://github.com/PabloCorbCon/Taur")
        commands_embed.set_footer(text="By Pablo Corbalán | Twitter: @pablocorbcon - GitHub: @PabloCorbCon")

        print(decorators.responded_to('t/commands'))
        await message.channel.send(embed=commands_embed)


    elif message.content.startswith('t/invite'):
        #create the bot link
        bot_invite_link = 'https://discord.com/oauth2/authorize?client_id=745535486784831509&scope=bot&permissions=268690782'

        print(decorators.responded_to('t/invite'))
        await message.channel.send("You can invite Taur using this link:\n\n{}".format(bot_invite_link))


    elif message.content.startswith('t/ping'):
        await message.channel.send('Pong! {}'.format(round(bot.latency, 1)))
        print(decorators.responded_to('t/ping'))


    elif message.content.startswith('t/members'):

        # get the list of members
        list_of_members = ''
        for member in message.guild.members:
            list_of_members += ' {0} |'.format(member.name)

        # create the embed message
        members_embed=discord.Embed(title="Taur | Members",
            description='{}'.format(list_of_members),
            color=0x087d1b)
        members_embed.set_author(name="Taur",
            url="https://github.com/PabloCorbCon/Taur")
        members_embed.set_footer(text="By Pablo Corbalán | Twitter: @pablocorbcon - GitHub: @PabloCorbCon")

        # send the message
        await message.channel.send('Members of the server: ', embed=members_embed)  


    elif message.content.startswith('t/joke'):
        # the bot tells a joke, so we have to open the jokes file
        with open('dic/jokes.txt') as f:
            joke_index = random.randint(1, len(f.readlines()) + 1)
            joke_to_tell = f.readlines()[joke_index]
            await message.channel.send(joke_to_tell)
        print(decorators.responded_to('t/joke'))


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
    print(decorators.responded_to('t/kick', ctx))
    add_reactions(message, (':thumbsup:'))


bot.run(TOKEN)