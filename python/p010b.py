#!/usr/bin/python
# run time real	0m1.343s

from math import sqrt
from math import floor
from funfunctions import primetest

maxvalue = 2000000

sievebound = (maxvalue - 1)/2
maxindex = int((floor(sqrt(maxvalue))-1)/2)

sieve = [True]*sievebound

for index in range(1, maxindex):
	if sieve[index]:
		for jndex in range((2*index*(index+1)),sievebound,(2*index+1)):
			sieve[jndex] = False

aggregator = 2

for index in range(1, sievebound):
	if sieve[index]: 
		aggregator += (2*index+1)

	
print aggregator