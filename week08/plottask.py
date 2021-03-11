import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4])

plt.plot(x, '-bo', label = 'f(x)')
plt.plot(x**2, '-go', label = 'g(x)',)
plt.plot(x**3, '-ro', label = 'h(x)')


plt.legend()
plt.xlabel('x')
plt.ylabel('Function')
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.grid(color='grey', linestyle='-', linewidth=.1)
plt.show()