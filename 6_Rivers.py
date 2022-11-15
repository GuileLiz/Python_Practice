rivers = {
	'anggat':'bulacan',
	'pasig river':'pasig',
	'nile':'egyp'
	}
for key, value in rivers.items():
	print(f'{key.title()} runs through {value.title()}')

survey_fav_progtamming_language = {
	'Ana':'pthon',
	'Bea':'C++',
	'Clare':'Java'
	}
language = {
	'Guile':'python',
	'Ana':'pthon',
	}
print('\n')
for key in language.keys():
	if key in survey_fav_progtamming_language:
		print(f'{key}, Thank you for participating ')
	else:
		print(f'{key},I invite you participate')