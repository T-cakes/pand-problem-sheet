#This program calculates the number of e's in a text file
# obtained from an argument on the command line

#author: Stephen Caulfield

#imports library with functions that take arguments from command line
import sys  

y = 0
z = 0

#Takes argument from command line for txt file.
txt = sys.argv[1]   

#Loops through each letter in submitted txt file and increments y with each 'e' found.
with open(txt, "rt") as f:  
    while 1:
        g = f.read(1)
        if g == "e" or g == "E":
            y += 1
        if not g: 
            break

print(y)