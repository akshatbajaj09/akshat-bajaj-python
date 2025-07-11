# Dictionary comprehensions offer us a simple way to generate
# dictionaries just like list and set comprehensions.
# Examples:
# A dictionary which has values as the square of 
# each value of a given sample dictionary.
sample_dict ={
    'a': 1,
    'b': 2
}
my_dict = {key: value ** 2 for key, value in sample_dict.items()}
print(my_dict)

# A dictionary where key is the string, value is its length from
# a given list of strings.
given_list = ['apple', 'banana', 'cherry']
my_dict2 = {string:len(string) for string in given_list}
print(my_dict2)

# Exercise: 
# You are given a dictionary where the keys are student names 
# and the values are their total marks (out of 100):
# Using dictionary comprehension, create a new dictionary that 
# contains only the students who scored 75 or more. But instead
# of their marks, the value should be 'Passed'.
grades = {
    'Alice': 92,
    'Bob': 67,
    'Charlie': 85,
    'David': 73,
    'Eve': 58,
    'Frank': 88
}
required_dict = {key:'Passed' for key,value in grades.items() if value >= 75}
print(required_dict)