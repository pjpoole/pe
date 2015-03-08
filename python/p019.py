#!/usr/bin/python

caloffset 		= [31,28,31,30,31,30,31,31,30,31,30,31]
leapoffset		= [31,29,31,30,31,30,31,31,30,31,30,31]

firstsundays	= 0
dayoftweek		= 366

for index in range(1,101):
	print 1900+index
	if (index%4 == 0):
		for offset in leapoffset:
			if (dayoftweek%7 == 0):
				firstsundays += 1
				print dayoftweek
			dayoftweek += offset
	else:
		for offset in caloffset:
			if (dayoftweek%7 == 0):
				firstsundays += 1
				print dayoftweek
			dayoftweek += offset

print firstsundays