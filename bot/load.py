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
		print(help_commands)

		with open(route) as f:

			help_commands = json.loads(f.read())['commands'][0]
			print('\nHELP COMMANDS: ', help_commands)

			if not string:

				# return the diccionary (p:string == False)
				return help_commands

		# return the string (p:string == True)
		st = ''
		for command_key, command in zip(help_commands.keys(), help_commands.values()):

			print(command_key, command)

			# syntax of the string
			st = st + '\n{}: {}'.format(command_key, command)

		return st

	# the route is not valid
	except FileNotFoundError as e:

		print(f'Could not find the file {route} in load.py/load_help_commands() function\n', e)



def load_jokes(route, single=False, string=False):

	"""
	This function will load all the bot jokes
	(route.txt) to then store them in a Python tuple and return them.
	It recibes 3 parameters, the first one called route is the route
	of the file to open, the second one (single[False]) is used to load
	a single joke instead of all the documment.
	The third one (string[False]) means if the 
	text should be returned as a string with the following
	syntax:

		'joke1<br>joke2<br>joke3<br>....jokeN'

	If string is not True (string == False) it will return a
	tuple with the following syntax.

		(
			joke1,
			joke2,
			joke3,
			...
			jokeN
		)

	So if the p:single is not False (is a number) and p:string=False
	the programm will return a tuple with a single element.
	"""

	try:

		jokes = []
		jokes_to_tell = ()

		with open(route) as f:

			jokes = f.readlines()
			# we check if the user wants to return a single joke or the user 
			# wants to load all the jokes file
			if single != False:
				# get the single line as a tuple inside the jokes statement
				jokes_to_tell = (jokes[single])

			else:
				# the user wants to load all the jokes inside a list
				jokes_to_tell = tuple(jokes)

			if string:
				#return the jokes_to_tell tuple as a string
				st = ''
				br_line = ''
				if not single:
					br_line = '\n'

				for joke in jokes_to_tell:
					st += '{}{}'.format(joke, br_line)
				return st
			return jokes_to_tell

	except FileNotFoundError as e:

		print(f'Could not find the file {route} in load.py/load_jokes() function\n', e)