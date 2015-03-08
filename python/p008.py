#!/usr/bin/python

numberfile = open("/Users/pjpoole/Documents/euler/Problem8.txt", "r")

lines = numberfile.readlines()

bignumber = []
maxval = 0
maxindex = 0


for line in lines:
	line = line.rstrip()
	number = [int(letter) for letter in line]
	bignumber.extend(number)

for index in range(len(bignumber)-4):
	candidate = 1
	for iterat in range(5):
		candidate *= bignumber[index+iterat]
	if candidate > maxval:
		maxval = candidate
		maxindex = index

print maxval

numberfile.close()