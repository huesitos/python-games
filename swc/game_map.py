class Place(object):
	"""A Place is any of the places where the player can go to"""
	def __init__(self, name, greeting, farewell):
		super(Place, self).__init__()
		self.name = name
		self.greeting = greeting
		self.farewell = farewell

	def enter(self):
		print self.name
		print '-' * len(self.name)
		print self.greeting

	def leave(self):
		print self.farewell

class Exhibition(Place):
	"""An Exhibition is a place in which the player spends money to see interesting showings"""
	def __init__(self, name, price, greeting, farewell, walkthrough):
		super(Exhibition, self).__init__()
		self.price = price
		self.walkthrough = walkthrough

	def walkthrough(self):
		print walkthrough

	def enter(self, player):
		if player.money == self.price:
			player.pay(self.price)
			super()
			self.walkthrough()
		else:
			print "I can't enter '%s'. I need $%d for the ticket." % (self.name, self.price))

class Attraction(Place):
	"""An Attraction is a game which the player can participate in and win money."""
	def __init__(self, name, greeting, farewell):
		super(Attraction, self).__init__(name, greeting, farewell)

	def play(self):
		print "Not implemented"

class Riddles(Attraction):
	"""Riddles is an attraction where the player can try to guess riddles and win money."""
	def __init__(self, name, greeting, farewell):
		super(Riddles, self).__init__(name, greeting, farewell)
		
class GuessNumber(Attraction):
	"""GuessNumber is an attraction where the player can try to guess a secret number and win money."""
	def __init__(self, name, greeting, farewell):
		super(GuessNumber, self).__init__(name, greeting, farewell)

class Map(object):
	"""A Map has all the possible places a player can go to"""
	places = {}

	def __init__(self, start_place):
		super(Map, self).__init__()
		self.start_place = start_place

	def move_place(self, place_name):
		return Map.places[place_name]
		