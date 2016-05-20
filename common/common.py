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
			picked.append(thePick)
			if thePick in left:
				left.remove(thePick)
			else:
				continue
		
		results.append(picked)
		count += 1

	for i in results:
		return Counter(results[i])
	
print grind(2)

