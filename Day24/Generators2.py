# We could get generator objects using comprehensions too just like
# list comprehensions:
nums = [1, 2, 3, 4, 5]
squares_list = [i ** 2 for i in nums]
squares_generator = (j ** 2 for j in nums)
print(squares_list)
# Returns a list of the squares of all numbers in nums.
print(squares_generator)
# Returns a generator object that can yield the squares of all numbers 
# in nums.

