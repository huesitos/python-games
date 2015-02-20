from game_map import *

STARTING_MONEY = 50

class Player(object):
	"""Player class contains a record of the money the player has."""
	def __init__(self, money):
		super(Player, self).__init__()
		self.money = money

	def pay(price):
		self.money -= price

	def earn(price):
		self.money += price

class Engine(object):
	"""The Engine has the logic of the game"""
	OPTIONS = "options"
	QUIT = "quit"
	PLAY = "play"
	MONEY = "check money"
	WHERE = "where"
	ENTER = "enter"

	def __init__(self, place_map):
		super(Engine, self).__init__()
		self.place_map = place_map
		self.player = Player(STARTING_MONEY)

	def intro(self):
		print "Story intro"

	def quit(self):
		print "Thanks for playing!"
		exit(1)

	def navigate(self):
		player_input = raw_input("> ").strip().lower()

		if player_input == Engine.OPTIONS:
			options = [Engine.OPTIONS, Engine.QUIT, Engine.MONEY, Engine.WHERE]
			if isinstance(Map.places[self.current_place], Attraction):
				options.append(Engine.PLAY)
			if isinstance(Map.places[self.current_place], Exhibition):
				options.append(Engine.ENTER)
			print "%s, %s" % (', '.join(Map.places.keys()), ', '.join(options))
		elif player_input == Engine.PLAY:
			if isinstance(Map.places[self.current_place], Attraction):
				Map.places[self.current_place].play()
			else:
				print "There is nothing to play with here."
		elif player_input == Engine.ENTER:
			if isinstance(Map.places[self.current_place], Exhibition):
				Map.places[self.current_place].enter(self.player)
		elif player_input == Engine.MONEY:
			print "You have %d in your pocket." % self.player.money
		elif player_input == Engine.WHERE:
			print "You are at the %s." % Map.places[self.current_place].name
		elif player_input == Engine.QUIT:
			self.quit()
		elif player_input == self.current_place:
			print "I am already here..."
		elif player_input in self.place_map.places:
			Map.places[self.current_place].leave()
			self.current_place = player_input
			Map.places[self.current_place].go()
		else:
			print "Invalid option (type 'options' to see acceptable options)."

	def play(self):
		self.current_place = self.place_map.start_place
		Map.places[self.current_place].go()

		while True:
			self.navigate()