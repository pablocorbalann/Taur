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

	return colorama.Fore.LIGHTMAGENTA_EX + 'Taur has sended a private message to: {0}.'.format(user)