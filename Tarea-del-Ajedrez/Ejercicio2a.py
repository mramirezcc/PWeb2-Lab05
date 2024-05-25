from interpreter import draw
from chessPictures import *
pic = rock.verticalMirror().negative().join(king).join(bishop).negative()
pic = pic.under(queen.negative().verticalMirror())
pic = pic.horizontalRepeat(3)
draw(pic)