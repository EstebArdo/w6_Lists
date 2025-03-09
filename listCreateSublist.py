####################################
# A filter - filters out some of the members 
# of the list and then 
# we can append them to a new list.

def only_upper(t):
    res=[]
    for s in t:
        if s.isupper():
            res.append(s)
            print(res)
    return res

lTest = ['A','b','C','d','E','f']

lNew = only_upper(lTest)
print('Original:', lTest)
print('New:', lNew)
