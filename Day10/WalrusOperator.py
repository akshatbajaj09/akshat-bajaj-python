a = 'Akshat Bajaj'
if len(a) > 10 :
    print(f'The string is too long and has {len(a)} elements.')
# But the above method calculates len(a) twice. 
# So we can use a walrus operator which can help us assign values to a variable within 
# an expression.
if (n := len(a)) > 10:
    print(f'The string is too long and has {n} elements.')
# Now we just need to calculate len(a) once and we can assign it to a variable, all within
# an expression.
# We can't simply use the assignment operator and do if (n = len(a)) because assignment
# operator doesn't work in an expression like if condition and will raise a 
# SyntaxError like: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# The walrus operator was designed to do so without any errors.

# We can also use this in various other places like in control flow statements:

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]      # Removing the last element of string each time.
print(a) 