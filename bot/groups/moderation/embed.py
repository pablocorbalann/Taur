from discord import Embed
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
		self.title

	def get_message():
		"""
		This method returns a discord.Embed() object to then send it.
		"""
	    e=discord.Embed(title=self.title,
	        description=self.d,
	        color=discord.Color.red())
	    e.set_author(name="Taur",
	        url="https://github.com/PabloCorbCon/Taur")
	    e.set_footer(text="By Pablo Corbalán | Twitter: @pablocorbcon - GitHub: @PabloCorbCon")
	    return e
	    
	def send_message(ctx):
		"""
		This method sends the embed message to an specific context 
		instance.
		""" 
		ctx.send(embed=self.get_embed())