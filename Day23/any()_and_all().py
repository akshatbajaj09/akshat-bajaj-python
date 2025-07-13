# any() and all():
# any() returns True if atleast one of the inputs is True.
# all() returns True if all of the inputs are True.
# Example:
# Check if any number in the list is divisible by 3:
nums = [2, 4, 6, 8, 10]
print(any(item % 3 == 0 for item in nums))
# Or:
print(any(item for item in nums if item % 3 == 0))
# Returns True which means there is atleast one item in nums which is divisible by 3.

#  Check if all passwords are strong (length > 8):
passwords = ['helloworld', '12345678', 'secret@123']
print(all(len(p) > 8 for p in passwords)) # False (second one is only 8)

# You're managing an online store. You have a list of products,
# where each product is a dictionary with:
# "name" (string)
# "price" (int)
# "stock" (int)
# Your Task:
# Write a function that returns True only if:
# All products have stock greater than 0.
# At least one product costs more than ₹500.
products = [
    {'name': 'Pen', 'price': 10, 'stock': 2000}, 
    {'name': 'Laptop', 'price': 50000, 'stock': 100},
    {'name': 'Notebook', 'price': 50, 'stock': 1000}
]
def check():
    condition1 = all(i['stock'] > 0 for i in products)
    condition2 = any(j['price'] > 500 for j in products)
    return condition1 and condition2
print(check())