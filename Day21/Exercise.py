# List sorting:
# Sort the given sample list in ascending order of the 2nd element of 
# each tuple item using lambda expressions.
sample_list = [(0, 2), (10, -1), (4, 3), (9, 9)]
sample_list.sort(key=lambda x: x[1])
print(sample_list)
# Without key= the list will be sorted based on the first tuple item.

# Sort by string length:
words = ['apple', 'fig', 'banana', 'kiwi']
# Expected Output: ['fig', 'kiwi', 'apple', 'banana']
words.sort(key=lambda item: len(item))
print(words)

# Sort by last character:
names = ['Sam', 'John', 'Alex', 'Zoe']
names.sort(key=lambda item: item[-1])
print(names)

# Sort this list of tuples based on the product of the two numbers in each tuple.
sample = [(2, 3), (1, 9), (5, 2), (3, 4)]
sample.sort(key=lambda item: item[0] * item[1])
print(sample)

# Sort the students in descending order based on their average marks
# across math and science, using a lambda function.

students = [
    ('Alice', {'math': 85, 'science': 90}),
    ('Bob', {'math': 78, 'science': 83}),
    ('Charlie', {'math': 95, 'science': 87}),
    ('David', {'math': 88, 'science': 93})
]

students.sort(key=lambda item: (item[1]['math'] + item[1]['science']) / 2)
print(students)
# But this just sorted it in ascending order, so for descending order we can 
# use reverse = True, which by default is set to False and hence, sort()
# sorts the items in ascending order.

students.sort(key=lambda item: (item[1]['math'] + item[1]['science']) / 2, reverse = True)
print(students)

# A simple example for understanding reverse=True:
a = [1, 47, 9, 15]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)