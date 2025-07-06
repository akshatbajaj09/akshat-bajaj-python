# MRO or Method Resolution Order is the order in which python looks 
# for a method or attribute in a hierarchy of classes.
# Benefits:
# It makes the code predictable and prevents ambiguity in cases involving 
# multiple inheritance.
# Example:  
#                object
#                  |
#                  A
#       ___________|_____________
#       |                       | 
#       B                       C 
#       |_______________________| 
#                  |
#                  D   
class A:
    num = 10
class B(A):
    num = 5
class C(A):
    num = 2
class D(B, C):
    num = 1
print(D.num)

# We can check this order by using the .mro() or .__mro__ method
print(D.mro())
# The order is D, B, C, A and then the base class -> object.

# Example - 2:
#                object
#       ___________|____________
#       |          |           |
#       X          Y           Z
#       \         / \        / |
#        \       /   \      /  |
#         \     /     \    /   | 
#          \   /       \  /    |
#           \ /         \/     | 
#            A           B     |
#            |___________|_____|
#                   |
#                   M
class X:
    pass
class Y:
    pass
class Z:
    pass
class A(X,Y):
    pass
class B(Y,Z):
    pass
class M(B,A,Z):
    pass
print(M.mro())
# The order is M, B, A, X, Y, Z and then the base class -> object.

# Now we don't need to understand about how this order came but generally,
# if our code looks this complex and involves so many stages of inheritance 
# and for a matter we haven't even coded anything in these classes and just passed
# them. Then there is a high chance that we need to look for a better
# way to solve the given problem.