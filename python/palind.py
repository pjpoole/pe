#!/usr/bin/python

def palindrome(candidate):
	
	digits = []
	
	while (candidate >= 1):
		digits.append(candidate%10)
		candidate /= 10
	
	lengthofnum = len(digits)
	for index in range(lengthofnum/2):
		if digits[index] != digits[(lengthofnum - index - 1)]:
			return False
	
	return True