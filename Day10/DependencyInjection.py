# The concept of global and nonlocal isn't the best practice because the scope of one is 
# accessing or modifying the other scopes which makes things confusing and hence 
# a better way of doing things is the idea of Dependency Injection (DI).
# In DI we just pass on the required values to the function on which the function is 
# dependent so in a way we are injecting the dependency and hence the name.
# Example:

total = 0
def count(total):
    total += 1
    return total
print(count(count(count(total))))

# Here we are passing the value of total so the innermost count takes on the total 
# from the global total and runs count(0) this after execution increments the total and
# returns total = 1 which is passed on to the next count() that runs count(1) and again
# total gets incremented to 2 and is returned. Now the final count() evaluates count(2),
# increments total to 3 and returns it. This 3 is then printed and displayed in the output.