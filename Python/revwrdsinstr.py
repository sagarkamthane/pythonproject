str1 = "Hello World"

l1 = str1.split()
l2 = []
print(l1)
for i in l1:
    l2.append(i[::-1])

print(' '.join(l2))

# factorial

n = 10