# zip() is a function that can be used to zip items from two or more iterables.
# Example:
# Imagine we have different datasets, all in the same sequential order of their 
# relatedness then we could simply zip them together.
# We can also zip different data types like lists and tuples.
# And we can pass as many iterables as we want.
data_set1 = ['Akshat', 'Ram', 'Krishna']
data_set2 = ['Akshat\'s address', 'Ram\'s address', 'Krishna\'s address']
data_set3 = ['Akshat\'s contact', 'Ram\'s contact', 'Krishna\'s contact']
print(list(zip(data_set1, data_set2, data_set3))) 
# or we could also use:
print('')
for item in (zip(data_set1, data_set2, data_set3)):
    print(item)
print('')
print(data_set1)
print(data_set2)
print(data_set3)
# The original datasets remain unchanged.
