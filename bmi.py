#This program calculates the user's BMI using their inputs
#author: Stephen Caulfield

#inputs for height and weight
weight = float (input ("enter weight: "))
height = float (input ("enter height: "))

#conversion of centimetres to metre squared
metresquared = (height/100)**2

#calculation of BMI
BMI = round(weight / metresquared, 2)

#BMI output
print("BMI is {}".format(BMI))