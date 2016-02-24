



def vote(x,y):
	voteFirst = 0
	voteSecond = 0
	
	a = ["A", "B", "C", "D", "E"]
	b = ["B", "A", "E", "D", "C"]
	c = ["C", "D", "A", "E", "B"]
	d = ["D", "B", "A", "E", "C"]
	e = ["E", "D", "B", "C", "A"]

	list = [a, b, c, d, e]
	
	for i in list:
		if i.index(x) < i.index(y):
			voteFirst += 1
		else:
			voteSecond += 1
	
	if voteFirst > voteSecond:
		return x, y
	else:
		return y, x


winner1, loser1 = vote("A","B")
winner2, loser2 = vote(winner1,"C")
winner3, loser3 = vote(winner2,"D")
winner4, loser4 = vote(winner3,"E")

print "Here are your final standings:\n{0}\n{1}\n{2}\n{3}\n{4}".format(winner4, loser4, loser3, loser2, loser1)





