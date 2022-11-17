alien_colors = ['yellow', 'red' , 'green']
if alien_colors[2] == 'green':
	print('you earned 5 points')
if alien_colors[0] != 'green':
	print('you earned 10 points','\n')

if alien_colors[2] != 'green':
	print('you earned 5 points')
else:
	print('you earned 10 points')

print('\n')
alien_color = alien_colors[2]
if alien_color == 'green':
	score = 5
elif alien_color == 'red':
	score = 10
else:
	score = 15
print(f"'you earned a {score} points")

print('\n')
age = 65
if age < 2:
	print('baby')
elif age < 4:
	print('toddler')
elif age < 13:
	print('kid')
elif age < 20:
	print('teenager')
elif age < 65:
	print('adult')
else:
	print('elder')


fav_fruit = ['apple','banana']
if 'banana' in fav_fruit:
	print(f'i love {fav_fruit[1]}')
if 'apple' in fav_fruit:
	print(f'i love {fav_fruit[0]}')