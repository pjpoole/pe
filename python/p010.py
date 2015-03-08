#!/usr/bin/python
# runs in 0m25.065s

from funfunctions import primetest

aggregator = 0
index = 2

while (index < 2000000):
	if primetest(index): aggregator += index
	index += 1
	
print aggregator