lottery_numbers = {13, 21, 22, 5, 8}

players = [
	{
    'name': 'PLAYER_1',
    'numbers': {1, 2, 3, 4, 5}
	},
	{
    'name': 'PLAYER_2',
    'numbers': {13, 21, 22, 5, 8}
	}
]

print("Player " + players[0]['name'] + " got " + str(len(lottery_numbers.intersection(players[0]['numbers']))) + " numbers right.")

print("Player " + players[1]['name'] + " got " + str(len(lottery_numbers.intersection(players[1]['numbers']))) + " numbers right.")