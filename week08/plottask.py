#displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

#author: Stephen Caulfield

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4])

#plotting f(x) = x
plt.plot(x, '-bo', label = 'f(x)')  

#plotting g(x) = x**2
plt.plot(x**2, '-go', label = 'g(x)',)  

#plotting h(x) = x**3
plt.plot(x**3, '-ro', label = 'h(x)')   

plt.legend()

plt.xlabel('x')

plt.ylabel('Function')

#Puts a dot at each point on the graph (https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib)
plt.xticks(np.arange(min(x), max(x)+1, 1))
plt.yticks(np.arange(0, 80, 10)) 

plt.grid(color='grey', linestyle='-', linewidth=.6) 

plt.savefig('graph.png')  

plt.show()