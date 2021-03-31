#This program finds square root of a number without using built in functions

#author: Stephen Caulfield

#Method of finding square root: https://www.youtube.com/watch?v=PJHtqMjrStk&ab_channel=tecmath


def sqrt(num):
    sqrnum = 0.0 

    basenum = 1.0 

    #Loops through numbers to find closest squared number to input number
    while sqrnum < num:
        
        sqrnum = basenum**2

        if sqrnum < num:
            basenum += 1

        else:
            basenum -= 1

    #Takes the closest squared integer under input and subtracts it from input
    sqrnum = basenum**2    

    numerator = num - sqrnum 

    denominator = basenum*2

    #gets decimal part of answer   
    decnum = numerator/denominator 

    answer = basenum + decnum 

    return answer

var = sqrt(138)

print(var)

