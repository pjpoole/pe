#!/usr/bin/python

from palind import palindrome

maxnum=0
numb1 = 0
numb2 = 0

for num1 in range(1, 899):
	for num2 in range(1, num1):
		num3 = (1000-num1) * (1000-num2)
		if palindrome(num3):
			if maxnum < num3: 
 				maxnum=num3
 				numb1 = (1000-num1)
 				numb2 = (1000-num2)
			
print maxnum, numb1, numb2