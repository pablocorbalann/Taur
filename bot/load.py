import json

def load_help_commands(route):

	"""
	This function will load all the bot commands
	(route.json) using the json Python package to
	then store them in a Python diccionary and return them.
	"""

	try:
	
		with open(route) as f:

			return json.loads(f)

	except FileNotFoundError as e:

		print(f'Could not find the file {route}', e)