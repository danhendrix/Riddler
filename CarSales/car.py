import random

def sale():

	n = random.randint(1000,5000)

	cards = [n, n+100, n+200, n+300, n+400]
	random.shuffle(cards)

	options = [cards[0] + 100, cards[0] + 200, cards[0] + 300, cards[0] + 400, cards[0] - 100, cards[0] - 200, cards[0] - 300, cards[0] - 400]


	options.remove(cards[1])
	options = [x for x in options if x <= min(cards[0] + 400, cards[1] + 400) and x >= max(cards[0] - 400, cards[1] - 400)]

	expected = sum(options)/len(options)
	if expected > cards[1]:
		return (cards[1] - n)
	else:
		options.remove(cards[2])
		options = [x for x in options if x <= min(cards[0] + 400, cards[1] + 400, cards[2] + 400) and x >= max(cards[0] - 400, cards[1] - 400, cards[2] - 400)]

		expected = sum(options)/len(options)
		if expected > cards[2]:
			return (cards[2] - n)
		else:
			options.remove(cards[3])
			options = [x for x in options if x <= min(cards[0] + 400, cards[1] + 400, cards[2] + 400, cards[3] + 400) and x >= max(cards[0] - 400, cards[1] - 400, cards[2] - 400, cards[3] - 400)]

			expected = sum(options)/len(options)
			if expected > cards[3]:
				return (cards[3] - n)
			else:
				return (cards[4] - n)

count = 0
results = []
while count < 1000000:
	results.append(sale())
	count += 1
	
print float(sum(results)/len(results))
	

