commands = {
	'help':'shows help',
	'info':'shows info'
}

d = ''

for i, j in zip(commands.values(), commands.keys()):

	d += '\n{}: {}'.format(j, i)

print(d)