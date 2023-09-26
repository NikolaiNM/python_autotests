import requests

#Переменные
token = "bd60660e4ae4a2e3618ff1850af1670e"
host = "https://api.pokemonbattle.me:9104"


#Создать покемона 
create_poke = requests.post(f"{host}/pokemons", json = {
    "name": "Bulbazar",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(create_poke.text)


#Смена имени покемона
change_poke = requests.put(f"{host}/pokemons", json = {
    "pokemon_id": "11243",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(change_poke.text)


#Поймать покемона в покебол
catch_poke = requests.post(f"{host}/trainers/add_pokeball", json = {
    "pokemon_id": "11244"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(catch_poke.text)


#Убить покемона
kill_poke = requests.post(f"{host}/pokemons/kill", json ={
    "pokemon_id": "11244"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(kill_poke.text)