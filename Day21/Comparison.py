# Why do we need to use list() function or for loop to see the outputs 
# of map(), filter() and zip() functions but not in reduce()?
# Because:
# The outputs in case of map(), filter() and zip() are iterators whereas
# in case of reduce() the actual value is returned.
# So in order to get the values from the iterator returned by map(), 
# filter() and zip() we need to run the next() function or use the 
# __next__ method and since we know that list and for loops handle all 
# these things internally, hence we need to use the list() function or for loop
# to view the output values obtained via the map(), filter() and zip() functions.