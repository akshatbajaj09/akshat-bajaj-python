# Again a just comment file to brief about some things.
# @classmethod and @staticmethod:
# The @classmethod has a default parameter of cls similar to self in regular methods.
# It is used to access and modify the elements of the whole class whereas
# @staticmethod doesn't have a default parameter and is used when we neither need class nor
# an object to be worked upon, it is general to the whole code.

# What is encapsulation:
# It is as the name suggests like wrapping up data in a capsule
# and protecting it from being change by the outside code.

# Private, Protected and Public variables:
# We have some private variables that we don't want to be changed so we have this idea
# of encapsulating them.
# We can access these private variables by a method called name mangling for example:
# A variable named self.__salary in a class say Employee
# is a private variable and can't be directly accessed but by name mangling
# we can use self._Employe__salary and access it. But this isn't recommended.
# The variables like self.salary are simply public variables and can be accessed safely.
# The variables like self._salary are protected variables and can also be accessed but it isn't
# a good practice to access them directly.