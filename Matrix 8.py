import random
import numpy
M = random.randrange(2,10)
N = random.randrange(2,10)
K = random.randrange(0,N)
print("M = ",M,"; N = ",N,"; K = ",K)
a = numpy.zeros((M, N))
for i in range(M):
    for j in range(N):
        a[i][j] = random.randrange(-5,5)
print(a)
print("Column ",K,": ")
for i in range(M):
    print(a[i][K],end="; ")
print()
Matrix = [[random.randrange(-5,5) for x in range(N)] for y in range(M)]
print(Matrix)
print("Column ",K,": ")
for i in range(M):
    print(Matrix[i][K],end="; ")
print()