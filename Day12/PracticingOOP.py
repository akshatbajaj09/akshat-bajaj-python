# Create a class named Book with an attribute title.
# Then create two objects:
# One with title "Sapiens"
# One with title "Hamlet"
# Print both titles.
class Book:
    def __init__ (self, title):
        self.title = title
obj1 = Book('Sapiens') 
obj2 = Book('Hamlet')
print(obj1.title)
print(obj2.title)   

# Create a class Car with:
# A class variable wheels set to 4
# An instance variable brand that you set via the constructor
# Then:
# Create two cars: Car("Toyota") and Car("Ford")
# Print both their brand and wheels
# Example output:
# Toyota 4  
# Ford 4
class Car:
    wheels = 4
    def __init__ (self, brand):
        self.brand = brand
car1 = Car('Thar')
car2 = Car('Fortuner')
print(f'{car1.brand} {Car.wheels}')
print(f'{car2.brand} {Car.wheels}')

# Create a class User with:
# Attributes: username and email
# A normal constructor that takes username and email
# A @classmethod named from_string that takes a string in the format: "username-email"
# and returns a User object.
# Create a user using User.from_string("akshat-akshat@email.com")
# Then print the username and email.
class User:
    def __init__ (self, username, email):
        self.username = username
        self.email = email
    @classmethod
    def from_string(cls, string):
        username, email = string.split('-')
        return cls(username, email)
user = User.from_string('akshat-akshat@email.com')
print(user.username)
print(user.email)

# Create a class MathTools with:
# A @staticmethod called add(x, y) that returns the sum of x and y
# Then call it using the class (don’t create any object), 
# and print the result of add(5, 7).
class MathTools:
    @staticmethod
    def add(x, y):
        return x + y
print(MathTools.add(5, 7))

# Create a class Employee that includes:
# Class variable: company = "OpenAI"
# Instance variables: name, role
# A @classmethod called change_company(cls, new_company) to update the class variable
# A @staticmethod called is_valid_role(role) that returns True if
# role is in ["Engineer", "Manager", "HR"], else False
# Then:
# Create an employee e1 = Employee("Akshat", "Engineer")
# Print e1.name, e1.role, and e1.company
# Call change_company("Neuralink")
# Print e1.company again
# Call and print Employee.is_valid_role("Janitor") → should return False
class Employee:
    company = 'OpenAI'
    def __init__ (self, name, role):
        self.name = name
        self.role = role
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
    @staticmethod
    def is_valid_role(role):
        if role in ['Engineer', 'Manager', 'HR']:
            return True
        else:
            return False
e1 = Employee('Akshat', 'Engineer')
print(e1.name)
print(e1.role)
print(e1.company)
e1.change_company('Neuralink')
print(e1.company)
print(Employee.is_valid_role('Janitor'))