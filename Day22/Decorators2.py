# Building our own decorator to check the performance time for a given function.
from time import time
# Again something to be discussed in the Modules section.
def performance(func):
    def wrapper_func(*args, **kwargs):
        initial_time = time()
        func(*args, **kwargs)
        final_time = time()
        return f'Time taken for execution = {final_time - initial_time} s.'
    return wrapper_func

@performance    
def sample_function():
    for i in range(10000000):
        i ** 2  
        # Doing some random calculations for recording the time of execution.

print(sample_function())
