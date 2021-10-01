import requests

artist = str(input('What is the artist of the song: '))
title = str(input('What is the title of the song: '))


r = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')
r = r.json()


if "lyrics" in r:
    print(r['lyrics'])
else:
    print('error, try again')

