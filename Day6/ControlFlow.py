# Problem: if magician and expert: "You are a master magician."
# if magician but not expert: "At least you're getting there."
# if not a magician: "You need magic powers."
# Given: 
is_magician = False
is_expert = False
# We can vary the inputs to True or False to check different conditions.
if is_magician and is_expert:
    print("You are a master magician.") 
elif is_magician and not(is_expert):
    print("At least you're getting there.")
elif not(is_magician):
    print("You need magic powers.")



