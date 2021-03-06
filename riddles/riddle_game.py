from riddles_list import riddles
from random import randint

print "What's your name?"

name = raw_input("> ");

print "Hello", name
print "Let's play a game!"
print "In fact, let's play a riddle game!"
print "The rules are simple, we will tell you a riddle and you have to guess the answer. Each time you answer correctly, you will win 10 coins! But if you get it wrong, you lose the same amount your money (don't worry, it's not real...). Every now and then you'll be prompted with the option of multiplying your bet up to 5 times. If you win, you earn more, but if you lose, you also lose more."
print "You start with 10 coins for the first bet. The game ends when you run out of money, decide to quit, or we run out of riddles (we can't know them all). We will help you by giving  you three possible answers from which you can pick the correct one. Let's see how much you can make!\n"

# Helper methods
# Randomly offers bonus money or just a normal bet
def calculate_bet(bet):
	offer_bonus = randint(0,100)
	if offer_bonus % 10 == 0:
		increase_times = randint(1, 6)
		increase_proportion = bet * increase_times
		print "Hey, would you like to increase your bet %d times? If you win, you'll win %d! But if you lose, you'll lose that amount of money..." % (increase_times, increase_proportion)
		choice = raw_input("Type y or n: ")
		if choice == "y":
			return increase_proportion
	return bet

# Game settings and score
BET = 10
coins = 10

while coins > 0 and riddles:
	riddle = riddles.pop()
	print "You have %d coins." % coins
	actual_bet = calculate_bet(BET)

	print "Riddle:"
	print riddle[0]

	# Prints all possible answers
	for pos, answer in zip(range(0, len(riddle[2])), riddle[2]):
		print "%d. %s" % (pos + 1, answer)

	guess = raw_input("Answer (just the number): ")

	# Compares if the chosen answer is the correct one
	if riddle[2][int(guess)-1] == riddle[1]:
		print "Correct! You win %d coins!\n" % actual_bet
		coins += actual_bet
	else:
		print "Nope. The correct answer is\n", riddle[1]
		coins -= actual_bet

if coins > 0:
	print "That's as many riddles as I know!"
	print "Congragulations, %s! You won %d coins, you are rich now!" % (name, coins)
elif coins < 0:
	print "What a shame %s! You not only lost all your money, now you owe me %d!" % (name, coins)
else:
	print "Sorry, %s. You lost all your money, I guess riddles aren't for ya." % (name)
