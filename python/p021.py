#!/usr/bin/python

amicable = [sum([x for x in range(1,i) if i%x == 0]) for i in range(0,10001)]

agg = 0

for i in range(0,10001):
	if amicable[i] <= 10000 and amicable[i] != i and amicable[amicable[i]]==i:
			agg += i

print agg