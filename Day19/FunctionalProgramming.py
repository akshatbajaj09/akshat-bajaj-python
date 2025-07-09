# Functional Programming(FP) is a style which supports the idea of seperating the data
# and the created functions. It recommends making pure functions that are seperate
# from the data.
# Pure functions - Are the functions which:
# 1. Give the same output for the same input irrespective of how many times
# we execute our program.
# 2. Don't have any side effects, meaning they should not affect the outside world.
# Benefits of FP:
# Code is more reusable (DRY) as the data being seperate can be changed easily. 
# Less bugs and cleaner code.
# Example:
def multiply_by_2(sample_list):
    new_list = []
    for item in sample_list:
        new_list.append(item * 2)
    return new_list
print(multiply_by_2([1, 2, 3]))

# Is the above function pure?
# To tell this we will verify the two criterias:
# 1. Same output for same input: Satisfied, as no matter how may times we 
# run this function on [1, 2, 3] we will always get [2, 4, 6].
# 2. No side effects: Satisfied as this function doesn't affects the outside
# world. However functions like:

def multiply_by_3(sample_list):
    new_list2 = []
    for item in sample_list:
        new_list2.append(item * 3)
    print(new_list2)
multiply_by_3([1, 2, 3])

# are not pure as this is printing new_list2 which means it is interacting with the 
# outside world.

# Another example of a function which is not pure can be:
new_list3 = []
def multiply_by_4(sample_list):
    for item in sample_list:
        new_list3.append(item * 4)
    return new_list3
print(multiply_by_4([1, 2, 3]))

# Here even if it is not printing anything but it is interacting with 
# new_list3 which is declared outside of its scope. Hence, it is interacting
# with the outside world which means this is not a pure function.