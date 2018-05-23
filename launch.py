from modules.utils import play_game

print("Let's play some tic-tac-toe!\n")
print("Instructions:")
print("Each possible space has a corresponding name, shown below. When it is your turn, enter that name to place your 'X' or 'O'")
print(' a1 | a2 | a3 ')
print('----|----|----')
print(' b1 | b2 | b3 ')
print('----|----|----')
print(' c1 | c2 | c3 ')
input("When you're ready to start, hit ENTER:\n")

play_game()