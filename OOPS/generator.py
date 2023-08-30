# generator

def give_square():
    for i in range(10):
        yield i**2


a = give_square()

for sq in a:
    print(sq)

# iterator:

# Iterable (list)
my_list = [1, 2, 3, 4, 5]

# Creating an iterator from the iterable
my_iterator = iter(my_list)

# Using the iterator to get values
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
# ...

# Using the iterable with a for loop
for item in my_list:
    print(item)

