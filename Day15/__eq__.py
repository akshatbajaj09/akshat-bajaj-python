# The __eq__ dunder method:
# Now this falls back to the basics of == vs is, discussed in Day 6.
# == checks for the value and is checks for both value and memory location.

a = 4
b = 4
print(a == b)   
# True (they are equal in value).
print(a is b)   
# True (they are equal in value and share the same memory for
# memory optimization as they are small integers).


# Now what does this have to do with __eq__ method?
# The == operator whenever called internally runs the __eq__ method and this 
# __eq__ method checks identity for custom objects but only value for anything 
# except custom objects (like integers, strings, etc.).
# Case 1: When the operands are two class objects then this __eq__ method checks for
# the memory locations too and since two different objects share different 
# memory locations it always returns False, unless we customize it.
# Case 2: When the operands are not class objects, they can be integers or strings or
# anything else too as long as they have same value, even if they share different
# memory locations the __eq__ returns true.
# So in a way we could summarize by saying:
# Case 1: a == b when a and b are class objects is equivalent to a is b and returns
# False unless customized.
# Case 2: a == b for a and b being anything except class objects, simply compares
# the values of a and b.

# Implementation:

# Case 1: a == b when a and b are class objects.
class Book:
    def __init__(self, name):
        self.name = name
Book1 = Book('Sapiens')
Book2 = Book('Sapiens')
print(Book1 == Book2)               
# False as for class objects Book1 == Book2 calls __eq__ which in this case
# is equivalent to Book1 is Book2 and since Book1 and Book2 are at different
# memory locations, it returns False.

# Customizing:
class CustomizedBook:
    def __init__(self, name):
        self.name = name
    def __eq__(self, another):
        return self.name == another.name
Book1 = CustomizedBook('Sapiens')
Book2 = CustomizedBook('Sapiens')
print(Book1 == Book2)  
# Book1 == Book2 again calls __eq__ internally but this time we customized
# the __eq__ method to compare the values and not the memory locations 
# which it did by default. So now only the values gets compared and since they
# both have the same value of 'Sapiens' it returns True.

# Case 2:
c = 9
d = 9
print(c == d)
# In this case c == d again calls __eq__ which in this case as c and d are 
# not any class objects, it simply checks for their value equality
# and since they are equal in value it returns True.