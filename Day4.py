# Some common string methods.
sample_string1 =  'why so serious?'
print(sample_string1)                           #
print(sample_string1.capitalize())              #
print(sample_string1)                           #
print(sample_string1.upper())                   # The original string remains the same.
print(sample_string1)                           #
print(sample_string1.lower())                   #
print(sample_string1)                           #

sample_string1 = sample_string1.capitalize()    #
print(sample_string1)                           #    
sample_string1 = sample_string1.upper()         # A new string is created every time.
print(sample_string1)                           #
sample_string1 = sample_string1.lower()         #
print(sample_string1)                           #
 


# A cool thing about string slicing.
sample_string2 = 'Akshat'
                # 012345  --> Represents the indices of the strings.
print(sample_string2[::-1]) # Prints the reversed string.



# Password checker (hides password characters with asterisks).
username = input('Please enter your username: ')
password = input('Please enter your password: ')
password_length = len(password)
hidden_password = '*' * password_length
print(f'Hey {username}, your password {hidden_password} is {password_length} letters long.')


