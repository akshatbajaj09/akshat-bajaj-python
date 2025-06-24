# Password checker (hides password characters with asterisks).
username = input('Please enter your username: ')
password = input('Please enter your password: ')
password_length = len(password)
hidden_password = '*' * password_length
print(f'Hey {username}, your password {hidden_password} is {password_length} letters long.')
