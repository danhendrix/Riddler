import random

def movingIn(size):
	open = range(size)
	taken = []
	houseVisits = 0

	while houseVisits < size:
		houseWanted = random.choice(open)
		if houseWanted + 1 in taken or houseWanted - 1 in taken:
			open.remove(houseWanted)
			houseVisits +=1
		else:
			taken.append(houseWanted)
			open.remove(houseWanted)
			houseVisits += 1
			
	return len(taken)
	
print movingIn(100000)
	