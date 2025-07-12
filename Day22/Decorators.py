# Decorators:
# Pre-requisites:
# 1. Concept of functions as first class citizens:
# A function being a first class citizen simply means that it can be passed as
# an argument, assigned to a variable, can be returned from another function.
# 2. Higher Order functions:
# The functions that take another function as an argument or returns another function
# are called Higher Order functions.
# Recall that the functions map(), filter() and reduce() are all Higher Order functions
# because they took another function as an argument but the function zip() isn't a 
# Higher Order function as it only took iterables.

# Now what are decorators:
# Decorators are Higher Order functions that take a function and enhances its 
# working without modifying the actual function.
# It is a function that simply wraps another function and enhances it.
# Examples:
# @classmethod and @staticmethod discussed in OOP.
# We could also build our own decorators.
