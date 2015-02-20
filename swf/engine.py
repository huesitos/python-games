from game_map import *

STARTING_MONEY = 30

class Player(object):
	"""Player class contains a record of the money the player has."""
	def __init__(self, money):
		super(Player, self).__init__()
		self.money = money

	def pay(self, price):
		self.money -= price

	def receive(self, price):
		self.money += price

class Engine(object):
	"""The Engine has the logic of the game"""
	HELP = "help"
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
		print "\nThe 'Seven Wonders Fair' opened today. You have been waiting for this day for a long time. While walking to the fair, you can't help but imagine what these 'seven wonders' might be. The exhibitions probably cost good money, but maybe you could play some of the games and win what you need to buy the ticket...\n"
		self.play()

	def bad_ending(self):
		print "\nAfter a long day of playing around you weren't able to win the money for the exhibitions. In fact, you now have no money!\n"
		again = raw_input("Would you like to play again? (y or n): ")
		if again == "y":
			self.intro()

	def good_ending(self):
		print "\nCongratulations! After a long day of playing around were able to visit all the exhibitions.\n"
		self.quit()

	def quit(self):
		print "Thanks for playing!"
		exit(1)

	def navigate(self):
		player_input = raw_input("> ").strip().lower()

		if player_input == Engine.HELP:
			options = [Engine.QUIT, Engine.MONEY, Engine.WHERE]
			if isinstance(Map.places[self.current_place], Game):
				options.append(Engine.PLAY)
			if isinstance(Map.places[self.current_place], Exhibition):
				options.append(Engine.ENTER)
			print "Actions: %s" % ', '.join(options)
			print "Places: %s" % ', '.join(Map.places.keys())
		elif player_input == Engine.PLAY:
			if isinstance(Map.places[self.current_place], Game):
				Map.places[self.current_place].play(self.player)
				print "You now have %d in your wallet." % self.player.money
			else:
				print "There is nothing to play with here."
		elif player_input == Engine.ENTER:
			if isinstance(Map.places[self.current_place], Exhibition):
				Map.places[self.current_place].enter(self.player)
		elif player_input == Engine.MONEY:
			print "You have %d in your wallet." % self.player.money
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
			if self.game_over(): self.bad_ending()
			if self.game_won(): self.good_ending()

	def game_over(self):
		return self.player.money <= 0

	def game_won(self):
		exhibitions = []
		for place in Map.places.values():
			if isinstance(place, Exhibition):
				exhibitions.append(place)

		won = True
		for exhibition in exhibitions:
			won = (won and exhibition.visited)

		return won
			