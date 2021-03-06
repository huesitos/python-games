import thread, threading
from time import time
from pet import *

class Engine(object):
	"""Pet simulator Engine"""

	def __init__(self, pet):
		super(Engine, self).__init__()
		self.pet = pet
		self.commands = {"feed": self.pet.eat, "sleep": self.pet.sleep, "walk pet": self.pet.take_walk, "bath": self.pet.bath, "play": self.pet.play, "train": self.pet.train, "do trick": self.pet.do_trick, "pet": self.pet.pet, "help": self.help, "save": self.save, "quit": self.quit}
		self.commands_help = {"feed": "feed your pet until it's full.", "sleep": "put pet to sleep until it is rested.", "walk pet": "walk your pet when it wants to go.", "bath": "clean your pet.", "play": "play with your pet and build a good relationship with it.", "train": "train your pet so it learns new skills.", "do trick": "order your pet to do a learned trick.", "pet": "pet your pet and build a good relationship with it.", "save": "saves the state of your pet, in a document named as your pet, so you can reload it later.", "quit": "exit the game (progress is not saved automatically)."}

	def play(self):
		while True:
			p_input = raw_input("> ")
			if p_input not in self.commands:
				print "Command is not recognized."
			else:
				self.commands[p_input]()
				if p_input != "help" and p_input != "save":
					self.passage_of_time()

	def help(self):
		print "List of commands:"
		for command in self.commands_help.items():
			print "\"%s\": %s" % (command[0], command[1])

	def quit(self):
		exit(1)

	def passage_of_time(self):
		prev_age = self.pet.attribs["age"]
		self.pet.attribs["age"] += 0.1
		if self.pet.attribs["age"] - int(prev_age) >= 1:
			print "Congratulations! %s is now %d years old." % (self.pet.attribs["name"], self.pet.attribs["age"])

		self.pet.attribs["stuff_in_belly"] -= 1
		self.pet.attribs["stuff_in_intestine"] += 1
		self.pet.attribs["hygine"] -= 0.5
		self.pet.attribs["energy"] -= 0.5

		self.pet.check_state()

	def save(self):
		data = ""
		for a in self.pet.attribs:
			if a != 'skills':
				data += "%s:%s" % (a, str(self.pet.attribs[a]))
			else:
				data += "%s:%s" % (a, (',').join(self.pet.attribs["skills"].keys()))
			data += ';'
		try:
			with open(self.pet.attribs["name"], 'w+') as f:
				f.write(data[:-1])
			print "Game was saved sucessfully."
		except:
			print "Game could not be saved."

	def load(self, name):
		try:
			with open(self.pet.attribs["name"], 'read') as f:
				data = f.read().strip()
				data = data.split(';')
				for a in data:
					a = a.split(':')
					if a[0] not in ["name", "skills", 'type']:
						self.pet.attribs[a[0]] = float(a[1]) 
					elif a[0] in ["name", "type"]:
						self.pet.attribs[a[0]] = a[1]
					else:
						skills = a[1]
						if len(skills):
							skills = a[1].split(',')
							for skill in skills:
								self.pet.attribs[a[0]] = skill_set[skill][2]
			print "Game loaded sucessfully."
			self.pet.check_state()
			return True
		except:
			print "No game found for the pet \"%s\"." % name
			return False

def start():
	start = False
	print "For a new game, type 'n'. To load a game, type the name of your pet."

	while not start:
		p_input = raw_input("> ")
		if p_input == "n":
			print "\nWhat kind of pet do you want, cat or dog?"
			pet_type = raw_input("> ")

			print "\nGive your pet a name"
			name = raw_input("> ")
			
			print "You receive a wonderfull newborn %s. It's name will be %s. Take good care of it!" % (pet_type, name)
			pet = Pet(name, pet_type)
			game = Engine(pet)
			start = True
		else:
			pet = Pet(p_input, '')
			game = Engine(pet)
			start = game.load(p_input.strip())

	if start:
		game.play()

def intro():
	print "Welcome to pet simulator!"
	print "In this game you will receive a pet, and  you'll have to take care of it so it stays healthy. Prompts with the status of your pet will appear to indicate you what your pet needs at the moment."
	print "Whenever you don't know what to do next, type the command 'help'. If you have to go, you can save your game using the command 'save'. You can load the game by typing the name of your pet. Whenever you want to exit the game, type 'quit'."
	print "-" * 40
	start()

intro()