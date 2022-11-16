availabe_toppings = ['chesses','mushroom']
request_toppings = ['mushroom', 'pineapple']

if request_toppings: #it is false if the list is empty
	for request_topping in request_toppings:
		if request_topping in availabe_toppings:
			print(f'adding {request_topping}')
		else:
			print(request_topping,'toppings not availabe')
	print('finish making your pizza')
else:
	print('are you sure you want a plain pizza')