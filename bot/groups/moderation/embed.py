import discord
class ModerationEmbed():

	"""
	This class stores the moderation embed message using the discord.Embed() class
	to create a red alert message.
	"""
	def __init__(self, d, title='Taur | Moderation'):
		"""
		This is the __init__ method from the ModerationEmbed() class,
		from here all the attributes are created
		"""
		self.d = d
		self.title = title

	def get(self):
		"""
		This method returns a discord.Embed() object to then send it.
		using the discord.Embed() class (in this file Embed())
		"""
		e = discord.Embed(title=self.title, description=self.d, color=discord.Color.red())
		e.set_author(name="Taur", url="https://github.com/PabloCorbCon/Taur")
		e.set_footer(text="By Pablo Corbalán | Twitter: @pablocorbcon - GitHub: @PabloCorbCon")
		return e

	async def send(self, ctx):
		"""
		This method sends the embed message to an specific context 
		instance.
		""" 
		await ctx.send(embed=self.get())