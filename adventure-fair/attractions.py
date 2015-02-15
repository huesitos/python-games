class Attraction(object):
	"""An Attraction is a game which the player can participate in and win money."""
	def __init__(self, name, greeting, farewell):
		super(Attraction, self).__init__()
		self.name = name
		self.greeting = greeting
		self.farewell = farewell

	def greeting(self):
		print "\"Welcome to %s!\"" % self.name
		print self.greeting

	def farewell(self):
		print "\"Hope to see you soon at %s!\"" % self.name
		self.farewell

class RiddleGame(Attraction):
	"""docstring for RiddleGame"""
	def __init__(self, name, greeting, farewell):
		super(RiddleGame, self).__init__(name, greeting, farewell)
		
class GuessNumber(Attraction):
	"""docstring for GuessNumberAttraction"""
	def __init__(self, name, greeting, farewell):
		super(GuessNumber, self).__init__(name, greeting, farewell)
