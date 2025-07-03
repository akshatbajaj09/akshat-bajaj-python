# Abstraction means hiding the internal implementation details and
# only exposing the essential parts.

# Abstract classes prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod

# For now, the above thing is used to setup the working on abstract classes and I don't know 
# what exactly is this, but it will be understood after we learn modules.

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car.")

    def stop(self):
        print("This car is stopped.")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle.")

    def stop(self):
        print("This motorcycle is stopped.")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

# vehicle.stop()
car.stop()
motorcycle.stop()