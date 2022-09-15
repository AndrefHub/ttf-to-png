import os
from fontforge import *

font = open(os.sys.argv[1])
for glyph in font:
    filename = glyph + ".svg"
    font[glyph].export(filename)
