# Set Comprehensions are similar to list comprehensions and offer
# a simple way to make sets.
# Just like we did in list comprehensions we can simply change
# the notation from [] to {} to get a set.
# Examples:
my_set = {char for char in 'Hello'}
print(my_set)
my_set2 = {item ** 2 for item in range(1, 11)}
print(my_set2)
my_set3 = {item ** 2 for item in range(1, 11) if item % 2 == 0}
print(my_set3)
