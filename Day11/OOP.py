# Why do we need Object - oriented programming (OOP)?
# Answer:
# 1: It offers a paradigm to think, order and structure our code.
# 2: It helps us to bunch up reusable and similar patterns in long codes.
# 3: It helps us simulate real life objects and attributes (properties) related to them like:
# we can create an object named car and run methods on it like accelerate() or honk() etc.

# Terminologies: classes, objects, instances and instantiating.
# Classes are like a blueprint and an object is an actual thing made from that blueprint.
# Instances are different objects, and instantiating is the process of creating an object 
# from the class.

# Example:
class Phone:    # Naming convention is to capitalize the name of class and use camelcase.
    def __init__ (self, brand, price):
        self.brand = brand
        self.price = price
    def details(self):
        print(f'Brand: {self.brand}, Price: {self.price}')
apple_phone = Phone('Apple', 100000)
samsung_phone = Phone('Samsung', 100000)

# In the above example:
# Class: Phone
# Objects or instances: apple_phone and samsung_phone
# Instantiating means creating an object using the class like done in the lines:
# apple_phone = Phone('Apple', 100000) and samsung_phone = Phone('Samsung', 100000).