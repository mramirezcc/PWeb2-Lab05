from interpreter import draw
from chessPictures import *
pic = rock.verticalMirror().negative().join(king).join(bishop).negative()
draw(pic)