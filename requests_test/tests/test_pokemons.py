import requests
import pytest

token = "0a8bd85fec6204cb14e5118fe3a188a4"
host = "https://api.pokemonbattle.me:9104"

#Проверка статуса ответа 200 на запрос конкретного тернера 2316
def test_status_code():
  response = requests.get(f"{host}/trainers", params={'trainer_id': 2654})
  assert response.status_code == 200

#Обновление информации по тренеру (имя и город) и проверка сообщения  ифнормация обновлена
def test_part_of_body():
  response = requests.put(f"{host}/trainers", 
                          headers={"trainer_token" : token}, 
                          json={
                            'name':'Test',
                            'city':'Belgrade'
                          })
  assert response.json()["message"] == 'Информация о тренере обновлена'


#Фикстура
@pytest.mark.parametrize("key, value", [("trainer_name", "Test"), 
                                        ("id", "2316"), 
                                        ("city", "Belgrade") ])

def test_response_json(key, value):
  response = requests.get(f'{host}/trainers', params={"trainer_id": 2316})
  assert response.json()[key] == value
