sample_tuple = (1, 2, 3, 4, 5, 5)
print(sample_tuple[0])
# sample_tuple[3] = 'a'  --> Error: Tuples are immutable.
# Hence we can assign tuples as keys to dictionaries unlike lists.
# We can't sort or reverse a tuple like list, which makes them less flexible.
# But their immutability makes their execution faster than lists.
print(5 in sample_tuple)
print(len(sample_tuple))
# Tuple methods
print(sample_tuple.count(5))
print(sample_tuple.index(3))
# Tuple slicing
print(sample_tuple[1:3])
print(sample_tuple[1:2])
# A tuple with a single element has a comma too.

# Tuple unpacking
x, y, z, *other = ('a', 'b', 'c','d', 'e')
print(x)          # The 1st element is assigned to x.
print(y)          # The 2nd element is assigned to y. 
print(z)          # The 3rd element is assigned to z.
print(other)      # The remaining elements are assigned as a list to other.


