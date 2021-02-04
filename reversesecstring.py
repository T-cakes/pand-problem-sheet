inString = input("please enter a string:")
i = len(inString)
secLetter = inString[1:i:2]
backString = secLetter[::-1]
print(backString)