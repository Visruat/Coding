# Python program to
# demonstrate private members
# "__" double underscore represents private attribute. 
# Private attributes start with "__".

# Creating a Base class
class Base:
    def __init__(self) -> None:
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks" 

    def __str__(self) -> str: 
        return(f"{self.__c = }")

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
    
    def __str__(self) -> str: 
        return(f"{self.__c = }")


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# print(obj1.c)

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class\

# obj2 = Derived()
# print(obj2)