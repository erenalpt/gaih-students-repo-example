import random
from sympy import randprime

rndPrmMatrix = [[random.choice([x for x in range(2, 1000) if not [t for t in range(2, x) if not x % t]]) for x in range(3)] for x in range(3)]

# for sympy
# rndPrmMatrix = [[randprime(0, 100) for x in range(3)] for x in range(3)]

print(rndPrmMatrix)

#for i in range(3):
#    print(rndPrmMatrix[i])

# Exam Output: [[821, 163, 643], [467, 67, 563], [971, 109, 349]]
