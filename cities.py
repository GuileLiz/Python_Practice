def describe_city(name_city,name_country='Philippines'):
	"""Diplay the information about cities"""
	print(f"{name_city.title()} is in {name_country.title()}")

describe_city('bohol','Philippines')
describe_city('bohol')
describe_city(name_city='bohol',name_country='Philippines')