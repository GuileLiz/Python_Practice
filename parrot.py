prompt = "\nTellme something and I will returned it to you:"
prompt += '\nEnter Quit to end the prorgram\n'
message = ''

while message != 'quit':
	message = input(prompt)
	print(message) 

#alternative
active = True; #flag
while active:
	message = input(prompt)

	if message == 'quit':
		active = False; #flag
	else:
		print(message)

#alternative
active = True; #flag
while active:
	message = input(prompt)

	if message == 'quit':
		break
	else:
		print(message)