#Procedure to find the biggest number in the given parameters

def biggest(a,b,c):
	if a>b and a>c:
		return a
	elif b>a and b>c:
		return b
	elif c>a and c>b:
		return c


#print biggest(4,7,8)

#procedure to find the median if three numbers are given

def median(a,b,c):
	if biggest(a,b,c)== a:
		if b>c:
			return b
		else:
			return c
	elif biggest(a,b,c)== b:
		if a>c:
			return a
		else:
			return c

	elif biggest(a,b,c)== c:
		if a>b:
			return a
		else:
			return b
		

print median(10,20,9)




