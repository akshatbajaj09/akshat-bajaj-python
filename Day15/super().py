# super(): 
# super() is a built-in function that lets you
# call methods of a parent class from a child class.
# Benefits:
# Makes code efficient by increasing reusability and we don't need
# to define the methods again in the child classes.
# We could also use the name of Parent class to call our method but that isn't 
# recommended as it does not work well with cases involving multiple inheritance.

# Example:
class Vehicle:
    def __init__(self, brand):
        print('Vehicle created: ', brand)
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        print(f'Car created: {brand} - {model} ')
obj = Car('Bugatti', 'Veyron')