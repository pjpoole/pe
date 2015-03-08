#!/usr/bin/python

numberdict 	= {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',
				9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
				16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',
				40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',
				1000:'thousand'}
				
words = ['' for i in range(0,1000)]
digits = [0,0,0,0]


for index in range(len(words)):
	curnumber = index+1
	for poweroften in [0,1,2,3]:
		digits[poweroften] = curnumber%10
		curnumber /= 10
	if (digits[3] == 1):
		words[index] += numberdict[(digits[3])]+numberdict[1000]
	if (digits[2] >= 1):
		words[index] += numberdict[(digits[2])]+numberdict[100]
	if ((digits[1]*10+digits[0] != 0) and ((digits[2] != 0) or (digits[3] != 0))):
		words[index] += 'and'
	if (digits[1] <=1):
		words[index] += numberdict[(digits[1]*10+digits[0])]
	else:
		words[index] += numberdict[(digits[1]*10)]+numberdict[(digits[0])]
	
print words

lenaccum = 0

for index in range(len(words)):
	lenaccum += len(words[index])
	
print lenaccum