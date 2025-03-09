####################################################
# list argument 
t = [1,2,3] 
print(t)

print(t[1:]) 
print(t)

# function only deletes from a local copy.
#   original list is unaffected.
def bad_delete_head(t):
    t = t[2:]
    print(t)

bad_delete_head(t)
print(t)    

########################################
# Alternative way is to write a function that 
#  creates and returns a new list.

def tail(t):
    return t[1:]

tLetters = ['a','b','c']
print('The letters : ', tLetters)
rest = tail(tLetters)
print('The tail of letters: ', rest)

