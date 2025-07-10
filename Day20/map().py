# map() is a simple function which is widely used in FP.
# It takes two arguments: 
# 1st: A function (it will be better if the function is pure).
# 2nd: An iterable
# So the function is the action we need to perform and the iterable our dataset.
# In this way we maintain the principle of FP of keeping action and data separate.
# Example:
# Without map():
given_list = [1, 2, 3]
def multiply_by_2(sample_list):
    new_list = []
    for item in sample_list:
        new_list.append(item * 2)
    return new_list
print(multiply_by_2(given_list))
print(given_list)
# The given_list stays same, this means we are creating a new list (obviously we have 
# that declared in our function) and not modifying the outside world.
# And we are also getting the same output for same input, which means we are 
# satisfying both the criteria of a pure function.

# With map():
# Find cubes of given numbers:
given_list2 = [1,2,3]
def cube(num):
    return (num ** 3)
print(list(map(cube, given_list2)))
print(given_list2)
# Notice how the given_list2 also remains the same.

# Find the length of the input strings:
given_list3 = ['Apple', 'Banana', 'Mango']
def len_of_string(given_string):
    return len(given_string)
print(list(map(len_of_string, given_list3)))
print(given_list3)
# The given_list3 also remains the same.

# So it means that both the functions we made while using map() are pure (same
# output for same input and no side effects).

# Note: While passing the function as an argument we don't need to call it as it 
# is automatically called and evaluated for each item one by one.