#!/usr/bin/python

from math import sqrt

for index in range(300, 500):
	for index2 in range(300, index):
		idiff = (index-index2)
		isum = (index+index2)
		imult = idiff*isum
		iroot = sqrt(imult)
		if (sqrt(imult)==int(sqrt(imult))):
			if ((iroot+index+index2)==1000):
				print index, index2, iroot
				print index*index2*iroot
			