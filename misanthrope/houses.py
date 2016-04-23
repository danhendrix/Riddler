import random
from bokeh.plotting import figure, output_file, show

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
			
	return float(len(taken))/size
	
def test(number):
	count = 0
	results = []
	while count < 1000:
		results.append(movingIn(number))
		count += 1
	return float(sum(results))/1000
	
testResults = []
numbers=range(101)

for i in numbers[1:len(numbers)]:
	testResults.append(test(i))
	
print testResults[99]

output_file("lines.html", title="Home Buyers")

p = figure(title="Misanthrope", x_axis_label="Number of Homes", y_axis_label='Percentage Occupied')

p.line(numbers[1:len(numbers)],testResults)

show(p)
