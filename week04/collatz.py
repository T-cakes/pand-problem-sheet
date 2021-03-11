#This programs asks the user to input any positive integer
#divides by 2 if even
#multiplies by 3 and adds 1 if odd
#continues to do so until result is 1
#prints out each answer

#author: Stephen Caulfield

#initialise i as -1 so it is not a positive integer to engage while loop
i = -1

#Asks user for positive integer repeatedly until postive integer is entered
while i < 0:
    i = int (input("Enter a positive integer:"))
    if i < 0:
        print("not a postive integer")

#amends the user input to a string
result = str(i)+" "

#as long as i is not equal to 1 this will loop
while i != 1:

    #gets modulus of i / 2
    n = i % 2
    
    #will divide by 2 if modulus i is 0
    if n == 0:
        i = int(i / 2)
    
    #will multiply by 3 and add 1 if modulus i/2 is not 0
    else:
        i = int(i * 3 + 1)
        
    #ammends i to printed result
    result += str(i) + " "

#prints the end result
print(result)
    

