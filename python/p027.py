#!/usr/bin/python
# 
#  it must be the case that a > -(b+1)
#  This problem is a modification of euler's original forumla, 
#  n**2 + n + 41, and a shifts by -2 each time
#  Generating a list of primes under, say, 1 million in a text file
#  might speed things up
#  b is always prime - why?

from funfunctions import isprime

def f(n,a,b):
	return n**2+a*n+b

maxa = 0
maxb = 0
maxn = 0
n = 0

for a in range(-999,1000,1):
	for b in range(-999,1000,1):
		n = 0
		while isprime(f(n,a,b)):
			n += 1
		if n > maxn:
			maxa = a
			maxb = b
			maxn = n
			
print maxa*maxb