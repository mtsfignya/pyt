import random
A = random.randrange(-3,3)
B = random.randrange(-3,3)
print("Число A:", A)
print("Число B:", B)
if A != B:
    A = B = A+B
else:
    A = B = 0
print("Число A:", A)
print("Число B:", B)