# Context Managers:
# A Context Manager in Python is used to manage resources — like files, 
# database connections, network sockets, etc. It handles setup and teardown
# automatically.

# Built-in Context Managers:
with open('Sample.txt', 'w') as f:
    f.write('Hellooooo!')

# The above code is equivalent to:
f = open('Sample.txt', 'w')             # Calls __enter__()
try:
    f.write('Hellooooo!')             
finally:
    f.close()                           # Calls __exit__()

# Custom Context Manager using classes:
class OpenFile:
    def __init__ (self, filename, mode):
        self.filename = filename
        self.mode = mode
    def  __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with OpenFile('Example.txt', 'w') as f:
    f.write('Hi, how are you?')

print(f.closed)     # Checking if the file got closed automatically?

# Custom Context Manager using Decorators:
from contextlib import contextmanager
@contextmanager
def open_file(file_name, file_mode):
    f2 = open(file_name, file_mode)
    try:
        yield f2
# yield separates the __enter__ and __exit__ parts.
# Code before yield = setup -> __enter__()
# Code after yield = teardown -> __exit__()
    finally:
        f2.close()

with open_file('Testing.txt', 'w') as f2:
    f2.write('Testing successfull!')

print(f2.closed)
