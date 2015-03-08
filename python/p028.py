#!/usr/bin/python
# commented code does the exact same thing as uncommented code
# accum = 0
# 
# i = 1
# k = 1
# 
# while (i < 1001**2):
# 	for j in [0,1,2,3]:
# 		accum += i
# 		i += 2*k
# 	k += 1
# 	
# accum += 1001**2
# 	
# print i, j, k
# 
# print accum
# 
accum = 0

for i in range(1, 501):
	accum += (2*i+1)**2 - 3 * i
	
accum *= 4

accum += 1

print accum