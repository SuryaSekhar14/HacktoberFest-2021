import requests

if str(input('Do you want to read a joke? y/n: ')) == "y":
    print("I'm thinking...")
    r = requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,explicit&type=twopart')
    r = r.json()
    print('-----------')
    print(r["setup"], '\n')
    print(r["delivery"])
    print('-----------', '\n')
