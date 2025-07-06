# Create a class SmartList that mimics some behaviors of a Python list using dunder methods.
class SmartList:
# __init__ – to initialize with a list
    def __init__ (self, sample_list):
        self.sample_list = sample_list
# __str__ – user-friendly print
    def __str__ (self):
        return f'SmartList: {self.sample_list}'
# __repr__ – developer-friendly
    def __repr__ (self):
        return f'SmartList({self.sample_list})'
# __len__ – make len(obj) work
    def __len__ (self):
        return len(self.sample_list)
# __getitem__ – make obj[index] work
    def __getitem__ (self, index):
        return self.sample_list[index]
# __setitem__ – make obj[index] = value work
    def __setitem__ (self, index, value):
        self.sample_list[index] = value
# __contains__ – make value in obj work
    def __contains__ (self, item):
        return item in self.sample_list
# __add__ – make obj1 + obj2 combine lists
    def __add__ (self, other):
        return SmartList(self.sample_list + other.sample_list)
# __eq__ – compare SmartList objects based on data
    def __eq__ (self, other):
        return self.sample_list == other.sample_list
# Defining a .sum() method that returns the sum of the elements.
    def sum(self):
        return sum(self.sample_list)
    
a = SmartList([1, 2, 3])
b = SmartList([4, 5])

print(a)                                # SmartList: [1, 2, 3]
print(repr(a))                          # SmartList([1, 2, 3])
print(len(a))                           # 3
print(a[1])                             # 2
a[1] = 20
print(a)                                # SmartList: [1, 20, 3]
print(20 in a)                          # True
print(a + b)                            # SmartList: [1, 20, 3, 4, 5]
print(a == SmartList([1, 20, 3]))       # True
print(a.sum())
print(b.sum())
# __iter__ vs __getitem__
print(sum(a))                           
# Works although 'a' being a class object is not iterable but as we defined the
# __getitem__ method, this acts as a fallback for the __iter__ method. But this 
# isn't recommended. Why?
# Because the __getitem__ fallback of the interpreter stops when an IndexError is raised
# but what if there isn't any IndexError, then the program may run infinitely and crash.
# Also by using __iter__ the execution is faster and it improves readability too.
# We can define __iter__ like this:
    # def __iter__ (self):
    #     return iter(self.sample_list)
# More on this iter() function in the __iter__.py file.