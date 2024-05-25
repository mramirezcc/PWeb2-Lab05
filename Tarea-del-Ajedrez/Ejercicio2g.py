from interpreter import draw
from chessPictures import *

board = square.join(square.negative())
board = board.horizontalRepeat(4)
board = board.up(board.negative())
board = board.verticalRepeat(4)

draw(board)