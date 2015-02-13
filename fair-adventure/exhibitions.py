class Exhibition(object):
	"""An Exhibition is a place in which the player spends money to see interesting showings"""
	def __init__(self, name, price, greeting, farewell, walkthrough):
		super(Exhibition, self).__init__()
		self.name = name
		self.price = price
		self.greeting = greeting
		self.farewell = farewell
		self.walkthrough = walkthrough

	def greeting(self):
		print "\"Welcome to %s!\"" % self.name
		print self.greeting

	def walkthrough(self):
		print walkthrough

	def farewell(self):
		print "\"Hope to see you soon at %s!\"" % self.name
		print self.farewell

class WeirdMonsters(Exhibition):
	"""docstring for Monster"""
	def __init__(self, name, price, greeting, farewell, walkthrough):
		super(Monster, self).__init__(name, price, greeting, farewell, walkthrough)