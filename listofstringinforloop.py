# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

#p=['Dave','Sebastian','Katy']
#print p[1][0]
def measure_udacity(p):
	sum=0 
	for i in range(len(p)):
		if p[i][0]=='U':
			sum=sum+1
	return sum

#print measure_udacity(p)


print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2