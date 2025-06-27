# Sum of elements in a list.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in my_list:
    sum = sum + i
print('The sum of elements of the given list is: ', sum, '\n')

# Exercise: Print a * for 1 and a space for 0 in the given picture.
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],    
]

# Solution:
for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
print('')
# Exercise: Check for duplicates in a list.
sample_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate= []
for item in sample_list:
    if sample_list.count(item) > 1:
        if item not in duplicate:
            duplicate.append(item)
print('Duplicates are: ', duplicate)

