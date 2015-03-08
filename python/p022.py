#!/usr/bin/python

namesfile = open("/Users/pjpoole/Documents/euler/names.txt","r")

allnames = namesfile.read()

namesfile.close()

nameslist = allnames.strip('\"').split('\",\"')

del allnames

nameslist.sort()

indexer = 1
totaler = 0
subtotal= 0

for name in nameslist:
	for chara in name:
		subtotal += ord(chara)-ord('A')+1
	totaler += subtotal*indexer
	subtotal = 0
	indexer += 1
	
print totaler

#for i in range(0,10):
#	print nameslist[i]