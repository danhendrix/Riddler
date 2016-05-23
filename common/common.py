import random
from collections import Counter

def grind(number):
	count = 1
	results = []
	while count <= number: 
		choices = ["common", "common", "common", "uncommon", "uncommon", "rare"]
		left = ["common", "uncommon", "rare"]
		picked = []

		thePick = random.choice(choices)

		left.remove(thePick)

		while len(left) > 0:
			thePick = random.choice(choices)
			results.append(thePick)
			if thePick in left:
				left.remove(thePick)
			else:
				continue
		
		#results.append(picked)
		count += 1

	return Counter(results)
	
print grind(1000000)

#Results from 1,000,000 simulations: Common: 3.157733 Uncommon: 2.102899 Rare: 1.050436