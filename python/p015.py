#!/usr/bin/python

solution = 1

for i in range(21,41):
	solution *= i

for i in range(1,21):
	solution /= i
	
print solution