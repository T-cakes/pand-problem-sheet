#This program takes a string input and prints every second letter backwards
#author: Stephen Caulfield

inString = input("please enter a string:")

i = len(inString)

#removes every second letter from string starting with first letter
secLetter = inString[1:i:2]

#creates the processed string backwards
backString = secLetter[::-1]

print(backString)