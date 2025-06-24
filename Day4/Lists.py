# Lists
sample_list = [1, 2.5, True, 'a']
print(sample_list)
sample_list[0] = 9
print(sample_list)             # Lists are mutable unlike strings.

# Copying a list versus modifying a list.
stationary_list = ['Notebooks', 'Pens', 'Highlighters']
new_list = stationary_list     # new_list points to the same memory location as that of stationary_list.
new_list[1] = 'Pencils'        # The modifications in new_list will be modified in stationary_list too.   
print(stationary_list)
print(new_list)

groceries_list = ['Ketchup', 'Rice', 'Salt']
new_list2 = groceries_list[:]  # This makes a copy of groceries_list
new_list2[0] = 'Mayo'          # The changes made to new_list2 does not modify groceries_list.
print(groceries_list)
print(new_list2)


