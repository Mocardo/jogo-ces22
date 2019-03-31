import numpy as np
from scipy.stats import *

arr = [1, 2, 3]

print(arr)

nu = range(1,6)
x = nu
y = chi2(x,nu)

print(y)


df = 3
vals = chi2.pdf([0.001, 0.5, 10], df)
print(vals)

