import numpy as np
from scipy.stats import *
import math
import random
"""
arr = [1, 2, 3]

print(arr)




df = 3
vals = 1/(0.1+chi2.cdf([0.001, 0.5, 10, 100], df))
print(vals)

teste = chi2.rvs(df,size = 10)
print(teste[0])

vals = []


qtde = 1000
k = 1

i = 1

level = []

while len(level) < qtde:
    level.append(chi2.rvs(i, size = 1))
    i = i+1
print(level)


while len(vals) < qtde:

    vals.append(math.ceil(1/(0.1+chi2.cdf(chi2.rvs(i,size = 1), i))))
    i = i+1
print(vals)
"""

""""""""""""""""""""


"vou querer q a entrada seja um numero aleatorio entre 0 e 90% da cdf"
qtde = 300
nivel = 10
"entradas = (chi2.rvs(nivel, size = qtde))"
upperlimit = 10 + math.floor(chi2.ppf(0.90,nivel))
entradas = [random.randrange(1, upperlimit) for _ in range(qtde)]
dificuldade = []
i = 0
while len(dificuldade) < qtde:
    dificuldade.append(math.ceil(1/(0.1+chi2.cdf(entradas[i], nivel))))
    i = i+1

"print(dificuldade)"


sum = 0
for cell in dificuldade:
    sum = sum + cell


mean = sum/len(dificuldade)
print(mean)
"print(entradas)"




