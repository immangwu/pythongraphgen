import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(100000)
plt.hist(x,1000)
plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
plt.savefig('matplotlib_histogram1.png');
plt.show()
