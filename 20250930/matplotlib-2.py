#-* coding :utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

y = [5, 3, 7, 10, 9, 5, 3.5, 8]
x = range(len(y))
colors=['red' if val>7 else 'blue' for val in y]
plt.bar(x, y, width=0.4, color=colors)
plt.title("bar graph",fontsize='20',c='g',fontweight='bold')
plt.xlabel('hi', fontsize=12, fontweight='bold')
plt.ylabel('bye', fontsize=12, fontweight='bold')
plt.show()