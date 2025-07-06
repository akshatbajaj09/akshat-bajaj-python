# Exercise:
# Extend the functionality of built-in lists.
# Create a class of SuperList and make len() for any
# object in that class to return 1000.
# Also implement the built-in methods like .append() which a 
# list already has.
# Answer:
# This can be done by simply using inheritance and making our 
# custom class inherit the characteristics of the parent class -> list.
class SuperList(list):
    def __len__ (self):
        return 1000
obj = SuperList()
print(len(obj))
obj.append(4)
# We could use the built-in methods for list using inheritance
print(obj[0])
# We could also use the power of list indexing again due to inheritance.

# Just like we discussed the isinstance keyword in object introspection
# to check whether an object is an instance of a class, we also have
# an issubclass keyword to check whether a class is a subclass of some
# parent class.
print(issubclass(SuperList, list))      # True
print(issubclass(list, object))         # True
print(issubclass(SuperList, object))    # True
# Remember object being the base class for all?

# Exploring
print(issubclass(list, list))           # True
# So this means every class is a subclass of itself.
# It can be easily understood using Venn Diagrams or Set theory because it 
# is equivalent to saying A is a subset of A, which is true because every element 
# of A is present in A.
