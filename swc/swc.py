from game_map import *
from engine import *

player = None
STARTING_MONEY = 50

Map.places = {
	'entrance': Place(
		name = "Seven Wonders Local Fair",
		greeting="You are at the entrace of the fair.",
		farewell="You leave the fair and head towards your home."
		),
	'riddles': Riddles(
		name = "Mr. D's riddles",
		greeting = "",
		farewell = ""
		),
	'guess the number': GuessNumber(
		name = "",
		greeting = "",
		farewell = ""
		),
	'monster exhibition': Exhibition(
		name = "",
		greeting = "",
		farewell = ""
		)
}

place_map = Map('entrance')
a_game = Engine(place_map)
a_game.intro()
a_game.play()