# str1 = "my name is sagar"
# ll = []
# ll.append(str1[0].upper())
# for i, j in enumerate(str1):
#     print(i, j)
#     if str1[i-1] == ' ':
#         ll.append(j.upper())
#
#
# print(ll)

str1 = "eleven plus two"
str2 = "twelve plus one"

str1 = str1.replace(' ', '')
str2 = str2.replace(' ', '')

str1 = list(str1)
str2 = list(str2)

str1.sort()
str2.sort()
print(str1, str2)
print(str1==str2)
