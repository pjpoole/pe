#!/usr/bin/python

# sum of all numbers divisible by three plus
# sum of all numbers divisible by five minus
# sum of all numbers divisible by fifteen
# (basic set theory)

from math import floor

def trinum(number):
	return (number * (number + 1))/2

maxthree = floor(1000/3)

agg = 3 * trinum(maxthree)

maxfive = floor(1000/5) - 1

agg += 5 * trinum(maxfive)

maxfifteen = floor(1000/15)

agg -= 15 * trinum(maxfifteen)

print agg
