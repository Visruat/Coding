# INHERITANCE

## Introduction 

> Parent(attr, methods) -> Child(attr++, methods++)

Inheritance is the capability of one class to derive or inherit the properties from another class. 

***Syntax***

```
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
```

#### Subclassing (Calling constructor of parent class)

This involves invoking the "\_\_init\_\_" of the parent in the child class. This is done to ensure on initialization of the child object even the parent attritbutes are invoked to be able to use both child and parent methods.

"\_\_init\_\_" is a contructor that is executed during initialization of an instance/object.


***What is an object class?***

The object is the root of all classes. In other words the base class.

- In Python 3.x, “class Test(object)” and “class Test” are same. 
- In Python 2. x, “class Test(object)” creates a class with the object as a parent (called a new-style class), and “class Test” creates an old-style class (without an objecting parent). 

***Example***

```
# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()

```

#### The super() Function

The super() function is a built-in function that returns the objects that represent the parent class. It allows to access the parent class’s methods and attributes in the child class

***Example***

```
# parent class
class Person1():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

class Person2():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.age, self.name)

# child class
class Student(Person2, Person1):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rahul", age)

  def displayInfo(self):
    print(self.sName, self.sAge)

obj = Student("Mayank", 23)
obj.displayInfo()
obj.display()

```
> Note: 
>- The super() function will invoke the first parent class that is provided to the child class. 
>- It also does not require adding the 'self' as a positional argument.

#### Types of Inheritances

* ***Single inheritance***: When a child class inherits from only one parent class, it is called single inheritance.

* ***Multiple inheritances***: When a child class inherits from multiple parent classes, it is called multiple inheritances. 

```
# Python example to show the working of multiple
# inheritance

class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):

        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()

```

* ***Multilevel inheritance***: When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.

```
# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"

class Base(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    # To get name
    def getAge(self):
        return self.age

# Inherited or Sub class (Note Person in bracket)


class GrandChild(Child):

    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    # To get address
    def getAddress(self):
        return self.address


# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())

```

* ***Hierarchical inheritance***: More than one derived class can be created from a single base.
* ***Hybrid inheritance***: This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.

## Method Overriding

The process occurs when the subclass (child) has all a method with the same name, the same parameters and the same return type as the super class (parent).

![image2](https://media.geeksforgeeks.org/wp-content/uploads/20200114114917/overriding-in-python.png)

```
# Python program to demonstrate 
# Defining parent class 
class Parent(): 
    
    # Constructor 
    def __init__(self): 
        self.value = "Inside Parent"
        
    # Parent's show method 
    def show(self): 
        print(self.value) 
        
# Defining child class 
class Child(Parent): 
    
    # Constructor 
    def __init__(self): 
        super().__init__()  # Call parent constructor
        self.value = "Inside Child"
        
    # Child's show method 
    def show(self): 
        print(self.value) 
        
# Driver's code 
obj1 = Parent() 
obj2 = Child() 

obj1.show()  # Should print "Inside Parent"
obj2.show()  # Should print "Inside Child"
```

#### Accessing the Parent Class Method after it has been Overriden

This is achieved by using super()

```
# Python program to demonstrate 
# calling the parent's class method 
# inside the overridden method using 
# super() 
class Parent(object): 
    
    def show(self) -> str: 
        print("Inside Parent") 
        
class Child(Parent): 

    def __init__(self, Enable=True) -> None:
        self.Enable = Enable
    
    def show(self) -> str: 
        
        if(self.Enable):
            print("Inside Child") 
        else:
            super().show() 
        
        
# Driver's code 
obj = Child(False) 
obj.show() 

```

#### Operator Overload

Can be explored later; not a requirement.

|Operator |	Magic Method|
| :-------: | ----------- |
|\+	      |\_\_add\_\_(self, other)|
|–	      |\_\_sub\_\_(self, other)|
|\*	      |\_\_mul\_\_(self, other)|
|/	      |\_\_truediv\_\_(self, other)|
|//	|\_\_floordiv\_\_(self, other)|
|%	      |\_\_mod\_\_(self, other)|
|\*\*	  |\_\_pow\_\_(self, other)|
|\>\>	  |\_\_rshift\_\_(self, other)|
|<<	      |\_\_lshift\_\_(self, other)|
|&	      |\_\_and\_\_(self, other)|
||	      |\_\_or\_\_(self, other)|
|^	      |\_\_xor\_\_(self, other)|

|Operator |	Magic Method|
| :----:  | ----------- |
|<	|\_\_lt\_\_(self, other)|
|\>	|\_\_gt\_\_(self, other)|
|<=	|\_\_le\_\_(self, other)|
|\>=|	\_\_ge\_\_(self, other)|
|==	|\_\_eq\_\_(self, other)|
|\!=|	\_\_ne\_\_(self, other)|


|Operator |	Magic Method |
|:------:| -------------- |
|\-=|	\_\_isub\_\_(self, other)|
|\+=|	\_\_iadd\_\_(self, other)|
|\*=|	\_\_imul\_\_(self, other)|
|/=	|\_\_idiv\_\_(self, other)|
|//=|	\_\_ifloordiv\_\_(self, other)|
|%=	|\_\_imod\_\_(self, other)|
|\*\*=|	\_\_ipow\_\_(self, other)|
|\>\>=|	\_\_irshift\_\_(self, other)|
|<<=	|\_\_ilshift\_\_(self, other)|
|&=	|\_\_iand\_\_(self, other)|
|\|=	|\_\_ior\_\_(self, other)|
|^=	|\_\_ixor\_\_(self, other)|

|Operator |	Magic Method |
|:-----:| -------------- |
|\-	|\_\_neg\_\_(self) |
|\+	|\_\_pos\_\_(self) |
|~	|\_\_invert\_\_(self) |


Note: It is not possible to change the number of operands of an operator. For example: If we can not overload a unary operator as a binary operator. The following code will throw a syntax error.