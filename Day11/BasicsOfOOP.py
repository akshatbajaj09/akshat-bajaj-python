# As we know that one of the benefit of OOP is to make real world objects and run methods on them, so
# let's create a class of Company in which employees have details like name, age and salary.

class Company:        # Naming convention is to capitalize the name of class and use camelcase.
    bonus = 1.04
    def __init__ (self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def increase(self):
        self.salary = int(self.salary * self.bonus)
        return self.salary 
    def details(self):
        print(dict(Name = self.name, Age = self.age, Salary = self.salary))
        return f'Above are all the details of {self.name}.'
employee1 = Company('Akshat', 20, 100000)
employee1.bonus = 1.2
employee2 = Company('Test', 22, 50000)

print(employee2.age)
print(employee1.salary)
print(employee2.salary)

employee1.increase()
employee2.increase()
print(employee1.salary)
print(employee2.salary)

print(employee1.details())
print(Company.details(employee1))



# Class variables and instance variables
# The bonus = 1.04 is a class variable and is for all instances but let's say employee1 deserves more
# bonus than others so we can create a employee1.bonus = 1.2 variable which is an instance variable
# and is specific to employee1 only.
# How the interpreter works? It looks in the value for a varible at instance level and if not
# found it moves to class level, similar to what we learned in the LEGB rule of functions.