# Exercise: Create a function that returns the highest even number of the list from 
# the given list.
def highest_even(given_list):
    highest_even = 0
    for i in given_list:
        if i % 2 == 0:
            if i > highest_even:
                highest_even = i
    return highest_even
print(highest_even([10, 2, 3, 4, 8, 11]))

# There's an error in the above code.
# What if we get a list where there isn't any even number, 
# it will output 0 which is wrong.
# Corrected code: Initialize highest_even as None.

def highest_even(given_list):
    highest_even = None
    for i in given_list:
        if i % 2 == 0:
            # Short circuiting:
            # If highest_even is None, Python won't evaluate i > highest_even.
            # This avoids a TypeError for comparing int and None
            # and safely sets the first even number.
            if highest_even is None or i > highest_even:  
                highest_even = i                                    
    return highest_even
print(highest_even([10, 2, 3, 4, 8, 11]))

# More examples:
print(highest_even([1, 3, 5, 7, 9]))       # All odds.
print(highest_even([-1, -3, -57, 3, -4]))  # Odds and negatives.
print(highest_even([-4, -2, 1, 13, 14.0])) # 14.0 % 2 == 0.0 and 0.0 == 0 evaluates to True.
print(highest_even([-4, -2, 1, 0, 13]))    # Negatives, odds and zero.