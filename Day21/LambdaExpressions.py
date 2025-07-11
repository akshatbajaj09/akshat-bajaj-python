# Lambda expression:
# These are useful when we need to define a function that is only used once.
# So we don't need to store that function and we don't need to name it too.
# Example:

# Basic lambda:
# Squaring:
num = int(input('Enter your number: '))
print(f'The square of {num} is: ', (lambda item: item ** 2)(num))

# lambda with map():
# Multiply each number in the list [1, 2, 3, 4] by 10.
given_list = [1, 2, 3, 4]
print('Your desired list is: ', list(map(lambda item: item * 10, given_list)))

# lambda with filter():
# Keep only even numbers from [1, 2, 3, 4, 5, 6].
given_list2 = [1, 2, 3, 4, 5, 6]
print('The list with only evens is: ', list(filter(lambda item: item % 2 == 0, given_list2)))

# lambda with reduce():
# Compute the product of all elements in [1, 2, 3, 4].
given_list3 = [1, 2, 3, 4]
from functools import reduce
print('The product of all the elements of the list is: ', reduce(lambda acc, item: acc * item, given_list3))

