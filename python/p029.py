#!/usr/bin/python

maxint = 100

thingy = [0 for i in range(0,(maxint+1)**2)]

for a in range(2,maxint+1):
	for b in range(2,maxint+1):
		thingy[maxint*(a-1)+b]=a**b
		
print len(set(thingy))-1
