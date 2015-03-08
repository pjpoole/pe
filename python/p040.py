#!/usr/bin/python

numstring = ''

for i in range(0,1000000):
	numstring += str(i)

blah = 1

for i in range(0,7):
	blah *= int(numstring[10**i])

print blah