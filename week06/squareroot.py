#This program finds square root of a number without using built in functions

#author: Stephen Caulfield

#Method of finding square root: https://www.youtube.com/watch?v=PJHtqMjrStk&ab_channel=tecmath


def sqrt(num):
    y = 0.0 
    x = 1.0 #will equal closest squared integer to input

    #Loops through numbers to find closest squared number to input number
    while y < num:
        y = x**2

        if y < num:
            x += 1
        
        else:
            x -= 1

    #Takes the closest squared integer under input and subtracts it from input
    y = x**2    
    z = num - y

    n = x*2 #denominator of the answer is x times 2
    o = z/n #gets decimal part of answer   
    p = x + o #puts the whole number and decimal for the approximate square root of input
    return p

#calls function 'sqrt'
var = sqrt(138)

print(var)

