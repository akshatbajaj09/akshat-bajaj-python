# Dunder or Double underscore methods also known as Magic methods are 
# special methods that Python automatically calls in.
# Example: __init__ method is automatically called while instantiating an object.
# Benefits:
# They give us the ability to customize our classes and make our objects 
# behave like built-in types.

# Implementation:
class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author
obj = Book('Sapiens', 'Yuval Noah Harari')
print(obj)
# Sample output: <__main__.Book object at 0x0000014970625D60>
# This above output is useless to us so we will customize these classes by using 
# Dunder methods to get meaningful output like: 'Sapiens'
# Also methods like len() can't be implemented on obj but we can customize it too.
# print(len(obj)) -> Error.

# Customizing
class CustomizedBook:
    def __init__ (self, title, author): 
        self.title = title
        self.author = author
    def __str__(self):
        return self.title
    def __len__ (self):
        return len(self.title)
new_obj = CustomizedBook('White Nights', 'Fyodor Dostoevsky')
print(new_obj)
print(len(new_obj))

