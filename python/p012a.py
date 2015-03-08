#!/usr/bin/python

from math import sqrt
from math import floor

def primetest( candidate ):
	candroot = floor(sqrt(candidate))
	
	if candidate <= 1: return False
	if candidate < 4: return True
	if candidate%2 == 0: return False
	if candidate < 9: return True
	if candidate%3 == 0: return False
	
	testfactor = 5
	
	while (testfactor <= candroot):
		if candidate%testfactor == 0: return False
		if candidate%(testfactor+2) == 0: return False
		testfactor += 6
	
	return True

candi = 1
primes = [2]

while candi <= 2**16:
	candi += 2
	if primetest(candi):primes.append(candi)

n = 3
Dn = 2
count = 0

while count <= 500:
	n = n+1
	n1 = n
	if n1%2 == 0: n1 = n1/2
	Dn1 = 1
	
	for index in range(len(primes)):
		
		if primes[index]*primes[index] > n1:
			Dn1 *= 2
			break
		
		exponent = 1
		
		while n1%primes[index] == 0:
			exponent += 1
			n1 = n1/primes[index]
			
		if exponent > 1: Dn1 *= exponent
			
		if n1 == 1: break
	
	count = Dn * Dn1
	Dn = Dn1
	
print n*(n-1)/2