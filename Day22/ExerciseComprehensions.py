# Remember what we did on Day7:
# Exercise: Check for duplicates in a list.
sample_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []
for item in sample_list:
    if sample_list.count(item) > 1:
        if item not in duplicate:
            duplicate.append(item)
print('Duplicates are: ', duplicate)

# Now our task is to get the same result using comprehensions.
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
my_duplicates_using_lists = [item for item in my_list if my_list.count(item) > 1]
# But using a list I will get the duplicates for every occurence of a duplicate. 
print('Duplicates using list comprehension: ', my_duplicates_using_lists)
# So we should use a set, as it does not accepts same values more than once.
my_duplicates_using_sets = {item for item in my_list if my_list.count(item) > 1}
print('Duplicates using set comprehension: ', my_duplicates_using_sets)

# But if the problem specifically asks for us to give a list of duplicates?
# Well we could simply make a list of that set using list().
required_list = list(my_duplicates_using_sets) 
print('Final list of duplicates: ',required_list)