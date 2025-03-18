# start a game
# Define the pieces that are in a game
# Define how the pieces move
# Define the space in which the pieces can move, i.e. the board
# Define how a game starts and end
# Check moves and validate who wins.
# Create a 2D Matrix of size 8x8
# Define the pieces, what is the best DS or way of initialising it ?

from src.pieces import Board


board = Board(game_state=0)
# Init game
# print(board.put_pieces_on_board())
board.print_state_of_board()

x, y = (1, 2)
print(x, y)