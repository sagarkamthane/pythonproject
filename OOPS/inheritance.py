class Grandpa:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Im grandpa', self.name, self.age)


class Papa(Grandpa):
    def __init__(self, gname, gage, name, age):
        Grandpa.__init__(self, gname, gage)
        self.name = name
        self.age = age
        print('Im papa', self.name, self.age)

class Son(Papa):
    def __init__(self, gname1, gage1, pname, page, name, age):
        Grandpa.__init__(self, gname1, gage1)
        Papa.__init__(self, gname1, gage1, pname, page)
        self.name = name
        self.age = age
        print('Im son', self.name, self.age)


son = Son('shankar', 80, 'sanjeev', 50, 'sagar', 25)



# single inheritance


class Par:
    def __init__(self):
        self.a = 10


class Ch(Par):
    def __init__(self):
        super().__init__() #Par.__init__() can also be used

c = Ch()
print(c.a)  # Outputs: 10 20


class Uni:
    def __init__(self, uni_name):
        self.uni_name = uni_name


class Stu(Uni):
    def __init__(self, uni_name):
        super().__init__(uni_name) #Uni.__init__(self, uni_name) can also be used

c = Ch()
print(c.a)  # Outputs: 10 20

# multiple inheritance



# Method Resolution Order (MRO):
# In Hybrid Inheritance the method resolution order is decided based on MRO algorithm.
# This algorithm is also known as C3 algorithm.
# Samuele Pedroni proposed this algorithm.
# It follows DLR (Depth First Left to Right) i.e Child will get more priority than Parent.
# Left Parent will get more priority than Right Parent.
# MRO(X) = X+Merge(MRO(P1),MRO(P2),...,ParentList)


class A:
    statvar = 'Sa'
    def __init__(self, a):
        self.a = a

    def instm(self):
        print(self.statvar, self.a)

    @staticmethod # we can't use instance variables in staticmethod , we can use class variable using class name
    def statm():
        print(A.statvar)

    @classmethod #we can't use instance variable
    def clsm(cls):
        print(cls.statvar)

cla = A(5)