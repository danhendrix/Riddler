#Riddler Feb 21
import random


def seatTest():
	openSeatsList = range(1,101)
	openSeats = range(1,101)
	seatList = []
	line = []
	seatsTaken = []

	for x in range(1,101):
		seatList.append(random.choice(openSeatsList))
		openSeatsList.remove(seatList[x-1])
		
	firstGuy = random.choice(openSeats)
	openSeats.remove(firstGuy)
	seatsTaken.append(firstGuy)

	line = sorted(seatList, key=lambda k: random.random())
	counter = 1

	while counter < 99:
		if line[counter] in openSeats:
			openSeats.remove(line[counter])
			seatsTaken.append(line[counter])
			counter += 1
		else:
			seat = random.choice(openSeats)
			openSeats.remove(seat)
			seatsTaken.append(seat)
			counter += 1
			
	return line[99] == openSeats[0]
	
testResults = []
testCount = 0
while testCount < 1000:
	testResults.append(seatTest())
	testCount += 1
	

print float(sum(testResults))/len(testResults)

		
		
		

