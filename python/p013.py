#!/usr/bin/python
# there are several ways to do this.
# one of them involves iterating all of the digits in the file in order from smallest to largest,
# 	carrying as you go - since there are 100 numbers, the max carry from each sum is 1000,
#	which is hardly big enough to be worrysome.
# in this method, we would enqueue/dequeue up to ten digits at a time, using 
#	from collections import deque
#	and the appendleft() and pop() methods to add/remove digits.
# instead, I'll just be generating the entire sum and rolling with it.

summands = open("/Users/pjpoole/Documents/euler/problem13.txt","r")

total = [0,[]]

for line in summands:
	line = line.rstrip()
	linelength = len(line)
	for digit in range(0,linelength):
		if total[digit+1] == []:
				total[digit+1] = 0
				total.append([])
		total[digit] += int(line[linelength-digit-1])
		for element in range(len(total)-1):
			while (total[element] >= 10):
				if total[element+1] == []:
					total[element+1] = 0
					total.append([])
				total[element] -= 10
				total[element+1] += 1
		
print total

summands.close()

