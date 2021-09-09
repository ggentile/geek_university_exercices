import numpy as np

a = np.zeros((5, 5))
np.fill_diagonal(a, 1)
print(a)