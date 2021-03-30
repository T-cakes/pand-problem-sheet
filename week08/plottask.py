#displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
#in the range [0, 4] on the one set of axes.

#author: Stephen Caulfield

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4]) #creates array wioth numbers o-4

plt.plot(x, '-bo', label = 'f(x)')  #plotting f(x) = x

plt.plot(x**2, '-go', label = 'g(x)',)  #plotting g(x) = x**2

plt.plot(x**3, '-ro', label = 'h(x)')   #plotting h(x) = x**3

plt.legend()    #creates legend for graph

plt.xlabel('x') #labels x axis as 'x'

plt.ylabel('Function')  #labels y axis as 'function'

plt.xticks(np.arange(min(x), max(x)+1, 1))    #https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib

plt.grid(color='grey', linestyle='-', linewidth=.1) #creates a grid for clearer presentation

plt.show()  #displays graph