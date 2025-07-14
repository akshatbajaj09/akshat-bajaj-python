# Generators return an iterator which doesn't have all the values stored in 
# memory and waits for us to call them one by one using the next() function or
# via loops.
# Benefits:
# Since they don't store all the values, the memory usage is lesser.
# They are faster in execution too.
# Example:
my_list = [1, 2, 3, 4, 5]
def square_nums(given_list):
    result = []
    for i in given_list:
        result.append(i ** 2)
    return result
def my_generator(given_list):
    for item in given_list:
        yield item ** 2     
        # The yield keyword turns a function into a generator.
        # It pauses the execution while remembering the state just like an 
        # iterator object. 
print(square_nums(my_list))
# This returns a list of squares for the input list.
print(my_generator(my_list))
# This returns a generator object ready to return values using next() or loops.
# So all the values aren't stored in memory simultaneously in this case and
# hence we get lesser memory usage and faster execution too.

# To return the values from this generator object we could simply use the
# next() function or loops, like:
g = my_generator(my_list)
# Using next():
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) -> raises StopIteration exception.

# Using loops:
x = my_generator(my_list)
for num in x:
    print(num)

# We could also get a list from this generator object using list(), like:
print(list(my_generator(my_list)))
# But this reduces the performance and memory efficiency again as lists stores 
# all the values simultaneously unlike generators.