#!/usr/bin/python

def trinumber(num):
	return int(num*(num+1)/2)

def reduceit(location, depth):
	reducedtri[location] = (max(reducedtri[location+depth],reducedtri[location+depth+1])
							+trianglelist[location])

trianglefile = open("/Users/pjpoole/Documents/euler/triangle5.txt","r")

maxdepth = 15
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
	
reducedtri[trinumber(maxdepth-1):trisize]=trianglelist[trinumber(maxdepth-1):trisize]

ldepth = maxdepth-1
dcounter = maxdepth-1
for index in range(trinumber(maxdepth-1)-1,-1,-1):
	if (dcounter == 0):
		ldepth -= 1
		dcounter = ldepth
	reduceit(index,ldepth)
	dcounter -= 1
	
print reducedtri[0]