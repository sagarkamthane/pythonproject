# complex data type
import sys

c = 10 + 20j
d = 20 + 30j

print(c+d)
print(c.real, c.imag)

e = complex(10,5)
print(e)

#bool data type
a = True
b = False

#

print(bool(None))

#if two objects have same value, then objects are stored at same memory location
nn = 10 + 5j
mm = 10 + 5j

print(nn is mm, id(nn), id(mm))

# list
aa = [10, 20, 30]
aa.append(40)
aa.extend([50, 60, 70])
aa.remove(70)
print(aa)

val_to_rem = [50,60]
newlist = [x for x in aa if x not in val_to_rem]
print(newlist)

t1 = [1,2,3]
print(id(t1))
t2 = [4,5,6]
t1 += t2
print(id(t1))
print(t1, type(t1))



# use range data type to create list

list1 = list(range(10))
list2 = list(range(50,56))
list1[2:2] = list2
print(list1)
list1 = list(range(10))
list3 = list1[:2] + list2 + list1[2:]
print(list3)

s = "my name is sagar".split()
eve, vfv, fr, vf = s
print(eve, vfv, fr, vf)

lo = 5
jo = 6
if lo > jo:
    print(lo)
else:
    print(jo)


for i in range(5):
    print(((4-i)*' ')+ (i*2+1)*'*')

for i in range(1, 4 + 1):
        print(" " * (4 - i) + "*" * i)

n = 5
for i in range(1, n+1):
    print((n-i)*' ', end = '')
    print(i*'* ')

s="Learning Python is very easy"
print(s.find("Python")) #9


s = 'abababababababab'
for i, j in enumerate(s):
    if j == 'a':
        print(i)

# assert 5 in [1,2,3,4]


def addbraces(func):
    def brace(text):
        result = func(text)
        return '('+str(result)+')'
    return brace


@addbraces
def tuplenobrace(a):
    return a

print(tuplenobrace(1))


def gen():
    for i in range(10):
        yield i


for i in gen():
    print(i)


t = (4,5,3,2,6,7,1)
t = sorted(t)
print(t, type(t))

ls = [1,2,3,4,5,3,4,6,1,1,1,1]
ls = [ls]

for l in ls:
    ls.remove(l) if ls.count(l)>1 else None

print(ls)

name = 'sagar'
print(id(name))
name = 'sagar'+'k'
print(id(name))

s1 = 'sagar'
s2 = 'sagar'

print(s1==s2)

s2 = ''.join(reversed(s1))
print(s2)

t1 = (1,2,3)
print(id(t1))
t2 = (4,5,6)
t1+=t2
print(t1, id(t1))

print(*t1)

d1 = {1:2, 2:3, 3:4, 4:5, 5:5, 6:5}
d1[3]=3
print(d1)
d1.pop(1)
print(d1)

val = 5
key = [x for x,y in d1.items() if y == val]
print(key)

set1 = {4,5,5,5,5}
set2 = {4,5,6,7,8}

print(set1^set2, set2.issuperset(set1))


name1 = " sagar kamthane"
print(name1.endswith('ne'))
print(list(name1))

lst = [1,1,2,2,3,3,3,4,4,4,4,' ', ' ']
lst2 = []
# lst = set(lst)
# lst.remove(' ')
# print(lst)
[lst2.append(x) for x in lst if x not in lst2]
print(lst2)

a = 2 + 3j
print(a.real, a.imag)

a = 1
b = 10
def pr(a, b):

    if a<=b:
        print(a)
        a+=1
        pr(a, b)
pr(a,b)

a = 'saagaar'
print(a.count('a'))


# generator
def dd():
    for i in range(10):
        yield i+1

a = dd()

for y in a:
    print(y)


def myname(name, age):
    print(name, age)


rew = lambda x: x**2

print(rew(5))




def add_par(func):
    def wrapper():
        r = func()
        r = '(' + str(r) + ')'
        return r
    return wrapper


@add_par
def no_par():
    return 5

a = no_par()
print(a)

l = ['sagar', 'kamthane', 'pune']
la = [li + '\n' for li in l]
with open('file.txt', mode='a') as f:
    f.writelines(la)



ss = 'sagarkamthane'
# sy = ''.join(sorted(ss))
# print(sy)
sss = ''

for s in ss:
    if ss.count(s)==1:
        sss = sss + s
print(sss)


ls = [1,2,3,2,3,4,2,5]

l2 = [l for l in ls if ls.count(l)==1]
print(l2)

lis = [6,6,3,4,5,2,8,9]
i = 0
while i<= len(lis)+2:
    for l in range(len(lis)-1):
        if lis[l] > lis[l+1]:
            lis[l], lis[l+1] = lis[l+1], lis[l]
            i+=1

print(lis)


for i,j in enumerate(range(10,21)):
    print(i, j)

a = iter(range(10))
print(next(a))


sst = '''sagar
kamthane
pune'''

print(sst.replace('\n', ''))

a = 'listen'
b = 'silent'
print(''.join(sorted(a)), ''.join(sorted(b)))

import random
