# Nested list comprehensions:
# Print the square of all even integers in the given matrix as a list.
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

required_list = [item ** 2 for row in data for item in row if item % 2 == 0]
print(required_list)

# Although the code may look concise,
# but this kind of code decreases readability so we 
# always have to think of trade-offs.

# if-else comprehensions: 
# Label numbers from 1 to 5 as even or odd
labels = ['even' if x % 2 == 0 else 'odd' for x in range(1, 6)]
print(labels)  

