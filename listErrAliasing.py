nums = [1,2,3,4]
chars = ['a','b','c','d']
t = chars.sort()
print(t)
# none

# To add an element to a list.
t = [1,2,3,4]
x = 44
t.append(x)
print(t)
t = t + [x]
print(t)

# these are wrong
print('###### These are wrong #######')
x=55
#t.append([x])
#t=t.append(x)
t+[x]
print(t)

###
t=t+x
# TypeError: can only concatenate list (not "int") to list

#######################################3
# So Make copies to avoid aliasing!!
orig = t[:]
t.sort()
# or use the func sorted()

