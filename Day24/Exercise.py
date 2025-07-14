# Generator for the 1st n values of Fibonacci Sequence:
def fib(n): 
    a = 0
    b = 1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b

for item in fib(6):
    print(item)

