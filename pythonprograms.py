# Write a Program to reverse a string without using String inbuilt function.
s = 'my name is sagar'
rs = ''
for i in range(len(s)-1, -1, -1):
    rs = rs + s[i]

print(rs)

# Write a Java Program to swap two given Strings
s1 = 'my name is sagar'
s2 = "I'm engineer"

s2, s1 = s1, s2
print(s1, s2)
