# Practice:
# Generator to yield all even numbers from 0 to n (inclusive):
def even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

print(even(10))
g = even(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) -> Raises StopIteration.

# Generator that yields the first n multiples of a given number x:
def multiples(n, x):
    for i in range(1, n+1):
        yield i * x

n = int(input('Enter the value of n: '))
x = int(input('Enter the value of x: '))

print(f'The first {n} multiples of {x} are: ')
g2 = multiples(n, x)
for item in g2:
    print(item)