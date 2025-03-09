###############################################################
# List as Argument
# pass a list to a function and the function gets
#  a reference to the list.  And so if it changes a 
#  list parameter then the caller sees the change.

# In this example, the parameter t and the variable "letters" 
#   are aliases for the same object.

def delete_head(t):
    del t[0]

letters = ['a','b','c']
delete_head(letters)
print(letters)



