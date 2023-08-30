str1 = "my name is sagar. I'm a software engineer"

str1 = str1.split()

longest = ''
has_dups = False
for s in str1:
    if len(s)>len(longest):
        for ss in s.split():
            if s.count(ss)!=1:
                has_dups = True
        if has_dups==False:
            longest = s
    has_dups = False

print(longest)

