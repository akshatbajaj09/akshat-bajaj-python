# The LEGB rule: Local, Enclosed, Global and Built-in.

# Whenever the interpreter is supposed to print something in a function the rule is:
# 1: It looks for a local value in the function.
# 2: If there's not any local then it looks for the parent to that local function or 
# simpy called the enclosing function.
# 3: Still no value then it looks for a global value.
# 4: And lastly if still it didn't find any value it looks for it in the Built-ins of Python.
# Therefore this makes a simple LEGB rule as stated on top.

# Now if we print something outside of a funciton then the interpreter skips checking 
# the L (local) and E (enclosing) part and directly goes to global (G) and then
# Built-ins (B).

# Example:
# Case 1: All local, enclosing and global are present.
a = 10
def enclosed():
    a = 5
    def local():
        a = 2
        print(a)
        # 'a' is defined locally so it just accepts a = 2 and doesn't move to check 'a'
        # in enclosed function or globally.
    return local()
enclosed()
print(a)    # In this statement we aren't calling any function so it skips L and E and
            # simply put the global value of the input variable in all the cases.

# Case 2: Local is absent while, enclosing and global are present.
b = 10
def enclosed():
    b = 5
    def local():
        print(b)
        # 'b' isn't defined locally so it moves to enclosed function, finds 'b'
        # and puts b = 5 and then doesn't move further to find 'b' globally.
    return local()
enclosed()
print(b)

# Case 3: Local and enclosing are absent and only global is present.
c = 10
def enclosed():
    def local():
        print(c)
        # 'c' isn't defined in local or enclosing so it finds global 'c' and puts c = 10.
    return local()
enclosed()
print(c) 

# Case 4: Built-ins
def enclosed():
    def local():
        print(sum([1, 2, 3])) 
        # sum isn't defined in local, enclosed or global scope so the interpreter
        # checks for Built-ins.
    return local()
enclosed()

