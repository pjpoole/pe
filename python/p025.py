#!/usr/bin/python

import sys
from math import floor

def suminplace(numone, numtwo):
	carrydig = 0
	tempdigsum = 0
	lenone = len(numone)
	lentwo = len(numtwo)
	for digit in range(lentwo):
		if (digit > lenone-1):
			numone.append(0)
			lenone += 1
		tempdigsum = carrydig + int(numone[digit]) + int(numtwo[digit])
		carrydig = int(floor(tempdigsum/10))
		numone[digit] = tempdigsum%10

	while (carrydig > 0):
		digit += 1
		if (digit > lenone-1):
			numone.append(0)
			lenone += 1
		tempdigsum = carrydig + int(numone[digit])
		carrydig = int(floor(tempdigsum/10))
		numone[digit] = tempdigsum%10
	
	return

thingy = [1]
whatev = [1]
alternate = True
fibindex = 2
maxlength = 1000

while (len(thingy) < maxlength and len(whatev) < maxlength):
	if (alternate):
		suminplace(thingy, whatev)
		alternate = False
	else:
		suminplace(whatev, thingy)
		alternate = True
	fibindex += 1

print fibindex

if (alternate):
	wlength = len(whatev)
	for i in range(wlength):
		digit = str(int(whatev[wlength-i-1]))
		sys.stdout.write(digit)
else:
	wlength = len(thingy)
	for i in range(wlength):
		digit = str(int(thingy[wlength-i-1]))
		sys.stdout.write(digit)

sys.stdout.write('\n')
print wlength