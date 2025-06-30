# This is an important file, it contains no codes and is created to address this doubt of:
# Why do we need scope?
# Why can't we define all things globally and have access to them always?
# Answer:
# For efficient memory usage. Elaboratively, when a fucntion runs a statement of say x = 4, it
# is not executed until we call the function and no memory is used in assigning 4 to x till then.
# Also when we call a function and its part is done the memory inside it like x = 4 is deleted again 
# as the interpreter believes that ok now that the function has been called and used, we don't
# need this x = 4 and hence it clears that memory for us to reuse.
# Now this small efficiency in memory of removing x = 4 after its use may sound less but it is useful
# when it comes to large codes.