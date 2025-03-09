############################################
# It is important to distinguish between operations that modify lists 
# and operations that create new lists. 

t1 = [1,2]

# append does not return anything
# so it doesn't create a new list in t2.
t2 = t1.append(3)

print(t1)
print(t2)

###################################
# Concatenate two lists with the + operator.
#   so t3 is a new list.
t3 = t1 + [4]
print(t3)
[1,2,3,4]
