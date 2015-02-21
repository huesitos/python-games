import thread, threading
from time import time
from pet import *



class Engine(object):
	"""Pet simulator Engine"""

	def __init__(self, pet_name):
		super(Engine, self).__init__()
		self.pet = Pet(pet_name)
		self.commands = {"feed": self.pet.eat, "sleep": self.pet.sleep, "walk pet": self.pet.take_walk, "bath": self.pet.bath, "play": self.pet.play, "train": self.pet.train, "do trick": self.pet.do_trick, "pet": self.pet.pet, "hepl": self.help}

	def help(self):
		print "List of commands"

	def passage_of_time(self):
		prev_age = self.pet.age
		self.pet.age += 0.1
		if self.pet.age - int(prev_age) >= 1:
			print "Congratulations! %s is now %d years old." % (self.pet.name, self.pet.age)

		if self.pet.asleep:
			self.pet.stuff_in_belly -= 0.5
			self.pet.stuff_in_intestine += 0.5
		else:
			self.pet.stuff_in_belly -= 1
		self.pet.stuff_in_intestine += 1
		self.pet.hygine -= 0.5
		self.pet.energy -= 0.5

		self.pet.check_state()

	def play(self):
		print "You receive a wonderfull pet..."
		while True:
			p_input = raw_input("> ")
			if p_input not in self.commands:
				print "Command is not recognized."
			else:
				self.commands[p_input]()
				if p_input != "help":
					self.passage_of_time()
def start():
	print "Welcome to pet simulator!"
	print "How to play:..."
	print "-" * 50

	print "\nGive your pet a name"
	name = raw_input("> ")

	game = Engine(name)
	game.play()

start()