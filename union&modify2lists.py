# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def union(list1,list2):
	for i in list1:
		for j in list2:
			if j not in list1:
				list1.append(j)
	#print list1
			
				

	




# To test, uncomment all lines 
# below except those beginning with >>>.

list1 = [1,2,3]
list2 = [2,4,6]
union(list1,list2)
print list1 
#>>> [1,2,3,4,6]
#print list2
#>>> [2,4,6]
