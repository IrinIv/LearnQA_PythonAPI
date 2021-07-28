import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
first_response = response.history[0]
print(first_response.url)
second_response = response.history[1]
print(second_response.url)
third_response = response.history[2]
print(third_response.url)

