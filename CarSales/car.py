import random

n = random.randint(1000,50001)

cards = [n, n+100, n+200, n+300, n+400]
random.shuffle(cards)

options = [cards[0] + 100, cards[0] + 200, cards[0] + 300, cards[0] + 400, cards[0] - 100, cards[0] - 200, cards[0] - 300, cards[0] - 400]




print "Your first card is....{0}!".format(cards[0])
choice = input("Do you want to take it? (Y)/(N)")

if choice == "n" or "N":
	print ("Ok..fine. Your next card is {0}").format(cards[1])
else:
	print "I think that means yes. Congratulations! By the way I would have taken {0}".format(n)

options.remove(cards[1])
options = [x for x in options if x <= min(cards[0] + 400, cards[1] + 400) and x >= max(cards[0] - 400, cards[1] - 400)]

expected = sum(options)/len(options)

print "Well, the expected value at this point is {0}".format(expected)
choice = input("Do you want to take it? (Y)/(N)")

if choice == "n" or "N":
	print ("Ok..fine. Your next card is {0}").format(cards[2])
else:
	print "I think that means yes. Congratulations! By the way I would have taken {0}".format(n)
	
options.remove(cards[2])

options = [x for x in options if x <= min(cards[0] + 400, cards[1] + 400, cards[2] + 400) and x >= max(cards[0] - 400, cards[1] - 400, cards[2] - 400)]

expected = sum(options)/len(options)

print "Well, the expected value at this point is {0}".format(expected)
choice = input("Do you want to take it? (Y)/(N)")

if choice == "n" or "N":
	print ("Ok..fine. Your next card is {0}").format(cards[3])
else:
	print "I think that means yes. Congratulations! By the way I would have taken {0}".format(n)

options.remove(cards[3])

options = [x for x in options if x <= min(cards[0] + 400, cards[1] + 400, cards[2] + 400, cards[3] + 400) and x >= max(cards[0] - 400, cards[1] - 400, cards[2] - 400, cards[3] - 400)]

expected = sum(options)/len(options)

print "Well, the expected value at this point is {0}".format(expected)
choice = input("Do you want to take it? (Y)/(N)")

if choice == "n" or "N":
	print "Well you held out for either the big prize or..not. Here's your price: ${0}".format(cards[4])
else:
	print "I think that means yes. Congratulations! By the way I would have taken {0}".format(n)
	