from __future__ import division
import random



def whichguyser():
	guysers = [random.randint(1,121), random.randint(1,241), random.randint(1,361)]
	return guysers.index(min(guysers))
	
count = 1
a = 0
b = 0
c = 0


while count < 1000000:
	whichOne = whichguyser()
	if whichOne == 0:
		#print "The lowest is guyser A!"
		a += 1
		count += 1
	elif whichOne == 1:
		#print "The lowest is guyser B!"
		b += 1
		count += 1
	elif whichOne == 2:
		#print "Whoa, the lowest is guyser C!"
		c += 1
		count += 1
	else:
		#print "Something happened."
		count += 1
		
print "A was {0}\nB was {1}\nC was {2}\n".format(a/(a+b+c),b/(a+b+c),c/(a+b+c))
