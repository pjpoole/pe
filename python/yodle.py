#!/usr/bin/python

def trinumber(num):
	return int(num*(num+1)/2)

def reduceit(location, depth):
	reducedtri[location] = (max(reducedtri[location+depth],reducedtri[location+depth+1])
							+trianglelist[location])

trianglefile = open("/Users/pjpoole/Desktop/triangle.txt","r")

maxdepth = 100
trisize  = trinumber(maxdepth)

trianglelist = [[] for i in range(0,trisize)]
reducedtri	 = [[] for i in range(0,trisize)]


listindex = 0

for line in trianglefile:
	line = line.rstrip()
	splitline = line.split()
	for item in splitline:
		trianglelist[listindex] = int(item)
		listindex += 1

trianglefile.close()
	
reducedtri[trinumber(99):trisize]=trianglelist[trinumber(99):trisize]

ldepth = 99
dcounter = 99
for index in range(trinumber(99)-1,-1,-1):
	if (dcounter == 0):
		ldepth -= 1
		dcounter = ldepth
	reduceit(index,ldepth)
	dcounter -= 1
	
print reducedtri[0]