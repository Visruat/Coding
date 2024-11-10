# OBJECT ORIENTED PROGRAMMING STRUCTURES (OOPS)

## Introduction

The main concept of object-oriented Programming (OOPs) or oops concepts in Python is to bind the data and the functions that work together as a single unit so that no other part of the code can access this data.

**Core OOP Principles:**
- classes 
- objects 
- inheritance
- encapsulation
- polymorphism
- abstraction

#### Classes

> Class(attributes, methods)

Class is a collection of objects of a certain State, Behavior and Identity. These objects are defined by the classes attributes and methods.

#### Objects

> Object(Identity, State, Behavior)

An Object is an entity that consists of a **State, Behavior and Identity**. They can classify under a collection of objects called classes. When a Class is called by an instance, the object initialization takes place where the 3 components(Mainly State and Behavior) are defined the by **Class's attributes and methods**.

In Short, everything used in Python is a object that can be part of a certain class. For Example,  "int" is a class and the instance calling it becomes the object of class "int".

***Example***

```
class Dog:

    # class attribute
    attr1: str= "mammal"

    # Instance attribute
    def __init__(self, name: str) -> None:
        self.name = name
        
    def __str__(self) -> str: 
        return(f"{self.attr1 = } and {self.name = }")
    
    def bark(self) -> str:
        return(f"'Woof!' by {self.name}")

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
print(Rodger)
print(Rodger.bark())
print(Tommy)
print(Rodger.bark())
```

#### Encapsulation

The concept of tying all data and methods that are used to perform certain tasks in one unit. It also limits the accessibility of the data and methods.

![example1](https://media.geeksforgeeks.org/wp-content/uploads/20191013164254/encapsulation-in-python.png)

***Example***

```
# Python program to
# demonstrate private members
# "__" double underscore represents private attribute. 
# Private attributes start with "__".

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks" 

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


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
```

#### Data Abstraction

It hides unnecessary code details from the user. Also,  when we do not want to give out sensitive parts of our code implementation and this is where data abstraction came.

***Example***

```
class Rectangle:
    def __init__(self, length, width):
        self.__length = length  # Private attribute
        self.__width = width    # Private attribute

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")          # Output: Area: 15
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 16

# print(rect.__length)  # This will raise an AttributeError as length and width are private attributes
```

#### Inheritance

> Parent(attr, methods) -> Child(attr++, methods++)

The ability of a child class to derive the attributes and methods from a Parent class is called Inheritance.

**Types:**

- Single Inheritance: Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.
- Multilevel Inheritance: Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from its parent class. 
- Hierarchical Inheritance: Hierarchical-level inheritance enables more than one derived class to inherit properties from a parent class.
- Multiple Inheritance: Multiple-level inheritance enables one derived class to inherit properties from more than one base class.

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
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
    
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()
```

> Note: 
> - The Parent Class was Passed as an Arguement to the Child Class.
> - The object keyword is a base class. It cannot take any arguments and returns a new featureless instance that has no attributes and cannot be added to as well.

#### PolyMorphism

The Concept which states that a class can have many forms which can have the main functionality retained but certain methods can have different approaches to achieve the result. For Example, A car does the same work but it can be of Manual Transmission or Automated Transmission

***Example***

```
class Bird:
  
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
  
    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

```

> Note: The Polymorphism seems to make use of the concept of Inheritance.

#### Summary

> Overall, The OOPS Principles are inter linked to each other but separated by different names to highlight the use cases. Exploring all in detail should give a good undertanding before starting automation in full swing.