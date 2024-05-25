from interpreter import draw
from chessPictures import *
pic = rock.verticalMirror().negative().join(king).join(bishop).negative()
pic = pic.up(queen.negative().verticalMirror())
draw(pic)