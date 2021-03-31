#This program calculates the number of e's in a text file
# obtained from an argument on the command line

#author: Stephen Caulfield

#Txt file obtained from https://www.gutenberg.org/files/2701/old/moby10b.txt

#imports library with functions that take arguments from command line
import sys  

e = 0
z = 0

#Takes argument from command line for txt file.
txt = sys.argv[1]   

#Loops through each letter in submitted txt file and increments e with each 'e' found.
with open(txt, "rt") as f:  
    while 1:
        g = f.read(1)
        if g == "e" or g == "E":
            e += 1
        if not g: 
            break

print(e)