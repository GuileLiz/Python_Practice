def make_album(name,album,number_of_song=[]):
	"""Dictionary discribe a music album"""
	if number_of_song:
		album = {'name':name, 'album':album,'number of song':number_of_song}
	else:
		album = {'name':name, 'album':album}
	return album

active = True
while active:
	message = input('type quit to exit, press Enter to continue\n')
	
	
	if message == 'quit':
		active = False
	else:
		name_input = input('Enter the name of the artist: ')
		album_input = input('Enter the album of the artist: ')
		song_input = input('Enter the number of the songs in album: ')
		album1=make_album(name_input,album_input,song_input)
		print(album1)
	
	