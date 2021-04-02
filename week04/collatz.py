#This programs asks the user to input any positive integer
#divides by 2 if even
#multiplies by 3 and adds 1 if odd
#continues to do so until result is 1
#prints out each answer

#author: Stephen Caulfield

i = -1

#Buffers for positive integer
while i < 0:

    i = int (input("Enter a positive integer:"))

    if i < 0:

        print("not a postive integer")

#Casts the user input to a string
result = str(i)+" "

#Performs Algorithm Requested
while i != 1:

    n = i % 2
    
    if n == 0:
        i = int(i / 2)
    
    else:
        i = int(i * 3 + 1)
        
    #ammends i to printed result
    result += str(i) + " "

print(result)