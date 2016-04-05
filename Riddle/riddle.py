import random

possible1 = range(1,10)
possible2 = range(1,10)

possiblex = []
possiblesum = []

for i in possible1:
	for y in possible2:
		possiblex.append(i * y)
	
for i in possible1:
	for y in possible2:
		possiblesum.append(i + y)

possiblex = list(set(possiblex))
possiblesum = list(set(possiblesum))

def sumCount(number,range):
	count = 0
	for i in range:
		for y in range:
			if i + y == number:
				count += 1
	return count

def multCount(number,range):
	count = 0
	for i in range:
		for y in range:
			if i*y == number:
				count += 1
	return count
	

print sumCount(6, range(1,10))
print multCount(6, range(1,10))
	
possiblexeach = {}
possiblesumeach = {}

for i in possiblex:
	possiblexeach[i] = multCount(i,range(1,10))

for i in possiblesum:
	possiblesumeach[i] = sumCount(i,range(1,10))
	
print "Sums! {0}".format(possiblesumeach)
print "Mults! {0}".format(possiblexeach)

