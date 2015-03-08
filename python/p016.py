#!/usr/bin/python

digits = [0]*303

digits[0] = 2
highest = 2
tempo = 0

for index in range(1,1000):
	carry = 0
	for digit in range(0,highest):
		tempo = digits[digit]*2+carry
		if (tempo >= 10):
			carry = 1
			tempo -= 10
		else:
			carry = 0
		digits[digit] = tempo
	if (digits[highest-1] == 1): highest += 1

digitsum = 0
	
for index in range(0,302):
	digitsum += digits[index]
	
print digitsum