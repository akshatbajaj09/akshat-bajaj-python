# Inheritance: 
# When one class takes the attributes and methods from another class then this 
# comes under the idea of inheritance.
# The class which passes the attributes and methods is the parent class and the one
# which inherits them is the child class.
# Benefits:
# It increases reusability and hence makes the code clean and efficient.

# Example:
# Basic:
class Animal:
    def sound(self):
        print('Some sound')

class Dog(Animal):
    def breed(self):
        print('Golden Retriever')
    
obj = Dog()
obj.sound()
obj.breed()

# Method overriding
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

obj2 = Car()
obj2.start()
# The child class overrides the method of the parent class.
obj3 = Vehicle()
obj3.start()
# However the original method in the parent class stays same.

#Creating new method in the child class:
class Person:
    def greet(self):
        print("Hello!")

class Student(Person):
    def study(self):
        print("I'm studying Python.")

obj4 = Student()
obj4.greet()
obj4.study()

# Notice how we didn't use the __init__ method in the above examples because
# there is no need to pass any arguments in the parent class.

# The isinstance function:
print(isinstance(obj, Dog))             # True
print(isinstance(obj, Animal))          # True

# Everything in Python is an object because all classes either directly or indirectly 
# inherit from the built-in base class object.

print(isinstance(Vehicle, object))      # True
print(isinstance(Dog, object))          # True
print(isinstance(obj3, object))         # True