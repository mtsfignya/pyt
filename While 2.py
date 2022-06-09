import random
A = random.randrange(50,100)
B = random.randrange(1,A)
print('A = ', A)
print('B = ', B)
r = A - B
n = 1
while r >= B:
    r -= B
    n += 1
print("Количество размещений B в A: ", n)
print("Остаток: ", r)