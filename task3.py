import math
def getfactor(n):
	isprime=True
	for i in range(2,int(math.sqrt(n)+1)):
		if (n%i)==0:
			isprime=False
			if i!=n/i:
				print i
				print n/i
			else:
				print i
	if(isprime):
		print 'Prime Number'

n=int(raw_input('Enter number: '))
getfactor(n)



	
