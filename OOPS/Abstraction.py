# Abstract Method:
# Sometimes we don't know about implementation, still we can declare a method. Such types of methods are called abstract methods.i.e abstract method has only declaration but not implementation.
# In python we can declare abstract method by using @abstractmethod decorator as follows.
from abc import *

@abstractmethod
def m1():
    pass

# @abstractmethod decorator present in abc module. Hence compulsory we should import abc module,otherwise we will get error.
# abc -> abstract base class module

class Abst:
    @abstractmethod
    def m1(self):
        pass

# Child classes are responsible to provide implemention for parent class abstract methods.

# CASE1
class Test(ABC):
    pass

t=Test()

# In the above code we can create object, even it is derived from ABC class,b'z it does not contain any abstract method.

# CASE2
class Abst2(ABC):
    @abstractmethod
    def m2(self):
        pass

# abs = Abst2()
# TypeError: Can't instantiate abstract class Abst2 with abstract method m2

# CASE3
class Test:
    @abstractmethod
    def m1(self):
        print("Hello")

t1 =Test()
t1.m1()

# We can create object even class contains abstract method b'z we are not extending ABC

"abstract class with abstract method instantiation is not possible"

'''If we are extending abstract class and does not override its abstract method then child class is also abstract and instantiation is not possible.'''

class Vehicle(ABC):

    @abstractmethod
    def noofwheels(self):
        pass

class Auto(Vehicle):

    def noofwheels(self):
        return 3

auto = Auto()
print(auto.noofwheels())


## Interfaces In Python:
# In general if an abstract class contains only abstract methods such type of abstract class is considered as interface.