str1 = 'nitin'
str2 = ''

#approach
for i in range(len(str1)-1, -1, -1):
    str2 += str1[i]
    print(str1[i])
print(str1==str2)

# approach2
print(str1==str1[::-1])