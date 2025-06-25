sample_set = {1, 2, 3, 4, 5, 5}
print(sample_set) # Sets contain unique values only.
# So 5 is printed only once.
print(sample_set.add(100))
# The .add() method does not return a value and adds the input to the set in place.
sample_set.add(2)
print(sample_set) # Again sets contain unique values only.
# Hence, 100 was added but 2 being already present doesn't appear twice.

# We can also make a list from a set or vice-versa.
print(list(sample_set))
sample_list = ['a', 'b', 'b', 'c']
print(set(sample_list))

# Copying and clearing a set.
new_set = sample_set.copy()
print(sample_set.clear()) # The .clear() method clears the set in place and 
# doesn't return a value.
print(sample_set)         # The set was cleared.  
print(new_set)
