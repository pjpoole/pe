#!/usr/bin/python
# runs in real	0m23.505s

from funfunctions import primetest

aggregator = 5
index = 5

while (index < 2000000):
	if primetest(index): aggregator += index
	index += 2
	
print aggregator