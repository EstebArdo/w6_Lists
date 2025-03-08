
a='banana'
b='banana'
a is b
# True
# a and b refer to the same string object.

c=[1,2,3]
d=[1,2,3]
c is d
# False
# c and d refer to two different objects 
#   that are equivalent.
# When you create two lists, you get two objects

#############################################
# Aliasing

e = 'apple'
f = e
e is f
# True - f is an alias to e.  both refer to the same object.
# e and f are variables that reference the same object.

# object with  more than 1 reference has more than one name.
# So we say this object is "Aliased."
###########################################
# if the object is mutable.
# changes to one alias affect the other.

#usually avoid aliasing to avoid errors with mmutable objects.
# For MImmutable objects like strings, it is not much of a problem.
