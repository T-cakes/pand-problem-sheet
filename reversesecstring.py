#This program takes a string input and prints every second letter backwards
#author: Stephen Caulfield

#user input for string
inString = input("please enter a string:")

#takes length of string as an integer
i = len(inString)

#removes every second letter from string starting starting with first letter(in "the"; "t" is removed)
secLetter = inString[1:i:2]

#creates the processed string backwards
backString = secLetter[::-1]

#prints final output to user
print(backString)