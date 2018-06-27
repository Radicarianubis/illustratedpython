friends = ['Bob', 'Mary', 'John', 'George', 'Axel', 'Jason', 'Monty', 'Judas']
friendavg = 0
#print(len(friends[0]))
for name in friends:
	friendavg += len(name)
avg = (friendavg / len(friends))
print(avg)

for name in friends:
	if name != 'John':
		continue	
	else:
		print('Not found')
	
