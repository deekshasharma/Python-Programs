#! /usr/bin/env python
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]



def check_sudoku(list1):
	column=[] 
	# this loop to traverse through the given list which is list1. ielement is each sublist inside the main list.
	for ielements in list1:
		# This for loop to traverse through the inner lists. jelements is each elements in ielement list
		for jelements in ielements:
			#checking the condition if each jelements start from 1 till len(list) or there are no duplicates in the rows of sudoku.
			if jelements not in range(1, len(list1) + 1) or ielements.count(jelements) > 1 :
				return "False row"
				# If the above condition is met then check the columns of sudoku
			else:
				# this loop to traverse through the index of each ielements in list1. The range of index will always start from 0 and end at len(list1)
				for index in range(0,len(list1)):
					#using list comprehensions to store the ielements[0] till ielements[2] in a variable "items".So all ielements at index 0 will be saved, then at index 1 and finally at index 2 
					items=[ielements[index] for ielements in list1]
					#now these elements are appended to the new emepty list column[]
					column.append(items)
					#check for the duplicates in column[]. this contains all columns from the sudoku.
					for newelements in column:
						for subelements in newelements:
							if newelements.count(subelements)>1:
								return "False column"


	return "True"




print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False