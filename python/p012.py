#!/usr/bin/python
# 
# def trinum(num):
# 	return int((num*(num+1))/2)
# 
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

num1 = 1
num2 = 1
numprimes = 0
altr = True
primes = [2]

while True:
	tem1 = num1
	tem2 = num2
	divlist = []
	primenum = 0
	divisor = -1
	
	if primetest(num2):
		if primes[numprimes] != num2:
			primes.append(num2)
			numprimes += 1
	
	while tem1 > 1 or tem2 > 1:
		prime = primes[primenum]
		if tem1%prime == 0 or tem2%prime == 0:
			divisor += 1
			divlist.append(0)
			while tem1%prime == 0:
				divlist[divisor] += 1
				tem1 /= prime
			while tem2%prime == 0:
				divlist[divisor] += 1
				tem2 /= prime
		primenum += 1
		
	divisors = 1
	
	for index in range(divisor+1):
		divisors *= divlist[index]+1
		
	if divisors > 500:
		print num1*num2
		break

	if altr:
		num2 += 2
	else:
		num1 += 1
		
	altr = not altr