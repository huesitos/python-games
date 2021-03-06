from game_map import *
from engine import *

def welcome():
	print "%s Seven Wonders Fair %s" % ("*" * 20, "*" * 20)

	print "\nWelcome to the 'Seven Wonders Fair' text based game.\n"
	print "This is a text based game where you will be able to explore the different games and exhibitions at the 'Seven Wonders Fair'. You travel around by writing the name of the place you want to go to or the action you want to do. To check what places or actions you can do, you can type the command 'help' and press enter. A list of all the actions and places will be printed on screen.\n"
	print "Press ENTER to start the game.\n"
	raw_input("*" * 63)

Map.places = {
	'entrance': Place(
		name = "Seven Wonders Fair Entrance",
		greeting="You are at the entrace of the fair. The fair is moderately crowded. By your left there is an old man smoking his pipe, sitting in front of a small stand that has a sign that reads \"Mr. D's Riddles\". By your left is another small stand with a sign that reads \"Alice's Secret Number\". There is a little girl stading near it, looking at you and smiling. In front of you, but further away, is the tent where the \"First Wonder - Strange Create of the East Exhibition\" is being held.",
		farewell="You leave the entrance.\n"
		),
	'riddles': Riddles(
		name = "Mr. D's Riddles",
		greeting = "You approach the stand. The old man stops smoking and stares at you. \n\"If you didn't come here just to stare, then we can play a game of riddles. The bet is $10, if you guess the riddle, I'll give you double that. If you don't, I keep them.\"",
		farewell = "You start walking away. The old man goes back to smoking his pipe in silence.\n"
		),
	'secret number': GuessNumber(
		name = "Alice's Secret Number",
		greeting = "You approach the stand. The little girl standing in front of it waves at you. \n\"Hello there! Let's play a game. I will think of a number from 1-100 and you have to guess it! You will have at much 7 tries, and I will help you along the way! To play you pay $5. If you win, you'll get $10, if you lose, I'll keep the $5. So, I hope you lose a lot! Want to play?\"",
		farewell = "You start walking away. The little girl follows you with her eyes and a big smile on her face.\n"
		),
	'first wonder exhibition': Exhibition(
		name = "First Wonder - Strange Create of the East",
		greeting = "You approach the big tent. A big crowd stands in front of the entrance.",
		farewell = "You walk your way through the crowd and leave.",
		walkthrough = "\nThe exhibition was astonishing. Never in your live had you seen a beast like that.",
		price = 300
		)
}

place_map = Map('entrance')
a_game = Engine(place_map)
welcome()
a_game.intro()