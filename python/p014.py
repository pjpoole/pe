#!/usr/bin/python
#run time real	0m9.444s

depthdict	= dict.fromkeys(range(1,1000000),0)
depthdict[1]= 1

tracestack = []

maxlink = 0

for numbertest in range(1,1000000):
	linknumber = numbertest
	while (depthdict.setdefault(linknumber, 0) == 0):
		tracestack.append(linknumber)
		if (linknumber%2==0):
			linknumber /= 2
		else:
			linknumber = 3*linknumber+1	
		if linknumber > maxlink: maxlink = linknumber
			
	height = depthdict[linknumber]
	
	while (len(tracestack)>0):
		height += 1
		previous = tracestack.pop()
#		nextarray[previous] = linknumber
		depthdict[previous] = height

maxdepth = 0
maxindex = 0

print "Finding max"

for numbertest in range(1,1000000):
	if (depthdict[numbertest] > maxdepth):
		maxdepth = depthdict[numbertest]
		maxindex = numbertest
		
print maxdepth, maxindex

print maxlink