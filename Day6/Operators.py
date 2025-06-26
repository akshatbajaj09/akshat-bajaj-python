# is vs ==
# == can work for different types as well.
print(True == 1)        # True - bool True and int 1 both have same value.
print('' == 1)          # False - '' is an empty string and 1 is an int (different types and values).
print('1' == 1)         # False - '1' is a string and 1 is an int (different types). 
print([] == 1)          # False - [] is a list and 1 is an int (different types and values). 
print(10 == 10.0)       # True - 10 and 10.0 both have same value.
print([] == [])         # True - they both represent an empty list.

# In case of is, the two items must be exactly same (same type, same object and same memory location).
# We can ignore the syntax warnings like:
# SyntaxWarning: "is" with 'str' literal. Did you mean "=="?  
# We are using 'is' intentionally. 
print(True is 1)        # False - True is bool and 1 is an int (different types).
print('' is 1)          # False - '' is an empty string and 1 is an int (different types and values).
print('1' is 1)         # False - again as '1' is string and 1 is an int (different types).
print([] is 1)          # False - [] is a list and 1 is an int (different types and values).
print(10 is 10.0)       # False - 10 is an int and 10.0 is a float (different types).
print([] is [])         # False - everytime you create a list,
                        # it is created in a new memory location. Hence, both lists are different.
