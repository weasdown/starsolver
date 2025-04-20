# Example of using the solver

import starsolver as s

board: s.Board = s.Board()

print(f'{board.num_blanks = }')
print(f'{board.num_dots = }')
print(f'{board.num_stars = }\n')

board[0][0].dot()
print(board[0][0])

print(f'\n{board.num_blanks = }')
print(f'{board.num_dots = }')
print(f'{board.num_stars = }')

print(f'\n{board[0].cells}')
