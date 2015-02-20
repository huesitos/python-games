from random import randint, shuffle
from riddles_list import riddles

class Place(object):
	"""A Place is any of the places where the player can go to"""
	def __init__(self, name, greeting, farewell):
		super(Place, self).__init__()
		self.name = name
		self.greeting = greeting
		self.farewell = farewell

	def go(self):
		print self.name
		print '-' * len(self.name)
		print self.greeting

	def leave(self):
		print self.farewell

class Exhibition(Place):
	"""An Exhibition is a place in which the player spends money to see interesting showings"""
	def __init__(self, name, greeting, farewell, price, walkthrough):
		super(Exhibition, self).__init__(name, greeting, farewell)
		self.price = price
		self.walkthrough = walkthrough

	def walkthrough(self):
		print walkthrough

	def enter(self, player):
		print "You approach the person selling tickets. She asks you for $%d for one ticket." % self.price
		if player.money == self.price:
			player.pay(self.price)
			self.walkthrough()
		else:
			print "You don't have enough money to buy it."

class Game(Place):
	"""A game in which the player can participate in and win money."""
	def __init__(self, name, greeting, farewell):
		super(Game, self).__init__(name, greeting, farewell)

	def play(self):
		print "Not implemented"

class Riddles(Game):
	"""Riddles is a game where the player can try to guess riddles and win money."""
	BET = 10
	def __init__(self, name, greeting, farewell):
		super(Riddles, self).__init__(name, greeting, farewell)

	def play(self, player):
		chosen_riddle = randint(0, len(riddles)-1)
		riddle = riddles[chosen_riddle]

		answer = riddle[1]
		options = riddle[2]
		shuffle(options)

		print "\n\"Listen well, I won't repeat myself:\""
		print riddle[0]

		# Prints all possible options
		for pos, option in zip(range(0, len(options)), options):
			print "%d. %s" % (pos + 1, option)

		guess = raw_input("\nAnswer (just the number): ")

		# Compares if the chosen answer is the correct one
		if options[int(guess)-1] == answer:
			print "\"Correct. Here are your $%d...\"" % (Riddles.BET*2)
			player.receive(Riddles.BET*2)
		else:
			print "Nope. The correct answer is %s. I'll have my %d, please." % (answer, Riddles.BET)
			player.pay(Riddles.BET)

		again = raw_input("\n\"Would you like to play again? (y or n): \"")
		if again == "y":
			self.play(player)
		
class GuessNumber(Game):
	"""GuessNumber is a game where the player can try to guess a secret number and win money."""
	BET = 5
	MAX_TRIES = 7
	def __init__(self, name, greeting, farewell):
		super(GuessNumber, self).__init__(name, greeting, farewell)

	def play(self, player):
		number = randint(0, 100)
		tries = 0
		won = False

		print "\n\"Alrighty, I picked my number. Try to guess it!\""

		while tries <= GuessNumber.MAX_TRIES and not won:
			tries += 1
			guess = raw_input("Try number " + str(tries) + ": ")
			if int(guess) == number:
				print "\"Huuray! You guessed the number! Here are your %d.\"" % (GuessNumber.BET*2)
				won = True
				player.receive(GuessNumber.BET*2)
			elif int(guess) > number:
				print "\"Why not a smaller number?\""
			else:
				print "\"Why not a bigger number?\""

		if not won:
			print "\"Huuray! You lost! Give me my $%d.\"" % GuessNumber.BET
			player.pay(GuessNumber.BET)

		again = raw_input("\"Would you like to play again? (y or n)\": ")
		if again == "y":
			self.play(player)

class Map(object):
	"""A Map has all the possible places a player can go to"""
	places = {}

	def __init__(self, start_place):
		super(Map, self).__init__()
		self.start_place = start_place