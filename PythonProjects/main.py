import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'token'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name":"pytest",
    "photo_id":-1
}

body_new_name = {
    "pokemon_id": "46034",
    "name": "New Name",
    "photo_id": 2
}

body_add = {
    "pokemon_id": "46034"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(response_change_name.text)'''

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)