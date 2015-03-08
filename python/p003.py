#!/usr/bin/python

from math import sqrt

bignumber = 600851475143

root = int(sqrt(bignumber))
rootlist = []

for iterat in range(3, root):
	if bignumber%iterat == 0: 
		rootlist.append(iterat)
		bignumber /= iterat
		iterat -= 1

print rootlist
