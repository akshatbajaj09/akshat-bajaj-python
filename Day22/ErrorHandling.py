# Error Handling helps us to keep the program running even if something causes 
# it to crash.
while True:
    try:
        age = int(input('Please enter your age: '))
        print(age)
    except ValueError:
        print('Please enter a valid input.')

    else: 
        print('Thank you!')
        break
# try block: Contains code that might cause errors.
# except block: Runs when a specific error occurs.
# else block: Runs if no error occurs in try block.

# Multiple except blocks can catch different types of errors. Like:
while True:
    try:
        age2 = int(input('Please enter your age for code 2: '))
        print(10/age2)
    except ValueError:
        print('Please enter a valid input.')
    except ZeroDivisionError:
        print('Please enter age greater than zero.')
    else: 
        print('Thank you!')
        break

# Only one except block runs per error – the first one that matches.
# For example if we write 2 different codes for the same error then the 
# 1st one will be executed.
while True:
    try:
        age3 = int(input('Please enter your age for code 3: '))
        print(age3)
    except ValueError:
        print('Please enter a valid input.')
    except ValueError:
        print('The entered input is invalid.')
    else: 
        print('Thank you!')
        break