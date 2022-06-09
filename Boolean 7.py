import random
A = random.randrange(-10,10)
B = random.randrange(-6,6)
C = random.randrange(-10,10)
print("A = ", A)
print("B = ", B)
print("С = ", C)
x = ((A<B) and (B<C)) or ((C<B) and (B<A))
print("B находится между A и C: ", x)