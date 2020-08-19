# This is the main file of Taur. Our Discord bot written in discord.py
# if you need more information about Taur, you can check the GitHub repository
# https://github.com/PabloCorCon/Taur

import discord
import colorama
import platform
import json

colorama.init(autoreset=True)

# we create the discord client.
client = ()
with open('doc/description.txt') as description:

    client = discord.Client(description=description.read())

@client.event
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
    print('\nLogged in as {}, id: {} | Servers: {} | Users: {}'.format(client.user.name,
                                                                     client.user.id,
                                                                     len(client.guilds),
                                                                     len(set(client.get_all_members()))) + ' users')

    # bot python information
    print('\nPython version: {} | Discord.py version: {}'.format(platform.python_version(),
                                                               discord.__version__))

    #liks
    invite = 'https://discord.com/oauth2/authorize?client_id=745535486784831509&scope=bot&permissions=268690782'
    print('\nUse this link to invite {}:'.format(client.user.name)
    print(invite)

    github_repo = 'github.com/PabloCorbCon/Taur'
    print('\nGitHub repository: {}'.format(github_repo))



if __name__ == '__main__':

    with open('doc/token.txt', 'r') as token:

        # run the client with a token.
        client.run(token.read())