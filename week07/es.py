#This program calculates the number of e's in a text file
# obtained from an argument on the command line

#author: Stephen Caulfield

import sys

y = 0
z = 0

txt = sys.argv[1]

with open(txt, "rt") as f:
    while 1:
        g = f.read(1)
        if g == "e" or g == "E":
            y += 1
        if not g: 
            break

print(y)
