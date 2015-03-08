#!/usr/bin/python

factorial = 1
aggregate = 0

for i in range(1,100):
	factorial *= i
	
while (factorial >= 1):
	aggregate += factorial%10
	factorial /= 10
	
print aggregate