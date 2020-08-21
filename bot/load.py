import json

def load_help_commands(route, string=False):

	"""
	This function will load all the bot commands
	(route.json) using the json Python package to
	then store them in a Python diccionary and return them.
	It recibes 2 parameters, the first one called route is the route
	of the file to open, the second one (string[False]) means if the 
	text should be returned as a string with the following
	syntax:

		't/command: info about the command'

	If string is not True (string == False) it will return a
	diccionary with the following syntax.

		{
			'command':'info about the command'
		}
	"""

	try:

		# create the help commands variable
		help_commands = None
	
		with open(route) as f:

			if not string:

				# return the diccionary (p:string == False)
				help_commands = json.loads(route)['commands']
				return help_commands

		# return the string (p:string == True)
		st = None
		for command_key, command in zip(help_commands.keys(), help_commands.values()):

			# syntax of the string
			st += '\n{}: {}'.format(command_key, command)

		return st

	# the route is not valid
	except FileNotFoundError as e:

		print(f'Could not find the file {route} in load.py/load_help_commands() function\n', e)