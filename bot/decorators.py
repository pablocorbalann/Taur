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
	return colorama.Fore.LIGHTMAGENTA_EX + 'Taur has responded to a command ({0}).'.format(command)
