#!/usr/bin/python

def trinumber(num):
	return int(num*(num+1)/2)

def reduceit(location, depth):
	reducedtri[location] = (max(reducedtri[location+depth],reducedtri[location+depth+1])
							+trianglelist[location])

trianglefile = open("/Users/pjpoole/Documents/euler/triangle.txt","r")
outputtri	 = open("/Users/pjpoole/Documents/euler/triangle2.txt","a")

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

accum = 0
lpdepth = 1

for index in range(0,trinumber(100)):
	outputtri.write(str(trianglelist[index]).rjust(5)+',')
	
	accum += 1
	
	if (accum == lpdepth):
		lpdepth += 1
		accum = 0
		outputtri.write('\n')
		
outputtri.close()
		