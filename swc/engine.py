class Player(Character):
	"""Player class contains a record of the money the player has."""
	def __init__(self, name, money):
		super(Player, self).__init__(name)
		self.money = money

	def pay(price):
		self.money -= price

	def earn(price):
		self.money += price

class Engine(object):
	"""The Engine has the logic of the game"""
	OPTIONS = "options"
	QUIT = "quit"
	WALK = "walk around"
	PLAY = "play"
	MONEY = "check money"
	WHERE = "where"

	def __init__(self, place_map):
		super(Engine, self).__init__()
		self.place_map = place_map

	def intro(self):
		print "Story intro"

	def end(self):
		self.current_place.leave()
		Maps.places[self.place_map.start_place].leave()
		print "Thanks for playing!"
		exit(1)

	def navigate(self):
		player_input = raw_input("> ").strip().lower()

		if player_input == OPTIONS:
			options = [OPTIONS, QUIT, MONEY, WHERE]
			if self.current_place is Attraction:
				options.push(PLAY)
			elif self.current_place is Exhibition:
				options.push(WALK)
			print self.place_map.keys().join(', ') + options.join(', ')
		elif player_input == PLAY:
			if self.current_place is Attraction:
				self.current_place.play()
			else:
				print "There is nothing to play with here."
		elif player_input == WALK:
			if self.current_place is Exhibition:
				self.current_place.walkthrough()
			else:
				print "Not much to see around here."
		elif player_input == MONEY:
			print "I have %d in my pocket." % player.money
		elif player_input == WHERE:
			print "You are at the %s." % Map.places(self.current_place).name
		elif player_input == QUIT:
			self.end()
		elif player_input == self.current_place:
			print "I am already here..."
		elif player_input in self.place_map:
			current_place.leave()
			current_place = self.place_map.next_place(next_place)
			current_place.enter()
		else:
			print "Invalid option (type 'options' to see acceptable options."

	def play(self):
		self.current_place = self.place_map.start_place
		self.current_place.enter()

		while True:
			navigate()