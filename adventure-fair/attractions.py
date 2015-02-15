class Attraction(Place):
	"""An Attraction is a game which the player can participate in and win money."""
	def __init__(self, name, greeting, farewell):
		super(Attraction, self).__init__(name, greeting, farewell)

	def enter(self):
		super()
		self.game()

	def game(self):
		print "Not implemented"

class Riddles(Attraction):
	"""docstring for Riddles"""
	def __init__(self, name, greeting, farewell):
		super(Riddles, self).__init__(name, greeting, farewell)

	def game(self):
		pass
		
class GuessNumber(Attraction):
	"""docstring for GuessNumberAttraction"""
	def __init__(self, name, greeting, farewell):
		super(GuessNumber, self).__init__(name, greeting, farewell)

	def game(self):
		pass
