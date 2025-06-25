dictionary = {
    'Name': 'Akshat',
    'Age':  20,
    'Numbers': [1, 2, 3],
    'Letters': ['a', 'b','c']
}
# Dictionary is a collection of key: value pairs.
# The key must be something immutable like we can't assign a list as a key.
# The values may be mutable too.
print(dictionary)
print(dictionary['Letters'][2])                             
# Prints the element at the 2nd index of the 'Letters' key.
# If unsure whether a key exists in the dictionary, use .get() instead of [] to avoid KeyError.
print(dictionary.get('Name'))
# Prints the value corresponding to the 'Name' key.
print(dictionary.get('Position', 1))
# Prints the value corresponding to the 'Position' key but 
# since the 'Position' key is absent it assigns the default value as 1 (our input).
# However if 'Position' key had a value say 2 then it will print 2 only.
# Our input is a default value for the case when there is absence of the key. 
print(dict(user = 'Krishna', number = 1))
# Another way of printing a dictionary using dict function (less commonly used).
print('Name' in dictionary.keys())
print(20 in dictionary.values())
print(dictionary.items())

# More methods
new_dictionary = dictionary.copy()
print(dictionary.clear())
# The .clear() method does not return anything and clears the dictionary in place.
print(dictionary)
# An empty dictionary is printed.
print(new_dictionary)
# print(new_dictionary.pop())
# print(new_dictionary)                             
# Error we need to give argument in .pop() method.
print(new_dictionary.pop('Age'))
# The .pop() method returns the value corresponding to the entered key.
print(new_dictionary)
print(new_dictionary.popitem())
# The .popitem() method removes the last key value pair from the dictionary and
# returns that key value pair as a tuple.
print(new_dictionary)
# print(new_dictionary.popitem('Name'))
# print(new_dictionary)                             
# Error we can not give argument in .popitem() method.         
print(new_dictionary.update({'Greeting': 'Hello'}))
# The .update() method allows us to update a value for a key or helps to add
# new key value pair(s).
print(new_dictionary)
