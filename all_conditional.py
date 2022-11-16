usernames = ['admin', 'anna', 'bea', 'bryan', 'clare']
new_users = ['charles', 'Anna']

if new_users:
	for new_user in new_users:
		if new_user.lower() in usernames:
			print("username already exist, try to create another one")
		else:
			print('you username is now created')
			usernames.append(new_user)

if usernames:
	for username in usernames:
		if username == 'admin':
			print(f'Hello {username.title()}, would you like to see a status report')
		else:
			print(f'Hello {username.title()}, thank you for logging in again')
else:
	print('we need more user')


ordinal_number = list(range(1,10))
for number in ordinal_number:
	if number == 1:
		print(f'{number}st')
	elif number == 2:
		print(f'{number}nd')
	else:
		print(f'{number}th')
