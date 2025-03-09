########################################################
# Forum 6
########################################################

tomsClasses = ['math', 'reading','science'] 
davidsClasses =  ['math', 'reading','science']
tomsClasses is davidsClasses 
# False 
# When creating the two lists they are separate objects.

###########################################################
# Try it with strings instead of lists....

Subject1 = 'Chemistry'  
Subject2 = 'Chemistry'  
Subject1 is Subject2
# True
# When creating two variables for the string,
#   you are creating two variables pointing to the same object.
# so the is operator returns True.