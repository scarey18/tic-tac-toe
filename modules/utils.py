

def play_game():
	board = {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ', 'b2': ' ', 'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}
	turn = 'X'

	while check_for_moves(board):
		print_board(board)

		take_turn(turn, board)
		if check_for_victory(board):
			print("\nCongrats %s, you win!!" % turn)
			print_board(board)
			if not play_again():
				return

		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'

	print("\n It's a tie!")
	print_board(board)
	play_again()

def check_for_moves(board):
	if ' ' in (board[space] for space in board.keys()):
		return True
	return False

def print_board(board):
	print('\n')
	print(' %s | %s | %s ' % (board['a1'], board['a2'], board['a3']))
	print('---|---|---')
	print(' %s | %s | %s ' % (board['b1'], board['b2'], board['b3']))
	print('---|---|---')
	print(' %s | %s | %s ' % (board['c1'], board['c2'], board['c3']))

def check_for_victory(board):
	groups = [
		('a1', 'a2', 'a3'),
		('b1', 'b2', 'b3'),
		('c1', 'c2', 'c3'),
		('a1', 'b1', 'c1'),
		('a2', 'b2', 'c2'),
		('a3', 'b3', 'c3'),
		('a1', 'b2', 'c3'),
		('c1', 'b2', 'a3'),
	]
	for group in groups:
		if board[group[0]] == board[group[1]] == board[group[2]] and board[group[0]] != ' ':
			return True

def take_turn(turn, board):
	answer = input("%s, it's your turn. Input the name of an empty space to place your marker: " % turn)
	if answer.lower() not in board.keys():
		print("That's not a valid space! Try again.")
		take_turn(turn, board)
	elif board[answer.lower()] != ' ':
		print("That space has already been taken! Try again.")
		take_turn(turn, board)
	else:
		board[answer.lower()] = turn


def play_again():
	answer = input("\nWould you like to play again? y/n: ")
	if answer == 'y' or answer == 'Y':
		play_game()
	elif answer == 'n' or answer == 'N':
		print("Ok byyyye :(")
		return False
	else:
		print("\nThat's not one of the options!")
		play_again()