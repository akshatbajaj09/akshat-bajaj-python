sample_list1 = [1, 2, 3, 4]
print(sample_list1)
# Adding methods
sample_list1.append(100)                # Appends an element to the end of the list.
print(sample_list1)
sample_list1.insert(2, 9)               # Inserts 9 at the 2nd index.
print(sample_list1)
sample_list1.extend(['a', 'b', 'c'])    # Extends the list and adds ['a', 'b', 'c'] to it.
print(sample_list1)

#Removing methods
sample_list1.pop(2)                     # Pops the item from the index we input.
print(sample_list1)
sample_list1.remove(4)                  # Removes the item we input to it.
print(sample_list1)
sample_list1.clear()                    # Clears the list (self-explanatory).
print(sample_list1)

# Which method returns a value?
sample_list2 = ['x', 'y', 'z']
print(sample_list2)
new_list1 =  sample_list2.append(99)    # Does not return a value and changes the list in place so new_list1 contains nothing.
print(new_list1)                        # None    
print(sample_list2)                     # The appended list is printed.
new_list2 = sample_list2.pop(1)         # Returns the value of the index we gave as an input and changes the list too.
print(new_list2)                        # Contains the element at the 1st index of sample_list2.
print(sample_list2)                     # ['x', 'z', 99].