from random import randint

UNLOYAL = 20
NEUTRAL = 50
LOYAL = 80
FULL = CLEAN = POOP = RESTED = 10

def play_dead(name):
	print "%s drops to the ground and plays dead." % name
play_dead = ('play dead', 20, play_dead)

def lay_down(name):
	print "%s lays down." % name
lay_down = ('lay down', 10, lay_down)

def shake_hand(name):
	print "%s shakes paw with you." % name
greet = ('greet', 10, shake_hand)

def sit(name):
	print "%s sits." % name
sit = ('sit', 5, sit)

skill_set = {'sit': sit, 'greet': greet, 'lay down': lay_down, 'play dead': play_dead}

class Pet(object):
	"""A Pet is an animal that the player has to take care of."""
	def __init__(self, name):
		super(Pet, self).__init__()
		self.name = name
		self.age = 0.0
		self.energy = RESTED
		self.stuff_in_belly = FULL # it is full
		self.stuff_in_intestine = 0 # it doesn't need to go
		self.hygine = CLEAN # it's clean
		self.skill_level = 0 # it isn't trained at all
		self.skills = {} # it doesn't know any tricks
		self.loyalty = 0 # it's not very loyal. max 100

	# status check functions
	def hungry(self):
		return self.stuff_in_belly < 5

	def poopy(self):
		return self.stuff_in_intestine > 6

	def sleepy(self):
		return self.energy < 4

	# commands functions
	def sleep(self):
		if self.energy < 4:
			self.energy = RESTED
			print "%s is rested." % self.name
		else:
			print "%s doesn't want to sleep now." % self.name

	def take_walk(self):
		print "You take %s to a walk." % self.name
		self.stuff_in_intestine = 0
		self.energy -= 1
		self.hygine -= 1
		self.loyalty += 0.5

	def bath(self):
		print "You bath %s. It smells like flowers." % self.name
		self.hygine = 10
		self.loyalty += 0.5

	def pet(self):
		print "You pet %s affectionately. It enjoys it." % self.name
		self.loyalty += 1

	def eat(self):
		print "%s is now full and happy." % self.name
		self.stuff_in_belly = 10
		self.loyalty += 0.5

	def play(self):
		if not self.hungry() and not self.poopy():
			print "You had a good time playing with %s." % self.name
			self.loyalty += 7
		else:
			print "%s is not in the mood." % self.name

	# order pet to train in a skill. depending on the loyalty of the pet, it will obay or not
	def train(self):
		if self.loyalty <= UNLOYAL:
			print "%s does everything but what you want it to do." % self.name
		elif self.loyalty <= NEUTRAL:
			obey = randint(0, 5) != 0
			if obey:
				print "%s did good in the training session." % self.name
				self.skill_level += 1
				self.stuff_in_belly -= 1
				self.energy -= 1
			else:
				print "%s training is not effective today." % self.name
		elif self.loyalty < LOYAL:
			obey = randint(0, 20) != 0
			if obey:
				print "%s did good in the training session." % self.name
				self.skill_level += 1.5
				self.stuff_in_belly -= 1
				self.energy -= 1
			else:
				print "%s training is not effective today." % self.name
		else:
			print "%s did good in the training session." % self.name
			self.skill_level += 2
			self.stuff_in_belly -= 1
			self.energy -= 1

		self.learned_skill()

	# makes the pet do a trick, if it knows it
	def do_trick(self):
		trick = raw_input("> Which trick?: ")
		if trick in self.skills:
			self.skills[trick](self.name)
		else:
			print "%s doesn't know how to do that." % self.name

	# checks if the skill level is enough to learn a new trick
	def learned_skill(self):
		for skill in skill_set:
			if self.skill_level == skill_set[skill][1]:
				self.skills[skill_set[skill][0]] = skill_set[skill][2]
				print "%s learned %s!" % (self.name, skill)

	# checks the state of the pet and informs the owner
	def check_state(self):
		if self.stuff_in_belly < 5 and self.stuff_in_belly > 2:
			print "%s is hungry..." % self.name
		elif self.stuff_in_belly < 3 and self.stuff_in_belly > 0:
			if self.loyalty <= UNLOYAL:
				print "%s ran way. You should take better care of your pet." % self.name
				exit(1)
			else:
				print "%s is starving." % self.name
		elif self.stuff_in_belly == 0:
			print "%s died of hunger. Shame on you." % self.name
			exit(1)

		if self.stuff_in_intestine > 6 and self.stuff_in_intestine < POOP:
			print "%s wants to go." % self.name
		elif self.stuff_in_intestine == POOP:
			print "%s made a mess." % self.name
			self.hygine = 1
			self.stuff_in_intestine = 0

		if self.hygine < 4 and self.hygine > 0:
			print "%s stinks, please bath it." % self.name
		elif self.hygine < 0:
			print "%s got sick and died. You are a horrible owner." % self.name
			exit(1)

		if self.energy < 4 and self.energy > 0:
			print "%s is tired. Put it to sleep." % self.name
		elif self.energy == 1:
			if self.loyalty <= UNLOYAL:
				print "%s ran way. You should take better care of your pet." % self.name
				exit(1)
			else:
				print "%s is starving." % self.name
		elif self.energy == 0:
			print "%s died of exhaustion. Hopefully you are not so unresponsible with yourself." % self.name
			exit(1)
