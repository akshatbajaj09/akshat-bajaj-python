sample_list = [1, 71, 4, 9, 2]
sample_list.sort()              # Sorts the list. [1, 2, 4, 9, 71].
print(sample_list)
sample_list.reverse()           # Reverses the list. [71, 9, 4, 2, 1]
new_list = sample_list[::-1]    # Creates a reversed COPY of the list [71, 9, 4, 2, 1] as [1, 2, 4, 9, 71].
                                # and the original list [71, 9, 4, 2, 1] stays same.
print(sample_list)              # This remains as [71, 9, 4, 2, 1].
print(new_list)                 # This changes to [1, 2, 4, 9, 71].
print('\n')

# Range 
print(list(range(1,101)))       # Prints a list from 1 to 100.
print('\n')

# The .join() method.
space = ' '                  
introduction = space.join(['Hi', 'my', 'name', 'is', 'Akshat', 'Bajaj.'])
print(introduction)
print('\n')
# Joins each item of the list with a space to form a string.

# List unpacking
a, b, *other, c = [1, 2, 3, 4, 5, 6, 7]
print(a)                       # The 1st element gets assigned to a.
print(b)                       # The 2nd element gets assigned to b.
print(other)                   # All the middle elements remain as a list and are stored in other.
print(c)                       # The last element gets assigned to c.
