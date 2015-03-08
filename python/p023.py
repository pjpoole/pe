#!/usr/bin/python

from funfunctions import isabundant

maxint = 20162

abundant = [i for i in range(1,maxint) if isabundant(i)]

sumofabundant = [False for i in range(1,2*maxint)]

for index in range(len(abundant)):
	for jndex in range(index,len(abundant)):
		sumofabundant[abundant[index] + abundant[jndex] - 1] = True

total = 0

for index in range(maxint):
	if (not sumofabundant[index]):
		total += index+1
		maxindex = index
		
print maxindex
		
print total