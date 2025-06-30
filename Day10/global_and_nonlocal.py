# total = 0
# def count():
#     total += 1
#     return total
# print(count())

# The above code throws an error because in count function the total is an unknown.
# And now we don't want to create a new total and assign it to 0 becuase 
# that just consumes more memory instead we wish to use the globally created total.
# So here comes the global keyword in the picture.

total = 0
def count():
    global total        
    # This tells the interpreter that whenever we say total inside this function
    # we are referring to the global total we created.
    total += 1
    return total
count()             # total becomes 1.
count()             # total becomes 2.
print(count())      # total becomes 3.

# The nonlocal keyword.

x = 'global'
def outer():
    x = 'nonlocal'
    def inner():
        x = 'local'
        print('Inner: ', x)
    inner()
    print('Outer: ', x)
outer()
print(x)
# The above code works as expected:
# An x is assigned globally: x = 'global'.
# An outer function is defined which assigns another x as: x = 'nonlocal' and
# defines an inner function, which is then called by outer function so while the
# execution of inner a new x as: x = 'local'.
# Now the print('Inner: ', x) statement looks for x locally and prints x as local.
# Then the print('Outer: ', x) statement is executed and since the scope of x as 
# x = 'local' is restricted to inner function this print considers outer as its 
# local function and finds and prints x as nonlocal.
# The print(x) statement is independent of the functions so it simply outputs  x = global.

# Now if we use the nonlocal keyword.
x = 'global'
def outer():
    x = 'nonlocal'
    def inner():
        nonlocal x
        x = 'local'
        print('Inner: ', x)
    inner()
    print('Outer: ', x)
outer()
print(x) 

# Here using the nonlocal keyword makes the x of x = 'local' and x = 'nonlocal' the same
# and pointing to the same memory location so when after using this keyword we assign
# x = 'local' then it changes the x in outer() function too.
# The print(x) again returns x = global.

# Playing around:
x = 'global'
def outer():
    x = 'nonlocal'
    def inner():
        global x
        x = 'local'
        print('Inner: ', x)
    inner()
    print('Outer: ', x)
outer()
print(x)

# This will make the global x and x in the inner() function point to same 
# memory location so changes in one will be visible in other too.
# This time the x in outer() remains unaffected.