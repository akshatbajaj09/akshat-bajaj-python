# finally keyword:
# The code in the finally block is executed EVERYTIME.
# Example:
while True:
    try:
        age = int(input('Please enter your age: '))
        print(age)
    except ValueError:
        print('Please enter a valid input.')
    else:
        print('Thank you!')
        break
    finally:
        print('Done!')
    # Now this finally block will be executed everytime we run this program.

# raise keyword:
# The raise keyword helps us to manually raise exceptions or customize 
# pre-defined errors.
# Example:
while True:
    try:
        age2 = int(input('Please enter your age for code 2: '))
        print(age2)
        raise ValueError('Stop execution')
    except ValueError as e:
        print(e)
    else:
        print('Thank you!')
        break
    finally:
        print('Done!')
# The else block will never be reached here as we are raising an error for every input.
# The as keyword here assigns the error message to the variable 'e'.

     
        