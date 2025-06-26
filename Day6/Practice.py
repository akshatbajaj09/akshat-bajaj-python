# Make a program to check if a number is even or odd and also
# check its divisibility by 5 at the same time.
number = int(input("Enter your number: "))
if number % 2 == 0:
    if number % 5 == 0:
        print("The number is even and divisible by 5.")
    else:
        print("The number is even but not divisible by 5.") 
else:
    if number % 5 == 0:
        print("The number is odd and divisible by 5.")
    else:
        print("The number is odd but not divisible by 5.") 

# For doing this again to check divisibility with 3 (let's say),
# we can just replace number % 5 with number % 3.
# Make sure to change the print statements too, lol.   