# List comprehension is a simple way to create a list from an iterable
# using an expression or condition or both.
# Traditional way:
a = 'Hello'
my_list = []
for item in a:
    my_list.append(item)
print(my_list)

# Using List Comprehension:
my_list2 = [char for char in 'Hello']
print(my_list2)

# We could also use an expression instead of just a variable.
# For example:
# List of squares of numbers from 1 to 10.
my_list3 = [item ** 2 for item in range(1, 11)]
print(my_list3)

# We could also add conditions like:
# Squares of 1 to 10 that are even:
my_list4 = [item ** 2 for item in range(1, 11) if item % 2 == 0]
print(my_list4)

