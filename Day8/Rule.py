# There's a general rule to define a function.
# Rule: parameters, *args, default parameters, **kwargs.

def function(name, *args, age = 20, **kwargs):
    message1 = f'Hi {name}, you are {age} years old.'
    message2 = f'Your chosen numbers are {args}.'
    message3 = f'Your dictionary is {kwargs}.'
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.items())
    return(f'{message1}\n{message2}\n{message3}')
print(function('Akshat', 1, 2, 3, Country = 'India', College = 'NITJ' ))


# Note that *args gives a tuple of the input and **kwargs generates a dictionary.