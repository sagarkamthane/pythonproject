# Creating a Dictionary:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing Value
name = my_dict["name"]

# Adding or Modifying Elements:
my_dict["age"] = 25 #modifying dictionary
my_dict["job"] = "Engineer" #adding new key value pair

# Removing Elements:
del my_dict["city"]
my_dict.pop("name") # my_dict.pop("name", 0) returns 0 if "name" key is not present

# Checking Key Existence:
print("job" in my_dict)

# Getting Keys and Values:
print(my_dict.keys())
print(my_dict.values())

# Iterating Through a Dictionary:
for key in my_dict:
    print(key, my_dict[key])

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

# Clearing
# my_dict.clear()

# Dictionary Comprehension:
Squares = {str(X):str(X**2) for X in range(1, 11)}
print(Squares)

Cubes = {str(X):str(X**3) for X in range(11, 21)}
print(Cubes)

# Getting a Default Value:
age = my_dict.get("age", 0)  # Returns the value for "age" or 0 if not found

# Merging Dictionaries:
SQ = dict(**Squares, **Cubes)
print(SQ)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = dict1
for a in dict2:
    dict3[a] = dict2[a]
print(dict3)

# Dictionary Views
keys_view = my_dict.keys()       # View of keys
values_view = my_dict.values()   # View of values
items_view = my_dict.items()
print(Squares.keys(), values_view, items_view)

# Sorting a Dictionary:
dict_d = {x:str(x) for x in range(10, 0, -1)}
dict_d2 = {}
for keys in sorted(dict_d):
    dict_d2[keys] = dict_d[keys]

print(dict_d2)
