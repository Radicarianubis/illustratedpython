friends = ['Bob', 'Mary', 'John', 'George', 'Axel', 'Jason', 'Monty', 'Judas']
friendavg = 0
#print(len(friends[0]))
for name in friends:
	friendavg += len(name)
avg = (friendavg / len(friends))
print(avg)

johnCheck = False

for name in friends:
	if name != 'John':
		continue
	else:
		johnCheck = True

if johnCheck == False:
	print('Not found')

# Problem 3:
ages = (28, 14, 20, None, 32, 48)
firstnames = ('Ward', 'Zinik', 'Peta', 'John', 'Fox', 'Janet')
lastnames  = ('Maurd', 'Felice', 'Moroan', 'Clement', 'McCloud', 'Oreo')
# Calculate averag age first
ageavg = 0
for num in ages:
	if num == None:
		print('No age')	
	else:
		ageavg += num
ageavg = (ageavg / len(ages))
# Get first and last names into a list
# Smelly Code
#counter = 0
#for name in firstnames:
#	x = (name + ' ' + lastnames[0])
#	counter += 1
#	fullname.append(x)
fullnames = []
for index, name in enumerate(firstnames):
	x = (name + ' ' + lastnames[index])
	fullnames.append(x)
fulllist = []
for index, fullname in enumerate(fullnames):
	age = ages[index]
	if age == None:
		print("We don't know the age of " + fullname)
		continue
	if age > ageavg:
		print(fullname + ' is old!')
	elif age < ageavg:
		print(fullname + ' is young!')


	


	


	



