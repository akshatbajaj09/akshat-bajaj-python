# filter():
# As the name suggests, this function helps us filter elements from
# an iterable, unlike map() which returns the same number of elements.
# Example:
def only_even(item):
    return item % 2 == 0
print(list(filter(only_even, [1, 42, 97, 102, -99, 0 ,-4])))

# The original list stays the same while using filter() too, just like map().