#0 1 1 2 3 5 8 13
import math
import random

l = [0, 1]

for i in range(2, 10):
    l.append(l[i-1] + l[i-2])

print(l)

n = 23
even = False
for i in range(2, int(round(math.sqrt(n)))+1):
    if n%i == 0:
        even = True
print(even)

l1 = [i for i in range(1,51)]
l2 = [i for i in l1 if i%2 == 0]
print(l2)

print(random.randint(1, 100))

