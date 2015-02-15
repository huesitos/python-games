class Player(object):
	"""Player class contains the name of the player and the money earned"""
	def __init__(self, name, money):
		super(Player, self).__init__()
		self.name = name
		self.money = money

	def pay(price):
		self.money -= price

	def earn(price):
		self.money += price
	
	def say(say):
		print "%s: %s" % (self.name, say)

class Engine(object):
	"""The Engine has the logic of the game"""
	OPTIONS = "options"
	QUIT = "quit"
	WALK_AROUND = "walk around"
	PLAY = "play"

	def __init__(self, place_map):
		super(Engine, self).__init__()
		self.place_map = place_map

	def intro(self):
		print "%s Adventure at the fair %s" % ("*" * 20, "*" * 20)

		name = raw_input("What is your name? ")
		player = Player(name, STARTING_MONEY)

		print "\nWelcome to the 'Adventure at the fair' text based game, %s." % (self.player.name)
		print "Instructions and overview"

		print "*" * 63

	def end(self):
		self.current_place.leave()
		Maps.places[self.place_map.start_place].leave()
		print "Thanks for playing!"
		exit(1)

	def navigate(self):
		player_input = raw_input("> ").strip().lower()

		if player_input == OPTIONS:
			options = [OPTIONS, QUIT]
			if self.current_place is Attraction:
				options.push(PLAY)
			elif self.current_place is Exhibition:
				options.push(WALK_AROUND)
			print self.place_map.keys().join(', ') + options.join(', ')
		elif player_input == PLAY:
			if self.current_place is Attraction:
				self.current_place.play()
			else:
				player.say("There is nothing to play with here.")
		elif player_input == WALK_AROUND:
			if self.current_place is Exhibition:
				self.current_place.walkthrough()
			else:
				player.say("Not much to see around.")
		elif player_input == QUIT:
			self.end()
		elif player_input == self.current_place:
			player.say("I am already here...")
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