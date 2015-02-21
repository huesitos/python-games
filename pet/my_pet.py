from random import randint

UNLOYAL = 20
NEUTRAL = 50
LOYAL = 80

def play_dead(name):
	print "%s drops to the ground and plays dead." % name
play_dead = ['play dead', 20, play_dead]

def lay_down(name):
	print "%s lays down."
lay_down = ['lay down', 10, lay_down]

def shake_hand(name):
	print "%s shakes hand with you." % name
greet = ['greet', 10, shake_hand]

def sit(name):
	print "%s sits."
sit = ['sit', 5, sit]

skill_set = [sit, greet, lay_down, play_dead]

class Pet(object):
	"""A Pet is an animal that the player has to take care of."""
	def __init__(self, name):
		super(Pet, self).__init__()
		self.name = name
		self.asleep = False
		self.age = 0.0
		self.energy = 10
		self.stuff_in_belly = 10 # it is full
		self.stuff_in_intestine = 0 # it doesn't need to go
		self.hygine = 10 # it's clean
		self.skill_level = 0 # it isn't trained at all
		self.skills = {} # it doesn't know any tricks
		self.loyalty = 0 # it's not very loyal. max 100

	def hungry(self):
		return self.stuff_in_belly < 6

	def poopy(self):
		return self.stuff_in_intestine > 5

	def sleepy(self):
		return self.energy < 4

	def go_sleep(self):
		if self.energy > 3:
			self.asleep = True
		elif self.asleep:
			print "%s is already sleeping." % self.name
		else:
			print "%s is doesn't want to sleep now." % self.name			

	def wake_up(self):
		if not self.asleep:
			print "%s is already awake." % self.name
		else:
			self.asleep = False

	def take_walk(self):
		print "You take %s to walk." % self.name
		self.stuff_in_intestine = 0
		self.energy -= 1
		self.hygine -= 1
		self.loyalty += 0.5

	def bath(self):
		print "You bath %s. It smells like flowers." % self.name
		self.hygine = 10

	def pet(self):
		print "You pet %s affectionately. It enjoys it." % self.name
		self.loyalty += 1

	def play(self):
		if not self.hungry and not self.poopy:
			print "You had a good time playing with %s." % self.name
			self.loyalty += 2
		else:
			print "%s is not in the mood."

	def train(self):
		if self.loyalty <= UNLOYAL:
			print "%s is not listening to your commands."
		elif self.loyalty <= NEUTRAL:
			obey = randint(0, 5) != 0
			if obey:
				self.skill_level += 1
				self.stuff_in_belly -= 1
				self.energy -= 1
			else:
				print "%s is not listening to your commands."
		elif self.loyalty < LOYAL:
			obey = randint(0, 20) != 0
			if obey:
				self.skill_level += 1.5
				self.stuff_in_belly -= 1
				self.energy -= 1
			else:
				print "%s is not listening to your commands."
		else:
			self.skill_level += 2
			self.stuff_in_belly -= 1
			self.energy -= 1

		self.learned_skill()

	def learned_skill(self):
		for skill in skill_set:
			if self.skill_level == skill[1]:
				self.skills[skill[0]] = skill[2]
				print "%s learned %s!" % (self.name, self.skill[0])

	def do_trick(self, trick):
		if trick in self.skills:
			self.skills[trick](self.name)
		else:
			print "%s doesn't know how to do that." % self.name

	def passage_of_time(self):
		if (self.age + 0.01) - int(self.age) == 1:
			print "%s is now %d years old." % (self.name, self.age)
		self.age += 0.01

		self.stuff_in_belly -= 1
		self.stuff_in_intestine += 1
		self.hygine -= 0.5

		if self.asleep:
			if not self.hungry() and not self.poopy() and self.energy < 10:
				self.energy += 1
			else:
				print "%s wakes up."
				self.wake_up()
		else:
			self.energy -= 0.5

		if self.stuff_in_belly < 6 and self.stuff_in_belly > 3:
			print "%s is hungry..." % self.name
		elif self.stuff_in_belly <= 3 and self.stuff_in_belly > 0:
			if self.loyalty <= UNLOYAL:
				print "%s ran way. You should take better care of your pet." % self.name
			else:
				print "%s is starving." % self.name
		elif self.stuff_in_belly == 0:
			print "%s died of hunger. Shame on you." % self.name
			exit(1)

		if self.stuff_in_intestine > 5 and self.stuff_in_intestine < 10:
			print "%s wants to go." % self.name
		elif self.stuff_in_intestine == 10:
			print "%s made a mess."
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
			else:
				print "%s is starving." % self.name
		elif self.energy == 0:
			print "%s died of exhaustion. Hopefully you are not so unresponsible with yourself." % self.name
			exit(1)

print "Give your pet a name"
name = raw_input("> ")

pet = Pet(name)
pet.play()
pet.pet()
pet.train()
pet.passage_of_time()

