# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(n):
	month=1
	z=0
	while month<=n:
		result = days_in_month[z]
		month = month+1
		z = z+1
	return result

		
		
    


print how_many_days(1)
#>>> 31

#print how_many_days(9)
#>>> 30