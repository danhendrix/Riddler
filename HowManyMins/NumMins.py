import random
def presents():
	possibleTime = [1,2,3,4,5]
	sameTime = False
	waitTime = 0
	wait1 = 0
	wait2 = 0	
	while sameTime == False:
		if(wait1 == wait2 and wait1 > 0):
			waitTime += wait1
			sameTime = True
			
		else:
			choice1 = random.choice(possibleTime)
			wait1 += choice1
			if(wait1 == wait2):
				waitTime += wait1
				sameTime = True
			elif(wait1 < wait2 and wait2 > 0):
				choice1 = random.choice(possibleTime)
				wait1 += choice1
				if(wait1 == wait2):
					waitTime += wait1
					sameTime = True
				else:
					choice2 = random.choice(possibleTime)
					wait2 += choice2
					if(wait1 == wait2):
						waitTime += wait1
						sameTime = True
					elif(wait2 < wait1):
						choice2 = random.choice(possibleTime)
						wait2 += choice2
						if(wait1 == wait2):
							waitTime += wait1
							sameTime = True
					
			else:
				choice2 = random.choice(possibleTime)
				wait2 += choice2
				if(wait1 == wait2):
					waitTime += wait1
					sameTime = True
				elif(wait2 < wait1):
					choice2 = random.choice(possibleTime)
					wait2 += choice2
					if(wait1 == wait2):
						waitTime += wait1
						sameTime = True
				
				else:
					continue
	return waitTime				
		
count = 0
waitingTotal = []
while count < 10:
	waitingTotal.append(presents())
	count += 1
	

print float(sum(waitingTotal)) / float(len(waitingTotal))


	
	
		
		
		
		###choice1 = random.choice(possibleTime)
	###choice2 = random.choice(possibleTime)
	###wait1 += choice1
	###wait2 += choice2 
	