# The iter() function and __iter__ method:
# The iter() function calls the .__iter__ method behind the scenes.
# It takes an iterable as an input and returns an iterator.
# Now what are iterators and iterables?
# Iterables in a lay man language are anything that can be looped over.
# Like lists, tuples, sets, dictionaries, etc.
nums = [1, 2, 3]
for num in nums:
    print(num)
# Since we can loop over the list it is an iterable. But a technical
# define of iterable is anything which has .__iter__ method.
# Now we can check this by using Object Introspection.
# Remember the dir() function which tells us about all the associated 
# methods and attributes for an item? 
print(dir(nums))
# We can see the __iter__ method in the ouptput which means and we knew it too
# that nums is an iterable.
# Now what is an iterator?
# Anything which has a state so that it remembers where it was while execution.
# Technically, it is something which has a .__next__ method.
# And running this iter() function returns an iterator. 
# So,
an_iterator = iter(nums)    
# returns us an iterator and now if we check for
print('\n')
print(dir(an_iterator))     
# has a __next__ method too.
# The next() function is used to call .__next method behind the scenes.
print(next(an_iterator))    
# Returns the 1st item of the list nums.
print(next(an_iterator))            
# As iterators remember their state so now it
# returns the 2nd item of the list nums.
print(next(an_iterator))
# Returns the 3rd item of the list nums.
# print(next(an_iterator))    
# Raises a StopIteration exception.

# And this exactly what happens in behind the scenes of a for loop.
# The next() function runs on the iterator and the StopIteration 
# exception is handled internally.
# So this:
nums = [1, 2, 3]
for num in nums:
    print(num)
# is similar to this:
while True:
    try:
        item = next(an_iterator)
        print(item)
    except StopIteration:
        break

# Another characteristic of an iterator is it can only go forward using next()
# if you want to go back then you have to start from scratch.