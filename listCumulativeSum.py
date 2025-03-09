'''
Exercise 3  
Write a function that takes a list of numbers 
and returns the cumulative sum; 
that is, a new list where the ith element is the sum of the first i+1 elements from the original list. 
For example, 
the cumulative sum of [1, 2, 3] is [1, 3, 6].
'''

def cumSum(numList): 
    lNew = []
    i = 0
    total = 0
    for i in range(len(numList)):
        total += numList[i]
        lNew.append(total)  
        print(numList, lNew)
    return lNew 

numList =[1,2,3]
print(cumSum(numList))        



