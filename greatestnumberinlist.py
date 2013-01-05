# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.
#list1=[8,9,52,21,56,3,78]
def greatest(list1):
    max=0
    for i in list1:
        if i > max:
            max = i
            i=i+1
    return max
    
            
        
            




print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
