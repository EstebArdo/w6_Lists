############################################
# Deleting elements from lists
# 
# delete with pop

t = ['a','b','c']
print(t)
x = t.pop(1)
print(t)
print(x)

t.append('d')
print(t)

#######################################
# delete with del operator

print('###################################')
t = ['a','b','c']
print(t)
del t[1]
print(t)

#############################################
# delete with remove using element name.
print('###################################')
t = ['a', 'b', 'c']
print(t)
t.remove('b')
print(t)


#############################################
# delete with slice index.

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t)
del t[1:5]
print(t)

