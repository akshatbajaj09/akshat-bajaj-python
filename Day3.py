# Formatted strings
name = 'Akshat Bajaj'
age = str(20)
# Printing without using formatted strings (tedious).
print('Hi ' + name + '. You are ' + age + ' years old.') 
print('\n')
# Printing using formatted strings by .format() method (easier).
print('Hi {}. You are {} years old'.format(name, age))
print('\n')
# Printing using the f action (easiest).
print(f'Hi {name}. You are {age} years old.') 

