import numpy as np
from bqplot import pyplot as plt

size = 100
np.random.seed(0)
x_data = np.arange(size)
y_data = np.cumsum(np.random.randn(size)  * 100.0)

plt.figure(title='My First Plot')
plt.plot(x_data, y_data)
plt.show()
