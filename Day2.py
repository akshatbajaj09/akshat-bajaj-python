# Operators 
print('Operators')
print(2 ** 4)   # Gives 2 raised to the power of 4.
print(29 // 10) # Gives [29 / 10], where [.] represents the greatest integer function (maths hehe).
print(5 % 2)    # Gives the remainder of 5 / 2.
print('\n')

# Math functions
print('Math functions')
print(round(2.5142379))    # Rounds off the input to an integer.
print(round(2.5142379, 6)) # Rounds off the input upto 6 decimal places.
print('\n')

# Binary representation
print('Binary stuff')
print(bin(5)) #0b101
print(int('0b101', 2)) 
print(int('1001', 2))
print('\n')

# Strings and string concatenation
print('Strings')
first_name = 'Akshat'
last_name = 'Bajaj'
full_name = first_name + ' ' + last_name
print(full_name)
print ('Akshat' + ' Bajaj')
print('\n')

#Type conversion
print('Type conversion')
a = input('Enter your age: ')
print(type(a))
a = int(a)
print(type(a))
print(a + 5)
print(int(input('Enter your age: ')) + 5)