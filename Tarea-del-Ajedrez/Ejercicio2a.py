from interpreter import draw
from chessPictures import *
pic = Picture(knight.negative())
pic = pic.join(king)
draw(pic)