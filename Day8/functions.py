def say_hello_to(name):
    print(f'Hello {name}')
say_hello_to('Akshat')

# *args -> Used to pass multiple arguments to the function simultaneously. 
# Even if the function is defined with 1 parameter only.
# Notice parameters are when we define a function and arguments are when we call it.

def greet(*args):
    for i in args:
        print (f'Greetings Mr./Ms. {i}')
greet('Akshat', 'John', 'Dan')

# Using **kwargs -> The args often used are positional args and when we don't know 
# the position of a parameter to pass an arg, we can use keyword args.

def sample_function(name, age):
    print(dict(Name = name, Age = age))
sample_function('Akshat', 20) # Positional args.
sample_function(age = 20, name = 'Akshat') # In case we don't know the position of 
# parameters then **kvargs can be used.

# Now we also have a concept of default parameters.     
# Like b = 1 is a default parameter and if we just pass a single arg then it will return 
# 0 as anything divided by 1 has remainder of 0.
# So, we avoid an error even by passing a single arg.
def remainder(a, b = 1):
    '''
    Info: Returns the remainder of a / b.       
    '''
    print('Remainder: ', a % b)
remainder(10, 4)
remainder(10)
# The triple quote thing in the above function is known as a Docstring.
# Docstrings can tell us whatever we want to tell
# about a function by just hovering over the function when you call it.