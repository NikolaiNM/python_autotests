import requests


#Переменные
token = "0a8bd85fec6204cb14e5118fe3a188a4"
host = "https://api.pokemonbattle.me:9104"


#Создать покемона 
create_poke = requests.post(f"{host}/pokemons", json = {
    "name": "Bulbazar",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})
pokek = create_poke.json()["id"]
print(create_poke.text)


#Смена имени покемона
change_poke = requests.put(f"{host}/pokemons", json = {
    "pokemon_id": pokek,
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(change_poke.text)


#Поймать покемона в покебол
catch_poke = requests.post(f"{host}/trainers/add_pokeball", json = {
    "pokemon_id": pokek
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(catch_poke.text)


#Убить покемона
kill_poke = requests.post(f"{host}/pokemons/kill", json ={
    "pokemon_id": pokek
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(kill_poke.text)
