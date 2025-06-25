# Using the knowledge of Venn-diagrams the following methods can be understood easily.
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A.difference(B)) # It is simply: A - B.
# The .difference() method creates a new set of  A - B and returns it.
print(A) # Set A remains the same.
print(A.difference_update(B))
# Returns None and changes set A in place.
print(A)
# The .difference_update() method changes the set A to A - B.
A.discard(2)
print(A)
A = {1,2,3,4,5}
print(A.intersection(B)) 
# The intersection can be done using & symbol too.
print(A & B)
print(A.union(B)) 
# The union can be done using | symbol too.
print(A | B)
print(A.isdisjoint(B))
# Returns true if A & B is a null set.
print(A.issubset(B)) 
# Returns true if every element of A is present in B.
print(B.issuperset(A))
# Returns true if B contains every element of A.