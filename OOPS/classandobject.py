class Student: #class is a blueprint or template that encapsulates variables and methods
    role = 'student' #static variable

    # constructor : constructor is called whenever object of class is created
    def __init__(self, roll_no):  #self is an in built variable that points to current object
        self.roll_no = roll_no    #instance variable

# Where we can declare Instance Variables:
# 1) Inside Constructor by using self variable
# 2) Inside Instance Method by using self variable
# 3) Outside of the class by using object reference variable

# Various Places to declare Static Variables:
# 1) In general we can declare within the class directly but from out side of any method
# 2) Inside constructor by using class name
# 3) Inside instance method by using class name
# 4) Inside classmethod by using either class name

# local variable
# variables which are declared inside method ithout using self variable -> cls.name

# Instance method
# inside method if we are using instance variable, then that method is called instance method

# class method
# method which is we use only static variable (class variable)
# we can declare class method using @classmethod decorator
# variable is declared using cls variable

# Static method
# inside static methods no instance or class variable is used

class Prac:

    a = 10

    def meth(self):
        self.c = 100

    @classmethod
    def prac1(cls):
        Prac.a = 20

    @staticmethod
    def prac2():
        Prac.a = 30

t = Prac()
print(t.a)
t.prac1()
print(t.a)
t.prac2()
print(t.a)



ss = 'saagggaarr'
print(ss.count('a'))

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
        super().__init__(uni_name) #Par.__init__() can also be used

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
