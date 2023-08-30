# Overloading
# 1) Operator Overloading
# 2) Method Overloading
# 3) Constructor Overloading
# 3) Overriding
# 1) Method Overriding
# 2) Constructor Overriding

# Overloading
# We can use same operator or methods for different purposes.
# Eg 1: + operator can be used for Arithmetic addition and String concatenation
# print(10+20)#30
# print('durga'+'soft')#durgasoft

# We can use deposit() method to deposit cash or cheque or dd
# deposit(cash)
# deposit(cheque)
# deposit(dd)

# There are 3 types of Overloading
# 1) Operator Overloading
# 2) Method Overloading
# 3) Constructor Overloading

# Method overloading
class Over:
    def ovrld(self, *args):
        summ = 0
        for arg in args:
            summ = summ + arg
        print(summ)

ov = Over()
ov.ovrld(1,2,3,4,5)

# Constructor overloading
class Co:
    def __init__(self, *arg):
        print(arg)

co = Co(1,2,3,4)

# Method overriding

class Pa:
    def name(self):
        print('Pa')

class Ch(Pa):
    def name(self):
        print('Ch')

pa = Pa()
pa.name()
ch = Ch()
ch.name()

# constructor overriding
class Par:
    def __init__(self):
        print("I'm parent")

class Chi(Par):
    def __init__(self):
        # Par.__init__(self)
        print("I'm child")

p = Par()
c = Chi()