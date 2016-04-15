global budget
global days

budget = 1000000000
days = 1600

def getRussianEngines(number):
	global budget
	global days
	if number == 1: 
		budget -= 400000000
		days -= 200
	elif number ==2:
		budget -= 400000000 * number
		days -= (200 + (100* (number-1)))

def getIonEngines(number):
	global budget
	global days
	budget -= number * 150000000
	days  -= (50 * number)
	
	
def lightPayloads(number):
	global budget 
	budget -= 50000000 * number
	global days 
	days -= 25 * number
	
getRussianEngines(1)
getIonEngines(3)
lightPayloads(3)

print budget, days

#1,3,3 = 1,175 days

russianEngine = float(400000000 / 200)
ion = float(150000000/50)
payloads = float(50000000 / 25)

print russianEngine
print ion
print payloads