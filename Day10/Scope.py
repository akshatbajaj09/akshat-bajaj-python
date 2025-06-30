a = 10
def enclosed():
    a = 5
    def local():
        a = 2
        print(a)
    return local()
print(enclosed())

# A global a = 10 is assigned.
# A function enclosed is defined.
# The interpreter goes directly from line 3 to line 9.
# It sees the print function and says ok i am supposed to print whatever is the output of 
# the thing inside the paranthesis.
# It sees enclosed() and calls it.
# The enclosed function is executed and puts a = 5. This a has nothing to do with the global a.
# Inside enclosed() a local function is defined.
# The interpreter skips from line 5 to 8 and sees that enclosed is suppossed to return something.
# Now it evaluates this something to return it and sees that local() is called in this something.
# It then executes local and sets a = 2 which is different from both the previous 'a's. 
# Now it prints this a = 2. 
# Local has been executed but it didn't return anything so in the return statement of line 8
# The something we were talking about returns nothing or None.
# Hence the enclosed function returns None and this is now printed 
# while the interpreter moves back to line 9.
# Output:
# 2
# None