#!/usr/bin/python

def trinumber(num):
	return int(num*(num+1)/2)

# def bfs(location, depth):
# 	if (depth == 100):
# 		return trianglelist[location]
# 	else:
# 		return (max(bfs(location+depth,depth+1),bfs(location+depth+1,depth+1))+trianglelist[location])

def reduceit(location, depth):
	reducedtri[location] = (max(reducedtri[location+depth],reducedtri[location+depth+1])
							+trianglelist[location])

trianglefile = open("/Users/pjpoole/Documents/euler/triangle.txt","r")
directions	 = open("/Users/pjpoole/Documents/euler/triangle3.txt","w")

maxdepth = 100
trisize  = trinumber(maxdepth)

trianglelist = [[] for i in range(0,trisize)]
reducedtri	 = [[] for i in range(0,trisize)]
stringtri    = [[] for i in range(0,trisize)]

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

	
accum = 0
lpdepth = 1

for index in range(0,trinumber(99)):
	if (reducedtri[index+lpdepth]>reducedtri[index+lpdepth+1]):
		stringtri[index] = 'left'
	else:
		stringtri[index] = 'righ'
	
	accum += 1
	
	if (accum == lpdepth):
		lpdepth += 1
		accum = 0

		
accum = 0
lpdepth = 1

for index in range(0,trinumber(99)):
	directions.write(str(stringtri[index]).rjust(5))
	
	accum += 1
	
	if (accum == lpdepth):
		lpdepth += 1
		accum = 0
		directions.write('\n')
		
directions.close()

