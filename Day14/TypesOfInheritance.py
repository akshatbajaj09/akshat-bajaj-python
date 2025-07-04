# There are mainly 5 types of inheritance:
# Single, Multilevel, Hierarchical, Multiple and Hybrid.

# Single inheritance: One parent and one child (A -> B). 
class Device:
    def power_on(self):
        print('Powering on...')
class Phone(Device):
    def make_call(self):
        print('Making a call...')
# Device -> Phone.
obj1 = Phone()
obj1.power_on()
obj1.make_call()

# Multilevel inheritance: A child class inherits from other child class which itself inherits
# from a parent class (A -> B -> C).
class Organism:
    def alive(self):
        print('I\'m alive.')
class Animal(Organism):
    def move(self):
        print('I can move.')
class Cat(Animal):
    def meow(self):
        print('Meow!')
# Organism -> Animal -> Cat.
obj2 = Cat()
obj2.alive()
obj2.move()
obj2.meow()

# Hierarchical inheritance: When two or more child classes inherits from the same parent class
# (A -> B, A -> C).
class Shape:
    def identify(self):
        pass
class Circle(Shape):
    def identify(self):
        print('I\'m a circle.')
    def area_circle(self):
        radius = int(input('Please enter the radius of the circle: '))
        print(f'The area of a circle is {3.14*radius ** 2}.')
class Square(Shape):
    def identify(self):
        print('I\'m a square.')
    def area_square(self):
        side_length = int(input('Enter the side length of the square please: '))
        print(f'The area of a square is {(side_length) ** 2}.')
# Shape -> Circle, Shape -> Square.
obj3 = Circle()
obj4 = Square()
obj3.identify()
obj4.identify()
obj3.area_circle()
obj4.area_square() 

# Multiple inheritance: One child class inherits from two or more parent classes
# (A -> C, B -> C).
class Dancer:
    def dance(self):
        print('Dancing...')
class Singer:
    def sing(self):
        print('Singing...')
class Performer(Dancer, Singer):
    def perform(self):
        print('Performing...')
# Dancer -> Performer, Singer -> Performer.
obj5 = Performer()
obj5.dance()
obj5.sing()
obj5.perform()

# Hybrid inheritance: It is the mix of two or more types of inheritances. Example:
#         Employee
#            |
#         Engineer
#            |
#       +---------+
#       |         |
#    Manager   Researcher
#            |
#        TechLead
# Employee -> Engineer -> Manager
# Employee -> Engineer -> Researcher
# Manager, Researcher -> TechLead
class Employee:
    def work(self):
        print('Working...')
class Engineer(Employee):
    def code(self):
        print('Coding...')
class Manager(Engineer):
    def manage(self):
        print('Managing...')
class Researcher(Engineer):
    def explore(self):
        print('Exploring...')
class TechLead(Manager, Researcher):
    def lead(self):
        print('Leading...')
obj6 = TechLead()
obj6.work()
obj6.code()
obj6.manage()
obj6.explore()
obj6.lead()
