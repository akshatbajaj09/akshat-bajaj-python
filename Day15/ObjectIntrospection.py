# Object Introspection is the ability to examine an object at runtime.
# Example:
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author =  author
obj = Book('White Nights', 'Fyodor Dostoevsky')
print(type(obj))
# type() prints the type of the object.
print(dir(obj))
# dir() prints its attributes. 
print(hasattr(obj, 'title'))
# hasattr() checks if it has the mentioned attribute. 
print(getattr(obj, 'title'))
# getattr() gets the value of the mentioned attribute.
print(setattr(obj, 'title', 'Crime and Punishment'))    
# setattr() sets the value of the mentioned attribute in place and returns None.
print(getattr(obj, 'title'))
print(isinstance(obj, Book))       
# True
print(issubclass(Book, object))    
# True, since everything inherits from object in Python.
print(id(obj))                     
# id() gives the memory location of the mentioned object.
