#!/usr/bin/python

maxinteger = 200000
primes = 0

factoring = open("factors.txt", "a")

factoring.write("0\n1\n")

factorlist = [[] for i in range(maxinteger)]

for index in range(2, maxinteger):
	if factorlist[index]==[]:
		primes += 1
		multiplier = 2
		while (index * multiplier < maxinteger):
			factorlist[(index * multiplier)].append(index);
			multiplier += 1
			
	factoring.write(str(index))
	
	for factors in range(len(factorlist[index])):
		factoring.write((", "+str(factorlist[index][factors])))
	factoring.write("\n")

factoring.close()