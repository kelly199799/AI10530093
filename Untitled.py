
# coding: utf-8

# In[7]:


# %load sin_graph.py
import numpy as np
import matplotlib.pyplot as plt
# data
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
# plot graph
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()

