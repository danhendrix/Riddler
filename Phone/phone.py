import random

#breakHeight = random.randint(1,101)
breakHeight = 60
guessCap = 100



def drop(dropHeight):
	if dropHeight >= breakHeight:
		print "It broke at {0}!".format(dropHeight)
		return True
	else:
		print "It's all good at {0}.".format(dropHeight)
		return False
		

guess = 3
if drop(guess) == True:
	if drop((guess -2)) == True:
		print "It seems to break at {0}!".format(guess - 2)
	elif drop((guess -1)) == True:
		print "It seems to break at {0}!".format(guess - 1)
	else:
		print "It seems to break at {0}!".format(guess)
	
else:
	guess += 3
	while guess <= guessCap:
		if drop(guess) == True:
			if drop((guess - 2)) == True:
				print "It seems to break at {0}!".format(guess -2)
				break
			elif drop((guess - 1)) == True:
				print "It seems to break at {0}!".format(guess -1)
				break
			else:
				print "It seems to break at {0}!".format(guess)
				break
		else:
			guess += 3
			
		if guess >= guessCap:
			if drop((guess - 2)) == True:
				print "It seems to break at {0}!".format(guess -2)
				break
			elif drop((guess - 1)) == True:
				print "It seems to break at {0}!".format(guess -1)
				break
			else:
				print "It seems to break at {0}!".format(guess)
				break
				
			
			
		
			
	
	
	


