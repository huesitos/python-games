from game_map import *
from engine import *

player = None
STARTING_MONEY = 50

Map.places = {
	'entrance': Place(
		greeting="You arrive at the entrance. "
		),
	'riddles': Riddles(),
	'guess the number': GuessNumber(),
	'monster exhibition': Exhibition()
}

place_map = Map()
a_game = Engine(place_map)
a_game.intro()
a_game.play()