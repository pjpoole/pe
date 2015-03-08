#!/usr/bin/python

from math import sqrt
from math import floor
from math import ceil

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

def isprime(candidate):
	if candidate < 0: return False
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

def sumdigits(input):
	while (input >= 1):
		sum += input%10
		input /= 10
	return sum

def numberfactors(num):
    count = 0
    x = sqrt(num)
    y = int(ceil(x))
    if x - y == 0:
        count = 1
    count += 2*len(filter(lambda a: num%a == 0, range(1,y)))
    return count

def sumdivisors(num):
	sum = 1
	p = 2
	while p**2 <= num and num > 1:
		if num%p == 0:
			j = p**2
			num /= p
			while num%p == 0:
				j *= p
				num /= p
			sum *= j-1
			sum /= p-1
		if p == 2: p = 3
		else: p += 2
	if num > 1:
		sum *= num+1
	return sum

def sumproperdivisors(num):
	return sumdivisors(num)-num

def isabundant(num):
	return (num < sumproperdivisors(num))

def isperfect(num):
	return (num == sumdivisors(num))
