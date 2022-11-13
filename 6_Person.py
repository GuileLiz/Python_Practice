persons_1 = {
	'first_name':'guile',
	'last_name':'liz',
	'age':26,
	'city':'Bulacan'
	}
for key, value in persons_1.items():
	print(f'{key}: {str(value).title()}')

persons_2 = {
	'first_name':'trixie',
	'last_name':'liz',
	'age':19,
	'city':'Bulacan'
	}
people = [persons_1,persons_2]

for person in people:
	print('\n')
	for detail, value in person.items():
		print(f'{detail}: {str(value).title()}')


fav_numbers ={
	'Guile':[1,2],
	'trixie':[3,4]
	}
for person, fav_number in fav_numbers.items():
	print(f'{person.title()} favorate number is/are:')
	for number in fav_number:
		print(number)