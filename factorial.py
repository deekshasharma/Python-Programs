# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.
def factorial(number):
	product = 1
	while number!=0:
		product = product*number
		number = number -1
	return product



print factorial(4)
#>>> 24
#print factorial(5)
#>>> 120
#print factorial(6)
#>>> 720

