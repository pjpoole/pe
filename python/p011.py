#!/usr/bin/python

numberfile = open("/Users/pjpoole/code/py Project Euler code/problem11.txt", "r")
numbergrid = [[0 for i in range(20)] for j in range(20)]

# the first index in a python array is the row count.
# the second index, then, is the column count.

for rows in range(0,20):
	numberline = numberfile.readline()
	for columns in range(0,20):
		numbergrid[rows][columns] = int(numberline[(columns*3):(columns*3+2)])

numberfile.close()

maxproduct = 0
#datalist = [0,0,0]
	
for rows in range(0,20):
	for columns in range(0,17):
		horizproduct = 1
		vertproduct = 1
		for offset in range(0,4):
			horizproduct *= numbergrid[rows][columns+offset]
			vertproduct *= numbergrid[columns+offset][rows]
		if (horizproduct > maxproduct):
			maxproduct = horizproduct
#			datalist = [rows, columns, 1]
		if (vertproduct > maxproduct):
			maxproduct = vertproduct
#			datalist = [columns, rows, 2]
			
for rows in range(0,17):
	for columns in range(0,17):
		product1 = 1
		product2 = 1
		for offset in range(0,4):
			product1 *= numbergrid[rows+offset][columns+offset]
			product2 *= numbergrid[rows-offset+3][columns+offset]
		if (product1 > maxproduct):
			maxproduct = product1
#			datalist = [rows, columns, 3]
		if (product2 > maxproduct):
			maxproduct = product2
#			datalist = [rows, columns, 4]
	
print maxproduct
#print datalist