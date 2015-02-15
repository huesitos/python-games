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
			print player.say("I can't enter '%s'. I need $%d for the ticket." % (self.name, self.price))