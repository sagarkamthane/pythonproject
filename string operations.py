s = ' my name is sagar, sagar is my name '

print(s.rstrip())
print(s.lstrip())

text = "Hello World!!!"
print(text.strip('!'))
print(text.strip('H'))

print(s.find('sagar'))
print(s.rfind('sagar'))
print(s.find('sagar', 12, 25)) #finds from index 12 to 25
print(s.find('ocean')) #returns -1 as sub string not found
print(s.index('sagar'))
print(s.rindex('sagar'))


l = ['1', '2', '3']
name = 'sagar'
print(f'my name is {name}')



mama = [1,2,3,4]
kaka = [5,6,7,8]
mama[2:2] = kaka
print(mama)


l1 = [x for x in range(0,101,2)]
print(l1)

s = set()
s.update(range(5))
print(s)


r = {1:1, 2:3, 3:5}
print(r.get(2))

for i,j in r.items():
    print(j if i == 2 else '')

dic1 = {x:x**2 for x in range(10) }
print(dic1)

s = lambda a,b : a**2+b**2
print(s(2,4))