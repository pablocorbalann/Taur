import colorama
colorama.init(autoreset=True)

def add_reactions(msg, reactions = ()):

	"""
	This function will add the reactions to an specific discord message
	using two parameters:

		p:msg => The message to add the reaction
		p:reactions => A tupple with the reactions to add (tupple)
	"""

	for reaction in reactions:
		msg.add_reaction(reaction)


def responded_to(command):

	"""
	This public function is used as a debug tool and server side decorator that 
	will print in the python console the following message:

		Taur has responded to a command (t/command).

	Using the colorame.Fore module to print it in magenta
	"""
	return colorama.Fore.LIGHTMAGENTA_EX + 'Taur has responded to a command ({0}).'.format(command)


def sended_to(user):

	"""
	This public function is used as a debug tool and server side decorator that 
	will print in the python console the following message:

		Taur has sended a private message to: user.

	Using the colorame.Fore module to print it in cyan
	"""

	return colorama.Fore.CYAN + 'Taur has sended a private message to: {0}.'.format(user)


def deleted(message, word):

	"""
	This public function is used as a debug tool and server side decorator that 
	will print in the python console the following message:

		Taur has deleted the following message: msg from
		user because of the word "word".

	Using the colorame.Fore module to print it in red
	"""

	return colorama.Fore.RED + 'Taur has deleted the following message:\n\n```{}```\nfrom {} because of the word {}.'.format(message.content, message.author.name, word)