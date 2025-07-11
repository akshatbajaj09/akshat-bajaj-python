# reduce():
from functools import reduce
# The above line will be understood when we study about modules, for now 
# just think that we can't directly use reduce() in a program and we need to 
# import it first.
# The reduce() function takes:
# 1st: A function that takes 2 arguments.
# 2nd: An iterable.
# Optional 3rd: An initial value.
given_list = [1, 2, 3]
def accumulator(acc, item):
    return acc + item
print(reduce(accumulator, given_list, 0))

# To see what is happening behind the scenes we could add a print() statement like:
def accumulator(acc, item):
    print(acc, item)
    return acc + item
print(reduce(accumulator, given_list, 0))

# The '0' here is the optional initial value.
# If not provided, reduce() uses the first element of the list as the initial value.
# Example: reduce(accumulator, [1, 2, 3]) → starts with acc=1, item=2.