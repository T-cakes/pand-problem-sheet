#This program calculates the user's BMI using their inputs
#author: Stephen Caulfield

#Creating function to properly round numbers: credit: https://realpython.com/python-rounding/#rounding-half-up
import math
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier
#inputs for height and weight
weight = float (input ("enter weight(KG): "))
height = float (input ("enter height(CM): "))

#conversion of centimetres to metre squared
metreSquared = (height/100)**2

#calculation of BMI
BMI = round_half_up(weight / metreSquared, 2)

#BMI output
print("BMI is {}".format(BMI))