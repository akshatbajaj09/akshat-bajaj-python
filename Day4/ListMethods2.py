sample_list = ['a', 'b', 'c ', 'x', 'd', 'x']
print(sample_list.index('x'))       # Prints the index of 'x' for its 1st occurence.
print(sample_list.index('x', 0, 4)) # Prints the index of 'x' for the range [0:4].
# But what if we don't know if 'x' is there in the sample_list?
print('x' in sample_list)           # Tells us if 'x' is in sample_list or not.  
print(sample_list.count('x'))       # Prints the number of times 'x' appears in the sample_list.
 
# Sorting a list.
sample_list = ['a', 'b', 'c ', 'x', 'd', 'x']
print(sample_list) 
print(sample_list.sort())                       # Sorts the list in place and does not return a value. The output is None.
print(sample_list)                              # The list was sorted in place and hence the output is sorted list.
sample_list = ['a', 'b', 'c ', 'x', 'd', 'x']   # Restoring the unsorted form.
print(sample_list)          
sample_list.sort()                              # Since .sort() does not return a value so we must print the list separately.
print(sample_list)                              # The sorted list is printed.
sample_list = ['a', 'b', 'c ', 'x', 'd', 'x']   # Restoring the unsorted form again.
print(sample_list) 
print(sorted(sample_list))                      # Using the sorted function. 
                                                # This function returns a value and hence we can print directly.

# Reversing a list
sample_list = ['a', 'b', 'c ', 'x', 'd', 'x']
print(sample_list) 
sample_list.reverse()                           # This just reverse the list index wise.
print(sample_list)
# So what if we need a reversed list which is sorted too?
sample_list = ['a', 'b', 'c ', 'x', 'd', 'x']
print(sample_list) 
sample_list.sort()
sample_list.reverse()
print(sample_list)