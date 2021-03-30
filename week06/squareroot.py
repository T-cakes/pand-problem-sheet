#This program squares a number without using built in functions

#author: Stephen Caulfield

def sqrt(num):
    y = 0.0
    x = 1.0
    while y < num:
        y = x**2
        if y < num:
            x += 1
        else:
            x -= 1
    y = x**2
    z = num - y
    n = x*2
    o = z/n
    p = x + o
    return p

var = sqrt(138)

print(var)

