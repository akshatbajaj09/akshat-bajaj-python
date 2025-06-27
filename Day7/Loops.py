# Looping on a string.
for i in 'Akshat Bajaj':
    print(i)                # After printing by default we go to a new line.
print('')
for i in 'Akshat Bajaj':
    print(i, end = '')      # Telling the interpreter to stick to the same line.
print('\n')                   
# Looping on lists, tuples and sets.
sample_list = [1, 2, 3, 4, 5]
sample_tuple = (1, 2, 3, 4, 5)
sample_set = {1, 2, 3, 4, 5}
for j in sample_list:
    print(j)
print('')
for k in sample_tuple:
    print(k)
print('')
for l in sample_set:
    print(l)
print('')

# Looping on dictionaries.
dictionary = {
    'Name': 'Akshat',
    'Age': 20
}
for a, b in dictionary.items():
    print(a, b)
print('')
for m in dictionary.items():
    print(m)
print('')
for n in dictionary.keys():
    print(n)
print('')
for o in dictionary.values():
    print(o)
