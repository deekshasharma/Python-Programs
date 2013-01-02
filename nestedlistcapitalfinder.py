# Given the variable countries defined as:


#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the array.

def capital_finder(country):
	n=0
	while True:
		if countries[n][0]==country:
			return countries[n][1]
		else:
			n=n+1


print capital_finder('India')