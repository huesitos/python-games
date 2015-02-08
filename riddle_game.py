# Add some functions...
from riddles_list import riddles
from random import randint

print "Hello there! Let's play a game!"
print "In fact, let's play a riddle game!"
print "The rules are simple, we will tell you a riddle and you have to guess the answer. You will start with 50 coins and for each riddle you will have to make a 10 coins bet. If you guess correctly, you will receive double the money; ain't that awesome?! However if you lose, then you lose your money (don't worry, it's not real...). The game ends when you run out of money or decide to quit."
print "We will help you by giving  you three possible answers from which you can pick the correct one. Let's see how much you can make!\n"

coins = 50
bet = 10

for riddle in riddles:
	print "You have %d coins." % coins
	print "Riddle:"
	print riddle[0]
	# make it multiple choices...
	guess = raw_input("Answer: ")

	actual_bet = bet
	bonus = randint(0,1)
	if bonus == 1:
		increase_proportion = bet * randint(0, 5)
		print "Hey, would you like to increase your bet %d times? If you win, you'll win %d! But if you lose, you'll lose that amount of money..." % (increase_proportion, increase_proportion * bet)
		choice = raw_input("y or n")
		if choice == "y":
			actual_bet *= increase_proportion

	if guess == riddle[1]:
		print "Correct! You win %d coins!" % actual_bet
		coins += actual_bet
	else:
		print "Nope. The correct answer is", riddle[1]
		coins -= actual_bet

	if coins <= 0:
		break
	print ""

if coins > 0:
	print "That's as much riddles as I know! You won %d coins, you are rich now!" % coins
elif coins < 0:
	print "You not only lost all your money, now you owe me %d!" % coins
else:
	print "You lost all your money, I guess riddles aren't for ya."