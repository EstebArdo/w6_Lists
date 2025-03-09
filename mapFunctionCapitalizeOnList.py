def capitalize_all(t):
    res =[]
    for s in t:
        res.append(s.capitalize())
    return res

lTest = ['w','a','t','u','o','p']
lCap = capitalize_all(lTest)
print(lCap)

