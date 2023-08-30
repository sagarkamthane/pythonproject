# list comprehension
lista = ['my', 'name', 'is', 'sagar']
listc = lista[::-1]
listb = [f'{x} : {len(x)}' for x in lista[::-1]]
print(listb, listc)

