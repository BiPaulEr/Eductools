import numpy as np
from eductools.numpy_tools import add, subtract

a = 3 * np.eye(3)
b = 5 * np.eye(3)
print(f"{a} +  {b} =\n {add(a,b)}")
print(f"{a} - {b} =\n {subtract(a, b)}")
