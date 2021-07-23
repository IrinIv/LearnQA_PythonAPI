import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text)