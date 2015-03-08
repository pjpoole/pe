#!/usr/bin/python
# 
# def trinum(num):
# 	return int((num*(num+1))/2)
# 
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

def nofactors(num):
    count = 0
    x = sqrt(num)
    y = int(ceil(x))
    if x - y == 0:
        count = 1
    count += 2*len(filter(lambda a:num % a ==0,range(1,y)))    
    return(count)

num1 = 1
num2 = 1
altr = True

while True:
	
	divisors = nofactors(num1) * nofactors(num2) -1
	
	if divisors > 500:
		print num1*num2
		break

	if altr:
		num2 += 2
	else:
		num1 += 1
		
	altr = not altr